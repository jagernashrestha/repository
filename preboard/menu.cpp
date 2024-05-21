#include <iostream>
#include <fstream>
#include <string.h>
#include <conio.h>
#include <cstdio>
#include <stdlib.h>
#include <ctime>
#include <windows.h>
#include <dos.h>
#include <graphics.h>
#include <unistd.h>
using namespace std;
struct r
{
    char dish[50];
    string uname = "admin";
    string up_w = "admin";
    int key;
    float price;
} r;
class Resturant
{
public:
    void add_menu();
    void query();
    void display();
    void update();
    void delet();
    void admin();
    void introduction();
};
void Resturant::add_menu()
{
    char a;
    int k;
    fstream obj;
jaks:
    do
    {
        obj.open("resturant.txt", ios::in | ios::binary);
        cout << "Enter the dish key: ";
        cin >> k;
        while (obj.read((char *)&r, sizeof(r)))
        {
            if (r.key == k)
            {
                cout << "key is already exist! " << endl;
                obj.close();
                goto jaks;
            }
        }
        obj.close();
        obj.open("resturant.txt", ios::app | ios::binary);
        r.key = k;
        cin.ignore();
        cout << "ENTER THE DISH NAME: ";
        gets(r.dish);
        cout << "ENTER THE DISH PRICE: ";
        cin >> r.price;
        obj.write((char *)&r, sizeof(r));
        cout << " Do you want to add an other [y/n]: ";
        cin >> a;
        obj.close();
    } while (a == 'y' || a == 'Y');
}
void Resturant::display()
{
    int c = 0;
    fstream obj;
    obj.open("resturant.txt", ios::in | ios::binary);
    cout << "\tKey\t\tDISH NAME\t\tPRICE" << endl;
    while (obj.read((char *)&r, sizeof(r)))
    {
        cout << "\t" << r.key << "\t\t" << r.dish << "\t\t\t" << r.price << endl;
        c++;
    }
    if (c == 0)
    {
        cout << "list is empty" << endl;
    }

    obj.close();
}
/*void Resturant::query()
{
    int a, c = 0;
    fstream obj;
    obj.open("resturant.txt", ios::in);
    cout << "enter the dish key:";
    cin >> a;
    while (obj.read((char *)&r, sizeof(r)))
    {
        if (r.key == a)
        {
            cout << "\t" << r.key << "\t\t" << r.dish << "\t\t\t" << r.price << endl;
            c++;
        }
    }
    if (c == 0)
    {
        cout << "not found" << endl;
    }
    obj.close();
*/
void Resturant::update()
{
    int a, p, c = 0;
    fstream obj;
    obj.open("resturant.txt", ios::in | ios::out | ios::binary);
    cout << "enter the dish key:";
    cin >> a;
    obj.seekg(0);
    while (obj.read((char *)&r, sizeof(r)))
    {
        if (r.key == a)
        {
            cout << "destinatio record:" << endl;
            cout << "\t" << r.key << "\t\t" << r.dish << "\t\t\t" << r.price << endl;
            p = obj.tellg() - (sizeof(r));
            obj.seekp(p);
            cout << "enter the dish key:";
            cin >> r.key;
            cin.ignore();
            cout << "ENTER THE DISH NAME:";
            gets(r.dish);
            cout << "ENTER THE DISH PRICE:";
            cin >> r.price;
            obj.write((char *)&r, sizeof(r));
            c++;
        }
    }
    if (c == 0)
    {
        cout << "not found" << endl;
    }

    obj.close();
}
void Resturant::delet()
{
    int a, c;
    fstream obj, obj1;
    obj.open("resturant.txt", ios::in | ios::binary);
    obj1.open("temp.txt", ios::app | ios::binary);
    cout << "enter the dish key:";
    cin >> a;
    while (obj.read((char *)&r, sizeof(r)))
    {
        if (r.key == a)
        {
            c++;
            cout << "\t" << r.key << "\t\t" << r.dish << "\t\t\t" << r.price << endl;
            cout << "destination record is deleted" << endl;
        }
        if (r.key != a)
        {
            obj1.write((char *)&r, sizeof(r));
        }
    }
    obj.close();
    obj1.close();
    if (c == 0)
    {
        cout << "not found" << endl;
    }
    remove("resturant.txt");
    rename("temp.txt", "resturant.txt");
}
void Resturant::admin()
{
    char a;
    int kkkk;
    string get_uname;


    cout << "Enter your user id : ";
    login:
    cin.ignore();
    //getline(cin,get_uname);
    cin>>get_uname;
    if (get_uname == r.uname)
    {  
        cout << "Enter your user password: ";
        pass:
        kkkk= getch();
            string enteredPin;
            while (kkkk != 13)
            {
                enteredPin.push_back((char)kkkk);
                cout << "*";
                kkkk = getch();
                
            }
        
        if (enteredPin == r.up_w)
        {
            cout<<endl;
            do
            {
                SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 6);
                cout << "\t\t\t\t\t\t_________________________" << endl;
                cout << "\t\t\t\t\t\t|||||||||||||||||||||||||" << endl;
                cout << "\t\t\t\t\t\t|                       |" << endl;
                cout << "\t\t\t\t\t\t|  1) ADD DISH          |" << endl;
                cout << "\t\t\t\t\t\t|  2) Display           |" << endl;
                cout << "\t\t\t\t\t\t|  3) UPDATE            |" << endl;
                cout << "\t\t\t\t\t\t|  4) DELETE            |" << endl;
                cout << "\t\t\t\t\t\t|  0) EXIT TO MAIN MANU |" << endl;
                cout << "\t\t\t\t\t\t|                       |" << endl;
                cout << "\t\t\t\t\t\t|_______________________|" << endl;
                cout << "\t\t\t\t\t\tSelect the key: ";
                cin >> a;
                switch (a)
                {
                case '0':
                    break;
                case '1':
                    system("CLS");
                    add_menu();
                    break;
                case '2':
                    system("CLS");
                    display();
                    break;
                
                case '3':
                    system("CLS");
                    update();
                    break;
                case '4':
                    system("CLS");
                    delet();
                    break;
                }
            } while (a != '0');
        }
        else
        {
            cout << "\n\nEnter correct password!!: " ;
            goto pass;
        }
    }
    else
    {
        cout << "\n\nEnter the correct username!!!!: " ;
        goto login;
    }
}
struct
{
    char d[50];
    float p, amount;
    int qty, bill_no;
    string cust_name;

} rd;
class customer : public Resturant
{
public:
    void bill();
    void showbill();
    void dish_menu();
    void billnum();
    
};

void customer::billnum()
    {
        string pp;
        fstream p;
        p.open("billnum.txt");
        getline(p, pp);
        p.close();
        cout << " Bill no:" << pp << endl;
        rd.bill_no= stoi(pp);
        int b = stoi(pp);
        b++;
        p.open("billnum.txt");
        p << b;
        p.close();
        cout<<" Name: "<<rd.cust_name<<endl;
    }


void customer::bill()
{
    int grandtotal;
    int a, c = 0;
    char ch;
    float total = 0;
    fstream obj, obj1;
    dish_menu();
    obj1.open("bill.txt", ios::out | ios::binary);
    do
    {
        obj.open("resturant.txt", ios::in | ios::binary);
        cout << "Enter the dish key: ";
        cin >> a;
        while (obj.read((char *)&r, sizeof(r)))
        {
            if (r.key == a)
            {
                c++;
                cout << "Enter the quantity: ";
                cin >> rd.qty;
                rd.amount = rd.qty * r.price;
                cout << "\t" << r.dish << "\t\t" << r.price << "*" << rd.qty << "\t\t" << rd.amount << endl;
                strcpy(rd.d, r.dish);
                rd.p = r.price;
                obj1.write((char *)&rd, sizeof(rd));
                total = total + rd.amount;
                grandtotal=total;
            }
        }
        if (c == 0)
        {
            cout << "Not found" << endl;
        }

        cout << "Do you want to order more [y/n]? ";
        cin >> ch;
        obj.close();
    } while (ch == 'y' || ch == 'Y');
    obj1.close();
    if (total>1000 && total<3000)
            { SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 2);
                cout<<endl;
               cout<<"Your order is more than 1000"<<endl;
                cout<<"FREE!!! 1 CONFECTIONERY  items"<<endl;
        cout << "\t\t\t\t\t\t __________________" << endl;
        cout << "\t\t\t\t\t\t|    Bon Appetite  |" << endl;
        cout << "\t\t\t\t\t\t|__________________|" << endl;
        cout << "\t\t\t\t\t\t|                  |" << endl;
        cout << "\t\t\t\t\t\t|    1)waffles     |" << endl;
        cout << "\t\t\t\t\t\t|    2)macaroon    |" << endl;
        cout << "\t\t\t\t\t\t|    3)cupcake     |" << endl;
        cout << "\t\t\t\t\t\t|    4)pastry      |" << endl;
        cout << "\t\t\t\t\t\t|__________________|" << endl;
        cout << "\t\t\t\t\t\tSelect from the options: ";
        cin >> a;
        switch (a)
        {
        case 1:
        cout<<"\t\t\t~Enjoy your waffles~ "<<endl;
            break;
        case 2:
        cout<<"\t\t\t~Enjoy your macaroon~"<<endl;
            break;
        case 3:
        cout<<"\t\t\t~Enjoy your cupcake~"<<endl;
            break;
        case 4 :
        cout<<"\t\t\t~Enjoy your pastry~"<<endl;
        break;
        default:
        cout<<"\t\t\t~Invalid option~"<<endl;
        }
           }
            else if(total>3000)
           {
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 2);
            cout<<endl;
            cout<<"Your order is more than 3000"<<endl;
            cout<<"5% discount on total purchase"<<endl;
            grandtotal= total-(0.05*total);
            
           } 
    cout<<"\n\n\nEnter the name: ";
    cin.ignore();
    getline(cin,rd.cust_name);
   
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 7);
    cout << "..............................GENERATING BILL.............................." <<endl;
    
   
     for (int k=3;k<7;k++)
    {
for(int x=k; x<7;x++)
    { 
    
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),x);
        cout<<"  .";
        sleep(1);
      
    }

    }
    system("CLS");
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 4);
    cout << endl;
    billnum();
    
    cout << " ____________________________________________________________________________________________________________" << endl;
    cout << "|                                                                                                            |" << endl;
    cout << "| -----------------------------------------------------------------------------------------------------------|" << endl;
    cout << "|                                            JAKS FOOD HUB                                                   |" << endl;
    cout << "|                                                BILL                                                        |" << endl;
    cout << "|............................................................................................................|" << endl;
    showbill();
    cout << "|............................................................................................................|" << endl;
    cout << "|\t\t\t\t\t\t\t\t\tTOTAL=" << total << "  \t\t\t     |" << endl;
    cout <<"|\t\t\t\t\t\t\t\t\tGRANDTOTAL=" << grandtotal << "  \t\t\t   |" << endl;
    cout << "|------------------------------------------------------------------------------------------------------------|" << endl;
    cout << "|____________________________________________________________________________________________________________|" << endl;
    cout << "|                                   ~THANK YOU FOR USING OUR SERVICE~                                        |" << endl;
    cout << "|____________________________________________________________________________________________________________|" << endl;
    
}
void customer::showbill()
{

    fstream obj;
    obj.open("bill.txt", ios::in | ios::binary);
    cout << "\tDISH NAME\t\tPRICE\t\tQTY\t\tAMOUNT" << endl;
    while (obj.read((char *)&rd, sizeof(rd)))
    {

        cout << "\t" << rd.d << "\t\t\t" << rd.p << "\t\t" << rd.qty << "\t\t" << rd.amount << endl;
    }
    obj.close();
}
void customer::dish_menu()
{
    fstream obj;
    obj.open("resturant.txt", ios::in | ios::binary);
    while (obj.read((char *)&r, sizeof(r)))
    {

        cout << "\t\t" << r.key << ") " << r.dish << "-------RS  " << r.price << endl;
    }
    obj.close();
}

