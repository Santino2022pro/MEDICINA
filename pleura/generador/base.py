# -*- coding: utf-8 -*-
"""Plantillas compartidas: diapositiva con fondo y encabezado, separadores de
unidad, leyendas de secuencia, registro de fuentes (índice académico) y de
secuencias Morph (mapa de Morph)."""
from scenes import *
from fondos import BG

MORPHMAP = []   # (inicio, fin, mecanismo, objetos, transformación)
UNITS = {}      # unidad -> (inicio, fin, título)


def new(D, tag, ttl, bg='azul', morph=False, src=(), tsize=24):
    s = D.new(BG[bg] if bg in BG else bg)
    s.morph = morph
    s.src = list(src)
    s.tagname = tag
    header(s, tag, ttl, tsize)
    return s


def num(D):
    return len(D.slides)


class Seq:
    """registra una secuencia Morph: abrir antes de la primera diapositiva, cerrar después de la última"""
    def __init__(self, D, mech, objs, transf):
        self.D = D; self.mech = mech; self.objs = objs; self.transf = transf
        self.start = len(D.slides) + 1

    def close(self):
        MORPHMAP.append((self.start, len(self.D.slides), self.mech, self.objs, self.transf))


def unit_start(D, k, title):
    UNITS[k] = [len(D.slides) + 1, None, title]


def unit_end(D, k):
    UNITS[k][1] = len(D.slides)


def divider(D, roman, ttl, sub, topics, art, bg='blanco', src=()):
    """separador de unidad: gran título manuscrito, temario en recuadros y escena anatómica"""
    s = D.new(BG[bg])
    s.src = list(src); s.tagname = 'Unidad ' + roman
    s.morph = False
    s.shape(0.35, 0.3, 1.9, 0.75, 'rect', WHITE, BORDER, False, 'UNIDAD ' + roman, 24, F_HEAD, INK, True, 'c', 'm',
            name='Etiqueta sección')
    t = s.text(0.35, 1.2, 6.4, 1.7, ttl.upper(), 40, F_TITLE, INK, True, 'l', 'm', name='Título', minsize=24, lnspc=0.9)
    sb = s.shape(0.35, 2.95, 6.3, 0.62, 'rect', CEL, BORDER, False, sub, 17, F_HEAD, INK, True, 'c', 'm', name='Subtítulo', minsize=11)
    ids = []
    y = 3.8
    hh = min(0.52, (6.95 - y) / max(1, len(topics)) - 0.08)
    for i, tp in enumerate(topics):
        ids.append(s.shape(0.55, y + i * (hh + 0.08), 6.0, hh, 'rect', [WHITE, PALE][i % 2], THIN, False, tp, 14.5,
                           F_BODY, INK, True, 'l', 'm', (0.12, 0, 0.1, 0), name='Tema %d' % (i + 1), minsize=10))
    a = art(s)
    s.step(fade(t), fade(sb, after=True))
    s.step(*[wipe(x, 'l', after=bool(k), dur=300) for k, x in enumerate(ids)])
    return s


def legend(s, text, x=0.3, y=6.62, w=None, fill=WHITE, size=15, name='!!Leyenda', h=0.62):
    """leyenda de paso (misma forma en toda la secuencia: Morph transforma su texto)"""
    w = w or (SW - 0.6)
    return box(s, x, y, w, h, text, fill, size, name=name, minsize=10.5)


def step_badge(s, n, tot, x=0.3, y=0.86, name='!!Paso'):
    return s.shape(x, y, 1.15, 0.42, 'rect', GOLD, THIN, False, 'PASO %d/%d' % (n, tot), 13, F_HEAD, INK, True, 'c', 'm',
                   (0.02, 0, 0.02, 0), name=name, minsize=9)


def two_cards(s, items, x, y, w, h, gap=0.2, size=14):
    """columna de recuadros con encabezado: items = [(cabecera, texto, color)]"""
    n = len(items)
    hh = (h - gap * (n - 1)) / n
    return [box(s, x, y + i * (hh + gap), w, hh, t, f, size, head=hd, headfill=WHITE, align='l', anchor='m', bold=False)
            for i, (hd, t, f) in enumerate(items)]


def reveal(s, ids, per=1, kind='fade'):
    """revela una lista de objetos: 'per' objetos por clic"""
    for i in range(0, len(ids), per):
        grp = [x for x in ids[i:i + per] if x]
        if grp:
            s.step(*[(fade if kind == 'fade' else (lambda o, after=False: wipe(o, 'l', after=after)))(o, after=bool(k)) for k, o in enumerate(grp)])
