# Python Program - Convert Hexadecimal to Binary

print("Enter 'x' for exit.");
hexdec = input("Enter any number in Hexadecimal Format: ");
if hexdec == 'x':
    exit();
else:
    dec = int(hexdec, 16);
    print(hexdec,"in Binary =",bin(dec));