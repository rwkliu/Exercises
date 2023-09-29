import java.util.List;
import java.util.ArrayList;

class MyUnion {
  public static void main(String[] args) {
    String input1a = "zpadinton";
    String input1b = "paqefwtdjetyiytjneytjoeyjnejeyj";
    String expected1 = "zpadintoqefwjy";
    boolean compare1 = expected1.equals(union(input1a, input1b));
    System.out.println(compare1);

    String input2a = "ddf6vewg64f";
    String input2b = "gtwthgdwthdwfteewhrtag6h4ffdhsd";
    String expected2 = "df6vewg4thras";
    boolean compare2 = expected2.equals(union(input2a, input2b));
    System.out.println(compare2);

    String input3a = "rien";
    String input3b = "cette phrase ne cache rien";
    String expected3 = "rienct phas";
    boolean compare3 = expected3.equals(union(input3a, input3b));
    System.out.println(compare3);
  }

  public static String union(String input1, String input2) {
    List<Character> unionChars = new ArrayList<>();

    for (int i = 0; i < input1.length(); i++) {
      if (!unionChars.contains(input1.charAt(i))) {
        unionChars.add(input1.charAt(i));
      }
    }

    for (int i = 0; i < input2.length(); i++) {
      if (!unionChars.contains(input2.charAt(i))) {
        unionChars.add(input2.charAt(i));
      }
    }

    StringBuilder sb = new StringBuilder();
    for (Character c : unionChars) {
      sb.append(c);
    }
    return sb.toString();

  }
}
