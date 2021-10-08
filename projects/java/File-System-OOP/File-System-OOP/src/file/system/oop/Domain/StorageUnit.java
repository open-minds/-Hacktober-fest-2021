package file.system.oop.Domain;

import java.time.LocalDateTime;

/**
 * 
 * @author Tiago Ribeiro
 */
public abstract class StorageUnit implements Comparable<StorageUnit>{
    
    private String name;
    private long size;  //bytes
    private String path;
    private LocalDateTime creationDate;
    private LocalDateTime lastModified;
    private LocalDateTime lastAccessed;
    private boolean readPermission;
    private boolean writePermission;
    private boolean executePermission;
    
    public StorageUnit(String name, long size, String path){
        this.name = name;
        this.size = size;
        this.path = path;
        this.creationDate = LocalDateTime.now();
        this.lastModified = LocalDateTime.now();
        this.lastAccessed = LocalDateTime.now();
        this.readPermission = true;
        this.writePermission = true;
        this.executePermission = true;
    }

    public String getName() { return name; }
    public long getSize() { return size; }
    public String getPath() { return path; }
    public LocalDateTime getCreationDate() { return creationDate; }
    public LocalDateTime getLastModified() { return lastModified; }
    public LocalDateTime getLastAccessed() { return lastAccessed; }
    public boolean getReadPermission(){ return readPermission; }
    public boolean getWritePermission(){ return writePermission; }
    public boolean getExecutePermission(){ return executePermission; }
    
    public String checkPermissions(){
        return String.format("Read: %s | Write: %s | Execute: %s", this.readPermission, this.writePermission, this.executePermission);
    }
    
    public boolean isTypeFile(){
        return this instanceof File;
    }
    
    public void changeRead(){
        this.lastModified = LocalDateTime.now();
        this.lastAccessed = LocalDateTime.now();
        if(this.readPermission){
            this.readPermission = false;
            System.out.println("Permission to read is now denied.");
        }else{
            this.readPermission = true;
            System.out.println("Permission to read is now allowed.");
        }
    }
    
    public void changeWrite(){
        this.lastModified = LocalDateTime.now();
        this.lastAccessed = LocalDateTime.now();
        if(this.writePermission){
            this.writePermission = false;
            System.out.println("Permission to write is now denied.");
        }else{
            this.writePermission = true;
            System.out.println("Permission to write is now allowed.");
        }
    }
    
    public void changeExecute(){
        this.lastModified = LocalDateTime.now();
        this.lastAccessed = LocalDateTime.now();
        if(this.executePermission){
            this.executePermission = false;
            System.out.println("Permission to execute is now denied.");
        }else{
            this.executePermission = true;
            System.out.println("Permission to execute is now allowed.");
        }
    }
    
    public void setName(String name){
        this.lastModified = LocalDateTime.now();
        this.lastAccessed = LocalDateTime.now();
        this.name = name;
    }
    
    public void setSize(long size){
        this.lastModified = LocalDateTime.now();
        this.lastAccessed = LocalDateTime.now();
        this.size += size;
    }
    
    protected void setPath(String path){
        this.path = path;
    }
    
    public void updatePath(StorageUnit su){
        String newPath = String.format("%s\\%s", su.getPath(), this.name);
        this.setPath(newPath);
    }
    
    public void updateCreationDate(){
        this.creationDate = LocalDateTime.now();
    }
    
    public void updateLastModified(){
        this.lastModified = LocalDateTime.now();
    }
    
    public void updateLastAccessed(){
        this.lastAccessed = LocalDateTime.now();
    }
     
    public abstract StorageUnit copyUnit();
    
    @Override
    public String toString(){
        if(this instanceof Folder){
            return String.format("Name: %s, Type: Folder, Size: %d Bytes - (%s)", this.getName(), this.size, this.creationDate.toString());
        }else{
            return String.format("Name: %s, Type: %s, Size: %d Bytes - (%s)", this.getName(), ((File) this).getType(), this.size, this.creationDate.toString());
        }
    }
    
    @Override
    public int compareTo(StorageUnit storageUnit){
        return this.getName().compareTo(storageUnit.getName());
    }
}
