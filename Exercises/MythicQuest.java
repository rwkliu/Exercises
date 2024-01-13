// import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.Random;

class MythicQuestPlayer {
  int strength;
  int dexterity;
  int constitution;
  int intelligence;
  int wisdom;
  int charisma;
  int hitPoints;

  public MythicQuestPlayer() {
    this.strength = calculateAbilityScore();
    this.dexterity= calculateAbilityScore();
    this.constitution = calculateAbilityScore();
    this.intelligence = calculateAbilityScore();
    this.wisdom = calculateAbilityScore();
    this.hitPoints = getHitPoints(this.constitution);
  }

  public static int calculateAbilityScore(){
      Random random = new Random();
      int totalDieRolls = 4;
      int[] rolls = new int[totalDieRolls];
      for (int i = 0; i < totalDieRolls; i++)
      {
          rolls[i] = random.nextInt(6) + 1;          
      }
      
      int min = rolls[0];
      for (int i = 0; i < totalDieRolls; i++) {
        min = Math.min(min, rolls[i]);
      }

      // sum top three dice rolls
      int abilityScore = 0;
      for (int i = 0; i < totalDieRolls - 1; i++) {
          abilityScore += rolls[i];
      }

      return abilityScore - min;
  }

  public static int getHitPoints(int constitution) {
    int cm = (constitution - 10) / 2;
    int hp = cm + 10;
    return hp;
  }

  public void showAttributes() {
    System.out.println(this.strength);
    System.out.println(this.dexterity);
    System.out.println(this.constitution);
    System.out.println(this.intelligence);
    System.out.println(this.wisdom);
    System.out.println(this.charisma);
    System.out.println(this.hitPoints);
  }

  public static void main(String[] args) {
    MythicQuestPlayer player = new MythicQuestPlayer();
    player.showAttributes();
  }
}