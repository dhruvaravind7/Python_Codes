import java.util.ArrayList;

public class Array_Calc {

    private ArrayList<Integer> numbers = new ArrayList<Integer>();
    
    public  void generate_Array(int numelements, int range) {
        for (int i = 0; i< numelements; i++){
            int value = (int) ((Math.random() * range) + 1);
            numbers.add(value);
        }
    }

    public void print_Array(){
        System.out.println(numbers);
    }

    public int FindRange(){
        int maxNumber = numbers.get(0);
        int minNumber = numbers.get(0);
        for (int i = 1; i<numbers.size();i++){
            if (numbers.get(i) > maxNumber){
                maxNumber = numbers.get(i);
            } else if (numbers.get(i) < minNumber){
                minNumber = numbers.get(i);
            }
        }
        return (maxNumber - minNumber);
    }

    public double FindMedian() {
        double median;
        if (numbers.size() % 2 == 1){
            int pos = (int) (numbers.size() / 2);
            median = numbers.get(pos);
        } else
        {
            int num1 = numbers.get((numbers.size()/2) -1);
            int num2 = numbers.get(numbers.size()/2);
            median = (num1 + num2)/2;            
        }
        return (median);
    }

    private int[] findSmallestNum(int startingPos){
        int pos = startingPos;
        int smallestNum = numbers.get(startingPos);
        for (int i = startingPos + 1; i < numbers.size(); i++){
            if (numbers.get(i) < smallestNum){
                pos = i;
                smallestNum = numbers.get(i);
            }
        }
        int[] small = {smallestNum, pos};
        return(small);
    }

    public ArrayList<Integer> OrderList() {
        for (int i = 0; i<numbers.size(); i++){
            int smallestNum = findSmallestNum(i)[0];
            int smallestPos = findSmallestNum(i)[1];
            numbers.set(smallestPos, numbers.get(i));
            numbers.set(i, smallestNum);
        }
        return(numbers);
    }

    public int FindMode() {
        int longestNum = 0;
        int longestStreak = 0;
        for (int i = 0; i<numbers.size(); i++){
            int currStreak = 0;
            int currNum = numbers.get(i);
            for (int j = 0; j< numbers.size(); j++){
                if (numbers.get(j) == currNum){
                    currStreak ++;
                } 
            }
            if (currStreak > longestStreak){
                longestStreak = currStreak;
                longestNum = currNum;
            }
        }
        return (longestNum);
    }

    public void StandardDeviation() {
        
    }

    public static void main(String[] args) {
        Array_Calc array1 = new Array_Calc();
        array1.generate_Array(8,10);
        array1.print_Array();
        System.out.println(array1.FindRange());
        System.out.println(array1.FindMedian());
        System.out.println(array1.FindMode());
        array1.print_Array();
        System.out.println(array1.OrderList());
    }
}
