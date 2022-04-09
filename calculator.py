
#Rıza Doğukan Koşar 19253509

def add(a, b):
    return a + b

def divide(a, b):
    return a / b

print("Lütfen yapmak istediğiniz işlemi seçin \n" ,
        "1. Toplama\n" ,        
        "2. Bölme")
    
operation = int(input("İşlem numarasını seçin:"))
number1 = int(input("İlk sayınızı girin: "))
number2 = int(input("ikinci sayınızı girin: "))

if operation == 1:
    print(number1, "+", number2, "=",
                    add(number1, number2))
  
elif operation == 2:
    print(number1, "/", number2, "=",
                    divide(number1, number2))
else:
    print("Geçersiz bir işlem değeri girdiniz")