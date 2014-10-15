import java.io.*;
import java.util.Scanner;
import java.util.regex.MatchResult;

public class Searcha {
  public static void main(String[] args) throws FileNotFoundException {
    Scanner s = new Scanner(new File("data.txt"));
    while (null != s.findWithinHorizon("(?i)\\b消防\\b", 0)) {
      MatchResult mr = s.match();
      System.out.printf("Word found: %s at index %d to %d.%n", mr.group(),
        mr.start(), mr.end());
    }
  }
}
