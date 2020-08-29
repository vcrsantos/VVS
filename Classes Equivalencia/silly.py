import re

class Silly:
    def checkSilly (self, string):
        if string is None : 
            return False
        
        if len(string) < 1 or len(string) > 6:
            return False
        
        if not re.match("^[A-Za-z0-9]*$", string):
            return False

        if not re.match("^[A-Za-z]*$", string[0]):
            return False
            
        return True
        
        

def main():
    string = "hello"
    print(string+" is "+str(Silly.checkSilly(0, string)))

    string = "2hello"
    print(string+" is "+str(Silly.checkSilly(0, string)))
    

if __name__ == "__main__":
    main()
