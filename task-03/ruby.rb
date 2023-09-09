puts "Enter a number"
number = gets.chomp.to_i

if (number < 2)
  puts "There are no prime number below 2"
  
  
else 
  puts "Prime numbers upto #{number} are"
  for num in 2..number+1
    prime = true
    
    if num > 1
      for i in 2..num - 1
        if num % i == 0
          prime = false
          break
        end
      end  
    end
    
    puts num if prime
  end
end  
