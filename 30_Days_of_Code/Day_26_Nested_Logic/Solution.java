import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int retDay = scan.nextInt();
        int retMonth = scan.nextInt();
        int retYear = scan.nextInt();

        int expectedDay = scan.nextInt();
        int expectedMonth = scan.nextInt();
        int expectedYear = scan.nextInt();

        int fine = 0;

        if (retYear<expectedYear) {
            fine = 0;
        }
        else if (retYear<expectedYear && retMonth<expectedMonth) {
            fine = 0;
        }
        else if (retYear<expectedYear && retMonth<expectedMonth && retDay<expectedDay) {
            fine = 0;
        }
        else if(expectedDay < retDay){
            fine = 15 * (retDay - expectedDay);
            if (expectedMonth < retMonth) {
                fine = 500 * (retMonth - expectedMonth);
                if (expectedYear < retYear) {
                    fine = 10_000;
                }
            }
        }
        else if (expectedMonth < retMonth) {
            fine = 500 * (retMonth - expectedMonth);
                if (expectedYear < retYear) {
                    fine = 10_000;
                }
        }
        else if (expectedYear < retYear) {
                    fine = 10_000;
                }
        System.out.println(fine);
    }
}
