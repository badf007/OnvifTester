from onvif import ONVIFService
device_service = ONVIFService(
    'http://192.168.0.14', 'admin', '@DIRK#Zu2', 'C:\\Users\\Starlin Cerda\\AppData\\Roaming\\Python\\Python37\\site-packages\\onvif\\wsdl\\')

ret = device_service.GetHostName()
print(ret.FromDHCP)
