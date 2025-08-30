import java.util.Scanner;

public class BinarySearch {
    public static String FindNum(int targetNum, int [] data) {   

        int foundIndex = 1;
        int startIndex = 0;
        int Iterations = 0;
        boolean found = false;
        int endIndex = data.length - 1;

        while (startIndex != endIndex) {
            Iterations = Iterations + 1;
            int middleIndex = (int)(Math.floor((endIndex - startIndex + 1) / 2 + startIndex));
            if (targetNum == data[middleIndex]) {
                found = true;
                foundIndex = middleIndex;
                break;
            }
            else if(targetNum > data[middleIndex]) {
                startIndex = middleIndex + 1;
            }
            else {
                endIndex = middleIndex - 1;
            }
            if (targetNum < data[startIndex] || targetNum > data[endIndex]){
                found = false;
                break;
            }
        }
        if (data[startIndex] == targetNum) {
            found = true;
            foundIndex = startIndex;
        }
        if (found == true) {
            return("The number " + targetNum + " is found at position " + (foundIndex + 1) + ". It took " + Iterations + " iterations to find the answer.");
        }
        else {
            return("The number " + targetNum + " is not in the given list");
        }
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input the number you want to find.");
        int value = scanner.nextInt();
        scanner.close();
        int [] data = {-21, -4, -1, 0, 8, 9, 12, 17, 25, 201};
        System.out.println(FindNum(value, data));
    }
}