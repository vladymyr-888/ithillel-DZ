number = int(input('Enter number'))
while number > 9:
     product = 1
     for numbers in str(number):
         product *= int(numbers)
     number = product
print(number)