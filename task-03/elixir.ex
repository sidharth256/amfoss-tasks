IO.puts("Enter a number (n): ")
n_str = IO.gets("") |> String.trim()
n = String.to_integer(n_str)

IO.puts("Prime numbers up to #{n}:")
1..n
|> Enum.filter(fn x ->
  x == 2 || (x > 2 && rem(x, 2) != 0 && !Enum.any?(2..div(x, 2), fn y -> rem(x, y) == 0 end))
end)
|> IO.inspect()

