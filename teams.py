def teams():
    team_list = ["Montreal", "Boston", "Chicago", "Toronto", "New York", "Detroit"]

    choice = int(input("1: Select and play as a classic team\n2: League Expansion - Create a team\n"
                       "3: League Expansion - Select a team concept\n>  "))
    while choice > 3:
        print("Choose a valid option")
        choice = int(input(">  "))
    
    if choice == 1:
        team_choice = int(input("1: Montreal        2: Boston\n3: Chicago         4: Toronto\n"
                                "5: New York        6: Detroit\n>  "))
        while team_choice > 6 or team_choice < 1:
            print("Choose a valid option")
            team_choice = int(input(">  "))

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
    name = input("Enter the team name\n>  ")
    city = input("Enter the location of the team\n>  ") #Add verification for no name
    


teams()