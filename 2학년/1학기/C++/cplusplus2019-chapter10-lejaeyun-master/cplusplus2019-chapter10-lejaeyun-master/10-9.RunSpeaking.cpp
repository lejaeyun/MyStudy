// 10-9.RunSpeaking.cpp  10.5.1 RunSpeaking 함수의 재검토
#include <iostream>
#include <stdlib.h>
#include "time.h"
using namespace std;

class Point{
public:
    Point(int xp=0, int yp = 0):
    xPos(xp), yPos(yp)
    {}

     int x_Coor()
    {return xPos;}

    int y_Coor()
    {return yPos;}

    void x_Coor(int px)
    {xPos = px;}

    void y_Coor(int py)
    {yPos = py;}

    void operator += (Point p){
        xPos += p.xPos;
        yPos += p.yPos;
    }
private:
      int xPos, yPos;
};

class Animal{
public:
Animal(Point p = Point());
    //virtual ~Animal();
    virtual void Speak();
    //virtual void Speak() = 0;
    void JumpBy(int x_coord, int y_coord);
    void MoveTo(Point newPosition);

protected:
    Point position;
    void MoveOutput();
   };

Animal::Animal(Point p):
position(p)
{}

void Animal::Speak(){
    cout<<"Animal::Speak() -> The animal is making his verse"<<endl;
}

void Animal::JumpBy(int x_coord, int y_coord){
    position += Point(x_coord, y_coord);
}

void Animal::MoveTo(Point newPosition){
    position = newPosition;
}

void Animal::MoveOutput(){
    cout<<"Animal::MoveOutPut()-> x = " << position.x_Coor()<<", y = "<<position.y_Coor()<<"  ";
}


class Cow : public Animal{
public:
    Cow(Point p = Point(10, 10));
    void Speak();
};

class Dog : public Animal{
public:
    Dog(Point p = Point(20, 20));
    void Speak();
};


Cow::Cow(Point p):
Animal(p){}

void Cow::Speak(){
    MoveOutput();
    cout<<"Cow::Speak() ->moo"<<endl;
}

Dog::Dog(Point p):
Animal(p){}

void Dog::Speak(){
    MoveOutput();
    cout<<"Dog::Speak()->arf"<<endl;
}

//* 주석 1
void RunSpeaking(Animal& aml, int nSteps){
    srand((unsigned)time(NULL));
    for(int temp=0; temp < nSteps;++temp){
        int x_coord = (1 + rand() % 5) - 2;
        int y_coord = (1 + rand() % 5) - 2;

        aml.JumpBy(x_coord, y_coord);
        aml.Speak();
    }
}
//*/

/* 주석 2
template <class T>
void RunSpeaking(T& data, int nSteps){
    srand((unsigned)time(NULL));
    for(int temp=0; temp < nSteps;++temp){
        int x_coord = (1 + rand() % 5) - 2;
        int y_coord = (1 + rand() % 5) - 2;

        data.JumpBy(x_coord, y_coord);
        data.Speak();
    }
}
*/

void main(){
    Animal* mixedFlock[10];

    mixedFlock[0] = new Cow();
    mixedFlock[1] = new Dog();
    mixedFlock[2] = new Dog(Point (12,24));
    mixedFlock[3] = new Dog(Point (2,12));
    mixedFlock[4] = new Dog(Point (22,24));
    mixedFlock[5] = new Cow(Point (7,7));
    mixedFlock[6] = new Cow(Point (7,11));
    mixedFlock[7] = new Cow(Point (11,13));
    mixedFlock[8] = new Animal(Point (1,1));
    mixedFlock[9] = new Dog(Point (7,19));

    for(int temp=0; temp< 10; temp++)
        RunSpeaking(*mixedFlock[temp], 1);
        system("pause");
}
