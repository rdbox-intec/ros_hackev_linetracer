FROM rdbox/ros-core-catkinws:noetic

LABEL maintainer="INTEC Inc<info-rdbox@intec.co.jp>"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                                    python3-pip && \
    apt autoclean -y && \
    apt autoremove -y && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

COPY ./ros_hackev_linetracer /catkin_ws/src/ros_hackev_linetracer

COPY ./r2s2_for_rostest /catkin_ws/src/r2s2_for_rostest
RUN pip3 install -r /catkin_ws/src/r2s2_for_rostest/requirements.txt

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \
                cd /catkin_ws && \
                catkin_make"

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["roslaunch", "--screen", "--wait", "ros_hackev_linetracer", "linetracer.launch", "white:=80.0", "black:=20", "kp:=1.8", "ki:=1.67", "kd:=0.0324", "td:=0.027", "power:=10"]