from itertools import permutations

def print_permutations(string):
    permutations_list = permutations(string)
    for permutation in permutations_list:
        print(''.join(permutation))

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print_permutations(user_input)