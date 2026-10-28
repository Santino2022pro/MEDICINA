# -*- coding: utf-8 -*-
"""Identidad visual de la presentación (derivada de la referencia ilustrada):
paneles de color de borde a borde, títulos manuscritos azul oscuro, recuadros
amarillos con borde negro, etiquetas azul marino, moléculas de bolas y varillas."""
from lib import *
from ui import *
from ill import *
import math, random

# ---------------------------------------------------------------- paleta (muestreada de la referencia)
NAVY = '1F3864'      # títulos y etiquetas oscuras
TBLUE = '2B4C7E'     # azul de los títulos manuscritos
AMA = 'FFCC4A'       # amarillo cálido de los recuadros
AMA2 = 'FFC000'      # amarillo intenso
CREMA = 'FFF2CC'
ROJO = 'C00000'
ROSA = 'FDE4E4'
SALM = 'FF9393'
VERDE_OSC = '4E7A30'
VERDE = '6CA848'
VERDE_CL = 'A9CF86'
VERDE_V = '00A84F'
CELESTE = 'D8E6F2'
LAVANDA = 'DADAF2'
AZUL = '0070C0'
AZUL_M = '86AADA'
NARANJA = 'E67830'
NARANJA_OSC = 'C0560E'
DURAZNO = 'F2AB86'
DURAZNO_CL = 'F2C2A8'
BLANCO = 'FFFFFF'
CIELO = '00A8F0'

OSCUROS = {ROJO, VERDE_OSC, AZUL, NARANJA_OSC, NAVY, NARANJA, VERDE_V, '6E1A12', TBLUE}

GLOW_W = '<a:effectLst><a:glow rad="76200"><a:srgbClr val="FFFFFF"><a:alpha val="85000"/></a:srgbClr></a:glow></a:effectLst>'

UNIT = {
    0: ('BIOQUÍMICA CLÍNICA Y METABOLISMO', AMA),
    1: ('UNIDAD I · LABORATORIO', CELESTE),
    2: ('UNIDAD II · METABOLISMO', VERDE_CL),
    3: ('UNIDAD III · ANEMIAS', SALM),
    4: ('UNIDAD IV · IAM', AZUL_M),
    5: ('UNIDAD V · HEPATOPANCREÁTICO', DURAZNO),
}

# combinaciones de paneles por unidad: (tipo, colores)
FONDOS = {
    0: [('der', AMA, BLANCO), ('bandas', CELESTE, AMA), ('izq', CREMA, BLANCO)],
    1: [('izq', CELESTE, BLANCO), ('der', AMA, BLANCO), ('bandas', CREMA, CELESTE), ('der', AZUL_M, CELESTE), ('izq', CREMA, BLANCO)],
    2: [('der', VERDE_OSC, BLANCO), ('izq', VERDE_CL, BLANCO), ('bandas', DURAZNO_CL, VERDE_CL), ('der', VERDE, CREMA), ('izq', CREMA, BLANCO)],
    3: [('der', ROJO, ROSA), ('izq', ROSA, BLANCO), ('bandas', ROSA, SALM), ('der', SALM, BLANCO), ('izq', CREMA, BLANCO)],
    4: [('der', AZUL, LAVANDA), ('izq', LAVANDA, BLANCO), ('bandas', CELESTE, AZUL_M), ('der', ROJO, BLANCO), ('izq', CREMA, BLANCO)],
    5: [('der', NARANJA, BLANCO), ('izq', DURAZNO_CL, BLANCO), ('bandas', CREMA, DURAZNO), ('der', NARANJA_OSC, CREMA), ('izq', CREMA, BLANCO)],
}

# registro académico / morph para los entregables
REG = {'morph': [], 'slides': []}


def fondo(s, tipo, c1, c2):
    """dibuja los paneles del fondo (siempre detrás del contenido)"""
    if tipo == 'izq':
        s.set_bg(c2)
        s.shape(0, 0, 4.7, SH, 'rect', c1, None, False, name='Fondo panel')
    elif tipo == 'der':
        s.set_bg(c2)
        s.shape(9.05, 0, SW - 9.05, SH, 'rect', c1, None, False, name='Fondo panel')
    elif tipo == 'bandas':
        s.set_bg(BLANCO)
        s.shape(0, 0, 3.3, SH, 'rect', c1, None, False, name='Fondo panel izq')
        s.shape(10.25, 0, SW - 10.25, SH, 'rect', c2, None, False, name='Fondo panel der')
    elif tipo == 'lleno':
        s.set_bg(c1)
    elif tipo == 'franja':   # franja inferior
        s.set_bg(c2)
        s.shape(0, 4.9, SW, SH - 4.9, 'rect', c1, None, False, name='Fondo franja')


