# Australia Wildfire Assignment 🔥

This repository contains the complete solution for the **Australia Wildfire Analysis and Dashboard Assignment**.

The assignment is divided into two main parts:
- **Part 1:** Data analysis and visualization
- **Part 2:** Interactive dashboard using Dash and Plotly

The dataset used contains historical wildfire data in Australia starting from 2005.

---

## 📂 Dataset Description

The wildfire dataset includes the following variables:

- **Region**: One of the 7 regions in Australia  
- **Date**: Date in UTC (24-hour period)  
- **Estimated_fire_area**: Daily sum of estimated fire area (km²) for presumed vegetation fires with confidence > 75%  
- **Mean_estimated_fire_brightness**: Daily mean fire brightness (Kelvin)  
- **Mean_estimated_fire_radiative_power**: Daily mean radiative power (MW)  
- **Mean_confidence**: Daily mean confidence level  
- **Std_confidence**: Standard deviation of fire radiative power  
- **Var_confidence**: Variance of fire radiative power  
- **Count**: Daily number of fire pixels with confidence > 75%  
- **Replaced**: Indicates whether data was replaced with higher-quality standard data  

---

## 📊 Part 1: Analyzing the Wildfire Activities in Australia

This part is implemented using **Google Colab** and focuses on data exploration and visualization.

### Tasks Completed
- Line plot of average estimated fire area over time
- Monthly analysis of estimated fire area
- Bar plot of mean estimated fire brightness across regions (Seaborn)
- Pie chart showing the distribution of fire pixel counts across regions
- Customized pie chart for better visualization
- Histogram of mean estimated fire brightness (Matplotlib)
- Distribution of fire brightness across regions using Seaborn with hue
- Scatter plot showing correlation between:
  - Mean estimated fire radiative power
  - Mean confidence level
- Interactive map of Australia highlighting all seven regions using Folium

### File
- `Wildfire_Australia.ipynb`

### Open in Google Colab
