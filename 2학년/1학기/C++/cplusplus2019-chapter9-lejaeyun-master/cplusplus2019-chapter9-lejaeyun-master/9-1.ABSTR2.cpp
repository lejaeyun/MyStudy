// 9-1. ABSTR2.CPP  9.4 Ãß»ó class
#include <iostream>
using namespace std;

class Printer{
public:
    Printer (){ }
    virtual void Method (char * buffer) = 0;
    virtual int Dpi () = 0;
};

class DotMatrixPrinter : public Printer{
    int nDots;
public:
    DotMatrixPrinter (int n) :
        nDots (n)
        { }
	///*
    void Method (char * buffer){
        sprintf (buffer, "Dot matrix printer with %d pins", nDots);
    }
	//*/
    int Dpi (){
        switch (nDots){
            case 8: return 150;
            case 9: return 160;
            case 24: return 300;
            default: return 100;
        }
    }
} ;

void main(){
    char description [40];
    DotMatrixPrinter dmp (24);
    dmp.Method (description);
    cout << description << endl << "DPI: " << dmp.Dpi () << endl <<endl;
    Printer * pPri;
    pPri = new DotMatrixPrinter (9);
    pPri -> Method (description);
    cout << description << endl << "DPI: " << pPri -> Dpi ()<< endl <<endl;
	delete pPri;
	system("pause");
}