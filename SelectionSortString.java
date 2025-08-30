public class SelectionSortString {

    public static String ConvertArrayToString(String[] array){
        String SortedString = "[";
        int counter = 0;
        while (counter < array.length - 1){
            SortedString = SortedString + array[counter] + ", ";
            counter += 1;
        }
        SortedString = SortedString + array[counter] + "]";
        return(SortedString);
    }
    public static void main(String[] args){
        String [] data = {"Hello", "Together", "Only", "Phone", "Cricket", "Apple"};
        int i = 0;
        int j = 1;
        while (i < data.length){
            String smallestString = data[i];
            int smallestNumIndex = i;
            while (j < data.length){
                if (data[smallestNumIndex].compareTo(data[j]) > 0){
                    smallestString = data[j];
                    smallestNumIndex = j;
                }
                j += 1;
            }
            String holding = data[i];
            data[i] = smallestString;
            data[smallestNumIndex] = holding;
            i += 1;
            j = i;
        }
        System.out.println(ConvertArrayToString(data));
    }
}
