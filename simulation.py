# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:49:11 2023

@author: sz21463
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Reading data from csv file
data = np.genfromtxt('C:/left/rotated_count7-9.csv', delimiter=',')
timestamps = data[:, 0]
positions = data[:, 1:4]

# Select a specific timestamp to plot
target_timestamp = 15.949

# Find the index of the target timestamp
target_index = np.where(timestamps == target_timestamp)[0]

# Get the positions for the target timestamp
target_position = positions[target_index, :]

joint_names = [
    'Hand_WristRoot', 'Hand_ForearmStub', 'Hand_Thumb0', 'Hand_Thumb1', 'Hand_Thumb2', 'Hand_Thumb3', 'Hand_Index1',
    'Hand_Index2', 'Hand_Index3', 'Hand_Middle1', 'Hand_Middle2', 'Hand_Middle3',
    'Hand_Ring1', 'Hand_Ring2', 'Hand_Ring3', 'Hand_Pinky0', 'Hand_Pinky1', 'Hand_Pinky2',
    'Hand_Pinky3', 'Hand_ThumbTip', 'Hand_IndexTip', 'Hand_MiddleTip', 'Hand_RingTip', 'Hand_PinkyTip'
]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(target_position[:, 0], target_position[:, 1], target_position[:, 2])

# Display joint names
for i in range(len(joint_names)):
    ax.text(target_position[i, 0], target_position[i, 1], target_position[i, 2], joint_names[i])

# Plot connections
connections = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 8), (1, 9),
               (9, 10), (10, 11), (1, 12), (12, 13), (13, 14), (1, 15), (15, 16), (16, 17),
               (17, 18), (5, 19), (8, 20), (11, 21), (14, 22), (18, 23)]

for connection in connections:
    ax.plot([target_position[connection[0], 0], target_position[connection[1], 0]],
            [target_position[connection[0], 1], target_position[connection[1], 1]],
            [target_position[connection[0], 2], target_position[connection[1], 2]], 'k-')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Hand Joint Positions at Timestamp: {target_timestamp}')
ax.grid(True)
plt.show()
