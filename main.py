import function as fc # from function import *  works to

import pdb


if __name__ == "__main__":
    
    print("Who are the participants?")    
    participant1= input()
    pdb.set_trace()

    fc.add_participants(participant1)

    print(fc.participants)

    fc.add_more_participants()

    print("Do you want to add a skill?") 

    print(fc.add_competence()) 