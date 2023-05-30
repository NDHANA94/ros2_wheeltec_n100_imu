import numpy as np
class fdilink_header():
    def __init__(self):
        self.header_start:int
        self.data_type:int
        self.data_size:int
        self.serial_num:int
        self.header_crc8:int
        self.header_crc16_h:int
        self.header_crc16_l:int

class IMUData_packet_t():
    def __init__(self):
        self.gyroscope_x:float          # unit: rad/s
        self.gyroscope_y:float          # unit: rad/s
        self.gyroscope_z:float          # unit: rad/s
        self.accelerometer_x:float      # unit: m/s^2
        self.accelerometer_y:float      # unit: m/s^2
        self.accelerometer_z:float      # unit: m/s^2
        self.magnetometer_x:float       # unit: mG
        self.magnetometer_y:float       # unit: mG
        self.magnetometer_z:float       # unit: mG
        self.imu_temperature:float      # unit: C
        self.pressure:float             # unit: Pa
        self.pressure_temperature:float # unit: C
        self.Timestamp:np.int64         # unit: us

class AHRSData_packet_t():
    def __init__(self):
        self.RollSpeed:float            # unit: rad/s
        self.PitchSpeed:float           # unit: rad/s
        self.HeadingSpeed:float         # unit: rad/s
        self.Roll:float                 # unit: rad
        self.Pitch:float                # unit: rad
        self.Heading:float              # unit: rad
        self.Qw:float                   # w
        self.Qx:float                   # x
        self.Qy:float                   # y
        self.Qz:float                   # z
        self.Timestamp:np.int64         # unit: us

class INSGPSData_packet_t():
    def __init__(self):
        self.BodyVelocity_X:float            
        self.BodyVelocity_Y:float
        self.BodyVelocity_Z:float
        self.BodyAcceleration_X:float  
        self.BodyAcceleration_Y:float
        self.BodyAcceleration_Z:float
        self.Location_North:np.double
        self.Location_East:np.double
        self.Location_Down:np.double
        self.Velocity_North:float
        self.Velocity_East:float
        self.Velocity_Down:float
        self.Acceleration_North:float
        self.Acceleration_East:float
        self.Acceleration_Down:float
        self.Pressure_Altitude:float
        self.Timestamp:np.int64



# for IMU =============================================
class IMUData():
    def __init__(self):
        self.data_pack = IMUData_packet_t() # 56
        self.data_buff = [0]*56 # 56

class read_imu_struct():
    def __init__(self):
        self.header = fdilink_header() # 7
        self.data = IMUData()
        self.frame_end:int 
        
class read_imu_tmp():
    def __init__(self):
        self.frame_header = [0]*7
        self.read_msg = [0]*57


class imu_frame_read():
    def __init__(self):
        self.frame = read_imu_struct()
        self.read_buf = read_imu_tmp()
        self.read_temp = [0]*64
#for IMU ---------------------------------------------

# for AHRS ===========================================
class AHRSData():
    def __init__(self):
        self.data_pack = AHRSData_packet_t()
        self.data_buf = [0]*48

class read_ahrs_struct():
    def __init__(self):
        self.header = fdilink_header() # 7
        self.data = AHRSData()
        self.frame_end:int 
        
class read_ahrs_tmp():
    def __init__(self):
        self.frame_header = [0]*7
        self.read_msg = [0]*49


class ahrs_frame_read():
    def __init__(self):
        self.frame = read_ahrs_struct()
        self.read_buf = read_ahrs_tmp()
        self.read_temp = [0]*56
#for AHRS ---------------------------------------------

# for INSGPS ===========================================
class INSGPSData():
    def __init__(self):
        self.data_pack = INSGPSData_packet_t()
        self.data_buf = [0]*84
        
class read_insgps_struct():
    def __init__(self):
        self.header = fdilink_header() # 7
        self.data = INSGPSData()
        self.frame_end:int 
        
class read_insgps_tmp():
    def __init__(self):
        self.frame_header = [0]*7
        self.read_msg = [0]*85


class insgps_frame_read():
    def __init__(self):
        self.frame = read_insgps_struct()
        self.read_buf = read_insgps_tmp()
        self.read_temp = [0]*92
#for INSGPS ---------------------------------------------


