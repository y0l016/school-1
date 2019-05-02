def hex2rgb(hex):
    """ convert hex to rgb list """
    # peculiar case for this program
    if hex is None:
        return None

    if '#' in hex:
        hex = hex[1:]

    r = hex[0:2]
    g = hex[2:4]
    b = hex[4:]

    rgb = [int(r, 16), int(g, 16), int(b, 16)]

    return [float(i)/255 for i in rgb]
