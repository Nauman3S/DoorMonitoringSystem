<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIan][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Nauman3S/DoorMonitoringSystem">
    <img src="images/door-m-logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Door Monitoring System</h3>

  <p align="center">
    This is an IoT starter project to send phone's accelerometer data to NodeRED over MQTT.
    <br />
   
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![NodeRED Dashboard](images/scr17.png)

There are a number of IoT Starter Projects out there for you to explore. The purpose of this project is to provide you with an easy to use example of an IoT Project with the latest tech-trends in IoT space. This project doesn't require any hardware and make use of your Android Smartphone accelerometer sensor.

How it works?

This project has 3 parts.
* An android smartphone app to collect phone accelerometer data and send it to node-red dashboard over MQTT.
* An MQTT Broker(running on a Ubuntu Server) to receive data from smartphone app and forward it to NodeRED dashboard for visualization.
* A NodeRED app running on IBM Cloud to visualize the accelerometer data in real-time.

Once you run this project succesfully, you will be able to implement same set of instructions on your next IoT project.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This project is built with

* [Android Studio](https://developer.android.com/studio)
* [NodeRED](https://nodered.org/)
* [Mosquitto](https://mosquitto.org/)
* [IBM Cloud](https://www.ibm.com/cloud)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This section provides a set of instructions on how to run this project.

### Prerequisites

This is a list things you need have.

* Android Smartphone
* IBM Cloud Account
* Raspberry Pi(or any linux machine)

### Configuration of Raspberry Pi Gateway Program


Install the requirements using pip,

```sh
$ pip install -r requirements.txt
```

#### Gateway layer

- `gateway_client.py`: Contains code for the gateway client.
- `udp_listener.py`: The code for receiving and parsing [SensorUDP](https://github.com/Nauman3S/DoorMonitoringSystem/blob/main/android_app_sensor_udp/sensor-udp.apk) data sent by the Android device over sockets.
- `main.py`: The script that is supposed to run on raspberry pi as per the tutorial. It uses` gateway_client` and `udp_listener` internally.
- `gateway_config.yml`: This configuration file needs to created by you. Please refer to the tutorial to understand what it should contain.

#### Application layer

- `application.py`: Contains code for the application. The config for this can be provided by creating a file called `app_config.yml` in the same directory. Please refer to the tutorial to understand what this file should contain.
- 
### Configurations of Cloud and Smartphone

1. Install the app in android_app_sensor_upd folder on your smartphone.
2. Make a Classic Ubuntu Server 20.04 instance in your IBM Cloud account and install mosquitto broker on it.
3. Install NodeRED in your IBM Cloud Account
4. Install node-red-dashboard in your NodeRED instance.
5. Import the flow from NodeRED_Dashboard folder of this repository into your NodeRED dashboard.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Install the compiled android app on your Android Phone and in settings page put the public IP address of your Ubuntu Server 20.04 instance as a broker address and in the topic you can put ``data/val/accelerometer`` and then on the homepage of the app you can press start to start sending the data to the dashboard.

You can visulaize the data on the NodeRED dashboard ui page usually at the address ``http://appURL/ui``

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Android App
- [ ] Add iOS App

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Eclipse Public License 1.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

NaumanShakir - [NaumanShakir.com](https://NaumanShakir) - [@Nauman3S](https://twitter.com/Nauman3S) - NaumanShakir3s@gmail.com

Project Link: [https://github.com/Nauman3S/DoorMonitoringSystem](https://github.com/Nauman3S/DoorMonitoringSystem)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Nauman3S/DoorMonitoringSystem
[contributors-url]: https://github.com/Nauman3S/DoorMonitoringSystem/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Nauman3S/DoorMonitoringSystem
[forks-url]: https://github.com/Nauman3S/DoorMonitoringSystem/network/members
[stars-shield]: https://img.shields.io/github/stars/Nauman3S/DoorMonitoringSystem
[stars-url]: https://github.com/Nauman3S/DoorMonitoringSystem/stargazers
[issues-shield]: https://img.shields.io/github/issues/Nauman3S/DoorMonitoringSystem
[issues-url]: https://github.com/Nauman3S/DoorMonitoringSystem/issues
[license-shield]: https://img.shields.io/github/license/Nauman3S/DoorMonitoringSystem
[license-url]: https://github.com/Nauman3S/DoorMonitoringSystem/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/naumanshakir3s
[product-screenshot]: images/scr17.png