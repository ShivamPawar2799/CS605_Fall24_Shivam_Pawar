# Simple Calculator 

## Overview

The Simple Calculator is a console-based application written in Python that performs basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.

This README provides instructions on how to use the calculator and an explanation of its code.

## Features

- Performs arithmetic operations: Addition, Subtraction, Multiplication, and Division.
- Text highlighted with colors for better User Interface.
- User friendly prompts and formatted results.


## Code Explanation
# Colored Text 
The calculator uses ANSI escape codes to apply colors to the text output. These codes are included as string constants at the beginning of the code.
These codes are used in the print_menu() function and throughout the program to enhance the readability of the output.

# Operator Symbols
The program uses a get_operator() function to determine the correct operator symbol based on the user's choice.
This function maps user choices to their corresponding arithmetic operators and is used to format the result string.

# Floating Point Arithmetic
Results are displayed as floating point numbers to accommodate fractional values.
This ensures that results like 10/3 are shown as 3.333333.... rather than rounding to the nearest integer.

## Text Prompts and User Interaction
# Prompts
The Calculator uses clear text prompts to guide user input. These prompts ensure that the user knows what information is needed for each operation.

# Error Handling
The program handles invalid input and provides error messages. 
For example: 
-if you enter non numeric values or invalid choices, the calculator will display an error messages.
-if you attempt to divide by zero, the calculator will display: Division by zero is not allowed.

# Exit Option
To exit, either type no when prompted to perform another calculation or select the 5 option from the menu.

## Steps to use the Calculator
# Step 1: View the Main Menu
Upon running the program, you will see the menu options:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

# Step 2: Choose an Operation
Enter the number corresponding to the desired operation (e.g.,4 for Divide) and press Enter.

# Step 3: Enter Numbers
The Calculator will prompt to enter the first and the second number to perform the operations.

# Step 4: Result Display
The Calculator will display the result. The output will include the number, operator used, and the result of the calculation.

# Step 5: Perform Another Calculation
Repeat or Exit: After displaying the result, the calculator will prompt:
-Type yes and press Enter to perform another calculation.
-Type no and press Enter to exit the calculator.





