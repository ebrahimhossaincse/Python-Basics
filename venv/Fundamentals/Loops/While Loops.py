print('Example 1: Simple while loop')
count = 0
while count < 5:
    print("Count:", count)
    count += 1

print('\nExample 2: Using while loop for user input validation')
while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) >= 18:
        print("You are eligible to vote.")
        break
    else:
        print("Invalid input. Please enter a valid age.")

print('\nExample 3: Using while loop with else block')
num = 10
while num > 0:
    print("Number:", num)
    num -= 1
else:
    print("Loop completed successfully")

print('\nExample 4: Using while loop with break statement')
num = 10
while True:
    print("Number:", num)
    if num == 5:
        break
    num -= 1

print('\nExample 5: Using while loop with continue statement')
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print("Number:", num)

print('\nExample 6: Infinite loop with while True')
while True:
    print("This loop runs infinitely. Press Ctrl+C to exit.")
