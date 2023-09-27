main :: IO ()
main = do
    putStr "Enter a number (n): "
    input <- getLine
    let n = read input :: Int
    if n<2
    then putStrLn "There are no prime numbers below 2"
    else do
    putStrLn $ "Prime numbers up to " ++ show n ++ ":"
    printPrimes 2 n

printPrimes :: Int -> Int -> IO ()
printPrimes current n
    | current > n = return ()
    | isPrime current = do
        putStr $ show current ++ " "
        printPrimes (current + 1) n
    | otherwise = printPrimes (current + 1) n

isPrime :: Int -> Bool
isPrime 2 = True
isPrime n
    | n <= 1 = False
    | otherwise = not $ any (\x -> n `mod` x == 0) [2..isqrt n]

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral
