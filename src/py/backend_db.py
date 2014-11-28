

import plyvel
import os

class storage(object):

    def __init__(self, db_path=None,):

        self.db_path = db_path or "/dev/shm/hello"

    def open(self):
        self.db = plyvel.DB(self.db_path , create_if_missing = True)

    def put(self, k, v):
        self.db.put(k ,v)

    def get(self, k):
        return self.db.get(k) 

    def close(self):
        self.db.close()

    def iter(self):
        return self.db.iterator()

def test():

    s = storage()
    s.open()
    f = s.iter()
    for i in f:
        print(i[0])

if __name__ == "__main__":
    test()
