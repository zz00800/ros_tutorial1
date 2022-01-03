# ros_tutorial1
## 실습1 (Turtlesim을 활용한 ROS 기초 프로그래밍)

### To Do

1. 원운동의 회전반경(radius), linear velocity(velocity), 회전방향(direction) 값을 포함하는 ROS 메세지 타입을 정의하고 이 토픽 메세지를 받아 Turtlesim에 속도명령(cmd_vel)을 주는 프로그램을 설계한다. 
2. ros2 launch로 turtlesim과 설계한 프로그램을 동시에 실행할 수 있는 launch 파일을 제작한다. 
3. turtlesim 실행 후, ros2 topic pub으로 새롭게 정의한 메시지 타입을 publish하여 등속 원운동을 명령한다.
4. C++ / Python등의 언어는 자유롭게 선택하여 진행한다.

### Node/Topic 요약!
[Screenshot from 2022-01-03 14-12-57](https://user-images.githubusercontent.com/53456054/147901314-d544720e-c1f0-4d17-b049-e67291879790.png)
velocity, radius, direction을 파라미터로 받아와 조정 가능
