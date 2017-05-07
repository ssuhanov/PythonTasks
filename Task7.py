userInput = input("Enter numbers with spacing please: ")
strNumbers = userInput.split()
numbers = [int(x) for x in strNumbers]

evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))

print("odds count: ", len(odds))
print("evens count: ", len(evens))
