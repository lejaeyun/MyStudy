package HW2_201624548_¿Ã¿Á¿±;

public class Counter_201624548_¿Ã¿Á¿± {
	public int Counter;
	
	public int returnCounter()
	{
		return Counter;
	}
	
	public void SetCounter() 
	{
		Counter = 0;
	}
	
	public void plusminusCounter(int type) 
	{
		if (type % 2 == 1) 
		{
			if (Counter > 0)
			{
				Counter -= 1;
			}
		}
		else
		{
			Counter += 1;
		}
	}

	public static void main(String[] args) {
		Counter_201624548_¿Ã¿Á¿± testcounter = new Counter_201624548_¿Ã¿Á¿±();
		testcounter.SetCounter();
		for (int i = 0; i < 1000; i++)
		{
			testcounter.plusminusCounter((int)(Math.random()*100));
			System.out.println(testcounter.returnCounter());
		}
	}
}
