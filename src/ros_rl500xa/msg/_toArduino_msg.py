"""autogenerated by genpy from ros_rl500xa/toArduino_msg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class toArduino_msg(genpy.Message):
  _md5sum = "f91b4a8598aa3fa9c07c3c68c4411337"
  _type = "ros_rl500xa/toArduino_msg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 fr_pwm
int32 lr_pwm
int32 turret_pulse_width
string xAxisDirection
string yAxisDirection
int32 movingRobot
int32 sendEncoderData
int32 resetEncoders

"""
  __slots__ = ['fr_pwm','lr_pwm','turret_pulse_width','xAxisDirection','yAxisDirection','movingRobot','sendEncoderData','resetEncoders']
  _slot_types = ['int32','int32','int32','string','string','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       fr_pwm,lr_pwm,turret_pulse_width,xAxisDirection,yAxisDirection,movingRobot,sendEncoderData,resetEncoders

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(toArduino_msg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.fr_pwm is None:
        self.fr_pwm = 0
      if self.lr_pwm is None:
        self.lr_pwm = 0
      if self.turret_pulse_width is None:
        self.turret_pulse_width = 0
      if self.xAxisDirection is None:
        self.xAxisDirection = ''
      if self.yAxisDirection is None:
        self.yAxisDirection = ''
      if self.movingRobot is None:
        self.movingRobot = 0
      if self.sendEncoderData is None:
        self.sendEncoderData = 0
      if self.resetEncoders is None:
        self.resetEncoders = 0
    else:
      self.fr_pwm = 0
      self.lr_pwm = 0
      self.turret_pulse_width = 0
      self.xAxisDirection = ''
      self.yAxisDirection = ''
      self.movingRobot = 0
      self.sendEncoderData = 0
      self.resetEncoders = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3i.pack(_x.fr_pwm, _x.lr_pwm, _x.turret_pulse_width))
      _x = self.xAxisDirection
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.yAxisDirection
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3i.pack(_x.movingRobot, _x.sendEncoderData, _x.resetEncoders))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.fr_pwm, _x.lr_pwm, _x.turret_pulse_width,) = _struct_3i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.xAxisDirection = str[start:end].decode('utf-8')
      else:
        self.xAxisDirection = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.yAxisDirection = str[start:end].decode('utf-8')
      else:
        self.yAxisDirection = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.movingRobot, _x.sendEncoderData, _x.resetEncoders,) = _struct_3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3i.pack(_x.fr_pwm, _x.lr_pwm, _x.turret_pulse_width))
      _x = self.xAxisDirection
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.yAxisDirection
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3i.pack(_x.movingRobot, _x.sendEncoderData, _x.resetEncoders))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.fr_pwm, _x.lr_pwm, _x.turret_pulse_width,) = _struct_3i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.xAxisDirection = str[start:end].decode('utf-8')
      else:
        self.xAxisDirection = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.yAxisDirection = str[start:end].decode('utf-8')
      else:
        self.yAxisDirection = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.movingRobot, _x.sendEncoderData, _x.resetEncoders,) = _struct_3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3i = struct.Struct("<3i")
