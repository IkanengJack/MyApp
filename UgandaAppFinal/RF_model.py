import pandas as pd

# Path to the .sav file
sav_file_path = 'RF_model_imp_feats.sav'

# Read the .sav file using pandas
df = pd.read_spss(sav_file_path)

# Path to save the CSV file
csv_file_path = 'RF_model_imp_feats.csv'

# Save the DataFrame as CSV
df.to_csv(csv_file_path, index=False)
