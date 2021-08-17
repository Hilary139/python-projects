# set reminder with python

import time
print('What shall i remind you about?')

text = str(input())

print('in how many minutes?')
local_time = float(input())
local_time = local_time * 60

time.sleep(local_time)

print(text)
