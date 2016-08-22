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
    return self

  def __exit__(self, type, value, traceback):
    self.ser.close()
    return True

  def __iter__(self):
    print("iter")
    return self

  def __next__(self):
    s = self.ser.readline()
    return s
