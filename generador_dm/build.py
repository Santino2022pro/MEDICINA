# -*- coding: utf-8 -*-
"""Genera DIABETES_OBESIDAD_TEJIDO_ADIPOSO_INTEGRACION_METABOLICA.pptx"""
import sys, importlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                                         'DIABETES_OBESIDAD_TEJIDO_ADIPOSO_INTEGRACION_METABOLICA.pptx')
MODS = sys.argv[2].split(',') if len(sys.argv) > 2 else ['u0', 'u1a', 'u1b', 'u1c', 'u1d', 'u2a', 'u2b', 'u3', 'u4', 'u5a', 'u5b',
                                                         'u6', 'u7', 'u8', 'u9', 'u10', 'u11']

D = Deck()
for m in MODS:
    importlib.import_module(m).build(D)
for i, s in enumerate(D.slides):
    if i > 0:
        pnum(s, i + 1)
D.save(OUT)
print('diapositivas:', len(D.slides), D.stats)
for w in WARN:
    print('AVISO', w)
