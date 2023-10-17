import os
import pandas as pd

folder_path = './data/'
dataframes = []

for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):  # Adjust the file extension as needed
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)
        dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)
combined_df =  combined_df.iloc[:, 1:]  # This removes the first column
print(combined_df.info())
output_file = 'ai_description.xlsx'  # Specify the output file path and name
combined_df.to_excel(output_file, index=False)  
