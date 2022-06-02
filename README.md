# dsc_sim_ws

Create a .svl_tests_env

```
# The external IP of the machine running the lgsvl_bridge and ROS2 nodes.
# If you're running the lgsvl_bridge and ROS2 nodes inside of the ADE container,
# then this is the IP of the computer running the container -- if the container
# is inside of WSL2, then it's the IP of the Windows machine.
# Leave this commented out if you're running SVL on the same machine.

# SVL_TESTS__AUTOPILOT_HOST="1.2.3.4"

# The external IP of the machine running the SVL simulator.
# Leave this commented out if you're running SVL on the same machine outside of ADE.
# If you're running SVL on the same machine inside of ADE, set this to "localhost".

SVL_TESTS__SIM_HOST="localhost"

# The GUID for the ego sensor config of the Dallara IL-15.

# IMPORTANT: When creating the configuration, choose the custom `ROS2 Bridge`.
# This must be done manually for your SVL account through the web browser GUI.

SVL_TESTS__EGO_SENSOR_UUID="9b928ff3-2995-487f-815d-3e8c3c768be2"

# The GUID for an `API Only` scenario.

SVL_TESTS__SCENARIO="fabd9f8f-f63f-4e3e-b823-f43b1ffc3a55"
```

Run rosdep install

```
rosdep install --from-paths src --ignore-src -y
```

Then build
```
colcon build
```

Then run
```
ros2 run svl_tests ims_demo
```

To modify objects go to `src/dummy_object_publisher/configs/dummy_3d_publisher_config.json` and change the number of objects or x and y coordinates

Topics of importance

Subscribe:
- `/ego_racecar/odom`: Odometry topic containing position, orientation and linear speeds
- `/dummy_detection`: Vision Detection3D array containing dummy obstacles. 

Publish
- `/drive`: Lgsvl Control message to publish to

