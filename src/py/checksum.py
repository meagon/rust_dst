import os,time
import sha, md5, binascii
import sys
from copy import deepcopy
import traceback

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO
import requests


class File(object):

    def __init__(self, content = StringIO(''), url =''):
        self.content = content

    def update_content(self, binary_file):
        self.content  = StringIO( binary_file )

    @property
    def v(self):
        return self.content.read()
    # self.content = content
    @property 
    def crc32(self):
        block_size = 8096
        self.content.seek(0)
        content = self.content
        buf = content.read(block_size)
        crc = 0
        while(len (buf) != 0):
            crc = binascii.crc32(buf, crc)
            buf = content.read(block_size)
        if crc >=0 :
            s = "%X" % (crc)
            s = "%s%s" % ((8-len(s))*'0', s)
        else:
            s = "%X" % (~crc ^ 0xffffffff)
            s = "%s%s" % ((8-len(s))*'0', s)
        return s

    @property
    def md5(self):
        self.content.seek(0)
        content = self.content
        m = md5.new()
        while 1:
            data = content.read(8096)
            if not data:
                break
            m.update(data)
        return m.hexdigest().upper()

    def __cmp__(self, other):
       pass

    def hash(self):
        #self.update_content()
        if self.content:
            #print(self.hash , self.md5)
            return self.md5 +"." + self.crc32
            return self.hash.upper() == self.md5 +"." + self.crc32
        else:
            print("_hash_check error ")
            return False



if __name__ == '__main__':
        #store_hash_check()
    avml_check()
