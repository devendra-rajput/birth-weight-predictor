# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split as ttl
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Load the dataset
babies_df = pd.read_csv("dataset/babies.csv")

# Drop the 'case' column as it's likely an identifier and not useful for prediction
babies_df.drop(columns=["case"], inplace=True)

# Remove rows with missing values to ensure model training isn't affected by NaNs
# (optional print statements are commented out for checking nulls)
# print(babies_df.isnull().sum())
babies_df.dropna(inplace=True)
# print(babies_df.isnull().sum())

# Separate the target variable (birth weight) and the features
y = babies_df["bwt"]                    # Target variable
x = babies_df.drop(columns=["bwt"])    # Feature variables

# Split the dataset into training and testing sets (80% train, 20% test)
x_train, x_test, y_train, y_test = ttl(x, y, test_size=0.20)

# Initialize three different regression models
lr = LinearRegression()
las = Lasso()
rid = Ridge()

# Train each model on the training data
lr.fit(x_train, y_train)
las.fit(x_train, y_train)
rid.fit(x_train, y_train)

# Make predictions using the test data
lr_predict = lr.predict(x_test)
las_predict = las.predict(x_test)
rid_predict = rid.predict(x_test)

# Evaluate model performance using R-squared
lr_score = r2_score(y_test, lr_predict)
las_score = r2_score(y_test, las_predict)
rid_score = r2_score(y_test, rid_predict)

# Evaluate model performance using Mean Squared Error (MSE)
lr_mse = mean_squared_error(y_test, lr_predict)
las_mse = mean_squared_error(y_test, las_predict)
rid_mse = mean_squared_error(y_test, rid_predict)

# Save the trained Linear Regression model using pickle
# (Only the Linear Regression model is saved here)
with open("models/model.pkl", "wb") as pklFile:
    pickle.dump(lr, pklFile)
