__version__ = '0.2.5'
import struct
import binascii


num_bytes = 16


def save(uuid, vector: list, geo: list, filename='data.bin'):
    f = open(filename, 'ab')
    f.write(struct.pack('B'*num_bytes, *uuid))
    data = [struct.pack('d', f) for f in vector]
    [f.write(d) for d in data]
    [f.write(d) for d in [struct.pack('d', f) for f in geo]]
    f.close()


def read_all(filename='data.bin'):
    f = open(filename, 'rb')
    output = []
    Is = 'B'*num_bytes
    Fs = 'f'*512
    vec_len = 512*4
    while True:
        try:
            tmp = [binascii.hexlify(bytearray(struct.unpack(Is, f.read(16)))),
                   struct.unpack(Fs, f.read(vec_len))]
            output.append(tmp)
        except:
            break
    f.close()
    return output


def save_all(list_of_lists, filename='data.bin'):
    open(filename, 'w').write('')
    for item in list_of_lists:
        save(item[0], item[1], filename)
