from random import randint, shuffle

def start():
    while True:
        
        try:
            player_amount = int(input("Enter player amount (2 - 5): "))
            
            if 2 <= player_amount <= 5:
                players = [str(input(f"Enter player name {_+1}: ")).capitalize() for _ in range(player_amount)]
                return players
            else:
                print(f"Invalid value: {player_amount}! Please choose number between (2 - 5)")
            
        except ValueError:
            print(f"Invalid input! Please provide a number between (2 - 5)!\n")


def game(players):
    
    results = [0 for _ in range(len(players))]
    while True:
        try:
            rolls = int(input("How many rolls for each round (1 - 5): "))
            
            if 1 <= rolls <= 5:
                print(f"Game with {rolls} rolls!")
                break
            else:
                print(f"Invalid value: {rolls}! Please choose number between (1 - 5)!\n")
        
        except ValueError:
            print("Please provide a number from (1 - 5)!\n")
    
    shuffle(players)
    
    name_width = len(max(players, key=len)) + 2
    roll_width = 5
    player_width = len(max(players, key=len))
    
    while True:
        
        print()
        input("Press Enter to start round!")
        print()
        
        current_results = [0 for _ in range(len(players))]
        messages = []
        
        header = f"{'Name':<{name_width}} {''.join(f'Roll {i+1:<{roll_width}}' for i in range(rolls))} {'Result':<{roll_width}}"
        print(header)
        print("=" * len(header))

        for i in range(len(players)):
            print(f"{players[i]:<{player_width}}", end = f"{' ' *  roll_width}")
            
            has_one = False
            first_roll = None
            all_same = True
            
            for _ in range(rolls):
                dice = randint(1, 6)
                print(f"{dice:<{roll_width}}", end = f"{' ' * roll_width}")
                current_results[i] += dice
                
                if dice == 1:
                    has_one = True
                    
                if first_roll is None:
                    first_roll = dice
                elif dice != first_roll:
                    all_same = False
                
            if all_same and not has_one:
                messages.append(f"{players[i]} rolled all {dice}! All earned points for this round are doubled!")
                current_results[i] *= 2
            
            elif has_one and results[i] > 0 and current_results[i] == 2:
                messages.append(f"Oh no! {players[i]} rolled all {dice}! All earned points are lost!")
                current_results[i] = 0    
                results[i] = 0 
            
            elif has_one:
                messages.append(f"Oh no! {players[i]} rolled one! All points for this round are lost!")
                current_results[i] = 0
            
            results[i] += current_results[i]
            
            print(f"{results[i]:<{roll_width}}")
            
            if results[i] >= 100:
                print()
                print(f"{players[i]} won with {results[i]} points!")
                break
        
        if messages:
            print("\nMessages:")
            for message in messages:
                print(message)
            
        if results[i] >= 100:
            break


players = start()
game(players)
    

        
        
        