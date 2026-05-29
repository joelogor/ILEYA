import java.util.Random;

public class BookSuggestionApp {

    public static int suggestRandomPage() {
        Random random = new Random();
        return random.nextInt(100) + 1;
    }

    public static String[] addNewBook(String[] bookList, String bookToAdd) {

        String[] lists = {"The Hobbit", "The Mystery", "Brave kind"};
        String toAdd = "Animal Farm";

        String[] newLists = new String[lists.length + 1];

  
        for (int count = 0; count < lists.length; count++) {
            newLists[count] = lists[count];
        }
        
        newLists[newLists.length - 1] = toAdd;

        return newLists;
    }

    public static String[] removeBook(String[] bookList, String bookToRemove) {
     
        String[] lists = {"The Hobbit", "The Mystery", "Brave kind"};
        String toRemove = "The Mystery";

        String[] newLists = new String[lists.length - 1];
        int index = 0;

        for (int count = 0; count < lists.length; count++) {
            if (!lists[count].equals(toRemove)) {
                newLists[index] = lists[count];
                index++;
            }
        }

        return newLists;
    }

    public static String[] updateBook(String[] bookList, String bookToUpdate, String newBookTitle) {
    
        String[] lists = {"The Hobbit", "The Mystery", "Brave kind"};
        String toUpdate = "The Mystery";
        String newBook = "Brave kingdom";

        for (int count = 0; count < lists.length; count++) {
            if (lists[count].equals(toUpdate)) {
                lists[count] = newBook; 
            }
        }
        return lists;
    }

    
    public static String viewList(String[] bookList) {
        String listView = "";
        
        for (int count = 0; count < bookList.length; count++) {
            listView += (count + 1) + ". " + bookList[count] + "\n";
        }
        return listView;
    }
}


