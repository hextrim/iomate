import cobbler.api as capi

cobbler_server = capi.BootAPI(is_cobblerd=True)

something = {}
something = cobbler_server.systems().hostname

print something

#system = cobbler_server.new_system()
#system.name = system_name
#cobbler_server.systems().add(system,with_copy=True)
#cobbler_server.add_system(system, save=True)
#os.system("service cobblerd restart")

