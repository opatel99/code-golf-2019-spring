import zlib
print((str(zlib.decompress(b'x\x9c\xe3R \x11h\xc1\x00\x17\x88I\xaan\x98\x11\\0\x93H\xd4\x08\xd7\x8cp\t1\xd6A\xd5\xc1\xb5"\tc1\x05\x8b\x04\x8aNL\xdd\xe8\x00I\x1d\x9a>\x1c\xda\xb9\xb8\x00\xbeF4\xed'),'utf-8')*3).rstrip()[1:])