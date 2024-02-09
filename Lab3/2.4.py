def filter_prime(numbers):
    is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    return list(filter(lambda x: is_prime(x), numbers))

input_numbers = input("Enter the numbers: ").split()
numbers = [int(num) for num in input_numbers]

prime_numbers = filter_prime(numbers)

print("Prime numbers: ", prime_numbers)