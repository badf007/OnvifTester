import rtsp

CAMERA_URI = 'rtsp://192.168.1.14:554'

# single picture
client = rtsp.Client(rtsp_server_uri=CAMERA_URI)
image = client.read()
f = open("pic.png", "w+")
f.write(image)
client.close()

# stream Preview
# with rtsp.Client(CAMERA_URI) as client:
#    client.preview()
