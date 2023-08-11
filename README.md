# Startup Profit Prediction Using Linear Regression

This repository contains Python code to predict the profits of startups based on their R&D spending, administration costs, marketing expenses, and state using linear regression.

## Getting Started

### Prerequisites

- Python (version 3)
- Required libraries: pandas, matplotlib, scikit-learn

### Installation

1. Clone the repository:
git clone  https://github.com/dineshghadge2002/Linear_Regression_Sartup_Data.git
2. Install the required libraries:
pip install pandas matplotlib scikit-learn

### Usage

1. Load the dataset `50_Startups.csv` using pandas.
2. Preprocess the data by selecting features and creating dummy variables for the 'State' column.
3. Split the data into training and testing sets.
4. Train a linear regression model on the training data.
5. Make predictions on the test data and calculate the Mean Absolute Error.

```python
# Sample code snippet
# ...

# Applying error matrix
from sklearn import metrics
mae = metrics.mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)
