
public class Ranger {
    
    private String username;
    private int rangerId;
    private String password;

    public Ranger(String username, int rangerId, String password) {
        this.username = username;
        this.rangerId = rangerId;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public int getRangerId() {
        return rangerId;
    }

    public String getPassword() {
        return password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setRangerId(int rangerId) {
        this.rangerId = rangerId;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    
    
    
    
    
}