def titulo(s, text, size=30, w=None, color=TBLUE, y=0.12, x=0.4, align='l', name='Título'):
    t = smart_upper(text)
    w = w or 9.0
    sz = size
    while text_w(plain(t), F_TITLE, True, sz) > w - 0.1 and sz > 18:
        sz -= 1
    lines = 1 if text_w(plain(t), F_TITLE, True, sz) <= w - 0.1 else 2
    h = (0.78 if lines == 1 else 1.3) * sz / 30
    return s.shape(x, y, w, max(h, 0.62), 'rect', None, None, False, t, sz, F_TITLE, color, True, align, 'm', (0, 0, 0, 0),
                   name=name, fit=True, minsize=16, reff=GLOW_W, lnspc=0.92)


def etiqueta_unidad(s, unit):
    lab = UNIT[unit][0]
    tw = text_w(lab, F_HEAD, True, 12.5) + 0.36
    return s.shape(SW - 0.3 - tw, 0.2, tw, 0.4, 'roundRect', NAVY, (INK, 1.25), False, lab, 12.5, F_HEAD, BLANCO, True, 'c', 'm',
                   (0.05, 0, 0.05, 0), name='Etiqueta sección', adj={'adj': 30000}, fit=False)


def nueva(D, unit, text, fondo_i=None, tipo=None, c1=None, c2=None, src=(), morph=False, tsize=30, tw=None, notas=None):
    s = D.new(BLANCO)
    s.unit = unit
    s.morph = morph
    k = fondo_i if fondo_i is not None else len(D.slides)
    f = FONDOS[unit][k % len(FONDOS[unit])]
    fondo(s, tipo or f[0], c1 or f[1], c2 or f[2])
    s.fondo = (tipo or f[0], c1 or f[1], c2 or f[2])
    titulo(s, text, tsize, w=tw)
    etiqueta_unidad(s, unit)
    s.meta = {'titulo': plain(smart_upper(text)), 'unit': unit, 'src': list(src)}
    if notas:
        s.note(notas)
    return s


# ---------------------------------------------------------------- recuadros de la serie
def caja(s, x, y, w, h, text, fill=AMA, size=16, color=None, head=None, headfill=NAVY, name=None, align='l', anchor='t',
         minsize=12, lw=1.75, geom='roundRect', bold=False, spc=4, shadow=False, grow=True):
    """recuadro con borde negro grueso y esquinas suaves; encabezado opcional (etiqueta azul marino)"""
    color = color or (BLANCO if fill in OSCUROS else INK)
    adj = {'adj': 9000} if geom == 'roundRect' else None
    if grow and text:
        iw = w - 0.3; ih = h - (0.38 if head else 0.16)
        top = min(size * 1.3, 22)
        sz = size
        while sz + 0.5 <= top and text_h(text, iw, sz + 0.5, F_BODY, bold, spc * (sz + 0.5) / size) <= ih * 0.86:
            sz += 0.5
        size = sz
    if head:
        g = s.group_start(name or ('Recuadro ' + plain(head)[:28]))
        s.shape(x, y + 0.22, w, h - 0.22, geom, fill, (INK, lw), shadow, text, size, F_BODY, color, bold, align, anchor,
                (0.15, 0.3, 0.15, 0.08), minsize=minsize, spc=spc, adj=adj)
        hs = 14
        t = smart_upper(head)
        hw = min(text_w(plain(t), F_HEAD, True, hs) + 0.34, w - 0.2)
        s.shape(x + 0.14, y, hw, 0.42, 'rect', headfill, (INK, 1.5), False, t, hs, F_HEAD,
                BLANCO if headfill in OSCUROS else INK, True, 'c', 'm', (0.04, 0, 0.04, 0), minsize=10)
        return s.group_end()
    return s.shape(x, y, w, h, geom, fill, (INK, lw), shadow, text, size, F_BODY, color, bold, align, anchor,
                   (0.15, 0.08, 0.15, 0.08), name=name, minsize=minsize, spc=spc, adj=adj)