void Resturant:: introduction()
 { cout<<"\t\t\t";
for (int h=3;h<15;h++)
    {
for(int x=h; x<15;x++)
    { 
    
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),x);
        cout<<"*";
    }
    }
cout<<endl;
SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),5);
cout<<"\t\t\t||                     Welcome to JAKS FOOD MENU                            ||"<<endl;
cout<<"\t\t\t||                 .Innovation.Iniciative.Imagination.                      ||"<<endl;
cout<<"\t\t\t||--------------------------------------------------------------------------||"<<endl;
cout<<"\t\t\t||                                                                          ||"<<endl;
cout<<"\t\t\t|| .MEMBERS.                                                                ||"<<endl;
cout<<"\t\t\t||* Aryav                                                                   ||"<<endl;
cout<<"\t\t\t||* Jagerna                                                                 ||"<<endl;
cout<<"\t\t\t||* Kritishma                                                               ||"<<endl;
cout<<"\t\t\t||* Shristi                                                                 ||"<<endl;
cout<<"\t\t\t||--------------------------------------------------------------------------||"<<endl;
cout<<"\t\t\t||                                                 Acme Engineering College ||"<<endl;
cout<<"\t\t\t||                                                   Sitapaila,Kathmandu    ||"<<endl;     

 cout<<"\t\t\t";
