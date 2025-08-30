import java.util.ArrayList;

public class MergingSortedLists {
    
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
    public static void main(String[] args){

        int [] list1 = {-21, 0, 9, 22, 217};
        int [] list2 = {-5, -1, 7, 15, 99};
        int Position1 = 0;
        int Position2 = 0;
        ArrayList<Integer> SortedList = new ArrayList<>();
        while (Position1 < list1.length && Position2 < list2.length){
            if (list1[Position1] < list2[Position2]){
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
