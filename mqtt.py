#import the libraries
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import random
#import time to set how often the temp will be published
import time
#set the broker url 
broker="mqtt.eclipse.org"
#set the port number
port=1880
#set the topic
topic="class/topic"
#makes the senseHat object and clears the senseHat display
sense = SenseHat()
sense.clear()

#defines the colours
R = (255, 0, 0)
Y = (255,255,0)
O = (0, 0, 0)

#sets up booleans for if a zone was responded too and to check if there was a ranger created for each zone
responded1= "False"
responded2= "False"
responded3= "False"
responded4= "False"

ranger1="False"
ranger2="False"
ranger3="False"
ranger4="False"


#creats a mqttclient 
client= mqtt.Client("client id")

#sets up the different states for the senseHat display 
def ROOO():
    
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

def RROO():
    
    display = [
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return display
    
def RRRO():
    
    display = [
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    ]
    return display

def RRRR():
    
    display = [
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    ]
    return display

def ORRR():
    
    display = [
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    ]
    return display
    
def OORR():
    
    display = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    ]
    return display

def OOOR():
    
    display = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    ]
    return display

def OROO():
    
    display = [
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return display

def OORO():
    
    display = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    ]
    return display
    
def ROOR():
    
    display = [
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    ]
    return display

def RORO():
    
    display = [
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    ]
    return display

def RROR():
    
    display = [
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    R, R, R, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    R, R, R, O, O, R, R, R,
    ]
    return display
    
def OROR():
    
    display = [
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    O, O, O, O, O, R, R, R,
    ]
    return display



#this tells it to connect at the pi's ip address and to use port 8080 because this is the port that mqtt is running on 
client.connect("localhost",8080,60)
#this subscribes to the phone on the topic test1 and resets the users 
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  f=open('temp.txt','w+')
  client.subscribe("class/test1")
#these are the parameters for what should be done with each message 
def on_message(client, userdata, msg):
#this sets the message variable
  message=msg.payload.decode()
  global ranger1
  global ranger2
  global ranger3
  global ranger4
  #if the message sent back says sector 1 set it to be responded and change respponded 1 to true
  if "Sector 1" in message:
      print("Sector 1 responded")
      global responded1
      responded1= "True"
      #if flase is found in ranger 1 this just means that sector 1 doesnt have a ranger yet and sets this to true and writes the user to a file for the website to access
      if "False" in ranger1:
          print("User created")
          print(msg.payload.decode())
          f=open('temp.txt','a')
          f.write(msg.payload.decode() + ",")
          f.close()
          ranger1="true"
          
  # the previous code is repeated for each sector  
  elif "Sector 2" in message:
     print("Sector 2 responded")
     global responded2
     responded2= "True"
     if "False" in ranger2:
         print("User created")
         print(msg.payload.decode())
         f=open('temp.txt','a')
         f.write(msg.payload.decode() + ",")
         f.close()
         ranger2="true"
     
  elif "Sector 3" in message:
     print("Sector 3 responded")
     global responded3
     responded3= "True"
     if "False" in ranger3:
         print("User created")
         print(msg.payload.decode())
         f=open('temp.txt','a')
         f.write(msg.payload.decode() + ",")
         f.close()
         ranger3="true"
     
  elif "Sector 4" in message:
     print("Sector 4 responded")
     global responded4
     responded4= "True"
     if "False" in ranger4:
         print("User created")
         print(msg.payload.decode())
         f=open('temp.txt','a')
         f.write(msg.payload.decode() + ",")
         f.close()
         ranger4="true"
    
