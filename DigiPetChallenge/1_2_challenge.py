"""
    DigiPet CLI Application -

        DigiPet is a simple application that lets the user care for one or more cute and lovely pets. Simple activities such as walking, playing and sleeping will affect the DigiPet's
    happiness and energy. Let either one fall too low and your cute and lovely pet will become daisy fertilizer. ( not good! )

    Specifications:
        - Use the starter code provided below
        - Add the following commands
            walk - "Implement Walk"
            play - "Implement Play"
            feed - "Implement Feed"
            sleep - "Implement Sleep"
            do trick - "Implement Do Trick"
            switch - "Implement Switch"
            - Any other commands should return “Invalid Command”

        - Update "menu" command to list menu options
            - use a tuple store the menu options

    Process Builders -
        - Refer to yours or some other source of working code that is similar.
        - Plan before you build; pseudo code
        - Ideally, each student will have their own copy with 1 student sharing their screen and everyone working together to decide the code you will all use.
"""

is_active = True
# add menu items #

digipet = {
    'Name:':"Kanji",
    "Health:": 90,
    "Energy:": 100,
    'Friendship:':0,
}

while is_active:
    menu = ('walk','play','feed','sleep','do trick','switch',"stats")
    
    #Stats checker
    if digipet['Health:'] <= 0 or digipet['Energy:'] <= 0:
        print(f"{digipet['Name:']} is dead")
        is_active = False
        continue

    command = input("\ncommand-> ")
    if digipet['Friendship:'] == 100:
        print(f"Congrats! {digipet['Name:']}'s friendship is 100. \n They really like you. \n Great work!")

    if command == "menu":
        print('----------')
        for i in menu:
            print(i)
    
# Digipet Commands
            
# WALKIES
    elif command == "walk":
        digipet['Friendship:'] += 1
        digipet['Energy:'] -= 10
        if digipet["Health:"] < 100:
            digipet["Health:"] +=10
        print(f"You take {digipet['Name:']} for a walk.\n {digipet['Name:']}'s Energy: {digipet['Energy:']}\n {digipet['Name:']}'s Health: {digipet['Health:']}")
# PLAY WITH ME 
    elif command == "play":
        digipet['Friendship:'] += 5
        digipet['Energy:'] -= 15
        print(f"You play with {digipet['Name:']} for a bit. \n {digipet['Name:']}'s Energy:{digipet['Energy:']}")
# FEED ME
    elif command =='feed':
        digipet['Friendship:'] += 5
        if digipet['Energy:'] < 100:
            digipet['Energy:'] += 15
        if digipet['Health:'] < 100:
            digipet['Health:'] + 10
        print(f"You fed {digipet['Name:']}.\n {digipet['Name:']}'s Energy:{digipet['Energy:']}")
# GO MII MIIS
    elif command =='sleep':
        digipet['Energy:'] = 100
        print(f"{digipet['Name:']} took a nap.\n {digipet['Name:']}'s Energy:{digipet['Energy:']}")
    elif command == 'do trick':
        digipet['Energy:'] -= 20
        digipet['Friendship:'] -=5
        print(f"{digipet['Name:']} performed tricks for you.\n {digipet['Name:']}'s Energy: {digipet['Energy:']}")
#Stats checker
    elif command == "stats":
        for i in digipet.items():
            print(i)
#Exit game
    elif command == "quit":
        is_active = False
# Commands does not match
    else:
        print("Invalid command")

# Secert Command
    if command == "kill":
        digipet['Health:'] = 0
        digipet['Energy:'] = 0
    
    elif command == "max":
        digipet['Friendship:'] = 100
    

    # add other commands #

print('--------')
print("Have A Nice Day!")


