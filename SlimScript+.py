global availablecommands,availablepars,memory,prefix; prefix = "slimS"; availablecommands = ["+","-","R","move","copy","del","rpt","rng","memory","memories",prefix+".help",prefix+".guide",prefix+'.memory',prefix+".changelog",prefix+".upcomingFeatures","prefix","M1","M2","M3","S1","S2","S3","Sp1","Sp2","L1"]; availablepars = ["RD","Rpt","Val"]; import time, webbrowser;from random import randint
def Guide(command):
    if command == "+": print("\nAdds 1 to one of the memory values.")
    elif command == "-": print("\nRemoves 1 from one of the memory values.")
    elif command == "R": print("\nResets all memory values' contents.")
    elif command == "move": print("\nMoves a memory value's contents to another one.")
    elif command == "copy": print("\nCopies a memory value's contents to another one. ")
    elif command == "del": print("\nResets a memory value's contents.")
    elif command == "rpt": print("\nRepeats the specified command X times.")
    elif command == "memory": print("\nDisplays the memory values.")
    elif command == "memories": print("\nDisplays the names of the memory values.")
    elif command == prefix+".help": print("\nDisplays the available commands.")
    elif command == prefix+".guide": print("\nDisplays the guide for a command.")
    elif command == prefix+".varGuide": print("\nDisplays the guide for variables.")
    elif command == prefix+".guide": print("\nDisplays the guide for a command.")
    elif command == "prefix": print("\nChanges the prefix for commands starting with '"+prefix+"'. The default prefix is 'slimS'.")
    elif "M" in command or "S" in command or "Sp" in command or "L" in command or "P" in command: print("\nDisplays an error and the cause.")
def Do(command):
    global memory1,memory2,memory3,prefix; memory = [memory1,memory2,memory3]; memories = ["memory1","memory2","memory3"]
    if command == "+":
        a = input("Pars? (type in pars for help) ")
        if a in availablepars:
            if a == "pars": print("Available parameters: 'RD', 'Rpt', 'Val'")
            elif a == "RD":
                b = input("Redirect to? ")
                if b in availablecommands: Do(b)
                else: print("! S3")
        else: print("! S4")
    elif command == "-":
        if isinstance(memory1,int) == True and isinstance(memory2,int) == True and isinstance(memory3,int) == True:
            if memory1 > 0: memory1 -= 1
            elif memory1 == 0:
                if memory2 > 0: memory2 -= 1
                elif memory2 == 0:
                    if memory3 > 0: memory3 -= 1
                    else: print("! M2")
        else: print("! M3")
    elif command == "R": memory1 = memory2 = memory3 = 0; print("Memory values have been reset.")
    elif command == "move":
        a = input("Choose a memory value to move: "); input("Choose a memory value to move "+ a +" to: ")
        if a in memories and input in memories:
            if a == "memory1":
                if input == "memory2": memory2 = memory1; memory1 = 0
                elif input == "memory3": memory3 = memory1; memory1 = 0
            elif a == "memory2":
                if input == "memory1": memory1 = memory2; memory2 = 0
                elif input == "memory3": memory3 = memory2; memory2 = 0
            else:
                if input == "memory1": memory1 = memory3; memory3 = 0
                elif input == "memory2": memory2 = memory3; memory3 = 0
            if a == input: print("! S2"); Do("move")
        else: print("! S1"); Do("memories"); Do("move")
    elif command == "copy":
        a = input("Choose a memory variable to copy: "); input("Choose a memory variable to copy "+ a +" to: ")
        if a in memories and input in memories:
            if a == "memory1":
                if input == "memory2": memory2 = memory1
                elif input == "memory3": memory3 = memory1
            elif a == "memory2":
                if input == "memory1": memory1 = memory2
                elif input == "memory3": memory3 = memory2
            else:
                if input == "memory1": memory1 = memory3
                elif input == "memory2": memory2 = memory3
            if a == input: print("! S2"); Do("copy")
        else: print("! S1"); Do("memories"); Do("copy")
    elif command == "del":
        input("Choose a memory variable to delete: ")
        if input in memories:
                if memory1 == 0 and memory2 == 0 and memory3 == 0: print("! M2")
                elif input == "memory1": memory1 = 0
                elif input == "memory2": memory2 = 0
                else: memory3 = 0
        else: print("! S1"); Do("del")
    elif command == "rng":
        input("Choose a memory value to affect. (Type 'all' to affect all values) ")
        if input in memories:
            if input == "memory1": memory1 = randint(0,9)
            elif input == "memory2": memory2 = randint(0,9)
            elif input == "memory3": memory3 = randint(0,9)
        elif input == "all": memory1 = randint(0,9); memory2 = randint(0,9); memory3 = randint(0,9)
        else: print("! S3"); Do("rng")
    elif command == "memory": print(memory)
    elif command == "memories": print("Memory value names:\nmemory1\nmemory2\nmemory3")
    elif command == prefix+".help": print("Available commands:",availablecommands)
    elif command == prefix+".guide":
        c = input("Choose a command to get info on. ")
        if c in availablecommands: Guide(c)
        else: print("! S3")
    elif command == "prefix":
        b = input("Your prefix is '"+prefix+"'. Would you like to change it? ")
        if "yes" in b or "Yes" in b:
            a = input("Type your old prefix: ")
            if prefix == a: c = input("Type your new prefix: "); prefix = c
            else: print("! L1"); Do("prefix")
    elif command == prefix+".memory":
        a = input("Type a memory value to change: ")
        if input in memories:
            if input == "memory1": b = input("Change '"+input+"' to what?"); memory1 == input
            elif input == "memory2": b = input("Change '"+input+"' to what?"); memory2 == input
            elif input == "memory3": b = input("Change '"+input+"' to what?"); memory3 == input
        else: print("! S3")
    elif command == prefix+".changelog":
        a = input("Open up the changelog? ")
        if "Yes" in a or "yes" in a:
            b = str(randint(0,12)); c = str(randint(0,16)); d = input("Please enter the answer to this question to prove that you're not a bot: "+b+"+"+c+" ")
            if d == str(int(b)+int(c)): webbrowser.open("https://google.com/404/",new=1,autoraise=True)
            else: print("! L1"); Do(prefix+".changelog")
    elif command == "M1": print("MemoryError: memory is full. (Memory >= 1110)")
    elif command == "M2": print("MemoryError: memory values are empty. (Memory <= 0)")
    elif command == "M3": print("MemoryError: memory values are not in range or not of class int. (One or more memory values are corrupted or outside of possible range [0-9])")
    elif command == "S1": print("SyntaxError: assigned values not found in availablecommands. (Input isn't a command)")
    elif command == "S2": print("SyntaxError: unexpected match between value 1 and value 2. (A memory value can't affect itself.)")
    elif command == "S3": print("SyntaxError: input not found in availablecommands. (Not a command)")
    elif command == "Sp1": print("SpecialError: value too large for command. (Cap reached)")
    elif command == "Sp2": print("SpecialError: value too small for command. (Value is <= 0)")
    elif command == "L1": print("LogError: verification failed. (Verification isn't the right value)")
def CheckForSyntax():
    line = input(">> ")
    if line in availablecommands: Do(line)
    else: print("! S3")
memory1 = memory2 = memory3 = 0; totalmemory = int(str(memory3 + memory2 + memory1)); print("Great! You're using the official version of SlimScript+. All features of SlimScript+ v0.0.0 are included in this release.")
while True: CheckForSyntax()