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
        userAggressionChoice = input("\nWhat would you like to set the computer's aggression level at? \nThe computer's aggresion level is the number at which they will bank their turn: ")
        return int(userAggressionChoice)


class Gameplay:
    def __init__(self):
        self.max_score = int(sys.argv[1])
        self.gameMode = input("What game mode would you like to play? \nA: Player 1 versus Player 2 \nB: Player 1 versus Computer\nC: Player 1 versus Player 2 versus Computer \nEnter A, B or C....")
        self.playerList = self.initialisePlayers()

    def initialisePlayers(self):
        playerList = []
        self.player1 = Player("Player 1")
        playerList.append(self.player1)
        if self.gameMode == "A":
            self.player2 = Player("Player 2")
            playerList.append(self.player2)
        elif self.gameMode == "B":
            self.player2 = Robot("Computer")
            playerList.append(self.player2)
        else:
            self.player2 = Player("Player 2")
            self.player3 = Robot("Computer")
            playerList.append(self.player2)
            playerList.append(self.player3)
        return playerList

    def game_start(self):
        for player in self.playerList:
            print ("Welcome {0}!\n".format(player.Name))
        print("==========================================\n")

        while max((self.player1.totalScore, self.player2.totalScore)) < self.max_score:
            for player in self.playerList:
                playerTurn = Turn(player,self.max_score)
                playerTurn.announceTurn()
                playerTurn.gameplay()
                if player.totalScore > self.max_score:
                    self.game_over()
                    break

    def game_over(self):
        winningPlayerName = ''
        winningPlayerScore = 0
        for player in self.playerList:
            if player.totalScore > winningPlayerScore:
                winningPlayerScore = player.totalScore
                winningPlayerName = player.Name
        print ("Congratulations {0}! - You have won with: {1} points".format(winningPlayerName,winningPlayerScore))

class Turn:
    def __init__(self,player,max_score):
        self.player = player
        self.turnscore = 0
        self.max_score = max_score
    def announceTurn(self):
        print ("{0}'s Turn!!\n".format(self.player.Name))

    def roll(self):
        return random.randint(1,6)

    def totalScoreMessage(self):
        print ("{0}'s Total Score is: {1}\n".format(self.player.Name,self.player.totalScore))
        print ("==========================================\n")

    def robotPlayAgain(self):
        play_again = "Yes"
        if self.turnscore > self.player.aggression_level or self.turnscore + self.player.totalScore > self.max_score:
            play_again = "No"
        return play_again

    def gameplay(self):
        print("\nYour turn score is: " +str(self.turnscore) + "\n")
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
                    play_again = input("\nWould you like to continue? Yes or No: ")
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

g = Gameplay()
g.game_start()
