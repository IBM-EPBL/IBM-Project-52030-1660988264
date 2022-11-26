                                  CODE FOR GOA EXPRESS

import wiotp.sdk.device
import time
import random
myConfig = {
"identity" :{
"orgId":"njd5v1",
"typeId":"nodeMCU",
"deviceId":"Goa_Express"
},
"auth":{
"token":"Prems1428"
}
}
def myCommandCallback(cmd):
  print("Message received fromIBM IoT Platform: %s" % cmd.data['command'])
  m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
def pub(data):
  client.publishEvent(eventId = "status", msgFormat="json", data=myData, qos=0, onPublish=None)
  print("Published data Successfully: %s",myData)

while True:
    myData = {'name':'Goa Express','lat':11.688572, 'lon':78.098877}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':11.711433, 'lon':78.076905}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':11.978226, 'lon':78.116730}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':12.085676, 'lon': 78.119477}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':12.402400, 'lon':78.023347}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':12.884795, 'lon':77.707490}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':13.018630,'lon':77.614106}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':13.334194, 'lon':77.086762}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':13.299448, 'lon':76.858796}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':13.344884,'lon': 76.205109}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':13.619985, 'lon':75.966157}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':13.974739, 'lon':76.119965}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':14.423398, 'lon':75.949677}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':14.922914, 'lon':75.389374}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.119216, 'lon':75.389374}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.449980, 'lon':74.406230}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.352006,'lon':74.307353}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.314922, 'lon':74.218089}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.283131, 'lon':74.146678}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.276839, 'lon':74.129855}
    pub(myData)
    time.sleep(3)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.282800, 'lon':74.125392}
    pub(myData)
    time.sleep(3)
    time.sleep(3)
    myData = {'name':'Goa Express','lat':15.296378,'lon':74.135692}
    pub(myData)
    time.sleep(3)
    client.commandCallback = myCommandCallback
client.disconnect()
