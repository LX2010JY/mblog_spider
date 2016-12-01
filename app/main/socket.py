from .. import socketio
from flask import session,request
from flask_socketio import SocketIO,emit,join_room,leave_room,close_room,rooms,disconnect

thread = None
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(1000)
        count += 1
        socketio.emit('service_response',
                      {'data': '服务器生成事件', 'count': count},
                      namespace='/main')


@socketio.on('connect',namespace='/main')
def connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

    # session[request.sid] = message['name']
    emit('service_response',{'data':'连接成功','count':0})

@socketio.on('chat',namespace='/main')
def chat(message):
    name = message['name']
    content = message['content']

    emit('service_response',{'name':name,'content':content},broadcast=True)