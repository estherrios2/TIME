# TIME

# I. Introduction

Utilizing the UNIX terminal is of great importance and utility, especially if you want to be able
to perform many functions deeper and more complex than what can be achieved with the
computer’s user interface (UI). The UNIX terminal or shell is a command-line interpreter (CLI)
which can be used to direct the operation of the computer by entering commands as text for the
CLI to execute or by creating text scripts of one or more such commands (The Unix Shell). The
terminal or UNIX shell allows command use for handling files, system processes, permissions,
networking, search, compression, and shortcuts.
Since terminal commands are abbreviated, these can give a hard time for beginners and even
experienced terminal users. It is usually a hassle for programmers and other users to remember all
the commands apart from the usual ones used for file handling, which most people can easily
recall. The “Terminal Interaction Made Easy” or T.I.M.E. programming language will be designed
and implemented as a solution for dealing with those commands in the terminal that are not that
intuitive.

# II. Language Features

As previously mentioned, T.I.M.E.’s sole purpose is to facilitate the understanding and use of
terminal commands for end users. Its language structure and syntax will be similar to Java’s in
terms of how the methods use verbs or nouns to denote an Object, which in T.I.M.E.’s case is via
the word time. Dots are used to separate the class from the specific action or function that will take
place (see part III for examples). Thus, programmers with Java and/or C++ coding experience can
easily grasp the lexicon of the language and quickly start programming.
T.I.M.E. will consolidate the communication with the system terminal application through
native shell commands for system and process management handling. The following commands
to be implemented have been chosen because these are commonly used in the Operating Systems
class for the Computer Engineering program in the University of Puerto Rico at Mayagüez.
Students often have the difficulty of remembering these commands and understanding the meaning
behind it. Not because a command is shorter and abbreviated means that these are easier to
remember. The system commands, written in UNIX, to be implemented are the following:

1. time.displayInformation(user_goes_here) //display user information
2. time.manual() //show command manual
3. time.manualSummary(files_go_here) //display a summary (one line) for each file
4. time.manualHeaders(keywords_go_here) //displays the header lines that contain any of the keywords
5. time.diskUsage() //present disk usage
6. time.space() //display directory space utilization
7. time.activeProcesses() //show all current active processes
8. time.allProcesses() //displays all processes
9. time.schedulerData() //displays scheduler data
10. time.runningProcesses() //present all running processes

These shell operations will be incorporated as T.I.M.E.’s features through a readable structure
and syntax that will only work for the Linux operating system.

# III. Example of a Program

T.I.M.E. is very much alike Java and C++ structure and syntax. The first example of the
proposed language is the terminal command finger user:
time.displayUserInfo(user)

It can be observed that, as stated in the previous section, the Object of this command is time. The
function it is referring to denotes that the shell application should present on the screen the
information of a particular user in a simpler form than the native UNIX code.
Another example is that of top where the command displays all of the running processes in the
system. With T.I.M.E., it should be written as:

time.displayRunProcesses()

# IV. TIME Walkthrough

https://youtu.be/OqaQlwodN3U

# Note:
TIME project was developed by Anderson Roman, Leslie Soto, and Esther Rios for the ICOM4036 Course given by Professor Wilson Rivera at the University of Puerto Rico, Mayaguez Campus.
