package HW2_201624548_¿Ã¿Á¿±;

public class Grades_201624548_¿Ã¿Á¿± {
	public int GradeA;
	public int GradeB;
	public int GradeC;
	public int GradeD;
	public int GradeF;
	public String nameA;
	public String nameB;
	public String nameC;
	public String nameD;
	public String nameF;
	
	public int sumAllGrade() {
		return GradeA + GradeB + GradeC +GradeD + GradeF;
	}
	
	public int returnPercent(int quot ,int div)
	{
		return (int)Math.round((int) ((double)quot / (double)div * 50));
	}
	
	public void setAllGrades() 
	{
		nameA = "A"; GradeA = 1;
		nameB = "B"; GradeB = 4;
		nameC = "C"; GradeC = 6;
		nameD = "D"; GradeD = 2;
		nameF = "F"; GradeF = 1;
	}

	public void readAllGrades() 
	{
		System.out.print(nameA + ": " + GradeA + ", ");
		System.out.print(nameB + ": " + GradeB + ", ");
		System.out.print(nameC + ": " + GradeC + ", ");
		System.out.print(nameD + ": " + GradeD + ", ");
		System.out.println(nameF + ": " + GradeF);
	}

	public void MakeBarGraph() 
	{
		int i = 0;
		int sum = sumAllGrade();
		
		System.out.print("0 ");
		for (i = 1; i < 40; i++) {
			if ( (i + 1) % 4 == 0) {
				System.out.print((i + 1) / 4 * 10);
			}
			else {
				System.out.print(" ");
			}
		}
		System.out.println();
		
		System.out.print("|");
		for (i = 1; i < 50; i++) {
			if ( (i + 1) % 5 == 0) {
				System.out.print("|");
			}
			else {
				System.out.print(" ");
			}
		}
		System.out.println();
		
		for (i = 0; i < 50; i++) {
			System.out.print("*");
		}
		System.out.println();
		
		for (i = 0; i < returnPercent(GradeA,sum) ; i++) {
			System.out.print("*");
		}
		System.out.println(" " + nameA);	

		for (i = 0; i < returnPercent(GradeB,sum) ; i++) {
			System.out.print("*");
		}
		System.out.println(" " + nameB);
		
		for (i = 0; i <  returnPercent(GradeC,sum); i++) {
			System.out.print("*");
		}
		System.out.println(" " + nameC);	

		for (i = 0; i <  returnPercent(GradeD,sum); i++) {
			System.out.print("*");
		}
		System.out.println(" " + nameD);

		for (i = 0; i < returnPercent(GradeF,sum); i++) {
			System.out.print("*");
		}
		System.out.println(" " + nameF);
		
	}
	
	public static void main(String[] args) {
		Grades_201624548_¿Ã¿Á¿± grades = new Grades_201624548_¿Ã¿Á¿±();
		grades.setAllGrades();
		grades.readAllGrades();
		System.out.println();
		grades.MakeBarGraph();
	}
}
