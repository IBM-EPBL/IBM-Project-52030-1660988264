                                              CODE FOR MYSURU EXPRESS

import wiotp.sdk.device
import time
import random
myConfig = {
"identity" :{
"orgId":"njd5v1",
"typeId":"nodeMCU",
"deviceId":"Mysuru_Express"
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
    myData = {'name':'Mysuru SF Express','lat':11.024938,'lon':76.982315}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':11.220325,'lon':77.570083}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':11.564960,'lon':77.993057}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':11.780142,'lon':78.037002}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.134824,'lon':78.130386}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.226105,'lon':78.091934}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.344187,'lon':78.037002}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.489034,'lon':78.009536}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.655239,'lon':77.866714}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.735622,'lon':77.756851}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.907020,'lon':77.696426}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.987323,'lon':77.646988}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.955205,'lon':77.509659}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.665958,'lon':77.136123}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.548022,'lon':76.921890}
    pub(myData)
    time.sleep(3)
    myData = {'name':'Mysuru SF Express','lat':12.336809,'lon':76.644485}
    pub(myData)
    time.sleep(3)
    client.commandCallback = myCommandCallback
client.disconnect()
