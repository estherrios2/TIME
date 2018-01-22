import timeParser as Parser
import os
import re

class Time_Manager:
    def __init__(self):
        self.name = "Handler"
        # List of available commands:
        self.commandInfo = [
            {"function": "time.displayInformation(p)", "description": "display the user information", "parameter": "the username as a parameter"},
            {"function": "time.manual(p)", "description": "display the command manual", "parameter": "a file as a parameter"},
            {"function": "time.manualSummary(p)", "description": "display a summary of one line for each file", "parameter": "the files as a parameter"},
            {"function": "time.manualHeaders(p)", "description": "display the header lines that contain any of the keywords", "parameter": "takes the keywords as a parameter" },
            {"function": "time.diskUsage()", "description": "display the present disk usage", "parameter": "no parameters"},
            {"function": "time.space()", "description": "display the directory space utilization", "parameter": "no parameters"},
            {"function": "time.activeProcesses()", "description": "display all current active processes", "parameter": "no parameters"},
            {"function": "time.allProcesses()", "description": "display all processes", "parameter": "no parameters"},
            {"function": "time.schedulerData()", "description": "display the scheduler data", "parameter": "no parameters"},
            {"function": "time.runningProcesses()", "description": "display all running processes", "parameter": "no parameters"}
        ]
        self.commandFunction = {
            "displayInformation": "finger ",
            "manual": "man ",
            "manualSummary": "man -f ",
            "manualHeaders": "man -k ",
            "diskUsage": "df",
            "space": "du",
            "activeProcesses": "ps",
            "allProcesses": "ps -e",
            "schedulerData": "ps -c",
            "runningProcesses": "top"
        }

        self.cmd = ""
        self.param = ""
        self.userCommand = ""

    def displayAvailableCommands(self):
        print("=" * 75 + "****T.I.M.E.****" + "=" * 75)
        for command in self.commandInfo:
            print(command["function"], " \n")

        print("=" * 75 + "****T.I.M.E.****" + "=" * 75 + "\n")

    def displayCommandsInfo(self):
        print("=" * 75 + "****T.I.M.E.****" + "=" * 75)
        for command in self.commandInfo:
            print("If you want to " + command["description"] + ", type in: " + command["function"] + ". This takes " + command["parameter"] + ". \n")

        print("=" * 75 + "****T.I.M.E.****" + "=" * 75 + "\n")

    def clearConsole(self):
        print("\n" * 150)

    def getCommand(self):
        info =  Parser.Parse.parse(self.userCommand)
        if info is not None:
            self.cmd = info["command"]
            self.param = info["parameter"]
            return True
        else:
            self.validateUserInput()
            return False

    def printCommand(self):
        if self.getCommand():
            self.clearConsole()
            print("=" * 75 + "****T.I.M.E.****" + "=" * 75)
            self.executeCommand()
            print("=" * 75 + "****T.I.M.E.****" + "=" * 75 + "\n")
        else:
            return

    def executeCommand(self):
        toExecute = self.commandFunction[self.cmd] + self.param
        os.system(toExecute)

    def validateUserInput(self):
        print("=" * 75 + "****T.I.M.E.****" + "=" * 75)
        if "time." not in self.userCommand or self.userCommand[0:5] != "time.":
            print("Error at library declaration. \nExpected format: time.commandName(param)")
            print("=" * 75 + "****T.I.M.E.****" + "=" * 75 + "\n")
            return False

        commandInFunctions = {"present": False, "command": ""}
        for function in self.commandFunction:
            if function in self.userCommand:
                commandInFunctions["present"] = True
                commandInFunctions["command"] = function

        if not commandInFunctions["present"]:
            print("Error at command input. Make sure it's a command from the available list.")
            print("=" * 75 + "****T.I.M.E.****" + "=" * 75 + "\n")
            return False

        param = self.userCommand.replace("time."+commandInFunctions["command"], "")[1:-1]
        match = re.match(r'[a-zA-Z0-9._^%$\#!~@]*', param).group()

        if param != "" and not match:
            print("Error at parameter. Make sure you have the right one")
            print("=" * 75 + "****T.I.M.E.****" + "=" * 75 + "\n")
            return False

#Create the object instance of the class here.
if __name__ == '__main__':
    time = Time_Manager()

    while True:
        userChoice = input(
            "What do you want to do? \n" +
            "A) See available commands \n" +
            "B) See command details \n" +
            "C) Enter a command \n" +
            "D) Clear the terminal screen \n" +
            "E) Exit the program \n"
        ).upper()

        if userChoice not in "ABCDE" or len(userChoice) != 1:
            print("Please select one of the proper options. \n")
            continue
        if userChoice == 'A':
            time.displayAvailableCommands()

        if userChoice == 'B':
            time.displayCommandsInfo()

        elif userChoice == 'C':
            time.userCommand = input("Enter the command of your choice: \n")
            time.printCommand()

        elif userChoice == 'D':
            time.clearConsole()

        elif userChoice == 'E':
            break