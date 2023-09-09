const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter a number (n): ", (n) => {
  n = parseInt(n);
  if (n < 2){
  console.log('There are no prime numbers less than 2')
  }else {console.log(`Prime numbers up to ${n}:`)}
  
  
  
  for (let i = 2; i <= n; i++) {
    let isPrime = true;
    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      console.log(i);
    }
  }

  rl.close();
});

