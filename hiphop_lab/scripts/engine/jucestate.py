"""Read/write JUCE VST3 plugin state (MemoryBlock base64) so factory patches (.fxp) can be loaded headless via pedalboard."""
import re
TABLE = ".ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+"
IDX = {c: i for i, c in enumerate(TABLE)}


def juce_b64_decode(s):
    size, data = s.split('.', 1)
    size = int(size); out = bytearray(size); pos = 0
    for ch in data:
        v = IDX[ch]
        for b in range(6):
            if v >> b & 1:
                bit = pos + b
                if bit // 8 < size: out[bit // 8] |= 1 << (bit % 8)
        pos += 6
    return bytes(out)


def juce_b64_encode(b):
    nbits = len(b) * 8; chars = []
    for pos in range(0, nbits, 6):
        v = 0
        for k in range(6):
            bit = pos + k
            if bit < nbits and b[bit // 8] >> (bit % 8) & 1: v |= 1 << k
        chars.append(TABLE[v])
    return f"{len(b)}." + ''.join(chars)


def get_component(raw_state):
    xml = raw_state[8:].decode('utf-8', 'ignore') if raw_state[:4] == b'VC2!' else raw_state.decode('utf-8', 'ignore')
    m = re.search(r'<IComponent>([^<]+)</IComponent>', xml)
    return juce_b64_decode(m.group(1).strip())


def set_component(raw_state, comp_bytes):
    head = raw_state[:8]
    xml = raw_state[8:].decode('utf-8', 'ignore')
    xml = re.sub(r'<IComponent>[^<]+</IComponent>', '<IComponent>' + juce_b64_encode(comp_bytes) + '</IComponent>', xml)
    body = xml.encode('utf-8').rstrip(b'\x00')
    # VC2! header: magic + little-endian uint32 length of the xml payload (payload is NUL-terminated)
    import struct
    return b'VC2!' + struct.pack('<I', len(body)) + body + b'\x00'


def load_fxp_into(plugin, fxp_path):
    data = open(fxp_path, 'rb').read()
    i = data.find(b'sub3')
    plugin.raw_state = set_component(plugin.raw_state, data[i:])
    return plugin
