#include<iostream>
#include <cstdlib>
#include <ctime>
#include<fstream>
#include<windows.h>
using namespace std;
void otpp();
void transcation();
void balanceinquiry();
void fastcash();
void userdetail();
void pinchange();
void rcpt();
void datetime();
int otp ,newpin,yyy,mmm,ddd,amount,wdamount,pin;
string name,address,type;
static int B=0;

int main(){
    int key,abc,choice;
    char receipt;
gett:
    transcation();
    cout<<"1.Enter your pin"<<endl;
    cout<<"2.Generate OTP for pin"<<endl;
    cout<<"3.Creat a account"<<endl;
    cout<<"4.Exit"<<endl;
    cin>>choice;
    switch (choice)
    
    {
    case 1:
        cout<<"Enter the pin:";
        get:  cin>>key;
        if(key==pin){
        cout<<"1.Balance Inquiry"<<endl;
        cout<<"2.Fast Cash"<<endl;
        cout<<"3.Cash Withdrawl"<<endl;
        cout<<"4.Pin Change"<<endl;
        cin>>choice;
        switch (choice)
        {
            case 1:

                balanceinquiry();
                break;
            case 2:

                fastcash();

                int b;
                cin>>b;
                    if(b==1){

                    transcation();

                    cout<<"Do you wanna receive receipt(y/n):";
                    cin>>receipt;
                    if(receipt=='y'){
                    cout<<"              Transaction Receipt"<<endl;
                    cout<<"                 Pragyan Bank"<<endl;
                    datetime();
                    cout<<endl;
                    cout<<"Withdrawal amount : 500.00"<<endl;
                    cout<<"Charge amount: 0.00"<<endl;
                    cout<<"Remaining balance:"<<(amount-1000)-500;
                    cout<<"Thank you for using our ATM.";
                    } 
                    if(receipt=='n'){
                        cout<<"Thank you for using our ATM.";
                    }
                        }

                    else if(b==2){

                        transcation();

                  cout<<"Do you wanna receive receipt(y/n):";
                  cin>>receipt;
                  if(receipt=='y'){
                   cout<<"              Transaction Receipt"<<endl;
                   cout<<"                 Pragyan Bank"<<endl;
                   datetime();
                   cout<<endl;
                   cout<<"Withdrawal amount : 1000.00"<<endl;
                   cout<<"Charge amount: 0.00"<<endl;
                   cout<<"Remaining balance:"<<(amount-1000)-1000;
                   cout<<"Thank you for using our ATM.";
                  }
                  if(receipt=='n'){
                   cout<<"Thank you for using our ATM.";
                  }
                  }

                  else if(b==3){

                    transcation();

                  cout<<"Do you wanna receive receipt(y/n):";
                  cin>>receipt;
                  if(receipt=='y'){
                   cout<<"              Transaction Receipt"<<endl;
                   cout<<"                 Pragyan Bank"<<endl;
                   datetime();
                   cout<<endl;
                   cout<<"Withdrawal amount : 2000.00"<<endl;
                   cout<<"Charge amount: 0.00"<<endl;
                   cout<<"Remaining balance:"<<(amount-1000)-2000;
                   cout<<"Thank you for using our ATM.";
                  }
                  if(receipt=='n'){
                   cout<<"Thank you for using our ATM.";
                  }
                  }

                  else if(b==4){

                    transcation();

                  cout<<"Do you wanna receive receipt(y/n):";
                  cin>>receipt;
                  if(receipt=='y'){
                   cout<<"              Transaction Receipt"<<endl;
                   cout<<"                 Pragyan Bank"<<endl;
                   datetime();
                   cout<<endl;
                   cout<<"Withdrawal amount : 5000.00"<<endl;
                   cout<<"Charge amount: 0.00"<<endl;
                   cout<<"Remaining balance:"<<(amount-1000)-5000;
                    cout<<"Thank you for using our ATM.";
                }
                if(receipt=='n'){
                    out<<"Thank you for using our ATM.";
                }
                }
                
                else if(b==5){

                    transcation();

                cout<<"Do you wanna receive receipt(y/n):";
                cin>>receipt;
                if(receipt=='y'){
                    cout<<"              Transaction Receipt"<<endl;
                    cout<<"                 Pragyan Bank"<<endl;
                    datetime();
                    cout<<endl;
                    cout<<"Withdrawal amount : 10000.00"<<endl;
                    cout<<"Charge amount: 0.00"<<endl;
                    cout<<"Remaining balance:"<<(amount-1000)-10000;
                    cout<<"Thank you for using our ATM.";
                    }
                if(receipt=='n'){
                    cout<<"Thank you for using our ATM.";
                  }
                  }

                  else if(b==6){

                    transcation();

                  cout<<"Do you wanna receive receipt(y/n):";
                  cin>>receipt;
                  if(receipt=='y'){
                    cout<<"              Transaction Receipt"<<endl;
                    cout<<"                 Pragyan Bank"<<endl;
                    datetime();
                    cout<<endl;
                   cout<<"Withdrawal amount : 15000.00"<<endl;
                   cout<<"Charge amount: 0.00"<<endl;
                   cout<<"Remaining balance:"<<(amount-1000)-15000;
                   cout<<"Thank you for using our ATM.";
                  }
                  if(receipt=='n'){
                   cout<<"Thank you for using our ATM.";
                   exit(0);
                  }
                  }
                
               break;
  
             case 3:
               cout<<"Cash withdraw"<<endl;
               here: cout<<"Enter the amount you want to withdrawl:";
               cin>>wdamount;
               if(wdamount<(amount-1000)){
                int aa;
                  transcation();
                  cout<<"Do you wanna receive receipt(y/n):";
                  cin>>aa;
                  if(aa='y'){
                    rcpt();
                  }
                  else{
                    cout<<"Thank you for using our ATM.";
                    exit(0);
                  }
                  

               }
               else{
                char P;
                cout<<"Insufficient Balance !!!!"<<endl;
                cout<<"Re-enter the amount ?(y/n)";
                cin>>P;
                if(P=='y'){
                  goto here;
                }
                else{
                 exit(0);
                }
               
               }
                 
               break;
             case 4:

               pinchange();

               break;

             default:
             break;
            } 
         }
        else{
              B++;
              if(B>2){
                cout<<"You have entered wrong pin 3 times !!!"<<endl;
                cout<<"Try again after 15 minutes."<<endl;
                exit(0);
              }
             cout<<"Incorrect pin!!"<<endl;
             cout<<"Re-enter the pin:";
          
             goto get;
         }
       break;


       case 2:

         otpp();
         cout<<"OTP has been sent to the file 'APP' "<<endl;

         cout<<"Enter the  OTP:";
          take :
          cin>>abc;
         if(abc==otp){
           cout<<"Set a new pin:";
           cin>>newpin;
           pin=newpin;
           cout<<"Your new pin has been successfully changed."<<endl;
           goto gett;
         }
         else{
          int A=1;
          if(A>3){
            cout<<"You have entered wrong OTP 3 times !!!"<<endl;
            cout<<"Further process Terminated due to security reason"<<endl;
            exit(0);
          }
          cout<<"Incorrect OTP!!!"<<endl;
          cout<<"Re-enter the OTP"<<endl;
          A++;
          goto take;
         }
         break;
       case 3:

         userdetail();
         cout<<"Rs.1000 will be on hold.you cannot withdrawl this until you close the account."<<endl<<endl;

         goto gett;
         break;
       case 4:
         exit(0);
         break;

       default:
       break;
      }

}
void otpp(){
  srand(time(NULL));      
   otp = ( rand() % 999999 ) +100000; //Generates OTP
  ofstream file("APP.txt",ios::out);
     file<<otp;
     file.close();
     
}

