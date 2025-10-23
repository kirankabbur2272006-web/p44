# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_count = 0
odd_count = 0
prime_count=0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if is_prime(num):
        prime_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Prime numbers:", prime_count)
