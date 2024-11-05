




# program2.py

# Prompting user for input
#Naming convention: Snake Case (snake_case) is used for readability, with underscores separating words.
#Assignment operator "=" assigns the converted integer value to the variable.
#input(x) function: Collects user input as a string.
# Quotation Marks (' or ")
#  	Definition: Used to define string literals. Strings can be enclosed in single quotes (') or double quotes ("), allowing flexibility in string representation.
first_name = input("Enter the author's first name: ")
last_name = input("Enter the author's last name: ")
title = input("Enter the book title: ")
isbn = input("Enter the ISBN: ")


# Print an empty line
# print(*objects, sep=' ', end='\n', file=sys.stdout) Prints objects to the console or another file. Parameters in parentheses are not shown in the line of program, \
# but are functional.
print()


# Print the table header
# print(*objects, sep=' ', end='\n', file=sys.stdout) Prints objects to the console or another file. Parameters in parentheses are not shown in the line of program.
# F-strings (formatted string literals) are not technically functions; they are a convenient, built-in syntax feature for string formatting in Python.\
#    They are also often more efficient since expressions inside {} are evaluated directly at runtime, eliminating the need to call a separate formatting function.
# Format specifiers are use in f-strings, str.format(), and printf-style formatting. These specifiers help control the alignment, width, padding, precision, and type of data displayed. This program is using left and right alignment format specifiers.
#     f"{'text':<10}"  # 'text      '
#     f"{'text':>10}"  # '      text'
print(f"{'Author':<30}{'Title':<30}{'ISBN':>10}")
print(f"{'_' * 30}{'_' * 30}{'_' * 10}")


# Format and print the data row
# Assignment operator "=" assigns the converted integer value to the variable.
# F-strings (formatted string literals) are not technically functions; they are a convenient, built-in syntax feature for string formatting in Python.\
#    They are also often more efficient since expressions inside {} are evaluated directly at runtime, eliminating the need to call a separate formatting function.
# Format specifiers are use in f-strings, str.format(), and printf-style formatting. These specifiers help control the alignment, width, padding, precision, and type of data displayed. This program is using left and right alignment format specifiers.
#     f"{'text':<10}"  # 'text      '
#     f"{'text':>10}"  # '      text'
author = f"{last_name}, {first_name}"
print(f"{author:<30}{title:<30}{isbn:>10}")
