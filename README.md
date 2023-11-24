# HandTracking
This project aims to retrive hand tracking data from Meta Quest2 headset.
## Install and run
1.create a 3D environment project in Unity.

2.Install oculus integration.

3.Configure data export file and real time bone display with the following picture. Change the file storage path.
![Image text](https://user-images.githubusercontent.com/78681139/258791096-8a1c00eb-508e-42cc-8794-871f1ac857b9.png)​​​)
![Image text](https://user-images.githubusercontent.com/78681139/258790886-91df5a8c-60b9-4369-994b-2f91bec450a9.png))

4.Set passthrough Mixed Reality environment with the following video.

https://www.youtube.com/watch?v=6hocgJQ10Z8

5. Use Windows, Mac, Linus build. Make sure using the following settings. Now press play button to start collecting data.
![Image text]([https://user-images.githubusercontent.com/78681139/258791096-8a1c00eb-508e-42cc-8794-871f1ac857b9.png](https://github.com/JessicaWangCode/HandTracking/assets/78681139/2b65d374-2562-4f0b-bd25-75dcb3bb182e))​​​)
![Image text](https://user-images.githubusercontent.com/78681139/258790886-91df5a8c-60b9-4369-994b-2f91bec450a9.png))
## Simulate with 3D hand point cloud
open pointcloud_simu file

Run pos_drift_solver.py to fix the position drift problem on the collected data.

Run simulation.py to simulate hand point cloud on a single timestamp.

Run animation.py to show animation on chosen timestamps.

![Image text](https://user-images.githubusercontent.com/78681139/258797009-6589935b-3bb4-4a52-a3ed-1fbe2800d9bc.png))
## Simulate robot hand with pybullet
Open robo_simu file

Run CleanTheDataSet.py to calculate joint angles for pybullet.

Run main.py to simulate with robotic hand model.

![Image text](https://user-images.githubusercontent.com/78681139/258797028-77e228e8-4721-4068-a170-8101a9cc0e22.png)
