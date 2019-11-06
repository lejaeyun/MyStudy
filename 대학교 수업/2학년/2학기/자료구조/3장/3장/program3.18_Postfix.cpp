//3.6.2 postfix notation
//3.18~19
#include <iostream>
#include <memory>
#include "string.h"
#include "PostFixHeader.h"
typedef char* Expression;
typedef char Token;
using namespace std;

const int maxsize = 1000;
int index = 0;

char NextToken(char* e)
{
	char token = e[index];
	index++;
	return token;
}

bool isOperand(char x)
{
	if (x == '+' || x == '-' || x == '*' || x == '/' ||
		x == '(' || x == ')' || x == '%' || x == '#')
		return false;
	else
		return true;
}

int isp(char a)
{
	if (a == '(')
		return 0;
	else if (a == ')')
		return 19;
	else if (a == '+' || a == '-')
		return 12;
	else if (a == '*' || a == '%' || a == '/')
		return 13;
	else
		return 0;
}

int icp(char a)
{
	if (a == '(')
		return 20;
	else if (a == ')')
		return 19;
	else if (a == '+' || a == '-')
		return 12;
	else if (a == '*' || a == '%' || a == '/')
		return 13;
	else
		return 0;
}

Expression Postfix(Expression e)
{
	Stack<char> stack;
	stack.Push('#');

	int i = 0;
	char* postfix = new char[maxsize] {NULL};
	char x;

	for (char x = NextToken(e); x != NULL; x = NextToken(e))
	{
		//cout << "x = " << x << endl;
		if (isOperand(x)) {
			cout << x;
			postfix[i++] = x;
		}
		else if (x == ')')
		{
			while (stack.Top() != '(')
			{
				cout << stack.Top();
				postfix[i++] = stack.Top();
				stack.Pop();
			}
			stack.Pop();
		}
		else
		{
			for (; isp(stack.Top()) >= icp(x); stack.Pop()) {
				cout << stack.Top();
				postfix[i++] = stack.Top();
			}
			stack.Push(x);
		}
	}

	while ((x = stack.Top()) != '#')
	{
		cout << x;
		postfix[i++] = x;
		stack.Pop();
	}
	postfix[i] = '\0';
	cout << endl;
	return postfix;
}

void Eval(char* e){
	Stack<Token> stack;
	stack.Push('#');
	index = 0;
	double result = 0;
	double start, end;
	double chkt;
	for (Token x = NextToken(e);; x = NextToken(e)) {
		if (x == '\0')
			break;
		if (isOperand(x)) {
			stack.Push(x);
		}
		else {
			start = (double)(stack.Top() - '0');
			stack.Pop();
			end = (double)(stack.Top() - '0');
			stack.Pop();

			if (x == '+')
				chkt = start + end;
			else if (x == '-')
				chkt = start - end;
			else if (x == '*')
				chkt = start * end;
			else if (x == '%')
				chkt = start / end;

			result = chkt;
			stack.Push(result + '0');
			cout << result << endl;
			//remove the correct number of operands for operator x from stack;
			//perform the operation x and store the result onto the stack;
		}
	}
	cout << "result : " << result << endl;
}

void main()
{
	index = 0;
	char infix[maxsize] = {NULL};
	char* postfix;
	scanf("%s", infix);
	cout << infix << endl;
	postfix = Postfix(infix);
	Eval(postfix);
	cout << "postfix = " << postfix << endl;
	delete postfix;
	system("pause");
}
