
public class LemonadeChange {
  public static void main(String[] args) {
    int[] bills1 = {5,5,5,10,20};
    int[] bills2 = {5,5,10,10,20};
    int[] bills3 = {10,10};

    System.out.println(lemonadeChange(bills1));
    System.out.println(lemonadeChange(bills2));
    System.out.println(lemonadeChange(bills3));
  }

  public static boolean lemonadeChange(int[] bills) {
    int fives = 0;
    int tens = 0;

    for (int bill : bills) {
      if (bill == 5) {
        fives++;
      } else if (bill == 10) {
        if (fives < 1) {
          return false;
        }
        fives--;
        tens++;
      } else if (bill == 20) {
        if (fives > 0 && tens > 0) {
          fives--;
          tens--;
        } else if (fives >= 3) {
          fives -= 3;
        } else {
          return false;
        }
      }
    }
    return true;
  }
}
