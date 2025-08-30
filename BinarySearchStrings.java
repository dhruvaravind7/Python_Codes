import java.util.Scanner;

public class BinarySearchStrings {
    public static String FindString(String target, String[] data) {   

        int foundIndex = 1;
        int startIndex = 0;
        int Iterations = 0;
        boolean found = false;
        int endIndex = data.length - 1;

        while (startIndex != endIndex) {
            Iterations = Iterations + 1;
            int middleIndex = (int)(Math.floor((endIndex - startIndex + 1) / 2 + startIndex));
            if (target.equals(data[middleIndex])) {
                found = true;
                foundIndex = middleIndex;
                break;
            }
            else if (target.compareTo(data[middleIndex]) > 0) {
                startIndex = middleIndex + 1;
            }
            else {
                endIndex = middleIndex - 1;
            }
            if (target.compareTo(data[startIndex]) < 0 || target.compareTo(data[endIndex]) > 0){
                found = false;
                break;
            }
        }
        if (data[startIndex] == target) {
            found = true;
            foundIndex = startIndex;
        }
        if (found == true) {
            return("The string, " + target + " is found at position " + (foundIndex) + ". It took " + Iterations + " iterations to find the answer.");
        }
        else {
            return("The string, " + target + " is not in the given list");
        }
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the string you want to find.");
        String value = scanner.nextLine();
        scanner.close();
        String [] data = {"Apple", "Falling", "Hello", "Home", "Never", "One", "Together", "World", "Zebra"};
        System.out.println(FindString(value, data));
    }
}