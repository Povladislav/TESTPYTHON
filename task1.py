#VIVOD POSLEDNIX 4 CIFR,OSTALNOE ZVEZDI
num = input('Введите номер из 16 цифр ')
def password(num):
    num2 = num[12:17]
    return f'************{num2}'
print(password(num))



