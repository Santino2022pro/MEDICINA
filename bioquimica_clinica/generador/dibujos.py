# -*- coding: utf-8 -*-
"""Ilustraciones originales de esta presentación (formas nativas editables).
Cada función devuelve el id del grupo (o de la forma) creada."""
from estilo import *

SH_I = (8, 4, 28)


# ================================================================ laboratorio
def tubo(s, x, y, w, h, capas=None, tapa='C0392B', name='!!Tubo', vidrio=True, etiqueta=None, grupo=None):
    """tubo de ensayo vertical. capas = [(fracción desde abajo, color, nombre)] dibujadas como objetos independientes
    (fuera del grupo del vidrio, para que Morph pueda transformarlas)."""
    ids = {}
    if grupo:
        outer = s.group_start(grupo)
    g = s.group_start(name)
    # cuerpo: rectángulo + fondo redondeado
    body = 'M 0 0 L 1000 0 L 1000 820 C 1000 930 780 1000 500 1000 C 220 1000 0 930 0 820 Z'
    s.free(x, y + h * 0.1, w, h * 0.9, body, ('a', 'EAF2FA', 55), ('5D6D7E', 1.75), SH_I, name='Vidrio')
    s.shape(x - w * 0.08, y, w * 1.16, h * 0.12, 'roundRect', shade(tapa, 0.35, 0.3), (darken(tapa, 0.5), 1.25), False, name='Tapón',
            adj={'adj': 25000})
    s.free(x + w * 0.14, y + h * 0.16, w * 0.12, h * 0.7, 'M 0 0 L 1000 0 L 1000 1000 L 0 1000 Z', ('a', 'FFFFFF', 70), None, name='Brillo')
    gid = s.group_end()
    ids['vidrio'] = gid
    if capas:
        base = y + h - h * 0.02
        acc = 0
        inner_h = h * 0.84
        for k, (fr, col, nm) in enumerate(capas):
            hh = inner_h * fr
            top = base - acc - hh
            if k == 0:
                d = 'M 0 0 L 1000 0 L 1000 600 C 1000 850 760 1000 500 1000 C 240 1000 0 850 0 600 Z'
                ids[nm] = s.free(x + w * 0.05, top, w * 0.9, hh, d, col if isinstance(col, (tuple, list)) else shade(col, 0.25, 0.2, (40, 40)),
                                 (darken(col if isinstance(col, str) else col[1][1][1], 0.35), 0.75), name=nm)
            else:
                ids[nm] = s.shape(x + w * 0.05, top, w * 0.9, hh, 'rect', col if isinstance(col, (tuple, list)) else ('lin', [(0, lighten(col, 0.25)), (100, col)], 90),
                                  (darken(col if isinstance(col, str) else col[1][1][1], 0.35), 0.75), False, name=nm)
            acc += hh
    if etiqueta:
        ids['etq'] = s.shape(x - 0.2, y + h + 0.06, w + 0.4, 0.36, 'rect', None, None, False, etiqueta, 13, F_HEAD, INK, True, 'c', 'm',
                             (0, 0, 0, 0), name='Rótulo ' + name.replace('!!', ''), minsize=10)
    if grupo:
        return s.group_end()
    return ids


def jeringa(s, x, y, w, name='!!Jeringa', lleno=0.7):
    h = w * 0.22
    g = s.group_start(name)
    s.shape(x + w * 0.15, y, w * 0.62, h, 'rect', ('a', 'EAF2FA', 60), ('5D6D7E', 1.5), False, name='Cilindro')
    s.shape(x + w * 0.15 + w * 0.62 * (1 - lleno), y + h * 0.1, w * 0.62 * lleno, h * 0.8, 'rect', shade('B3261E', 0.3, 0.2), None, False, name='Sangre')
    s.shape(x, y - h * 0.15, w * 0.04, h * 1.3, 'rect', '7F8C8D', ('34495E', 1.0), False)
    s.shape(x + w * 0.03, y + h * 0.4, w * 0.13, h * 0.2, 'rect', 'BDC3C7', ('34495E', 0.75), False)
    s.shape(x + w * 0.77, y + h * 0.3, w * 0.06, h * 0.4, 'rect', 'D5DBDB', ('34495E', 0.75), False)
    s.arrow([(x + w * 0.83, y + h * 0.5), (x + w, y + h * 0.5)], '7F8C8D', 1.5, tail=None)
    for i in range(1, 6):
        s.arrow([(x + w * (0.2 + 0.1 * i), y), (x + w * (0.2 + 0.1 * i), y + h * 0.3)], '5D6D7E', 0.75, tail=None)
    return s.group_end()


def brazo(s, x, y, w, name='!!Brazo'):
    h = w * 0.42
    g = s.group_start(name)
    pts = [(0, 250), (300, 200), (620, 230), (900, 300), (1000, 420), (980, 700), (880, 800), (600, 770), (300, 800), (0, 780)]
    s.free(x, y, w, h, smooth(pts, True, 0.6), shade('F5CBA7', 0.35, 0.18), ('A0522D', 1.5), SH_I)
    strokes(s, x, y, w, h, ['M 40 520 C 300 470 520 560 760 520 C 860 505 930 520 990 560'], '5B7DB1', 4.5)
    strokes(s, x, y, w, h, ['M 40 520 C 300 470 520 560 760 520 C 860 505 930 520 990 560'], '85A5D6', 2.0)
    return s.group_end()


