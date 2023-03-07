def minion_game(string):
    players_points = {'Stuart': 0 ,'Kevin': 0 } 
    vowels = {'A','E','I','O','U'}
    
    for i in range(len(string)):
        if string[i] in vowels:
            players_points['Kevin'] += len(string) - i
        else:
            players_points['Stuart'] += len(string) - i
    
    if players_points['Kevin'] > players_points['Stuart']:
        print(f'Kevin {players_points["Kevin"]}') 
    elif players_points['Kevin'] < players_points['Stuart']:
       print(f'Stuart {players_points["Stuart"]}')
    else:
        print('Draw')
                     
if __name__ == '__main__':
    s = input()
    minion_game(s)