# yasm-servermonitor
Yet Another Server Monitor. A simple server monitoring tool built on the Flask web application framework.

![image](https://user-images.githubusercontent.com/1324254/170273975-fa0c632b-c8e3-4733-97a9-657a412fab67.png)

## Introduction
This project does not claim to be a full-featured application or server monitoring solution. There are far more feature-rich tools out there. But instead, this is just a personal excercise in Python and Flask application development. (And I wanted something quick and dirty to check my home lab servers from a small screen or phone.)

> NOTE: If you find this project useful, feel free to use it (under [MIT license](https://github.com/biomekanika/yasm-servermonitor/blob/master/LICENSE)) and maybe even help to improve it by giving me feedback or contributing code. Thanks! :)

### How It Works
YASM Server Monitor relies primarily on sending ICMP Ping requests to check for host availability. As such, target hosts that specifically block ping requests will show as unreachable.

> NOTE: I am looking for more robust means of checking for availability without having to resort to using a custom server solutions that is installed on the target host (like Zabbix for example), but we shall see.

## Getting Started
1. Folder Structure (WIP)

2. Installation process
    
    Before running the application, edit the ```config.yml``` file located in ```./config/``` of the root of the project directory to add target hosts. These can be host names or IP addresses:

    ```
    hosts:
        -
            name: Google
            host: google.com
            port: 
        -
            name: Home Router
            host: 192.168.1.1
            port:
    ```
    > NOTE: As of writing, the ```port``` is an unsued attribute and may be left blank.

    To run the application, simply execute as you would a regular Flask application:

    ```$ flask run```

    The web app will run on default port 80.

3. Software dependencies

    YASM Server Monitor was built on a Debian 11 box using the following:
    - Python 3.9.2
    - Flask 2.1.2
    - PyYAML 5.4.1
    
4. Latest releases

    Version 1.0.0
    - Initial release

5. API References (WIP)

## Build and Test (WIP)
> NOTE: I am currently testing a Docker image build and will publish it as soon as it is ready.