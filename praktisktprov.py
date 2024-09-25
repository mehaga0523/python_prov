#author: mehmet ali agac
#date 2023 09 25



calculate = (input("enter number:"))
calculate = calculate.split()

for b in range (len(calculate)):
 print(" ")
 print(calculate[b])
 for i in range (1,11):
    calculated_number = (float(calculate[b]) * i)
    
    print(calculated_number)
