# Wyrestorm Matrix Switcher Python Script
This Python script will facilitate sending commands to a Wyremstorm MXV-0808-H2A unit by running this Python script in the console. Other capabilities are possible but not tested. 

## Requirements
The following is required to run the script
- Python v3.12
- telNet

Note: The Version of Python is important. In V3.13, Python removed the Telnet library, and instead, they suggest you install telnetlib3 separately. To limit the number of items to install, this script chooses to use the original telnetlib library

### Installing Python v3.12
link: https://www.python.org/downloads/release/python-31210/

Use the above link to download the appropriate installer. 

### Enabling Telnet(Windows)
Source w/ images: https://www.makeuseof.com/enable-telnet-windows/

#### 1. Enable Telnet on Windows using the Control Panel
You can enable Telnet Client using the Classic Control Panel. Since it is an optional feature, you can enable it using the Windows Optional Feature dialog. You can use it add or remove other users' optional features on Windows.

To enable Telnet Client using the Control Panel:

1. Press Win + R to open Run.
2. Type control and click OK to open Control Panel.
3. In Control Panel, Click on Uninstall a Program under Programs and Features.
4. In the left pane, click on the Turn Windows feature on or off.
5. In the Windows Features dialog, scroll down and select Telnet Client.
6. Click OK and wait for the feature to install. Once installed, restart your PC to apply the changes and enable the feature.

If you need to disable Telnet:

1. Open the Windows Features dialog and unselect Telnet Client.
2. Click OK and wait for the feature to uninstall.
3. Click on Restart now to reboot your PC and apply the changes.

#### 2. Enable Telnet Client using Windows PowerShell
1. Press Win + X to open the WinX menu.
2. Click on Windows Terminal(Admin) and click Yes to open the terminal app as administrator. If you are using Windows 10, type PowerShell in Windows Search and open Windows PowerShell administrator.
3. In the PowerShell window, type the following command and press Enter to enable Telnet:
```
Enable-WindowsOptionalFeature -Online -FeatureName TelnetClient
```
4. This process may take several minutes, so wait for it to complete and return a status report. If successful, you’ll see the result as Online:True.
5. If you want to disable Telnet Client, use the following command instead:
```
Disable-WindowsOptionalFeature -Online -FeatureName TelnetClient
```
6. Close PowerShell and restart your PC.

#### 3. Install Telnet Client Using Command Prompt
If you prefer Command Prompt over PowerShell, you can use the DISM /Online command to enable the optional features on your Windows 11 computer.

Follow these steps to install Telnet using Command Prompt:

1. Press the Win key and type cmd.
2. Right-click on Command Prompt and select Run as administrator.
3. In the Command Prompt window, type the following command and press Enter:
```
dism /online /Enable-Feature /FeatureName:TelnetClient
```
4. Command Prompt will start enabling the feature and display the operation completed successfully message.
5. If you need to disable Telnet, type the following command and press Enter:
```
dism /Online /Disable-Feature /FeatureName:TelnetClient
```
6. Wait for the success message.
7. Type exit and press Enter to close Command Prompt.

## Config
Before this script can be used, you must modify the config file.
**IP:** This is the IP Address of the Wyrestorm machine. REQUIRED.
**PORT:** This is the Port of the Wyrestorm. Currently, it's set to the default port and should not need to be changed.

## How to use
Using this script is super simple. Use the following line PowerShell
```
py "C:\path\to\file\WyrestormTelnet.py" <Prompt> <Arguments>
```
example:
```
py "C:\path\to\file\WyrestormTelnet.py" VIDEO 4 5
```
This line will set output 5 to input 4

### Available Prompts
#### VIDEO
Takes 2 arguments. Sets Output #<Output> to HDMI Input <Input>.
```
VIDEO <Input> <Output>
```
Each argument must be a whole number(Integer) between 0 and 8 inclusive.
**Input:** 0 turns the output off. 1-8 sets the output to that HDMI input
**Output:** 0 sets every output to the requested input. 1-8 sets that specific output to the requested input

#### AUDIO
Takes 2 arguments and sets audio Output #<Output> to HDMI Input <Input>.
```
AUDIO <Input> <Output>
```
Each argument must be a whole number(Integer) between 0 and 8 inclusive.
**Input:** 0 turns the output off. 1-8 sets the output to that HDMI input
**Output:** 0 sets every output to the requested input. 1-8 sets that specific output to the requested input

NOTE: This prompt will only function if the audio channels have been switched to independent mode

#### LOADPRESET
Takes 1 argument and loads the requested preset
```
LOADPRESET <Preset>
```
**Preset:** Must be a whole number(Integer) between 1 and 3 inclusive. Loads that preset

#### SAVEPRESET
Takes 1 argument and saves the current state of the machine to the requested preset
```
SAVEPRESET <Preset>
```
**Preset:** Must be a whole number(Integer) between 1 and 3 inclusive. saves to that preset

### Future Prompts
The API has the functionality to allow for more prompts. If requests, the prompts can be created.

Examples:
- Querying video outputs
- Switching Audio mode
- Querying Audio Outputs
- Muting/unmuting Audio Outputs
- Querying Audio Mute state
- Controlling display power Via CEC
- Matrix EDID Settings(MX-040-HDMI Only)
- IR Config
- Reboot/Reset

## other compatibility
This script should be able to be compatible with any product that uses the same API. Specifically, it should be compatible with any Wyrestorm **MX-H2A**, **MXV**, and **MX-KIT** series Matrix Switchers. These products are, in theory, compatible but have not been tested.
One issue would be the limit of inputs and outputs. This was designed for the MXV-0808-H2A, which has 8 inputs and 8 outputs; As such, the code limits you from changing anything past output 8. If you have a 0404 product, then this script will allow you to modify outputs 5-8, which don't exist and could cause an error, or if Wyrestorm released a product with 10 outputs, this script won't allow you to modify any output or input past 8. This will likely change soon, as the solution is quicker than this explanation. 

