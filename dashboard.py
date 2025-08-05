import streamlit as st
import plotly.express as px
from data_cleaning import load_and_clean_data
from status_logic import calculate_status
from analysis import average_scores_by_role, module_completion_heatmap, status_counts

st.title("Onboarding Dashboard")

df = load_and_clean_data('onboarding_dataset.csv')
df = calculate_status(df)

st.subheader("Average Final Assessment Score by Role")
avg_scores = average_scores_by_role(df)
fig_bar = px.bar(avg_scores, x=avg_scores.index, y=avg_scores.values, labels={'x':'Role', 'y':'Average Score'})
st.plotly_chart(fig_bar)

st.subheader("Onboarding Status Distribution")
status = status_counts(df)
fig_pie = px.pie(names=status.index, values=status.values, title="Status Distribution")
st.plotly_chart(fig_pie)

st.subheader("Module Completion Rate by Role (Heatmap)")
heatmap_data = module_completion_heatmap(df)
fig_heat = px.imshow(heatmap_data, text_auto=True, aspect="auto", color_continuous_scale='Blues')
st.plotly_chart(fig_heat)

st.dataframe(df)