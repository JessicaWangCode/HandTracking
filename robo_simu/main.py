import os
import pybullet as p
import pybullet_data as pd

import pandas as pds
import time

p.connect(p.GUI)
p.setGravity(0,0,0)

p.setAdditionalSearchPath(pd.getDataPath())
p.resetDebugVisualizerCamera(cameraDistance=0.5,cameraYaw=30,
                             cameraPitch=-30,cameraTargetPosition=[0.5,-0.9,0.75])

handuid=p.loadURDF(os.path.join(pd.getDataPath(),r"C:\scripts\simox_ros-master\sr_grasp_description\urdf\shadowhand.urdf"),useFixedBase=True)
joints = [p.getJointInfo(handuid, i) for i in range(p.getNumJoints(handuid))]
print(joints)

data = pds.read_csv('C:/left/grab1.csv')
dataset = data.values.tolist()

num_joints = p.getNumJoints(handuid)
# Go through each joint and print the name of the joint
for i in range(num_joints):
    joint_info = p.getJointInfo(handuid, i)
    joint_name = joint_info[1]
    print(f"Joint {i} name: {joint_name.decode('utf-8')}")

# Print the initial angle of each joint
for i in range(num_joints):
    joint_info = p.getJointState(handuid, i)
    print(f"Joint {i} angle: {joint_info[0]}")


for data in dataset:
    # In each simulation step, set each joint's target position
    for i, target_position in enumerate(data):
        p.setJointMotorControl2(handuid, i, p.POSITION_CONTROL, targetPosition=target_position)

    # Advance the simulation by one step
    p.stepSimulation()

    # Print the state of each joint and link
    for i in range(num_joints):
        print(f"Joint {i} state: {p.getJointState(handuid, i)}")
        print(f"Link {i} state: {p.getLinkState(handuid, i)}")
    
    # Sleep for a set amount of time (e.g., 0.01 seconds)
    time.sleep(0.001)


