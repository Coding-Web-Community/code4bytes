#!/usr/bin/env elixir

defmodule Mix.Tasks.C4b15 do
  use Mix.Task
  require Logger

  def decode_hex(word) do
    word |> decode_hex_impl()
  end

  def decode_hex_impl(word, acc \\ 0)
  def decode_hex_impl("", acc), do: acc
  def decode_hex_impl(_, :error), do: :error
  
  def decode_hex_impl(<<thing::size(8), rest::binary >>, acc) do
    <<zero::size(8), nine::size(8), a::size(8), f::size(8), biga::size(8), bigf::size(8)>> = "09afAF"
    ret = case thing do
      num when num in zero..nine -> num - zero
      small when small in a..f -> small - a + 10
      big when big in biga..bigf -> big - biga + 10
      _ -> :error
    end
    if ret == :error do
      decode_hex_impl(rest, :error)
    else
      decode_hex_impl(rest, ret + acc * 16)
    end
  end

  # Usage mix c4b15 tests.json
  def run(file) do
    File.read!(file)
    |> Jason.decode!()
    |> Enum.map(fn json ->
      hex = json["input"] |> decode_hex()
      map = %{"input" => json["input"],
        "result" => if hex == :error do 0 else hex end,
        "fails" => hex == :error}
      if map == json do
        Logger.info("OK: #{inspect(map)}")
      else
        Logger.error(inspect(map))
        Logger.debug("SHOULD BE #{inspect(json)}")
      end
    end)
  end

end

