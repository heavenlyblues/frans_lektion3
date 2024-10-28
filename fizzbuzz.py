# Using if elif statements
for n in range(1, 101):
    if n % 3 != 0 and n % 5 != 0:
        print(f"{n}")
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")

# Using string concantenation              
for n in range(1, 101):
    output = ""
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    print(output or n)


for n in range(1, 101):
    result = (
        "FizzBuzz" if n % 15 == 0 else
        "Fizz" if n % 3 == 0 else
        "Buzz" if n % 5 == 0 else
        str(n)
    )
    print(result)