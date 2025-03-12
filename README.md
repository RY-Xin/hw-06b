# Triangle Classification Project

This project contains a Python program that classifies triangles based on their side lengths. The classification includes identifying whether the triangle is Equilateral, Isosceles, Scalene, or Invalid. It also checks for right-angled triangles.

## Project Structure

- `classify_triangle.py`: Contains the main function `classify_triangle()` that classifies triangles based on side lengths.
- `test_classify_triangle.py`: Contains unit tests for the `classify_triangle()` function to ensure its correctness.
- `result.txt`: Contains the output from running the unit tests.

## Description

The `classify_triangle.py` program includes a function `classify_triangle(a, b, c)` which:
- Takes three sides of a triangle as input.
- Classifies the triangle based on the following criteria:
  - **Equilateral Triangle**: All sides are equal.
  - **Isosceles Triangle**: Two sides are equal.
  - **Scalene Triangle**: All sides are different.
  - **Invalid Triangle**: If the sum of two sides is less than or equal to the third side or if any side is non-positive.

The program also checks for **Right-Angled Triangles** by using the Pythagorean theorem.

## Requirements

- Python 3.x

## Installation

To install and run the project:

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
Navigate to the project directory:

bash
Copy
Edit
cd Triangle-Classification
Run the program:

bash
Copy
Edit
python3 classify_triangle.py
Testing
The test_classify_triangle.py file contains unit tests that verify the functionality of the classify_triangle() function. The tests cover various scenarios, including:

Equilateral triangles
Isosceles triangles
Scalene triangles
Right-angled triangles
Invalid triangles
To run the tests, use the following command:

bash
Copy
Edit
python3 -m unittest test_classify_triangle.py
Test Results
All tests passed successfully, confirming the correctness of the code. Here is a summary of the tests:

Test ID	Input	Expected Results	Actual Result	Pass or Fail
1	(5, 5, 5)	Equilateral Triangle	Equilateral Triangle	Pass
2	(2, 2, 3)	Isosceles Triangle	Isosceles Triangle	Pass
3	(3, 4, 5)	Scalene Triangle and Right	Scalene Triangle and Right	Pass
4	(1, 1, 2)	Invalid Triangle	Invalid Triangle	Pass
Reflection
The tests were designed to cover all edge cases, including both valid and invalid triangles, as well as right-angled triangles. The bug in the initial implementation was fixed by correctly checking the sum of the sides and adjusting the logic to handle right-angled triangles.

Contribution
Feel free to fork this repository and contribute by submitting pull requests for improvements or bug fixes.



