import pandas as pd

def extract_values(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, header=None)

    # Extract the values from rows 1 and 4
    extracted_data = df.iloc[[0]]

    # Transpose the DataFrame to have variables as columns
    extracted_data = extracted_data.transpose()

    # Set column names
    extracted_data.columns = extracted_data.iloc[0]

    # Drop the first row (contains column names)
    extracted_data = extracted_data[1:]

    # Save as CSV
    extracted_data.to_csv(output_file, index=False)

# Example Usage
input_file = 'variables_input.xlsx'
output_file = 'output.csv'
extract_values(input_file, output_file)
