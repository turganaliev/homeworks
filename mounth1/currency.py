import currancy_exchange

while 1:
    _from = input("Kakuyu valutu: ")
    _to = input("V kakuyu valutu: ")
    amount = int(input("Vvedite kolichestvo: "))

    exchange = currancy_exchange.exchange(_from, _to, amount, whole=True)
    print(exchange)
