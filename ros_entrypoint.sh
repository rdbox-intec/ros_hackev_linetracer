#!/bin/bash
set -e

# setup ros environment
# shellcheck source=/opt/ros/$ROS_DISTRO/setup.bash
source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/catkin_ws/devel/setup.bash"

exec "$@"