def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(money - expense))
    print("Centavos:")
    print(int((float(money-expense)-int(money-expense))*100))
