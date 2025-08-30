import java.util.Scanner;

public class ModHashing {

    public static boolean Search(int Num, int[] HashedArray){
        boolean Found = false;
        int Position =  (int)(Math.floor(Num % 100));
        for (int i=0; i < HashedArray.length; i++){
            if (Position == HashedArray.length){
                Position = 0;
            }
            if (HashedArray[Position] == Num){
                Found = true;
                break;
            } else if (HashedArray[Position] == -1){
                break;
            }
            Position += 1;
        }
        return(Found);
    }

    public static int[] PlacePosition(int[] HashedArray, int Position, int Num){
        for (int i=0; i < HashedArray.length; i++){
            if (Position == HashedArray.length){
                Position = 0;
            }
            if (HashedArray[Position] == -1){
                HashedArray[Position] = Num;
                break;
            } else {
                Position += 1;
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

    public static int[] Mod(int[] data){
        int [] HashedArray = new int[100];
        for (int j=0; j < data.length; j++){
            HashedArray[j] = -1;
        }
        for (int i = 0; i < data.length; i++){
            int Position = data[i] % 100;
            HashedArray = PlacePosition(HashedArray, Position, data[i]);
        }
        return (HashedArray);
    }

    public static void main(String[] args){
        int[] data = GenerateRandomArray(1, 10000);
        int[] HashedArray = Mod(data);
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
