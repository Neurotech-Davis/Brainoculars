## Training
This directory contains files related to training data. Instructions for each training stage, as well as dependencies, can be found below.

### Stage I Data Collection Instructions
It is important you follw the below steps carefully.
1. Open the PsychoPy Coder
2. Click the "Open File" icon on the top-left of the task bar (it should be a folder icon)
3. Open the Brainoculars/Stimuli/Stage1Training/stage1train.py folder
4. Now in your terminal, navigate to the Brainoculars folder
5. Connect the OpenBCI Cyton board Dongle the computer conducting this experiment
    - Ensure the dongle switch is set to GPIO6
    - Ensure the Cyton board is powered on and the switch is set to BLE
6. Enter the command ```python .\Training\collect_training_data.py --train1```
7. If everything is working as expected, you will receive a prompt that you do NOT yet follow.
    - A red LED on the Cyton dongle under TXD indicates it is currently communicating with the board
8. Go back to the PsychoPy Coder
9. Hit the green "Run in Python" play button at the top of the taskbar and wait for the stimuli to load
10. Once you see the 8 flashing regions, you will be able to hit "enter/return" to begin the data collection
    - You only need to do this once, as both the stimuli and data collection files are listening for this input
    - Please be aware that the key-press is detected from anywhere, so you must follow these instructions step-by-step to avoid pressing it on accident

### Stage II Data Collection Instructions

### Dependencies
You will need the following modules to properly collect data. Check if 
they are installed by running ```pip list``` in your terminal.
If the libraries are not installed, run the commands following them
* BrainFlow
    - ```pip install brainflow```
* Keyboard
    - ```pip install keyboard```
* PySerial
    - ```pip install pyserial```

You will also need to install the PyschoPy software to display the stimuli.