def centrifuga(s, x, y, d, name='!!Centrífuga', tubos=6):
    g = s.group_start(name)
    s.shape(x - d * 0.08, y + d * 0.55, d * 1.16, d * 0.62, 'roundRect', shade('B0BEC5', 0.4, 0.3), ('37474F', 1.75), SH_I, adj={'adj': 12000})
    s.shape(x, y, d, d, 'ellipse', shade('ECEFF1', 0.3, 0.25), ('37474F', 2.0), SH_I, name='Rotor')
    s.shape(x + d * 0.38, y + d * 0.38, d * 0.24, d * 0.24, 'ellipse', shade('78909C', 0.3, 0.3), ('263238', 1.25), False)
    for i in range(tubos):
        a = 2 * math.pi * i / tubos
        cx = x + d / 2 + d * 0.32 * math.cos(a); cy = y + d / 2 + d * 0.32 * math.sin(a)
        s.shape(cx - d * 0.07, cy - d * 0.07, d * 0.14, d * 0.14, 'ellipse', shade('C0392B', 0.3, 0.3), ('641E16', 1.0), False)
    s.shape(x + d * 0.25, y + d * 1.0, d * 0.5, d * 0.1, 'roundRect', '263238', None, False, adj={'adj': 50000})
    return s.group_end()


def giro(s, x, y, d, name='Giro', color=NAVY):
    """flecha circular de rotación"""
    return s.shape(x, y, d, d, 'circularArrow', color, (INK, 1.0), False, name=name, adj={'adj1': 9000, 'adj2': 1142319, 'adj3': 20457681, 'adj4': 10800000, 'adj5': 11000})


def diana(s, x, y, d, impactos, name='!!Diana', centro=(0, 0)):
    g = s.group_start(name)
    cols = ['FFFFFF', 'D6EAF8', 'FFFFFF', 'D6EAF8', 'C00000']
    for i, c in enumerate(cols):
        f = 1 - i * 0.2
        s.shape(x + d * (1 - f) / 2, y + d * (1 - f) / 2, d * f, d * f, 'ellipse', c, (INK, 1.25), False)
    gi = s.group_end()
    hits = []
    for k, (dx, dy) in enumerate(impactos):
        hx = x + d / 2 + dx * d / 2 - 0.08; hy = y + d / 2 + dy * d / 2 - 0.08
        hits.append(s.shape(hx, hy, 0.16, 0.16, 'ellipse', '1E1E1E', ('FFFFFF', 1.0), False, name='Impacto %d' % (k + 1)))
    return gi, hits


def gauss_path(mu=500, sd=150, H=1000, top=80):
    pts = []
    for i in range(0, 1001, 25):
        yv = math.exp(-((i - mu) ** 2) / (2 * sd * sd))
        pts.append((i, int(H - 40 - (H - 40 - top) * yv)))
    return pts


def ejes(s, x, y, w, h, xlab=None, ylab=None, name='!!Ejes', color=INK, size=14):
    g = s.group_start(name)
    s.arrow([(x, y + h), (x, y - 0.1)], color, 2.25)
    s.arrow([(x, y + h), (x + w + 0.1, y + h)], color, 2.25)
    if xlab:
        s.text(x + w - 3.0, y + h + 0.06, 3.1, 0.35, xlab, size, F_HEAD, color, True, 'r', 't', minsize=10)
    if ylab:
        s.text(x - 0.05, y - 0.5, 4.0, 0.36, ylab, size, F_HEAD, color, True, 'l', 'b', minsize=10)
    return s.group_end()


def curva(s, x, y, w, h, pts, color, wpt=4.5, name='!!Curva', dash=None, fill=None, W=1000, H=1000):
    """curva suave abierta en coordenadas 0..W x 0..H (y hacia abajo)"""
    d = smooth(pts, closed=False, t=0.9)
    if fill:
        dfill = d + ' L %d %d L %d %d Z' % (pts[-1][0], H, pts[0][0], H)
        return s.free(x, y, w, h, [(dfill, True, False), (d, False, True)], fill, (color, wpt, dash), name=name, W=W, H=H)
    return s.free(x, y, w, h, [(d, False, True)], None, (color, wpt, dash), name=name, W=W, H=H)


