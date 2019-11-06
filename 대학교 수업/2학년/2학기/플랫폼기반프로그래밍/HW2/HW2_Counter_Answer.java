package hw02;

public class HW2_Counter_Answer {
	private int count;
	
	// Method to set the counter to 0
	// The only method that can set the counter is the one that sets it to zero
	public void reset() {
		count = 0;
	}
	
	// Method to increase the count by 1
	public void increase() {
		count++;
	}
	
	// Method to decrease the count by 1
	// no method allows the value of the counter to become negative
	public void decrease() {
		if(count != 0) count--;
	}
	
	// Accessor method that returns the current count value
	public int getCount() {
		return count;
	}
	
	// Method that displays the count on the screen
	public void displayCount() {
		System.out.println(getCount());
	}
	
	public static void main(String args[]) {
		HW2_Counter_Answer ca = new HW2_Counter_Answer();
		ca.increase();
		ca.increase();
		ca.decrease();
		ca.displayCount();
		ca.reset();
		ca.displayCount();
		ca.decrease();
		ca.displayCount();
	}
}
