row=int(input("Enter the row value"))
ascii=65
for i in range(0,row):
    for j in range(0,i+1):
        char=chr(ascii)
        print(char, end='')
        ascii+=1
    print('')
