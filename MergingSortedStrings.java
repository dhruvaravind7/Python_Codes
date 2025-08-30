import java.util.ArrayList;

public class MergingSortedStrings {
    
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
    public static void main(String[] args){

        String [] list1 = {"falling", "hello", "home", "one", "world"};
        String [] list2 = {"apple", "never", "together", "zebra" };
        int Position1 = 0;
        int Position2 = 0;
        ArrayList<String> SortedList = new ArrayList<>();  
        while (Position1 < list1.length && Position2 < list2.length){
            if (list1[Position1].compareTo(list2[Position2]) < 0){
                SortedList.add(list1[Position1]);
                Position1 += 1;
            }
            else {
                SortedList.add(list2[Position2]);
                Position2 += 1;
            }
        }
        if (Position1 == list1.length){
            while (Position2 < list2.length){
                SortedList.add(list2[Position2]);
                Position2 += 1;
            }
        }
        else{
            while (Position1 < list1.length){
                SortedList.add(list1[Position1]);
                Position1 += 1;
            }
        }
        System.out.println(ConvertArrayListToString(SortedList));
    }
}
