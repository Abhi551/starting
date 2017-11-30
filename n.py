def nqueens(a):
	for i in range(4):
		a[0][1]=1;
		for i in range(4):
			if a[i][0]==0:
				a[i][0]=2;
			if a[0][i]==0:
				a[0][i]=2;
		print a;
	for i in range(4):
		for j in range(4):
			if a[i][j]==1:
				s=i;
				t=j;
	while s<3 and t<3:
		a[s+1][t+1]=2;
		s,t=s+1,t+1;
		print a;
	while s>0 and t>0:
		a[s-1][t-1]=2
		s,t=s-1,t-1;
		print a;
	while s>0 and t<4:
		a[s-1][t+1]=2;
		s,t=s-1,t+1;
	while s<4 and t>0:
		a[t-1][s+1]=2;
		t,s=t-1,s+1;
	return a;
