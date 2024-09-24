# Python file   : Praktikum 2 PIT
# author        : Reza Taqyuddin

# 1. Variable Declaration

variable1 = 10
variable2 = 10.5
variable3 = "Sepuluh"
variable4 = True

# 2. Operators -> +, -, *, /, %, =


# 3. Perulangan -> Looping
# for statement

i = 0
for i in range(5):
    for j in range (5):
      print("Aku Hebat")  
    print()

print("==========================")

i = 0
while i < 10 :
    i += 1
    print(1)
    
# While iteration -> Need Condi
baris2 = 0
tengah = 5
while baris2 < 5 :
    kolom2 = 0
    if(baris2 % 2 == 1) :
        while kolom2 < 5:
            if(kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5 :
            print("*",end="")
            kolom2 += 1
    print()
    baris2 += 1