import argparse
import time
import keyboard

import serial.tools.list_ports
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets


def file_args():
    '''
    Parse through the arguments for running this file.
    Expected, mutually-exclusive arguments: --train1, --train2

    :returns Namespace: the detected argument
    '''
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--train1", action="store_true", help="Choose training stage 1")
    group.add_argument("--train2", action="store_true", help="Choose training stage 2")
    
    return parser.parse_args()


def find_cyton_port():
    '''
    Find the serial port that is connected to the OpenBCI Cyton Board dongle.
    
    :returns str: the device port to which the board is connected
    :raises RuntimeError: raises an exception if port is not found
    '''
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Replace with actual VID and PID for OpenBCI Cyton
        if port.vid == 0x0403 and port.pid == 0x6015:  # Common VID:PID for Cyton (FTDI)
            print(f"OpenBCI Cyton found on port: {port.device}")
            return port.device
    raise RuntimeError("OpenBCI Cyton board not found. Please check the connection.")


def main():
    # Setup Arguments that Specify which Training Stimuli is Being Used
    args = file_args()
    
    # Determine the Settings for the Selected Training
    expected_wait_time = 0
    expected_targets = 0
    if args.train1:
        # Training Stage I Settings
        print("Training Stage 1 selected")
        expected_targets = 8        # 8 stimuli targets
        expected_wait_time = 48     # 1 second trials for each target (each displayed 6 times)
    elif args.train2:
        # Training Stage II Settings
        print("Training Stage 2 selected")
        expected_targets = 32       # 32 stimuli targets
        expected_wait_time = 192    # 1 second trials for each target (each displayed 6 times)
    
    samples_to_collect = 250 * expected_wait_time   # 250 Hz Sampling Rate for Expected Time

    params = BrainFlowInputParams()     # BrainFlow Parameters Initialization
    eeg_data = None

    try:
        # Initialize BrainFlow Connection
        params.serial_port = find_cyton_port()
        board = BoardShim(BoardIds.CYTON_BOARD, params)
        eeg_channels = board.get_eeg_channels(BoardIds.CYTON_BOARD.value)   # Channels from Cyton board for EEG
        
        board.prepare_session()
        board.start_stream()        # begin to collect eeg data in the buffer

        # Wait until Key-Press to Trigger Timer for Data Collection
        # The Stimuli File will Also be Triggered Independently with this Same Key-Press
        print("Hit \"space\" to begin stimuli and data collection")
        keyboard.wait("space")
        time.sleep(expected_wait_time)

        # Get the Last samples_to_collect samples from the Cyton Board Buffer 
        data = board.get_current_board_data(samples_to_collect, BrainFlowPresets.DEFAULT_PRESET)
        eeg_data = data[eeg_channels]   # Get the specific EEG data
        board.stop_stream()
        board.release_session()

    except RuntimeError as e:
        print("USB Connection Error: ", e)
    except Exception as e:
        print("Brainflow Error:", e)
    finally:
        # f = open("./Stage1RawData/test.txt", "w")
        # f.write(", ".join(map(str, eeg_data)))
        # f.close()
        pass

if __name__ == '__main__':
    main()