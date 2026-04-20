# Mean-Variance-Standard Deviation Calculator

This project is part of the ***Data Analysis with Python*** certification from freeCodeCamp.

## Project Description

The goal of this project is to create a function that calculates statistical measures for a 3x3 matrix using Python.

The function assumes the input is the Python's list of numbers. In case there are provided numbers different from the 9 of them, it returns ValueError. In remaining cases it takes them and converts it into a 3x3 NumPy array. Then it calculates:

* Mean
* Variance
* Standard Deviation
* Max
* Min
* Sum

These calculations are performed across:

* rows
* columns
* the entire matrix

## Technologies Used

* Python
* NumPy

## How to Run

1. Clone the repository:
   git clone https://github.com/your-username/mean-variance-standard-deviation-calculator.git

2. Navigate to the project folder:
   cd mean-variance-standard-deviation-calculator

3. Run the script:
   python mean_var_std.py

## Example Usage

Input:
[0,1,2,3,4,5,6,7,8]

Output:
{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
 'max': [[6.0, 7.0, 8.0], [2.0, 5.0, 8.0], 8.0],
 'min': [[0.0, 1.0, 2.0], [0.0, 3.0, 6.0], 0.0],
 'sum': [[9.0, 12.0, 15.0], [3.0, 12.0, 21.0], 36.0]
 }

## Project Structure

* mean_var_std.py — main function implementation
* main.py — An entrypoint file to be used in development. It imports main function implemented and runs unit tests automatically.
* test_module.py — unit tests provided by freeCodeCamp

## License

This project is licensed under the MIT License.
