x = 'macos'

with open('fetchml/fetchml', 'r') as file:
    filedata = file.read()
    filedata = filedata.replace('$os', '{}').format(x)
with open('fetchml/fetchml', 'w') as file:
    file.write(filedata)
