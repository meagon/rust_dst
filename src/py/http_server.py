
#-encoding=utf-8 -*-
import bottle

from bottle import route,run,template

import bottle
from bottle import get,post,request,response, redirect
from bottle import  static_file, error
import traceback
import sys 
import os
#import gevent

import checksum
import backend_db

@route("/")
def index():
    html = """<form action="/upload/" enctype="multipart/form-data"  method="POST">
        <input type="file" name="file1" />
        <input type="text" name="scan" value="text"/>
        <input type="submit" value ="Submit">
    </form>
    """
    return html

@route('/upload/', method='POST') 
def do_upload():
    try:
        file_content =[]

        print(dir ( request ))
        #print(request.files)
        print(dir (request.files))
        fffs = request.files
        upload_file = fffs.get("file1")
        fffs = fffs.items()
        print("type",type(request.files.get("filename")))
        #$upload_file = request.files.file

        #print(upload_file.file.readlines())

        print(dir(upload_file))
        filename = upload_file.filename
        upload_file = upload_file.file
        upload_file.seek(0)
        db = backend_db.storage()
        db.open()
        f = checksum.File()
        f.update_content( upload_file.read() )
        k = f.hash()

        db.put(k , f.v)
        query = request.query
        file_name = query.get("filename")
    
    except Exception as exc:
        traceback.print_exc()

@route("/download/<hash_value>", method="GET")
def download(hash_value):
    
    db = backend_db.storage()
    db.open()
    z = db.get( hash_value )
    if z:
        return str(z)
    else:
        return bottle.HTTPError(404, "File does not exist.")


def http_run():
#    bottle.debug(True)
    bottle.run(reloader=False,host='0.0.0.0', port=8088)
    #gevent.sleep(0)

if __name__ == '__main__':
    http_run()
