abc = input().lower()
letter = abc[0]
number = int(abc[1])
letter_num = ord(letter) - 96
summ = letter_num + number
if summ % 2 == 0:
    print('черный')
else:
    print('белый')