def rotulo(s, x, y, text, fill=NAVY, size=14, color=None, w=None, h=None, name=None, geom='rect', lw=1.5, font=None):
    """etiqueta rectangular de la serie (azul marino con blanco, amarilla con negro, etc.)"""
    color = color or (BLANCO if fill in OSCUROS else INK)
    font = font or F_HEAD
    tw = text_w(plain(text), font, True, size) + 0.3
    w = w or tw
    h = h or size / 72 * 1.65
    return s.shape(x, y, w, h, geom, fill, (INK, lw), False, text, size, font, color, True, 'c', 'm', (0.05, 0.01, 0.05, 0.01),
                   name=name or ('Rótulo ' + plain(text)[:22]), minsize=9, adj={'adj': 20000} if geom == 'roundRect' else None)


def rotw(text, size=14):
    return text_w(plain(text), F_HEAD, True, size) + 0.3


def texto(s, x, y, w, h, text, size=16, color=INK, bold=False, align='l', anchor='t', name=None, font=None, minsize=12, glow=False):
    return s.shape(x, y, w, h, 'rect', None, None, False, text, size, font or F_BODY, color, bold, align, anchor, (0, 0, 0, 0),
                   name=name, minsize=minsize, reff=GLOW_W if glow else '')


def manuscrito(s, x, y, w, h, text, size=20, color=TBLUE, align='c', name=None, anchor='m'):
    """subtítulo en letra manuscrita (estilo referencia)"""
    return s.shape(x, y, w, h, 'rect', None, None, False, smart_upper(text), size, F_TITLE, color, True, align, anchor, (0, 0, 0, 0),
                   name=name, minsize=12, reff=GLOW_W, lnspc=0.92)


def flecha(s, pts, color=INK, w=2.5, curve=False, name=None, head=None, dash=None):
    return s.arrow(pts, color, w, head=head, curve=curve, name=name, dash=dash)


def num(s, x, y, n, d=0.46, fill=AMA2, name=None):
    return s.shape(x, y, d, d, 'ellipse', fill, (INK, 1.75), False, str(n), 15, F_HEAD, BLANCO if fill in OSCUROS else INK, True,
                   'c', 'm', (0, 0, 0, 0), name=name or ('Número %s' % n), fit=False)


# ---------------------------------------------------------------- moléculas de bolas y varillas (decorativas, estilo referencia)
ATOM = {'C': ('7ED67A', 1.0), 'O': ('F0505A', 1.0), 'H': ('F4F4F4', 0.62), 'N': ('7C8CF0', 1.0), 'S': ('F5D33C', 1.1), 'P': ('F39C12', 1.1),
        'Fe': ('D35400', 1.2)}

