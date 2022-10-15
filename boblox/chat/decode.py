def decode(ip):
    ip = str(ip)
    nip = ''
    for char in ip:
        if char == 'n': nip = nip + '1'
        if char == 'z': nip = nip + '2'
        if char == 'u': nip = nip + '3'
        if char == 'y': nip = nip + '4'
        if char == 'c': nip = nip + '5'
        if char == 'e': nip = nip + '6'
        if char == 'a': nip = nip + '7'
        if char == 'd': nip = nip + '8'
        if char == 'j': nip = nip + '9'
        if char == 'b': nip = nip + '0'
        if char == 'x': nip = nip + '.'
    return nip