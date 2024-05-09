# Notes
-----
Practice Project based on ROS2 For Beginners course.

## Re-build the project after every change
$ colcon build --packages-select my_py_pkg

## Run the node
$ ros2 run my_py_pkg py_node

# Important Tools
-----

## To view the contents of the .bashrc file:
` cat ~/.bashrc `

## To source the workspace
` source ~/.bashrc `

## Press Tab Twice after typing ros2
It will show all the commands that you can use

01 run = To run any package / executable \
02 pkg = To crate the package

## Demo Project
` ros2 run demo_nodes_cpp ` (tab twice)
` ros2 run demo_nodes_cpp talker `


## Custom Package
` ros2 run my_pk_pkg py_node `

## Help
` ros2 run -h `

# Getting basic information about the active node in talker mode
-----

01 Make sure the main node is running

` ros2 run my_py_pkg py_node `

