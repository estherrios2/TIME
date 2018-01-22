# --------------------------------------
#             TIME Lexer (Esther)
# --------------------------------------

import ply.lex as lex
import re

# Reserved words
reserved = {
    'time': 'LIBRARY',
    'displayInformation': 'COMMAND',
    'manual': 'COMMAND',
    'manualSummary': 'COMMAND',
    'manualHeaders': 'COMMAND',
    'diskUsage': 'COMMAND',
    'space': 'COMMAND',
    'activeProcesses': 'COMMAND',
    'allProcesses': 'COMMAND',
    'schedulerData': 'COMMAND',
    'runningProcesses': 'COMMAND'
}

# List of token names.
tokens = ["LIBRARY", "COMMAND", "PARAMETER"]

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_TIME(t):
    r'\btime\.'
    t.value = "time"
    t.type = reserved.get(t.value)
    return t

def t_DISPLAYINFORMATION(t):
    r'\bdisplayInformation\b'
    t.type = reserved.get(t.value)
    return t

def t_MANUAL(t):
    r'\bmanual\b'
    t.type = reserved.get(t.value)
    return t

def t_MANUALSUMMARY(t):
    r'\bmanualSummary\b'
    t.type = reserved.get(t.value)
    return t

def t_MANUALHEADERS(t):
    r'\bmanualHeaders\b'
    t.type = reserved.get(t.value)
    return t

def t_DISKUSAGE(t):
    r'\bdiskUsage\b'
    t.type = reserved.get(t.value)
    return t

def t_SPACE(t):
    r'\bspace\b'
    t.type = reserved.get(t.value)
    return t

def t_ACTIVEPROCESSES(t):
    r'\bactiveProcesses\b'
    t.type = reserved.get(t.value)
    return t

def t_ALLPROCESSES(t):
    r'\ballProcesses\b'
    t.type = reserved.get(t.value)
    return t

def t_SCHEDULERDATA(t):
    r'\bschedulerData\b'
    t.type = reserved.get(t.value)
    return t

def t_RUNNINGPROCESSES(t):
    r'\brunningProcesses\b'
    t.type = reserved.get(t.value)
    return t

def t_PARAMETER(t):
    r'\( [a-zA-Z0-9._^%$\#!~@]* \)'
    # If the parameter isn't empty, then take the value inside the parenthesis
    if len(t.value) > 2:
        t.value = t.value[1:-1]
    else:
        t.value = ""
    t.type = "PARAMETER"
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    # Un-comment only for Debugging purposes.
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
