use std::io;

fn main() {
    let mut input = String::new();

    println!("Enter a number (n):");

    io::stdin().read_line(&mut input).expect("Failed to read line");

    let n: u32 = input.trim().parse().expect("Invalid input. Please enter a valid number.");
    
    if n<2 {
        println!("There are no prime numbers below 2")
    } else {
    println!("Prime numbers up to {}:", n);
    }
    for num in 2..=n {
        let mut is_prime = true;
        for i in 2..num {
            if num % i == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            print!("{} ", num);
        }
    }

    println!();
}