def tabla_filas(s, x, y, colw, rows, rowh=0.46, size=14, head_fill=NAVY, fills=(CREMA, BLANCO), name='Tabla', heights=None,
                first_bold=True, col_fills=None, head_size=None, minsize=11):
    """tabla construida con formas: cada fila es un grupo (para animar fila por fila). Devuelve (ids_filas, alto)"""
    ids = []
    yy = y
    hs = head_size or size
    for r, row in enumerate(rows):
        hh = heights[r] if heights else rowh
        if not heights:
            for c, cell in enumerate(row):
                th = text_h(cell, colw[c] - 0.18, hs if r == 0 else size, F_BODY, r == 0) + 0.14
                hh = max(hh, th)
        g = s.group_start('%s fila %d' % (name, r))
        xx = x
        for c, cell in enumerate(row):
            if r == 0:
                f = head_fill; col = BLANCO if head_fill in OSCUROS else INK; b = True; sz = hs
            else:
                f = (col_fills[c] if col_fills and col_fills[c] else fills[(r - 1) % len(fills)])
                col = BLANCO if f in OSCUROS else INK; b = (c == 0 and first_bold); sz = size
            s.shape(xx, yy, colw[c], hh, 'rect', f, (INK, 1.25), False, cell, sz, F_BODY, col, b, 'l' if c or r else 'l', 'm',
                    (0.09, 0.03, 0.09, 0.03), minsize=minsize, spc=1)
            xx += colw[c]
        ids.append(s.group_end())
        yy += hh
    if yy > SH - 0.1:
        WARN.append('TABLA desborda (%s): %.2f' % (name, yy))
    return ids, yy - y


# ================================================================ sangre
def eritrocito(s, x, y, d, kind='normal', name='!!Eritrocito'):
    """vista frontal: disco bicóncavo (centro pálido). kind: normal, hipo, esfero, macro, micro, palido"""
    base = {'normal': ('C9372C', 'F29A8E'), 'hipo': ('D9645A', 'FBE3DE'), 'esfero': ('A8231A', 'B83229'),
            'reti': ('B05A8C', 'E3B4CF'), 'mega': ('C0392B', 'EFA095')}[kind]
    core = {'normal': 38, 'hipo': 62, 'esfero': 8, 'reti': 30, 'mega': 34}[kind]
    fill = ('rad', [(0, base[1]), (core, base[1]), (min(core + 30, 92), lighten(base[0], 0.15)), (100, darken(base[0], 0.35))], (50, 50))
    if kind == 'esfero':
        fill = ('rad', [(0, 'E35D52'), (55, 'B8261C'), (100, '6E1510')], (38, 32))
    sid = s.shape(x, y, d, d, 'ellipse', fill, ('6E1A12', 1.0), False, name=name)
    return sid


def eritrocito_perfil(s, x, y, w, name='!!Eritrocito perfil'):
    """corte lateral bicóncavo (forma de 'hueso')"""
    h = w * 0.36
    pts = [(0, 500), (60, 180), (220, 40), (380, 120), (500, 300), (620, 120), (780, 40), (940, 180), (1000, 500), (940, 820), (780, 960),
           (620, 880), (500, 700), (380, 880), (220, 960), (60, 820)]
    return s.free(x, y, w, h, smooth(pts, True, 0.7), vshade('C0392B', 0.3, 0.35), ('6E1A12', 1.25), SH_I, name=name)


def reticulocito(s, x, y, d, name='!!Reticulocito'):
    g = s.group_start(name)
    eritrocito(s, x, y, d, 'reti', name='Cuerpo')
    random.seed(4)
    paths = []
    for k in range(6):
        cx, cy = random.randint(250, 750), random.randint(250, 750)
        paths.append('M %d %d C %d %d %d %d %d %d' % (cx - 150, cy, cx - 50, cy - 120, cx + 50, cy + 120, cx + 150, cy - 30))
    strokes(s, x, y, d, d, paths, '4A235A', 1.5)
    return s.group_end()


def megaloblasto(s, x, y, d, name='!!Megaloblasto', nucleo=0.45):
    g = s.group_start(name)
    s.shape(x, y, d, d, 'ellipse', shade('E8A3B6', 0.4, 0.25), ('8E3A59', 1.25), SH_I, name='Citoplasma')
    s.shape(x + d * (0.5 - nucleo / 2), y + d * (0.5 - nucleo / 2), d * nucleo, d * nucleo, 'ellipse', ('rad', [(0, 'B39DDB'), (100, '5E35B1')], (40, 35)),
            ('311B92', 1.0), False, name='Núcleo')
    random.seed(9)
    dots = [(random.randint(300, 700), random.randint(300, 700), random.randint(20, 40)) for _ in range(14)]
    s.free(x + d * (0.5 - nucleo / 2), y + d * (0.5 - nucleo / 2), d * nucleo, d * nucleo, many_circles(dots), '311B92', None)
    return s.group_end()


