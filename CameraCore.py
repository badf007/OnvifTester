from onvif import ONVIFCamera
import json


CONFIG_TOKEN = 'video_encoder_config'
VIDEO_SOURCE_TOKEN = 'video_source'
VIDEO_SOURCE_CONFIG_TOKEN = 'video_source_config1'
VIDEO_SOURCE_MODE_TOKEN = '1'  # aparentemente son numericos consecutivos
VIDEO_PROFILE_TOKEN = 'media_profile1'
REQUEST_VIDEO = '{"StreamSetup": {"Stream": "RTP-Multicast","Transport": {"Protocol": "RTSP","Tunnel": {"Protocol": "RTSP"} } },"ProfileToken": "media_profile1"}'
FINAL_REQUEST = json.loads(REQUEST_VIDEO)

mycam = ONVIFCamera('192.168.1.14', 80, 'admin', '@DIRK#Zu2')
mycam.devicemgmt.GetServices(False)
media_service = mycam.create_media_service()
devicemgnmt_service = mycam.create_devicemgmt_service()
#receiver_service = mycam.create_receiver_service()

# Capabs = media_service.GetServiceCapabilities()  # Valido, posiblemente funcional
#Profiles = media_service.GetProfiles()
#Profile = media_service.GetProfile(VIDEO_PROFILE_TOKEN)
# PicURL = media_service.GetSnapshotUri(VIDEO_PROFILE_TOKEN)  # comando no soportado
# StreamURL = media_service.GetStreamUri(FINAL_REQUEST)
# VideoEncoderConfigs = media_service.GetVideoEncoderConfigurations() #Valido y funcional
# VideoSourceConfigs = media_service.GetVideoSourceConfigurations()  # Valido y funcional
# VideoSources = media_service.GetVideoSources()  # Valido y funcional
ServiceCapbs = media_service.GetServiceCapabilities()  # Valido y funcional
# VideoSourceModes = media_service.GetVideoSourceModes(VIDEO_SOURCE_TOKEN)  # Valido y funcional


# Valido y NOfuncional
# VideoAnalyticsConfigs = media_service.GetVideoAnalyticsConfigurations()

print(ServiceCapbs)

'''
for configs in VideoEncoderConfigs:
    print(configs.Name)
'''
