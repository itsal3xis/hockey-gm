def Teams():
    team_list = ["Montreal", "Boston", "Chicago", "Toronto", "New York", "Detroit"]

    choice = int(input("1: Select a team\n2: Create a team\n3: Select a team concept"))
    while choice > 3:
        print("Choose a valid option")
        choice = int(input(">  "))
    
    if choice == 1:
        team_choice = int(input("1: Montreal\n2: Boston\n3: Chicago\n4: Toronto\n5: New York\n6: Detroit"))
        while team_choice > 6:
            print("Choose a valid option")
            choice = int(input(">  "))

        if team_choice == 1:
            return "Montreal"
        elif team_choice == 2:
            return "Boston"
        elif team_choice == 3:
            return "Chicago"
        elif team_choice == 4:
            return "Toronto"
        elif team_choice == 5:
            return "New York"
        else:
            return "Detroit"


def create_team():
    pass