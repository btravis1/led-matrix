# 5x5 LED Matrix with Raspberry Pi

A simple 5x5 LED matrix project built using a Raspberry Pi. This project demonstrates how to control multiple LEDs using GPIO pins, create animations, display scrolling text, and add button interaction.

## 🚀 Features

* 5x5 LED matrix control
* Scrolling text display (e.g. "HELLO")
* LED animations (including a beating heart)
* Button-controlled modes
* Clean and compact design (with optional 3D printed case)

## 🧰 Hardware Used

* Raspberry Pi
* 25x LEDs
* Resistors
* Breadboard & jumper wires
* Push buttons
* (Optional) 3D printed case

## 💻 Software

* Python (GPIO control)
* Runs on Raspberry Pi OS

## ⚡ How It Works

The LEDs are arranged in a matrix layout, allowing rows and columns to be controlled efficiently using GPIO pins. The code cycles through rows quickly (multiplexing) to create the illusion that multiple LEDs are on at once.

## 📦 Setup

1. Clone this repository
2. Wire the LED matrix according to the diagram
3. Run the Python script:

   ```bash
   python main.py
   ```

## 🎮 Controls

* Button 1: Change animation
* Button 2: Toggle scrolling text

## 📂 Files

* `main.py` → Main program
* `animations.py` → LED patterns and effects
* `wiring_diagram.png` → Circuit layout
* `case.stl` → 3D printable enclosure

## 📸 Demo

(Add images or a link to your YouTube video here)

## 🔧 Future Improvements

* Add brightness control
* Add more animations
* Add sensor input (light or sound)

## 📜 License

This project is open-source and free to use.

---

Made as a fun electronics + coding project 🚀
