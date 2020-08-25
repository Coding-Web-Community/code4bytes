#!/usr/bin/env elixir

[s, t] = System.argv()

s = s
  |> String.to_charlist()
  |> Enum.group_by(& &1)
t = t
  |> String.to_charlist()
  |> Enum.group_by(& &1)

IO.puts(s == t)
