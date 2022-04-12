package com.program;

import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		float r, h;
		double A, V;

		Scanner userInput = new Scanner(System.in);

		System.out.print("Radius = ");
		r = userInput.nextFloat();
		System.out.print("Height = ");
		h = userInput.nextFloat();

		A = 2 * Math.PI * r * (r + h);
		V = Math.PI * Math.pow(r, 2) * h;

		System.out.printf("Area = %.2f\n", A);
		System.out.printf("Volume = %.2f\n", V);
	}
}