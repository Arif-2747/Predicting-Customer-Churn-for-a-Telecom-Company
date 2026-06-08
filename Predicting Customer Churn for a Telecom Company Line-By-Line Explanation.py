import pandas as pd
# This line imports the pandas library, commonly used for data manipulation and analysis.
# It's aliased as 'pd' for convenience.

#plt.savefig(file_name.png) - saves the output as png
# This is a commented-out line, indicating how to save a plot as a PNG file.
# It's a helpful note for future use but not executed in this script.

#plt.close() - closes the plot to free up memory
# This is another commented-out line, indicating how to close a plot to release memory.
# Also a helpful note, not executed directly in this script's main flow.

import numpy as np
# This line imports the numpy library, which is fundamental for numerical operations in Python,
# especially for working with arrays and mathematical functions. It's aliased as 'np'.

# Load the dataset
df = pd.read_csv('telecom_churn.csv')
# This line loads the dataset named 'telecom_churn.csv' into a pandas DataFrame called 'df'.
# A DataFrame is a tabular data structure with labeled axes (rows and columns).

# Display the first few rows
print("Initial DataFrame head:")
# This prints a descriptive header for the output that follows.
print(df.head())
# This displays the first 5 rows of the DataFrame 'df'. It's useful for a quick look at the data structure.

# Check the shape of the dataset
print(f'\nShape of the dataset: {df.shape}')
# This prints the dimensions (number of rows, number of columns) of the DataFrame.

# Get a summary of the dataset
print("\nInitial DataFrame info:")
# This prints a descriptive header.
print(df.info())
# This provides a concise summary of the DataFrame, including the data types of each column,
# the number of non-null values, and memory usage. It's crucial for identifying missing data and types.

# Check the distribution of the target variable
print("\nDistribution of 'churn' variable:")
# This prints a descriptive header.
print(df['churn'].value_counts())
# This calculates and displays the count of unique values in the 'churn' column.
# 'churn' is likely the target variable, indicating whether a customer churned or not.

# Get summary statistics
print("\nSummary statistics of the DataFrame:")
# This prints a descriptive header.
print(df.describe())
# This generates descriptive statistics (count, mean, std, min, max, quartiles)
# for all numerical columns in the DataFrame.

import matplotlib.pyplot as plt
# This imports the matplotlib.pyplot module, which is a plotting library for Python.
# It's aliased as 'plt' for convenience.

import seaborn as sns
# This imports the seaborn library, a high-level data visualization library based on matplotlib.
# It's aliased as 'sns' and is used for creating more aesthetically pleasing and informative statistical graphics.

# Histograms of numerical features
# Identify numerical columns for individual histograms
numerical_columns = df.select_dtypes(include=np.number).columns.tolist()
# This line selects all columns in the DataFrame 'df' that have a numerical data type
# (e.g., int, float) and converts their names into a list.

columns_to_exclude_from_hist = [] # No columns are excluded
# This initializes an empty list for columns that should not have histograms generated.
numerical_columns_for_hist = [col for col in numerical_columns if col not in columns_to_exclude_from_hist]
# This creates a new list of numerical columns, excluding any specified in `columns_to_exclude_from_hist`.

print(f"\nGenerating individual histograms for {len(numerical_columns_for_hist)} numerical features in separate interactive windows...")
# This prints a message indicating the start of histogram generation.

