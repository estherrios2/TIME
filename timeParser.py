# --------------------------------------
#             TIME Parser (Leslie)
# --------------------------------------

import ply.yacc as yacc
import timeLexer
from timeLexer import tokens

def p_statement(p):
    '''statement : statement_parseCommand'''
    print(p)
    p[0] = p[1]
    pass

def p_statement_parseCommand(p):
    'statement_parseCommand : LIBRARY COMMAND PARAMETER'
    p[0] = {"library": p[1], "command": p[2], "parameter": p[3]}

# ------------------ Syntax Error on Input ---------------
def p_error(p):
    # Un-comment only for Debugging purposes.
    # print("Syntax error in input! Token type: ", p)
    print()

Parse = yacc.yacc()

# myParse = Parse.parse("time.space(?)")

