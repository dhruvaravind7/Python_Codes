public class SelectionSort {

    public static String ConvertArrayToString(int[] array){
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
        int [] data = {1, 3, 0, 8, 6, 2, 9, 5};
        int i = 0;
        int j = 1;
        while (i < data.length){
            int smallestNumber = data[i];
            int smallestNumIndex = i;
            while (j < data.length){
                if (data[smallestNumIndex] > data[j]){
                    smallestNumber = data[j];
                    smallestNumIndex = j;
                }
                j += 1;
            }
            int holding = data[i];
            data[i] = smallestNumber;
            data[smallestNumIndex] = holding;
            i += 1;
            j = i;
        }
        System.out.println(ConvertArrayToString(data));
    }
}
