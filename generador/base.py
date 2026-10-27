# -*- coding: utf-8 -*-
"""Plantillas compartidas: diapositivas por unidad, separadores y mapa de órganos."""
from lib import *
from ui import *
from ill import *

UNITS = {
    0: ('INTEGRACIÓN METABÓLICA', PEACH),
    1: ('UNIDAD I · ESTADO ALIMENTADO', PEACH),
    2: ('UNIDAD II · AYUNO', 'F6B8AF'),
    3: ('UNIDAD III · LÍPIDOS Y CONTROL', YELBG),
    4: ('UNIDAD IV · NITRÓGENO Y HOMEOSTASIS', BLUEBG),
    5: ('UNIDAD V · PATOLOGÍA', 'F8C1C8'),
    6: ('UNIDAD VI · CASOS CLÍNICOS', PEACH),
}


def new(D, unit, ttl, tag=None, bg=None, morph=False):
    lab, ubg = UNITS[unit]
    s = D.new(bg or ubg)
    s.unit = unit
    s.morph = morph
    title(s, ttl, tag or lab)
    return s


GLOW = ('<a:effectLst><a:glow rad="127000"><a:srgbClr val="F39C5A"><a:alpha val="75000"/></a:srgbClr></a:glow></a:effectLst>')


def big_title(s, x, y, w, h, text, size=60, color=INK, name='!!Título principal', align='c'):
    return s.shape(x, y, w, h, 'rect', None, None, False, text, size, F_TITLE, color, True, align, 'm', (0, 0, 0, 0),
                   name=name, reff=GLOW, minsize=28, lnspc=0.9)


def divider(D, unit, roman, ttl, sub, topics, art, notes=''):
    """separador de unidad: gran título con resplandor + temario + ilustración"""
    lab, bg = UNITS[unit]
    s = D.new(bg)
    s.unit = unit
    s.morph = False
    chip(s, 0.6, 0.55, 'UNIDAD ' + roman, TAG, 22, h=0.6, name='Etiqueta unidad', shadow=SHD)
    big_title(s, 0.5, 1.35, 7.4, 2.1, ttl, 46, align='l', name='Título unidad')
    s.text(0.55, 3.45, 7.2, 0.5, sub, 18, F_HEAD, '5A2D0C', True, 'l', 'm')
    if len(topics) > 7:
        h1 = (len(topics) + 1) // 2
        g = s.group_start('Temario')
        card(s, 0.55, 4.05, 3.55, 3.05, '\n'.join(topics[:h1]), CREAM, 13.5, spc=2, grow=False)
        card(s, 4.2, 4.05, 3.55, 3.05, '\n'.join(topics[h1:]), CREAM, 13.5, spc=2, grow=False)
        tb = s.group_end()
    else:
        tb = card(s, 0.55, 4.05, 7.2, 0.4 * len(topics) + 0.35, '\n'.join(topics), CREAM, 16, name='Temario', spc=2, grow=False)
    art(s)
    s.step(fade(tb))
    if notes:
        s.note(notes)
    return s


# ---------------------------------------------------------------- mapa interorgánico
POS = {
    'brain': (5.55, 0.98, 2.1), 'liver': (0.55, 1.2, 3.0), 'pancreas': (3.75, 2.55, 1.75), 'adipose': (9.75, 0.98, 2.4),
    'intestine': (0.75, 4.45, 2.1), 'kidney': (5.05, 4.45, 1.05), 'muscle': (8.75, 4.55, 3.9), 'vessel': (0.3, 3.5, 12.75, 0.6),
}
LAB = {'brain': 'CEREBRO', 'liver': 'HÍGADO', 'pancreas': 'PÁNCREAS', 'adipose': 'TEJIDO ADIPOSO', 'intestine': 'INTESTINO',
       'kidney': 'RIÑÓN', 'muscle': 'MÚSCULO', 'vessel': 'SANGRE'}
LABPOS = {'brain': (7.7, 1.15), 'liver': (0.6, 1.0), 'pancreas': (3.8, 3.12), 'adipose': (8.0, 2.2), 'intestine': (2.9, 4.5),
          'kidney': (6.2, 5.55), 'muscle': (8.8, 6.6), 'vessel': (0.45, 3.58)}


