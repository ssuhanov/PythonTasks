userInput = input("Please enter numbers: ")
strNumbers = userInput.split()
numbers = [int(x) for x in strNumbers]

if (len(numbers) < 3) or (numbers[-1] != numbers[0] * 2):
    print("Error")
elif len(numbers) % 2 == 0:
    print(str(numbers[int(len(numbers) / 2) - 1]) + " " + str(numbers[int(len(numbers) / 2)]))
else:
    print(numbers[int(len(numbers) / 2)])
