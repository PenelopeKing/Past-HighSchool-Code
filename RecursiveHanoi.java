/*
Andrew Cheng + Penny King
APCS 4th Period
Unit 8 Lab 3
Tower of Hanoi 
*/

import java.util.*; // to import Scanner

// Towers of Hanoi Lab
public class RecursiveHanoi {
    // pegs numbered: 0, 1, 2
    public static String hanoi(int nDiscs, int fromPeg, int toPeg) {
        // base case
        if (nDiscs == 1) {
            return "Move from " + (fromPeg + 1) + "-->"+ (toPeg+1);
            // moves the disc in the starting position to the end position
        } // end if
        else {
            String output = "";
            int temp = 3 - fromPeg - toPeg;
            // this sets temp to a value (0-2) that start and end are not
                // ex) if start = 1, end = 2; temp => 0
                // ex) if start = 0, end = 2, temp => 1
            output += hanoi(nDiscs - 1, fromPeg, temp);
            output += "\nMove from " + (fromPeg + 1) + "-->" + (toPeg + 1);
            output += "\n" + hanoi(nDiscs - 1, temp, toPeg);
            return output;
            
        } // end else      
    } // end hanoi method

    public static void main (String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Give me how many discs you want.");
        int discs = input.nextInt();
        // assumes user inputs 1-3, but then changes to 0-2
        System.out.println("Give me a start position (1-3).");
        int start = input.nextInt() - 1;
        System.out.println("Give me an end position (1-3).");
        int end = input.nextInt() - 1;
        // calculate the min amount of turns needed to finish
        int minTurns = (int) Math.pow(2, discs) - 1;
        
        System.out.println("The minimum amount of turns is: " + minTurns);
        System.out.println(hanoi(discs, start, end));
        // tests out function

    } // end main method
}

