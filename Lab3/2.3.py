#x + y = 35
#2x + 4y = 94
#x = 35 - y
#2(35-y) + 4y = 94
#2*35-2*y + 4y = 94
#2rabbits = numlegs - 2numheads
#rabbits = (numlegs-2numheads)/2
#y = 12
#x = 23


def solve(num_heads, num_legs):
    rabbits = (num_legs - 2*num_heads)/2
    chickens = num_heads - rabbits
    print("Number of the rabbits: " + str(rabbits) + '\b\b\n' + "Number of the chickens: " + str(chickens) + '\b\b')


solve(int(input("Enter the number of heads: ")), int(input("Enter the number of legs: ")))