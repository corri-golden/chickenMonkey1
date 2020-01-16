# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
for i in range(1,101):
    if i % 5 == 0 and i % 7 == 0:
        print('ChickenMonkey')   
    elif i % 5 == 0:
        print('Chicken')
    elif i % 7 == 0:
        print('Monkey')
    else:
        print(i)

    

  