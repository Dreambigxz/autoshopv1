import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllibinsecure = requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
