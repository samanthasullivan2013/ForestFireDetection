#import the libraries
from sense_hat import SenseHat
import paho.mqtt.client as droneclient
#import time to set how often the temp will be published
import time
#set the broker url 
broker="localhost"
#set the port number
port=8080
#set the topic
topic="class/drone"

#create a client using the mqtt client imported at the start
#” anyclientid” identifies the client that uses this code e.g.
client1=droneclient.Client("clientid")
# connect the client to the broker. UNCOMMENT THIS TO CONNECT
client1.connect(broker, port)

sense=SenseHat()

R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
Y = (255, 255, 0)
O = (0, 0, 0)

def forwardLeft():
    
    display = [
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return display

#HI DANIEL AND KEVIN. USE THESE METHODS TO CHANGE THE SENSEHATS DISPLAY. 

def forwardRight():
    
    display = [
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return display

def forward():
    
    display = [
    R, R, R, O, O, G, G, G,
    R, R, R, O, O, G, G, G,
    R, R, R, O, O, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return display

def still():
    
    display = [
    R, R, R, O, O, G, G, G,
    R, R, R, O, O, G, G, G,
    R, R, R, O, O, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    B, B, B, O, O, Y, Y, Y,
    B, B, B, O, O, Y, Y, Y,
    B, B, B, O, O, Y, Y, Y,
    ]
    return display
    
def backward():
    
    display = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    B, B, B, O, O, Y, Y, Y,
    B, B, B, O, O, Y, Y, Y,
    B, B, B, O, O, Y, Y, Y,
    ]
    return display

def left():
    
    display = [
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    B, B, B, O, O, O, O, O,
    B, B, B, O, O, O, O, O,
    B, B, B, O, O, O, O, O,
    ]
    return display
    
def right():
    
    display = [
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, Y, Y, Y,
    O, O, O, O, O, Y, Y, Y,
    O, O, O, O, O, Y, Y, Y,
    ]
    return display

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x,1)
    y = round(y,1)
    z = round(z,1)
    
    print("x={0}, y={1}, z={2}".format(x,y,z))
    
    if y < 0:
        sense.set_pixels(forward())
        print("going forward")#This shows the drone tilted forward
        client1.publish(topic,"forward")

        
    elif y > 0.2:
      print("going back")
      sense.set_pixels(backward())#this shows the drone tilted back
      client1.publish(topic,"back")
      
    
    elif x > 0.2:
      print("going right")
      sense.set_pixels(right())#this shows the drone tilted right
      client1.publish(topic,"right")
      
    elif x < 0:
      print("going left")
      sense.set_pixels(left())#this shows the drone tilted left
      client1.publish(topic,"left")
      #HI DANIEL AND KEVIN. THIS IS AN EXAMPLE OF THE PI CHANGING COLOURS AND PUBLISHING
    
    else:
        print("All systems normal")
        sense.set_pixels(still())
        client1.publish(topic,"normal")
        
