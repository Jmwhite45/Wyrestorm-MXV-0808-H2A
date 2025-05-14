#Imports
import warnings # Telnet is Deprecated in this verison of python and is removed in future versions.  
warnings.filterwarnings("ignore", category=DeprecationWarning) # this stops the warning from showing up
from telnetlib import Telnet #library to connect with telnet
import sys
from  pathlib import Path
import json


def dictToString(Dict):
    return ", ".join([value for value in Dict])

# Validates 2 arguments for video and audio purposes
# there should be 2 arguments both need to following these rules:
# - be an Int
# - be a number between 0 and 8 inclusive
def avValidate():
    # Error check to make sure the correct number of arguments was given.
    if len(sys.argv) <4:
        print("ERROR: Not enough arguments(2 required). Run again with <input> <output>")
        quit()

    # Error check to make sure both inputs are Interagers
    err = ""
    try:
        argIn = int(sys.argv[2]) #input, 0 is off
    except:
        err += "ERROR: Input is not an Integer. Input should be a number between 0 and 8\n"
    try:
        argOut = int(sys.argv[3]) #ouput, 0 is all
    except:
        err += "ERROR: Output is not an Integer. Output should be a number between 0 and 8\n"
    # if an error occured, output the error and quit the program
    if len(err)>0:
        print(err)
        quit()

    # Error check to make sure inputs are in range
    if argIn>8 or argIn<0:
        err += "ERROR: Input is not in range. Input should be a number between 0 and 8\n"
    if argOut>8 or argOut<0:
        err += "ERROR: Output is not in range. Output should be a number between 0 and 8\n"
    # If error, output error and quit the program
    if len(err)>0:
        print(err)
        quit()
    return [argIn, argOut]

# Traslates 2 arguments into one to use in wyrestorm
def videoTranslate(argIn, argOut):
    if argOut == 0:
        argOut = "ALL"
    else:
        argOut = "OUT"+str(argOut)

    return "HDMIIN"+str(argIn) +" " + argOut

# Traslates 2 arguments into one to use in wyrestorm
def AudioTranslate(argIn, argOut):
    if argOut == 0:
        argOut = "ALL"
    else:
        argOut = "AUDIOOUT"+str(argOut)

    print([argIn, argOut, "HDMIIN"+str(argIn) +" " + argOut])
    return "HDMIIN"+str(argIn) +" " + argOut

def presetValidate(): 
    # Error check to make sure the correct number of arguments was given.
    if len(sys.argv) <3:
        print("ERROR: Not enough arguments(1 required). Run again with 1 preset")
        quit()

    # Error check preset is an Int
    try:
        arg = int(sys.argv[2]) #input, 0 is off
    except:
        print("ERROR: Preset is not an Integer. Input should be a number between 1 and 3")
        quit()
    
    # Error check to make sure inputs are in range
    if arg>3 or arg<1:
        print("ERROR: Input is not in range. Input should be a number between 1 and 3\n")
        quit()

    return [str(arg)]

def presetTranslate(argIn):
    return argIn

CMDs = {
    "VIDEO":{
        "cmd": "SET SW ",
        "valid": avValidate,
        "translate": videoTranslate
    },
     "AUDIO":{ # If audio matches video switches then this will not work
        "cmd": "SET AUDIOSW ",
        "valid": avValidate,
        "translate": AudioTranslate
    },
    "LOADPRESET":{
        "cmd": "RESTORE PRESET ",
        "valid": presetValidate,
        "translate": presetTranslate
    },
    "SAVEPRESET":{
        "cmd": "SAVE PRESET ",
        "valid": presetValidate,
        "translate": presetTranslate
    },
}
try:
    prompt = sys.argv[1]
    if prompt not in CMDs.keys():
        raise Exception("Invalid prompt")
except:
    print("ERROR: Prompt not valid. Please use one of the following: ", dictToString(CMDs.keys()))
    quit()


prompt = CMDs[prompt]


# command to be run
cmd = prompt["cmd"] + prompt["translate"](*prompt["valid"]())
print("Command: ", cmd)

#get IP address from config
with open(str(Path(__file__).parent.absolute())+'/config.json','r') as file:
    config = json.load(file)

try:
    tn = Telnet(config["IP"],config["PORT"]) #connect
except:
    print("ERROR: Unable to connect to Wyrestorm. Please check internet connection and the IP in the config file")
    quit()

tn.write(cmd.encode('ascii')+b"\r\n") #write commmand
tn.close() #exit