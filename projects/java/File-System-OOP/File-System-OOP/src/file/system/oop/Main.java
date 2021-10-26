package file.system.oop;

import file.system.oop.Domain.File;
import file.system.oop.Domain.Folder;

/**
 *
 * @author Tiago Ribeiro
 */
public class Main {

    public static void main(String[] args) {
        
        //Folders & Files creation
        Folder pearlJam = new Folder("Pearl_Jam");
        Folder ten = new Folder("Ten");
        
        File alive = new File("Alive", ".mp4", "...I'm still alive...");
        File jeremy = new File("Jeremy", ".mp4", "...King Jeremy the wicked...");
        File black = new File("Black", ".mp4", "...How quick the sun can, drop away...");

        //Move folder into another folder
        pearlJam.addUnit(ten);
        
        //Move files into 'album' folder
        ten.addUnit(alive);
        ten.addUnit(jeremy);
        ten.addUnit(black);
        
        //Change read permission
        System.out.printf("-> Before:\n%s\n", black.getContent());
        black.changeRead();
        System.out.printf("-> After:\n%s\n", black.getContent()); 
        
        //Copy a file
        File copiedFile = black.copyUnit();
        System.out.println("\nOriginal File: " + black);
        System.out.println("Copied File: " + copiedFile);
        
        //Folder content: sorted alphabetically due to Comparable
        System.out.println("\n" + ten.getUnits());
        
        //Check one song path
        System.out.println("\nPath: " + black.getPath());
    }
}
