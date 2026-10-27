# -*- coding: utf-8 -*-
"""Escena reutilizable de la señalización insulínica (miocito/adipocito) para las secuencias Morph."""
from base import *


def pchip(s, x, y, red=False, name=None, txt='P'):
    return s.shape(x, y, 0.3, 0.3, 'ellipse', 'C00000' if red else BOX, (INK, 1.0), False, txt, 9.5, F_HEAD,
                   WHITE if red else INK, True, 'c', 'm', (0, 0, 0, 0), fit=False, name=name or 'Fosfato')


def vesicle(s, x, y, name):
    g = s.group_start(name)
    s.shape(x, y, 0.62, 0.62, 'ellipse', ('rad', [(0, 'FFFFFF'), (100, 'FADBD8')], (40, 40)), ('B03A2E', 1.5), False)
    s.shape(x + 0.24, y + 0.12, 0.14, 0.38, 'roundRect', vshade('5DADE2', 0.3, 0.3), ('1F618D', 0.75), False, adj={'adj': 50000})
    return s.group_end()


def sig_scene(s, k, impaired=False, cell='MIOCITO / ADIPOCITO'):
    """k: 0 receptor libre · 1 insulina + autofosforilación · 2 IRS · 3 PI3K/PIP3 · 4 PDK1/Akt · 5 AS160/GLUT4 · 6 rama MAPK"""
    ids = {}
    lab(s, 3.4, 0.95, 3.0, 0.36, 'LÍQUIDO INTERSTICIAL', 13, align='l', name='!!Rótulo intersticio')
    s.shape(0.4, 2.95, 8.2, 4.1, 'roundRect', ('lin', [(0, 'FDEDEC'), (100, 'F5B7B1')], 90), ('B03A2E', 2.5), SHD, adj={'adj': 6000},
            name='!!Citosol')
    lab(s, 5.6, 6.55, 2.9, 0.36, 'CITOSOL · ' + cell, 12, align='r', name='!!Rótulo citosol')
    membrane_h(s, 0.4, 2.6, 8.2, 0.36, name='!!Membrana plasmática')
    ids['rec'] = insulin_receptor(s, 1.0, 2.6, 0.36, 1.25, name='!!Receptor de insulina')
    lab(s, 2.35, 1.3, 1.1, 0.5, 'RTK\nα_{2}β_{2}', 12, name='!!Rótulo RTK')
    if k >= 1:
        ids['ins'] = mol(s, 1.42, 1.6, 'ins', d=0.5, name='!!Insulina unida')
        ids['py'] = [pchip(s, 0.62, 3.55, name='!!PTyr 1'), pchip(s, 2.1, 3.55, name='!!PTyr 2')]
    # IRS
    if k >= 2:
        ids['irs'] = mbox(s, 2.55, 3.65, 1.35, 0.5, 'IRS-1/2', 'g', 13, caps=False, name='!!IRS')
        ids['irsp'] = pchip(s, 3.75, 3.45, red=impaired, name='!!IRS-P', txt='S' if impaired else 'P')
    else:
        ids['irs'] = mbox(s, 2.0, 5.35, 1.35, 0.5, 'IRS-1/2', 'w', 13, caps=False, name='!!IRS')
    # PI3K y fosfoinosítido
    if k >= 3:
        ids['pi3k'] = mbox(s, 4.05, 3.15, 1.0, 0.5, 'PI3K', 'g', 13, caps=False, name='!!PI3K')
        ids['pip'] = mbox(s, 4.0, 2.6, 1.1, 0.36, 'PIP_{3}', 'y', 12, name='!!Fosfoinosítido')
    else:
        ids['pi3k'] = mbox(s, 3.75, 6.0, 1.0, 0.5, 'PI3K', 'w', 13, caps=False, name='!!PI3K')
        ids['pip'] = mbox(s, 4.0, 2.6, 1.1, 0.36, 'PIP_{2}', 'w', 12, name='!!Fosfoinosítido')
    # PDK1 / Akt
    if k >= 4:
        ids['pdk'] = mbox(s, 5.25, 3.15, 0.9, 0.5, 'PDK1', 'g', 13, caps=False, name='!!PDK1')
        ids['akt'] = mbox(s, 6.3, 3.15, 0.9, 0.5, 'Akt', 'g' if not impaired else 'w', 14, caps=False, name='!!Akt')
        ids['aktp'] = pchip(s, 7.05, 2.98, name='!!Akt-P')
    else:
        ids['pdk'] = mbox(s, 5.0, 5.6, 0.9, 0.5, 'PDK1', 'w', 13, caps=False, name='!!PDK1')
        ids['akt'] = mbox(s, 6.1, 5.6, 0.9, 0.5, 'Akt', 'w', 14, caps=False, name='!!Akt')
    # AS160 y vesículas GLUT4
    if k >= 5:
        ids['as'] = mbox(s, 6.45, 4.1, 1.3, 0.5, 'AS160-P', 'g' if not impaired else 'w', 12.5, caps=False, name='!!AS160')
        vp = [(7.05, 2.45), (7.75, 2.45), (6.9, 4.95)] if not impaired else [(7.35, 2.45), (6.9, 5.4), (7.7, 5.0)]
    else:
        ids['as'] = mbox(s, 6.45, 4.1, 1.3, 0.5, 'AS160 (TBC1D4)', 'w', 11.5, caps=False, name='!!AS160')
        vp = [(6.9, 5.4), (7.7, 5.0), (7.55, 5.9)]
    ids['ves'] = [vesicle(s, x, y, '!!Vesícula GLUT4 %d' % i) for i, (x, y) in enumerate(vp)]
    # rama MAPK
    if k >= 6:
        g = s.group_start('!!Rama MAPK')
        for i, t in enumerate(['Grb2/SOS', 'Ras-GTP', 'Raf → MEK → ERK']):
            mbox(s, 0.7, 4.45 + i * 0.62, 1.95, 0.48, t, 'b', 12.5, caps=False)
            if i:
                s.arrow([(1.67, 4.45 + i * 0.62 - 0.13), (1.67, 4.45 + i * 0.62 - 0.01)], INK, 2)
        s.arrow([(1.67, 6.21), (1.67, 6.4)], INK, 2)
        s.shape(0.7, 6.42, 1.95, 0.5, 'rect', 'D2B4DE', (INK, 1.25), False, 'Núcleo: genes · proliferación', 10.5, F_HEAD, INK, True, 'c', 'm')
        ids['mapk'] = s.group_end()
    return ids


