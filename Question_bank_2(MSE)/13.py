# Calculate sum and average of strings and display it


# Input a string
input_string = input("Enter a string: ")

# Split the string into words and calculate sum and average
words = input_string.split()
total_length = sum(map(len, words))
average_length = total_length / len(input_string) if total_length > 0 else 0

# Display results
print("Sum of lengths of all words:", total_length)
print("Average length of words:", average_length)




'''OUTPUT
Enter a string: hiii
Sum of lengths of all words: 4
Average length of words: 1.0

Enter a string: Hello how are u
Sum of lengths of all words: 12
Average length of words: 0.8
'''
