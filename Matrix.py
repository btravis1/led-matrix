import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# ----- PIN SETUP -----
rows = [5, 6, 13, 19, 26]
cols = [12, 16, 20, 21, 25]

button_pin = 17
ldr_pin = 27  # simple digital light sensor

for r in rows:
    GPIO.setup(r, GPIO.OUT)
    GPIO.output(r, 0)

for c in cols:
    GPIO.setup(c, GPIO.OUT)
    GPIO.output(c, 1)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ldr_pin, GPIO.IN)

# ----- BRIGHTNESS -----
def get_delay():
    if GPIO.input(ldr_pin) == 0:
        return 0.002  # bright room
    else:
        return 0.006  # dark room

# ----- DISPLAY FUNCTION -----
def display(pattern, duration=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        delay = get_delay()
        for r in range(5):
            GPIO.output(rows[r], 1)
            for c in range(5):
                GPIO.output(cols[c], not pattern[r][c])
            time.sleep(delay)
            GPIO.output(rows[r], 0)

# ----- PATTERNS -----
heart1 = [
    [0,1,0,1,0],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [0,0,1,0,0],
]

heart2 = [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
]

smiley = [
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [1,0,0,0,1],
    [0,1,1,1,0],
]

# Simple font for scrolling text
letters = {
    "H": [
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
    ],
    "E": [
        [1,1,1],
        [1,0,0],
        [1,1,0],
        [1,0,0],
        [1,1,1],
    ],
    "L": [
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,1,1],
    ],
    "O": [
        [1,1,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,1,1],
    ]
}

def scroll_text(text):
    columns = []

    for char in text:
        if char in letters:
            for col in zip(*letters[char]):
                columns.append(list(col))
            columns.append([0,0,0,0,0])

    for i in range(len(columns) - 4):
        frame = []
        for r in range(5):
            row = []
            for c in range(5):
                row.append(columns[i+c][r])
            frame.append(row)
        display(frame, 0.1)

# ----- MODES -----
mode = 0
last_button = 1

try:
    while True:
        button = GPIO.input(button_pin)

        if button == 0 and last_button == 1:
            mode = (mode + 1) % 3
            time.sleep(0.3)

        last_button = button

        if mode == 0:
            display(heart1, 0.3)
            display(heart2, 0.3)

        elif mode == 1:
            display(smiley, 1)

        elif mode == 2:
            scroll_text("HELLO")

finally:
    GPIO.cleanup()
