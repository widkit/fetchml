os = ''
host = ''
kernel = ''
uptime = ''
packages = ''
shell = ''
resolution = ''
terminal = ''
cpu = ''
gpu = ''
memory = ''
desktop_enviroment = ''
window_manager = ''
wmtheme = ''

# Reading the file
with open('index.html', 'r') as file:
    filedata = file.read()

    # Doing the replacements of variables
    filedata = filedata.replace('$os', '{}').format(os)
    filedata = filedata.replace('$host', '{}').format(host)
    filedata = filedata.replace('$kernel', '{}').format(kernel)
    filedata = filedata.replace('$uptime', '{}').format(uptime)
    filedata = filedata.replace('$packages', '{}').format(packages)
    filedata = filedata.replace('$shell', '{}').format(shell)
    filedata = filedata.replace('$resolution', '{}').format(resolution)
    filedata = filedata.replace(
        '$desktop_enviroment', '{}').format(desktop_enviroment)
    filedata = filedata.replace('$window_manager', '{}').format(window_manager)
    filedata = filedata.replace(
        '$wmtheme', '{}').format(wmtheme)
    filedata = filedata.replace('$terminal', '{}').format(terminal)
    filedata = filedata.replace('$cpu', '{}').format(cpu)
    filedata = filedata.replace('$gpu', '{}').format(gpu)
    filedata = filedata.replace('$memory', '{}').format(memory)

    # Writing changes to new file
    with open('render.html', 'w') as file:
        file.write(filedata)
