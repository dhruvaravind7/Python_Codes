import java.util.Scanner;

public class DoubleHashing {

    public static boolean Search(int Num, int[] HashedArray, String Function){
        boolean Found = false;
        int Position = FindPosition(Num, Function);
        for (int i=0; i < HashedArray.length; i++){
            if (HashedArray[Position] == Num){
                Found = true;
                break;
            } else if (HashedArray[Position] == -1){
                break;
            }
            Position = (Position + FindPosition(Num, "Mod") + (FindPosition(Num, "Divide") * i)) % HashedArray.length;
        }
        return(Found);
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

    public static int AddDigits(int num){
        int Sum = 0;
        int Quotient = num;
        while (Quotient > 0){
            Sum += Quotient % 10;
            Quotient = (int)(Math.floor(Quotient /10));
        }
        return(Sum);
    }

    public static int MaxValue(int range){
        int Quotient = range;
        int PlaceValue = 0;
        while (Quotient > 1){
            PlaceValue += 1;
            Quotient = Quotient / 10;
        } 
        return(PlaceValue * 9);
    } 

    public static int KeyToLocation(int Num, int range){
        int MaximumNumber = MaxValue(range);
        int Index;
        int Position = 0;
        int Quotient = 100 % MaximumNumber;
        int Spots = (int)(Math.ceil(100 / MaximumNumber));
        int SumNum = AddDigits(Num);
        if (SumNum <= Quotient){
            double PositionRange = range / Spots;
            for (int i = 1; i <= Spots; i++){
                if (Num <= PositionRange){
                    Position = i;
                    break;
                }
                PositionRange += range/Spots;
            }
            Index = ((SumNum-1) * Spots) - 1 + Position;
        } else {
            double PositionRange = range / (Spots-1);
            for (int i = 1; i < Spots -1; i++){
                if (Num <= PositionRange){
                    Position = i;
                    break;
                }
                PositionRange += range / (Spots -1);
            }
            Index = Quotient * Spots;
            int Extra = SumNum - Quotient;
            Index += (Extra-1) * (Spots -1) -1 + Position;
        }
        return(Index);
    }

    public static int[] Add(int[] data, int range){
        int[] HashedArray = new int[100];
        for (int j=0; j < HashedArray.length; j++){
            HashedArray[j] = -1;
        }
        for (int i =0; i < data.length; i++){
            int Position = KeyToLocation(data[i], range);
            HashedArray = PlacePosition(HashedArray, Position, data[i]);
        }
        return(HashedArray);
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

    public static int[] PlacePosition(int[] HashedArray, int Position, int Num){
        for (int i=0; i < HashedArray.length; i++){
            if (Position >= HashedArray.length){
                Position = Position - HashedArray.length;
            }
            if (HashedArray[Position] == -1){
                HashedArray[Position] = Num;
                break;
            } else {
                Position += (FindPosition(Num, "Mod") + (FindPosition(Num, "Divide") * i)) % HashedArray.length;
            }
        }
        return(HashedArray);
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

    public static int FindPosition(int Num, String Function){
        int Position = 0;
        if (Function == "Divide"){
            Position = (int)(Math.floor(Num/100));
        } else if (Function == "Mod"){
            Position = (int)(Math.floor(Num % 100));
        } else if (Function == "Add"){
            Position = KeyToLocation(Num, 10000);
        } else if (Function == "Square"){
            Position = FindMiddleNum(Num);
        }
        return(Position);
    }
    
    public static void main(String[] args){
        int[] data = GenerateRandomArray(1, 10000);
        int[] HashedArray = Mod(data);
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number you wish to find ");
        int Num = input.nextInt();
        input.close();
        if (Search(Num, HashedArray, "Mod") == true){
            System.out.println("The number you searched for was found");
        } else {
            System.out.println("The number you searched for was not found");
        }
    }

}
