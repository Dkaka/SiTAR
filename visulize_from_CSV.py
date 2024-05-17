# # Import necessary libraries
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load the data from CSV
# df_results = pd.read_csv('results100.csv')  # Replace 'results2.csv' with your actual file name if different

# # Assuming your DataFrame df_results includes columns like 'error_1-2', 'error_2-3', etc.
# error_columns = [col for col in df_results.columns if 'error_' in col and col != 'error_mean']

# # Setup the plot
# plt.figure(figsize=(14, 7))
# # Choosing a uniform color, e.g., 'blue', and setting marker size with 's'
# for i, col in enumerate(error_columns):
#     plt.scatter(range(len(df_results)), df_results[col], color='blue', label=col, s=10)  # s is the size of the dot

# plt.title('Error Scatter Plot for Different Trajectory Pairs')
# plt.xlabel('Row Index')
# plt.ylabel('Error')
# plt.legend(title='Trajectory Pairs', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.grid(True)
# plt.show()

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from CSV
df_results = pd.read_csv('results100.csv')  # Replace 'results2.csv' with your actual file name if different

# Assuming your DataFrame df_results includes columns like 'error_1-2', 'error_2-3', etc.
error_columns = [col for col in df_results.columns if 'error_' in col and col != 'error_mean']

# Setup the plot
plt.figure(figsize=(12, 8))

# Initialize lists to collect all x and y values for the histogram
x_vals = []
y_vals = []

# Loop through each row and collect each error value at the corresponding x-coordinate
for index, row in df_results.iterrows():
    x = index + 1  # Adding 1 to start x-coordinates from 1
    y = row[error_columns].values  # Extract the error values for the row
    if not np.isnan(y).any():  # Check for NaN values
        x_vals.extend([x] * len(y))
        y_vals.extend(y)

# Ensure there are no NaN values in the data
if np.isnan(x_vals).any() or np.isnan(y_vals).any():
    raise ValueError("Data contains NaN values, please clean your data.")

# Determine the range for the histogram to avoid automatic detection issues
x_min, x_max = min(x_vals), max(x_vals)
y_min, y_max = min(y_vals), max(y_vals)
print(len(df_results))
# Create the 2D histogram
plt.hist2d(x_vals, y_vals, bins=[len(df_results), 50], range=[[x_min, x_max], [y_min, y_max]], cmap='viridis', density=True)
cb = plt.colorbar()
cb.set_label('Density')

plt.title('2D Histogram of Error Density Across Indices')
plt.xlabel('Index')
plt.ylabel('Error Magnitude')
plt.grid(True)
plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import gaussian_kde

# # Load the data from CSV
# df_results = pd.read_csv('results100.csv')  # Replace 'results2.csv' with your actual file name if different

# # Assuming your DataFrame includes columns like 'error_1-2', 'error_2-3', etc.
# error_columns = [col for col in df_results.columns if 'error_' in col and col != 'error_mean']

# # Preparing to plot
# n_rows = len(df_results)
# results = []

# # Creating a more targeted grid for KDE based on data's actual spread
# data_range = df_results[error_columns].stack().dropna()
# if data_range.empty:
#     raise ValueError("No valid data points to plot.")
# x_min, x_max = data_range.quantile(0.01), data_range.quantile(0.99)
# x_grid = np.linspace(x_min, x_max, 1000)

# # Compute 1D KDE for each row and store results
# for index, row in df_results.iterrows():
#     data = row[error_columns].dropna()
#     if data.size > 1:
#         kde = gaussian_kde(data)
#         results.append(kde(x_grid))
#     else:
#         results.append(np.zeros_like(x_grid))  # Fill with zeros if not enough data

# # Ensuring we have data to plot
# if not results:
#     raise ValueError("No KDE results were generated.")

# # Plotting
# plt.figure(figsize=(12, 8))
# plt.imshow(np.rot90(np.array(results),1), cmap='viridis')

# # plt.imshow(np.array(results), extent=[x_min, x_max, 0, n_rows], aspect='auto', origin='lower', cmap='viridis')
# plt.colorbar(label='Density')
# plt.title('Stacked KDE of Error Distributions Across Rows')
# plt.xlabel('Error Magnitude')
# plt.ylabel('Row Index')
# plt.show()
