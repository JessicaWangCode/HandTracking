# HandTracking
This project aims to retrive hand tracking data from Meta Quest2 headset.
## Install and run
1.create 3D environment in VR 

2.install oculus integration 

3.Configure data export file and real time bone display with the following picture. Change the file storage path.

4.Set passthrough Mixed Reality environment with the following video

https://www.youtube.com/watch?v=6hocgJQ10Z8

Press play button to start collecting data
## Simulate with 3D hand point cloud
Run pos_drift_solver.py to fix the position drift problem on the collected data.

Run simulation.py to simulate hand point cloud on a single timestamp.

Run animation.py to show animation on chosen timestamps.

## Simulate with pybullet
Run CleanTheDataSet.py to calculate joint angles for pybullet.

Run main.py to simulate with robotic hand model.
