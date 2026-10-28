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


def qa(fn):
    """controles que LibreOffice no detecta visualmente (PowerPoint sí aplica estos valores)"""
    import zipfile, re
    z = zipfile.ZipFile(fn)
    errs = []
    for n in z.namelist():
        if not re.match(r'ppt/slides/slide\d+\.xml$', n):
            continue
        x = z.read(n).decode('utf8')
        if '<a:spcPct' in x:
            errs.append('%s: interlineado proporcional (spcPct) presente' % n)
        for v in re.findall(r'<a:lnSpc><a:spcPts val="(\d+)"', x):
            if not 600 <= int(v) <= 8000:
                errs.append('%s: interlineado fuera de rango (%s)' % (n, v))
        for v in re.findall(r' sz="(\d+)"', x):
            if not 800 <= int(v) <= 6000:
                errs.append('%s: tamaño de letra fuera de rango (%s)' % (n, v))
        if '<a:t>' in x and '<a:lnSpc>' not in x:
            errs.append('%s: texto sin interlineado exacto' % n)
    f = z.read('ppt/fonts/font1.fntdata')
    if int.from_bytes(f[8:12], 'little') != 0x00020001 or int.from_bytes(f[34:36], 'little') != 0x504C:
        errs.append('fuente incrustada no es EOT válido')
    over = [w for w in WARN if w.startswith(('DESBORDE', 'PALABRA ANCHA', 'TABLA'))]
    print('QA: %d errores de XML · %d desbordes de texto' % (len(errs), len(over)))
    for e in errs[:20]:
        print('  ERROR', e)
    if errs or over:
        raise SystemExit('QA fallido')


qa(OUT)
if len(sys.argv) <= 2:
    import entregables
    entregables.write(D, os.path.join(HERE, '..'))
