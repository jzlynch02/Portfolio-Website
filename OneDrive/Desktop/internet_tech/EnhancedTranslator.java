import java.util.HashMap;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class EnhancedTranslator {
    private static HashMap<String, String> dictionary = new HashMap<>();
    
    public static void main(String[] args) {
        // Populate the dictionary with more words
        populateDictionary();
        
        Scanner scanner = new Scanner(System.in);
        
        while(true) {
            System.out.println("--------------------------------------------------");
            System.out.println("\nOptions:");
            System.out.println("1. Translate a word");
            System.out.println("2. List all words");
            System.out.println("3. Sort and list all words");
            System.out.println("4. Exit");
            System.out.print("Choose an option (1/2/3/4): ");
            
            int choice = scanner.nextInt();
            scanner.nextLine();  // consume newline
            
            switch(choice) {
                case 1:
                    System.out.print("Enter an English word to translate to Spanish: ");
                    String word = scanner.nextLine().toLowerCase();
                    translateWord(word);
                    break;
                case 2:
                    listWords();
                    break;
                case 3:
                    sortAndListWords();
                    break;
                case 4:
                    System.out.println("Goodbye!");
                    return;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }

    private static void populateDictionary() {
        dictionary.put("hello", "hola");
        dictionary.put("goodbye", "adiÃ³s");
        dictionary.put("please", "por favor");
        dictionary.put("thank you", "gracias");
        dictionary.put("friend", "amigo");
        dictionary.put("computer", "computadora");
        // Add more words as needed
    }
    
    private static void translateWord(String word) {
        if (dictionary.containsKey(word)) {
            System.out.println("The Spanish translation for '" + word + "' is: " + dictionary.get(word));
        } else {
            System.out.println("Sorry, that word is not available for translation.");
        }
    }
    
    private static void listWords() {
        System.out.println("\nAvailable words for translation:");
        for (String key : dictionary.keySet()) {
            System.out.println(key);
        }
    }
    
    private static void sortAndListWords() {
        ArrayList<String> sortedWords = new ArrayList<>(dictionary.keySet());
        Collections.sort(sortedWords);
        System.out.println("\nSorted words available for translation:");
        for (String word : sortedWords) {
            System.out.println(word);
        }
    }
}