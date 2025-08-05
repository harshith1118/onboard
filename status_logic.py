import pandas as pd

def calculate_status(df, today=pd.to_datetime('2025-08-04')):
    def get_status(row):
        days_since_start = (today - row['Start_Date']).days
        modules_completed = row[['Module_1_Completed', 'Module_2_Completed', 'Module_3_Completed']].sum()
        expected_modules = min(3, days_since_start // 15)
        return 'On Track' if modules_completed >= expected_modules else 'Delayed'
    df['Status'] = df.apply(get_status, axis=1)
    return df
