ANY8BALL Application for M5StickC PLUS 2
A Product of ANYD3V of A Red Light Studio

Description
The ANY8BALL application is a fun and interactive project for the M5StickC PLUS 2, simulating a magic 8-ball that provides random fortunes when a button is pressed. It also displays the current battery level, changing color based on the battery percentage.

Features
Displays a random fortune when the M5 button is pressed.
A countdown timer shows how long the fortune will be displayed.
Battery level is displayed and color-coded:
Green for 80% and above
Yellow for 50% to 79%
Orange for 30% to 49%
Red for below 30%

Requirements
M5StickC PLUS 2
M5Stack library for MicroPython
Installation
Clone the Repository

Install from M5Burner

Refer to M5Stick C Plus 2 links for the M5Burner app for Linux, MacOS and Windows. This is the official tool to install UIFlow and other official firmware. Latest updates will be there and UIFlow.

1. Launch M5Burner
2. Select "StickC" from the menu on the left.
3. Use the search at the top of the app to look for "ANy-8Ball". Official upload is by "AnyD3v".
4.Click Download
5. Click Burn


Also available on UIFLOW 2.0
https://uiflow2.m5stack.com/?pkey=0a4f9f4186bd408cb9b7e4553cfd5894



Add Resources

Ensure that the image file Any-8Ball.png is available in the res/img/ directory on your device.

Usage
Power on the M5StickC PLUS 2.
Press the M5 button to display a random fortune.
The fortune will be shown for 2 seconds, after which it will clear automatically.

NOTE: UIFLOW version has battery display, M5launcher version currently does not but has dim display using Button B. Both versions are currently being developed to match and include more features in version 1.1.

Code Explanation
setup(): Initializes the UI elements, including the fortune display and battery level.
update_battery_display(): Updates the battery label and color based on the battery level.
loop(): Handles button presses to show fortunes and manage the countdown timer.


Attribution
This project is a product of ANY-D3V of A Red Light Studio.
