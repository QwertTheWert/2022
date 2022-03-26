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
	}
}