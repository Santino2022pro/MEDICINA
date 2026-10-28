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


def text_collisions(z):
    """recuadros de texto que se superponen entre sí (incluidos título e indicador de paso)"""
    import re
    from lxml import etree
    ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
          'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
    out = []
    for n in z.namelist():
        if not re.match(r'ppt/slides/slide\d+\.xml$', n):
            continue
        x = etree.fromstring(z.read(n))
        boxes = []
        for sp in x.iter('{%s}sp' % ns['p']):
            if not ''.join(sp.xpath('.//a:t/text()', namespaces=ns)).strip():
                continue
            if sp.find('.//p:cNvPr', ns).get('name') == 'Número':
                continue
            xf = sp.find('p:spPr/a:xfrm', ns)
            o = xf.find('a:off', ns); e = xf.find('a:ext', ns)
            top = sp
            while top.getparent() is not None and etree.QName(top.getparent()).localname == 'grpSp':
                top = top.getparent()
            boxes.append((int(o.get('x')) / 914400, int(o.get('y')) / 914400, int(e.get('cx')) / 914400,
                          int(e.get('cy')) / 914400, id(top)))
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a, c = boxes[i], boxes[j]
                w = min(a[0] + a[2], c[0] + c[2]) - max(a[0], c[0])
                h = min(a[1] + a[3], c[1] + c[3]) - max(a[1], c[1])
                if w > 0.04 and h > 0.04 and not (a[4] == c[4] and min(w, h) < 0.06):
                    out.append('%s: textos superpuestos' % n)
    return out


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
    errs += text_collisions(z)
    over = [w for w in WARN if w.startswith(('DESBORDE', 'PALABRA ANCHA', 'TABLA'))]
    print('QA: %d errores (XML, fuente, textos superpuestos) · %d desbordes de texto' % (len(errs), len(over)))
    for e in errs[:20]:
        print('  ERROR', e)
    if errs or over:
        raise SystemExit('QA fallido')


qa(OUT)
if len(sys.argv) <= 2:
    import entregables
    entregables.write(D, os.path.join(HERE, '..'))
