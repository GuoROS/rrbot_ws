## ros2_control 示例

### 测试使用
- colcon build 编译项目功能包
- ros2 launch controlko_bringup rrbot_sim_gazebo_classic.launch.py (rrbot_sim_gazebo.launch.py 为新版的gazebo)
- ros2 launch test_joint_trajectory_controller.launch.py 启动控制程序，控制两个joint的trajectory运动 （轨迹控制算法， 类似movit2）


### hardware_interface  on_init()
- hardware_interface 中 on_init() 函数传入的 HardwareInfo &info 用来保存ros2_control的xacro文件中硬件资源的信息
- info通过resource manager初始化传递参数给它
- RRBotHardwareInterface 继承了 SystemInterface，里面有一个可以被子类继承的info_（通过hardware_info传递），所以RRBotHardwareInterface可以使用info_


### hardware_interface  on_configure()
- 初始化和硬件通信的代码
- 
