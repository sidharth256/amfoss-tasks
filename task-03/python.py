num = int(input("Enter a number : "))
if num < 2:
    print("There are no prime numbers upto", num)
else:
    print("Prime numbers upto", num, "are : ")
    for num in range(2, num + 1):
        is_prime = True
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(num)
