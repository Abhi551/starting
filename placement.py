class student(object):
	
	def __init__(self,minsalary=[]):

			n=input("no of students :- ");
			self.n=n;
			for i in range(1,n+1):
				salary=input("enter minimum salary expected :- ");
				minsalary.append(salary);
			self.minsalary=minsalary;
			print minsalary;
				

			
		

class company(student):
	
	def no_of_company(self,selected=[]):
		m=input("no of companies");
		self.m=m;
		self.selected=selected;

	def salary_offered(self,qual=[]):
		for i in range(self.m):
			x=[];
			offer=input("salary offerred : ");
			x.append(offer);
			no_of_offers=input("no of offers : ");
			x.append(no_of_offers);
			qual.append(x);
		print qual;
		
	def select_candi(self):
		for i in range(self.n):
			status=[]
			for i in range(self.m):
				print "print 1 for selected else 0";
				x=input("enter :- ");
				print x;
				status.append(x);
			print status;	
			self.selected.append(status);
		print self.selected;

class selection(company):
	
	def __init__(self):
		for i  in company.selected:
			max=0;
			for j in range(i): 
				if i[j]==1 and  self.minsalary <= self.qual[j][0]:
					if max<=self.qual[j][0]:
						max=self.qual[j][0];
				



c=company();
s=selection();
c.no_of_company();
c.select_candi();
c.salary_offered();

