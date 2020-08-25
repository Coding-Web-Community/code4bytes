import java.util.HashMap;
import java.util.Map;

public class Main {

	public static void main(String[] args) {
		if(args.length < 2) System.exit(1);
		String input = args[0];
		String comparison = args[1];

		Map<Character,Integer> inputLetters = new HashMap<>();
		Map<Character,Integer> comparisonLetters = new HashMap<>();
		for(String i : input.split("")) {
			inputLetters.put(i.charAt(0), inputLetters.getOrDefault(i.charAt(0),0)+1);
		}
		for(String i : comparison.split("")) {
			comparisonLetters.put(i.charAt(0), comparisonLetters.getOrDefault(i.charAt(0),0)+1);
		}
		if(inputLetters.equals(comparisonLetters)) {
			System.out.println("True");
			System.exit(0);
		}
		System.out.println("False");
	}

}
