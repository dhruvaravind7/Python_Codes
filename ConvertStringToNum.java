
import java.util.Scanner;

public class ConvertStringToNum {
    public static int GetNumber(String CodeInput, int Index){
        char Character = CodeInput.charAt(Index);
        double Num = Character;
        Num = Num - 96;
        double Extra = 0;
        if (Num == 26){
            return(9999);
        }
        if (Num == 19){
            return(7777);
        }
        if (Num > 18){
            Extra = -0.35;
        }
        if (Num % 3 == 0){
            Num = Num /3 +1;
        } else {
            Num = Num / 3 +2 + Extra;
        }
        double Rotation = Math.round((Num % 1) * 3);
        if (Rotation == 0.0 && Num < 8){
            Rotation = 3.0;
        } else if (Rotation == 0.0 && Num >= 8){
            Rotation = 2.0;
        }
        int Remainder = 0;
        for (int i = 0; i < (int)Rotation; i++){
            Remainder = Remainder +  (int)Math.pow(10, i) * (int)(Num);
        }
        return(Remainder);
    }

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string you want to code: ");
        String CodeInput = sc.nextLine();
        sc.close();
        String CodeNum = "";
        CodeInput = CodeInput.toLowerCase();
        for (int i=0; i < CodeInput.length(); i++){
            CodeNum = CodeNum + GetNumber(CodeInput, i) + " " ;
        }
        System.out.println(CodeNum);
    }
}

