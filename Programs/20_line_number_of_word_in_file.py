# WAP to check at which line given word is present 

word = input("Enter the word of which you want to find line number : ")

with open("Files\Line_number_program.txt") as f:
    content = f.readlines()

found = False
line_numbers = []
for i in range(len(content)):
    if word in content[i]:
        found = True
        line_numbers.append(i+1)
        # i+1 because index starts from 0
        # but line number starts from 1

if found:
    print(f"'{word}' is present in line number(s): {line_numbers}")
else:
    print(f"'{word}' not found in file")
        
  

 
'''OUTPUT
Enter the word of which you want to find line number : is
'is' is present in line number(s): [1, 6]

Enter the word of which you want to find line number : how are you
'how are you' is present in line number(s): [5]

Enter the word of which you want to find line number : rainy
'rainy' not found in file
'''   
  