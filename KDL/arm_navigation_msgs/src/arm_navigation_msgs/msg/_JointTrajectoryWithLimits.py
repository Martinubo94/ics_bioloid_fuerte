"""autogenerated by genpy from arm_navigation_msgs/JointTrajectoryWithLimits.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import trajectory_msgs.msg
import arm_navigation_msgs.msg
import genpy
import std_msgs.msg

class JointTrajectoryWithLimits(genpy.Message):
  _md5sum = "e31e1ba1b3409bbb645c8dfcca5935cd"
  _type = "arm_navigation_msgs/JointTrajectoryWithLimits"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# A trajectory message that encodes joint limits within it.
trajectory_msgs/JointTrajectory trajectory

# A vector of JointLimit messages.
# Each message contains the limits for a specific joint
arm_navigation_msgs/JointLimits[] limits

================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
float64[] positions
float64[] velocities
float64[] accelerations
duration time_from_start
================================================================================
MSG: arm_navigation_msgs/JointLimits
# This message contains information about limits of a particular joint (or control dimension)
string joint_name

# true if the joint has position limits
bool has_position_limits

# min and max position limits
float64 min_position
float64 max_position

# true if joint has velocity limits
bool has_velocity_limits

# max velocity limit
float64 max_velocity
# min_velocity is assumed to be -max_velocity

# true if joint has acceleration limits
bool has_acceleration_limits
# max acceleration limit
float64 max_acceleration
# min_acceleration is assumed to be -max_acceleration

"""
  __slots__ = ['trajectory','limits']
  _slot_types = ['trajectory_msgs/JointTrajectory','arm_navigation_msgs/JointLimits[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       trajectory,limits

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointTrajectoryWithLimits, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.trajectory is None:
        self.trajectory = trajectory_msgs.msg.JointTrajectory()
      if self.limits is None:
        self.limits = []
    else:
      self.trajectory = trajectory_msgs.msg.JointTrajectory()
      self.limits = []

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
      buff.write(_struct_3I.pack(_x.trajectory.header.seq, _x.trajectory.header.stamp.secs, _x.trajectory.header.stamp.nsecs))
      _x = self.trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectory.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.positions))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.velocities))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.accelerations))
        _v1 = val1.time_from_start
        _x = _v1
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
      length = len(self.limits)
      buff.write(_struct_I.pack(length))
      for val1 in self.limits:
        _x = val1.joint_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_B2dBdBd.pack(_x.has_position_limits, _x.min_position, _x.max_position, _x.has_velocity_limits, _x.max_velocity, _x.has_acceleration_limits, _x.max_acceleration))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.trajectory is None:
        self.trajectory = trajectory_msgs.msg.JointTrajectory()
      if self.limits is None:
        self.limits = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.trajectory.header.seq, _x.trajectory.header.stamp.secs, _x.trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = struct.unpack(pattern, str[start:end])
        _v2 = val1.time_from_start
        _x = _v2
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.trajectory.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.limits = []
      for i in range(0, length):
        val1 = arm_navigation_msgs.msg.JointLimits()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.joint_name = str[start:end].decode('utf-8')
        else:
          val1.joint_name = str[start:end]
        _x = val1
        start = end
        end += 35
        (_x.has_position_limits, _x.min_position, _x.max_position, _x.has_velocity_limits, _x.max_velocity, _x.has_acceleration_limits, _x.max_acceleration,) = _struct_B2dBdBd.unpack(str[start:end])
        val1.has_position_limits = bool(val1.has_position_limits)
        val1.has_velocity_limits = bool(val1.has_velocity_limits)
        val1.has_acceleration_limits = bool(val1.has_acceleration_limits)
        self.limits.append(val1)
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
      buff.write(_struct_3I.pack(_x.trajectory.header.seq, _x.trajectory.header.stamp.secs, _x.trajectory.header.stamp.nsecs))
      _x = self.trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectory.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.positions.tostring())
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.velocities.tostring())
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.accelerations.tostring())
        _v3 = val1.time_from_start
        _x = _v3
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
      length = len(self.limits)
      buff.write(_struct_I.pack(length))
      for val1 in self.limits:
        _x = val1.joint_name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_B2dBdBd.pack(_x.has_position_limits, _x.min_position, _x.max_position, _x.has_velocity_limits, _x.max_velocity, _x.has_acceleration_limits, _x.max_acceleration))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.trajectory is None:
        self.trajectory = trajectory_msgs.msg.JointTrajectory()
      if self.limits is None:
        self.limits = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.trajectory.header.seq, _x.trajectory.header.stamp.secs, _x.trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _v4 = val1.time_from_start
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.trajectory.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.limits = []
      for i in range(0, length):
        val1 = arm_navigation_msgs.msg.JointLimits()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.joint_name = str[start:end].decode('utf-8')
        else:
          val1.joint_name = str[start:end]
        _x = val1
        start = end
        end += 35
        (_x.has_position_limits, _x.min_position, _x.max_position, _x.has_velocity_limits, _x.max_velocity, _x.has_acceleration_limits, _x.max_acceleration,) = _struct_B2dBdBd.unpack(str[start:end])
        val1.has_position_limits = bool(val1.has_position_limits)
        val1.has_velocity_limits = bool(val1.has_velocity_limits)
        val1.has_acceleration_limits = bool(val1.has_acceleration_limits)
        self.limits.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_2i = struct.Struct("<2i")
_struct_B2dBdBd = struct.Struct("<B2dBdBd")
