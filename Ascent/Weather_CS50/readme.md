This README file provides an overview of the provided code and instructions on how to run it. Please follow the steps below to execute the code successfully.
## Prerequisites
* Python 3.x
* Pandas library
* Scikit-learn library


## Installation
1. Install Python: If you don't have Python installed, please download and install the latest version from the official [Python website](https://www.python.org).

2. Install required libraries: Open a terminal or command prompt and execute the following command to install the necessary libraries
```json
pip install pandas scikit-learn
```
## Usage
1. Data Preparation:

* Ensure that the training data is available in a CSV file named 'train.csv'. Make sure the file does not contain any missing values (NaN).
* Prepare a testing CSV file named 'test.csv' with the same format as 'train.csv'. Remove any missing values (NaN) from the file.
* Prepare a CSV file named 'final_test.csv' containing the data for which you want to make predictions. Ensure that the file has the same format as 'train.csv'. Remove any missing values (NaN) from the file.
2. Code Execution:

* Save the provided code in a file, e.g., 'prediction_script.py'.
* Open a terminal or command prompt and navigate to the directory where the 'prediction_script.py' file is located.
* Run the code by executing the following command:
```
python prediction_script.py
```
3. Output:

* The code will generate a file named 'list.csv' in the same directory.
* 'list.csv' will contain the predicted weather values for the data provided in 'final_test.csv'.