while True:
       #the below section is used to spoof data if you want actual readings just remove the comment on temp as this will et you use the sensehat temprature
        #temp = sense.get_temperature()
        x=random.randint(1,4)
        t=random.randint(35,80)
        #ex=random.randint(1,2)
        #t= round(temp)
        #x=1
        # x corresponds to the sector that it is reading from at that moment
        if(x==1):
        #we have different catches for different temprature ranges the first being if its above or equal to 70
            if t>=70:
                # in this statement we set the sensehat display red in the section that represents sector 1 
                sense.set_pixels(ROOO())
                #this sets the string to be published for the phone to read and lets the phone know what zones need to be responded to and updates the phone on ones that have been dealt with
                l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                client.publish(topic,l)
                #resets the responded message 
                responded1="False"
                #connects to the mqtt broker and subscribes to phone 
                client.on_connect = on_connect
                client.on_message = on_message 
                #sets a delay before clearing the sense display and writing the temprature to a file for charting on the server
                time.sleep(1)
                sense.clear()
                f=open('Zone1temp.txt','a')
                f.write(str(t) + "\n")
                f.close()
                print(l)
                print("Zone 1 Status: on Fire")
                #this is a set that reads if the fire is hot enough to spread to other zones that spoofs which zone it would spread to
                if t>75:
                    print("Fire may spread")
                    spreading= random.randint(1,2)
                    if spreading== 1:
                         print('Emergency spreaded to sector 2')
                         sense.set_pixels(RROO())
                         time.sleep(2)
                    elif spreading == 2:
                         print('Emergency spreaded to sector 3')
                         sense.set_pixels(RORO())
                         time.sleep(2)
            #this is for tempratures greater than 40 but less than 70 and it prints the temprature to a file aswell as resets the responded1 variable  
            elif t>40:
               
                    l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                    client.publish(topic,l)
                    responded1="False"
                    client.on_connect = on_connect
                    client.on_message = on_message
                    time.sleep(5)
                    sense.clear()
                    f=open('Zone1temp.txt','a')
                    f.write(str(t) + "\n")
                    f.close()
                    
                    print(l)
                    print("Zone 1 Status: no Fire (caution)")
            #this is for tempratures less than 40 and it prints the temprature to a file aswell as resets the responded1 variable         
            elif t<40:
             
                        l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                        client.publish(topic,l)
                        responded1="False"
                        client.on_connect = on_connect
                        client.on_message = on_message
                        time.sleep(5)
                        sense.clear()
                        f=open('Zone1temp.txt','a')
                        f.write(str(t) + "\n")
                        f.close()
                        print(l)
                        print("Zone 1 Status: no Fire (ideal temprature)")
             #this just loops the client to listen to published messages so it doesnt miss something coming in from the phone            
            client.loop()
        # the steps for sector 1 repeat for the other 3    
        elif(x==2): 
            if t>=70:
                sense.set_pixels(OROO())
                l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                client.publish(topic,l)
                responded2="False"
                client.on_connect = on_connect
                client.on_message = on_message
                time.sleep(5)
                sense.clear()
                f=open('Zone2temp.txt','a')
                f.write(str(t) + "\n")
                f.close()
                print(l)
                print("Zone 2")
                if t>75:
                    print("Fire may spread")
                    spreading= random.randint(1,2)
                    if spreading== 1:
                         print('Emergency spreaded to sector 1')
                         sense.set_pixels(RROO())
                         time.sleep(2)
                    elif spreading == 2:
                         print('Emergency spreaded to sector 4')
                         sense.set_pixels(OROR())
                         time.sleep(2)
            elif t>40:
            
                    l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                    client.publish(topic,l)
                    responded2="False"
                    client.on_connect = on_connect
                    client.on_message = on_message
                    time.sleep(5)
                    sense.clear()
                    f=open('Zone2temp.txt','a')
                    f.write(str(t) + "\n")
                    f.close()
                    print(l)
                    print("Zone 2")
            elif t<40:
                 
                        l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                        client.publish(topic,l)
                        responded2="False"
                        client.on_connect = on_connect
                        client.on_message = on_message
                        time.sleep(5)
                        sense.clear()
                        f=open('Zone2temp.txt','a')
                        f.write(str(t) + "\n")
                        f.close()
                        print(l)
                        print("Zone 2")
                        
            client.loop()
        elif(x==3):  
            if t>=70:
                sense.set_pixels(OORO())
                l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                client.publish(topic,l)
                responded3="False"
                client.on_connect = on_connect
                client.on_message = on_message
                time.sleep(5)
                sense.clear()
                f=open('Zone3temp.txt','a')
                f.write(str(t) + "\n")
                f.close()
                print(l)
                print("Zone 3")
                if t>75:
                    print("Fire may spread")
                    spreading= random.randint(1,2)
                    if spreading== 1:
                         print('Emergency spreaded to sector 4')
                         sense.set_pixels(OORR())
                         time.sleep(2)
                    elif spreading == 2:
                         print('Emergency spreaded to sector 1')
                         sense.set_pixels(RORO())
                         time.sleep(2)
            elif t>40:
                 
                    l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                    client.publish(topic,l)
                    responded3="False"
                    client.on_connect = on_connect
                    client.on_message = on_message
                    time.sleep(5)
                    sense.clear()
                    f=open('Zone3temp.txt','a')
                    f.write(str(t) + "\n")
                    f.close()
                    print(l)
                    print("Zone 3")
            elif t<40:
                     
                        l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                        client.publish(topic,l)
                        responded3="False"
                        client.on_connect = on_connect
                        client.on_message = on_message
                        time.sleep(5)
                        sense.clear()
                        f=open('Zone3temp.txt','a')
                        f.write(str(t) + "\n")
                        f.close()
                        print(l)
                        print("Zone 3")
                        
            client.loop()
        elif(x==4):  
            if t>=70:
                sense.set_pixels(OOOR())
                l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                client.publish(topic,l)
                responded4="False"
                client.on_connect = on_connect
                client.on_message = on_message
                time.sleep(5)
                sense.clear()
                f=open('Zone4temp.txt','a')
                f.write(str(t) + "\n")
                f.close()
                print(l)
                print("Zone 4")
                if t>75:
                    print("Fire may spread")
                    spreading= random.randint(1,2)
                    if spreading== 1:
                         print('Emergency spreaded to sector 2')
                         sense.set_pixels(OROR())
                         time.sleep(2)
                    elif spreading == 2:
                         print('Emergency spreaded to sector 3')
                         sense.set_pixels(OORR())
                         time.sleep(2)
            elif t>40:
                 
                    l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                    client.publish(topic,l)
                    responded4="False"
                    client.on_connect = on_connect
                    client.on_message = on_message
                    time.sleep(5)
                    sense.clear()
                    f=open('Zone4temp.txt','a')
                    f.write(str(t) + "\n")
                    f.close()
                    print(l)
                    print("Zone 4")
            elif t<40:
                     
                        l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                        client.publish(topic,l)
                        responded4="False"
                        client.on_connect = on_connect
                        client.on_message = on_message
                        time.sleep(5)
                        sense.clear()
                        f=open('Zone4temp.txt','a')
                        f.write(str(t) + "\n")
                        f.close()
                        print(l)
                        print("Zone 4")
            #this just loops the client to listen to published messages so it doesnt miss something coming in from the phone            
            client.loop()  
