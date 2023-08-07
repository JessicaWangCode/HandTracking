import pandas as pd
from scipy.spatial.transform import Rotation as R
import numpy as np

def rename_joints(data):
    # Define the old and new names
    old_names = data[' Joint'].unique().tolist()
    new_names = ['Hand_WristRoot', 'Hand_ForearmStub',
                 'Hand_Thumb0', 'Hand_Thumb1', 'Hand_Thumb2', 'Hand_Thumb3',
                 'Hand_Index1', 'Hand_Index2', 'Hand_Index3',
                 'Hand_Middle1', 'Hand_Middle2', 'Hand_Middle3',
                 'Hand_Ring1', 'Hand_Ring2', 'Hand_Ring3',
                 'Hand_Pinky0', 'Hand_Pinky1', 'Hand_Pinky2', 'Hand_Pinky3',
                 'Hand_ThumbTip', 'Hand_IndexTip', 'Hand_MiddleTip', 'Hand_RingTip','Hand_PinkyTip']

    # Create a dictionary mapping old names to new names
    name_dict = dict(zip(old_names, new_names))

    # Replace the old names with the new names
    data[' Joint'] = data[' Joint'].replace(name_dict)

    # Select the columns to keep
    data = data[[' Joint', ' RotationX', ' RotationY', ' RotationZ', ' RotationW']]

    return data


def compute_rotation_angle(data_original):
    # This function will compute the rotation angle between two quaternions
    def rotation_angle(rotation1, rotation2):
        r1 = R.from_quat(rotation1)
        r2 = R.from_quat(rotation2)
        relative_rotation = r2.inv() * r1
        return relative_rotation.magnitude()

    # Create an empty DataFrame to store the computed rotation angles
    rotation_angles = pd.DataFrame(columns=['Name', 'Value'])

    # Compute the number of groups
    num_groups = len(data_original) // 24

    # Get the first group of data
    first_group = data_original.iloc[0:24, :]

    # Compute the rotation angle for each group compared to the first group
    for g in range(1, num_groups):
        group = data_original.iloc[g*24:(g+1)*24, :]
        # Reset the index of the group
        group.reset_index(drop=True, inplace=True)
        for i in range(24):
            rotation1 = first_group.iloc[i, 1:5]
            rotation2 = group.iloc[i, 1:5]
            angle = rotation_angle(rotation1, rotation2)
            new_row = pd.DataFrame({'Name': [first_group.iloc[i, 0]], 'Value': [angle]})
            rotation_angles = pd.concat([rotation_angles, new_row], ignore_index=True)

    return rotation_angles


def transform_data(data):
    # Create a new column 'Group' to identify each group of 24 rows
    data['Group'] = data.index // 24

    # Define the mapping and new column names as before
    mapping = {
        'Hand_Index1': 'FFJ3',
        'Hand_Index2': 'FFJ2',
        'Hand_Index3': 'FFJ1',
        'Hand_Middle1': 'MFJ3',
        'Hand_Middle2': 'MFJ2',
        'Hand_Middle3': 'MFJ1',
        'Hand_Ring1': 'RFJ3',
        'Hand_Ring2': 'RFJ2',
        'Hand_Ring3': 'RFJ1',
        'Hand_Pinky0': 'LFJ5',
        'Hand_Pinky1': 'LFJ3',
        'Hand_Pinky2': 'LFJ2',
        'Hand_Pinky3': 'LFJ1',
        'Hand_Thumb0': 'THJ5',
        'Hand_Thumb1': 'THJ4',
        'Hand_Thumb2': 'THJ2',
        'Hand_Thumb3': 'THJ1',
    }
    columns_new = ['WRJ2', 'WRJ1', 'FFJ4', 'FFJ3', 'FFJ2', 'FFJ1', 'FFtip', 'MFJ4', 'MFJ3', 'MFJ2', 'MFJ1', 'MFtip', 'RFJ4', 'RFJ3', 'RFJ2', 'RFJ1',
                   'RFtip', 'LFJ5', 'LFJ4', 'LFJ3', 'LFJ2', 'LFJ1', 'LFtip', 'THJ5', 'THJ4', 'THJ3', 'THJ2', 'THJ1', 'thtip']

    # Create a new DataFrame to hold the transformed data
    df_new = pd.DataFrame(columns=columns_new)

    # For each group of 24 rows...
    for group, data_grouped in data.groupby('Group'):
        # Create a new row in the new DataFrame
        row_new = pd.Series(index=columns_new)
        # Fill the new row using the original data and the mapping
        for col_new in columns_new:
            if col_new in mapping.values():
                col_original = [k for k, v in mapping.items() if v == col_new][0]
                row_new[col_new] = data_grouped[data_grouped['Name'] == col_original]['Value'].values[0]
            else:
                row_new[col_new] = 0
        # Add the new row to the new DataFrame using pd.concat
        df_new = pd.concat([df_new, pd.DataFrame(row_new).transpose()])

    return df_new


# Call the functions in sequence
data = pd.read_csv('C:/left/grab.csv')
data = rename_joints(data)
data = compute_rotation_angle(data)
df_new = transform_data(data)
df_new.to_csv('C:/left/grab1.csv', index=False)
