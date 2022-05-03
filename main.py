#!/usr/bin/env python3
import imgkit
import os
import json

# Generating input from Neofetch and opening it as dict.
os.system('neofetch --json > neofetch_output.json')
neofetch_output = json.load(open('neofetch_output.json'))

# Assigning command outputs as variables to display in HTML file
nf_os = neofetch_output['OS']
nf_host = neofetch_output['Host']
nf_kernel = neofetch_output['Kernel']
nf_uptime = neofetch_output['Uptime']
nf_packages = neofetch_output['Packages']
nf_shell = neofetch_output['Shell']
nf_resolution = neofetch_output['Resolution']
nf_desktop = neofetch_output['DE']
nf_window = neofetch_output['WM']
nf_window_theme = neofetch_output['WM Theme']
nf_terminal = neofetch_output['Terminal']
nf_cpu = neofetch_output['CPU']
nf_gpu = neofetch_output['GPU']
nf_memory = neofetch_output['Memory']

# Reading the file
with open('index.html', 'r') as file:
    filedata = file.read()

    # Doing the replacements of variables
    filedata = filedata.replace('$os', nf_os)
    filedata = filedata.replace('$host', nf_host)
    filedata = filedata.replace('$kernel', nf_kernel)
    filedata = filedata.replace('$uptime', nf_uptime)
    filedata = filedata.replace('$packages', nf_packages)
    filedata = filedata.replace('$shell', nf_shell)
    filedata = filedata.replace('$resolution', nf_resolution)
    filedata = filedata.replace(
        '$desktop_enviroment', nf_desktop)
    filedata = filedata.replace('$window_manager', nf_window)
    filedata = filedata.replace(
        '$wmtheme', nf_window_theme)
    filedata = filedata.replace('$terminal', nf_terminal)
    filedata = filedata.replace('$cpu', nf_cpu)
    filedata = filedata.replace('$gpu', nf_gpu)
    filedata = filedata.replace('$memory', nf_memory)

    # Writing changes to new file
    with open('render.html', 'w') as file:
        file.write(filedata)
# Using IMGKIT to render the render.html and outputting as result.png
imgkit.from_file('render.html', 'result.png')

# Using feh to display the output image
os.system("echo Viewing")
os.system("feh result.png")

# Function to remove Junk files. Reason behind I wrote
# this as function is being able to disable it easier.
def remove_junk():
    remove_junk = input('You want to remove junk files? (y/n): ')
    if remove_junk == 'y':
        os.remove("result.png")
        os.remove("render.html")
        os.remove("neofetch_output.json")
    elif remove_junk == 'n':
        quit()
    else:
        print('Invalid input. Try again.')
        remove_junk()


remove_junk()
