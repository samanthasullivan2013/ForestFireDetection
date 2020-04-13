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
sense = SenseHat()
sense.clear()


R = (255, 0, 0)
Y = (255,255,0)
O = (0, 0, 0)

responded1= "False"
responded2= "False"
responded3= "False"
responded4= "False"

ranger1="False"
ranger2="False"
ranger3="False"
ranger4="False"



client= mqtt.Client("client id")
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




client.connect("localhost",8080,60)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  f=open('temp.txt','w+')
  client.subscribe("class/test1")

def on_message(client, userdata, msg):
  message=msg.payload.decode()
  global ranger1
  global ranger2
  global ranger3
  global ranger4
  if "Sector 1" in message:
      print("Sector 1 responded")
      global responded1
      responded1= "True"
      if "False" in ranger1:
          print("User created")
          print(msg.payload.decode())
          f=open('temp.txt','a')
          f.write(msg.payload.decode() + " ,")
          f.close()
          ranger1="true"
          
    
  elif "Sector 2" in message:
     print("Sector 2 responded")
     global responded2
     responded2= "True"
     if "False" in ranger2:
         print("User created")
         print(msg.payload.decode())
         f=open('temp.txt','a')
         f.write(msg.payload.decode() + " ,")
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
         f.write(msg.payload.decode() + " ,")
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
         f.write(msg.payload.decode() + " ,")
         f.close()
         ranger4="true"
    
while True:
    
 #       temp = sense.get_temperature()
        x=random.randint(1,4)
        t=random.randint(35,80)
        #ex=random.randint(1,2)
        #t= round(temp)
        #x=1
      
        if(x==1):
            if t>=70:
                sense.set_pixels(ROOO())
                l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                client.publish(topic,l)
                responded1="False"
                client.on_connect = on_connect
                client.on_message = on_message 
                time.sleep(1)
                sense.clear()
                f=open('Zone1temp.txt','a')
                f.write(str(t) + "\n")
                f.close()
                print(l)
                print("Zone 1 Status: on Fire")
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
                
            elif t>40:
         #           sense.set_pixels(medium)
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
                    print("Zone 1 Status: no Fire (cation)")
                    
            elif t<40:
             #           sense.set_pixels(low)
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
                        
            client.loop()
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
            #        sense.set_pixels(medium)
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
                 #       sense.set_pixels(low)
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
                 #   sense.set_pixels(medium)
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
                     #   sense.set_pixels(low)
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
                 #   sense.set_pixels(medium)
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
                     #   sense.set_pixels(low)
                        l= "(temp:"+str(t)+"zone:"+str(x)+"R1:"+responded1+"R2:"+responded2+"R3:"+responded3+"R4:"+responded4+")"
                        client.publish(topic,l)
                        responded4="False"
                        client.on_connect = on_connect
                        client.on_message = on_message
                        time.sleep(5)
                        #sense.clear()
                        f=open('Zone4temp.txt','a')
                        f.write(str(t) + "\n")
                        f.close()
                        print(l)
                        print("Zone 4")
            client.loop()  
