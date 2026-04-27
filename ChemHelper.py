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
                    break
            finally:
                if type(chemical) == int:
                    if chemical <=0:
                        print("Please enter only positive integers and please try again.")
                        continue
                    else:
                        for i in PT.Chemicals:
                            if PT.Chemicals[i]["Atomic Number"] == chemical:
                                chemical = i
                                break
                        break
        return(chemical)
        
    def chemical_Lookup():
        #determine if user looking for a group search or a single element.
        LookingFor= input("Are looking for what elements are in a group or just wanting info on a single element? TYPE group or single: ")
        LookingFor=LookingFor.lower()
        match LookingFor:
            case "group":
                #ListOfE is the List of all of the elements that fall under that Element Type
                ListOfE=[]
                print("To help with spelling errors please input a number for the selection\n1. Alkali Metal\n2. Alkaline Earth Metal\n3. Transition Metal\n4. Post-transition Metal\n5. Metalloid\n6. Reactive Nonmetal\n7. Noble Gas\n8. Lanthanide\n9. Actinide\n10. Unknown Chemical Properties")
                Group=int(input("What group would you like?: "))
                match Group:
                    case 1:
                        Group= "Alkali Metal"
                    case 2:
                        Group= "Alkaline Earth Metal"
                    case 3:
                        Group= "Transition Metal"
                    case 4:
                        Group= "Post-transition Metal"
                    case 5:
                        Group= "Metalloid"
                    case 6:
                        Group= "Reactive Nonmetal"
                    case 7:
                        Group= "Noble Gas"
                    case 8:
                        Group= "Lanthanide"
                    case 9:
                        Group= "Actinide"
                    case 10:
                        Group= "Unknown Chemical Properties"
                    case _:
                        print("Error please enter a number")               
                for Chem in PT.Chemicals.keys():
                    for prop in PT.Chemicals[Chem].keys():
                        if prop == "Element Type":
                            if (PT.Chemicals[Chem][prop]) == Group:
                                #Somewhere here doesnt output correctly? should be [Chemical1, Chemical2] instead its ['Chemical1', 'Chemical2']
                                ListOfE.append(Chem)
                #Could also be the case here? should be [Chemical1, Chemical2] instead its ['Chemical1', 'Chemical2']
                return(print(f"This is the elements in the {Group} group.\n{ListOfE}"))
            case _:
                chemical=main.Chemical_Input_Only()
                if chemical in PT.Chemicals:
                    print(f'\n#{PT.Chemicals[chemical]["Atomic Number"]} | {chemical}\n')
                    for prop in PT.Chemicals[chemical].keys():
                        print(f'\t{prop} | {PT.Chemicals[chemical][prop]}')

                else:
                    return (print(f"Yikers. The chemical with the name {chemical} isnt in the file currently."))

    def launch_info():
        print("List of Chemicals and current info", end="")
        #print("___________________________________________________")
        for i in PT.Chemicals:
            print("\n________________________________________________________________")
            print(f'\n#{PT.Chemicals[i]["Atomic Number"]} | {i}')
            for prop in PT.Chemicals[i].keys():
                match prop:
                    case "Melting Point" | "Boiling Point":
                        print(f'\t{prop} | {PT.Chemicals[i][prop]}',"\u00B0C")
                    case "Density":
                        print(f'\t{prop} | {PT.Chemicals[i][prop]}g/cm', end="\u00b3")
                    case _:
                        print(f'\t{prop} | {PT.Chemicals[i][prop]}')
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

                            combinedmass+=((PT.Chemicals[j]["Atomic Mass"])*numberUsed)
                            
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
            
main.chemical_Lookup()