def leucocito(s, x, y, d, kind='neutrofilo', name=None):
    g = s.group_start(name or ('!!' + kind.capitalize()))
    cyto = {'neutrofilo': 'F5E6EF', 'eosinofilo': 'FADBD8', 'basofilo': 'E8DAEF', 'linfocito': 'E3F2FD', 'monocito': 'EDE7F6'}[kind]
    s.shape(x, y, d, d, 'ellipse', shade(cyto, 0.4, 0.12), ('7D3C98', 1.25), SH_I)
    random.seed(len(kind))
    if kind in ('neutrofilo', 'eosinofilo', 'basofilo'):
        gcol = {'neutrofilo': 'D7BDE2', 'eosinofilo': 'E74C3C', 'basofilo': '4A235A'}[kind]
        dots = [(random.randint(150, 850), random.randint(150, 850), random.randint(22, 34)) for _ in range(40)]
        dots = [p for p in dots if (p[0] - 500) ** 2 + (p[1] - 500) ** 2 < 360 ** 2]
        s.free(x, y, d, d, many_circles(dots), gcol, None)
        if kind == 'neutrofilo':
            lobes = [(330, 420, 120), (500, 330, 120), (660, 450, 120), (520, 600, 110)]
        else:
            lobes = [(380, 450, 160), (630, 470, 160)]
        s.free(x, y, d, d, many_circles(lobes), ('rad', [(0, '9B59B6'), (100, '5B2C6F')], (40, 35)), ('4A235A', 1.0))
    elif kind == 'linfocito':
        s.shape(x + d * 0.14, y + d * 0.14, d * 0.72, d * 0.72, 'ellipse', ('rad', [(0, '7E57C2'), (100, '311B92')], (40, 35)), ('1A0F4F', 1.0), False)
    else:
        s.free(x, y, d, d, smooth([(250, 300), (450, 230), (700, 300), (720, 500), (600, 560), (480, 520), (380, 640), (230, 560)]),
               ('rad', [(0, '9575CD'), (100, '4527A0')], (40, 35)), ('311B92', 1.0))
    return s.group_end()


def plaqueta(s, x, y, d, name='Plaqueta', activa=False):
    if activa:
        pts = [(500, 0), (600, 350), (1000, 300), (680, 560), (900, 1000), (500, 700), (100, 1000), (320, 560), (0, 300), (400, 350)]
        return s.free(x, y, d, d, smooth(pts, True, 0.4), shade('C39BD3', 0.4, 0.2), ('6C3483', 1.0), name=name)
    return s.shape(x, y, d, d * 0.62, 'ellipse', shade('D2B4DE', 0.4, 0.2), ('6C3483', 1.0), False, name=name)


def megacariocito(s, x, y, d, name='!!Megacariocito'):
    g = s.group_start(name)
    pts = [(500, 40), (700, 90), (880, 230), (960, 450), (900, 700), (760, 880), (520, 960), (280, 900), (110, 720), (50, 470), (120, 240), (300, 90)]
    s.free(x, y, d, d, smooth(pts), shade('E8DAEF', 0.4, 0.2), ('6C3483', 1.5), SH_I)
    s.free(x, y, d, d, many_circles([(400, 420, 150), (580, 380, 140), (560, 580, 150), (380, 600, 130)]), ('rad', [(0, '8E44AD'), (100, '4A235A')], (40, 35)),
           ('4A235A', 1.0))
    return s.group_end()


def capilar(s, x, y, w, h, name='!!Capilar'):
    g = s.group_start(name)
    s.shape(x, y, w, h, 'roundRect', vshade('E57373', 0.25, 0.3), ('8E2A22', 1.75), SH_I, adj={'adj': 50000})
    s.shape(x + 0.06, y + h * 0.2, w - 0.12, h * 0.6, 'roundRect', ('lin', [(0, 'FADBD8'), (50, 'FDEDEC'), (100, 'F5B7B1')], 90), ('C0392B', 0.75),
            False, adj={'adj': 50000})
    return s.group_end()


def proteina_bola(s, x, y, d, color='F4D03F', text=None, name='Proteína'):
    return s.shape(x, y, d, d, 'ellipse', shade(color, 0.4, 0.25), (darken(color, 0.5), 1.0), False, text, 11, F_HEAD, INK, True, 'c', 'm',
                   (0, 0, 0, 0), name=name, fit=False)


def hemoglobina(s, x, y, d, name='!!Hemoglobina'):
    """tetrámero 2α + 2β con 4 grupos hemo (Fe)"""
    g = s.group_start(name)
    for i, (cx, cy, col, t) in enumerate(((0.3, 0.3, 'E57373', 'α'), (0.7, 0.3, 'F5B041', 'β'), (0.3, 0.7, 'F5B041', 'β'), (0.7, 0.7, 'E57373', 'α'))):
        s.shape(x + d * (cx - 0.24), y + d * (cy - 0.24), d * 0.48, d * 0.48, 'ellipse', shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), False,
                t, max(10, d * 13), F_HEAD, INK, True, 'c', 't', (0, d * 0.05, 0, 0), fit=False)
        s.shape(x + d * (cx - 0.07), y + d * (cy + 0.02), d * 0.14, d * 0.14, 'diamond', 'C0392B', ('641E16', 0.75), False)
    return s.group_end()


