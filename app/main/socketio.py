from .. import socketio
from flask_socketio import SocketIO,emit

@socketio.on('my event')
def my_event(message):
    print('received msg:'+str(message))
    emit('my response','您好，我是魏春华')
@socketio.on('my response')
def my_response(message):
    print('res:'+str(message))