void transcation(){
   cout<<"Your transaction is being processed ";
   for(int i=0;i<6;i++){
      cout<<"."<<" ";
      Sleep(500);
    }cout<<endl;
}

void balanceinquiry(){
   cout<<"Account Holder's Name:"<<name<<endl;
   cout<<"Actual balance is:"<<amount<<endl;
   cout<<"Available balance is:"<<(amount-1000)<<endl;
   cout<<"Interest Rate: 7.4 %"<<endl;
}

void fastcash(){
   
   cout<<"1. 500"<<endl;
   cout<<"2. 1000"<<endl;
   cout<<"3. 2000"<<endl;
   cout<<"4. 5000"<<endl;
   cout<<"5. 10000"<<endl;
   cout<<"6. 15000"<<endl;
   
}

void userdetail(){
   cout<<"Enter the following data:"<<endl;
   cout<<"Full Name:";
   cin>>name;
   getline(cin,name);
   cout<<"Permanent Address:";
   getline(cin,address);
   cout<<"Date of birth (yyyy/mmmm/dddd):";
   cin>>yyy>>mmm>>ddd;
   cout<<"Account type:";
   cin>>type;
   cout<<"Deposite amount:";
   cin>>amount;
}

void pinchange(){
      cout<<"Enter the new pin:";
      cin>>newpin;
      pin=newpin;
}

void rcpt(){
   cout<<"              Transaction Receipt"<<endl;
   cout<<"                 Pragyan Bank"<<endl;
   datetime();
   cout<<endl;
   cout<<"Withdrawl Amount: "<<wdamount<<endl;
   cout<<"Transaction Charge: 0.00"<<endl;
   cout<<"Remaining balance:"<<(amount-1000)-wdamount<<endl;
   cout<<"           Thank you for using our ATM"<<endl;
}

void datetime(){
  time_t now = time(0);
  char* dt= ctime(&now);
  cout<<"Date & Time:"<<dt<<endl;
}