import os as _os
import shlex as _shlex

def LevelPrint(level, msg=None):
    for i in range(level):
        print("    ", end="", flush=True)
    if msg != None:
        print(msg)


def LevelInput(level, msg=""):
    LevelPrint(level)
    return input(msg)


def AnyKeyDialog(msg=""):
    if msg != "":
        msg += " - "
    msg += "Press enter to continue..."
    input(msg)


def ClearConsoleWindow():
    _os.system("cls" if _os.name == "nt" else "clear")
    return

def Prompt_YesOrNo(question:str) -> bool:
    '''
    prompts user indefinitely until one of the choices are picked

    output style: <question> [Y/N]:
    @return: boolean yes=True, no=False
    '''
    
    while(True):
        answer = input(question + " [Y/N]:").upper()
        if(answer == "Y"):
            return True
        elif(answer == "N"):
            return False



def Print_SelectFileDialog(message="Enter File Paths",printlevel=0) -> list[str]|None:
    LevelPrint(printlevel, f"-{message}")
    filepathString = LevelInput(printlevel, "-")
    filepaths = _shlex.split(filepathString)
    if(len(filepaths) == 0):
        return None
    return filepaths

