import random
# friuts =["Apple","Mango","Orange"]
# for i in friuts:
#     print(i)
#     print(i+"pie")
#     total=0;
#     for number in range(1,101):
#         print(number)
#         total=total+number
#     print(total)
alphabets = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '-', '_', '=', '+',
        '[', ']', '{', '}',
        '\\', '|',
        ';', ':',
        "'", '"',
        ',', '.', '<', '>',
        '/', '?',
        '`', '~']

print("Welcme to the Password Generator")
nralphabets=int(input("enter the number of aplhabets: "))
nrnumbers=int(input("enter the number of numbers: "))
nrsymbols=int(input("enter the symbols: "))
password=""
for alpha in range(1,nralphabets+1):
    password+=random.choice(alphabets)

for number in range(1,nrnumbers+1):
    password+=random.choice(numbers)

for symbol in range(1,nrsymbols+1):
    password+=random.choice(symbols)

print(password)


