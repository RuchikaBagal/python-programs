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



# 1's count in binary

#include <stdio.h>
def binarycount(number):
    count =0
    while number>0:
        if number%2==1:
            count= count+1
        number = number//2
    return count

number= int(input("enter the number: "))
if number<0:
    print("enter a non negative number")
else:
    result= binarycount(number)
    print("the number 1's binary counts are ", result)




# int countOnesInBinary(int num) {
#     int count = 0;
#     while (num > 0) {
#         if (num % 2 == 1) {
#             count++;
#         }
#         num /= 2; // Divide by 2 to move to the next binary digit
#     }
#     return count;
# }

# int main() {
#     int num;

#     printf("Enter an integer: ");
#     scanf("%d", &num);

#     if (num < 0) {
#         printf("Please enter a non-negative integer.\n");
#     } else {
#         int onesCount = countOnesInBinary(num);
#         printf("Number of 1's in binary representation of %d is: %d\n", num, onesCount);
#     }

#     return 0;
# }





