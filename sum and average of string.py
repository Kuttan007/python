""" Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496" 
"""
#!/usr/bin python3
str1 = "PYnative29@#8496"
total = 0
cnt = 0
for char in str1:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)
