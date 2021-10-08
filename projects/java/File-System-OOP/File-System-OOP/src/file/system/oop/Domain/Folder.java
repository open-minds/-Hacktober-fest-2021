package file.system.oop.Domain;

import java.util.*;

/**
 *
 * @author Tiago Ribeiro
 */
public class Folder extends StorageUnit{
    
    private TreeSet<StorageUnit> units;
    
    private static final int INITIAL_SIZE = 0;
    
    public Folder(String name) {
        super(name, INITIAL_SIZE, String.format("%s\\%s", System.getProperty("user.dir"), name) );
        this.units = new TreeSet<>();
    }
    
    public boolean addUnit(StorageUnit unit){
        if(unit != null){
            unit.updateLastAccessed();
            this.units.add(unit);
            unit.updatePath(this); //parent unit
            this.setSize(this.getSize() + unit.getSize());
            return true;
        }
        return false;
    }
    
    public boolean deleteUnit(StorageUnit unit){
        if(unit != null){
            return units.remove(unit);
        }
        return false;
    }
    
    public TreeSet<StorageUnit> getUnits() { return units; }

    @Override
    public Folder copyUnit() {
        this.updateCreationDate();
        this.updateLastModified();
        this.updateLastAccessed();
        String copyName = this.getName() + " - Copy";
        return new Folder(copyName);
    }
}
