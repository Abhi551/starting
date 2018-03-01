k=0;
TOL=0;
A,b,x=[],[],[]
#A=[[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]]
x1=[0,0]

n=input('no of iterations ' )
N=input('Enter the no of variables : ');
sum=0
for i in range(N):
	a=input('Enter the values of equations ')
	x.append(0.0)
	b.append(float(a))
print 'b = ',b
print 'x = ',x
for i in range(N):
	a=[]
	for j in range(N):
		y=input("Enter the elements :")
		a.append(float(y));
	A.append(a)

for i in range(N):
			print A[i]
while k<n:
	for i in range(N):
		for j in range(N):
			if i!=j:
				sum=sum+A[i][j]*x[j]
			#print 'sum',sum
			x1[i]=float((b[i]-sum)/(float(A[i][i])))
		sum=0
	x=x1
	print x
	k=k+1








