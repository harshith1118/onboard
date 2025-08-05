# Onboarding Dashboard

This project provides an interactive dashboard for analyzing employee onboarding data using Streamlit and Plotly.

## Features

- **Data Cleaning:** Cleans and preprocesses onboarding data.
- **Status Calculation:** Identifies employees as "On Track" or "Delayed" based on module completion and start date.
- **Analysis:** Calculates average assessment scores by role.
- **Visualizations:** Interactive bar charts, pie charts, and heatmaps.
- **Modular Code:** Logic is split into separate files for maintainability.

## File Structure

- `onboarding_dataset.csv` — The onboarding data.
- `data_cleaning.py` — Data loading and cleaning functions.
- `status_logic.py` — Onboarding status calculation.
- `analysis.py` — Analysis and aggregation functions.
- `dashboard.py` — Streamlit dashboard app.

## Setup

1. **Install dependencies:**

   ```powershell
   pip install streamlit plotly pandas
   ```

2. **Run the dashboard:**

   ```powershell
   streamlit run dashboard.py
   ```

3. **View in browser:**  
   Streamlit will open a local server; follow the link in your terminal.

## Usage

- Explore onboarding trends and employee status.
- Filter and sort data interactively.
- Visualize module completion rates and assessment scores.

## Customization

- Update `onboarding_dataset.csv` with your own data.
- Modify analysis or visualization logic in the respective Python files.

---
