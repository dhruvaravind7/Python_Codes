public class HashingFunctions {
    public static int LargestNumber(int[] data){
        int LargestNumber = data[0];
        for (int i = 0; i < data.length - 1; i++){
            if (LargestNumber < data[i + 1]){
                LargestNumber = data[i + 1];
            }
        }
        return (LargestNumber);
    }

    public static int Mod(int[] data){
        int [] HashedArray = new int[100];
        for (int i = 0; i < data.length; i++){
            int Position = data[i] % 100;
            HashedArray[Position] += 1;
        }
        return (LargestNumber(HashedArray));
    }

    public static int Divide(int[] data, int range){
        int [] HashedArray = new int[100];
        int DivideBy = range / 100;
        for (int i = 0; i < data.length; i++){
            int Position = (int)(Math.floor(data[i] / DivideBy));
            HashedArray[Position] = HashedArray[Position] + 1;
        }
        return (LargestNumber(HashedArray));
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

    public static int Add(int[] data, int range){
        int[] HashedArray = new int[100];
        for (int i =0; i < data.length; i++){
            HashedArray[KeyToLocation(data[i], range)] += 1;
        }
        return(LargestNumber(HashedArray));
    }

    public static void main(String[] args){
        int[] data = {12, 1234, 230, 235, 8932, 1233, 123, 1231, 1234, 2, 56, 432, 54};
        int range = 10000;
        if (Mod(data) < Divide(data, range) && Mod(data) < Add(data, range)){
            System.out.println("Using the module hashing function gives the least collision");
        } else if (Divide(data, range) < Mod(data) && Divide(data, range) < Add(data, range)){
            System.out.println("Using the divide hashing function gives the least collision");
        } else if (Add(data, range) < Mod(data) && Add(data, range) < Divide(data, range)){
            System.out.println("Using the adding digits hashing function gives the least collision");
        } else {
            System.out.println("Both hashing functions give the same amount of collision");
        }
    }
}
