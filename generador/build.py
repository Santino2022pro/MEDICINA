# -*- coding: utf-8 -*-
"""Genera INTEGRACION_METABOLICA_AVANZADA_ANIMADA.pptx"""
import sys, importlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'INTEGRACION_METABOLICA_AVANZADA_ANIMADA.pptx')
MODS = sys.argv[2].split(',') if len(sys.argv) > 2 else ['u0', 'u1', 'u1b', 'u1c', 'u1d', 'u2', 'u2b', 'u3', 'u3b', 'u3c', 'u4', 'u4b', 'u5', 'u6']

D = Deck()
for m in MODS:
    importlib.import_module(m).build(D)
for i, s in enumerate(D.slides):
    if i > 0:
        pagenum(s, i + 1)
D.save(OUT)
print('diapositivas:', len(D.slides), D.stats)
for w in WARN:
    print('AVISO', w)
