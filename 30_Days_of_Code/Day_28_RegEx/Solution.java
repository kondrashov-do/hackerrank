import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        // Create a Pattern object (compiled RegEx) and save it as 'p'
        Pattern p = Pattern.compile(".+@gmail\\.com$");//Pattern.compile("^[a-z]+\\s");

        Scanner scan = new Scanner(System.in);
        int arrSize = scan.nextInt();
        List<String> list = new ArrayList();

        for (int i = 0; i < arrSize; i++) {
            String name = scan.next();
            String email = scan.next();
            //System.out.println(arr[i]);
            // We need a Matcher to match our compiled RegEx to a String
            Matcher matcher = p.matcher(email);
            if (matcher.find()){
                list.add(name);
            }
        }
        Collections.sort(list);
        for (String s : list) {
            System.out.println(s);
        }
    }
