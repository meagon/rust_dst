

import plyvel
import  zmq
import gevent


def open_db(db_dir):

    # Create a database with options that result in additional object
    # allocation (e.g. LRU cache).

    db = plyvel.DB(
                db_dir,
                create_if_missing = True,
                lru_cache_size=1024 * 1024,
                bloom_filter_bits=10 ) 
    
    return db

    db.put(b'key', b'value')
    wb = db.write_batch()
    sn = db.snapshot()
    it = db.iterator()
    snapshot_it = sn.iterator()



