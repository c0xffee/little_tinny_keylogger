import datetime


log = 'keylog.dll'

f = open(log, 'r', encoding='latin-1')
content = f.read()[48:].split('\n')  #skip the first 48 bytes (dll magic number)
f.close()
res = ''
for char in content:
  if char == 'space':
    char = ' '
  elif char == 'enter':
    char = '\n'
  elif len(char) > 1:
    char = '[%s]\n'%char

  res = '%s%s'%(res, char)

f = open('klog.txt', 'w')
f.write('================%s================\n'%datetime.datetime.now().isoformat())
f.write(res)
f.close()  
print(res)
