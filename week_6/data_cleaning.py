# Data cleaning script for 'Untitled form.csv' using pandas
import pandas as pd

# Load the CSV file
df = pd.read_csv('Untitled form.csv')

# Clean Seat Number (remove non-numeric, fill missing with -1)
df['Seat Number'] = pd.to_numeric(
    df['Seat Number'], errors='coerce').fillna(-1).astype(int)

# Save cleaned data to a new CSV
df.to_csv('Untitled_form_cleaned.csv', index=False)

print('Data cleaning complete. Cleaned file saved as Untitled_form_cleaned.csv')
