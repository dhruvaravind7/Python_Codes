public class Workspace {

    public static double Sum(double num1, double num2){
        return(num1 + num2);
    }

    public static void main(String[] args) {
        double[] array = {2.4, 3.2};
        
        System.out.println(Sum(array[1], array[0]));
    }
}
