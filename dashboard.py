import streamlit as st
import plotly.express as px
import pandas as pd
from data_cleaning import load_and_clean_data
from status_logic import calculate_status
from analysis import average_scores_by_role, module_completion_heatmap, status_counts

st.title("Onboarding Dashboard 📊")
st.markdown("### Key Insights and Analytics")

# Load and process data
df = load_and_clean_data('onboarding_dataset.csv')
df = calculate_status(df)

# Key Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Employees", len(df))
with col2:
    on_track = len(df[df['Status'] == 'On Track'])
    st.metric("On Track", f"{on_track} ({on_track/len(df)*100:.1f}%)")
with col3:
    avg_score = df['Final_Assessment_Score'].mean()
    st.metric("Avg Assessment Score", f"{avg_score:.1f}%")

# Role Performance Analysis
st.header("📈 Role Performance Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Average Assessment Score by Role")
    avg_scores = average_scores_by_role(df)
    fig_bar = px.bar(avg_scores, x=avg_scores.index, y=avg_scores.values, 
                     labels={'x':'Role', 'y':'Average Score'},
                     color=avg_scores.values,
                     color_continuous_scale='Viridis')
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader("Onboarding Status Distribution")
    status = status_counts(df)
    fig_pie = px.pie(names=status.index, values=status.values,
                     title="Status Distribution",
                     color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_pie, use_container_width=True)

# Module Progress Analysis
st.header("📊 Module Completion Analysis")
st.subheader("Module Completion Rate by Role")
heatmap_data = module_completion_heatmap(df)
fig_heat = px.imshow(heatmap_data, 
                     text_auto=True,
                     aspect="auto",
                     color_continuous_scale='Blues',
                     labels=dict(x="Module", y="Role", color="Completion Rate"))
st.plotly_chart(fig_heat, use_container_width=True)

# Detailed Data View
st.header("🔍 Detailed Employee Data")
st.markdown("Filter and explore individual employee progress")

# Add filters
col1, col2, col3 = st.columns(3)
with col1:
    selected_role = st.selectbox("Filter by Role", ["All"] + list(df['Role'].unique()))
with col2:
    selected_status = st.selectbox("Filter by Status", ["All"] + list(df['Status'].unique()))
with col3:
    score_range = st.slider("Filter by Score Range", 
                           float(df['Final_Assessment_Score'].min()),
                           float(df['Final_Assessment_Score'].max()),
                           (float(df['Final_Assessment_Score'].min()),
                            float(df['Final_Assessment_Score'].max())))

# Apply filters
filtered_df = df.copy()
if selected_role != "All":
    filtered_df = filtered_df[filtered_df['Role'] == selected_role]
if selected_status != "All":
    filtered_df = filtered_df[filtered_df['Status'] == selected_status]
filtered_df = filtered_df[
    (filtered_df['Final_Assessment_Score'] >= score_range[0]) &
    (filtered_df['Final_Assessment_Score'] <= score_range[1])
]

st.dataframe(filtered_df, use_container_width=True)