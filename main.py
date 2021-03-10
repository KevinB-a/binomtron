import function as fc

if __name__ == "__main__":
    print("Who are the participants?")    
    participant1= input()

    fc.add_participants(participant1)

    print(fc.participants)

    fc.add_more_participants()

    print("Do you want to add a skill?") 

    print(fc.add_competence()) 