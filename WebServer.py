from flask import Flask
from flask import render_template
#https://flask.palletsprojects.com/en/3.0.x/deploying/eventlet/
import eventlet
from eventlet import wsgi
from flask_socketio import SocketIO
from flask_socketio import emit
app = Flask(__name__)
#socketio = SocketIO(app)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/weather')
def weather():
   return render_template('weather.html')

@app.route('/aboutus')
def aboutus():
   return render_template('aboutus.html')

@app.route('/task')
def task():
   return render_template('task.html')

@socketio.event
def PestDetection(RxData):
  socketio.emit('PestDetect', RxData)
  print('Receive Pest Data from BBBW')

@socketio.event
def BBBW1Event(RxData):
    print(f'Emitting data to Web_BBBW1Event: {RxData}')
    socketio.emit('Web_BBBW1Event', RxData)
    print('Receive Data from BBBW1')

@socketio.event
def BBBW2Event(RxData):
    print(f'Emitting data to Web_BBBW2Event: {RxData}')
    socketio.emit('Web_BBBW2Event', RxData)
    print('Receive Data from BBBW2')

@socketio.event
def BBBW3Event(RxData):
    print(f'Emitting data to Web_BBBW3Event: {RxData}')
    socketio.emit('Web_BBBW3Event', RxData)
    print('Receive Data from BBBW3')

@socketio.event
def BBBW4Event(RxData):
    print(f'Emitting data to Web_BBBW4Event: {RxData}')
    socketio.emit('Web_BBBW4Event', RxData)
    print('Receive Data from BBBW4')

@socketio.event
def BBBW5Event(RxData):
    print(f'Emitting data to Web_BBBW5Event: {RxData}')
    socketio.emit('Web_BBBW5Event', RxData)
    print('Receive Data from BBBW5')

@socketio.event
def BBBW6Event(RxData):
    print(f'Emitting data to Web_BBBW6Event: {RxData}')
    socketio.emit('Web_BBBW6Event', RxData)
    print('Receive Data from BBBW6')

# Fire Alarm System (234518D)
@socketio.event
def ControlUSR0Led(RxData):
    socketio.emit('ControlUSR0Led', RxData)
    print('Manual Call Point Reset')

@socketio.event
def flame_click(RxData):
    socketio.emit('flame_click', RxData)
    print('Receive Data from Flame Sensor', RxData)

@socketio.event
def tamper_click(RxData):
    socketio.emit('tamper_click', RxData)
    print('Receive Data from tamper click', RxData)
  
@socketio.event
def DoorDetection(RxData):
    socketio.emit('DoorDetection', RxData)
    print('Received status from Door:', RxData)

if __name__ == '__main__':
#app.run(host='192.168.0.X')
  wsgi.server(eventlet.listen(("172.27.145.141", 5000)), app)