for col in numerical_columns_for_hist:
# This loop iterates through each numerical column identified for histogram plotting.
    fig, ax = plt.subplots(figsize=(10, 6)) # Create a new figure and axes for each plot
    # This creates a new figure and a set of subplots (axes) for each histogram.
    # `figsize` sets the width and height of the figure in inches.
    df[col].hist(bins=30, ax=ax)
    # This generates a histogram for the current numerical column (`col`) using 30 bins.
    # `ax=ax` ensures the histogram is drawn on the newly created axes.
    ax.set_title(f'Histogram of {col}', fontsize=16) # Set subplot title
    # This sets the title of the current histogram.
    ax.set_xlabel(col, fontsize=12)
    # This sets the label for the x-axis.
    ax.set_ylabel('Frequency', fontsize=12)
    # This sets the label for the y-axis.
    ax.grid(axis='y', alpha=0.75) # Improve grid visibility
    # This adds a grid to the y-axis for better readability.
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    # This automatically adjusts subplot parameters for a tight layout, preventing labels from overlapping.

    # Set the window title
    try:
    # This `try` block attempts to set the title of the interactive plot window.
        fig.canvas.manager.set_window_title(f'Histogram: {col}')
        # This line specifically sets the title of the matplotlib window.
    except Exception as e:
    # This `except` block catches any errors that might occur if the window manager is not available.
        print(f"Could not set window title for {col}: {e}") # Handle if manager is not available in environment
        # This prints an error message if the window title cannot be set.

    plt.show()
    # This displays the generated histogram in a separate interactive window.

# Bar plot of categorical features
current_categorical_columns = df.select_dtypes(include=['object']).columns
# This line selects all columns in the DataFrame 'df' that have an 'object' data type (typically strings, representing categorical data).

print(f"\nGenerating individual bar graphs for {len(current_categorical_columns) - 1 if 'churn' in current_categorical_columns else len(current_categorical_columns)} categorical features in separate interactive windows...")
# This prints a message indicating the start of bar graph generation,
# adjusting the count if 'churn' is still considered an object type.

for column in current_categorical_columns:
# This loop iterates through each categorical column.
    if column != 'churn': # Exclude the target variable if it's still an object type
    # This condition ensures that the 'churn' column (which is the target) is not plotted as a categorical bar graph if it's still an object.
        fig, ax = plt.subplots(figsize=(12, 7)) # Create a new figure and axes, increased size
        # This creates a new figure and axes for each bar graph.
        df[column].value_counts().plot(kind='bar', ax=ax)
        # This calculates the frequency of each unique value in the current categorical column
        # and then plots these counts as a bar graph on the specified axes.
        ax.set_title(f'Bar Graph of {column}', fontsize=16) # Set subplot title
        # This sets the title of the current bar graph.
        ax.set_xlabel(column, fontsize=12)
        # This sets the label for the x-axis.
        ax.set_ylabel('Count', fontsize=12)
        # This sets the label for the y-axis.
        plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for neatness, adjust alignment
        # This rotates the x-axis labels by 45 degrees and aligns them to the right for better readability, especially with long labels.
        plt.tight_layout() # Adjust layout to prevent labels from overlapping
        # This automatically adjusts subplot parameters for a tight layout.

        # Set the window title
        try:
        # This `try` block attempts to set the title of the interactive plot window.
            fig.canvas.manager.set_window_title(f'Bar Graph: {column}')
            # This line sets the title of the matplotlib window.
        except Exception as e:
        # This `except` block catches any errors if the window manager is not available.
            print(f"Could not set window title for {column}: {e}")
            # This prints an error message if the window title cannot be set.

        plt.show()
        # This displays the generated bar graph in a separate interactive window.

# Pairplot to see relationships
# Ensure only existing numeric columns are included for pairplot
numeric_cols_for_pairplot = ['account length', 'total day minutes', 'total day charge',
                             'total eve minutes', 'total eve calls', 'total eve charge',
                             'total night minutes', 'total night calls', 'total night charge',
                             'total intl minutes', 'total intl calls', 'total intl charge',
                             'customer service calls', 'area code', 'number vmail messages']
# This defines a list of specific numerical columns that are intended for the pairplot.

print("\nGenerating Pairplot of Key Features in a separate interactive window...")
# This prints a message indicating the start of pairplot generation.

