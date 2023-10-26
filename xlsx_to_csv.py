import pandas as pd


def extract_values(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file, header=None)

    # Extract the variables (from row 0) and values (from row 3)
    variables = df.iloc[0].tolist()
    #values = df.iloc[3].tolist()

    # Create a new DataFrame with variables in the first column and values in the second column
    extracted_data = pd.DataFrame({'Variables': variables})#, 'Values': values})

    # Save as CSV
    extracted_data.to_csv(output_file, index=False)

# Example Usage
input_file = 'variables_input.xlsx'
output_file = 'output.csv'
extract_values(input_file, output_file)

