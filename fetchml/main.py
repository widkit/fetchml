#!/usr/bin/env python3
import imgkit
import os
import sys
###


###PYFETCH CODE


###

### DISTRO ###


def distro():
    try:
        with open('/etc/os-release') as f:
            for line in f:
                if 'PRETTY_NAME' in line:
                    return line.split('=')[1].translate(str.maketrans('', '', '"'))
    except FileNotFoundError:
        return 'Unknown'

### MEMORY ###


def mem():
    # Formula: usedmem = MemTotal + Shmem - MemFree - Buffers - Cached - SReclaimable
    # Source: https://github.com/KittyKatt/screenFetch/issues/386#issuecomment-249312716
    try:
        with open('/proc/meminfo') as f:
            current_mem = f.read().strip().split('\n')

        mem_total = int(
            [i for i in current_mem if 'MemTotal' in i][0].split()[1])
        mem_shared = int(
            [i for i in current_mem if 'Shmem' in i][0].split()[1])
        mem_free = int(
            [i for i in current_mem if 'MemFree' in i][0].split()[1])
        mem_buffers = int(
            [i for i in current_mem if 'Buffers' in i][0].split()[1])
        mem_cached = int(
            [i for i in current_mem if 'Cached' in i][0].split()[1])
        mem_sreclaimable = int(
            [i for i in current_mem if 'SReclaimable' in i][0].split()[1])

        return {
            'used_mem': mem_total
            + mem_shared
            - mem_free
            - mem_buffers
            - mem_cached
            - mem_sreclaimable,
            'total_mem': mem_total
        }

    except FileNotFoundError:
        return {
            'used_mem': 0,
            'total_mem': 0
        }

### CPU ###


def cpu():
    try:
        with open('/proc/cpuinfo') as f:
            current_cpu = f.read().strip().split('\n')

            cpu_model = [i for i in current_cpu if 'model name' in i][0].split(':')[
                                                                               1].strip()
            # cpu_cores = [i for i in current_cpu if 'cpu cores' in i][0].split(':')[1].strip()
            # cpu_siblings = [i for i in current_cpu if 'siblings' in i][0].split(':')[1].strip()
            # flags = [i for i in current_cpu if 'flags' in i][0].split(':')[1].strip().split(' ')

            return {
                'model': cpu_model,
                # 'cores': cpu_cores,
                # 'threads': cpu_siblings,
                # 'flags': flags
            }
    except FileNotFoundError:
        return {
            'model': 'Unknown',
            # 'cores': 0,
            # 'threads': 0,
            # 'flags': []
        }

### KERNEL ###


def kernel():
    try:
        with open('/proc/version') as f:
            return f.read().split()[2]
    except FileNotFoundError:
        return 'Unknown'

### WEATHER ###
# def weather():
#     return os.popen('curl -s wttr.in/?format="%c%C%20%t"').read()

### POWER CONSUMPTION ###
# def power():
    # only works on battery power
    # try:
    #     with open('/sys/class/power_supply/BAT0/power_now') as f:
    #         return int(f.read().strip()) / 1000000
    # except:
    #     return 'N/A'


### SHELL ###
try:
    shell = os.environ['SHELL']
except KeyError:
    shell = 'Unknown'

### WM/DE ###
try:
    wm = os.environ['XDG_CURRENT_DESKTOP']
except KeyError:
    wm = 'Unknown'

### HOSTNAME AND USER ###
try:
    with open('/etc/hostname') as f:
        hostname = f.read().strip()
    user = os.environ['USER']
except (FileNotFoundError, KeyError):
    hostname = 'Unknown'
    user = 'Unknown'
### VARS FOR MEM ###
x = mem()
total_mem = round(x['total_mem'] / 1024)
used_mem = round(x['used_mem'] / 1024)
free_mem = total_mem - used_mem

### VARS FOR CPU ###
y = cpu()
cpu_model = y['model']
# cpu_cores = y['cores']
# cpu_threads = y['threads']
# cpu_flags = y['flags']

### OUTPUT STRING ###
fetch = f""{user}@{hostname}{distro().strip()}{cpu_model}{wm}{kernel()}{shell}{used_mem}MB / {total_mem}MB{reset}
"""

print(fetch)

###

### END OF PYFETCH

###


# Assigning command outputs as variables to display in HTML file
system = ''
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
    filedata = filedata.replace('$os', '{}').format(system)
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
# Using IMGKIT to render the render.html and outputting as result.png
imgkit.from_file('render.html', 'result.png')
# Using feh to display the output image
os.system("feh result.png")
