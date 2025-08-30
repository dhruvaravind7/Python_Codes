import java.util.ArrayList;
import java.util.Scanner;

public class RandomNameGenerator {
    
    public static String ConvertArrayListToString(ArrayList<String> array){
        String SortedString = "[";
        int counter = 0;    
        while (counter < array.size() - 1){
            SortedString = SortedString + array.get(counter) + ", ";
            counter += 1;
        }
        SortedString = SortedString + array.get(counter) + "]";
        return(SortedString);
    }

    public static ArrayList<String> GenerateNames(){
        ArrayList<String> NameBank = new ArrayList<String>();
        while (true) {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter a name you wish to add. Type exit to finish adding names");
            String name = sc.nextLine();
//            System.out.println(name);
            if (name.equals("exit")) {
                break;
            } else {
                NameBank.add(name);
            }
        }  
        
        return (NameBank);
    }  
    public static ArrayList<String> PrintName(ArrayList<String> NameBank, int NumNames){
        for (int i = 0; i < NumNames; i++){
            if (NameBank.size() == 0){
                System.out.println("There are no more names left");
                return(NameBank);
            }
            int Position = (int)(Math.random()*(NameBank.size()-1+1)+0);
            System.out.println(NameBank.get(Position));
            NameBank.remove(Position);
        }
        return (NameBank);
    }

    public static void main(String[] args){
        ArrayList<String> NameBank = new ArrayList<String>();
        NameBank = GenerateNames();
        Scanner sc = new Scanner(System.in);
        System.out.println("How many scorers do you want");
        int Scorers = sc.nextInt();
        NameBank = PrintName(NameBank, Scorers);
        Scanner in = new Scanner(System.in);
        System.out.println("How many umpires do you want");
        int Umpires = in.nextInt();
        NameBank = PrintName(NameBank, Umpires);
   } 
}