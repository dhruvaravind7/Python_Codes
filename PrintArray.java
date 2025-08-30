public class PrintArray {
    public static String ConvertArrayToString(int[] array){
        String Convert = "[";
        int counter = 0;
        while (counter < array.length - 1){
            Convert = Convert + array[counter] + ", ";
            counter += 1;
        }
        Convert = Convert + array[counter] + "]";
        return(Convert);
    }
}