import java.util.*;
class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int numComputers = input.nextInt();

        String[] names = new String[numComputers];
        int[] ram = new int[numComputers];
        int[] cpu = new int[numComputers];
        int[] space = new int[numComputers];

        for(int i = 0; i < numComputers; i++){
            names[i] = input.nextLine();
            ram[i] = input.nextInt();
            cpu[i] = input.nextInt();
            space[i] = input.nextInt();
        }
    }
}