try:
# This `try` block encloses the pairplot generation to handle potential errors.
    existing_numeric_cols_for_pairplot = [col for col in numeric_cols_for_pairplot if col in df.columns]
    # This filters the `numeric_cols_for_pairplot` list to include only columns that actually exist in the DataFrame.
    if existing_numeric_cols_for_pairplot:
    # This checks if there are any suitable numeric columns left for plotting.
        # Use a smaller subset for pairplot if there are too many columns to avoid congestion
        # Selecting top 5 features by correlation with churn for better clarity if many columns
        if len(existing_numeric_cols_for_pairplot) > 5:
        # If there are more than 5 numerical columns, a subset will be chosen for clarity.
            print("Warning: Many numeric columns for pairplot. Plotting a subset of top 5 correlated features for clarity.")
            # This prints a warning about plotting a subset.
            if 'churn' in df.columns and pd.api.types.is_numeric_dtype(df['churn']):
            # This checks if 'churn' column exists and is numeric.
                temp_df_for_corr = df.copy()
                # Creates a copy of the DataFrame to avoid modifying the original during correlation calculation.
                if temp_df_for_corr['churn'].dtype == 'bool':
                # If 'churn' is boolean, convert it to integer (0 or 1) for correlation calculation.
                    temp_df_for_corr['churn'] = temp_df_for_corr['churn'].astype(int)
                # Ensure only numeric columns are passed to .corr()
                numeric_cols_for_corr_calc = [col for col in existing_numeric_cols_for_pairplot + ['churn'] if pd.api.types.is_numeric_dtype(temp_df_for_corr[col])]
                # Filters to ensure only truly numeric columns are used for correlation.
                correlations = temp_df_for_corr[numeric_cols_for_corr_calc].corr()
                # Calculates the pairwise correlation between numerical columns.
                # Check if 'churn' is in correlations index before accessing
                if 'churn' in correlations.columns:
                # Checks if 'churn' is a column in the correlation matrix.
                    top_features = correlations['churn'].abs().sort_values(ascending=False).index.tolist()
                    # Sorts features by their absolute correlation with 'churn' in descending order.
                    # Remove 'churn' itself from top_features if present
                    if 'churn' in top_features:
                    # Removes 'churn' from the list of top features if it's there.
                        top_features.remove('churn')
                    top_features = top_features[:5] # Get top 5 features
                    # Selects the top 5 most correlated features.
                else:
                    top_features = existing_numeric_cols_for_pairplot[:5] # Fallback if churn not in correlation
                    # Fallback to the first 5 existing numeric columns if 'churn' is not found in correlations.
                
                if top_features:
                # If top features are identified, proceed with pairplot.
                    g = sns.pairplot(df, hue='churn', vars=top_features)
                    # This generates a pairplot using seaborn.
                    # `hue='churn'` colors the points based on the 'churn' variable,
                    # allowing visualization of how features relate to churn.
                    # `vars` specifies the columns to include in the pairplot.
                else: # Fallback if no suitable features after correlation
                    g = sns.pairplot(df, hue='churn', vars=existing_numeric_cols_for_pairplot[:5])
                    # Fallback to the first 5 existing numeric columns if no suitable features are found.
            else:
                g = sns.pairplot(df, hue='churn', vars=existing_numeric_cols_for_pairplot[:5])
                # If 'churn' is not numeric, plot with the first 5 numeric columns.
        else:
            g = sns.pairplot(df, hue='churn', vars=existing_numeric_cols_for_pairplot)
            # If there are 5 or fewer numerical columns, all are included in the pairplot.

        # Set the window title for the PairGrid figure
        try:
        # This `try` block attempts to set the title of the interactive plot window.
            g.fig.canvas.manager.set_window_title('Pairplot of Key Features')
            # This sets the title of the matplotlib window for the pairplot.
        except Exception as e:
        # This `except` block catches any errors if the window manager is not available.
            print(f"Could not set window title for Pairplot: {e}")
            # This prints an error message if the window title cannot be set.

        plt.show() # Display the plot window
        # This displays the generated pairplot.
    else:
        print("\nNo suitable numeric columns found for pairplot.")
        # This message is printed if no numeric columns are available for the pairplot.
except Exception as e:
# This `except` block catches any general errors during pairplot generation.
    print(f"Error during pairplot: {e}.")
    # This prints an error message if an error occurs.
    
# Convert 'voice mail plan' from 'Yes'/'No' to 1/0 for numerical correlation
if 'voice mail plan' in df.columns and df['voice mail plan'].dtype == 'object':
# This checks if 'voice mail plan' column exists and its data type is 'object' (string).
    df['voice mail plan'] = df['voice mail plan'].replace({'No': 0, 'Yes': 1})
    # This replaces 'No' with 0 and 'Yes' with 1 in the 'voice mail plan' column, converting it to a numerical type.
    print("\n'voice mail plan' column converted to numeric.")
