'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Difficulty : easy

'''

def reverse_digits(number):
    flag = 1
    if (number < 0):
        number = -number
        flag = -1

    reverse_number = 0
    while (number != 0):
        digit = number % 10
        number = (number/10)
        reverse_number = reverse_number * 10 + digit

    return reverse_number * flag;

if __name__ == '__main__':
    print (reverse_digits(1))
    print (reverse_digits(123456789))
    print (reverse_digits(-1))
    print (reverse_digits(-1234))

