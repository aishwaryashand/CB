#!/usr/bin/python2

import os
import webbrowser
#import camera

#nam=camera.name1()
#os.system(scp -i ../Downloads/warya.pem "subject_id" ubuntu@172.31.46.125)'

# copy image captured to instance
os.system("scp -i /home/adhoc/Downloads/warya.pem /home/adhoc/Desktop/attendance/Gallery/aishwarya.jpg ubuntu@18.222.253.203:/var/www/html/images")



