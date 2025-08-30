import java.util.Scanner;

public class MiddleSquareHashing {

    public static boolean Search(int Num, int[] HashedArray){
        boolean Found = false;
        int Position = FindMiddleNum(Num);
        for (int i=0; i < HashedArray.length; i++){
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
            if (Position == HashedArray.length){
                Position = 0;
            }
            if (HashedArray[Position] == -1){
                HashedArray[Position] = Num;
                break;
            } else {
                Position = (Position + i) % HashedArray.length;
            }
        }
        return(HashedArray);
    }

    public static int FindNumDigits(int Num){
        int PlaceValue = 0;
        int Quotient = Num;
        while (Quotient >= 1){
            PlaceValue += 1;
            Quotient = Quotient / 10;
        }
        return (PlaceValue);
    }

    public static int FindMiddleNum(int Num){
        int MiddleNum;
        int PlaceValue = FindNumDigits(Num);
        int Quotient = Num;
        int counter = 0;
        while (counter < (int)(Math.floor(PlaceValue / 2))-1){
            Quotient = Quotient / 10;
            counter += 1;
        }
        MiddleNum = Quotient % 10;
        Quotient = Quotient / 10;
        MiddleNum = MiddleNum + ((Quotient % 10) * 10);
        return(MiddleNum);
    }
    
    public static int[] GenerateRandomArray(int min, int max){
        int[] data = new int[100];
        for (int i = 0; i < data.length; i++){
            data[i] = (int)(Math.random()*(max-min)) - min;
        }
        return (data);
    }
    
    public static int[] MiddleSquare(int[] data){
        int[] HashedArray = new int[100];
        for (int j=0; j < HashedArray.length; j++){
            HashedArray[j] = -1;
        }
        int Num = 0;
        for (int i = 0; i < data.length; i++){
            Num = data[i] * data[i];
            int Position = FindMiddleNum(Num);
            HashedArray = PlacePosition(HashedArray, Position, data[i]);
        }
        return(HashedArray);
    }
    
    public static void main(String[] args){
        int[] data = GenerateRandomArray(1, 10000);
        int[] HashedArray = MiddleSquare(data);
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