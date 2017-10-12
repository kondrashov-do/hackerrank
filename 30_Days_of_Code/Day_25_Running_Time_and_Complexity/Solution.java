import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int amountOfChecks = scan.nextInt();
        for(int i=0; i < amountOfChecks; i++) {
            int checkInt = scan.nextInt();
            int divisor = 2;
            boolean isPrime = true;
            while (divisor < checkInt) {
                if (checkInt % divisor == 0) {
                    isPrime = false;
                    break;
                }
                divisor += 1;
            }
            String result = isPrime && checkInt > 1 ? "Prime" : "Not prime";
            System.out.println(result);
        }
    }
}
