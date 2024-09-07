# Test Document for Calculator

## Test Cases

| **Test Case ID** | **Description**                           | **Input**                                                      | **Expected Output**                                 | **Observed Result**                               | **Status** |
|------------------|-------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------|------------|
| 1                | Adding Operation with Positive Integers| Operation: Adding (1)<br>First number: 8<br>Second number: 12 | Result: `8 + 12 = 20`                               | Result: `8 + 12 = 20`                            | Pass       |
| 2                | subtracting Operation with Positive Integers | Operation: subtracting (2)<br>First number: 15<br>Second number: 5 | Result: `15 - 5 = 10`                               | Result: `15 - 5 = 10`                            | Pass       |
| 3                | Multiplication Operation with Positive Integers | Operation: Multiplication (3)<br>First number: 7<br>Second number: 6 | Result: `7 * 6 = 42`                                | Result: `7 * 6 = 42`                             | Pass       |
| 4                | Dividing Operation with Positive Integers | Operation: Dividing (4)<br>First number: 20<br>Second number: 4  | Result: `20 / 4 = 5.0`                              | Result: `20 / 4 = 5.0`                           | Pass       |
| 5                | Dividing by Zero                          | Operation: Dividing (4)<br>First number: 10<br>Second number: 0  | Error Message: `Error: Dividing by zero is not allowed.` | Error Message: `Error: Dividing by zero is not allowed.` | Pass       |
| 6                | Invalid Operation Choice                  | Operation: Invalid choice (e.g., 6)                             | Error Message: `Invalid choice. Please select a number between 1 and 5.` | Error Message: `Invalid choice. Please select a number between 1 and 5.` | Pass       |
| 7                | Non-Numeric Input                         | Operation: Adding (1)<br>First number: `abc`<br>Second number: 5 | Error Message: `Invalid input. Please enter a number.` | Error Message: `Invalid input. Please enter a number.` | Pass       |
| 8                | Perform Multiple Calculations             | Perform Adding: 5 + 3<br>Perform subtracting: 12 - 7<br>Select `no` to exit | Result of Adding: `5 + 3 = 8`<br>Result of subtracting: `12 - 7 = 5`<br>Exit Message: `Exiting the calculator. Goodbye!` | Result of Adding: `5 + 3 = 8`<br>Result of subtracting: `12 - 7 = 5`<br>Exit Message: `Exiting the calculator. Goodbye!` | Pass       |

## Summary

All test cases have been executed successfully. The Simple Calculator application handles basic arithmetic operations, error scenarios such as Dividing by zero, and invalid inputs effectively. It also supports multiple calculations in a single session and provides appropriate feedback.

## Notes

- **Color Display**: Ensure your terminal or command prompt supports ANSI escape codes for color formatting.
- **Decimal Results**: Results of Dividing are shown as floating-point numbers to reflect accurate calculations.

