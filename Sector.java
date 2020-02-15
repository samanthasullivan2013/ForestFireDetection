
package firewatch;

public class Sector {
    
    public String sectorName;
    public String ranger;
    public int criticalTemperature;
    public int currentTemperature;
    public boolean isOnFire;

    public Sector(String sectorName, String ranger, int criticalTemperature, int currentTemperature, boolean isOnFire) {
        this.sectorName = sectorName;
        this.ranger = ranger;
        this.criticalTemperature = criticalTemperature;
        this.currentTemperature = currentTemperature;
        this.isOnFire = isOnFire;
    }

    public String getSectorName() {
        return sectorName;
    }

    public String getRanger() {
        return ranger;
    }

    public int getCriticalTemperature() {
        return criticalTemperature;
    }

    public int getCurrentTemperature() {
        return currentTemperature;
    }

    public boolean getIsOnFire() {
        return isOnFire;
    }

    public void setSectorName(String sectorName) {
        this.sectorName = sectorName;
    }

    public void setRanger(String ranger) {
        this.ranger = ranger;
    }

    public void setCriticalTemperature(int criticalTemperature) {
        this.criticalTemperature = criticalTemperature;
    }

    public void setCurrentTemperature(int currentTemperature) {
        this.currentTemperature = currentTemperature;
    }

    public void setIsOnFire(boolean isOnFire) {
        this.isOnFire = isOnFire;
    }
    
}
