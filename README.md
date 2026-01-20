# TOPSIS Python Module  - https://test.pypi.org/project/Topsis-Shivam-102303041/1.0.0/
Technique for Order Preference by Similarity to Ideal Solution

---

## Introduction

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) technique used to rank alternatives based on multiple criteria.

The basic idea of TOPSIS is:
- The best alternative should be closest to the ideal solution.
- The best alternative should be farthest from the worst solution.

This project provides a Python implementation of the TOPSIS method as a command-line based program, following all the constraints given in the assignment.

---

## Features

- Command-line based execution
- Works with any number of criteria
- Input validation and error handling
- Computes TOPSIS score and rank
- Simple and beginner-friendly implementation

---

## Project Structure

Topsis-Shivam-102303041  
│  
├── topsis  
│   ├── __init__.py  
│   ├── __main__.py  
│   └── data.csv  
│  
├── setup.py  
├── MANIFEST.in  
├── README.md  
├── LICENSE  
└── .gitignore  

---

## Input File Format

The input file must be a CSV file with:
- First column: Alternatives (e.g., Fund Name)
- Remaining columns: Numeric criteria values

Example input file (`data.csv`):

Fund Name,P1,P2,P3,P4,P5  
M1,0.67,0.45,6.5,42.6,12.56  
M2,0.60,0.36,3.6,53.3,14.47  
M3,0.82,0.67,3.8,63.1,17.10  
M4,0.60,0.36,3.5,69.2,18.42  

---

## Command Line Usage

Syntax:

python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>

Example:

python topsis.py data.csv "1,1,1,1,1" "+,+,-,-,-" result.csv

Where:
- Weights define the importance of each criterion.
- Impacts use '+' for benefit criteria and '-' for cost criteria.
- Output file contains TOPSIS score and rank.

---

## Methodology

The TOPSIS method is implemented using the following steps:

1. Read the input CSV file.
2. Normalize the decision matrix.
3. Multiply normalized values by weights.
4. Identify ideal best and ideal worst values.
5. Calculate Euclidean distance from ideal best and worst.
6. Compute TOPSIS score for each alternative.
7. Rank alternatives based on TOPSIS score.

---

## Output File

The output CSV file contains:
- Original input data
- Topsis Score
- Rank

The alternative with the highest TOPSIS score is ranked 1 and considered the best option.

---

## Google Colab Notebook

A Google Colab notebook is included only for demonstration and explanation purposes.

Since Google Colab does not support command-line arguments directly, weights and impacts are defined inside the notebook for demonstration.  
The actual solution is implemented as a command-line program.

---

## Installation (Optional)

To install the module locally:

pip install -e .

To run the program after installation:

topsis

---

## Dependencies

- Python 3.7 or above
- pandas
- numpy

---

## Conclusion

This project demonstrates a complete and flexible implementation of the TOPSIS decision-making method using Python.  
It satisfies all assignment requirements and can be used for academic and learning purposes.

---

## Author

Shivam Sukhija  
Roll Number: 102303041  

---

## License

This project is licensed under the MIT License.
