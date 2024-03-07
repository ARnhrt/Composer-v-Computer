package ccscmusicgen;

import java.lang.reflect.Array;
import java.util.*;

public class CCSCMusicGen {

    public static void main(String[] args) {
        //Constant variables
        final int TIME = 4;
        final int COUNTS = 3;
        final int MEASURES = 4;
        final int BEATS = COUNTS * MEASURES;
        //New random
        Random rand = new Random();

        //Key signature
        ///variables and lists
        char[] startingNote = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
        System.out.print(Array.getChar(startingNote, rand.nextInt(7)));
        switch (rand.nextInt(3)) {  //Choose Sharp, Flat, or Natural
            case 0 ->
                System.out.print("# ");
            case 1 ->
                System.out.print("b ");
            case 2 ->
                System.out.print(" ");
        }
        switch (rand.nextInt(2)) {  //Choose Major or Minor
            case 0 ->
                System.out.println("Major");
            case 1 ->
                System.out.println("Minor");
        }
        //loop and selection structure
        //scanner
        Scanner input = new Scanner(System.in);
        //sentinnel
        String loop = "Stop";
        do {
            System.out.println("");
        } while (!"Stop".equals(loop));
    }

    public static void melody(int beats, int time) {
        Random rand = new Random();
        //Rhythm
        double[] noteLengths = {0.25, 0.5, 0.75, 1.0, 2.0, 3.0, 4.0};
        //double[] noteLength = {0.33, 0.66, 1.0, 2.0, 3.0};   //for 6/8 time
        int count = 0;
        int total = 0;
        double n;
        ArrayList<Double> rhythm = new ArrayList<>();

        while (count < beats) {
            n = Array.getDouble(noteLengths, rand.nextInt(7));
            rhythm.add(n);
            count++;
            total += n;

//            if (total > beats) {
//                n -= beats - total;
//                rhythm.set(count - 1, n);
//            }
        }
        System.out.println("\nRhythm: ");
        for (double i : rhythm) {
            System.out.print(i + " ");
        }
        System.out.println("\nTotal: " + total);
        //Notes
        int[] melody = new int[count];
        for (int i = 0; i < count; i++) {
            melody[i] = rand.nextInt(8);
        }
        System.out.println("\nNotes: ");
        for (int i : melody) {
            System.out.print(i + " ");
        }
    }
}
