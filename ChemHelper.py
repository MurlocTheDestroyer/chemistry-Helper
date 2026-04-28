import PeriodicTable as PT
class main ():
    def __init__(self) -> None:
        pass
    # Chemical_Input_Only is the decider of if the input is The elements(name, atomic Number or Symbol)
    def Chemical_Input_Only():
        #make initial var nothing so that when while loop is entered. Input is always asked first 
        chemical = None
        while True:
            chemical=input("\nPlease input element by the element (Atomic Number, Name, or Symbol):\t")
            try:
                chemical=int(chemical)
            except ValueError:
                chemical=chemical.capitalize()
                if chemical == "Quit" or chemical == "Stop":
                    break
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
                else:
                    return(chemical)
        return(chemical)
        
    def chemical_Lookup():
        #This determines if user is looking for a element group search or a single elements information.
        LookingFor= input("Are looking for what elements are in a group or just wanting info on a single element? TYPE group or single: ")
        LookingFor=LookingFor.lower()
        match LookingFor:
            case "group":
                #ListOfE is the List of all of the elements that fall under that Element Type
                ListOfE=[]
                print("To help with spelling errors please input a number for the selection\n1. Alkali Metal\n2. Alkaline Earth Metal\n3. Transition Metal\n4. Post-transition Metal\n5. Metalloid\n6. Reactive Nonmetal\n7. Noble Gas\n8. Lanthanide\n9. Actinide\n10. Unknown Chemical Properties")
                Group=input("What group would you like?: ")
                while type(Group)!=int:   
                    try:
                        Group=int(Group)
                    except ValueError:
                        print("Error! Please input a number from 1 to 10.")
                        Group=input("What group would you like?: ")
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
                x=f'[{", ".join(ListOfE)}]'
                return(print(f"\nThis is the elements in the {Group} group.\n\n{x}\n\n"))
            case _:
                chemical=main.Chemical_Input_Only()
                if chemical in PT.Chemicals:
                    print(f'\n#{PT.Chemicals[chemical]["Atomic Number"]} | {chemical}\n')
                    for prop in PT.Chemicals[chemical].keys():
                        print(f'\t{prop} | {PT.Chemicals[chemical][prop]}')
                    print("\n")
                else:
                    return (print(f"Yikers. The chemical with the name {chemical} isnt in the file currently."))

    def launch_info():
        print("List of Chemicals and current info", end="")
        #print("___________________________________________________")
        # i in this instance to be the current chemical as it will loop through each chemical name within the Chemicals dictionary
        for i in PT.Chemicals:
            print("\n________________________________________________________________")
            #formatted to look nicer in output
            print(f'\n#{PT.Chemicals[i]["Atomic Number"]} | {i}')
            #prop will loop through i's keys aka (Current Chemicals properties/attributes) and print out all of the properties and values in a formal output.
            for prop in PT.Chemicals[i].keys():
                match prop:
                    case "Melting Point" | "Boiling Point":
                        print(f'\t{prop} | {PT.Chemicals[i][prop]}',"\u00B0C")
                    case "Density":
                        print(f'\t{prop} | {PT.Chemicals[i][prop]}g/cm', end="\u00b3")
                    case _:
                        print(f'\t{prop} | {PT.Chemicals[i][prop]}')
            print("\n")

    def chemical_Add():
        ''' 
        # Found this mapping method for dynamic numbers to avoid needing to import modules
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        Variable=123
        print(f"Subscript: {Variable.translate(SUB)}") # Output: ₁₂₃
        print(f"Superscript: {Variable.translate(SUP)}") # Output: ¹²³
        '''
        #further explanation of how this is to be implemented is commented on Line 147
        # desired outcome if elements are put in {combined symbols} and {combined mass} EX: hydrogen hydrogen == H₂, 2.016g WORKS NOW
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        SymbolAdd={}
        finalSymbolAdd=""
        combinedmass=0
        while True:
            chemical = main.Chemical_Input_Only()
            if chemical == "Stop" or chemical == "Quit":
                break
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
                            SymbolAdd.update({(PT.Chemicals[j]["Symbol"]):(numberUsed)})

                        combinedmass+=((PT.Chemicals[j]["Atomic Mass"])*numberUsed)
                        
                        if numberUsed == 1:
                            print(f'{numberUsed} atom of {j} added to solution\n')
                        else:
                            print(f'{numberUsed} atoms of {j} added to solution\n')
            else:
                print(f"Yikers. The chemical with the name {chemical} isnt in the file currently. Please try again.\n")
            #This will take each element and its total number of atoms and Convert something like H2O to H₂O by using the translation
        for k in SymbolAdd:
            finalSymbolAdd+=f"{k}{str(SymbolAdd[k]).translate(SUB)}"
            #The reason this works is that the integers will keep being added and once the "Stop or Quit" command is entered
            #The integers are each turned into strings and translated to be added into the desired formula output
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