from gameScore import gameScore

if __name__ == '__main__':
    num_of_players = int(input('Enter number of players: '))
    games = []
    for i in range(num_of_players):
        games.append(gameScore(10))
    previous_ball = [0]*num_of_players
    previous_frame = [1]*num_of_players
    current_frame = [1]*num_of_players

    def playGame(player):
        game = games[player]
        while(not game.gameIsOver()):
            current_frame[player] = game.rollingFrame
            if(current_frame[player] != previous_frame[player]):
                previous_ball[player] = 0
            a = int(input('Enter number between 0-'+str(10-previous_ball[player])+': '))
            while(a + previous_ball[player] > 10):
                a = int(input('Enter number between 0-'+str(10-previous_ball[player])+': '))
            print(game.roll(a))
            previous_ball[player] = a
            previous_frame[player] = current_frame[player]


    # game = games[0]
    # previous_ball = 0
    # previous_frame = 1
    # while(not game.gameIsOver()):
    #     current_frame = game.rollingFrame
    #     if(current_frame != previous_frame):
    #         previous_ball = 0
    #     a = int(input('Enter number between 0-'+str(10-previous_ball)+': '))
    #     while(a + previous_ball > 10):
    #         a = int(input('Enter number between 0-'+str(10-previous_ball)+': '))
    #     print(game.roll(a))
    #     previous_ball = a
    #     previous_frame = current_frame
    playGame(0)

    # i = 0    
    # previous_frame = 1
    # while(not games[i].gameIsOver()):
    #     current_frame = games[i].rollingFrame
    #     if(current_frame != previous_frame):
    #         i = (i+1)%num_of_players
    #     player = 'Player' + str(i+1)
    #     a = int(input(player+' please enter number between 0-10 '))
    #     games[i].roll(a)
    #     for j in range(num_of_players):
    #         print(games[j].frameScores)
    #     previous_frame = current_frame