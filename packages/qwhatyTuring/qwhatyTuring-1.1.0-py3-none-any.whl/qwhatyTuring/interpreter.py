from .graphicsDisplay import *
from .exceptions import InvalidFileType

# Acts in a similar way to a list, but everything is index from the original start point
class Tape:

    # If the index is not in range of the current defined tape, then return a blank symbol
    def __getitem__(self, index: int):
        if index in range(self.min, self.max + 1):
            return self.tape[index - self.min]
        else:
            return "_"

    def __setitem__(self, index: int, value):
        if index in range(self.min, self.max + 1):
            self.tape[index - self.min] = value
        elif index < self.min:
            self.min = index
            self.tape[0] = value
        else:
            self.max = index
            self.tape.append(value)

    def returnTape(self):
        string = ""
        for i in self.tape:
            string += i
        return string

    def __init__(self, tape: str):
        self.min = 0
        self.max = len(tape) - 1
        self.tape = list(tape)

# Iterprets a line of the delta function and adds it to the dict
def interpretDelta(line: str, deltaFunction: dict):
    #sN,1 -> sM,1,>

    leftRight = line.split("->")
    if len(leftRight) != 2:
        raise SyntaxError

    left = leftRight[0].strip().split(",")
    right = leftRight[1].strip().split(",")

    if len(left) != 2 or len(right) != 3:
        raise SyntaxError
    
    startState = left[0]
    read = left[1]
    if len(read) != 1:
        raise SyntaxError
    
    endState = right[0]
    write = right[1]
    if len(write) != 1:
        raise SyntaxError

    leftOrRight = right[2]
    if leftOrRight not in ["<",">","-"]:
        raise SyntaxError

    if startState not in deltaFunction:
        deltaFunction[startState] = {}
    deltaFunction[startState][read] = [endState, write, leftOrRight]

    return deltaFunction

def getParameter(line: str, parameter: str):
    if not line.startswith(parameter + ":"):
        raise SyntaxError
    
    leftRight = line.split(":")
    if len(leftRight) != 2:
        raise SyntaxError
    
    return leftRight[1].strip()

# Interpret one line from the Turing Machine file
def interpretLine(line: str, deltaFunction: dict, arguments: list, requiredParameters: list):
    if line == "\n" or line == "":
        return None, None
    for param in enumerate(requiredParameters):
        try:
            arguments[param[1]] = getParameter(line, param[1])
            requiredParameters.pop(param[0])
            return arguments, None
        except SyntaxError:
            pass
    deltaFunction = interpretDelta(line, deltaFunction)
    return None, deltaFunction

# Execute one cycle of the Turing Machine
def stepTuringMachine(deltaFunction: dict, tape: Tape, currentIndex, currentState):
        detail = deltaFunction[currentState][tape[currentIndex]]
        currentState, tape[currentIndex] = detail[0], detail[1]
        
        if detail[2] == "<":
            currentIndex -= 1
        elif detail[2] == ">":
            currentIndex += 1
        
        return currentState, currentIndex, tape

class TuringMachine:

    REQUIRED_PARAMETERS = ["start", "tape", "halt"]

    def _interpretFile(self):
        line = "\n"
        arguments = {}
        deltaFunction = {}
        END_OF_FILE = ""

        with open(self.file, "r") as f:
            while line != END_OF_FILE:
                line = f.readline()
                argumentsTemp, deltaFunctionTemp = interpretLine(line, deltaFunction, arguments, self.REQUIRED_PARAMETERS)

                # Check which return value has been returned (i.e. the parameter not returned will be None)
                # And update accordingly
                if not argumentsTemp and deltaFunctionTemp: 
                    deltaFunction = deltaFunctionTemp
                elif not (argumentsTemp or deltaFunctionTemp):
                    pass
                else:
                    arguments = argumentsTemp 
        
        deltaFunction[arguments["halt"]] = {}
        return deltaFunction, arguments

    def _init(self):
        startState, haltingState = self.arguments["start"], self.arguments["halt"]
        tape = Tape(self.arguments["tape"])
        currentState = startState
        return haltingState, tape, currentState

    def _runWithoutGraphics(self, stepMode: bool):
        haltingState, tape, currentState = self._init()
        currentIndex = 0
        operations = [[currentState, currentIndex, [tape.returnTape(), tape.min, tape.max]]]

        while currentState != haltingState:
            if stepMode:
                print(" "*currentIndex + "H")
                print(tape.returnTape())
                input("Press enter to continue... ")
            
            currentState, currentIndex, tape = stepTuringMachine(self.deltaFunction, tape, currentIndex, currentState)
            operations.append([currentState, currentIndex, [tape.returnTape(), tape.min, tape.max]])
        
        return operations, tape

    # Run the Turing Machine first, then iterate over each step in a graphical display
    def _runWithGraphics(self):
        operations, tape = self._runWithoutGraphics(False)
        
        tapeDisplay = TapeDisplay()
        tapeDisplay.run(operations)
        

    def run(self, stepMode=False, graphicsMode=False):
        if not graphicsMode:
            operations, tape = self._runWithoutGraphics(stepMode)
            print("Result: " + tape.returnTape().strip("_"))
        else:
            self._runWithGraphics()

    def __init__(self, file: str):
        if not file.endswith(".turing"):
            raise InvalidFileType("File type must be .turing")
        self.file = file
        self.deltaFunction, self.arguments = self._interpretFile()
        self.haltingState = self.arguments["halt"]

if __name__ == "__main__":
    myTuringMachine = TuringMachine("example.turing")
    myTuringMachine.run(graphicsMode=True)