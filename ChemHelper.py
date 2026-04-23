import time
import PeriodicTable as PT
class main ():
    def __init__(self) -> None:
        pass

    def chemical_Lookup():
        #inputtype=input("would you like to input element by their (Atomic Number, Name, or Symbol?\n1: Atomic Number\n2: Name\n3: Symbol\n Your Choice: ")
        chemical=input("Please input element by The elements (Atomic Number, Name, or Symbol):\t")
        try:
            chemical=int(chemical)
            print("Number worked")
        except ValueError:
            chemical=chemical.capitalize()
            if len(chemical)<5:
                for i in PT.Chemicals:
                    if PT.Chemicals[i]["Symbol"] == chemical:
                        chemical = i
            else:
                print("No conversion needed")
        finally:
            if type(chemical) == int:
                for i in PT.Chemicals:
                    if PT.Chemicals[i]["AtomicNumber"] == chemical:
                        chemical = i
        print("what happens here?")
        if chemical in PT.Chemicals:
            fieldData=input(f"What data do you want from the element [{chemical}]?\n 1.Symbol\n 2.Atomic Mass\n 3.Atomic Number\n Enter a number or hit the ENTER key for all fields of data:\t")
            #for d in PT.Chemicals:
            match fieldData:
                case "1": #if chemical == i:
                    return (print(f'\nThe Symbol of the chemical {chemical} is {PT.Chemicals[chemical]["Symbol"]}\n'))
                case "2": #if chemical == i:
                    return (print(f'\nThe Atomic Mass of the chemical {chemical} is {PT.Chemicals[chemical]["AtomicMass"]}\n'))
                case "3": #if chemical == i:
                    return (print(f'\nThe Atomic Number of the chemical {chemical} is {PT.Chemicals[chemical]["AtomicNumber"]}\n'))
                case _: #if chemical == i:
                    return (print(f'#{PT.Chemicals[chemical]["AtomicNumber"]} | {chemical}\n\tSymbol | {PT.Chemicals[chemical]["Symbol"]}\n\tAtomic Mass | {PT.Chemicals[chemical]["AtomicMass"]}\n\tAtomic Number | {PT.Chemicals[chemical]["AtomicNumber"]}\n'))
                #used for testing purposes dont include in stuff
                #print("Incorrect Chemical match")
        else:
            return (print(f"Yikers. The chemical with the name {chemical} isnt in the file currently."))

    def launch_info():
        print("List of Chemicals and current info")
        print("___________________________________________________")
        for i in PT.Chemicals:
            print(f' #{PT.Chemicals[i]["AtomicNumber"]} | {i}\n\tSymbol | {PT.Chemicals[i]["Symbol"]}\n\tAtomic Mass | {PT.Chemicals[i]["AtomicMass"]}\n\tAtomic Number | {PT.Chemicals[i]["AtomicNumber"]}\n')
            time.sleep(0.1)

    def chemical_Add():
        # desired outcome if elements are put in {combined symbols} and {combined mass} EX: hydrogen hydrogen == H2, 2.016g
        SymbolAdd={}
        finalSymbolAdd=""
        combinedmass=0
        i=1
        while True:
            chemical=input(f"Please input name of chemical to add\nChemical #{i}:")
            chemical=chemical.capitalize()
            if chemical == "Quit" or chemical == "Stop":
                break
            else:
                if chemical in PT.Chemicals:
                    numberUsed=int(input(f"Please input how many atoms of {chemical} are in the solution: "))
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

main.chemical_Lookup()