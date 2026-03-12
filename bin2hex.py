from myhdl import *

@block
def bin2hex(HEX, value):
    """Conversor binário (4 bits) para display de 7 segmentos."""

    @always_comb
    def comb():
        v = int(value)

        if v == 0x0: HEX.next = 0b1000000
        elif v == 0x1: HEX.next = 0b1111001
        elif v == 0x2: HEX.next = 0b0100100
        elif v == 0x3: HEX.next = 0b0110000
        elif v == 0x4: HEX.next = 0b0011001
        elif v == 0x5: HEX.next = 0b0010010
        elif v == 0x6: HEX.next = 0b0000010
        elif v == 0x7: HEX.next = 0b1111000
        elif v == 0x8: HEX.next = 0b0000000
        elif v == 0x9: HEX.next = 0b0010000
        elif v == 0xA: HEX.next = 0b0001000
        elif v == 0xB: HEX.next = 0b0000011
        elif v == 0xC: HEX.next = 0b1000110
        elif v == 0xD: HEX.next = 0b0100001
        elif v == 0xE: HEX.next = 0b0000110
        elif v == 0xF: HEX.next = 0b0001110
        else: HEX.next = 0b1111111

    return instances()