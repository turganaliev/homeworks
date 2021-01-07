to_do = []
done = []
while True:
    print("1) Dobavit delo: ")
    print("2) Otmetit delo: ")
    option = int(input("Vyberite variant: "))
    if option == 1:
        delo = input("Vvedite nazvaniye dela: ")
        to_do.append(delo)

    if option == 2:
         num = int(input("Vvedite index dela: "))
         done.append(num)

    print(to_do)
    print(done)
