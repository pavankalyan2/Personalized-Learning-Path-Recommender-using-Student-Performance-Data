# notebooks/02_Model_Training.ipynb
# Copy this content into a new Jupyter notebook

"""
# Model Training

This notebook contains the model training pipeline for the learning path recommender.

## Contents
1. Data Preprocessing
2. Feature Engineering
3. Model Selection
4. Training
5. Model Saving
"""

# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

