# notebooks/01_EDA.ipynb
# Copy this content into a new Jupyter notebook

"""
# Exploratory Data Analysis (EDA)

This notebook contains the exploratory data analysis for the learning path recommender project.

## Contents
1. Data Loading
2. Data Overview
3. Data Cleaning
4. Visualization
5. Insights and Conclusions
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set plotting style
plt.style.use('default')
sns.set_palette('husl')

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

