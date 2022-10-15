def encrypt(ip):
    ip = str(ip)
    nip = ''
    for char in ip:
        if char == '1': nip = nip + 'n'
        if char == '2': nip = nip + 'z'
        if char == '3': nip = nip + 'u'
        if char == '4': nip = nip + 'y'
        if char == '5': nip = nip + 'c'
        if char == '6': nip = nip + 'e'
        if char == '7': nip = nip + 'a'
        if char == '8': nip = nip + 'd'
        if char == '9': nip = nip + 'j'
        if char == '0': nip = nip + 'b'
        if char == '.': nip = nip + 'x'
    return nip