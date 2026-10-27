# -*- coding: utf-8 -*-
"""Ilustraciones científicas vectoriales (formas nativas editables, sombreado
radial al estilo de la serie). Cada función devuelve el id del grupo."""
from lib import *
from ui import shade, vshade, lighten, darken, mol, label, chip
import math, random


# ---------------------------------------------------------------- utilidades de trazado
def circ(cx, cy, r, ry=None):
    ry = ry or r
    k = 0.5523
    return ('M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z' % (
        cx + r, cy, cx + r, cy + ry * k, cx + r * k, cy + ry, cx, cy + ry,
        cx - r * k, cy + ry, cx - r, cy + ry * k, cx - r, cy,
        cx - r, cy - ry * k, cx - r * k, cy - ry, cx, cy - ry,
        cx + r * k, cy - ry, cx + r, cy - ry * k, cx + r, cy))


def smooth(pts, closed=True, t=1.0):
    """Catmull-Rom -> Bézier cúbicas"""
    n = len(pts)
    d = 'M %d %d ' % pts[0]
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = pts[(i - 1) % n] if (closed or i > 0) else pts[i]
        p1 = pts[i]; p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else pts[(i + 1) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6 * t, p1[1] + (p2[1] - p0[1]) / 6 * t)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6 * t, p2[1] - (p3[1] - p1[1]) / 6 * t)
        d += 'C %d %d %d %d %d %d ' % (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
    return d + ('Z' if closed else '')


def many_circles(lst):
    return ' '.join(circ(*c) for c in lst)


def blob(s, x, y, w, h, pts, fill, line, W=1000, H=1000, name=None, shadow=False, **kw):
    return s.free(x, y, w, h, smooth(pts), fill, line, shadow, name=name, W=W, H=H, **kw)


def strokes(s, x, y, w, h, paths, color, wpt, W=1000, H=1000, name=None, dash=None):
    """varias curvas abiertas como una sola forma (solo trazo)"""
    return s.free(x, y, w, h, [(p, False, True) for p in paths], None, (color, wpt, dash), name=name, W=W, H=H)


# ---------------------------------------------------------------- organelas
def mito(s, x, y, w, h=None, name=None, color='EE9A3A', rot=0):
    h = h or w * 0.5
    g = s.group_start(name or 'Mitocondria')
    s.shape(x, y, w, h, 'ellipse', shade(color, 0.35, 0.3), (darken(color, 0.5), 1.0), False, rot=rot)
    s.shape(x + w * 0.07, y + h * 0.14, w * 0.86, h * 0.72, 'ellipse', lighten(color, 0.62), (darken(color, 0.25), 0.75), False, rot=rot)
    # crestas
    pts = []
    n = 7
    for i in range(n * 2 + 1):
        px = 90 + 820 * i / (n * 2)
        py = 200 if i % 2 == 0 else 800
        pts.append((px, py))
    d = smooth(pts, closed=False, t=0.6)
    s.free(x + w * 0.07, y + h * 0.14, w * 0.86, h * 0.72, [(d, False, True)], None, (darken(color, 0.35), 1.25), rot=rot)
    return s.group_end()


def nucleus(s, x, y, d, name=None, color='7D5BA6'):
    g = s.group_start(name or 'Núcleo')
    s.shape(x, y, d, d * 0.9, 'ellipse', shade(color, 0.45, 0.3), (darken(color, 0.4), 1.0), False)
    s.shape(x + d * 0.52, y + d * 0.3, d * 0.22, d * 0.2, 'ellipse', darken(color, 0.35), None, False)
    return s.group_end()


def rer(s, x, y, w, h, name=None, color='C39BD3'):
    g = s.group_start(name or 'Retículo endoplasmático')
    n = 3
    for i in range(n):
        yy = y + i * h / n
        pts = [(0, 300), (250, 0), (500, 300), (750, 0), (1000, 300), (1000, 700), (750, 1000), (500, 700), (250, 1000), (0, 700)]
        s.free(x, yy, w, h / n * 0.75, smooth(pts, True, 0.5), lighten(color, 0.35), (darken(color, 0.35), 0.75))
        dots = [(int(60 + 880 * k / 11), 120 if k % 2 else 880, 45) for k in range(12)]
        s.free(x, yy - h / n * 0.08, w, h / n * 0.9, many_circles(dots), '5D3A6E', None)
    return s.group_end()


def granule(s, x, y, d, name=None, core='1F4E9A'):
    g = s.group_start(name or 'Gránulo de insulina')
    s.shape(x, y, d, d, 'ellipse', ('rad', [(0, 'FFFFFF'), (100, 'D6E4F5')], (40, 40)), ('5B7DB1', 1.0), False)
    s.shape(x + d * 0.3, y + d * 0.3, d * 0.4, d * 0.4, 'ellipse', shade(core, 0.3, 0.2), None, False)
    return s.group_end()


def glycogen(s, x, y, w, h, n=14, name='Glucógeno', seed=3, color='B03A6E'):
    random.seed(seed)
    cs = []
    for k in range(n):
        cx, cy = random.randint(120, 880), random.randint(120, 880)
        for a in range(6):
            cs.append((int(cx + 70 * math.cos(a)), int(cy + 70 * math.sin(a)), 38))
    return s.free(x, y, w, h, many_circles(cs), color, None, name=name)


def lipid_drops(s, x, y, w, h, lst, name='Gotas lipídicas'):
    return s.free(x, y, w, h, many_circles(lst), ('rad', [(0, 'FFF6C2'), (100, 'E9B90B')], (35, 30)), ('9A7D0A', 0.75), name=name)


# ---------------------------------------------------------------- células
def hepatocyte(s, x, y, w, name='!!Hepatocito', detail=True, color='E8A08A'):
    h = w * 0.82
    g = s.group_start(name)
    pts = [(120, 80), (500, 20), (880, 90), (980, 450), (860, 900), (480, 980), (110, 900), (20, 470)]
    s.free(x, y, w, h, smooth(pts, True, 0.55), shade(color, 0.45, 0.25), (darken(color, 0.55), 2.0), SHD_ILL)
    if detail:
        nucleus(s, x + w * 0.4, y + h * 0.36, w * 0.22, name='Núcleo hepatocito')
        rer(s, x + w * 0.12, y + h * 0.15, w * 0.24, h * 0.22)
        for (mx, my, r) in ((0.66, 0.2, 0), (0.7, 0.62, 25), (0.2, 0.62, -20), (0.45, 0.75, 10)):
            mito(s, x + w * mx, y + h * my, w * 0.16, rot=r)
        glycogen(s, x + w * 0.62, y + h * 0.4, w * 0.22, h * 0.18, 8)
        lipid_drops(s, x + w * 0.15, y + h * 0.38, w * 0.2, h * 0.2, [(300, 300, 160), (700, 650, 120)])
    return s.group_end()


SHD_ILL = (8, 4, 30)


def beta_cell_body(s, x, y, w, h, name='!!Célula beta'):
    """cuerpo de la célula beta (membrana doble) para la secuencia de secreción"""
    g = s.group_start(name)
    s.shape(x, y, w, h, 'roundRect', ('rad', [(0, 'FFF1E8'), (100, 'F9CDB8')], (50, 50)), ('B94A48', 9), SHD_ILL, adj={'adj': 16000})
    s.shape(x + 0.02, y + 0.02, w - 0.04, h - 0.04, 'roundRect', None, ('F5CBA7', 4), False, adj={'adj': 16000})
    nucleus(s, x + w * 0.08, y + h * 0.55, w * 0.18, name='Núcleo')
    rer(s, x + w * 0.3, y + h * 0.66, w * 0.17, h * 0.2)
    return s.group_end()


def adipocyte_white(s, x, y, d, name='!!Adipocito blanco'):
    g = s.group_start(name)
    s.shape(x, y, d, d, 'ellipse', shade('F6D7B0', 0.4, 0.25), ('8C5A2B', 1.75), SHD_ILL)
    s.shape(x + d * 0.05, y + d * 0.05, d * 0.9, d * 0.9, 'ellipse', ('rad', [(0, 'FFF8D0'), (50, 'F7DC6F'), (100, 'D4AC0D')], (35, 30)),
            ('B7950B', 1.0), False, name='Gota lipídica')
    s.shape(x + d * 0.72, y + d * 0.06, d * 0.22, d * 0.12, 'ellipse', shade('7D5BA6', 0.4, 0.3), (darken('7D5BA6', 0.4), 0.75), False, rot=40)
    mito(s, x + d * 0.08, y + d * 0.74, d * 0.1, rot=-40)
    return s.group_end()


def adipocyte_brown(s, x, y, d, name='!!Adipocito marrón'):
    g = s.group_start(name)
    pts = [(150, 120), (500, 30), (860, 130), (970, 500), (850, 880), (480, 970), (120, 860), (30, 480)]
    s.free(x, y, d, d, smooth(pts, True, 0.6), shade('C9715A', 0.45, 0.25), ('6E2C1E', 1.75), SHD_ILL)
    lipid_drops(s, x, y, d, d, [(260, 260, 95), (700, 250, 85), (780, 620, 90), (300, 720, 85), (520, 820, 70), (180, 500, 65), (760, 420, 60)])
    for (mx, my, r) in ((0.35, 0.12, 10), (0.5, 0.3, -30), (0.12, 0.62, 60), (0.58, 0.6, 20), (0.62, 0.84, -10), (0.36, 0.5, 80), (0.8, 0.8, 40)):
        mito(s, x + d * mx, y + d * my, d * 0.16, color='C0581F', rot=r)
    nucleus(s, x + d * 0.4, y + d * 0.38, d * 0.2)
    return s.group_end()


def rbc(s, x, y, d, name='Eritrocito', side=False):
    if side:
        return s.shape(x, y, d, d * 0.42, 'ellipse', vshade('C0392B', 0.3, 0.35), ('7B241C', 0.75), False, name=name)
    return s.shape(x, y, d, d, 'ellipse', ('rad', [(0, 'E06A5F'), (38, 'EF8C80'), (72, 'C9372C'), (100, '7B1F17')], (50, 50)),
                   ('6E1A12', 0.75), False, name=name)


def muscle_fiber(s, x, y, w, h, name='!!Fibra muscular', color='C9483D', nuclei=True):
    g = s.group_start(name)
    s.shape(x, y, w, h, 'roundRect', vshade(color, 0.32, 0.38), (darken(color, 0.55), 1.25), SHD_ILL, adj={'adj': 50000})
    n = max(int(w / 0.09), 4)
    lines = ['M %d 80 L %d 920' % (int(1000 * (i + 0.5) / n), int(1000 * (i + 0.5) / n)) for i in range(n)]
    strokes(s, x + h * 0.25, y, w - h * 0.5, h, lines, darken(color, 0.35), 1.0)
    if nuclei:
        for fx_ in (0.2, 0.55, 0.85):
            s.shape(x + w * fx_, y + h * 0.04, h * 0.5, h * 0.18, 'ellipse', shade('7D5BA6', 0.4, 0.3), None, False)
    s.shape(x + w - h * 0.42, y + h * 0.04, h * 0.4, h * 0.92, 'ellipse', ('rad', [(0, 'F9E79F'), (100, 'E59866')], (50, 50)),
            (darken(color, 0.5), 1.0), False)
    return s.group_end()


def neuron(s, x, y, w, name='!!Neurona', color='8E7CC3'):
    h = w * 0.55
    g = s.group_start(name)
    dk = darken(color, 0.4)
    dend = ['M 280 500 C 200 420 150 300 60 230', 'M 260 470 C 220 380 230 250 200 120', 'M 270 560 C 180 620 120 700 40 780',
            'M 300 600 C 280 700 260 820 230 940', 'M 330 430 C 340 320 380 200 420 80']
    strokes(s, x, y, w, h, dend, dk, 6.5)
    strokes(s, x, y, w, h, dend, color, 4.5)
    ax = ['M 360 520 C 500 520 650 470 900 500']
    strokes(s, x, y, w, h, ax, dk, 7)
    strokes(s, x, y, w, h, ax, lighten(color, 0.2), 5)
    s.free(x, y, w, h, smooth([(230, 430), (330, 380), (400, 470), (380, 600), (280, 640), (210, 560)], True), shade(color, 0.45, 0.25), (dk, 1.5))
    s.free(x, y, w, h, circ(305, 510, 40), darken(color, 0.3), None)
    s.free(x, y, w, h, many_circles([(920, 470, 35), (940, 540, 30), (895, 560, 28)]), shade(color, 0.4, 0.2), (dk, 1.0))
    return s.group_end()


def astrocyte(s, x, y, w, name='!!Astrocito', color='9ACD8C'):
    h = w * 0.8
    g = s.group_start(name)
    dk = darken(color, 0.45)
    pr = ['M 500 500 C 420 380 330 300 180 220', 'M 500 500 C 560 360 600 250 680 120', 'M 500 500 C 650 520 780 480 940 420',
          'M 500 500 C 420 640 330 760 200 900', 'M 500 500 C 600 650 700 760 820 920', 'M 500 500 C 380 520 230 540 60 520']
    strokes(s, x, y, w, h, pr, dk, 8)
    strokes(s, x, y, w, h, pr, color, 6)
    s.free(x, y, w, h, smooth([(420, 420), (520, 380), (610, 460), (590, 580), (480, 620), (400, 540)], True), shade(color, 0.45, 0.25), (dk, 1.5))
    s.free(x, y, w, h, circ(505, 500, 50), shade('5D8A4E', 0.3, 0.3), None)
    return s.group_end()


def enterocyte_row(s, x, y, w, h, n=4, name='!!Epitelio intestinal', color='F5B7A5'):
    g = s.group_start(name)
    cw = w / n
    for i in range(n):
        cx = x + i * cw
        s.shape(cx, y + h * 0.1, cw, h * 0.9, 'rect', shade(color, 0.4, 0.15), (darken(color, 0.5), 1.25), False)
        mv = ['M %d 0 L %d 100' % (int(1000 * (k + 0.5) / 9), int(1000 * (k + 0.5) / 9)) for k in range(9)]
        strokes(s, cx, y, cw, h * 0.1 + 0.01, mv, darken(color, 0.4), 2.25)
        s.shape(cx + cw * 0.32, y + h * 0.66, cw * 0.36, h * 0.2, 'ellipse', shade('7D5BA6', 0.4, 0.3), (darken('7D5BA6', 0.4), 0.75), False)
    return s.group_end()


def tubule_cell(s, x, y, w, h, name='!!Célula del túbulo proximal', color='F3C2A0'):
    g = s.group_start(name)
    s.shape(x, y + h * 0.1, w, h * 0.9, 'roundRect', shade(color, 0.4, 0.2), (darken(color, 0.55), 1.75), SHD_ILL, adj={'adj': 8000})
    n = int(w / 0.09)
    mv = ['M %d 0 L %d 100' % (int(1000 * (k + 0.5) / n), int(1000 * (k + 0.5) / n)) for k in range(n)]
    strokes(s, x, y, w, h * 0.1 + 0.01, mv, darken(color, 0.45), 2.25)
    nucleus(s, x + w * 0.08, y + h * 0.58, w * 0.18)
    for (mx, my, r) in ((0.72, 0.7, 80), (0.82, 0.68, 85), (0.62, 0.72, 95), (0.3, 0.3, 10)):
        mito(s, x + w * mx, y + h * my, w * 0.13, rot=r)
    return s.group_end()


# ---------------------------------------------------------------- membranas y proteínas
def membrane_h(s, x, y, w, h=0.36, name='!!Membrana', head='F1948A', tail='FDEBD0'):
    g = s.group_start(name)
    s.shape(x, y + h * 0.18, w, h * 0.64, 'rect', tail, None, False)
    n = max(int(w / 0.1), 4)
    W = int(w * 1000); H = int(h * 1000)
    r = int(min(W / n / 2 * 0.95, H * 0.2))
    top = [(int(W * (i + 0.5) / n), r, r) for i in range(n)]
    bot = [(int(W * (i + 0.5) / n), H - r, r) for i in range(n)]
    s.free(x, y, w, h, many_circles(top + bot), shade(head, 0.3, 0.2), (darken(head, 0.45), 0.5), W=W, H=H)
    tails = []
    for i in range(n):
        cx = int(W * (i + 0.5) / n)
        tails += ['M %d %d L %d %d' % (cx - r // 3, 2 * r, cx - r // 3, H // 2 - 10), 'M %d %d L %d %d' % (cx + r // 3, 2 * r, cx + r // 3, H // 2 - 10),
                  'M %d %d L %d %d' % (cx - r // 3, H - 2 * r, cx - r // 3, H // 2 + 10), 'M %d %d L %d %d' % (cx + r // 3, H - 2 * r, cx + r // 3, H // 2 + 10)]
    strokes(s, x, y, w, h, tails, darken(tail, 0.35), 0.75, W=W, H=H)
    return s.group_end()


def membrane_v(s, x, y, h, w=0.36, name='!!Membrana', head='F1948A', tail='FDEBD0'):
    g = s.group_start(name)
    s.shape(x + w * 0.18, y, w * 0.64, h, 'rect', tail, None, False)
    n = max(int(h / 0.1), 4)
    W = int(w * 1000); H = int(h * 1000)
    r = int(min(H / n / 2 * 0.95, W * 0.2))
    lft = [(r, int(H * (i + 0.5) / n), r) for i in range(n)]
    rgt = [(W - r, int(H * (i + 0.5) / n), r) for i in range(n)]
    s.free(x, y, w, h, many_circles(lft + rgt), shade(head, 0.3, 0.2), (darken(head, 0.45), 0.5), W=W, H=H)
    return s.group_end()


def glut(s, x, y, h=0.7, name='!!GLUT', color='5DADE2', text='GLUT', open_=True, horizontal=False):
    """transportador (dos lóbulos con poro). x,y = esquina sup. izq.; h = espesor transmembrana"""
    g = s.group_start(name)
    lw = h * 0.36; gap = h * 0.12 if open_ else 0.0
    if not horizontal:
        s.shape(x, y, lw, h, 'roundRect', vshade(color, 0.35, 0.3), (darken(color, 0.5), 1.25), False, adj={'adj': 45000})
        s.shape(x + lw + gap, y, lw, h, 'roundRect', vshade(color, 0.35, 0.3), (darken(color, 0.5), 1.25), False, adj={'adj': 45000})
        if text:
            label(s, x - 0.4, y + h + 0.02, 2 * lw + gap + 0.8, 0.26, text, 11.5, darken(color, 0.55))
    else:
        s.shape(x, y, h, lw, 'roundRect', ('lin', [(0, darken(color, 0.3)), (40, lighten(color, 0.35)), (100, darken(color, 0.3))], 0),
                (darken(color, 0.5), 1.25), False, adj={'adj': 45000})
        s.shape(x, y + lw + gap, h, lw, 'roundRect', ('lin', [(0, darken(color, 0.3)), (40, lighten(color, 0.35)), (100, darken(color, 0.3))], 0),
                (darken(color, 0.5), 1.25), False, adj={'adj': 45000})
        if text:
            label(s, x - 0.1, y - 0.3, h + 0.2, 0.26, text, 11.5, darken(color, 0.55))
    return s.group_end()


def channel(s, x, y, h=0.8, open_=True, name='!!Canal', color='8E44AD', flank='C39BD3', text=None, horizontal=False):
    """canal iónico: poro central (2 hemicanales) + subunidades laterales"""
    g = s.group_start(name)
    fw = h * 0.3; pw = h * 0.26; gap = h * 0.16 if open_ else 0.01
    tot = 2 * fw + 2 * pw + gap
    if not horizontal:
        s.shape(x, y + h * 0.08, fw, h * 0.84, 'roundRect', vshade(flank, 0.3, 0.25), (darken(flank, 0.5), 1.0), False, adj={'adj': 40000})
        s.shape(x + fw, y, pw, h, 'roundRect', vshade(color, 0.35, 0.3), (darken(color, 0.5), 1.25), False, adj={'adj': 40000})
        s.shape(x + fw + pw + gap, y, pw, h, 'roundRect', vshade(color, 0.35, 0.3), (darken(color, 0.5), 1.25), False, adj={'adj': 40000})
        s.shape(x + fw + 2 * pw + gap, y + h * 0.08, fw, h * 0.84, 'roundRect', vshade(flank, 0.3, 0.25), (darken(flank, 0.5), 1.0), False, adj={'adj': 40000})
        if text:
            label(s, x - 0.5, y + h + 0.02, tot + 1.0, 0.28, text, 11.5, darken(color, 0.5))
    else:
        s.shape(x + h * 0.08, y, h * 0.84, fw, 'roundRect', flank, (darken(flank, 0.5), 1.0), False, adj={'adj': 40000})
        s.shape(x, y + fw, h, pw, 'roundRect', color, (darken(color, 0.5), 1.25), False, adj={'adj': 40000})
        s.shape(x, y + fw + pw + gap, h, pw, 'roundRect', color, (darken(color, 0.5), 1.25), False, adj={'adj': 40000})
        s.shape(x + h * 0.08, y + fw + 2 * pw + gap, h * 0.84, fw, 'roundRect', flank, (darken(flank, 0.5), 1.0), False, adj={'adj': 40000})
        if text:
            label(s, x - 0.3, y - 0.32, h + 0.6, 0.28, text, 11.5, darken(color, 0.5))
    return s.group_end()


def insulin_receptor(s, x, y, mh=0.36, scale=1.0, name='!!Receptor de insulina', active=False):
    """receptor tirosina cinasa α2β2; (x,y) = esquina sup. izq. de la membrana en el receptor"""
    k = scale
    g = s.group_start(name)
    col = '5B8DEF'
    # subunidades α (extracelulares)
    for dx, flip in ((0, False), (0.62 * k, True)):
        d = smooth([(100, 900), (60, 450), (250, 80), (520, 60), (700, 300), (560, 520), (520, 900)], True, 0.7)
        s.free(x + dx, y - 1.05 * k, 0.55 * k, 0.95 * k, d, shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), flipH=flip)
    # β transmembrana + dominio cinasa
    for dx in (0.2 * k, 0.72 * k):
        s.shape(x + dx, y - 0.12 * k, 0.16 * k, mh + 0.24 * k, 'roundRect', vshade('2E86C1', 0.3, 0.3), (darken('2E86C1', 0.5), 1.0), False, adj={'adj': 50000})
        s.shape(x + dx - 0.12 * k, y + mh + 0.1 * k, 0.4 * k, 0.75 * k, 'roundRect', shade('85C1E9', 0.35, 0.25), (darken('2E86C1', 0.5), 1.25), False, adj={'adj': 35000})
    s.shape(x + 0.35 * k, y - 0.32 * k, 0.4 * k, 0.1 * k, 'rect', '1B4F72', None, False)  # puentes disulfuro
    return s.group_end()


def gpcr(s, x, y, mh=0.36, scale=1.0, name='!!GPCR', color='7DCEA0', text=None):
    k = scale
    g = s.group_start(name)
    hw = 0.13 * k; gap = 0.035 * k
    for i in range(7):
        s.shape(x + i * (hw + gap), y - 0.1 * k, hw, mh + 0.2 * k, 'roundRect', vshade(color, 0.35, 0.3), (darken(color, 0.5), 1.0), False, adj={'adj': 50000})
    W = 7 * (hw + gap)
    loops = []
    for i in range(6):
        cx = int(1000 * ((i + 0.5) * (hw + gap) + hw / 2) / W) + int(1000 * (hw + gap) / W / 2) - int(1000 * (hw + gap) / W / 2)
        x1 = int(1000 * (i * (hw + gap) + hw / 2) / W); x2 = int(1000 * ((i + 1) * (hw + gap) + hw / 2) / W)
        if i % 2 == 0:
            loops.append('M %d 1190 Q %d 1400 %d 1190' % (x1, (x1 + x2) // 2, x2))
        else:
            loops.append('M %d 210 Q %d 0 %d 210' % (x1, (x1 + x2) // 2, x2))
    strokes(s, x, y - 0.2 * k, W, mh + 0.4 * k, loops, darken(color, 0.5), 1.5, W=1000, H=1400)
    if text:
        label(s, x - 0.3, y - 0.55 * k, W + 0.6, 0.3, text, 12, darken(color, 0.6))
    return s.group_end()


def gprotein(s, x, y, scale=1.0, name='!!Proteína G', alpha_col='F5B041', text='Gs', gtp=True):
    k = scale
    g = s.group_start(name)
    s.shape(x, y, 0.55 * k, 0.45 * k, 'ellipse', shade(alpha_col, 0.4, 0.25), (darken(alpha_col, 0.5), 1.25), False,
            'α' + ('·GTP' if gtp else '·GDP'), 10, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.shape(x + 0.5 * k, y + 0.02 * k, 0.32 * k, 0.32 * k, 'ellipse', shade('AED6F1', 0.4, 0.25), ('2471A3', 1.0), False,
            'β', 11, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.shape(x + 0.76 * k, y + 0.0 * k, 0.2 * k, 0.2 * k, 'ellipse', shade('D2B4DE', 0.4, 0.25), ('6C3483', 1.0), False,
            'γ', 9, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    if text:
        label(s, x - 0.1, y + 0.45 * k, 0.75 * k + 0.2, 0.26, text, 11, darken(alpha_col, 0.6))
    return s.group_end()


def lipoprotein(s, x, y, d, core='F7DC6F', text='QM', apos=(), name=None, tsize=None):
    """apos: lista de (color, ángulo_inicio, extensión, grosor_pt, etiqueta)"""
    g = s.group_start(name or ('!!' + plain(text)))
    s.shape(x, y, d, d, 'ellipse', ('rad', [(0, lighten(core, 0.6)), (70, core), (100, darken(core, 0.2))], (40, 35)), ('8C6D1F', 1.0), SHD_ILL)
    n = max(int(d * 3.14 / 0.07), 12)
    R = 470; r = int(min(28, 1000 * 3.14 / n / 2.2))
    heads = [(int(500 + R * math.cos(2 * math.pi * i / n)), int(500 + R * math.sin(2 * math.pi * i / n)), r) for i in range(n)]
    s.free(x, y, d, d, many_circles(heads), shade('F1948A', 0.3, 0.2), ('922B21', 0.5))
    for (col, a0, ext, wpt, lab) in apos:
        pts = []
        for j in range(9):
            a = math.radians(a0 + ext * j / 8)
            pts.append((int(500 + 500 * math.cos(a)), int(500 + 500 * math.sin(a))))
        s.free(x, y, d, d, [(smooth(pts, False, 1.0), False, True)], None, (col, wpt))
        if lab:
            a = math.radians(a0 + ext / 2)
            lx = x + d / 2 + (d / 2 + 0.22) * math.cos(a); ly = y + d / 2 + (d / 2 + 0.16) * math.sin(a)
            s.text(lx - 0.5, ly - 0.13, 1.0, 0.26, lab, 10.5, F_HEAD, darken(col, 0.3), True, 'c', 'm', minsize=8)
    s.text(x, y + d * 0.3, d, d * 0.4, text, tsize or max(10, min(18, d * 16)), F_HEAD, INK, True, 'c', 'm', minsize=8)
    return s.group_end()


# ---------------------------------------------------------------- órganos
def liver(s, x, y, w, name='!!Hígado', color='B5473A', gall=True):
    h = w * 0.62
    g = s.group_start(name)
    if gall:
        s.free(x + w * 0.27, y + h * 0.78, w * 0.13, h * 0.36, smooth([(300, 0), (950, 60), (800, 800), (450, 1000), (120, 700)], True),
               shade('8DB255', 0.4, 0.3), ('4E6B22', 1.25), name='Vesícula biliar')
    pts = [(40, 250), (120, 110), (300, 50), (520, 55), (720, 75), (900, 120), (975, 190), (940, 250), (820, 300), (690, 370),
           (560, 470), (440, 570), (330, 610), (230, 580), (140, 480), (60, 380)]
    s.free(x, y, w, h, smooth(pts), shade(color, 0.42, 0.3, (30, 25)), (darken(color, 0.55), 2.0), SHD_ILL, W=1000, H=620)
    strokes(s, x, y, w, h, ['M 560 70 C 545 180 530 280 520 400'], darken(color, 0.4), 1.75, W=1000, H=620)
    strokes(s, x, y, w, h, ['M 200 200 C 260 160 330 150 400 170', 'M 640 160 C 700 150 760 160 820 190'], lighten(color, 0.35), 2.5, W=1000, H=620)
    return s.group_end()


def kidney(s, x, y, w, name='!!Riñón', color='B03A2E'):
    h = w * 1.4
    g = s.group_start(name)
    pts = [(350, 30), (520, 60), (640, 200), (680, 400), (660, 620), (580, 820), (420, 960), (250, 960), (140, 860), (110, 700),
           (170, 600), (270, 560), (300, 500), (260, 430), (160, 400), (100, 300), (140, 150), (230, 60)]
    s.free(x, y, w, h, smooth(pts), shade(color, 0.4, 0.3), (darken(color, 0.55), 2.0), SHD_ILL, W=700, H=1000)
    # médula (pirámides)
    pyr = []
    for (cx, cy, a) in ((440, 220, 200), (520, 420, 180), (500, 640, 160), (380, 820, 120)):
        pyr.append('M %d %d L %d %d L %d %d Z' % (cx, cy - 70, cx + 90, cy + 50, cx - 60, cy + 70))
    s.free(x, y, w, h, pyr, darken(color, 0.3), (darken(color, 0.55), 0.75), W=700, H=1000)
    s.free(x, y, w, h, smooth([(300, 470), (380, 380), (420, 500), (380, 620), (300, 560)]), 'F5CBA7', ('A04000', 1.0), W=700, H=1000)
    strokes(s, x, y, w, h, ['M 300 520 C 220 560 200 700 230 1000'], 'E59866', 5, W=700, H=1000)
    return s.group_end()


def pancreas(s, x, y, w, name='!!Páncreas', color='EDB98A'):
    h = w * 0.42
    g = s.group_start(name)
    pts = [(30, 300), (60, 220), (150, 190), (250, 230), (360, 250), (480, 200), (600, 170), (740, 140), (880, 120), (970, 150),
           (960, 220), (860, 250), (740, 280), (620, 320), (500, 370), (380, 400), (250, 410), (120, 390)]
    s.free(x, y, w, h, smooth(pts), shade(color, 0.45, 0.25), (darken(color, 0.5), 1.75), SHD_ILL, W=1000, H=420)
    random.seed(7)
    bumps = []
    for i in range(26):
        t = i / 25
        cx = int(80 + 860 * t); cy = int(300 - 160 * t + random.randint(-25, 25))
        bumps.append((cx, cy, random.randint(18, 30)))
    s.free(x, y, w, h, many_circles(bumps), None, (darken(color, 0.25), 0.75), W=1000, H=420)
    isl = [(260, 300, 26), (520, 260, 22), (760, 200, 24), (420, 320, 18)]
    s.free(x, y, w, h, many_circles(isl), shade('F5B7B1', 0.5, 0.2), ('C0392B', 1.0), W=1000, H=420, name='Islotes')
    strokes(s, x, y, w, h, ['M 100 320 C 300 300 600 230 930 170'], 'F7DC6F', 2.0, W=1000, H=420)
    return s.group_end()


def islet(s, x, y, d, name='!!Islote', seed=5):
    g = s.group_start(name)
    s.shape(x - d * 0.06, y - d * 0.06, d * 1.12, d * 1.12, 'ellipse', ('a', 'F5CBA7', 60), ('B9770E', 1.0, 'dash'), False)
    random.seed(seed)
    cells = []
    R = 430
    for ring, nn in ((0, 1), (130, 7), (260, 12), (380, 17)):
        for i in range(nn):
            a = 2 * math.pi * i / nn + ring
            cells.append((500 + ring * math.cos(a), 500 + ring * math.sin(a)))
    cols = {'b': ('7FB3D5', 'β'), 'a': ('F1948A', 'α'), 'd': ('F7DC6F', 'δ'), 'p': ('C39BD3', 'PP')}
    kinds = []
    for i, (cx, cy) in enumerate(cells):
        r = random.random()
        kinds.append('a' if r < 0.3 else ('d' if r < 0.38 else ('p' if r < 0.41 else 'b')))
    for (cx, cy), kd in zip(cells, kinds):
        col, t = cols[kd]
        rr = 62
        s.shape(x + d * (cx - rr) / 1000, y + d * (cy - rr) / 1000, d * 2 * rr / 1000, d * 2 * rr / 1000, 'ellipse',
                shade(col, 0.4, 0.25), (darken(col, 0.5), 0.75), False, t, max(7, d * 9), F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    strokes(s, x, y, d, d, ['M 0 620 C 250 560 420 700 600 600 C 760 520 880 560 1000 520'], 'C0392B', 3.0)
    return s.group_end()


def brain(s, x, y, w, name='!!Cerebro', color='F1A7B5'):
    h = w * 0.78
    g = s.group_start(name)
    s.free(x, y, w, h, circ(720, 640, 150, 95), shade('E8919F', 0.35, 0.3), (darken(color, 0.55), 1.5), W=1000, H=780, name='Cerebelo')
    strokes(s, x, y, w, h, ['M 600 610 C 610 680 620 730 640 780'], darken(color, 0.5), 9, W=1000, H=780)
    pts = [(100, 520), (70, 380), (130, 230), (260, 120), (430, 70), (600, 70), (760, 120), (890, 220), (950, 360), (930, 480),
           (860, 560), (760, 600), (640, 620), (540, 640), (440, 660), (320, 650), (200, 610)]
    s.free(x, y, w, h, smooth(pts), shade(color, 0.4, 0.25), (darken(color, 0.55), 2.0), SHD_ILL, W=1000, H=780)
    gy = ['M 180 300 C 260 260 280 360 360 320 C 430 280 420 200 500 190', 'M 560 160 C 620 230 700 200 760 260 C 820 320 800 380 870 400',
          'M 150 460 C 240 430 300 500 380 470 C 460 440 500 520 580 500', 'M 420 330 C 480 380 560 330 620 380 C 680 430 740 400 800 470',
          'M 300 560 C 380 540 420 600 500 580', 'M 640 520 C 700 500 760 540 820 520']
    strokes(s, x, y, w, h, gy, darken(color, 0.4), 1.75, W=1000, H=780)
    return s.group_end()


def heart(s, x, y, w, name='!!Corazón', color='C0392B'):
    h = w * 1.05
    g = s.group_start(name)
    pts = [(450, 230), (560, 110), (720, 70), (860, 170), (900, 360), (800, 570), (620, 770), (450, 950), (290, 770), (110, 570),
           (10, 360), (50, 170), (190, 70), (340, 110)]
    s.free(x, y, w, h, smooth(pts), shade(color, 0.42, 0.3), (darken(color, 0.55), 2.0), SHD_ILL, W=900, H=1000)
    strokes(s, x, y, w, h, ['M 450 260 C 470 420 500 600 470 860'], darken(color, 0.4), 2.0, W=900, H=1000)
    return s.group_end()


def intestine(s, x, y, w, name='!!Intestino', color='F0A39B'):
    h = w * 0.85
    g = s.group_start(name)
    colon = 'M 140 900 L 120 220 C 120 120 200 90 300 90 L 720 90 C 820 90 880 130 880 230 L 880 900'
    strokes(s, x, y, w, h, [colon], '7E3F2A', 26, W=1000, H=1000)
    strokes(s, x, y, w, h, [colon], 'D4876B', 21, W=1000, H=1000)
    loops = 'M 300 280 C 420 200 560 360 680 280 C 760 230 760 380 660 400 C 520 430 420 330 300 420 C 220 480 260 560 360 540 C 480 510 580 600 700 540 C 780 500 790 650 680 680 C 540 720 420 640 320 700 C 240 750 300 840 420 820'
    strokes(s, x, y, w, h, [loops], '8E3B32', 22, W=1000, H=1000)
    strokes(s, x, y, w, h, [loops], color, 17, W=1000, H=1000)
    strokes(s, x, y, w, h, [loops], lighten(color, 0.5), 3, W=1000, H=1000)
    return s.group_end()


def stomach(s, x, y, w, name='!!Estómago', color='F1948A'):
    h = w * 1.1
    g = s.group_start(name)
    pts = [(250, 40), (420, 60), (520, 200), (700, 260), (900, 420), (900, 650), (720, 850), (480, 930), (300, 900), (420, 760),
           (560, 640), (560, 480), (380, 400), (240, 260)]
    s.free(x, y, w, h, smooth(pts), shade(color, 0.4, 0.25), (darken(color, 0.55), 1.75), SHD_ILL, W=1000, H=1000)
    return s.group_end()


def adipose_tissue(s, x, y, w, name='!!Tejido adiposo'):
    g = s.group_start(name)
    d = w / 2.6
    for (dx, dy) in ((0, 0.25), (0.82, 0), (1.62, 0.3), (0.45, 0.95), (1.25, 0.9)):
        adipocyte_white(s, x + dx * d, y + dy * d, d * 0.98, name='Adipocito')
    return s.group_end()


def muscle(s, x, y, w, name='!!Músculo', fibers=3):
    g = s.group_start(name)
    fh = w * 0.16
    for i in range(fibers):
        muscle_fiber(s, x + i * w * 0.04, y + i * fh * 1.05, w * (1 - 0.04 * (fibers - 1)), fh, name='Fibra')
    return s.group_end()


def vessel(s, x, y, w, h, name='!!Vaso sanguíneo', rbcs=6, seed=2, label_txt=None):
    g = s.group_start(name)
    s.shape(x, y, w, h, 'roundRect', vshade('C0392B', 0.3, 0.35), ('6E1A12', 1.25), SHD_ILL, adj={'adj': 50000})
    s.shape(x + h * 0.15, y + h * 0.18, w - h * 0.3, h * 0.64, 'roundRect', ('lin', [(0, 'F2B8B0'), (50, 'F8D3CD'), (100, 'EBA59C')], 90),
            ('A93226', 0.75), False, adj={'adj': 50000})
    random.seed(seed)
    for i in range(rbcs):
        rx = x + h * 0.3 + (w - h * 0.8) * (i + random.random() * 0.4) / max(rbcs, 1)
        ry = y + h * 0.25 + random.random() * h * 0.25
        rbc(s, rx, ry, h * 0.42, name='Eritrocito')
    if label_txt:
        label(s, x, y + h * 0.18, w, h * 0.64, label_txt, 12, '6E1A12')
    return s.group_end()


def person(s, x, y, h, name='!!Paciente', color='5D6D7E', fill='AEB6BF'):
    w = h * 0.8
    g = s.group_start(name)
    s.shape(x + w * 0.3, y, w * 0.4, w * 0.4, 'ellipse', shade(fill, 0.4, 0.2), (color, 1.5), False)
    s.free(x, y + w * 0.42, w, h - w * 0.42, smooth([(60, 1000), (60, 450), (200, 120), (500, 40), (800, 120), (940, 450), (940, 1000)], False),
           shade(fill, 0.4, 0.2), (color, 1.5))
    return s.group_end()


def human(s, x, y, h, name='!!Organismo', fill='F8D5C2', line='A0522D'):
    """silueta humana translúcida"""
    w = h * 0.5
    g = s.group_start(name)
    body = [(225, 150), (275, 150), (290, 170), (370, 190), (405, 230), (420, 330), (432, 450), (440, 540), (412, 548), (395, 455),
            (378, 340), (365, 330), (360, 470), (350, 545), (355, 700), (342, 860), (340, 960), (292, 972), (282, 860), (270, 690),
            (250, 600), (230, 690), (218, 860), (208, 972), (160, 960), (158, 860), (145, 700), (150, 545), (140, 470), (135, 330),
            (122, 340), (105, 455), (88, 548), (60, 540), (68, 450), (80, 330), (95, 230), (130, 190), (210, 170)]
    s.free(x, y, w, h, smooth(body, True, 0.45), ('a', fill, 70), (line, 1.75), False, W=500, H=1000)
    s.free(x, y, w, h, circ(250, 85, 62, 70), ('a', fill, 70), (line, 1.75), False, W=500, H=1000)
    return s.group_end()


def clock(s, x, y, d, hours=3, name='Reloj', color=INK):
    g = s.group_start(name)
    s.shape(x, y, d, d, 'ellipse', shade('FFFFFF', 0.0, 0.08), (color, 2.0), False)
    a = math.radians(hours * 30 - 90)
    s.arrow([(x + d / 2, y + d / 2), (x + d / 2 + d * 0.28 * math.cos(a), y + d / 2 + d * 0.28 * math.sin(a))], color, 2.5, tail=None)
    s.arrow([(x + d / 2, y + d / 2), (x + d / 2, y + d * 0.12)], color, 1.75, tail=None)
    return s.group_end()


def flame(s, x, y, w, name='Calor'):
    h = w * 1.3
    return s.free(x, y, w, h, smooth([(500, 0), (750, 300), (900, 650), (700, 980), (300, 980), (100, 650), (300, 420), (420, 520)], True),
                  ('lin', [(0, 'FFE066'), (60, 'F39C12'), (100, 'E74C3C')], 270), ('A04000', 1.25), name=name)


def tank(s, x, y, w, h, level=0.55, name='!!Glucemia (pool)'):
    """pool plasmático: tanque con nivel"""
    g = s.group_start(name)
    s.shape(x, y, w, h, 'rect', ('a', 'FFFFFF', 45), (INK, 2.0), False)
    s.shape(x + 0.03, y + h * (1 - level), w - 0.06, h * level - 0.03, 'rect', ('lin', [(0, '85C1E9'), (100, '2E86C1')], 90), None, False)
    return s.group_end()


def artery_wall(s, x, y, w, h, name='!!Pared arterial'):
    """corte longitudinal: luz / endotelio / íntima / media (músculo liso) / adventicia"""
    g = s.group_start(name)
    lum = h * 0.3
    s.shape(x, y, w, lum, 'rect', ('lin', [(0, 'F5B7B1'), (100, 'E6B0AA')], 90), None, False, name='Luz arterial')
    n = int(w / 0.75)
    for i in range(n):
        s.shape(x + i * w / n, y + lum, w / n, h * 0.06, 'roundRect', shade('F8C471', 0.4, 0.2), ('9C640C', 0.75), False, adj={'adj': 50000})
    s.shape(x, y + lum + h * 0.06, w, h * 0.24, 'rect', ('lin', [(0, 'FDEBD0'), (100, 'FAD7A0')], 90), ('B9770E', 0.75), False, name='Íntima')
    s.shape(x, y + lum + h * 0.3, w, h * 0.26, 'rect', 'E59866', ('873600', 0.75), False, name='Media')
    m = int(w / 0.9)
    for i in range(m):
        for j in range(2):
            s.shape(x + i * w / m + (0.3 if j else 0), y + lum + h * 0.33 + j * h * 0.11, w / m * 0.9, h * 0.08, 'ellipse',
                    vshade('E8836B', 0.3, 0.3), ('873600', 0.5), False)
    s.shape(x, y + lum + h * 0.56, w, h * 0.14, 'rect', ('lin', [(0, 'F6DDCC'), (100, 'EDBB99')], 90), ('873600', 0.75), False, name='Adventicia')
    return s.group_end()