def organ_map(s, which=('brain', 'liver', 'pancreas', 'adipose', 'intestine', 'kidney', 'muscle', 'vessel'), labels=True,
              prefix='!!', dim=()):
    ids = {}
    for k in which:
        x, y, w = POS[k][:3]
        nm = prefix + LAB[k].capitalize()
        if k == 'brain':
            ids[k] = brain(s, x, y, w, name=nm)
        elif k == 'liver':
            ids[k] = liver(s, x, y, w, name=nm)
        elif k == 'pancreas':
            ids[k] = pancreas(s, x, y, w, name=nm)
        elif k == 'adipose':
            ids[k] = adipose_tissue(s, x, y, w, name=nm)
        elif k == 'intestine':
            ids[k] = intestine(s, x, y, w, name=nm)
        elif k == 'kidney':
            ids[k] = kidney(s, x, y, w, name=nm)
        elif k == 'muscle':
            ids[k] = muscle(s, x, y, w, name=nm)
        elif k == 'vessel':
            ids[k] = vessel(s, x, y, POS['vessel'][2], POS['vessel'][3], name=nm, rbcs=14)
        if labels and k != 'vessel':
            lx, ly = LABPOS[k]
            ids[k + '_lab'] = chip(s, lx, ly, LAB[k], TAG if k not in dim else 'E5E7E9', 13, name=prefix + 'Rótulo ' + LAB[k].lower())
    if labels and 'vessel' in which:
        lx, ly = LABPOS['vessel']
        ids['vessel_lab'] = chip(s, lx + 5.6, ly + 0.1, 'SANGRE', 'FFFFFF', 12, name=prefix + 'Rótulo sangre', line=('6E1A12', 1.0))
    return ids


def mover(s, key, x, y, text=None, d=0.4, name=None):
    """ficha molecular para animar trayectorias"""
    return mol(s, x, y, key, text, d, name=name)


def organ_icon(s, key, x, y, size=1.0):
    """ícono de órgano dentro de una caja de ~size x size"""
    k = size
    if key == 'liver':
        return liver(s, x, y + 0.15 * k, 1.0 * k, name='Ícono hígado')
    if key == 'muscle':
        return muscle(s, x, y + 0.2 * k, 1.0 * k, name='Ícono músculo', fibers=2)
    if key == 'adipose':
        return adipocyte_white(s, x + 0.1 * k, y + 0.05 * k, 0.8 * k, name='Ícono adiposo')
    if key == 'brain':
        return brain(s, x, y + 0.1 * k, 1.0 * k, name='Ícono cerebro')
    if key == 'kidney':
        return kidney(s, x + 0.2 * k, y, 0.6 * k, name='Ícono riñón')
    if key == 'intestine':
        return intestine(s, x + 0.05 * k, y + 0.05 * k, 0.9 * k, name='Ícono intestino')
    if key == 'pancreas':
        return pancreas(s, x, y + 0.3 * k, 1.0 * k, name='Ícono páncreas')
    if key == 'rbc':
        return rbc(s, x + 0.1 * k, y + 0.1 * k, 0.8 * k, name='Ícono eritrocito')
    if key == 'heart':
        return heart(s, x + 0.12 * k, y + 0.02 * k, 0.75 * k, name='Ícono corazón')
    if key == 'astro':
        return astrocyte(s, x, y + 0.1 * k, 1.0 * k, name='Ícono astrocito')
    if key == 'gut':
        return enterocyte_row(s, x, y + 0.2 * k, 1.0 * k, 0.6 * k, 3, name='Ícono enterocito')
    if key == 'tumor':
        return s.shape(x + 0.1 * k, y + 0.1 * k, 0.8 * k, 0.8 * k, 'ellipse', shade('A569BD', 0.4, 0.3), ('5B2C6F', 1.25), False, name='Ícono célula')
    if key == 'adrenal':
        return s.free(x + 0.1 * k, y + 0.1 * k, 0.8 * k, 0.75 * k, smooth([(500, 0), (900, 500), (850, 1000), (150, 1000), (100, 500)]), shade('F5B041', 0.4, 0.3), ('9C640C', 1.25), name='Ícono suprarrenal')
    return None


def organ_tiles(s, data, x0=0.4, y0=1.1, cols=4, tw=3.05, th=2.9, gx=0.12, gy=0.12, size=15.5, icon=0.95):
    """mosaico de órganos: data = [(key, título, texto, color)] ; devuelve ids de grupos"""
    ids = []
    for i, (k, t, txt, f) in enumerate(data):
        x = x0 + (i % cols) * (tw + gx); y = y0 + (i // cols) * (th + gy)
        g = s.group_start('Tile ' + plain(t))
        s.shape(x, y, tw, th, 'rect', f, (INK, 1.25), SHD)
        organ_icon(s, k, x + 0.1, y + 0.08, icon)
        s.text(x + icon + 0.25, y + 0.1, tw - icon - 0.35, 0.8, t, 15.5, F_HEAD, INK, True, 'l', 'm')
        s.text(x + 0.15, y + icon + 0.25, tw - 0.3, th - icon - 0.35, txt, size, F_BODY, INK, False, 'l', 't', spc=2)
        s.group_end(); ids.append(g)
    return ids
