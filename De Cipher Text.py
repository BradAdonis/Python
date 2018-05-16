code = input("Please enter the coded text")
distance = int(input("Please enter the distance value"))
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if(cipherValue < ord('a')):
        cipherValue = ord('z') - (distance - (ord('a') - ordValue + 1))
    plainText += chr(cipherValue)
print(plainText)
