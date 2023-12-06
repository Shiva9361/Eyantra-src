// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ebot_docking:srv/DockSw.idl
// generated code does not contain a copyright notice

#ifndef EBOT_DOCKING__SRV__DETAIL__DOCK_SW__STRUCT_H_
#define EBOT_DOCKING__SRV__DETAIL__DOCK_SW__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'rack_no'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/DockSw in the package ebot_docking.
typedef struct ebot_docking__srv__DockSw_Request
{
  bool linear_dock;
  bool orientation_dock;
  double distance;
  double orientation;
  rosidl_runtime_c__String rack_no;
} ebot_docking__srv__DockSw_Request;

// Struct for a sequence of ebot_docking__srv__DockSw_Request.
typedef struct ebot_docking__srv__DockSw_Request__Sequence
{
  ebot_docking__srv__DockSw_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ebot_docking__srv__DockSw_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/DockSw in the package ebot_docking.
typedef struct ebot_docking__srv__DockSw_Response
{
  /// indicate successful run of triggered service
  bool success;
  /// informational, e.g. for error messages
  rosidl_runtime_c__String message;
} ebot_docking__srv__DockSw_Response;

// Struct for a sequence of ebot_docking__srv__DockSw_Response.
typedef struct ebot_docking__srv__DockSw_Response__Sequence
{
  ebot_docking__srv__DockSw_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ebot_docking__srv__DockSw_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // EBOT_DOCKING__SRV__DETAIL__DOCK_SW__STRUCT_H_
