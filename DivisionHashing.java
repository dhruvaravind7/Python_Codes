import java.util.Scanner;

public class DivisionHashing {

    public static boolean Search(int Num, int[] HashedArray){
        boolean Found = false;
        int Position =  (int)(Math.floor(Num / 100));
        for (int i=1; i <= HashedArray.length; i++){
            if (HashedArray[Position] == Num){
                Found = true;
                break;
            } else if (HashedArray[Position] == -1){
                break;
            }
            Position = (Position + i) % HashedArray.length;
        }
        return(Found);
    }

    public static int[] PlacePosition(int[] HashedArray, int Position, int Num){
        for (int i=1; i <= HashedArray.length; i++){
            if (HashedArray[Position] == -1){
                HashedArray[Position] = Num;
                break;
            } else {
                Position = (Position + i) % HashedArray.length;
            }
        }
        return(HashedArray);
    }

    public static int[] GenerateRandomArray(int min, int max){
        int[] data = new int[100];
        for (int i = 0; i < data.length; i++){
            data[i] = (int)(Math.random()*(max-min)) - min;
        }
        return (data);
    }

    public static int[] Divide(int[] data, int range){
        int [] HashedArray = new int[100];
        for (int j=0; j < HashedArray.length; j++){
            HashedArray[j] = -1;
        }
        int DivideBy = range / 100;
        for (int i = 0; i < data.length; i++){
            int Position = (int)(Math.floor(data[i] / DivideBy));
            HashedArray = PlacePosition(HashedArray, Position, data[i]);
        }
        return (HashedArray); 
    } 

    public static void main(String[] args){
        int[] data = GenerateRandomArray(1, 10000);
        int[] HashedArray = Divide(data, 10000);
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number you wish to find ");
        int Num = input.nextInt();
        input.close();
        if (Search(Num, HashedArray) == true){
            System.out.println("The number you searched for was found");
        } else {
            System.out.println("The number you searched for was not found");
        }
    }    
}
