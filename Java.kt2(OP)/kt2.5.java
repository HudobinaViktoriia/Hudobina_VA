import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите числа через пробел:");
        String input = scanner.nextLine();

        String[] numbers = input.split(" ");
        int sum = 0;

        for (String number : numbers) {
            int num = Integer.parseInt(number);
            sum += num * num; // добавляем квадрат числа к сумме
        }

        System.out.println("Сумма квадратов чисел: " + sum);
    }
}
