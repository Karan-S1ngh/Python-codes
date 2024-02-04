a = input("Enter First String : ")
b = input("Enter Second String : ")

print("1. Concatenation :",a+b)
print("2. Reversal :","String 1 = ",a[::-1],", String 2 =",b[::-1])
print("3. Slicing Till 3rd Character:","String 1 = ",a[0:3],", String 2 = ",b[0:3])
print("4. Length :","String 1 = ",len(a),", String 2 = ",len(b))
if a==b: n = "Both Strings are equal" 
else: n ="Both Strings are not equal"
print("5. Comparison :", n)
print("6. 3 times Repetition :","String 1 = ",a*3,", String 2 = ",b*3)
print("7. Finding count of 'a' in both strings :","String 1 = ",a.count('a'),", String 2 = ",b.count('a'))
print("8. Replacing 'a' with 'b' in both strings :","String 1 = ",a.replace('a','b'),", String 2 = ",b.replace('a','b'))
print("9. Capitalizing both strings :","String 1 = ",a.capitalize(),", String 2 = ",b.capitalize())




'''OUTPUT
Enter First String : Suresh
Enter Second String : Ramesh
1. Concatenation : SureshRamesh
2. Reversal : String 1 =  hseruS , String 2 = hsemaR
3. Slicing Till 3rd Character: String 1 =  Sur , String 2 =  Ram
4. Length : String 1 =  6 , String 2 =  6
5. Comparison : Both Strings are not equal
6. 3 times Repetition : String 1 =  SureshSureshSuresh , String 2 =  RameshRameshRamesh
7. Finding count of 'a' in both strings : String 1 =  0 , String 2 =  1
8. Replacing 'a' with 'b' in both strings : String 1 =  Suresh , String 2 =  Rbmesh
9. Capitalizing both strings : String 1 =  Suresh , String 2 =  Ramesh
'''
