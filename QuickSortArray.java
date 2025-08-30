public class QuickSortArray {

    // The function below converts an array into a string that looks like an array and prints it out.
    public static void PrintArray(int[] array){
        int counter = 0;
        String StringArray = "[";
        while (counter < array.length -1){
            StringArray = StringArray + array[counter] + ", ";
            counter += 1;
        }
        StringArray = StringArray + array[counter] + "]";
        System.out.println(StringArray);
    }
    public static int SortValue(int[] data, int splitNum, int startLock, int endLock) {

        // The SkipNum variable represents if we changed startLock to skip over the current number because it equals splitNum
        boolean SkipNum = false;

        // The while loop goes through every number and checks to see if they are larger or smaller than the inputted number 

        while (endLock + startLock < data.length -1) {
            
            // The if statement below checks to see if the current number is equal to the target number and adds 1 to startLock and changes SkipNum to true.
            if (data[startLock] == splitNum){
                startLock += 1;
                SkipNum = true;
            }
            // The outer if statement checks to see if the current number is greater than the target number and switches it with the last unlocked position.
            if (data[startLock] > splitNum) {
                int holding = data[startLock];
                    data[startLock] = data[data.length -1 -endLock];
                    data[data.length -1 -endLock] = holding;
                    endLock += 1;
                // The if statement below occurs if SkipNum was true and resets startLock to its original spot and converts SkipNum back to false.
                if (SkipNum == true){
                    startLock = startLock - 1;
                    SkipNum = false;
                }
            }
            // The code enters the section below if the current number is smaller than the target number.
            else {
                //When SkipNum is true, we switch the current number with the previous number.
                if (SkipNum == true){
                    int temp = data[startLock];
                    data[startLock] = data[startLock -1];
                    data[startLock -1] = temp;
                    SkipNum = false;
                }
                else {
                    // If SkipNum is false all we need to do is move startLock up by one locking up its position.
                    startLock += 1;
                }
            }
        }
        // The code below finds the index of the number that is equal to the inputted target num and returns it.
        int Index = 0;
        while (Index < data.length){
            if (data[Index] == splitNum){
                break;
            }
            Index += 1;
        }
        return(Index);
        
    }
    // This function calls the function above multiple times to sort the list.
    public static void SortArray(int[] array, int StartArray, int EndArray){
        // The if statement tells the computer to stop running the sort function because there are only one elments in the new list.
        if (EndArray - StartArray < 1){
            return;
        }
        //The line below calls the function above with the bounds and the target number. We change the position of the startLock and endLock to set the bounds for the part of the list we want to sort.
        int Index = SortValue(array, array[StartArray], StartArray, array.length - EndArray -1);
        // The two lines below recall this same function again with essentially two lists - the list to the left of the finalized positon and the list to right of it.
        SortArray(array, StartArray, Index -1);
        SortArray(array, Index + 1, EndArray);
    }
    
    public static void main(String[] args){
        // This is the main funciton where we set what the list is and start the code.
        int[] array = {5, 21, -21, -71, -1, 1, 71, 6, 22, 100, -99, 0, 2, -100, 72, 43};
        PrintArray(array);
        SortArray(array, 0, array.length -1);
        PrintArray(array);
    }
}
