defmodule Mix.Tasks.C4b14 do
  use Mix.Task
  require Logger
  # Usage: mix c4b14 <file>
  @format ~r/(?<start_time>.*) - (?<end_time>.*) \| (?<tag>\w+)/
  def run(args) do
    data = File.stream!(args)
    |> Stream.map(&Regex.named_captures(@format, &1))
    |> Stream.map(& %{&1 | "end_time" => Timex.parse!(&1["end_time"], "%F %T", :strftime), "start_time" => Timex.parse!(&1["start_time"], "%F %T", :strftime)})
    |> Stream.map(&Map.put(&1, :delta, Timex.diff(&1["end_time"], &1["start_time"], :seconds)))
    |> Enum.into([])
  
    avg = Enum.reduce(data, 0, fn x,acc -> x.delta + acc end)/Enum.count(data)

    IO.puts("shortest time delta:  #{Enum.min_by(data, & &1.delta)["tag"]}")
    IO.puts("longest time delta:  #{Enum.max_by(data, & &1.delta)["tag"]}")
    IO.puts("code closest to average time delta:  #{Enum.min_by(data, &abs(avg - &1.delta))["tag"]}")

  end
end
