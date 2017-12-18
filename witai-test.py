from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
sys.path.append("pywit/")

import subprocess
import os
from wit import Wit

access_token = '3PJW2EQMNAOULPSYI3EV25IIF5AQUSJS'

def send(request, response):
    print(response['text'])


client = Wit(access_token=access_token)
resp = None
print('nagrywanie rozpoczete')
cmd = 'arecord -q -r 16000 -f S16_LE -c 1 -d 3 tmp/tmp.wav'
subprocess.call(cmd, shell=True)
with open('tmp/tmp.wav', 'rb') as wav:
    resp = client.speech(wav, None, {'Content-Type': 'audio/wav'})
os.remove('tmp/tmp.wav')
print('Yay, got Wit.ai response: ' + str(resp))
