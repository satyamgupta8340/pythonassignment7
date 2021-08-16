# Questions
 #Prepare a jupyter notebook (recommended - Google Colab) to build, train and evaluate a Machine Learning model on the given dataset. Please read the instructions carefully.
 #Part A
 # Dataset - https://drive.google.com/file/d/1xS-hVwIZdO5yVkFt6BL3xbi2UUOEim0Z/view?usp=sharing
#  Data were collected on 81 patients undergoing corrective spinal surgery (Bell et al., 1989). The objective was to determine important risk factors for kyphosis following surgery. The risk factors are age in years, the starting vertebrae level of the surgery and the number of levels involved.
#1. Import Libraries/Dataset
#a. Download the dataset

#b. Import the required libraries



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('kyphosis.csv')
data
