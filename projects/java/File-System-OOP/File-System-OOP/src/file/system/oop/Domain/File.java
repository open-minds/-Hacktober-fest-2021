package file.system.oop.Domain;

/**
 *
 * @author Tiago Ribeiro
 */
public class File extends StorageUnit{
    
    private String content;
    private String type;
    
    public File(String name, String type, String content) {
        super(name, content.getBytes().length, System.getProperty("user.dir"));
        this.content = content;
        this.type = type;
    }
    
    public String getContent(){
        if(this.getReadPermission()){
            return this.content;
        }else{
            return String.format("No reading permission.");
        }
    }
    
    public String getType(){
        return this.type;
    }
    
    public void setContent(String content){
        if(this.getWritePermission()){
            this.content = content;
        }else{
            System.out.println("No writing permission.");
        }
    }  
    
    @Override
    public File copyUnit() {
        this.updateCreationDate();
        this.updateLastModified();
        this.updateLastAccessed();
        String copyName = this.getName() + " - Copy";
        return new File(copyName, this.type, this.content);
    }
}
