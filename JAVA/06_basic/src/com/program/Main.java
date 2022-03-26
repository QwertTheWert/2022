package  com.program;

public class Main {
	public static void main(String[] args) {
		System.out.println("I'm Anas Ahzar");
		System.out.printf("I'm %d years old, and %.2f.\n", 27, 178.5f);

		if (args.length > 0) {
			System.out.println("Args value are :");

			for (int index = args.length - 1; index >= 0; --index) {
				System.out.print((args[index] + " "));
			}
		} else {
			System.out.println("No Arguments Here!");
		}


		int number; //declaration
		number = 40; //asignment
		int numberAgain = 100;
		System.out.println(numberAgain + " " + number);
		// INTEGER, SHORT, LONG, BYTE
		// FLOAT, DOUBLE
		// CHAR, BOOL

		System.out.println(Integer.BYTES); // 4 BYTES = 32 BIT : +- 2 ^ 31 -1
		System.out.println(Integer.MAX_VALUE + 1);
		System.out.println(Short.MAX_VALUE);
		System.out.println(Long.MAX_VALUE);
		System.out.println(Byte.MAX_VALUE);
		System.out.println(Float.MAX_VALUE);
		System.out.println(Double.MAX_VALUE);
		System.out.println(Character.MAX_VALUE);
	}
}