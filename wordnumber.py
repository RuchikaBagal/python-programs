
#//Write a python program that displays given number in string format. e.g., 10 -> ten 100 -> hundred 5270 -> five thousand two hundred seventy

a = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
b = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
c = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
d = ["hundred", "thousand"]

number = int(input("Enter the number: "))

if 0 < number < 10:
    print(a[number])
elif 10 < number <= 19:
    x = number % 10
    print(b[x])
elif 100 < number < 1000:
    x = number % 100
    y = number // 100
    print(a[y], d[0], end=" ")
    if x != 0:
        if x < 10:
            print("and", a[x])
        elif 10 <= x <= 19:
            print("and", b[x - 10])
        else:
            print("and", c[x // 10], a[x % 10])
elif 10 < number < 100:
    print(c[number // 10], a[number % 10])
elif 1000 < number < 10000:
    x = number % 1000
    z = number // 10
    y = x // 10
    if z % 100 == 0:
        print(a[number // 1000], d[1], a[x % 10])
    else:
        print(a[number // 1000], d[1], a[x // 100], d[0], c[y % 10], a[x % 10])
else:
    print("zero")
