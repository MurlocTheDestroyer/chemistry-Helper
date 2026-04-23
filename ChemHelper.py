import time
import PeriodicTable as PT
class main ():
    def __init__(self) -> None:
        pass

    def Chemical_Input_Only():
        chemical = None
        while True:
            chemical=input("\nPlease input element by the element (Atomic Number, Name, or Symbol):\t")
            try:
                chemical=int(chemical)
            except ValueError:
                chemical=chemical.capitalize()
                if len(chemical)<=2:
                    for i in PT.Chemicals:
                        if PT.Chemicals[i]["Symbol"] == chemical:
                            chemical = i
                            break
            finally:
                if type(chemical) == int:
                    if chemical <=0:
                        print("Please enter only positive integers and please try again.")
                        continue
                    for i in PT.Chemicals:
                        if PT.Chemicals[i]["AtomicNumber"] == chemical:
                            chemical = i
                            break
            return(chemical)
        
    def chemical_Lookup():
        chemical=main.Chemical_Input_Only()
        if chemical in PT.Chemicals:
            fieldData=input(f"\n\nWhat data do you want from the element [{chemical}]?\n 1.Symbol\n 2.Atomic Mass\n 3.Atomic Number\n Enter a number or hit the ENTER key for all fields of data:\t")
            match fieldData:
                case "1":
                    return (print(f'\nThe Symbol of the chemical {chemical} is {PT.Chemicals[chemical]["Symbol"]}\n'))
                case "2":
                    return (print(f'\nThe Atomic Mass of the chemical {chemical} is {PT.Chemicals[chemical]["AtomicMass"]}\n'))
                case "3":
                    return (print(f'\nThe Atomic Number of the chemical {chemical} is {PT.Chemicals[chemical]["AtomicNumber"]}\n'))
                case _:
                    return (print(f'\n#{PT.Chemicals[chemical]["AtomicNumber"]} | {chemical}' +
                                  f'\n\tSymbol | {PT.Chemicals[chemical]["Symbol"]}'
                                  f'\n\tAtomic Mass | {PT.Chemicals[chemical]["AtomicMass"]}'
                                  f'\n\tAtomic Number | {PT.Chemicals[chemical]["AtomicNumber"]}\n'))
        else:
            return (print(f"Yikers. The chemical with the name {chemical} isnt in the file currently."))

    def launch_info():
        print("List of Chemicals and current info")
        print("___________________________________________________")
        for i in PT.Chemicals:
            print(f'\n#{PT.Chemicals[i]["AtomicNumber"]} | {i}' +
                  f'\n\tSymbol | {PT.Chemicals[i]["Symbol"]}'
                  f'\n\tAtomic Mass | {PT.Chemicals[i]["AtomicMass"]}'
                  f'\n\tAtomic Number | {PT.Chemicals[i]["AtomicNumber"]}\n')
            time.sleep(0.1)

    def chemical_Add():
        # desired outcome if elements are put in {combined symbols} and {combined mass} EX: hydrogen hydrogen == H2, 2.016g
        SymbolAdd={}
        finalSymbolAdd=""
        combinedmass=0
        i=1
        while True:
            chemical = main.Chemical_Input_Only()
            if chemical == "Quit" or chemical == "Stop":
                break
            else:
                if chemical in PT.Chemicals:
                    numberUsed=input(f"Please input how many atoms of {chemical} are in the solution: ")
                    while type(numberUsed)!=int:
                        try:
                            numberUsed=int(numberUsed)
                        except ValueError:
                            numberUsed=input(f"Please input a integer of how many atoms of {chemical} are in the solution: ")

                    for j in PT.Chemicals:
                        if j==chemical:
                            if PT.Chemicals[j]["Symbol"] in SymbolAdd:
                                SymbolAdd.update({(PT.Chemicals[j]["Symbol"]):(SymbolAdd.get(PT.Chemicals[j]["Symbol"]) + numberUsed)})
                            else:
                                SymbolAdd.update({PT.Chemicals[j]["Symbol"]:numberUsed})

                            combinedmass+=((PT.Chemicals[j]["AtomicMass"])*numberUsed)
                            
                            if numberUsed == 1:
                                print(f'{numberUsed} atom of {j} added to solution\n')
                            else:
                                print(f'{numberUsed} atoms of {j} added to solution\n')
                            
                    i+=1
                else:
                    print(f"Yikers. The chemical with the name {chemical} isnt in the file currently. Please try again.\n")
        for k in SymbolAdd:
            finalSymbolAdd+=f"{k}{SymbolAdd[k]}"
        return (print(f"This is the dictionary :{finalSymbolAdd}"), print(f"This is the combined mass for dictionary :{combinedmass}g"))
    
    def bootup():
        choice=input("What Command?\t Current commands (launch_info),(chemical_Lookup),(chemical_Add)\n")
        match choice.lower():
            case "launch_info":
                print(f"Running Command: {choice}")
                main.launch_info()
                print(f"Command ({choice}) has completed")
            case "chemical_lookup":
                print(f"Running Command: {choice}")
                main.chemical_Lookup()
                print(f"Command ({choice}) has completed")
            case "chemical_add":
                print(f"Running Command: {choice}")
                main.chemical_Add()
                print(f"Command ({choice}) has completed")
            case "dismiss" | "quit":
                return (print("As you wish. Good Bye!"))
            case _:
                print(f" ({choice}) COMMAND NOT FOUND. Please try again")
                main.bootup()
        main.Replay()
    def Replay():
        Stopper=input("Press any key to continue: ")
        decision= input("Would you like to use another tool? Y/N: ")
        match decision:
            case "Y" | "y":
                main.bootup()
            case "N" | "n":
                print("OK. GOODBYE")
            case _:
                print("\n\nPlease make a choice of 'Y' or 'N' ")
                main.Replay()
            
main.bootup()