import numpy as np
import pandas as pd
from scipy.linalg import svd

def clean_csv(input_file):
    # Read the input CSV file
    data = pd.read_csv(input_file)
    timestamps = data.iloc[:, 0].values
    positions = data.iloc[:, 2:5].values

    # Clean the data (subtract the first line from each subsequent line for each timestamp)
    for i in range(len(timestamps)):
        start_indices = np.where(timestamps >= timestamps[i])[0]
        target_positions = positions[start_indices, :]
        positions[start_indices, :] = target_positions - target_positions[0, :]

    # Prepare the cleaned data
    cleaned_data = np.column_stack([timestamps, positions])
    return cleaned_data


def rotate_positions(data):
    timestamps = data[:, 0]
    positions = data[:, 1:4]

    # Get unique timestamps
    unique_timestamps = np.unique(timestamps)

    # Select the first timestamp as the reference
    reference_timestamp = unique_timestamps[0]
    reference_positions = positions[timestamps == reference_timestamp, :]

    # Initialize rotated positions
    rotated_positions = np.zeros_like(positions)

    # Loop through unique timestamps
    for i in range(1, len(unique_timestamps)):  # start from the second timestamp
        # Select current timestamp
        target_timestamp = unique_timestamps[i]

        # Get the positions for the current timestamp
        target_positions = positions[timestamps == target_timestamp, :]

        # Compute the covariance matrix
        covariance_matrix = target_positions.T @ reference_positions

        # Perform Singular Value Decomposition (SVD) on the covariance matrix
        U, _, V = svd(covariance_matrix)

        # Compute the rotation matrix
        rotation_matrix = V @ U.T

        # Rotate the target point cloud
        rotated_target_positions = (rotation_matrix @ target_positions.T).T

        # Store the rotated positions
        rotated_positions[timestamps == target_timestamp, :] = rotated_target_positions

    return rotated_positions


def clean_and_rotate_csv(input_file, rotated_file):
    # Clean data
    cleaned_data = clean_csv(input_file)

    # Rotate positions
    rotated_positions = rotate_positions(cleaned_data)

    # Write rotated positions to a new CSV file
    cleaned_and_rotated_data = np.column_stack([cleaned_data[:, 0], rotated_positions])
    
    # Convert the data to a DataFrame and add column names
    df = pd.DataFrame(cleaned_and_rotated_data, columns=['timestamp', 'x', 'y', 'z'])
    
    # Write the DataFrame to a CSV file
    df.to_csv(rotated_file, index=False)


# Example usage:
input_file = 'C:/left/count7-9.csv'
rotated_file = 'C:/left/rotated_count7-9.csv'
clean_and_rotate_csv(input_file, rotated_file)
