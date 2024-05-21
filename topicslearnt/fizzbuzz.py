# 3-->fizz,  5--> buzz,  15-->fizzbuzz

for number in range(1, 101):
    if number % 3 == 0:  # divisible by 3
        print("Fizz")
    elif number % 5 == 0:  # divisible by 5
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:  # divisible by 3and5 both
        print("FizzBuzz")
    else:
        print(number)
