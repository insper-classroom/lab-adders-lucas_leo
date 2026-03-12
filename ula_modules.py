#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blocos combinacionais de somadores em MyHDL.

Este modulo declara implementacoes de:
- meio somador (half adder),
- somador completo (full adder),
- somador de 2 bits,
- somador generico por encadeamento,
- somador vetorial comportamental.
"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    """Meio somador de 1 bit.

    Args:
        a: Entrada de 1 bit.
        b: Entrada de 1 bit.
        soma: Saida de soma.
        carry: Saida de carry.
    """
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):

    s = [Signal(bool(0)) for _ in range(3)]
    # s[0] = soma intermediaria
    # s[1] = carry do primeiro HA
    # s[2] = carry do segundo HA

    half_1 = halfAdder(a, b, s[0], s[1])
    half_2 = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


@block
def adder2bits(x, y, soma, vaiUm):

    c0 = Signal(bool(0))

    # bit menos significativo
    ha0 = halfAdder(x[0], y[0], soma[0], c0)

    # bit mais significativo
    fa1 = fullAdder(x[1], y[1], c0, soma[1], vaiUm)

    return instances()

@block
def adder(x, y, soma, carry):

    n = len(x)

    faList = [None for _ in range(n)]
    c = [Signal(bool(0)) for _ in range(n)]

    for i in range(n):
        if i == 0:
            faList[i] = fullAdder(x[i], y[i], False, soma[i], c[i])
        else:
            faList[i] = fullAdder(x[i], y[i], c[i-1], soma[i], c[i])

    @always_comb
    def comb():
        carry.next = c[n-1]

    return instances()

@block
def addervb(x, y, soma, carry):

    @always_comb
    def comb():
        result = int(x) + int(y)
        soma.next = result % (2 ** len(x))
        carry.next = result >> len(x)

    return instances()