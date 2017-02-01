import ctypes

#~ Constantes de la API de Windows.
STD_OUTPUT_HANDLE = -11

color = 0x000F # Color Blanco Brillante.

#~ Método que reinicia al color original
def get_csbi_attributes(handle):
    #~ Basado en winconsole.py de IPython
    
    import struct
    
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr

#~ Métodos en variables que simplifican el nombre.
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)


