## ros2_control 示例

### 测试使用
- colcon build 编译项目功能包
- ros2 launch controlko_bringup rrbot_sim_gazebo_classic.launch.py (rrbot_sim_gazebo.launch.py 为新版的gazebo)
- ros2 launch test_joint_trajectory_controller.launch.py 启动控制程序，控制两个joint的trajectory运动 （轨迹控制算法， 类似movit2）