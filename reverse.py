#python program to reverse a number

# number = int (input("enter the number"))
# reverse = 0
# while number > 0:
#     remainder= number%10
#     reverse= (reverse*10)+remainder
#     number= number//10
# print(reverse)




# to find the length of a string


# string= input("enter the string: ")
# count = 0

# for i in string:
 
#     count=count+1
# print("the length of the string you have entered is ",count)



#to search for the keyword in the string


# def search(string, keyword):
#     if keyword in string:
#         return "Search successful"
#     else:
#         return "Search unsuccessful"

# string = input("Enter the main string: ")
# keyword = input("Enter the keyword/substring to search for: ")

# result = search(string, keyword)
# print(result)



#string compariison

# def compare_strings(str1, str2):
#     if str1 == str2:
#         return 0
#     else:
#         return -1

# # Input from the user
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# # Compare the strings and display the result
# result = compare_strings(string1, string2)
# if result == 0:
#     print("Strings are equal")
# else:
#     print("Strings are not equal")

# print("the type of string is ", type(string1))



# python code for 1's count in binary

# def binarycount(number):
#     count =0
#     while number>0:
#         if number%2==1:
#             count= count+1
#         number = number//2
#     return count

# number= int(input("enter the number: "))
# if number<0:
#     print("enter a non negative number")
# else:
#     result= binarycount(number)
#     print("the number 1's binary counts are ", result)

# for i in number:
#     a[i]= number%2
#     number= number/2



# python code to find the index of an array

# def index(arr, size, value):
#     for i in range(size):
#         if arr[i] == value:
#             return i
#     return -1


# array = []
# size = int(input("Enter the size of the array: "))
    
# for i in range(size):
#     element = int(input(f"Enter element {i+1}: "))
#     array.append(element)
    
# print("Your entered array is:", end=" ")
# for element in array:
#     print(element, end=" ")

# size = len(array)

# value = int(input("\nEnter the value to search: "))
    
# index_found = index(array, size, value)

# if index_found == -1:
#     print("Element not found.")
# else:
#     print(f"Element found at index: {index_found}")



#  python code to expand the string

# string = input("Enter the string: ")
# print(f"Your entered string is {string}")

# if string[0] == '-':
#     for ch in range(ord(string[1]), ord(string[3]) + 1):
#         print(chr(ch), end="")
# else:
#     length = len(string)
#     print(f"The length of the string is {length}")
    
#     if length > 5:
#         for ch in range(ord(string[0]), ord(string[2]) + 1):
#             print(chr(ch), end="")
        
#         for i in range(ord(string[3]), ord(string[5]) + 1):
#             print(chr(i), end="")
#     else:
#         for ch in range(ord(string[0]), ord(string[2]) + 1):
#             print(chr(ch), end="")






