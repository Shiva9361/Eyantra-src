// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ebot_docking:srv/DockSw.idl
// generated code does not contain a copyright notice

#ifndef EBOT_DOCKING__SRV__DETAIL__DOCK_SW__BUILDER_HPP_
#define EBOT_DOCKING__SRV__DETAIL__DOCK_SW__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ebot_docking/srv/detail/dock_sw__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ebot_docking
{

namespace srv
{

namespace builder
{

class Init_DockSw_Request_rack_no
{
public:
  explicit Init_DockSw_Request_rack_no(::ebot_docking::srv::DockSw_Request & msg)
  : msg_(msg)
  {}
  ::ebot_docking::srv::DockSw_Request rack_no(::ebot_docking::srv::DockSw_Request::_rack_no_type arg)
  {
    msg_.rack_no = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Request msg_;
};

class Init_DockSw_Request_orientation
{
public:
  explicit Init_DockSw_Request_orientation(::ebot_docking::srv::DockSw_Request & msg)
  : msg_(msg)
  {}
  Init_DockSw_Request_rack_no orientation(::ebot_docking::srv::DockSw_Request::_orientation_type arg)
  {
    msg_.orientation = std::move(arg);
    return Init_DockSw_Request_rack_no(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Request msg_;
};

class Init_DockSw_Request_distance
{
public:
  explicit Init_DockSw_Request_distance(::ebot_docking::srv::DockSw_Request & msg)
  : msg_(msg)
  {}
  Init_DockSw_Request_orientation distance(::ebot_docking::srv::DockSw_Request::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_DockSw_Request_orientation(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Request msg_;
};

class Init_DockSw_Request_orientation_dock
{
public:
  explicit Init_DockSw_Request_orientation_dock(::ebot_docking::srv::DockSw_Request & msg)
  : msg_(msg)
  {}
  Init_DockSw_Request_distance orientation_dock(::ebot_docking::srv::DockSw_Request::_orientation_dock_type arg)
  {
    msg_.orientation_dock = std::move(arg);
    return Init_DockSw_Request_distance(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Request msg_;
};

class Init_DockSw_Request_linear_dock
{
public:
  Init_DockSw_Request_linear_dock()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DockSw_Request_orientation_dock linear_dock(::ebot_docking::srv::DockSw_Request::_linear_dock_type arg)
  {
    msg_.linear_dock = std::move(arg);
    return Init_DockSw_Request_orientation_dock(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ebot_docking::srv::DockSw_Request>()
{
  return ebot_docking::srv::builder::Init_DockSw_Request_linear_dock();
}

}  // namespace ebot_docking


namespace ebot_docking
{

namespace srv
{

namespace builder
{

class Init_DockSw_Response_message
{
public:
  explicit Init_DockSw_Response_message(::ebot_docking::srv::DockSw_Response & msg)
  : msg_(msg)
  {}
  ::ebot_docking::srv::DockSw_Response message(::ebot_docking::srv::DockSw_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Response msg_;
};

class Init_DockSw_Response_success
{
public:
  Init_DockSw_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DockSw_Response_message success(::ebot_docking::srv::DockSw_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_DockSw_Response_message(msg_);
  }

private:
  ::ebot_docking::srv::DockSw_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ebot_docking::srv::DockSw_Response>()
{
  return ebot_docking::srv::builder::Init_DockSw_Response_success();
}

}  // namespace ebot_docking

#endif  // EBOT_DOCKING__SRV__DETAIL__DOCK_SW__BUILDER_HPP_
