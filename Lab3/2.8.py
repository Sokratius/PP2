def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

user_input = input()
numbers = list(map(int, user_input.split()))

result = spy_game(numbers)
print(result)