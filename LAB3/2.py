def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)  # dzielenie i floorowanie liczby jeśli jest większa / równa 1
        print(num % 2, end='')


print('Podaj liczbe dziesietna: ')
num = int(input())
if num >= 1:
    DecimalToBinary(num)
elif num == 0:
    print(0)
else:
    print('Podaj liczbe większa, lub równą 0')