for (int h=3;h<15;h++)
    {
for(int x=h; x<15;x++)
    { 
    
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),x);
        cout<<"*";
    }
    }
    cout<<endl;
 }
int main()
{

    char a;
    customer obj, obj2;
    system("CLS");
    obj2.introduction();
    
    do
    {
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 3);
        cout << "\t\t\t\t\t\t __________________" << endl;
        cout << "\t\t\t\t\t\t|    MAIN MENU     |" << endl;
        cout << "\t\t\t\t\t\t|__________________|" << endl;
        cout << "\t\t\t\t\t\t|                  |" << endl;
        cout << "\t\t\t\t\t\t|    1)Admin       |" << endl;
        cout << "\t\t\t\t\t\t|    2)Custmer     |" << endl;
        cout << "\t\t\t\t\t\t|    0)Exit        |" << endl;
        cout << "\t\t\t\t\t\t|__________________|" << endl;
        cout << "\t\t\t\t\t\tSelect the menu: ";
        cin >> a;
        switch (a)
        {
        case '0':
            break;
        case '1':
            system("CLS");
            obj.admin();
            break;
        case '2':
            system("CLS");
            time_t now = time(0);

            // convert now to string form
            char *dt = ctime(&now);
            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 50);
            cout << "\t\t\t____________________________WELCOME TO JAKS FOOD MENU_______________________________________" << endl;
            cout << "\t\t\t\t\t\t\t" << dt << endl;

            char *k;
            strcpy(k, dt);
            string s = k; // constant char converted to std::string
            string l = s.substr(0, 3);
            const char *g = l.c_str(); // std::string converted to  constant char

            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 5);

            if (strcmp(g, "Sun") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!SUNDAY OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t2 Burger,1 pack fries,500ml coke,crunchy fried chicken 1 piece" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            else if (strcmp(g, "Mon") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!!MONDAY OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t2 cocktail,1 pack fries,chicken momo,small meatlovers pizza" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            else if (strcmp(g, "Tue") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!!TUESDAY  OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t2 waffles,1 pack fries, salami bowl,small pepperoni pizza" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            else if (strcmp(g, "Wed") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!!WEDNESDAY OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t2 potato wedges,1 pack fries,mohito,crunchy fried chicken 1 piece" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            else if (strcmp(g, "Thu") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!THURSDAY OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t2 choupsey,1 pack fries,variety smoothie, burrittos" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            else if (strcmp(g, "Fri") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!!!!FRIDAY OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t2 Tacos,1 pack fries,iceream rolls,gourmet rice" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            else if (strcmp(g, "Sat") == 0)
            {
                cout << "\t\t\t\t\t!!!!!!!!!!!!!!!!!!!SATURDAY OFFERS!!!!!!!!!!!" << endl;
                cout << "\t\t\t\t\t\tBiryani,1 sandeko momo, coke, french salad" << endl;
                cout << "\t\t\t\t\t\t\tJust for Rs:900" << endl;
            }

            SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 5);

            obj.bill();
            break;
        }
    } while (a != '0');
}
