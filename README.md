# Smart Keylogger

Smart Keylogger is a simple keylogger tool written in Python using the `pynput` library. It captures and logs keystrokes to a file for monitoring purposes. This tool supports both Linux and Windows platforms.

## Features

- Logs keystrokes to a text file.
- Supports both Linux and Windows.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Visual Studio Code (VS Code) installed (optional, but recommended).
- `pynput` library.

### Linux Installation

1. **Install Dependencies:**
   Ensure `pynput` is installed. If not, you can install it using `apt`:

   ```
   sudo apt update
   sudo apt install python3-pynput
   
### Alternatively, you can use pip:

  ```
  pip install pynput
  ```
### Clone the Repository:

```
git clone https://github.com/nagrajnaik1416/Smart-Keylogger.git

cd Smart-Keylogger
```

### Run the Keylogger:

```
python3 smartkeylogger.py
```

### Stopping the Keylogger: 

To stop the keylogger, press the `ESC` key.

## Windows Installation

### Install Dependencies:
- Install `pynput` using `pip`:

```
pip install pynput
```
- Clone the Repository:
  Open VS Code and use the integrated terminal to clone the repository:

```
git clone https://github.com/nagrajnaik1416/Smart-Keylogger.git
cd Smart-Keylogger
```

- Open the Project in VS Code:

  Open Visual Studio Code.

  Go to `File` -> `Open Folder` and select the `Smart-Keylogger` directory you just cloned.

- Run the Keylogger:

 In VS Code, open the integrated terminal (`Ctrl + ``) and run:
```
python smartkeylogger.py
```
- Stopping the Keylogger:
  
  To stop the keylogger, press the `ESC` key.

## Packaging (Optional):
You can package the script into an executable using PyInstaller for easier deployment.

### Install PyInstaller:

```
pip install pyinstaller
```

### Create an Executable:

```
pyinstaller --onefile smartkeylogger.py
```

The executable will be located in the `dist` directory.

##Using the Executable Remotely:

Once you have created the executable using PyInstaller, you can deploy and use it remotely. Here’s how you can do it:

### Transfer the Executable:

Windows: Copy the executable from the `dist` directory to the remote machine using methods such as email, cloud storage (e.g., Google Drive, Dropbox), or file transfer tools (e.g., SCP, FTP).
- Linux: Use scp, rsync, or any other file transfer method to move the executable to the remote machine.

#### Run the Executable:

- Windows: On the remote machine, double-click the executable or run it from the command prompt.

- Linux: Make the executable file executable if necessary:

```
chmod +x smartkeylogger
```

### Then run it:

```
./smartkeylogger
```

### Monitoring:

The keylogger will create and update the key_log.txt file in the same directory where the executable is run. Ensure you have access to this file for monitoring.

#### Stopping the Keylogger: To stop the keylogger, press the `ESC` key.


## Usage:

- The keylogger logs keystrokes to `key_log.txt`.
- The log file will be updated in real-time as keys are pressed.

## Legal and Ethical Considerations
- Permission: Ensure you have explicit permission to run this keylogger on any computer.
- Compliance: Follow all local laws and regulations regarding privacy and monitoring.

  
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
If you have suggestions or improvements, please submit a pull request or open an issue.

## Contact
For any questions or support, contact nagrajnaik657@gmail.com or open an issue on the GitHub repository page.
