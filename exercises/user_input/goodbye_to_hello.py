#!/usr/bin/env python3

import re

class GoodByeHello:
    
    input_array = []
    def __init__(self, version: str) -> None:
        self.version = version
        
    def __str__(self):
        return f"{self.__class__} {self.version}: Replaces the instance of goodbye in a line with hello"
    
    def match_using_replace_method(self):
        for each_line in GoodByeHello.input_array:
            print(f"{each_line.lower().replace('goodbye','hello')}")
    
def main() -> None:
    
    re_quit = re.compile("(q|quit)")
    
    print("Enter a line with different permutations of 'goodbye'\nType 'q/quit' when done\n")
    while True:
        input_line = input()
        m = re_quit.match(input_line)
        if m:
            print("Bye for now!!!")
            break
        else:
            GoodByeHello.input_array.append(input_line)
            
    h = GoodByeHello("v1")
    print(h)
    h.match_using_replace_method()
    
if __name__ == "__main__":
    main()
        