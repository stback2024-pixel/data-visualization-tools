#!/usr/bin/env python
import socketio
from bokeh.plotting import figure, show
from bokeh.io import curdoc

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.on('message')
def message(sid, data):
    print('message ', data)

if __name__ == '__main__':
    socketio.serve(app, host='0.0.0.0', port=5000)