# ros2_control 示例

## 测试使用
- colcon build 编译项目功能包
- ros2 launch controlko_bringup rrbot_sim_gazebo_classic.launch.py (rrbot_sim_gazebo.launch.py 为新版的gazebo)
- ros2 launch test_joint_trajectory_controller.launch.py 启动控制程序，控制两个joint的trajectory运动 （轨迹控制算法， 类似movit2）

## hardware_interface 解读
### on_init()
- hardware_interface 中 on_init() 函数传入的 HardwareInfo &info 用来保存ros2_control的xacro文件中硬件资源的信息
- info通过resource manager初始化传递参数给它
- RRBotHardwareInterface 继承了 SystemInterface，里面有一个可以被子类继承的info_（通过hardware_info传递），所以RRBotHardwareInterface可以使用info_


### on_configure()
- 初始化和硬件通信的代码
- 例子中DrDenisRRBotComms是假装控制一个机械臂，用一个数组【0.0, 0.0】去进行控制机械臂的joint的角度位置


### export_state_interfaces()
- 初始化state_interface 实际的代码类
- sensor中是包含了所有的state_interface, 长度为6,
- StateInterface 继承了 ReadOnlyHandle类，对应实际的StateInterface，get_name(),get_value()
- get_value()传递的是一个指针，在外部改变值的时候，StateInterface也会体现
- export_state_interfaces返回的state_interfaces值，由指针返回给StateInterface类，同时在外部改变指针的值，StateInterface也会改变。 
- StateInterface里的值传递给resource manager，再暴露给controller，这样controller就可以读取对应的值


### export_command_interfaces()
- 初始化 CommandInterface，与export_state_interfaces类似
- CommandInterface继承ReadWriteHandle类， ReadWriteHandle继承ReadOnlyHandle类，多一个set_value()

### 可选 prepare_command_mode_switch() perform_command_mode_switch()
- 控制state_interfaces和command_interfaces的开关，切换 控制模式

### on_activate()
- 激活硬件，并工作 

### on_deactivate() shut_down()


### read() 和 write()
- 按频率定时调用 读取和写入
- read读取硬件数据，放入到StateInterface类
- write读取改变好的 CommandInterface的值，写入到硬件