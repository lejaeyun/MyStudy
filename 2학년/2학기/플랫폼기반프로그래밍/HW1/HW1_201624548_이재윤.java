package HW1_201624548_ÀÌÀçÀ±;
import java.util.Scanner;

public class HW1_201624548_ÀÌÀçÀ± {
	public static void main(String[] args) {
		float input = 0;
		Scanner keyboard = new Scanner(System.in);
		System.out.print("Please enter a number : ");
		input = keyboard.nextFloat();
		if (((input >= (float)60.30) && (input <= (float)70.25)) ||
			 (input > (float)150.45)) {
			System.out.println("Yes");
		}
		else {
			System.out.println("NO");
		}
	}
}