def sig_panel(s, n, head, text, h=4.75, y=1.15):
    g = s.group_start('!!Panel')
    s.shape(8.85, y, 4.1, h, 'rect', WHITE, (INK, 1.5), SHD)
    s.shape(9.0, y + 0.12, 0.6, 0.55, 'rect', BOX, (INK, 1.5), False, n, 16, F_HEAD, BOXT, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.text(9.75, y + 0.07, 3.1, 0.65, head, 16.5, F_HEAD, INK, True, 'l', 'm')
    s.text(9.05, y + 0.85, 3.75, h - 0.95, text, 14.5, F_BODY, INK, False, 'l', 't', spc=5)
    return s.group_end()


def sig_progress(s, active, labels=('Insulina', 'RTK-P', 'IRS', 'PI3K/PIP3', 'Akt', 'GLUT4', 'Glucosa')):
    g = s.group_start('!!Progreso señal')
    for i, t in enumerate(labels):
        on = (i + 1) in active
        s.shape(8.85 + i * 0.59, 6.2, 0.55, 0.62, 'rect', BOX if on else WHITE, (INK, 1.0), False, t, 9, F_HEAD, INK, True, 'c', 'm',
                (0.01, 0, 0.01, 0), minsize=7, name='Etapa %d' % (i + 1))
    return s.group_end()
