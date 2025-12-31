# Coolpad-V1    

<img src="https://github.com/TM1988/Coolpad-V1/blob/main/Assets/Render%20Images/Full%20Case%20Isometric.png?raw=true" width="400">

Coolpad-V1 is a macropad for [Blueprint](https://blueprint.hackclub.com) by [Hack Club](https://hackclub.com)! 

It has a clean 6-key (2x3) layout powered by Seeed Studio XIAO-RP2040 with CircuitPython firmware. It includes a rotary encoder and 0.91" OLED display in a minimalist white box-like case.

This is my first hardware based project so I was kind of clueless half of the time, Shoutout to Hack Club's Slack for all the help!

## Features
- 6 Keys in 2x3 matrix layout
- 2 Part Case + OLED Cover
- Clean white design
- 0.91" 128x64 OLED Screen
- EC11 Rotary Encoder
- Powered by Seeed XIAO-RP2040 Microcontroller
- 60° Angle
- Custom Firmware & App (WIP)

## Challenges
I had no idea how to use KiCad or Fusion 360 so I had to learn both of them. I also had a lot of trouble with fitting the parts and I had to start twice!

## CAD
### How it Works
Designed in [Fusion360](https://www.autodesk.com/products/fusion-360/overview) around an ecport of my KiCad PCB. Case is supposed to be held together with 4 M3x16mm screws and the OLED cover will be glued on? (Might change once I get the parts)

<img src="https://github.com/TM1988/Coolpad-V1/blob/main/Assets/Render%20Images/Full%20Case%20Left.png?raw=true" width="400">

### Parts
- **Bottom case**: Houses PCB & Components
- **Top case**: Switch & Encoder cutouts, Bars to hold the OLED module
- **OLED cover**: Holds the OLED in place and hides OLED PCB

## PCB and Schematic
Designed in [KiCad](https://www.kicad.org/) with 2x3 key matrix.
### Pcb:
<img src="https://github.com/TM1988/Coolpad-V1/blob/main/Assets/Render%20Images/PCB.png?raw=true" width="400">

### Schematic:
<img src="https://github.com/TM1988/Coolpad-V1/blob/main/Assets/Render%20Images/Schematic.png?raw=true" width="400">

### Files
[PCB Design Files](https://github.com/TM1988/Coolpad-V1/tree/main/PCB)

## Firmware
- [x] Basic Firmware (CircuitPython)
- [ ] Basic App (Web/Local) for Macros, Layers, Graphics
- [ ] Automatic Standby Timer
- [ ] Active App Detection for Macros
- [ ] OLED Graphics + Macros Mode
- [ ] More once I think of new things

CircuitPython base running on XIAO-RP2040. I have planned a web/local (haven't decided which) app will handle macro switching, layer control, and app detection, graphics, etc.

[Firmware Files](https://github.com/TM1988/Coolpad-V1/tree/main/Firmware)

## BOM
- 1x - 0.91" OLED Display (I2C: SDA-SCL-VCC-GND)
- 1x - EC11 Rotary Encoder
- 6x - Blank DSA Keycaps
- 6x - Cherry MX Switches
- 1x - Seeed Studio XIAO-RP2040
- 4x - M3x16mm Screws
- 1x - 3D Printed Case (Top + Bottom + OLED Cover)

## More Links

[3D Models](https://github.com/TM1988/Coolpad-V1/tree/main/Assets/3D%20Models) | [Rendered Images](https://github.com/TM1988/Coolpad-V1/tree/main/Assets/Render%20Images)

Most 3D Models of the components can be found [here](https://grabcad.com) (I think)