# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ebot_docking:srv/DockSw.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DockSw_Request(type):
    """Metaclass of message 'DockSw_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ebot_docking')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ebot_docking.srv.DockSw_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__dock_sw__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__dock_sw__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__dock_sw__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__dock_sw__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__dock_sw__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DockSw_Request(metaclass=Metaclass_DockSw_Request):
    """Message class 'DockSw_Request'."""

    __slots__ = [
        '_linear_dock',
        '_orientation_dock',
        '_distance',
        '_orientation',
        '_rack_no',
    ]

    _fields_and_field_types = {
        'linear_dock': 'boolean',
        'orientation_dock': 'boolean',
        'distance': 'double',
        'orientation': 'double',
        'rack_no': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.linear_dock = kwargs.get('linear_dock', bool())
        self.orientation_dock = kwargs.get('orientation_dock', bool())
        self.distance = kwargs.get('distance', float())
        self.orientation = kwargs.get('orientation', float())
        self.rack_no = kwargs.get('rack_no', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.linear_dock != other.linear_dock:
            return False
        if self.orientation_dock != other.orientation_dock:
            return False
        if self.distance != other.distance:
            return False
        if self.orientation != other.orientation:
            return False
        if self.rack_no != other.rack_no:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def linear_dock(self):
        """Message field 'linear_dock'."""
        return self._linear_dock

    @linear_dock.setter
    def linear_dock(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'linear_dock' field must be of type 'bool'"
        self._linear_dock = value

    @builtins.property
    def orientation_dock(self):
        """Message field 'orientation_dock'."""
        return self._orientation_dock

    @orientation_dock.setter
    def orientation_dock(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'orientation_dock' field must be of type 'bool'"
        self._orientation_dock = value

    @builtins.property
    def distance(self):
        """Message field 'distance'."""
        return self._distance

    @distance.setter
    def distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'distance' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._distance = value

    @builtins.property
    def orientation(self):
        """Message field 'orientation'."""
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'orientation' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'orientation' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._orientation = value

    @builtins.property
    def rack_no(self):
        """Message field 'rack_no'."""
        return self._rack_no

    @rack_no.setter
    def rack_no(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'rack_no' field must be of type 'str'"
        self._rack_no = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockSw_Response(type):
    """Metaclass of message 'DockSw_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ebot_docking')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ebot_docking.srv.DockSw_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__dock_sw__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__dock_sw__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__dock_sw__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__dock_sw__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__dock_sw__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DockSw_Response(metaclass=Metaclass_DockSw_Response):
    """Message class 'DockSw_Response'."""

    __slots__ = [
        '_success',
        '_message',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.message != other.message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value


class Metaclass_DockSw(type):
    """Metaclass of service 'DockSw'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ebot_docking')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ebot_docking.srv.DockSw')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__dock_sw

            from ebot_docking.srv import _dock_sw
            if _dock_sw.Metaclass_DockSw_Request._TYPE_SUPPORT is None:
                _dock_sw.Metaclass_DockSw_Request.__import_type_support__()
            if _dock_sw.Metaclass_DockSw_Response._TYPE_SUPPORT is None:
                _dock_sw.Metaclass_DockSw_Response.__import_type_support__()


class DockSw(metaclass=Metaclass_DockSw):
    from ebot_docking.srv._dock_sw import DockSw_Request as Request
    from ebot_docking.srv._dock_sw import DockSw_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
