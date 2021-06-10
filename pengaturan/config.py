# base path to YOLO directory
MODEL_PATH = "yolo-coco"

# initialize minimum probability to filter weak detections along with the
# threshold when applying non-maxim suppression
MIN_CONF = 0.3  #letak lebih kecil suapya lebih mudah mendetek org gituh
NMS_THRESH = 0.3 #untuk buat bounding box ketika mendetek orang jadi

# should NVIDIA CUDA GPU be used?
USE_GPU = True

# define the minimum safe distance (in pixels) that two people can be from each other
MIN_DISTANCE = 10
# ini gunakan nilai pixel kerna, kita lihat dari gambar. jadi 
# jadi jarak 2 meter itu kira 50 pixel.jadi jarak antara org itu minimal 2 meter bersamaan 50 pixel


People_Counter = True

Thread = True
# Set the threshold value for total violations limit.
Threshold = 50
# Enter the ip camera url (e.g., url = 'http://191.138.0.100:8040/video');
# Set url = 0 for webcam.
url = '0'
# Turn ON/OFF the email alert feature.
ALERT = False
# Set mail to receive the real-time alerts. E.g., 'xxx@gmail.com'.
MAIL = 'myransr02@gmail.com'
# Set if GPU should be used for computations; Otherwise uses the CPU by default.
USE_GPU = True
# Define the max/min safe distance limits (in pixels) between 2 people.
MAX_DISTANCE = 80
# MIN_DISTANCE = 50
