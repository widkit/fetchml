os = 'macos'

# Reading the file
with open('index.html', 'r') as file:
    filedata = file.read()

    # Doing the replacements of variables
    filedata = filedata.replace('$os', '{}').format(os)

# Writing changes to new file
with open('render.html', 'w') as file:
    file.write(filedata)
