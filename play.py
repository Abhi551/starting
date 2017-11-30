class queens(object):
	
	def __init__(self,n):
		self.n=n;
		self.board=[[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0]];
		
	def change_to_two(self,row,column):
		x=1;
		while row+x<4:
			self.board[row+x][column]=2;
			x+=1;
		x=1;
		while row-x>-1:
			self.board[row-x][column]=2;
			x+=1;
		x=1;
		while column+x<4:
			self.board[row][column+x]=2;
			x+=1;
		x=1;
		while column-x>-1:
			self.board[row][column-x]=2;
			x=x+1;
		x=1;
		while row-x>-1 and column-x>-1:
			self.board[row-x][column-x]=2;
			x+=1;
		x=1;
		while row+x<4 and column+x<4:
			self.board[row+x][column+x]=2;
			x+=1;
		x=1;
		while row-x<-1 and column-x>-1:
			self.board[row-x][column-x]=2;
			x+=1;
		x=1
		while row-x>-1 and column+x<4:
			self.board[row-x][column+x]=2;
			x+=1;
		x=1;
		while column-x>-1 and row+x<4:
			self.board[row+x][column-x]=2;
			x+=1;		
	def show(self):
		for i in range(4):
			print self.board[i];
		print "\n"

	def function(self): #function  for recursion of board
		pass;
	def change_to_one(self):
		for i in self.board:
			if 0 in i:
				for k in range(4):
					for j in range(4):
						if self.board[k][j]==0:
							self.board[k][j]=1;
							self.change_to_two(k,j);
						

		
	def place(self,inc):
		self.row=0;
		self.column=0;
		self.board[self.row][self.column]=1;
		for i in range(4):
			for j in range(4):
				if self.board[i][j]==1:
					self.change_to_two(i,j);
					self.change_to_one(); 

	


x=queens(4);
x.place(0);