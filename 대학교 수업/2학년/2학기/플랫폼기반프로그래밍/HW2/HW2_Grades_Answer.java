package hw02;

public class HW2_Grades_Answer {
	private int a;
	private int b;
	private int c;
	private int d;
	private int f;
	
	// Set the number of each of the letter grades A, B, C, D, and F
	public void setTotalGrades(int a, int b, int c, int d, int f) {
		if(!(a < 0 || b < 0 || c < 0 || d < 0 || f < 0)) {
			this.a = a;
			this.b = b;
			this.c = c;
			this.d = d;
			this.f = f;
		}
	}
	
	// Read the number of each of the letter grades A, B, C, D, and F
	public void readAllGrades() {
		System.out.println("A: " + a + ", B: " + b + ","
				+ " C: " + c + ", D: " + d + ", F: " + f);
	}
	
	// Return the total number of grades
	public int getTotalGrades() {
		return a + b + c + d + f;
	}
	
	// Return the percentage of each letter grade as a whole number between 0 and 100, inclusive
	public double getPercentageA() {
		if(getTotalGrades() != 0)
			return (double)a / getTotalGrades() * 100;
		else
			return 0;
	}
	
	public double getPercentageB() {
		if(getTotalGrades() != 0)
			return (double)b / getTotalGrades() * 100;
		else
			return 0;
	}
	
	public double getPercentageC() {
		if(getTotalGrades() != 0)
			return (double)c / getTotalGrades() * 100;
		else
			return 0;
	}
	
	public double getPercentageD() {
		if(getTotalGrades() != 0)
			return (double)d / getTotalGrades() * 100;
		else
			return 0;
	}
	
	public double getPercentageF() {
		if(getTotalGrades() != 0)
			return (double)f / getTotalGrades() * 100;
		else
			return 0;
	}
	
	// Draw a bar graph of the grade distribution
	public void drawGraph() {
		if(getTotalGrades() != 0) {
			System.out.print("0    ");
			for(int i=1; i!=9; ++i) {
				System.out.print(i*10);
				System.out.print("   ");
			}
			
			System.out.println("90  100");
			for(int i=1; i!=10; ++i) System.out.print("|    ");
			System.out.println("|   |");
			for(int i=0; i!=50; ++i) System.out.print('*');
			System.out.println();
			
			for(int i=0; i!=(int)(getPercentageA() / 2 + 0.5); ++i)
				System.out.print('*');
			System.out.println(" A");
			
			for(int i=0; i!=(int)(getPercentageB() / 2 + 0.5); ++i)
				System.out.print('*');
			System.out.println(" B");
			
			for(int i=0; i!=(int)(getPercentageC() / 2 + 0.5); ++i)
				System.out.print('*');
			System.out.println(" C");
			
			for(int i=0; i!=(int)(getPercentageD() / 2 + 0.5); ++i)
				System.out.print('*');
			System.out.println(" D");
			
			for(int i=0; i!=(int)(getPercentageF() / 2 + 0.5); ++i)
				System.out.print('*');
			System.out.println(" F");
			
		}
	}
	
	public static void main(String[] args) {
		HW2_Grades_Answer g = new HW2_Grades_Answer();
		g.setTotalGrades(1, 4, 6, 2, 1);
		System.out.println(g.getTotalGrades());
		System.out.println(g.getPercentageA());
		System.out.println(g.getPercentageB());
		System.out.println(g.getPercentageC());
		System.out.println(g.getPercentageD());
		System.out.println(g.getPercentageF());
		g.readAllGrades();
		g.drawGraph();
	}
}
