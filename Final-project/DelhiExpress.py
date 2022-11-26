                                                    CODE FOR DELHI EXPRESS


import wiotp.sdk.device
import time
import random
myConfig = {
"identity" :{
"orgId":"njd5v1",
"typeId":"nodeMCU",
"deviceId":"Delhi_Express"
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
 myData = {'name':'Delhi Express','lat':13.344279,'lon':80.214367}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':13.515254,'lon':80.093518}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':13.728799,'lon':80.005627}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':13.910160,'lon':79.906750}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':14.102035,'lon':79.851819}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':14.261807,'lon':79.862805}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':14.623537,'lon':79.950695}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':15.111987,'lon':79.994641}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':15.313413,'lon':80.005627}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':15.567568,'lon':80.104504}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':15.747405,'lon':80.269299}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':15.821409,'lon':80.302258}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':15.927082,'lon':80.445080}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':16.022141,'lon':80.554943}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':17.033801,'lon':80.295512}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':18.383088,'lon':18.383088}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':19.074762,'lon':79.487698}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':20.179065,'lon':79.001439}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':21.306421,'lon':78.789356}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':22.518024,'lon':77.829404}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':23.264139,'lon':77.429333}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':24.509723,'lon':78.330212}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':25.668840,'lon':78.451062}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':26.177704,'lon':78.170910}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':27.505914,'lon':77.676526}
 pub(myData)
 time.sleep(3)
 myData = {'name':'Delhi Express','lat':28.302041,'lon':77.308484}
 pub(myData)
 time.sleep(3)
 client.commandCallback = myCommandCallback
client.disconnect




 
