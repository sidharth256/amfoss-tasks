package main

import "fmt"

func main() {
    var n int
    fmt.Print("Enter a number (n): ")
    fmt.Scan(&n)
    
    if (n<2) {
        fmt.Print("There are no prime numbers below 2")
    } else {
        fmt.Printf("Prime numbers up to %d: ", n)
    }

    for i := 2; i <= n; i++ {
        isPrime := true
        for j := 2; j*j <= i; j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        if isPrime {
            fmt.Printf("%d ", i)
        }
    }

    fmt.Println()
}

