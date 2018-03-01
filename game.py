from sys import exit;
from random import randint; 


class Engine(object):

	def __init__(self,scene_map):
		self.scene_map=scene_map;

	def play(self):
		
		current_scene=self.scene_map.opening_scene()
		while True:
			print "";
			next_scene_name=current_scene.enter();
			current_scene=self.scene_map.next_scene(next_scene_name);


class Scene(object):

	def  enter(self):
		print "this scene not completed";
		exit(1);

class Death(Scene):
	quips=[
			"you died . You kinda at this",
			"Your mom would be proud.......of she were smarter",
			"Such a  loser",
			"Even a small puppy is better at this"
	];

	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)];
		exit(1);

class Central_Corridor(Scene):

	def enter(self):
		print "the gothons of planet #25 have invaded your ship and destroyed";
		print "your entire crew is dead , u r the last surviving member and your last";
		print "mission is to get the nuetron destruct bomb from the weapon armory";
		print "put it in the bridge , and blow the ship up after getting into an escape pod ";
		print "\n you're running down the central corridor to the  weapons Armory when";
		print "a Gohton jumps out , red scaly skin , dark grimy teeth , and evil clown costume ";
		print "flowing around his hate filled body  . He's blocking the door to armory";

		action =raw_input(">>");
		if action=="shoot":
			print "you are dead";
			return 'Death';
		elif action=="dodge":
			print "your head gets eaten ";
			return "death";

		elif action=="tell a joke":
			return "laser weapon armory";

		else :
			print "doesn't understand";
			return "central_corridor";

		
	pass;

class Weapons(Scene):
		
	def enter(self):
		print "you look for weapons  in room";
		print "to get weapons , enter three digits code";
		code="%d%d%d"%(randint(1,3),randint(1,3),randint(1,3));
		guess=input("keypad>>");
		guesses=0;
		while guess!=code and guesses<10:
			print "BZZZZED!!!";
			guesses+=1;
			guess=input("keypad>>");
		if guess==code:
			print "you grab the bomb";
			return "bridge"
		else :
			return "death";



class Bridge(Scene):
	
	def enter(self):
		print "you go to the brdige with bomb";

		action =raw_input(">>");

		if action=="throw the bomb":
			print "Gothons shoot back at you";
			print "bomb goes off ";
			return "death";
		elif action=="slowly place bomb":
			print "bomb is placed";
			print "run to escape pod";
			return "escape_pod";
		else :
			print "does not compute";
			return "the_bridge";

class Escape_pod(Scene):
	
	def enter(self):
		print "you rush through the ship trying to make it";
		print "there are 5 pods  ";
		print "which one will you choose ???? HURRY!!";
		good_pod=randint(1,3)
		guess=raw_input("pod chosen>>");

		if int(guess)!=good_pod:
			print "you jump into pod %s"%guess;
			print "entered into a void space";
			return "death";
		else :
			print "you jump into pod %s "%guess;
			print "you reach your planet safely";
			print "YOU WON!!!";

			return "FINISHED!!!!!!";

class Map(object):

	scenes={
			"central_corridor":Central_Corridor(),
			"weapon":Weapons(),
			"the_bridge":Bridge(),
			"escape_pod":Escape_pod(),
			"death":Death()
			}

	def __init__(self,scene_map):
		self.scene_map=scene_map;



	def next_scene(self,start_scene):
		return Map.scenes.get(start_scene)


	def opening_scene(self):
		return self.next_scenes(self.scene_map);


a_map=Map("central_corridor");
a_game=Engine(a_map);
a_game.play();


def gold_room():
	print "this room is full of gold. How much  do u need ?????";
	print "ur  choice";
	next=input(">");

	if next<52:
		print "Nice , u r not greedy";
		print "u win.........";
		exit(0);
	else :
		dead("u r greedy");

def bear_room():
	print "there is a bear ";
	print "he has honey and is sitting in front of another door";
	print "what u r going to do?????????";
	bear_moved=False;
	print "you will have following choices \n 1. take honey \n 2. taunt bear ";
	while True:
		next=raw_input(">");

		if next=="take honey":
			dead("the bear looks at u and slapps u.");
		elif next=="taunt bear" and not bear_moved:
			print "the bear moved , u r safe ";
			bear_moved=True;
			print "what next???????";
			print "ur choices are \n 1. open door \n2. taunt bear";
			next=raw_input(">");
			if next=="taunt bear" and bear_moved:
				dead("the bear is pissed off and kill u");
			elif next=="open door" and bear_moved:
				gold_room();
		else :
			print "print again";

def cthulhu_room():
	print "here u see great evil Cthulhu";
	print "He stares at you and you go insane";
	print "Do you flee or eat ur head";

	next=raw_input(">");

	if "flee" in next:
		start();
	elif "head" in next :
		dead("well that was tasty");
	else :
		cthulhu_room();

def dead(why):
	print why,"good job";
	exit(0);

def start():
	print "you r in a dark room";
	print "there is door to your right and left ";
	print "ur choice ????????";
	next=raw_input(">");

	if next=="left":	
		bear_room();
	elif next=="right":
		cthulhu_room();
	else : 
		dead("u r lostb in a maze forever till u starve and die");



