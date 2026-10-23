number = int(input())
thousands = number // 1000
hundreds = ( number - thousands * 1000 )//100
tens = ( number - thousands * 1000 - hundreds * 100 ) // 10
units =  number - thousands * 1000 - hundreds * 100 - tens * 10
if thousands == units and hundreds == tens:
    print ('настоящее')
else:
    print ('кривое')