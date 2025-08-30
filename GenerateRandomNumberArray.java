public class GenerateRandomNumberArray {
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

    public static int[] GenerateRandomArray(String[] args){
        int max = 10000;
        int min = 1;
        int[] data = new int[100];
        for (int i = 0; i < data.length; i++){
            data[i] = (int)(Math.random()*(max-min)) - min;
        }
        return (data);
    }
}
