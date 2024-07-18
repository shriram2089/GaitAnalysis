# GaitAnalysis
Developed a real-time gait analysis system using ESP32 IMU (Inertial Measurement Unit) sensors to capture the coordinates of leg movements and visualize the gait pattern through a Python-based simulation

Components:
ESP32 IMU Sensors:

Used to capture the acceleration, gyroscope, and magnetometer data of the legs.
The sensors are attached to key points on the legs (e.g., thigh, shin, and foot).
ESP32 Microcontroller:

Serves as the main processing unit for the IMU data.
Facilitates wireless communication (e.g., Wi-Fi or Bluetooth) to send the captured data to a computer running the Python simulation.
Python Code:

Processes the incoming IMU data to calculate the coordinates and angles of the legs in real-time.
Provides a graphical simulation of the leg movements, allowing for analysis and visualization of the gait pattern.
Methodology:
1. Hardware Setup:
Attach the ESP32 IMU sensors to the designated points on the legs using straps or adhesive.
Connect the IMU sensors to the ESP32 microcontroller.
Ensure the ESP32 microcontroller is powered and has a reliable wireless connection to the computer.
2. Data Collection:
Initialize the IMU sensors to start collecting raw data (acceleration, gyroscope, and magnetometer).
Use the ESP32 microcontroller to preprocess the data if necessary and transmit it wirelessly to the computer.
3. Data Processing in Python:
Receive the IMU data using a Python script.
Apply sensor fusion algorithms to combine acceleration, gyroscope, and magnetometer data for accurate orientation and positioning.
Calculate the coordinates of the leg joints (e.g., hip, knee, and ankle) based on the orientation and length of the leg segments.
4. Real-Time Simulation:
Use a Python visualization library (e.g., Pygame, Matplotlib, or a custom OpenGL application) to create a graphical representation of the legs.
Continuously update the simulation with the latest coordinates from the IMU data.
Display the gait pattern in real-time, allowing for immediate analysis and adjustments.
