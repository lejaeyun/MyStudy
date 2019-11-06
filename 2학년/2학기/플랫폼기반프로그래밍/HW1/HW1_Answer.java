package test;

import java.util.Scanner;

public class HW1_Answer {
	public static void main(String argv[]) {
		Scanner s = new Scanner(System.in);		// Scanner 사용
		
		System.out.print("Please enter a number: ");		// 출력 (출력이 일치하지 않을 시 -15점)
		Double d = s.nextDouble();		// double 값 입력
		
		// 조건문 (조건이 일치하지 않을 시 -20점, between = 없어도 인정)
		if(d > 150.45 || (d >= 60.30 && d <= 70.25))	
			System.out.println("YES");		// YES or NO 출력 (출력이 일치하지 않을 시 -15점)
		else
			System.out.println("NO");
		
		s.close();		// Scanner 닫기
	}
}
