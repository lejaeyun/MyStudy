// 10¿Â-13.STACK4.H 10.4.2 template argument

template <class T, int nEl = 50> class Stack{
    T data [nEl];
    int nElements;
public:
    Stack () : nElements (0)
    { }
    void Push (T elem);
    T Pop ();
    int Number ();
    int Empty ();
    int Full ();
} ;