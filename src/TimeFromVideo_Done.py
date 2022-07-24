import pytz
from win32com.propsys import propsys, pscon
import os
from datetime import datetime

properties = propsys.SHGetPropertyStoreFromParsingName('3-1.MOV')
dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()

if not isinstance(dt, datetime):
    dt = datetime.datetime.fromtimestamp(int(dt))
    dt = dt.replace(tzinfo=pytz.timezone('UTC'))

dt_thai = dt.astimezone(pytz.timezone('Asia/Bangkok'))
print('\n',type(dt_thai),dt_thai)
print(dt_thai.strftime("%X"))

created= os.stat('3-1.MOV').st_ctime
print(datetime.fromtimestamp(created))


import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime('3-1.MOV')))
print("created: %s" % time.ctime(os.path.getctime('3-1.MOV')))

