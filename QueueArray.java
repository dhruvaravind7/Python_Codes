import java.util.ArrayList;
import java.util.Scanner;

public class QueueArray {

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
    
    public static int Pop(ArrayList<Integer> Queue){
        int Num = Queue.get(0);
        Queue.remove(0);
        return(Num);
    }  

    public static void Push(ArrayList<Integer> Queue){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number you wish to add");
        int Num = sc.nextInt();
        Queue.add(Num);
        System.out.println("You have successfully added the number");
    }   
    public static void main(String[] args){
        ArrayList<Integer> Queue = new ArrayList<Integer>();
        while (true){
            Scanner sc = new Scanner(System.in);
            System.out.println("To push a number press '1', to pop a number press '2'");
            int Function = sc.nextInt();
            if (Function == 1){
                Push(Queue);
            } else if (Function == 2){
                Pop(Queue);
            }
            System.out.println(ConvertArrayListToString(Queue));
        }
    }
}
