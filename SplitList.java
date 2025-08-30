public class SplitList {
    public static int SortValue(int[] data, int splitNum) {

        int startLock = 0;
        int endLock = 0;
        boolean SkipNum = false;

        /** The while loop goes through every number and checks to see if they are larger or smaller than the inputted number */

        while (endLock + startLock < data.length -1) {
            if (data[startLock] == splitNum){
                startLock += 1;
                SkipNum = true;
            }
            if (data[startLock] > splitNum) {
                int holding = data[startLock];
                data[startLock] = data[data.length -1 -endLock];
                data[data.length -1 -endLock] = holding;
                endLock += 1;
                if (SkipNum == true){
                    startLock = startLock - 1;
                    SkipNum = false;
                } 
            }
            else {
                if (SkipNum == true){
                    int temp = data[startLock];
                    data[startLock] = data[startLock -1];
                    data[startLock -1] = temp;
                    SkipNum = false;
                }
                else {
                    startLock += 1;
                }
            }
        }
        
        int Index = 0;
        while (Index < data.length){
            if (data[Index] == splitNum){
                break;
            }
            Index += 1;
        }
        return(Index);
        
    }
    public static void main(String[] args){
        int[] array = {3, 5, -5, 21, 1, 71, 6, 22, 7, 100, -100, -99, -89}; 
        SortValue(array, 5);
    }
}
