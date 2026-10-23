from binascii import a2b_base64
from zlib import adler32

pincode = int(input())
if pincode < 1000 or pincode > 9999:
    print('ERROR')
elif 1900 <= pincode <= 2050:
    print('ERROR')
else:
    a1 = pincode // 1000
    a2 = (pincode - a1*1000)//100
    a3 = (pincode - a1*1000 -  a2*100)//10
    a4 = pincode%10
    if a1 != a2 and a1 != a3 and a1 != a4 and a2 != a3 and a2 != a4 and a3 != a4:
        print('OK')
    else:
        print('ERROR')