import requests, json
from datetime import timedelta
import requests

def push_to_ifttt(ifttt_name, api_key, notification):
	requests.post(url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(ifttt_name, api_key), data = {'value1':notification})

# Netatmo vSmart authentication
url = 'https://app.netatmo.net/oauth2/token'
messageBody = {
            	"app_version": '1.0.0.22',
            	"grant_type": 'password',
            	"client_id": 'na_client_android_vaillant',
            	"client_secret": '929a9f6253babbee1a6e8d4bd51745f0',
            	"username": 'my@mail.com',
            	"password": 'mypassword',
            	"user_prefix": 'vaillant',
              }

apiResponse = requests.post(url, data = messageBody)
if not apiResponse.ok:
	print('Netatmo Connect oauth2 API returned: %s' % (apiResponse.status_code))
	exit(1)

vSmart = json.loads(apiResponse.text)
accessToken = vSmart["access_token"]
#refreshToken = vSmart["refresh_token"]
#expiresIn = vSmart["expires_in"]
#print('refresh_token: %s' % (refreshToken))
#print('expires_in: %s' % (timedelta(seconds=expiresIn)))
print('access_token: %s' % (accessToken))

# Netatmo vSmart get data
url= 'https://app.netatmo.net/api/getthermostatsdata'
messageBody = {
            	"app_version": '1.0.0.22',
            	"sync_device_id": 'all',
            	"device_type": 'NAVaillant',
            	"access_token": accessToken,
              }
              
apiResponse = requests.post(url, data = messageBody)
if not apiResponse.ok:
	print('Netatmo Connect getthermostatsdata API returned: %s' % (apiResponse.status_code))
	exit(1)

vSmart = json.loads(apiResponse.text)
rawData = vSmart["body"]
devList = rawData["devices"]
deviceId = devList[0]["_id"]
moduleList = devList[0]["modules"]
moduleId = moduleList[0]["_id"]

print('device_id: %s' % (deviceId))
print('module_id: %s' % (moduleId))

# Netatmo vSmart disable manual mode
url= 'https://app.netatmo.net/api/setminormode'
messageBody = {
            	"app_version": '1.0.0.22',
            	"access_token": accessToken,
            	"device_id" : deviceId,
            	"module_id" : moduleId, 
            	"setpoint_mode" : 'manual', 
            	"activate" : 'false',
                }
              
apiResponse = requests.post(url, data = messageBody)
if not apiResponse.ok:
	print('Netatmo Connect setminormode API returned: %s' % (apiResponse.status_code))
	print('vSmart disable manual mode disable: fail')
	push_to_ifttt("GFevent", "dg_jwCBCwT0ENLlpJhATiqKuopQFH1FAFZTHdA0Ub2R", "vSmart: Fail")
	exit(1)
else: 
	print('vSmart disable manual mode: success')
	push_to_ifttt("GFevent", "dg_jwCBCwT0ENLlpJhATiqKuopQFH1FAFZTHdA0Ub2R", "vSmart: Success")
	exit(0)
