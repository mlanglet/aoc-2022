import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class App {

    public static void main(String[] args) throws IOException {
        // Part one
        var lines = Files.readAllLines(Path.of("input/day1"));
        int current = 0, max = 0;
        for(var line : lines){
            if(line.isEmpty()){
                if(current > max){
                    max = current;
                }
                current = 0;
            } else {
                current += Integer.parseInt(line);
            }
        }
        System.out.printf("The most carried calories is %d%n", max);

        // Part two
        current = 0;
        int top1 = 0, top2 = 0, top3 = 0;
        for(var line : lines){
            if(line.isEmpty()){
                if(current > top1){
                    top3 = top2;
                    top2 = top1;
                    top1 = current;
                } else if (current > top2) {
                    top3 = top2;
                    top2 = current;
                } else if (current > top3) {
                    top3 = current;
                }
                current = 0;
            } else {
                current += Integer.parseInt(line);
            }
        }
        System.out.printf("The sum of calories carried by the three elves carrying the most is %d%n", (top1 + top2 + top3));
    }
}
