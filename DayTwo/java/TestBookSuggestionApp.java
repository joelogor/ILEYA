import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public  class TestBookSuggestionApp{

    @Test
     
    public void testThatAppKeepSuggestingBookWithRandomPageNumberBetweenOneAndHundred() {
        int actual = BookSuggestionApp.suggestRandomPage();
        
        assertTrue(actual >= 1);
        assertTrue(actual <= 100);
    }
    
     @Test
    public void testThatUserCanAddANewBookToTheList() {
        String[] bookList = {"The Hobbit", "The Mystery", "Brave kind"};
        String newBook = "Animal Farm";
        
        String[] expected = {"The Hobbit", "The Mystery", "Brave kind", "Animal Farm"};
        String[] actual = BookSuggestionApp.addNewBook(bookList, newBook);
        
        assertArrayEquals(expected, actual);
        
    }
    
    @Test
    public void testThatUserCanRemoveABookFromTheList() {
        String[] bookList = {"The Hobbit", "The Mystery", "Brave kind"};
        String bookToRemove = "The Mystery";
        
        String[] expected = {"The Hobbit", "Brave kind"};
        String[] actual = BookSuggestionApp.removeBook(bookList, bookToRemove);
        
        assertArrayEquals(expected, actual);
    }

    @Test
    public void testThatUserCanUpdateABookInTheList() {
        String[] bookList = {"The Hobbit", "The Mystery", "Brave kind"};
        String bookToUpdate = "The Mystery";
        String newBookTitle = "Brave kingdom";
        
        String[] expected = {"The Hobbit", "Brave kingdom", "Brave kind"};
        String[] actual = BookSuggestionApp.updateBook(bookList, bookToUpdate, newBookTitle);
        
        assertArrayEquals(expected, actual);
    }

    @Test
    public void testThatUserCanViewListOfBooksInTheList() {
        String[] bookList = {"The Hobbit", "Brave kingdom", "Animal Farm", "Brave kind"};
        
        String expected = "1. The Hobbit\n2. Brave kingdom\n3. Animal Farm\n4. Brave kind\n";
        String actual = BookSuggestionApp.viewList(bookList);
        
        assertEquals(expected, actual);
    }
}






