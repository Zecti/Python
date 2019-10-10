def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def divide (x,y):
    return x/y
print ("Kalkulator")
ulang = True
while ulang:
    print ("Pilih Operasi")
    print ("1. Jumlah")
    print ("2. Kurang")
    print ("3. Bagi")
    tanya = True
    
    while tanya:
        choice = input ("Masukkan pilihan (1 / 2 / 3):")

        num1 = int (input ("Masukkan bilangan pertama: "))
        num2 = int (input ("Masukkan bilangan kedua: "))

        if choice == '1':
            print (num1,"+",num2,"=", add(num1,num2))
            tanya = False
        elif choice == '2':
            print (num1,"-",num2,"=", subtract(num1,num2))
            tanya = False
        elif choice == '3':
            print (num1,"/",num2,"=", divide(num1,num2))
            tanya = False
        else:
            print ("Input Salah")
            tanya = True
            