def medula_osea(s, x, y, w, h, name='!!MedulaOsea', seed=3, celulas=22):
    g = s.group_start(name)
    s.shape(x, y, w, h, 'roundRect', ('lin', [(0, 'F6DDCC'), (100, 'EDBB99')], 90), ('873600', 2.0), SH_I, adj={'adj': 30000}, name='Hueso')
    s.shape(x + w * 0.06, y + h * 0.12, w * 0.88, h * 0.76, 'roundRect', ('rad', [(0, 'F9E79F'), (100, 'F5B7B1')], (50, 50)), ('A04000', 1.0), False,
            adj={'adj': 30000}, name='Médula')
    random.seed(seed)
    for k in range(celulas):
        cx = x + w * (0.12 + 0.76 * random.random()); cy = y + h * (0.2 + 0.6 * random.random())
        dd = min(w, h) * (0.08 + 0.05 * random.random())
        col = random.choice(['C39BD3', 'E8A3B6', 'F1948A', 'D7BDE2'])
        s.shape(cx, cy, dd, dd, 'ellipse', shade(col, 0.4, 0.25), (darken(col, 0.5), 0.75), False)
        s.shape(cx + dd * 0.3, cy + dd * 0.3, dd * 0.4, dd * 0.4, 'ellipse', '5B2C6F', None, False)
    return s.group_end()


# ================================================================ metabolismo
def mitocondria_grande(s, x, y, w, h, name='!!Mitocondria', crestas=True, prof=1.0):
    """mitocondria en corte: membrana externa, espacio intermembrana, membrana interna con crestas, matriz"""
    g = s.group_start(name)
    s.shape(x, y, w, h, 'roundRect', ('rad', [(0, 'FAD7A0'), (100, 'EB984E')], (50, 50)), ('784212', 3.0), SH_I, adj={'adj': 50000},
            name='Membrana externa')
    m = min(w, h) * 0.07
    s.shape(x + m, y + m, w - 2 * m, h - 2 * m, 'roundRect', ('rad', [(0, 'FEF5E7'), (100, 'FAD7A0')], (50, 50)), ('A04000', 3.5), False,
            adj={'adj': 50000}, name='Membrana interna (matriz)')
    if crestas:
        paths = []
        n = 7
        for i in range(n):
            cx = 120 + 760 * i / (n - 1)
            d1 = int(70 + 260 * prof); d2 = int(930 - 260 * prof)
            if i % 2 == 0:
                paths.append('M %d 70 L %d %d C %d %d %d %d %d %d L %d 70' % (cx - 30, cx - 30, d1, cx - 30, d1 + 50, cx + 30, d1 + 50, cx + 30, d1, cx + 30))
            else:
                paths.append('M %d 930 L %d %d C %d %d %d %d %d %d L %d 930' % (cx - 30, cx - 30, d2, cx - 30, d2 - 50, cx + 30, d2 - 50, cx + 30, d2, cx + 30))
        s.free(x + m, y + m, w - 2 * m, h - 2 * m, [(p, False, True) for p in paths], None, ('A04000', 3.0), name='Crestas')
    return s.group_end()


def proteina_membrana(s, x, y, w, h, color='5DADE2', text=None, name='!!Transportador', size=12):
    """proteína transmembrana (dos lóbulos con poro)"""
    g = s.group_start(name)
    s.shape(x, y, w * 0.45, h, 'roundRect', shade(color, 0.4, 0.25), (darken(color, 0.5), 1.25), False, adj={'adj': 50000})
    s.shape(x + w * 0.55, y, w * 0.45, h, 'roundRect', shade(color, 0.4, 0.25), (darken(color, 0.5), 1.25), False, adj={'adj': 50000})
    if text:
        s.text(x - 0.5, y + h + 0.02, w + 1.0, 0.3, text, size, F_HEAD, darken(color, 0.55), True, 'c', 't', minsize=9)
    return s.group_end()


def ficha(s, x, y, text, fill, w=None, h=0.42, size=14, name=None, geom='roundRect', color=None):
    """ficha molecular (píldora) para sustratos, productos, cofactores"""
    color = color or (BLANCO if fill in OSCUROS or fill in ('8E44AD', '2E86C1', '1F618D', 'B03A2E', '117A65', '6C3483', 'A04000', 'C0392B') else INK)
    w = w or (text_w(plain(text), F_HEAD, True, size) + 0.34)
    return s.shape(x, y, w, h, geom, shade(fill, 0.35, 0.2), (darken(fill, 0.5), 1.25), False, text, size, F_HEAD, color, True, 'c', 'm',
                   (0.03, 0, 0.03, 0), name=name or ('Ficha ' + plain(text)[:18]), adj={'adj': 50000} if geom == 'roundRect' else None, fit=False)


def enzima_globular(s, x, y, w, h, color, text, name, size=16, seed=1):
    """enzima con forma globular irregular"""
    random.seed(seed)
    pts = []
    n = 12
    for i in range(n):
        a = 2 * math.pi * i / n
        r = 420 + random.randint(-50, 60)
        pts.append((int(500 + r * math.cos(a)), int(500 + r * math.sin(a))))
    return s.free(x, y, w, h, smooth(pts), shade(color, 0.45, 0.25), (darken(color, 0.5), 1.75), SH_I, name=name,
                  text=text, size=size, font=F_HEAD, color=INK if color not in OSCUROS else BLANCO, bold=True, align='c', anchor='m',
                  ins=(0.03, 0.03, 0.03, 0.03), fit=False)


