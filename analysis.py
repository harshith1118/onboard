def average_scores_by_role(df):
    return df.groupby('Role')['Final_Assessment_Score'].mean().sort_values()

def module_completion_heatmap(df):
    return df.groupby('Role')[['Module_1_Completed', 'Module_2_Completed', 'Module_3_Completed']].mean()

def status_counts(df):
    return df['Status'].value_counts()