def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0



n = int(input("Enter a number: "))

result = is_power_of_two(n)
print(result)
