
import sys


def lex():
    global charclass, lexeme, nexttoken
    getnonblank()
    if charclass == LETTER:
        addchar()
        getchar()
        while (charclass == LETTER or charclass== DIGIT):
            addchar()
            getchar()
        nexttoken = IDENT
    elif charclass == DIGIT:
        addchar()
        getchar()
        while (charclass == LETTER or charclass == DIGIT):
            addchar()
            getchar()
        nexttoken = INT_LIT
    elif charclass == UNKNOWN:
        lookup(nextchar)
        getchar()
    else:
        nexttoken = EOF
        lexeme = "EOF"
    print "Next Token is: ", nexttoken , ", Next Lexeme is: ", lexeme
    lexeme = ""
    return nexttoken

def addchar():
    global lexeme, lexlen
    if lexlen <= 98:
        lexeme += nextchar
        lexlen += 1
    else:
        print "Error - lexeme is too long \n"


def getnonblank():
    while nextchar.isspace():
        getchar()
        

def lookup(ch):
    global nexttoken
    if ch == "(":
        addchar()
        nexttoken = LEFT_PAREN
    elif ch == ")":
        addchar()
        nexttoken = RIGHT_PAREN
    elif ch == "+":
        addchar()
        nexttoken = ADD_OP
    elif ch == "-":
        addchar()
        nexttoken = SUB_OP
    elif ch == "*":
        addchar()
        nexttoken = MULT_OP
    elif ch == "/":
        addchar()
        nexttoken = DIV_OP
    else:
        addchar()
        nexttoken = EOF
    return nexttoken
    

def getchar():
    global nextchar, charclass
    nextchar = in_fp.read(1)     
    if nextchar != "":          
        if nextchar.isalpha():     
            charclass = LETTER
        elif nextchar.isdigit():   
            charclass = DIGIT
        else:
            charclass = UNKNOWN
    else:
        charclass = EOF



# main function    
if __name__ == '__main__':
    
    # character classes
    LETTER = 0
    DIGIT = 1
    UNKNOWN = 99
    EOF = -1
    
    lexeme = ""   
    charclass = ""
    nextchar = ""
    lexlen = 0
    
    # token codes
    INT_LIT = 10
    IDENT = 11
    ASSIGN_OP = 20
    ADD_OP = 21
    SUB_OP = 22
    MULT_OP = 23
    DIV_OP = 24
    LEFT_PAREN = 25
    RIGHT_PAREN = 26
    
    parse = 0
    try:
        if len(sys.argv) == 2:              # to check whether input file is passed from command line
            in_fp = open(sys.argv[1],'r')
            parse = 1
        elif len(sys.argv) == 1:            # default input file in case of no input from command line
            in_fp = open('C:\\Users\\bharathreddy\\Desktop\\front.txt','r')
            parse = 1
        else:
            print "Usage:\n Python front.py[file-to-parse(optional,default = C:\\Users\\bharathreddy\\Desktop\\front.txt)]"
    except IOError:
        if len(sys.argv) == 2:
            print "File not found", sys.argv[1]
        else:
            print "File not found: front.txt"
    except:
            print "Expected error: ", sys.exc_info()[0]
            raise
    
    if parse:
        getchar()
        lex()
        while nexttoken != EOF:            
            lex()
        in_fp.close()       








        
        
        
        
    
            
