#Task 1: Length string
print("Task 1:Length of a string")
a = "Hello, World!"

#display string
print("String:",a)

#results
print("Length of the string:",len(a))

#Task 2: Numbers of character
print("\nTask 2:Numbers of character in a string")

#display string
x = 'Memento Mori'
print("String:",x)

#results
print("Numbers of characters in a string:" , len((x)))


#Task 3: changed to $
print("\nTask 3: first char have been changed to '$'")
e = "test String"

#display string
print("String:", e)
f = e[0]
for char in e[1:]:
    if char == e[0]:
        f+="$"
    else:
        f+=char
#results
print("Output:",f)


#Task 4: swaping characters
print("\nTask 4: Swap the first two characters")

#display two strings
print("str1 = abc")
print("str2 = xyz")
def swap_characters_and_combine(str1, str2):

   swapped_str1 = str2[:2] + str1[2:]

   swapped_str2 = str1[:2] + str2[2:]

   

   return swapped_str1 + " " + swapped_str2

# Test the function with two strings

#results
print("Output:",swap_characters_and_combine("abc", "xyz"))

# Task 5: concatenated four strings
print("\nTask 5: Concatenate four strings with spaces")

#define variables
a = "str1 = Memento"
b = "str2 = mori"
c = "str3 = Memento"
d = "str4 = Vivere"

#display strings
print(a)
print(b)
print(c)
print(d)

concatenated_string = a + " " + b + " " + c + " " + d

#results
print("Concatenated string:", concatenated_string)

#Task 6: Name and age in a paragraph
print("\nTask 6: Name and age in a paragraph")

# Define variables
name = "Kitt"
age = 22

#display variables
print("name =",name)
print("age =", age)

# Create a paragraph using concatenation
paragraph = "Hello, my name is " + name + " and I am " + str(age) + " years old."

# Display the paragraph
print("Concatenated Paragraph:",paragraph)

#Task 7: String from the user
print("\nTask 7: Two strings from the user and concatenate them")

# Get two strings from user input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Concatenate the strings
concatenated_string = string1 + " " + string2  # Adding a space between the strings

# Display the concatenated string
print("Concatenated String:", concatenated_string)
