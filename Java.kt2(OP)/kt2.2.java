import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ввод данных с клавиатуры
        System.out.println("Введите массив значений (пример: [1, 0, 1, 1, 1]): ");
        String input = scanner.nextLine();

        // Преобразование строки в массив булевых значений
        String[] valuesString = input.replaceAll("[^01]", "").split("");
        boolean[] values = new boolean[valuesString.length];
        for (int i = 0; i < valuesString.length; i++) {
            values[i] = valuesString[i].equals("1");
        }

        // Подсчет количества работников
        int countWorkers = 0;
        for (boolean value : values) {
            if (value) {
                countWorkers++;
            }
        }

        System.out.println("Количество работников: " + countWorkers);
    }
}