MOLS = {
    # (lista de átomos (símbolo, x, y), enlaces (i, j))
    'aa': ([('C', 0, 0), ('C', 1.0, -0.5), ('O', 1.9, -0.1), ('O', 1.1, -1.5), ('N', -0.9, -0.6), ('H', -1.7, -0.2), ('H', -1.0, -1.5),
            ('C', 0.0, 1.1), ('H', 0.7, 1.7), ('H', -0.7, 1.7), ('H', -0.5, 0.35)],
           [(0, 1), (1, 2), (1, 3), (0, 4), (4, 5), (4, 6), (0, 7), (7, 8), (7, 9), (0, 10)]),
    'piruvato': ([('C', 0, 0), ('C', 1.05, 0), ('C', -1.05, 0), ('O', 0, -1.1), ('O', 1.6, -0.9), ('O', 1.6, 0.9), ('H', -1.6, 0.8),
                  ('H', -1.6, -0.8), ('H', -1.5, 0.05)], [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (2, 8)]),
    'glucosa': ([('C', 0, 0), ('C', 1, 0.5), ('C', 2, 0), ('C', 2, -1.1), ('O', 1, -1.6), ('C', 0, -1.1), ('O', -0.9, 0.5), ('O', 1, 1.6),
                 ('O', 2.9, 0.5), ('C', -0.9, -1.7), ('O', -1.8, -1.2), ('H', -1.7, 0.1), ('H', 3.7, 0.1)],
                [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (0, 6), (1, 7), (2, 8), (5, 9), (9, 10), (6, 11), (8, 12)]),
    'hemo': ([('Fe', 0, 0), ('N', 0.9, 0), ('N', -0.9, 0), ('N', 0, 0.9), ('N', 0, -0.9), ('C', 1.5, 0.8), ('C', -1.5, 0.8), ('C', 1.5, -0.8),
              ('C', -1.5, -0.8), ('C', 0.8, 1.5), ('C', -0.8, 1.5), ('C', 0.8, -1.5), ('C', -0.8, -1.5)],
             [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 7), (2, 6), (2, 8), (3, 9), (3, 10), (4, 11), (4, 12), (5, 9), (6, 10), (7, 11), (8, 12)]),
    'acetil': ([('C', 0, 0), ('C', -1.1, 0.3), ('O', 0.3, -1.0), ('S', 1.1, 0.6), ('H', -1.7, -0.4), ('H', -1.5, 1.1), ('H', -1.0, 0.95),
                ('C', 2.2, 0.2), ('C', 3.2, 0.7)], [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (1, 6), (3, 7), (7, 8)]),
    'atp': ([('P', 0, 0), ('P', 1.2, 0), ('P', 2.4, 0), ('O', 0, -1), ('O', 1.2, -1), ('O', 2.4, -1), ('O', 0, 1), ('O', 1.2, 1),
             ('O', 2.4, 1), ('O', 3.4, 0), ('C', -1.2, 0.2), ('C', -2.1, -0.5), ('N', -2.9, 0.1)],
            [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (0, 6), (1, 7), (2, 8), (2, 9), (0, 10), (10, 11), (11, 12)]),
    'urea': ([('C', 0, 0), ('O', 0, -1.1), ('N', 1, 0.6), ('N', -1, 0.6), ('H', 1.8, 0.2), ('H', 1.0, 1.5), ('H', -1.8, 0.2), ('H', -1.0, 1.5)],
             [(0, 1), (0, 2), (0, 3), (2, 4), (2, 5), (3, 6), (3, 7)]),
}


def molecula3d(s, x, y, size, kind='aa', name=None, rot=0, alpha=None):
    """molécula de bolas y varillas en perspectiva (sombreado radial); size = ancho aprox. en pulgadas"""
    atoms, bonds = MOLS[kind]
    a = math.radians(rot)
    pts = [(sym, px * math.cos(a) - py * math.sin(a), px * math.sin(a) + py * math.cos(a)) for sym, px, py in atoms]
    xs = [p[1] for p in pts]; ys = [p[2] for p in pts]
    span = max(max(xs) - min(xs), max(ys) - min(ys)) + 1.2
    k = size / span
    ox = x + (size - (max(xs) - min(xs)) * k) / 2 - min(xs) * k
    oy = y + (size - (max(ys) - min(ys)) * k) / 2 - min(ys) * k
    g = s.group_start(name or ('Molécula 3D ' + kind))
    for i, j in bonds:
        p1 = (ox + pts[i][1] * k, oy + pts[i][2] * k); p2 = (ox + pts[j][1] * k, oy + pts[j][2] * k)
        s.arrow([p1, p2], 'B9B9B9', max(3, k * 16), tail=None)
        s.arrow([p1, p2], 'FFFFFF', max(1.5, k * 9), tail=None)
    order = sorted(range(len(pts)), key=lambda i: ATOM[pts[i][0]][1])
    for i in order:
        sym, px, py = pts[i]
        col, r = ATOM[sym]
        d = 0.62 * k * r * 1.3
        s.shape(ox + px * k - d / 2, oy + py * k - d / 2, d, d, 'ellipse',
                ('rad', [(0, 'FFFFFF'), (30, lighten(col, 0.25)), (75, col), (100, darken(col, 0.3))], (30, 25)), None, False)
    return s.group_end()


# ---------------------------------------------------------------- utilidades de animación
def clic(s, *ef):
    s.step(*ef)


def aparecen(s, ids, kind='fade', first_click=True, stagger=False):
    """agrupa varios ids en un mismo clic"""
    effs = []
    for i, sid in enumerate(ids):
        if kind == 'fade':
            effs.append(fade(sid, after=(stagger and i > 0)))
        elif kind == 'zoom':
            effs.append(zoom(sid, after=(stagger and i > 0)))
        else:
            effs.append(wipe(sid, kind, after=(stagger and i > 0)))
    s.step(*effs)


def registrar_morph(D, ini, fin, mecanismo, objetos, transformaciones):
    REG['morph'].append({'ini': ini, 'fin': fin, 'mec': mecanismo, 'obj': objetos, 'trans': transformaciones})
