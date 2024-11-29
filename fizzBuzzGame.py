x = int(input("Enter a number: "))
for n in range( 1 , x + 1 ):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    