else:
    print("\n'voice mail plan' column not found or already numeric.")
    # This message is printed if the column is not found or is already numeric.

# Check for missing values
print("\nMissing values after 'voice mail plan' conversion:")
# This prints a descriptive header.
print(df.isnull().sum())
# This calculates and displays the number of missing (NaN) values for each column in the DataFrame.

# --- Robust NaN Handling before further processing ---
# This step is added as an extra safeguard, even if df.isnull().sum() indicates no NaNs.
# It will fill any remaining numeric NaNs with their mean.
initial_nan_count = df.isnull().sum().sum()
# This calculates the total number of NaN values across the entire DataFrame.
if initial_nan_count > 0:
# This block executes only if there are any missing values found.
    print(f"\nFound {initial_nan_count} NaNs before comprehensive handling. Filling them now.")
    # Prints a message indicating that NaNs were found and will be filled.
    for col in df.columns:
    # This loop iterates through each column in the DataFrame.
        if df[col].dtype in ['float64', 'int64'] and df[col].isnull().any():
        # If the column is numeric (float or int) and has any missing values:
            df[col].fillna(df[col].mean(), inplace=True)
            # Missing values in that numerical column are filled with the mean of that column.
            # `inplace=True` modifies the DataFrame directly.
        elif df[col].dtype == 'object' and df[col].isnull().any():
        # If the column is an object (categorical) and has any missing values:
            # For object columns, fill with mode or a placeholder if NaNs are expected
            # For this dataset, based on df.info(), objects shouldn't have NaNs
            df[col].fillna(df[col].mode()[0], inplace=True) # Fill with mode for categorical NaNs
            # Missing values in that categorical column are filled with the mode (most frequent value) of that column.
else:
    print("\nNo missing values found in the DataFrame after initial conversions.")
    # This message is printed if no missing values are found.
# --- End Robust NaN Handling ---

# Correlation matrix
correlation_matrix = df.corr(numeric_only=True) # Exclude non-numeric columns from correlation calculation
# This calculates the pairwise correlation between all numerical columns in the DataFrame.
# `numeric_only=True` ensures only numerical columns are considered.
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# This generates a heatmap of the correlation matrix using seaborn.
# `annot=True` displays the correlation values on the heatmap.
# `cmap='coolwarm'` sets the color scheme for the heatmap.
plt.show()
# This displays the correlation heatmap.

# --- Crucial Fix: Drop 'phone number' as it's a unique identifier and not a feature ---
if 'phone number' in df.columns:
# This checks if the 'phone number' column exists in the DataFrame.
    df.drop('phone number', axis=1, inplace=True)
    # If it exists, this line drops the 'phone number' column from the DataFrame.
    # `axis=1` specifies that a column should be dropped. `inplace=True` modifies the DataFrame directly.
    # Phone numbers are unique identifiers and generally not useful features for machine learning models.
    print("\n'phone number' column dropped from the DataFrame.")
else:
    print("\n'phone number' column not found, no need to drop.")
    # This message is printed if the 'phone number' column is not found.

# Convert categorical columns to dummy variables
categorical_columns_for_dummies = df.select_dtypes(include=['object']).columns.tolist()
# This re-identifies categorical columns (object type) after previous modifications.

if 'phone number' in categorical_columns_for_dummies:
# This checks if 'phone number' is still in the list (though it should have been dropped).
    categorical_columns_for_dummies.remove('phone number')
    # Removes 'phone number' from the list if it's there.
    print("\n'phone number' column excluded from dummy variable creation.")

if 'churn' in categorical_columns_for_dummies:
# This checks if 'churn' is in the list of categorical columns.
    categorical_columns_for_dummies.remove('churn') # Remove churn from categorical columns to avoid dummy creation for target
    # Removes 'churn' from the list because it's the target variable and should not be converted to dummy variables.

