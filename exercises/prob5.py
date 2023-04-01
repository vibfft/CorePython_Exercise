# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class StringClass():
    
    def __init__(self) -> None:
        self.console_str = ""
        
    def getString(self) -> None:
        input_str = input("Enter any string: ")
        self.console_str = input_str
        
    def printString(self) -> None:
        print(f"Inputted string is {self.console_str}")
        
def main() -> None:
    s = StringClass()
    s.getString()
    s.printString()
    
if __name__ == '__main__':
    main()
    