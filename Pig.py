import random
class Player:
    def __init__(self,name):
        self.playerTotalScore = 0
        self.Name = name
        self.isRobot = False

class Robot:
    def __init__(self,name, aggression_level = None):
        self.playerTotalScore = 0
        self.Name = name
        self.isRobot = True
        self.aggression_level = aggression_level

class Gameplay:
    def __init__(self, robot = False):
        self.max_score = int(input("What would you like the winning number to be? "))
        self.robot = robot

    def game_start(self):
        self.player1 = Player("Player 1")
        if self.robot == False:
            self.player2 = Player("Player 2")
        else:
            self.player2 = Robot("Computer")
        print("Welcome {0} & {1} \n".format(self.player1.Name,self.player2.Name))
        while self.player1.playerTotalScore < self.max_score and self.player2.playerTotalScore < self.max_score:
            player1_turn = Turn(self.player1)
            player1_turn.announceTurn()
            player1_turn.gameplay()
            if self.player1.playerTotal > self.max_score:
                self.game_over()
            player2_turn = Turn(self.player2)
            player2_turn.announceTurn()
            player2_turn.gameplay()
        self.game_over()

    def game_over(self):
        if self.player1.playerTotalScore > self.player2.playerTotalScore:
            print ("Congratulations {0}! - You have won with: {1} points".format(self.player1.Name,self.player1.playerTotalScore))
        else:
            print ("Congratulations {0}! - You have won with: {1} points".format(self.player1.Name,self.player1.playerTotalScore))



class Turn:
    def __init__(self,player):
        self.player = player
        self.turnscore = 0
    
    def announceTurn(self):
        print ("{0}'s Turn!!\n".format(self.player.Name))

    def roll(self):
        return random.randint(1,6)

    def totalScoreMessage(self):
        print ("{0}'s Total Score is: {1}\n".format(self.player.Name,self.player.playerTotalScore))
        print ("==========================================\n")

    def robotPlayAgain(self):
        play_again = "Yes"
        if self.turnscore > 9:
            play_again = "No"
        return play_again

    def gameplay(self):
        print("Your turn score is: " +str(self.turnscore) + "\n")
        dice1 = self.roll()
        dice2 = self.roll()
        print('You rolled '+ str(dice1) + ' and ' + str(dice2) + "\n")
        if dice1 == 1 and dice2 == 1:
            self.player.playerTotalScore = 0
            self.totalScoreMessage()
            return self.player.playerTotalScore
        elif dice1 == 1 or dice2 == 1:
            self.turnscore = 0
            self.totalScoreMessage()
            return self.player.playerTotalScore
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
                    self.player.playerTotalScore +=self.turnscore
                    self.totalScoreMessage()
                    return self.player.playerTotalScore
                else:
                    print('Please enter a correct option')


## Note set Gameplay to "True" to intialise Robot, otherwise leave blank
g = Gameplay(False)
#g = Gameplay(True)
g.game_start()
