import java.util.ArrayList;
import java.util.Scanner;

public class StackArray {

    public static String ConvertArrayListToString(ArrayList<Integer> array){
        String SortedString = "[";
        int counter = 0;
        while (counter < array.size() - 1){
            SortedString = SortedString + array.get(counter) + ", ";
            counter += 1;
        }
        SortedString = SortedString + array.get(counter) + "]";
        return(SortedString);
    }

    public static int Count(ArrayList<Integer> Stack){
        return(Stack.size());
    }

    public static int Pop(ArrayList<Integer> Stack){
        int PopNum = Stack.get(Stack.size() - 1);
        Stack.remove(Stack.size() - 1);
        return(PopNum);
    }

    public static void Push(ArrayList<Integer> Stack){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number you wish to add to the list: ");
        int Num = sc.nextInt(); 
        Stack.add(Num);   
    }

    public static void main(String[] args){
        ArrayList<Integer> Stack = new ArrayList<Integer>();
        while (true){
            Scanner sc = new Scanner(System.in);
            System.out.println("To push enter 1, to pop enter 2, to count enter 3, to end the stack enter 4");
            int Function = sc.nextInt();
            if (Function == 1){
                Push(Stack);
                System.out.println("The number you inputted has been added to the Stack array.");
            } else if (Function == 2){
                System.out.println("The number " + Pop(Stack) + " has been popped from the Stack array");
            } else if (Function == 3){
                System.out.println("There are " + Count(Stack) + " elements in the Stack array");
            } else if (Function == 4){
                break;
            }
        }
        System.out.println(ConvertArrayListToString(Stack));
    }
}