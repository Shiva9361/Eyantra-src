// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ebot_docking:srv/DockSw.idl
// generated code does not contain a copyright notice

#ifndef EBOT_DOCKING__SRV__DETAIL__DOCK_SW__STRUCT_HPP_
#define EBOT_DOCKING__SRV__DETAIL__DOCK_SW__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ebot_docking__srv__DockSw_Request __attribute__((deprecated))
#else
# define DEPRECATED__ebot_docking__srv__DockSw_Request __declspec(deprecated)
#endif

namespace ebot_docking
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct DockSw_Request_
{
  using Type = DockSw_Request_<ContainerAllocator>;

  explicit DockSw_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->linear_dock = false;
      this->orientation_dock = false;
      this->distance = 0.0;
      this->orientation = 0.0;
      this->rack_no = "";
    }
  }

  explicit DockSw_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : rack_no(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->linear_dock = false;
      this->orientation_dock = false;
      this->distance = 0.0;
      this->orientation = 0.0;
      this->rack_no = "";
    }
  }

  // field types and members
  using _linear_dock_type =
    bool;
  _linear_dock_type linear_dock;
  using _orientation_dock_type =
    bool;
  _orientation_dock_type orientation_dock;
  using _distance_type =
    double;
  _distance_type distance;
  using _orientation_type =
    double;
  _orientation_type orientation;
  using _rack_no_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _rack_no_type rack_no;

  // setters for named parameter idiom
  Type & set__linear_dock(
    const bool & _arg)
  {
    this->linear_dock = _arg;
    return *this;
  }
  Type & set__orientation_dock(
    const bool & _arg)
  {
    this->orientation_dock = _arg;
    return *this;
  }
  Type & set__distance(
    const double & _arg)
  {
    this->distance = _arg;
    return *this;
  }
  Type & set__orientation(
    const double & _arg)
  {
    this->orientation = _arg;
    return *this;
  }
  Type & set__rack_no(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->rack_no = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ebot_docking::srv::DockSw_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ebot_docking::srv::DockSw_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ebot_docking::srv::DockSw_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ebot_docking::srv::DockSw_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ebot_docking__srv__DockSw_Request
    std::shared_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ebot_docking__srv__DockSw_Request
    std::shared_ptr<ebot_docking::srv::DockSw_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DockSw_Request_ & other) const
  {
    if (this->linear_dock != other.linear_dock) {
      return false;
    }
    if (this->orientation_dock != other.orientation_dock) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    if (this->orientation != other.orientation) {
      return false;
    }
    if (this->rack_no != other.rack_no) {
      return false;
    }
    return true;
  }
  bool operator!=(const DockSw_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DockSw_Request_

// alias to use template instance with default allocator
using DockSw_Request =
  ebot_docking::srv::DockSw_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ebot_docking


#ifndef _WIN32
# define DEPRECATED__ebot_docking__srv__DockSw_Response __attribute__((deprecated))
#else
# define DEPRECATED__ebot_docking__srv__DockSw_Response __declspec(deprecated)
#endif

namespace ebot_docking
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct DockSw_Response_
{
  using Type = DockSw_Response_<ContainerAllocator>;

  explicit DockSw_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit DockSw_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ebot_docking::srv::DockSw_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ebot_docking::srv::DockSw_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ebot_docking::srv::DockSw_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ebot_docking::srv::DockSw_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ebot_docking__srv__DockSw_Response
    std::shared_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ebot_docking__srv__DockSw_Response
    std::shared_ptr<ebot_docking::srv::DockSw_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DockSw_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const DockSw_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DockSw_Response_

// alias to use template instance with default allocator
using DockSw_Response =
  ebot_docking::srv::DockSw_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ebot_docking

namespace ebot_docking
{

namespace srv
{

struct DockSw
{
  using Request = ebot_docking::srv::DockSw_Request;
  using Response = ebot_docking::srv::DockSw_Response;
};

}  // namespace srv

}  // namespace ebot_docking

#endif  // EBOT_DOCKING__SRV__DETAIL__DOCK_SW__STRUCT_HPP_
