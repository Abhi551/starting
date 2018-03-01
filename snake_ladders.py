import sys;
import random;
import time;
y=time.time();
class SnakesLadders:

    p1,p2,k,counter=0,0,0,0;

    def __init__(self):
        self.Ladders=Ladders={2:38,7:14,8:31,15:26,21:42,28:84,36:44,51:67,71:91,78:98,87:94}
        self.Snakes=Snakes={16:6,46:25,49:11,62:19,64:61,74:53,89:68,92:88,95:75,99:80};

    def game_over(self,player):
        print "Player %d Wins!."%player;
        return "Player %d Wins!."%player;


    def end_of_game(self,x):
        if x>100:
            x=100-(x-100);
            return x;
    def play(self,die1,die2):
        
        self.die1,self.die2=die1,die2;
        self.k=self.k+1;
        
        
        if self.k%2==1:
            self.p1+=die1+die2;
            if self.p1>100:
                self.p1=self.end_of_game(self.p1);
            if self.p1 in self.Ladders:
                self.p1=self.Ladders[self.p1];
            elif self.p1 in self.Snakes:
                self.p1=self.Snakes[self.p1];
            print "p1",self.p1;
            if self.p1==100:
                self.game_over(1);
                print "Game Over";
                exit(1);
            if die1==die2:
                self.k=self.k-1;
            
            return "player 1 is on square %d"%self.p1;

        
        if self.k%2==0:
            self.p2+=die1+die2;
            if self.p2>100:
                self.p2=self.end_of_game(self.p2);
            if self.p2 in self.Ladders:
                self.p2=self.Ladders[self.p2];
            elif self.p2 in self.Snakes:
                self.p2=self.Snakes[self.p2];
            print "p2",self.p2;
            if self.p2==100:
                self.game_over(2);
                print "Game Over";
                exit(1);
            if die1==die2:
                self.k=self.k-1;
            return "player 2 is on square %d"%self.p2;

s=SnakesLadders()
for i in range(30):
    s.play(random.randint(1,6),random.randint(1,6))


