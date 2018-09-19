import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


/*


public class BearAndSteadyGene {

    private static int n;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        String s = scanner.next();
        Map<Character, Integer> map = new HashMap<>();
        map.put('A', 0);
        map.put('C', 0);
        map.put('G', 0);
        map.put('T', 0);
        for (Character c : s.toCharArray())
            map.put(c, map.get(c) + 1);

        int left = 0, right = 0, min = Integer.MAX_VALUE;
        while(right < n - 1){
            char rc = s.charAt(right++);
            map.put(rc, map.get(rc) - 1);
            while(isSteady(map)){
                min = Math.min(min, right - left);
                char lc = s.charAt(left++);
                map.put(lc, map.get(lc) + 1);
            }
        }
        System.out.println(min);
    }

    private static boolean isSteady(Map<Character, Integer> map) {
        for (Integer i : map.values())
            if (i > n / 4) return false;
        return true;
    }
}




*/
//------------------------------------------------------------

public class BearAndSteadyGene{
    //private static int n;

    // Complete the steadyGene function below.
    private static boolean isSteady(Map<Character, Integer> map,int n) {
        for (Integer i : map.values())
            if (i > n / 4) return false;
        return true;
    }
    static int steadyGene(String s,int n) {

        Map<Character, Integer> map = new HashMap<>();
        map.put('A', 0);
        map.put('C', 0);
        map.put('G', 0);
        map.put('T', 0);
        System.out.println(n);
        for (Character c : s.toCharArray())
            map.put(c, map.get(c) + 1);

        int left = 0, right = 0, min = Integer.MAX_VALUE;
        while(right < n - 1){
            char rc = s.charAt(right++);
            map.put(rc, map.get(rc) - 1);
            while(isSteady(map,n)){
                min = Math.min(min, right - left);
                System.out.println(min);
                char lc = s.charAt(left++);
                map.put(lc, map.get(lc) + 1);
            }
        }
        //System.out.println(min);
        System.out.println(n);
        return min;


    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String gene = scanner.nextLine();

        int result = steadyGene(gene,n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
