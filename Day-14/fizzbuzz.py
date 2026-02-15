def fizzBuzz(n):
    result = []

    if n <= 0:      # Edge case
        return result

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


# ---- Main Program ----
n = int(input("Enter a number: "))
output = fizzBuzz(n)

print(output)
