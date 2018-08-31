#!/usr/bin/python
import cobbler.api as capi
api_handle = capi.BootAPI()
matches = api_handle.find_system(name="ht-esxi-test",return_list=False)
print matches
