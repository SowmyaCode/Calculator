import requests
from requests_ntlm import HttpNtlmAuth

username = '\\'
password = ''
tfsApi = 'https://tfsemea1.ta.philips.com/tfs/TPC_Region22/IGT/_git/WF-CMP-SystemHandling?path=%2Flib%2Fpackages.config'

response = requests.get(tfsApi,auth=HttpNtlmAuth(username,password))
if(tfsResponse.ok):
    tfsResponse = tfsResponse.json()
    print(tfsResponse)
else:
    tfsResponse.raise_for_status()