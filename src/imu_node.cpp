#include "wheeltecN100_imu/imu_node.hpp"

// #include <serial>


// ImuNode::ImuNode() :frist_sn_(false), serial_timeout_(20), mag_offset_x_(0), mag_offset_y_(0), mag_offset_z_(0), mag_covariance_(0)
// {
  
// }
std::string serial_port;

class ImuNode : public rclcpp::Node
{
public:
  ImuNode() 
  : Node("imu_node")
  {
    this->declare_parameter("serial_port", "/dev/ttyACM0");
    this->declare_parameter("serial_baud", 921600);

    imu_pub_ = this->create_publisher<sensor_msgs::msg::Imu>("imu", 10);
    imu_trueEast_pub_ = this->create_publisher<sensor_msgs::msg::Imu>("imu_trueEast", 10);
    mag_pose_pub_ = this->create_publisher<geometry_msgs::msg::Pose2D>("imu/magnetic_pose_2d", 10);
    mag_pub_ = this->create_publisher<sensor_msgs::msg::MagneticField>("imu/magnetic_field", 10);
    timer_ = this->create_wall_timer(10ms, std::bind(&ImuNode::timer_callback, this));
    serial_port = this->get_parameter("serial_port").as_string();
    // std::vector<rclcpp::Parameter> all_new_parameters{rclcpp::Parameter("serial_port", "/dev/ttyACM0"), rclcpp::Parameter("serial_baud", 921600)};
    std::cout<<serial_port.c_str();
    try
    {
      {
        
      }
    }
    catch(const std::exception& e)
    {
      std::cerr << e.what() << '\n';
    }
    
  }

private:
  
  
  serial::Serial serial_;
  void timer_callback()
  {
    
    printf("hello from imu \n" );
    

  }
  

  rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr imu_pub_;
  rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr imu_trueEast_pub_;
  rclcpp::Publisher<geometry_msgs::msg::Pose2D>::SharedPtr mag_pose_pub_;
  rclcpp::Publisher<sensor_msgs::msg::MagneticField>::SharedPtr mag_pub_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ImuNode>());
  rclcpp::shutdown();
  return 0;
}
