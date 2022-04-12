package com.program;
import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		float a, b, result;
		boolean error = false;
		char operator; //String operator, 'a', "a"

		Scanner userInput = new Scanner(System.in);

		System.out.print("Value A  : ");
		a = userInput.nextFloat();
		System.out.print("Operator : ");
		operator = userInput.next().charAt(0);
		System.out.print("Value B  : ");
		b = userInput.nextFloat();

		switch (operator) {
			case '+' -> result = a + b;
			case '-' -> result = a - b;
			case '*' -> result = a * b;
			case '/' -> result = a / b;
			default -> {
				result = 0;
				error = true;
				System.out.println("Sorry, undefined operator!");
			}
		}

		if (!error) {
			if (result == (int)(result)) System.out.println("Result : " + (int) result);
			else System.out.printf("Result : %.2f\n", result);
		}
	}
}