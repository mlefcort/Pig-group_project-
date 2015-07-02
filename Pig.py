import random
class Player:
    def __init__(self,name):
        self.playerTotalScore = 0
        self.Name = name


class Gameplay:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.max_score = int(input("What would you like to play up to? "))

    def game_start(self):
        print("Welcome {0} & {1} \n".format(self.player1.Name,self.player2.Name))
        while self.player1.playerTotalScore < self.max_score and self.player2.playerTotalScore < self.max_score:
            player1_turn = Turn(self.player1)
            player1_turn.announceTurn()
            player1_turn.gameplay()
            player2_turn = Turn(self.player2)
            player2_turn.announceTurn()
            player2_turn.gameplay()
        print ("Game Over")

class Turn:
    def __init__(self,player):
        self.player = player
        self.turnscore = 0
    
    def announceTurn(self):
        print ("{0}'s Turn!!".format(self.player.Name))

    def roll(self):
        return random.randint(1,6)
    def gameplay(self):
        print("Your turn score is " +str(self.turnscore) + "\n")
        dice1 = self.roll()
        dice2 = self.roll()
        print('You rolled '+ str(dice1) + ' and ' + str(dice2) + "\n")
        if dice1 == 1 and dice2 == 1:
            self.player.playerTotalScore = 0
            return self.player.playerTotalScore
        elif dice1 == 1 or dice2 == 1:
            self.turnscore = 0
            return self.player.playerTotalScore
        elif dice1 == dice2:
            self.turnscore = dice1 + dice2
            return self.gameplay()
        else:
            self.turnscore += dice1 + dice2
            play_again = 0
            while play_again not in ["Yes","No"]:
                play_again = input("Would you like to continue? Yes or No: ")
                print('\n')
                if play_again == "Yes":
                    return self.gameplay()
                if play_again == "No":
                    self.player.playerTotalScore +=self.turnscore
                    print(self.player.playerTotalScore)
                    return self.player.playerTotalScore
                else:
                    print('Please enter a correct option')

g = Gameplay()
g.game_start()
