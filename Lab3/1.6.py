is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

if __name__ == "__main__":
    number = int(input("Enter the number: "))

    if is_prime(number):
        print(f"{number} - prime")
    else:
        print(f"{number} - is not prime")