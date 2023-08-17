# Dataset Cleaning and Processing for Grading Application
This Python program is designed for cleaning and analyzing student data stored in a CSV file. It performs various data cleaning tasks, such as adjusting NIM (Student ID) format, handling missing values, correcting anomalies, and calculating statistical measures.

## Features
- Cleans and organizes student data from a CSV file.
- Removes duplicate records based on NIM.
- Converts letter grades in the dataset to numerical equivalents.
- Calculates means, medians, and standard deviations for different assignment types.
- Identifies and analyzes outliers in the dataset.
- Provides insights into high and low-performing students based on specific criteria.

## Usage
1. Clone the repository: `git clone [repo_link]`
2. Navigate to the project directory: `cd [directory_location]`
3. Run the program: `python [python_file]`
4. Follow the on-screen instructions to input the location of the CSV file and review the results.

## Dependencies
This project requires only Python to be installed. No additional external libraries are used.

## Running the program
1. Open the IDE software on your device.
2. Run the code using your chosen IDE (PyCharm, VS Code, etc.).
3.Input the file location of the dataset you want to clean (e.g., Ex: D:\Project\dataset3.csv).
4. After inputting, a cleaned .csv file (dataset_fixed.csv) will be generated with the cleaned data, and a .txt file (hasil.txt) will contain the answers to the provided questions.
5. You'll receive instructions asking if you want to check another dataset. If you input 'Y', the program will loop, but the .csv and .txt files will be reset. It's recommended to rename them before entering new data. If you input 'N' or any other letter, the program will terminate.

## Results
After running the program, the cleaned dataset will be saved to a file named 'dataset_fixed.csv'. Additionally, the program generates a 'hasil' file containing statistical measures and data analysis results.