# ================================================================ corazón
def corazon_anat(s, x, y, w, name='!!Corazon', coronarias=True):
    """corazón anatómico (cara anterior) con aorta y arterias coronarias como objetos separados"""
    h = w * 1.1
    ids = {}
    g = s.group_start(name)
    # aorta y pulmonar
    s.free(x + w * 0.38, y, w * 0.32, h * 0.32, smooth([(150, 1000), (100, 500), (220, 120), (520, 0), (850, 80), (1000, 300), (880, 380),
                                                         (700, 250), (520, 230), (420, 420), (430, 1000)], True, 0.6),
           shade('D35454', 0.35, 0.3), ('7B1F17', 1.75), name='Aorta')
    s.free(x + w * 0.22, y + h * 0.1, w * 0.22, h * 0.25, smooth([(300, 1000), (250, 400), (500, 80), (900, 60), (950, 300), (650, 350), (650, 1000)], True, 0.6),
           shade('5B7DB1', 0.35, 0.3), ('1F3864', 1.5), name='Arteria pulmonar')
    pts = [(420, 230), (640, 200), (840, 260), (960, 440), (930, 640), (780, 820), (560, 980), (420, 900), (230, 760), (90, 560), (60, 380),
           (170, 250), (300, 210)]
    s.free(x, y + h * 0.18, w, h * 0.82, smooth(pts), shade('C0392B', 0.42, 0.32, (35, 30)), ('641E16', 2.25), SH_I, W=1000, H=1000,
           name='Miocardio')
    s.free(x + w * 0.04, y + h * 0.3, w * 0.28, h * 0.28, smooth([(200, 100), (700, 60), (950, 400), (800, 850), (300, 900), (60, 500)]),
           shade('B03A2E', 0.4, 0.3), ('641E16', 1.5), name='Aurícula derecha')
    ids['g'] = s.group_end()
    if coronarias:
        ids['ci'] = s.free(x, y + h * 0.18, w, h * 0.82, [('M 470 240 C 520 330 560 450 560 560 C 560 700 520 820 480 940', False, True),
                                                           ('M 470 240 C 600 260 760 330 880 450', False, True),
                                                           ('M 560 470 C 650 520 720 600 760 700', False, True)],
                           None, ('F4D03F', 4.5), name='!!ArteriaCoronaria izquierda')
        ids['cd'] = s.free(x, y + h * 0.18, w, h * 0.82, [('M 420 235 C 300 300 180 420 140 560 C 120 650 160 760 260 820', False, True)],
                           None, ('F4D03F', 4.5), name='!!ArteriaCoronaria derecha')
    return ids


def cardiomiocito(s, x, y, w, h, name='!!Cardiomiocito', detalle=True):
    """célula muscular cardíaca: estriaciones, núcleo central, mitocondrias, discos intercalares"""
    ids = {}
    g = s.group_start(name)
    pts = [(0, 200), (120, 120), (300, 90), (520, 110), (720, 80), (880, 120), (1000, 220), (1000, 780), (880, 880), (700, 910), (500, 880),
           (300, 910), (120, 870), (0, 790)]
    s.free(x, y, w, h, smooth(pts, True, 0.5), ('lin', [(0, 'E6837A'), (35, 'F5B7B1'), (65, 'EC9A90'), (100, 'C9564B')], 90), ('7B241C', 2.5), SH_I,
           name='Sarcolema')
    n = 22
    st = ['M %d 160 L %d 840' % (int(40 + 920 * i / n), int(40 + 920 * i / n)) for i in range(n + 1)]
    s.free(x, y, w, h, [(p, False, True) for p in st], None, ('A93226', 1.0), name='Estriaciones')
    s.shape(x - w * 0.015, y + h * 0.15, w * 0.03, h * 0.7, 'rect', '7B241C', None, False, name='Disco intercalar izq')
    s.shape(x + w * 0.985, y + h * 0.15, w * 0.03, h * 0.7, 'rect', '7B241C', None, False, name='Disco intercalar der')
    if detalle:
        nucleus(s, x + w * 0.44, y + h * 0.38, w * 0.12, name='Núcleo')
        for (mx, my) in ((0.12, 0.25), (0.28, 0.62), (0.68, 0.24), (0.8, 0.6), (0.62, 0.66), (0.2, 0.38)):
            mito(s, x + w * mx, y + h * my, w * 0.1)
    ids['g'] = s.group_end()
    return ids


