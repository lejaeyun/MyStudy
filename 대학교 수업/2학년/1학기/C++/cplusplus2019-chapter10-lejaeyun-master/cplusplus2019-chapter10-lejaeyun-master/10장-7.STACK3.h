// 10¿Â-7.STACK3.H  10.4 template class
template <class T>
class Stack{
    T data [50];
    int nElements;
public:
    Stack () : nElements (0)
    { }
    void Push (T elem);
    T Pop ();
    int Number ();
    int Empty ();
};