cript to edit portage resume list
# Jordan Callicoat < MonkeeSage at gmail dot com >
# public domain

import os, sys, pickle, re

if '-h' in sys.argv or '--help' in sys.argv:
   sys.exit('''
   Script to edit portage resume list

       -l              List items in resume list [default]
       -d NUM          Delete item from list
   ''')

int_rexp = re.compile(r'\d+')

def packge_list(how='read', what=None):
  try:
    if how == 'read':
      fhand = open('/var/cache/edb/mtimedb', 'rb')
      data  = pickle.load(fhand)
      fhand.close()
      return data
    else:
      fhand = open('/var/cache/edb/mtimedb', 'wb')
      pickle.dump(what, fhand)
      fhand.close()
      return True
  except:
    sys.exit()

data = packge_list()
if (not data.has_key('resume') or
    len(data['resume']['mergelist']) == 0):
  sys.exit('Nothing in resume list')
elif '-l' in sys.argv or len(sys.argv) == 1:
  counter = 1
  print 'Items in resume list:'
  for item in data['resume']['mergelist']:
    print '    %d.) %s' % (counter, item[2])
    counter += 1
elif '-d' in sys.argv:
  index = sys.argv.index('-d') + 1
  if len(sys.argv) == 2:
    sys.exit('Error: -d option requires an argument')
  elif not int_rexp.match(sys.argv[index]):
    sys.exit('Error: -d option requires a numeric argument')
  else:
    index = int(sys.argv[index]) - 1
    if len(data['resume']['mergelist']) >= index:
      del data['resume']['mergelist'][index]
      packge_list(how='write', what=data) 
