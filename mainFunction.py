class Main:
    def __init__(self):
        self.displayMenu()
    
    def displayMenu(self):
        print('''
Menu
-------------
1. Encode
2. Decode
3. Quit
              
''')
        self.captureInput()
    def captureInput(self):
        options = [1, 2, 3]
        while True:
            menuOptionSelected = input("Please enter an option: ")
            try:
                int(menuOptionSelected)
                break
            except:
                continue
        self.executeOption(int(menuOptionSelected))
        
    def executeOption(self, option):
        match option:
            case 1:
                self.getPassword()
                self.encodedPassword = self.encode(self.password)
                self.displayMenu()
            case 2:
                self.decode()
                self.displayMenu()
            


    def getPassword(self):
        while True:
            try:
                self.password = int(input("Please enter your password to encode: "))
                break
            except: 
                print("invalid input")

    def encode(self, password):
        stringPassword = str(password)
        lengthPassword = len(stringPassword)
        newString = ""
        for i in range(lengthPassword): #make dictionary to reorder string
            newString += str(int(stringPassword[i]) + 3)
        return int(newString)

    def decode(self): #finsihed tasks
        lengthPassword = len(str(self.encodedPassword))
        stringPassword = str(self.encodedPassword)
        newString = ""
        for i in range(lengthPassword):
            newString += str(int(stringPassword[i]) - 3)
        print(f"The encoded password is {self.encodedPassword}, and the original password is {int(newString)}")

instance = Main() ##finished tasks