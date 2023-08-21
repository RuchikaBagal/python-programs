#string compariison

from function import compare_strings

# Input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Compare the strings and display the result
result = compare_strings(string1, string2)
if result == 0:
    print("Strings are equal")
else:
    print("Strings are not equal")

print("the type of string is ", type(string1))