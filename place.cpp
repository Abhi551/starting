//Anubhav Pratik
// 15MA20008

#include<iostream>
#include<vector>
#define Companies 15
#define Students 10

using namespace std;


class student
{
public:
 long int minimum_salary;
 long double cgpa;
 int selecetd[Companies];
};

class company
{
public:
 long int Salary_offer;
 long double min_cgpa;
 int max_job_offers;
};


int main()
{
 int N,M,offers_done[Companies]={0},job_stud=0,comp_j=0,zero_job=0;
 long int total_salary=0,max=0;
 cout<<"Number of Students participated in Placement ";
 cin>>N;
 cout<<"\nTotal number of Companies taken part in Placement ";
 cin>>M;
 vector<class student > stud(N);
 vector<class company > comp(M);
 cout<<"\nMinimum salaries Expected by Each Student : \n";
 for(int i=0;i<N;i++)
 {
  cout<<"minimum_salary Expected for Student"<<i+1<<" --> ";
  cin>>stud[i].minimum_salary;
 }
 cout<<"\n CGPA  of the students : \n";
 for(int i=0;i<N;i++)
 {
  cout<<"CGPA for student "<<i+1<<" --> ";
  cin>>stud[i].cgpa;
 }
 cout<<"\nEnter  salaries which company provides : \n";
 for(int i=0;i<M;i++)
 {
  cout<<" Salary provided by the company "<<i+1<<" --> ";
  cin>>comp[i].Salary_offer;
 }
 cout<<"\n Maximum Job Vacancies in each company : \n";
 for(int i=0;i<M;i++)
 {
  cout<<"Maximum Job Vacancies in the company "<<i+1<<" --> ";
  cin>>comp[i].max_job_offers;
 }
 cout<<"\n Minimum CGPA required by the companies : \n";
 for(int i=0;i<M;i++)
 {
  cout<<"Minimum CGPA required by  company "<<i+1<<" --> ";
  cin>>comp[i].min_cgpa;
 }
 for(int i=0;i<N;i++)
 {
  for(int j=0;j<M;j++)
  {
   if(stud[i].cgpa>=comp[j].min_cgpa)
   {
    stud[i].selecetd[j]=1;
   }
   else
   {
    stud[i].selecetd[j]=0;
   }
   cout<<stud[i].selecetd[j]<<" ";
  }
  cout<<"\n";
 }
 for(int i=0;i<N;i++)
 {
  max=0,comp_j=0;
  for(int j=0;j<M;j++)
  {
   if(stud[i].selecetd[j]==1)
   {
    if((comp[j].Salary_offer>max)&&(offers_done[j]<comp[j].max_job_offers))
    {
     max=comp[j].Salary_offer;
     comp_j=j;
    }
   } 
  }
  if((max>=stud[i].minimum_salary)&&(offers_done[comp_j]<comp[comp_j].max_job_offers))
  {
   total_salary+=max;
   offers_done[comp_j]++;
   job_stud++;
   cout<<i<<"a";
  }
 }
 for(int i=0;i<M;i++)
 {
  if(offers_done[i]==0)
  {
   zero_job++;
  }
 }
 cout<<" Students Recruited by Companies : "<<job_stud<<"\n"<<"total_salary "<<total_salary<<"\n"<<"Companies which didn't  selected any one student : "<<zero_job<<"\n";
 return 0;
}