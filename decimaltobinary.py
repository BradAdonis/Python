decimal = int(input("Please enter a decimal value : "))
if decimal == 0:
    print(0)
else:
    print("Quotient remainder binary")
    bstring = ""
    while decimal > 0:
        remainder =  decimal % 2
        decimal = decimal // 2
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (decimal,remainder,bstring))
    print("The binary representation is",bstring)

    