if categorical_columns_for_dummies:
# This block executes if there are any categorical columns remaining to be converted.
    df = pd.get_dummies(df, columns=categorical_columns_for_dummies, drop_first=True)
    # This performs one-hot encoding on the specified categorical columns.
    # `pd.get_dummies` creates new binary (0 or 1) columns for each unique category.
    # `drop_first=True` prevents multicollinearity by dropping the first category's dummy column.
    print("\nCategorical columns converted to dummy variables.")
else:
    print("\nNo additional categorical columns found for dummy variable conversion.")
    # This message is printed if no additional categorical columns are found.

# Ensure the target column 'churn' is binary
if df['churn'].dtype == 'bool':
# This checks if the 'churn' column is of boolean type.
    df['churn'] = df['churn'].astype(int) # Correctly converts True to 1, False to 0
    # If boolean, it converts True to 1 and False to 0, making it an integer (binary) column.
    print("\n'churn' column converted from boolean to integer (0 and 1).")
elif df['churn'].dtype == 'object': # Fallback if it was somehow an object with 'Yes'/'No'
# This is a fallback in case 'churn' is still an object type (e.g., 'Yes'/'No' strings).
    df['churn'] = df['churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    # It converts 'Yes' to 1 and 'No' to 0.
    print("\n'churn' column converted from object (Yes/No) to integer (0 and 1).")
else:
    print("\n'churn' column is already numeric (0 or 1).")
    # This message is printed if 'churn' is already numeric.

# Print info after all preprocessing steps
print("\nDataFrame info after all preprocessing:")
# This prints a descriptive header.
print(df.info())
# This displays the DataFrame's information again after all preprocessing, showing the new column types and structure.

import numpy as np
# Re-imports numpy (already imported, but good practice if this was a standalone snippet).
from sklearn.preprocessing import StandardScaler
# Imports StandardScaler from scikit-learn, used for standardizing features.

# Separate features and target variable
X = df.drop('churn', axis=1)
# This creates a new DataFrame `X` by dropping the 'churn' column from `df`.
# `X` will contain all the features (independent variables) for the model.
y = df['churn']
# This creates a pandas Series `y` containing only the 'churn' column.
# `y` is the target variable (dependent variable) that the model will predict.

# --- Final Check for NaNs/Infs in X and y before scaling ---
print("\n--- Final check for NaNs/Infs in X and y before scaling ---")
# Prints a header for the final check.
final_nan_X = X.isnull().sum().sum()
# Calculates the total number of NaN values in the feature DataFrame `X`.
final_inf_X = X.isin([np.inf, -np.inf]).sum().sum()
# Calculates the total number of infinite values (positive or negative) in `X`.
final_nan_y = y.isnull().sum()
# Calculates the total number of NaN values in the target Series `y`.
final_inf_y = y.isin([np.inf, -np.inf]).sum()
# Calculates the total number of infinite values in `y`.

print(f"Final NaN values in X before scaling: {final_nan_X}")
print(f"Final Inf values in X before scaling: {final_inf_X}")
print(f"Final NaN values in y before scaling: {final_nan_y}")
print(f"Final Inf values in y before scaling: {final_inf_y}")
# Prints the counts of NaN and Inf values.
if final_nan_X > 0 or final_inf_X > 0 or final_nan_y > 0 or final_inf_y > 0:
# If any non-finite values are found:
    print("CRITICAL WARNING: Non-finite values still present in data before scaling. This WILL cause errors.")
    # Prints a critical warning.
    # You might want to stop execution here if this occurs again, to inspect 'X' and 'y' directly.
    # This comment suggests a potential debugging step.
# --- End Final Check ---

# Standardize the features
scaler = StandardScaler()
# This creates an instance of the StandardScaler.
# StandardScaler transforms features to have a mean of 0 and a standard deviation of 1.
X_scaled = scaler.fit_transform(X)
# This fits the scaler to the feature data `X` (calculates mean and std)
# and then transforms `X` using these calculated values.
# `X_scaled` now contains the standardized features.

from sklearn.model_selection import train_test_split
# Imports train_test_split from scikit-learn, used for splitting datasets.

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# This splits the standardized features (`X_scaled`) and target variable (`y`)
# into training and testing sets.
# `test_size=0.2` means 20% of the data will be used for testing, and 80% for training.
# `random_state=42` ensures reproducibility of the split.
print(f'Shape of X_train: {X_train.shape}')
print(f'Shape of X_test: {X_test.shape}')
print(f'Shape of y_train: {y_train.shape}')
print(f'Shape of y_test: {y_test.shape}')
# These lines print the dimensions of the newly created training and testing sets.

# --- Debugging checks before model training ---

print("\n--- Checking for NaNs/Infs in training data before model.fit() ---")
# Prints a header for debugging checks.
# Convert to DataFrame/Series for easy NaN/Inf checking with pandas methods
X_train_df = pd.DataFrame(X_train)
# Converts X_train (which is a numpy array after scaling) back to a DataFrame for easier NaN/Inf checking.
y_train_series = pd.Series(y_train)
# Converts y_train (which is a numpy array after splitting) back to a Series.

nan_in_X_train = X_train_df.isnull().sum().sum()
# Calculates total NaNs in X_train.
inf_in_X_train = X_train_df.isin([np.inf, -np.inf]).sum().sum()
# Calculates total Infs in X_train.
nan_in_y_train = y_train_series.isnull().sum()
# Calculates total NaNs in y_train.
inf_in_y_train = y_train_series.isin([np.inf, -np.inf]).sum()
# Calculates total Infs in y_train.

print(f"Number of NaN values in X_train: {nan_in_X_train}")
print(f"Number of Inf values in X_train: {inf_in_X_train}")
print(f"Number of NaN values in y_train: {nan_in_y_train}")
print(f"Number of Inf values in y_train: {inf_in_y_train}")
# Prints the counts of NaN and Inf values in training data.
if nan_in_X_train > 0 or inf_in_X_train > 0 or nan_in_y_train > 0 or inf_in_y_train > 0:
# If any non-finite values are found in training data:
    print("WARNING: Non-finite values detected in training data. This might cause issues during model fitting.")
    # Prints a warning.
print("--- End of debugging checks ---")

from sklearn.linear_model import LogisticRegression
# Imports the LogisticRegression model from scikit-learn.

# Create and train the model
model = LogisticRegression(max_iter=1000)
# This creates an instance of the Logistic Regression model.
# `max_iter=1000` sets the maximum number of iterations for the solver to converge,
# which can help prevent a `ConvergenceWarning` for larger datasets or complex models.
model.fit(X_train, y_train)
# This trains the Logistic Regression model using the training features (`X_train`)
# and their corresponding target values (`y_train`).
print("\nLogistic Regression model trained successfully.")
# Prints a confirmation message.

# Make predictions
y_pred = model.predict(X_test)
# This uses the trained model to make predictions on the unseen test features (`X_test`).
# `y_pred` will contain the predicted churn values (0 or 1).

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Imports evaluation metrics from scikit-learn:
# - `accuracy_score`: for calculating overall prediction accuracy.
# - `confusion_matrix`: for creating a matrix showing correct and incorrect predictions.
# - `classification_report`: for a detailed report of precision, recall, and f1-score.

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
# This calculates the accuracy of the model by comparing the true test target values (`y_test`)
# with the predicted values (`y_pred`).
print(f'Accuracy: {accuracy}')
# Prints the calculated accuracy.

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
# This generates the confusion matrix, which summarizes the performance of a classification algorithm.
# It shows the counts of true positives, true negatives, false positives, and false negatives.
print(f'Confusion Matrix:\n{conf_matrix}')
# Prints the confusion matrix.

# Classification Report
target_names = ['Customers who did not churn (i.e., they stayed with the service provider)',
                'Customers who did churn (i.e., they left/changed the service provider)']
# Defines human-readable names for the target classes (0 and 1).
class_report = classification_report(y_test, y_pred, target_names = target_names)
# This generates a detailed classification report, including precision, recall, f1-score,
# and support for each class, using the specified target names.
print(f'Classification Report:\n{class_report}')
# Prints the classification report.
