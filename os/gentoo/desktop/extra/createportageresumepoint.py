#!/bin/env python

# Script to create/delete a portage resume point
# Jordan Callicoat < MonkeeSage at gmail dot com >
# public domain

import os, sys, shutil

real_path = '/var/cache/edb/mtimedb'
back_path = '%s.resume' % real_path

if '-h' in sys.argv or '--help' in sys.argv:
   sys.exit('''
   Script to create/delete a portage resume point

       -r, --resume    Resumes from last point
       -d, --delete    Deletes resume point
       [default]       Creates resume point
   ''')
elif '-d' in sys.argv or '--delete' in sys.argv:
  try:
    os.unlink(back_path)
  except:
    pass
  print "Removed `%s'" % back_path
else:
  if '-r' in sys.argv or '--resume' in sys.argv:
    shutil.copy(back_path, real_path)
    os.system('emerge --resume')
  else:
    shutil.copy(real_path, back_path)
    print "Created `%s'" % back_path 
