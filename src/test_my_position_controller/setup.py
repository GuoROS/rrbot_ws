from setuptools import find_packages, setup

package_name = 'test_my_position_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gbb',
    maintainer_email='691452980@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "rrobot_position_pub=test_my_position_controller.rrobot_position_pub:main",
            "rrobot_position_sub=test_my_position_controller.rrobot_position_sub:main",

        ],
    },
)
