import os
import sys
import io
import M5
from M5 import *
import random
import time

# Global widget variables
ANY8BALL = None
FortuneCircle = None
Line1 = None
Line2 = None
Press = None
fortune_label = None
countdown_label = None
clear_fortune_timer = None
countdown_value = None
batteryLabel = None

fortunes = [
    "Yes", "No", "Ask again", "For Sure", "Hell NO",
    "IDK", "Maybe",
]

def setup():
    global ANY8BALL, FortuneCircle, Line1, Line2, Press, fortune_label, countdown_label, batteryLabel

    M5.begin()

    # Initialize UI elements
    ANY8BALL = Widgets.Label("ANY-8BALL", 19, 8, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
    FortuneCircle = Widgets.Circle(67, 113, 63, 0xffffff, 0x000000)
    Line1 = Widgets.Rectangle(-15, 33, 151, 2, 0xffffff, 0xffffff)
    Line2 = Widgets.Rectangle(-6, 198, 151, 2, 0xffffff, 0xffffff)
    Press = Widgets.Label("Press M5 For Fortune", 8, 213, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
    fortune_label = Widgets.Label("", 30, 105, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
    countdown_label = Widgets.Label("", 5, 180, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)
    batteryLabel = Widgets.Label("Power", 100, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu9)

def update_battery_display():
    global batteryLabel
    battery_level = Power.getBatteryLevel()
    batteryLabel.setText(f"{battery_level}%")
    
    # Set text color based on battery level
    if battery_level >= 80:
        batteryLabel.setColor(0x00FF00)  # Green
    elif battery_level >= 50:
        batteryLabel.setColor(0xFFFF00)  # Yellow
    elif battery_level >= 30:
        batteryLabel.setColor(0xFFA500)  # Orange
    else:
        batteryLabel.setColor(0xFF0000)  # Red

def loop():
    global fortune_label, countdown_label, clear_fortune_timer, countdown_value

    # Update battery display
    update_battery_display()

    # When the button is pressed, start or restart the countdown
    if M5.BtnA.wasPressed():
        selected_fortune = random.choice(fortunes)
        fortune_label.setText(selected_fortune)
        countdown_value = 2  # Set countdown to 2 seconds
        clear_fortune_timer = time.ticks_ms() + 2000  # 2000 milliseconds = 2 seconds

    # Update countdown and handle timer expiration
    if clear_fortune_timer:
        remaining_time = clear_fortune_timer - time.ticks_ms()
        if remaining_time > 0:
            countdown_value = remaining_time // 1000  # Convert milliseconds to seconds
        else:
            countdown_value = None

    # Display countdown or clear the label when time is up
    if countdown_value is not None:
        countdown_label.setText(f"{countdown_value}s")
    else:
        countdown_label.setText("")

    if clear_fortune_timer and time.ticks_ms() > clear_fortune_timer:
        fortune_label.setText("")
        countdown_label.setText("") 
        clear_fortune_timer = None  # Reset the timer
        countdown_value = None  # Ensure countdown value is reset

    M5.update()

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("Please update to the latest firmware")