def ecg_path(kind='normal', beats=2):
    """trazado de ECG en 0..1000 x 0..600 (línea isoeléctrica en y=350)"""
    base = 350
    seg = 1000 / beats
    d = 'M 0 %d ' % base
    for b in range(beats):
        o = b * seg
        def X(f):
            return int(o + f * seg)
        st = {'normal': 0, 'st': -110, 'q': -40, 'cicatriz': 0, 'ntinv': 0}[kind]
        t = {'normal': -90, 'st': -170, 'q': 80, 'cicatriz': -80, 'ntinv': 80}[kind]
        rr = {'normal': -280, 'st': -230, 'q': -120, 'cicatriz': -140, 'ntinv': -260}[kind]
        qq = {'normal': 20, 'st': 30, 'q': 150, 'cicatriz': 150, 'ntinv': 20}[kind]
        d += 'L %d %d ' % (X(0.08), base)
        d += 'C %d %d %d %d %d %d ' % (X(0.1), base - 50, X(0.16), base - 50, X(0.18), base)         # P
        d += 'L %d %d ' % (X(0.26), base)
        d += 'L %d %d ' % (X(0.28), base + qq)                                                        # Q
        d += 'L %d %d ' % (X(0.31), base + rr)                                                        # R
        d += 'L %d %d ' % (X(0.34), base + 90)                                                        # S
        d += 'L %d %d ' % (X(0.36), base + st)                                                        # punto J
        d += 'C %d %d %d %d %d %d ' % (X(0.42), base + st, X(0.46), base + t, X(0.52), base + t)     # ST-T
        d += 'C %d %d %d %d %d %d ' % (X(0.58), base + t, X(0.6), base, X(0.64), base)
        d += 'L %d %d ' % (X(1.0), base)
    return d


def ecg(s, x, y, w, h, kind='normal', beats=2, name='!!ECG', color='1E1E1E', grid=True):
    ids = {}
    if grid:
        g = s.group_start(name + ' papel')
        s.shape(x, y, w, h, 'rect', 'FFF5F5', ('E6B0AA', 1.25), False)
        n = int(w / 0.2)
        m = int(h / 0.2)
        lines = ['M %d 0 L %d 1000' % (int(1000 * i / n), int(1000 * i / n)) for i in range(1, n)] + \
                ['M 0 %d L 1000 %d' % (int(1000 * j / m), int(1000 * j / m)) for j in range(1, m)]
        s.free(x, y, w, h, [(p, False, True) for p in lines], None, ('F5B7B1', 0.5))
        ids['papel'] = s.group_end()
    ids['traza'] = s.free(x, y, w, h, [(ecg_path(kind, beats), False, True)], None, (color, 2.5), name=name + ' trazado', W=1000, H=600)
    return ids


def sarcomero_troponina(s, x, y, w, h, name='!!Filamento delgado', nombres=True):
    """filamento delgado: actina (cuentas), tropomiosina y complejo troponina C/T/I (objetos separados)"""
    ids = {}
    g = s.group_start(name)
    n = 16
    for i in range(n):
        for row in (0, 1):
            cx = x + w * (i + 0.5 * row) / n
            cy = y + h * (0.35 + 0.22 * row)
            s.shape(cx, cy, w / n * 1.05, h * 0.26, 'ellipse', shade('85C1E9', 0.4, 0.25), ('2471A3', 0.75), False)
    s.free(x, y + h * 0.3, w, h * 0.45, [(smooth([(i * 60, 300 + (180 if i % 2 else -180)) for i in range(18)], False, 0.8), False, True)],
           None, ('8E44AD', 3.5), name='Tropomiosina', W=1000, H=600)
    ids['g'] = s.group_end()
    tx = x + w * 0.42; ty = y + h * 0.02
    d = h * 0.32
    ids['TnT'] = s.shape(tx, ty + d * 0.65, d * 1.15, d * 0.8, 'ellipse', shade('F39C12', 0.4, 0.25), ('9C640C', 1.25), False, 'TnT', 13, F_HEAD, INK, True,
                         'c', 'm', (0, 0, 0, 0), name='!!Troponina T', fit=False)
    ids['TnC'] = s.shape(tx + d * 0.85, ty, d, d, 'ellipse', shade('58D68D', 0.4, 0.25), ('1E8449', 1.25), False, 'TnC', 13, F_HEAD, INK, True,
                         'c', 'm', (0, 0, 0, 0), name='!!Troponina C', fit=False)
    ids['TnI'] = s.shape(tx + d * 1.55, ty + d * 0.6, d * 1.05, d * 0.85, 'ellipse', shade('EC7063', 0.4, 0.25), ('922B21', 1.25), False, 'TnI', 13, F_HEAD,
                         INK, True, 'c', 'm', (0, 0, 0, 0), name='!!Troponina I', fit=False)
    return ids


# ================================================================ abdomen
def celula_acinar(s, x, y, w, h, name='!!CelulaAcinar', granulos=7, seed=2):
    """célula acinar piramidal: núcleo basal, RER basal, gránulos de zimógeno apicales (objetos separados)"""
    ids = {}
    g = s.group_start(name)
    pts = [(80, 1000), (920, 1000), (700, 60), (300, 60)]
    s.free(x, y, w, h, 'M 60 1000 L 940 1000 C 900 700 780 200 640 40 L 360 40 C 220 200 100 700 60 1000 Z',
           ('lin', [(0, 'FCE4EC'), (100, 'F8BBD0')], 90), ('880E4F', 2.25), SH_I, name='Membrana acinar')
    rer(s, x + w * 0.2, y + h * 0.66, w * 0.6, h * 0.12, color='CE93D8')
    nucleus(s, x + w * 0.36, y + h * 0.78, w * 0.28, name='Núcleo basal')
    ids['g'] = s.group_end()
    random.seed(seed)
    gr = []
    for k in range(granulos):
        gx = x + w * (0.34 + 0.28 * random.random()); gy = y + h * (0.12 + 0.42 * random.random())
        d = w * 0.13
        gr.append(s.shape(gx, gy, d, d, 'ellipse', ('rad', [(0, 'FFF9C4'), (60, 'FBC02D'), (100, 'C49000')], (35, 30)), ('7F6000', 1.0), False,
                          name='!!Zimogeno %d' % (k + 1)))
    ids['gr'] = gr
    return ids


