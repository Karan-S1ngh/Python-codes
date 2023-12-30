# WAP to make a folder and place multiple files, each file having a table of one number each

a = int(input("Enter the first number from where you want multiplication table : "))

b = int(input("Enter the last number till where you want multiplication table : "))

c = int(input("Enter the number till which u want each number's table : "))


for i in range(a, b):
    with open(f"Tables/Multiplication table of {i}",'w') as f:
        for j in range(1, c+1):
            f.write(f"{i} x {j} = {i*j}\n")
            

print("Folder generated")
            

