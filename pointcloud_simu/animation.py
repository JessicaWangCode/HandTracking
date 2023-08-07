

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load your data
data = pd.read_csv("C:/left/rotated_count0-9.csv")  # replace "your_file.csv" with your actual file name
timestamps = data["timestamp"].unique()  # replace "timestamp" with your actual timestamp column name

# Joint names
#joint_names = ['Hand_WristRoot', 'Hand_ForearmStub', 'Hand_Thumb0', 'Hand_Thumb1', 'Hand_Thumb2', 'Hand_Thumb3',
               #'Hand_Index1',
               #'Hand_Index2', 'Hand_Index3', 'Hand_Middle1', 'Hand_Middle2', 'Hand_Middle3',
               #'Hand_Ring1', 'Hand_Ring2', 'Hand_Ring3', 'Hand_Pinky0', 'Hand_Pinky1', 'Hand_Pinky2',
               #'Hand_Pinky3', 'Hand_ThumbTip', 'Hand_IndexTip', 'Hand_MiddleTip', 'Hand_RingTip', 'Hand_PinkyTip']
# Define the connection order
connections = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 8), (1, 9),
               (9, 10), (10, 11), (1, 12), (12, 13), (13, 14), (1, 15), (15, 16), (16, 17),
               (17, 18), (5, 19), (8, 20), (11, 21), (14, 22), (18, 23)]  # Update this with your actual connections

# Create the 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the axes limits
ax.set_xlim([-0.15, 0.15])
ax.set_ylim([-0.15, 0.15])
ax.set_zlim([-0.15, 0.15])

# Initialize the scatter plot
scat = ax.scatter([], [], [])

# Initialize the line objects
lines = [ax.plot([], [], [])[0] for _ in connections]

# Initialize the text objects
texts = [ax.text(0, 0, 0, '') for _ in range(24)]

# Animation update function
def update(frame):
    # Get the data for this frame
    frame_data = data[data["timestamp"] == timestamps[frame]]
    positions = frame_data[["x", "y", "z"]].values

    # Update the scatter plot
    scat._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])

    # Update the line objects
    for (start, end), line in zip(connections, lines):
        line.set_data(positions[[start, end], 0], positions[[start, end], 1])
        line.set_3d_properties(positions[[start, end], 2])

    # Update the text objects
    for pos, text in zip(positions, texts):
        text.set_position(pos[:2])
        text.set_3d_properties(pos[2], 'z')
        # text.set_text(name)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(len(timestamps)), interval=100)

# Display the animation
plt.show()
 
