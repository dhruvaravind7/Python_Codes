import java.util.ArrayList;

public class PrintArrayList {
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
}
