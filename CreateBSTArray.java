import java.util.Scanner;

public class CreateBSTArray{

    public static String ConvertArrayToString(int[] array){
        String Convert = "[";
        int counter = 0;
        while (counter < array.length - 1){
            Convert = Convert + array[counter] + ", ";
            counter += 1;
        }
        Convert = Convert + array[counter] + "]";
        return(Convert);
    }

    public static int[] DoubleArraySize(int[] data){
        int[] NewArray = new int[data.length * 2];
        for (int i=0; i<data.length; i++){
            NewArray[i] = data[i];
        }
        return(NewArray);
    }

    public static int[] AddElement(int[] data, int Num){
        int counter = 1;
        while (true){
            if (data[counter-1] == 0){
                data[counter-1] = Num;
                return(data);
            } else if (Num <= data[counter-1]){
                if ((counter*2) > data.length){
                    data = DoubleArraySize(data);
                }
                counter = counter *2;
            } else if (Num > data[counter-1]){
                if ((counter*2) + 1 > data.length){
                    data = DoubleArraySize(data);
                }
                counter = (counter *2) + 1;
            }
        }
    }

    public static void main(String[] args){
        int[] data = new int[10];
        while (true){
            Scanner input = new Scanner(System.in);
            System.out.println("Enter the number you wish to add. Type '-1' to print the BST in array form ");
            int Num = input.nextInt();
            if (Num == -1){
                System.out.println(ConvertArrayToString(data));
                break;
            }
            data = AddElement(data, Num);
        }
    }
}