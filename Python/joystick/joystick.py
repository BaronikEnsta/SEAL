from serial import Serial

class Joystick():
  def __init__(self, port, baud=57600):
    self.port = port
    self.baud = baud
    self.ser = None
  def open(self):
    try:
      self.ser = Serial(self.port, self.baud)
    except:
      print(" Open serial port %s failled with baudrate %d"%(self.port, self.baud))

  def __enter__(self):
    self.open()

  def __exit__(self):
    self.ser.close()

  def __iter__(self):
     return self

  def next(self):
    s = ser.readline()
    return s
