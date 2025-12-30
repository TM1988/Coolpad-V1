import board
import digitalio
import rotaryio
import displayio
import adafruit_displayio_ssd1306
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Pins
keys = [digitalio.DigitalInOut(board.D0), board.D1, board.D2, board.D3, board.D4, board.D5]
for k in keys: k.direction = digitalio.Direction.INPUT; k.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalIO(board.A0, board.A1)  # CLK, DT
switch = digitalio.DigitalInOut(board.A2); switch.pull = digitalio.Pull.UP

# OLED (I2C)
displayio.release_displays()
oled = adafruit_displayio_ssd1306.SSD1306I2C(128, 64, board.I2C(), addr=0x3C)
splash = displayio.Group()
splash.append(displayio.Label(oled.font, text="MACROPAD", x=10, y=30))
oled.show(splash)

k = Keyboard(usb_hid.devices)
layer = 0
mode = "normal"  # normal or graphic

while True:
    # Encoder turn
    if encoder.encoder > 0: layer += 1
    if encoder.encoder < 0: layer -= 1
    encoder.encoder = 0
    
    # Knob click toggle mode
    if not switch.value: mode = "graphic" if mode == "normal" else "normal"
    
    # Keys
    for i, key in enumerate(keys):
        if not key.value:
            k.press(Keycode.ONE + layer % 9)  # 1-9 keys
            k.release_all()
    
    # Update OLED
    splash[0].text = f"Layer: {layer}\nMode: {mode}"
