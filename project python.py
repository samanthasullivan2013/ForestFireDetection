#import the libraries
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
#import time to set how often the temp will be published
import time
#set the broker url 
broker="mqtt.eclipse.org"
#set the port number
port=1880
#set the topic
topic="class/topic"
sense = SenseHat()
sense.clear()


b = (0,0,255)
r = (255,0,0)
w = (255,255,255)

client1= mqtt.Client("client id")
low =[
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]

medium=[
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w
    ]

high=[
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]




client1.connect("localhost",1880,60)




while True:
        
        temp = sense.get_temperature()
        
        t= round(temp)

      
        
        if t>=45:
            sense.set_pixels(high)
            l= " "+str(t)
            client1.publish(topic,l)
            
            time.sleep(5)
            sense.clear()
            print(l)
        elif t>10:
                sense.set_pixels(medium)
                l= " "+str(t)
                client1.publish(topic,l)
                
                time.sleep(5)
                sense.clear()
                print(l)
        elif t<10:
                    sense.set_pixels(low)
                    l= " "+str(t)
                    client1.publish(topic,l)
                    
                    time.sleep(5)
                    sense.clear()
                    print(l)
                    
        