def acino(s, x, y, d, name='!!Acino', n=8):
    """corte de un ácino: células acinares en roseta alrededor de una luz central"""
    g = s.group_start(name)
    cx, cy = x + d / 2, y + d / 2
    for i in range(n):
        a = 2 * math.pi * i / n
        a1 = a - math.pi / n; a2 = a + math.pi / n
        R = d / 2; r = d * 0.12
        pts = [(cx + r * math.cos(a1), cy + r * math.sin(a1)), (cx + R * math.cos(a1), cy + R * math.sin(a1)),
               (cx + R * 1.02 * math.cos(a), cy + R * 1.02 * math.sin(a)), (cx + R * math.cos(a2), cy + R * math.sin(a2)),
               (cx + r * math.cos(a2), cy + r * math.sin(a2))]
        X0 = min(p[0] for p in pts); Y0 = min(p[1] for p in pts); W = max(p[0] for p in pts) - X0; H = max(p[1] for p in pts) - Y0
        dd = 'M ' + ' L '.join('%d %d' % ((p[0] - X0) / W * 1000, (p[1] - Y0) / H * 1000) for p in pts) + ' Z'
        s.free(X0, Y0, W, H, dd, ('rad', [(0, 'FCE4EC'), (100, 'F48FB1')], (50, 50)), ('880E4F', 1.25))
        gx = cx + d * 0.24 * math.cos(a); gy = cy + d * 0.24 * math.sin(a)
        s.shape(gx - d * 0.035, gy - d * 0.035, d * 0.07, d * 0.07, 'ellipse', 'FBC02D', ('7F6000', 0.5), False)
        nx = cx + d * 0.4 * math.cos(a); ny = cy + d * 0.4 * math.sin(a)
        s.shape(nx - d * 0.045, ny - d * 0.045, d * 0.09, d * 0.09, 'ellipse', '7D5BA6', None, False)
    s.shape(cx - d * 0.1, cy - d * 0.1, d * 0.2, d * 0.2, 'ellipse', 'FFF8E1', ('880E4F', 1.0), False)
    return s.group_end()


def arbol_biliar(s, x, y, w, h, name='!!ArbolBiliar', obstr=None):
    """esquema: hígado, conductos hepáticos, vesícula + cístico, colédoco, conducto pancreático, ampolla y duodeno.
    Devuelve dict con ids de cada estructura (objetos separados)."""
    ids = {}
    def P(px, py):
        return (x + w * px / 1000, y + h * py / 1000)
    ids['higado'] = liver(s, x, y, w * 0.66, name='!!Higado')
    dpath = 'M 330 0 C 260 300 280 700 520 860 C 700 980 930 900 990 640'
    ids['duodeno'] = s.free(x + w * 0.36, y + h * 0.56, w * 0.36, h * 0.4, [(dpath, False, True)], None, ('922B21', 30), name='!!Duodeno')
    ids['duo2'] = s.free(x + w * 0.36, y + h * 0.56, w * 0.36, h * 0.4, [(dpath, False, True)], None, ('F1948A', 23), name='!!Duodeno luz')
    ids['pancreas'] = pancreas(s, x + w * 0.47, y + h * 0.53, w * 0.52, name='!!Pancreas')
    ids['vesicula'] = s.free(x + w * 0.16, y + h * 0.43, w * 0.12, h * 0.22, smooth([(300, 0), (800, 80), (950, 600), (600, 1000), (200, 900), (80, 400)]),
                             shade('8DB255', 0.4, 0.3), ('4E6B22', 1.5), name='!!Vesicula')
    def duct(pts, nm, col='1E8449', wd=6):
        return s.arrow([P(*p) for p in pts], col, wd, tail=None, curve=len(pts) in (3, 4), name=nm)
    ids['hepaticos'] = duct([(380, 360), (410, 420), (440, 490)], '!!Conductos hepaticos')
    ids['cistico'] = duct([(270, 520), (360, 520), (440, 500)], '!!Conducto cistico')
    ids['coledoco'] = duct([(440, 490), (450, 640), (470, 790)], '!!Coledoco')
    ids['wirsung'] = duct([(950, 610), (700, 700), (490, 795)], '!!Conducto pancreatico', 'B7950B', 5)
    ap = P(470, 800)
    ids['ampolla'] = s.shape(ap[0] - w * 0.025, ap[1] - w * 0.025, w * 0.05, w * 0.05, 'ellipse', 'F4D03F', ('7D6608', 1.25), False, name='!!Ampolla de Vater')
    return ids


def higado_lobulo(s, x, y, w, h, name='!!Hepatocito'):
    return hepatocyte(s, x, y, w, name=name)
