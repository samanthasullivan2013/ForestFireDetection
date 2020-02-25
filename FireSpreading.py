import random
import time
from sense_hat import SenseHat

R = (255, 0, 0)
Y = (255,255,0)
O = (0, 0, 0)
sense=SenseHat()

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
    
while True:
  sense.set_pixels(ROOO())

  sectornum = random.randint(1,4)
  sectorname = ""
  temp = 0
  print sectornum 
  
  time.sleep(2.4)
  
  
  time.sleep(1)
  temp = random.randint(60,80)
  print temp
  
  if temp < 70:#no fire
    print 'no fire'
  else:#there is a fire
    if sectornum == 1:
      sectorname = "Sector 1"#fire in sector 1
      print ('Emergency started in sector 1')
      sense.set_pixels(ROOO())
      time.sleep(2)
  
    elif sectornum == 2:
      sectorname = "Sector 2"#fire in sector 2
      print ('Emergency started in sector 2')
      sense.set_pixels(OROO())
      time.sleep(2)
  

    elif sectornum == 3:
      sectorname = "Sector 3"#sector 3 fire
      print ('Emergency started in sector 3')
      sense.set_pixels(OORO())
      time.sleep(2)
  
    elif sectornum == 4:
      sectorname = "Sector 4"#sector 4 fire
      print ('Emergency started in sector 4')
      sense.set_pixels(OOOR())
      time.sleep(2)
  
  if temp > 75:
    print 'fire spreading to nearest sector'
    
    if sectornum == 1:
      print ('Emergency spreading from sector 1')
      time.sleep(2)
      spreading = random.randint(1,2)
      if spreading == 1:
        print('Emergency spreaded to sector 2')
        sense.set_pixels(RROO())
      
      elif spreading == 2:
        print('Emergency spreaded to sector 3')
        sense.set_pixels(RORO())

    elif sectornum == 2:
      print ('Emergency spreading from sector 2')
      time.sleep(2)
      spreading = random.randint(1,2)
      if spreading == 1:
        print('Emergency spreaded to sector 1')
      
      elif spreading == 2:
        print('Emergency spreaded to sector 4')
      
    
  
    elif sectornum == 3:
      print ('Emergency spreading from sector 3')
      time.sleep(2)
      spreading = random.randint(1,2)
      if spreading == 1:
        print('Emergency spreaded to sector 4')
      
      elif spreading == 2:
        print('Emergency spreaded to sector 1')
    
    
    elif sectornum == 4:
      print ('Emergency spreading from sector 4')
      time.sleep(2)
      spreading = random.randint(1,2)
      if spreading == 1:
        print('Emergency spreaded to sector 2')
      
      elif spreading == 2:
        print('Emergency spreaded to sector 3')
    
    
    
  else:
    print 'fire not spreading'
  
  
  
  
