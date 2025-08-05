import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()
    df['Start_Date'] = pd.to_datetime(df['Start_Date'])
    for col in ['Module_1_Completed', 'Module_2_Completed', 'Module_3_Completed']:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    return df