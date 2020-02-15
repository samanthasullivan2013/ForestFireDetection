
package firewatch;

public class Emergency {
    
    private String StartingSector;
    private double timeActive;
    private int avgTempCelsius;
    private int eventNumber;
    private String[] activeSectors;
    private int highestTempCelsius;

    public Emergency(String StartingSector, double timeActive, int avgTempCelsius, int eventNumber, String[] activeSectors, int highestTempCelsius) {
        this.StartingSector = StartingSector;
        this.timeActive = timeActive;
        this.avgTempCelsius = avgTempCelsius;
        this.eventNumber = eventNumber;
        this.activeSectors = activeSectors;
        this.highestTempCelsius = highestTempCelsius;
    }

    public String getStartingSector() {
        return StartingSector;
    }

    public double getTimeActive() {
        return timeActive;
    }

    public int getAvgTempCelsius() {
        return avgTempCelsius;
    }

    public int getEventNumber() {
        return eventNumber;
    }

    public String[] getActiveSectors() {
        return activeSectors;
    }

    public int getHighestTempCelsius() {
        return highestTempCelsius;
    }

    public void setStartingSector(String StartingSector) {
        this.StartingSector = StartingSector;
    }

    public void setTimeActive(double timeActive) {
        this.timeActive = timeActive;
    }

    public void setAvgTempCelsius(int avgTempCelsius) {
        this.avgTempCelsius = avgTempCelsius;
    }

    public void setEventNumber(int eventNumber) {
        this.eventNumber = eventNumber;
    }

    public void setActiveSectors(String[] activeSectors) {
        this.activeSectors = activeSectors;
    }

    public void setHighestTempCelsius(int highestTempCelsius) {
        this.highestTempCelsius = highestTempCelsius;
    }
    
    

}