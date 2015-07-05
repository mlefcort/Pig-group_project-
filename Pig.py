# Winning number is taken as a command line argument
#e.g. if you want 100 to be the winning score
# when initialising the game enter "python3 Pig.py 100" at the command line


import sys
import random
class Player:
    def __init__(self,name):
        self.totalScore = 0
        self.Name = name
        self.isRobot = False

class Robot:
    def __init__(self,name):
        self.totalScore = 0
        self.Name = name
        self.isRobot = True
        self.aggression_level = self.chooseAggression()

    def chooseAggression(self):
        userAggressionChoice = input("What would you like to set the computer's aggression level at? \nThe computer's aggresion level is the number at which they will bank their turn: ")
        return int(userAggressionChoice)


class Gameplay:
    def __init__(self, robot = False):
        self.max_score = int(sys.argv[1])
        self.robot = robot
        self.playerList = self.initialisePlayers()

    def initialisePlayers(self):
        playerList = []
        self.player1 = Player("Player 1")
        playerList.append(self.player1)
        if self.robot == False:
            self.player2 = Player("Player 2")
        else:
            self.player2 = Robot("Computer")
        playerList.append(self.player2)
        return playerList

    def game_start(self):
        print("Welcome {0} & {1} \n".format(self.player1.Name,self.player2.Name))
        
        while max((self.player1.totalScore, self.player2.totalScore)) < self.max_score:
            for player in self.playerList:
                playerTurn = Turn(player)
                playerTurn.announceTurn()
                playerTurn.gameplay()
                if player.totalScore > self.max_score:
                    self.game_over()

    def game_over(self):
        if self.player1.totalScore > self.player2.totalScore:
            print ("Congratulations {0}! - You have won with: {1} points".format(self.player1.Name,self.player1.totalScore))
            break
        else:
            print ("Congratulations {0}! - You have won with: {1} points".format(self.player2.Name,self.player2.totalScore))
            break


class Turn:
    def __init__(self,player):
        self.player = player
        self.turnscore = 0
    
    def announceTurn(self):
        print ("{0}'s Turn!!\n".format(self.player.Name))

    def roll(self):
        return random.randint(1,6)

    def totalScoreMessage(self):
        print ("{0}'s Total Score is: {1}\n".format(self.player.Name,self.player.totalScore))
        print ("==========================================\n")

    def robotPlayAgain(self):
        play_again = "Yes"
        if self.turnscore > self.player.aggression_level:
            play_again = "No"
        return play_again

    def gameplay(self):
        print("Your turn score is: " +str(self.turnscore) + "\n")
        dice1 = self.roll()
        dice2 = self.roll()
        print('You rolled '+ str(dice1) + ' and ' + str(dice2) + "\n")
        if dice1 == 1 and dice2 == 1:
            self.player.totalScore = 0
            self.totalScoreMessage()
            return self.player.totalScore
        elif dice1 == 1 or dice2 == 1:
            self.turnscore = 0
            self.totalScoreMessage()
            return self.player.totalScore
        elif dice1 == dice2:
            self.turnscore = dice1 + dice2
            return self.gameplay()
        else:
            self.turnscore += dice1 + dice2
            play_again = None
            while play_again not in ["Yes","No"]:
                if self.player.isRobot == False:
                    play_again = input("Would you like to continue? Yes or No: ")
                    print('\n')
                else:
                    play_again = self.robotPlayAgain()
                if play_again == "Yes":
                    return self.gameplay()
                elif play_again == "No":
                    self.player.totalScore +=self.turnscore
                    self.totalScoreMessage()
                    return self.player.totalScore
                else:
                    print('Please enter a correct option')


## Note set Gameplay to "True" to intialise Robot, otherwise leave blank
#g = Gameplay(False)
g = Gameplay(True)
g.game_start()
