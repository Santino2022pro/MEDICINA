# -*- coding: utf-8 -*-
"""Genera ENFERMEDADES_PLEURALES_ANIMADA.pptx y los entregables en Markdown."""
import sys, importlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *
import fondos

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'ENFERMEDADES_PLEURALES_ANIMADA.pptx')
MODS = sys.argv[2].split(',') if len(sys.argv) > 2 else ['u01', 'u02', 'u03', 'u04', 'u05', 'u06', 'u07', 'u08', 'u09']

if not all(os.path.exists(p) for p in BG.values()):
    fondos.make()
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
if len(sys.argv) <= 2:
    import entregables
    entregables.write(D, os.path.join(HERE, '..'))
