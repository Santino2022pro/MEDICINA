# -*- coding: utf-8 -*-
"""Tórax paramétrico (vista frontal, coronal esquemática).

Un único modelo anatómico que se redibuja con distinto ESTADO (derrame,
aire pleural, colapso, desplazamiento mediastínico, cúpula aplanada,
compresión de cavas) conservando los MISMOS nombres de objeto («!!»):
así Morph interpola entre diapositivas consecutivas sin reconstruir la
anatomía. Convención radiológica: el lado DERECHO del paciente se dibuja
a la IZQUIERDA de la imagen.

Coordenadas locales 0..1000 × 0..1000 escaladas al rectángulo (X, Y, W, H).
"""
from lib import *
from ui import *
from shapely.geometry import Polygon, LineString, Point, box as sbox, MultiPolygon
from shapely.ops import unary_union
import math

GLOW = ('<a:effectLst><a:glow rad="139700"><a:srgbClr val="FFFF00"><a:alpha val="70000"/></a:srgbClr></a:glow></a:effectLst>')
GLOW_R = ('<a:effectLst><a:glow rad="114300"><a:srgbClr val="FF0000"><a:alpha val="55000"/></a:srgbClr></a:glow></a:effectLst>')
SOFT = ('<a:effectLst><a:outerShdw blurRad="76200" dist="38100" dir="2700000" algn="tl" rotWithShape="0">'
        '<a:srgbClr val="000000"><a:alpha val="30000"/></a:srgbClr></a:outerShdw></a:effectLst>')


# ---------------------------------------------------------------- curvas
def catmull(pts, closed=True, n=7):
    """muestrea una curva Catmull-Rom (para geometría con shapely)"""
    out = []
    N = len(pts)
    rng = range(N) if closed else range(N - 1)
    for i in rng:
        p0 = pts[(i - 1) % N] if (closed or i > 0) else pts[i]
        p1 = pts[i]; p2 = pts[(i + 1) % N]
        p3 = pts[(i + 2) % N] if (closed or i + 2 < N) else p2
        for k in range(n):
            t = k / n; t2 = t * t; t3 = t2 * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    if not closed:
        out.append(pts[-1])
    return out


def biggest(g):
    if g is None or g.is_empty:
        return None
    if isinstance(g, MultiPolygon) or g.geom_type == 'GeometryCollection':
        ps = [x for x in getattr(g, 'geoms', []) if x.geom_type == 'Polygon']
        return max(ps, key=lambda p: p.area) if ps else None
    return g if g.geom_type == 'Polygon' else None


def polys(g, min_area=40):
    if g is None or g.is_empty:
        return []
    if g.geom_type == 'Polygon':
        return [g] if g.area >= min_area else []
    return [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon' and p.area >= min_area]


class Frame:
    """transforma coordenadas locales (0..1000) a pulgadas"""
    def __init__(self, X, Y, W, H):
        self.X, self.Y, self.W, self.H = X, Y, W, H

    def p(self, x, y):
        return (self.X + x / 1000 * self.W, self.Y + y / 1000 * self.H)

    def sx(self, v):
        return v / 1000 * self.W

    def sy(self, v):
        return v / 1000 * self.H


def draw_poly(s, F, geom, fill, line=None, name=None, shadow=False, holes=True, smooth_pts=False):
    """dibuja un Polygon/MultiPolygon de shapely como UNA forma libre (varios subtrazados)"""
    ps = polys(geom, 1)
    if not ps:
        return None
    allx = []; ally = []
    for p in ps:
        xs, ys = p.exterior.xy
        allx += list(xs); ally += list(ys)
    x0, x1, y0, y1 = min(allx), max(allx), min(ally), max(ally)
    bw = max(x1 - x0, 1); bh = max(y1 - y0, 1)
    PW, PH = 10000, int(10000 * bh / bw) if bw >= bh else 10000
    if bh > bw:
        PW = int(10000 * bw / bh)
    def ring(coords):
        c = list(coords)
        d = 'M %d %d ' % ((c[0][0] - x0) / bw * PW, (c[0][1] - y0) / bh * PH)
        d += ' '.join('L %d %d' % ((x - x0) / bw * PW, (y - y0) / bh * PH) for x, y in c[1:])
        return d + ' Z'
    d = ' '.join(ring(p.exterior.coords) + (' ' + ' '.join(ring(h.coords) for h in p.interiors) if holes else '') for p in ps)
    X, Y = F.p(x0, y0)
    return s.free(X, Y, F.sx(bw), F.sy(bh), d, fill, line, shadow, name=name, W=PW, H=PH)


def draw_lines(s, F, lines, color, wpt, name=None, dash=None, shadow=False):
    """varias polilíneas (coordenadas locales) como un único trazo"""
    lines = [l for l in lines if len(l) >= 2]
    if not lines:
        return None
    allx = [p[0] for l in lines for p in l]; ally = [p[1] for l in lines for p in l]
    x0, x1, y0, y1 = min(allx), max(allx), min(ally), max(ally)
    bw = max(x1 - x0, 1); bh = max(y1 - y0, 1)
    PW, PH = int(bw * 10), int(bh * 10)
    paths = []
    for l in lines:
        d = 'M %d %d ' % ((l[0][0] - x0) * 10, (l[0][1] - y0) * 10) + ' '.join('L %d %d' % ((x - x0) * 10, (y - y0) * 10) for x, y in l[1:])
        paths.append((d, False, True))
    X, Y = F.p(x0, y0)
    return s.free(X, Y, F.sx(bw), F.sy(bh), paths, None, (color, wpt, dash), shadow, name=name, W=PW, H=PH)


def geom_lines(g):
    if g is None or g.is_empty:
        return []
    if g.geom_type == 'LineString':
        return [list(g.coords)]
    return [list(x.coords) for x in getattr(g, 'geoms', []) if x.geom_type == 'LineString']


def ring_line(p):
    return [list(p.exterior.coords)]


# ---------------------------------------------------------------- geometría base del tórax
CAV_R = [(318, 128), (262, 150), (212, 196), (172, 262), (142, 345), (124, 440), (116, 540), (116, 640), (124, 735),
         (136, 812), (150, 872), (168, 872), (214, 818), (286, 772), (356, 764), (416, 786), (452, 812),
         (448, 700), (440, 590), (432, 480), (420, 370), (400, 262), (374, 182), (350, 140)]
MED_R = set(range(16, 24))      # índices del borde mediastínico (se desplazan con el mediastino)
DOME_R = [11, 12, 13, 14, 15]   # cúpula diafragmática
HIL_R = (395, 455)


def cav_left():
    pts = []
    for i, (x, y) in enumerate(CAV_R):
        X = 1000 - x
        Yy = y + (24 if i in DOME_R or i in (9, 10, 16) else 0)
        if i in (16, 17, 18):        # escotadura cardíaca
            X += {16: 70, 17: 58, 18: 30}[i]
        pts.append((X, Yy))
    return pts


CAV_L = cav_left()
HIL_L = (605, 455)

WALL = [(500, 40), (330, 70), (190, 120), (110, 190), (70, 300), (48, 450), (42, 600), (50, 760), (70, 890), (110, 975),
        (500, 1000), (890, 975), (930, 890), (950, 760), (958, 600), (952, 450), (930, 300), (890, 190), (810, 120), (670, 70)]


def side_pts(side, st):
    """contorno de la cavidad pleural (pleura parietal) de un lado según el estado"""
    base = CAV_R if side == 'R' else CAV_L
    shift = st.get('shift', 0)
    flat = st.get('flat' + side, 0)       # 0..1 aplanamiento / inversión de la cúpula
    widen = st.get('widen' + side, 0)     # 0..1 aumento de volumen del hemitórax
    out = []
    for i, (x, y) in enumerate(base):
        if i in MED_R:
            # el borde mediastínico sigue al mediastino (más abajo, más desplazamiento)
            k = 0.35 + 0.65 * min(1, max(0, (y - 150) / 600))
            x += shift * k
        if i in DOME_R:
            y += flat * (95 if i in (12, 13, 14) else 55)
        if widen:
            cx = 280 if side == 'R' else 720
            if i not in MED_R:
                x = cx + (x - cx) * (1 + 0.07 * widen)
        out.append((x, y))
    return out


def hilum(side, st):
    h = HIL_R if side == 'R' else HIL_L
    return (h[0] + st.get('shift', 0) * 0.7, h[1])


def meniscus_poly(side, cav, level, curv):
    """región por debajo de la curva de Damoiseau (cóncava hacia arriba, más alta lateralmente)"""
    xs = [p[0] for p in cav]
    xl, xm = (min(xs), max(xs)) if side == 'R' else (max(xs), min(xs))
    pts = []
    for k in range(41):
        x = xl + (xm - xl) * k / 40
        t = 1 - k / 40                  # 1 en la pared lateral
        y = level - curv * (t ** 2.2)
        pts.append((x, y))
    pts += [(xm, 1100), (xl, 1100)]
    return Polygon(pts).buffer(0)


def lung_geom(side, st, cav):
    """pulmón según estado: compresión por líquido (f) y retracción hacia el hilio por aire (c)"""
    P = biggest(Polygon(catmull(cav, True, 6)).buffer(0).buffer(-11, join_style=1))
    f = st.get('fluid' + side, 0); c = st.get('air' + side, 0)
    hx, hy = hilum(side, st)
    top = P.bounds[1]
    bottom = P.bounds[3]
    coords = list(P.exterior.coords)
    def tf(x, y):
        if f > 0:
            lvl = fluid_level(side, st, cav)
            ky = max(0.12, (lvl + 18 - top) / (bottom - top))
            ky = min(1, ky)
            y = top + (y - top) * ky
            x = hx + (x - hx) * (1 - 0.35 * f)
        if c > 0:
            ax, ay = hx, hy + 30
            k = 1 - 0.8 * c
            x = ax + (x - ax) * k
            y = ay + (y - ay) * k
            y -= 30 * c * 0.3
        return x, y
    L = Polygon([tf(x, y) for x, y in coords])
    if not L.is_valid:
        L = L.buffer(0)
    return L, tf


def fluid_level(side, st, cav):
    f = st.get('fluid' + side, 0)
    ys = [p[1] for p in cav]
    top, bot = min(ys), max(ys)
    return bot - 25 - f * (bot - top - 60)


# ramas vasculares/bronquiales del pulmón derecho (se reflejan para el izquierdo)
VESS_R = [[(395, 455), (330, 420), (250, 360), (205, 300)], [(330, 420), (300, 330), (285, 230)], [(395, 455), (300, 470), (200, 470), (150, 480)],
          [(300, 470), (230, 540), (175, 600)], [(395, 455), (330, 540), (270, 640), (215, 720)], [(330, 540), (360, 640), (330, 730)],
          [(270, 640), (190, 690), (150, 720)], [(250, 360), (180, 380), (140, 410)], [(300, 330), (240, 270)], [(230, 540), (240, 610), (210, 680)],
          [(395, 455), (380, 380), (350, 300), (330, 210)], [(200, 470), (170, 530)]]
FISS_R = [[(118, 470), (220, 478), (300, 470), (400, 455)], [(140, 760), (230, 650), (320, 540), (400, 470)]]
FISS_L = [[(866, 760), (770, 640), (680, 530), (608, 470)]]


def mirror(lines):
    return [[(1000 - x, y) for x, y in l] for l in lines]


def chest(s, X, Y, W, H, st=None, names=True, labels=False):
    """dibuja el tórax completo. st (todas las claves son opcionales):
    fluidR/fluidL 0..1 derrame · airR/airL 0..1 neumotórax · shift (+ = hacia la izquierda del paciente)
    flatR/flatL 0..1 cúpula aplanada · widenR · pus/exud/blood (color del líquido) · hydroR (nivel hidroaéreo)
    cava 0..1 compresión de cavas · heart 0..1 reducción de llenado · hl: conjunto de nombres a resaltar
    show: conjunto de capas (por defecto todas) · bubbles: burbujas en el aire."""
    st = st or {}
    F = Frame(X, Y, W, H)
    hl = st.get('hl', set())
    ids = {}
    def nm(n):
        return ('!!' + n) if names else n
    def eff(n, default=False):
        return GLOW if n in hl else default
    shift = st.get('shift', 0)
    cavR = side_pts('R', st); cavL = side_pts('L', st)
    PR = Polygon(catmull(cavR, True, 6)).buffer(0); PL = Polygon(catmull(cavL, True, 6)).buffer(0)
    wall = Polygon(catmull(WALL, True, 6))
    # pared torácica (partes blandas)
    ids['wall'] = draw_poly(s, F, wall, shade(C_SKIN, 0.35, 0.18, (50, 40)), (darken(C_SKIN, 0.55), 2), nm('ParedToracica'), SOFT)
    # mediastino
    inner = wall.buffer(-38)
    med = biggest(inner.difference(PR.buffer(4)).difference(PL.buffer(4)).intersection(sbox(330, 95, 670, 830)))
    ids['med'] = draw_poly(s, F, med, ('lin', [(0, 'F6E3DA'), (100, 'E9C9BD')], 90), (darken('E9C9BD', 0.4), 1), nm('Mediastino'))
    # costillas (detrás de los pulmones)
    ribs = []
    for k in range(9):
        y0 = 150 + k * 78
        for sgn in (-1, 1):
            cx = 500
            pts = [(cx + sgn * 30, y0), (cx + sgn * 150, y0 - 30 + k * 2), (cx + sgn * 300, y0 + 10), (cx + sgn * 410, y0 + 90),
                   (cx + sgn * 440, y0 + 170)]
            if shift and ((sgn < 0 and st.get('widenR')) or (sgn > 0 and st.get('widenL'))):
                pts = [(cx + (x - cx) * 1.05, y) for x, y in pts]
            ribs.append(catmull(pts, False, 6))
    g = s.group_start(nm('Costillas'))
    draw_lines(s, F, ribs, darken(C_BONE, 0.45), 11)
    draw_lines(s, F, ribs, C_BONE, 7.5)
    ids['ribs'] = s.group_end()
    # cavidades (espacio pleural visible como fondo pálido)
    ids['cavR'] = draw_poly(s, F, PR, ('a', 'EAF6FB', 85), None, nm('EspacioPleuralD'))
    ids['cavL'] = draw_poly(s, F, PL, ('a', 'EAF6FB', 85), None, nm('EspacioPleuralI'))
    # aorta (detrás del corazón)
    ao = [(530 + shift, 560), (522 + shift, 330), (560 + shift, 268), (612 + shift, 300), (606 + shift * 0.9, 420), (600 + shift * 0.7, 870)]
    ids['aorta'] = draw_poly(s, F, LineString(catmull(ao, False, 6)).buffer(19, cap_style=1), vshade(C_ART, 0.3, 0.3, 0), (darken(C_ART, 0.5), 1.25), nm('Aorta'))
    # tráquea y bronquios principales (desviación: la parte inferior sigue al mediastino)
    tr = [(500 + shift * 0.15, 40), (500 + shift * 0.45, 200), (500 + shift * 0.75, 340)]
    br = [[tr[-1], (452 + shift * 0.7, 395), hilum('R', st)], [tr[-1], (548 + shift * 0.7, 395), hilum('L', st)]]
    tg = unary_union([LineString(catmull(tr, False, 6)).buffer(22, cap_style=2)] + [LineString(b).buffer(14, cap_style=1) for b in br])
    g = s.group_start(nm('Traquea'))
    draw_poly(s, F, tg, vshade('D9E4EE', 0.4, 0.25, 0), ('5D7486', 1.5))
    rings = []
    for k in range(8):
        t = k / 8
        cx = 500 + shift * (0.15 + 0.6 * t); cy = 70 + t * 250
        rings.append([(cx - 18, cy), (cx + 18, cy)])
    draw_lines(s, F, rings, '8FA6B8', 2)
    ids['trachea'] = s.group_end()
    # pulmones
    LR, tfR = lung_geom('R', st, cavR); LL, tfL = lung_geom('L', st, cavL)
    LR = LR.intersection(PR.buffer(-3)); LL = LL.intersection(PL.buffer(-3))
    LR = biggest(LR) or LR; LL = biggest(LL) or LL
    # líquido / aire
    fill_fl = (('rad', [(0, 'E8C9C0'), (100, C_BLOOD)], (40, 20)) if st.get('blood') else
               ('a', C_PUS, 92) if st.get('pus') else ('a', C_EXUD, 88) if st.get('exud') else ('a', C_FLUID, 88))
    lfl = darken(C_PUS if st.get('pus') else C_EXUD if st.get('exud') else C_BLOOD if st.get('blood') else C_FLUID, 0.45)
    for side, P, L, cav in (('R', PR, LR, cavR), ('L', PL, LL, cavL)):
        f = st.get('fluid' + side, 0); a = st.get('air' + side, 0)
        D = 'D' if side == 'R' else 'I'
        if f > 0:
            lvl = fluid_level(side, st, cav)
            if st.get('hydro' + side):
                region = P.intersection(sbox(0, lvl, 1000, 1100))
            else:
                region = P.intersection(meniscus_poly(side, cav, lvl, min(110, 40 + 260 * f)))
            region = region.difference(L.buffer(2))
            ids['fluid' + side] = draw_poly(s, F, region, fill_fl, (lfl, 1.75), nm('LiquidoPleural' + D), eff('LiquidoPleural' + D))
            if st.get('septa') and side == 'R':
                b = region.bounds
                sl = []
                for k in range(5):
                    x = b[0] + (b[2] - b[0]) * (k + 0.7) / 5.5
                    ln = LineString([(x, b[1]), (x + 25, (b[1] + b[3]) / 2), (x - 15, b[3])]).intersection(region)
                    sl += geom_lines(ln)
                ids['septa'] = draw_lines(s, F, sl, 'FBF3D5', 4, nm('Tabiques'))
        if a > 0:
            region = P.difference(L.buffer(2))
            if f > 0:
                region = region.difference(P.intersection(sbox(0, fluid_level(side, st, cav) - 1, 1000, 1100)))
            ids['air' + side] = draw_poly(s, F, region, ('a', C_AIR, 92), ('7FB3D5', 1.5, 'dash'), nm('AirePleural' + D), eff('AirePleural' + D))
    # pulmones (parénquima + vasos + cisuras) — pleura visceral = contorno del pulmón
    for side, L, tf, D in (('R', LR, tfR, 'D'), ('L', LL, tfL, 'I')):
        col = st.get('lungcol' + side, C_LUNG)
        g = s.group_start(nm('Pulmon' + ('Derecho' if side == 'R' else 'Izquierdo')))
        draw_poly(s, F, L, shade(col, 0.45, 0.22, (40, 30)), None, None, SOFT)
        vs = VESS_R if side == 'R' else mirror(VESS_R)
        vl = []
        for v in vs:
            ln = LineString([tf(x, y) for x, y in v]).intersection(L.buffer(-6))
            vl += geom_lines(ln)
        draw_lines(s, F, vl, darken(col, 0.35), 2.25)
        fs = FISS_R if side == 'R' else FISS_L
        fl = []
        for v in fs:
            fl += geom_lines(LineString([tf(x, y) for x, y in catmull(v, False, 5)]).intersection(L.buffer(-2)))
        draw_lines(s, F, fl, darken(col, 0.5), 1.5, dash='dash')
        ids['lung' + side] = s.group_end()
        ids['visc' + side] = draw_lines(s, F, ring_line(L), C_VISCERAL, 3.5 if 'PleuraVisceral' + D in hl else 2.5,
                                        nm('PleuraVisceral' + D), shadow=eff('PleuraVisceral' + D))
    for side, P, D in (('R', PR, 'D'), ('L', PL, 'I')):
        ids['par' + side] = draw_lines(s, F, ring_line(P), C_PARIETAL, 4 if 'PleuraParietal' + D in hl else 3,
                                       nm('PleuraParietal' + D), shadow=eff('PleuraParietal' + D))
    # venas cavas y corazón
    cz = st.get('cava', 0)
    wS = 17 * (1 - 0.55 * cz); wI = 20 * (1 - 0.55 * cz)
    svc = LineString([(458 + shift * 0.55, 215), (462 + shift * 0.75, 400), (468 + shift, 560)]).buffer(wS, cap_style=2)
    ivc = LineString([(470 + shift * 0.6, 930), (472 + shift * 0.8, 860), (474 + shift, 770)]).buffer(wI, cap_style=2)
    ids['svc'] = draw_poly(s, F, svc, vshade(C_VEN, 0.35, 0.3, 0), (darken(C_VEN, 0.5), 1.25), nm('VenaCavaSup'), eff('VenaCavaSup'))
    ids['ivc'] = draw_poly(s, F, ivc, vshade(C_VEN, 0.35, 0.3, 0), (darken(C_VEN, 0.5), 1.25), nm('VenaCavaInf'), eff('VenaCavaInf'))
    hk = 1 - 0.18 * st.get('heart', 0)
    hc = (545 + shift, 660)
    hp = [(470, 560), (520, 528), (590, 540), (650, 575), (695, 640), (712, 720), (690, 790), (625, 810), (540, 800), (472, 772), (448, 700), (450, 620)]
    hp = [(hc[0] + (x - 545) * hk, hc[1] + (y - 660) * hk) for x, y in hp]
    g = s.group_start(nm('Corazon'))
    draw_poly(s, F, Polygon(catmull(hp, True, 6)), shade('C0392B', 0.4, 0.3, (35, 30)), (darken('C0392B', 0.55), 1.75), None, eff('Corazon', SOFT))
    sulc = [[(hc[0] + (x - 545) * hk, hc[1] + (y - 660) * hk) for x, y in catmull([(600, 548), (585, 640), (610, 740), (650, 800)], False, 5)]]
    draw_lines(s, F, sulc, darken('C0392B', 0.5), 1.5)
    ids['heart'] = s.group_end()
    if st.get('peric'):
        hpoly = Polygon(catmull(hp, True, 6))
        ring = hpoly.buffer(16).difference(hpoly.buffer(2))
        g = s.group_start(nm('Pericardio'))
        draw_poly(s, F, ring, ('lin', [(0, 'E5E7E9'), (100, 'AAB7B8')], 45), ('566573', 1.5))
        cs = list(hpoly.buffer(9).exterior.coords)[::9]
        from scenes import circles as _c
        _c(s, F, [(x, y, 7) for x, y in cs[::2]], 'FDFEFE', ('7B7D7D', 0.75))
        ids['peric'] = s.group_end()
    if st.get('emb'):
        hx_, hy_ = hilum('R', st)
        g = s.group_start(nm('Embolo'))
        from scenes import circles as _c
        _c(s, F, [(hx_ - 30, hy_ + 5, 26, 16)], shade('6E1A12', 0.3, 0.3), ('3B0D08', 1.5))
        ids['emb'] = s.group_end()
    if st.get('rind'):
        k = st['rind']
        ring = PR.difference(PR.buffer(-14 - 30 * k))
        bumps = [Point(x, y).buffer(14 + 26 * k) for x, y in list(PR.exterior.coords)[::9]]
        rind = unary_union([ring] + bumps).intersection(PR.buffer(4))
        if k < 0.5:
            rind = rind.intersection(sbox(0, 380, 1000, 1000))
        ids['rind'] = draw_poly(s, F, rind, shade('8E44AD', 0.3, 0.3, (40, 40)), ('4A235A', 2), nm('Mesotelioma'), eff('Mesotelioma'))
    if st.get('blebs'):
        ax_, ay_ = LR.bounds[0], LR.bounds[1]
        top = [p for p in LR.exterior.coords if p[1] < ay_ + 60]
        top = sorted(top, key=lambda p: p[0])
        cs_ = [(top[len(top) // 4][0], top[len(top) // 4][1] + 8, 16), (top[len(top) // 2][0], top[len(top) // 2][1] + 6, 20)]
        from scenes import circles as _c
        ids['blebs'] = _c(s, F, cs_, ('rad', [(0, 'FFFFFF'), (100, 'F5B7B1')], (40, 40)), (C_VISCERAL, 1.5), nm('Bulas'), eff('Bulas'))
    if st.get('consol'):
        cx_, cy_, cr = st['consol']
        cpoly = Point(cx_, cy_).buffer(cr).intersection(LR.buffer(-4))
        ids['consol'] = draw_poly(s, F, cpoly, ('rad', [(0, 'C0392B'), (100, ('D98880'))], (50, 50)), ('922B21', 1.25, 'dash'), nm('Consolidacion'), eff('Consolidacion'))
    if st.get('mass'):
        mx, my, mr = st['mass']
        from scenes import circles as _c
        ids['mass'] = _c(s, F, [(mx, my, mr, mr * 0.85)], shade('A569BD', 0.35, 0.3), ('4A235A', 2), nm('Tumor'), eff('Tumor'))
    # diafragma (sigue las cúpulas)
    domeR = [cavR[i] for i in [10, 11, 12, 13, 14, 15, 16]]
    domeL = [cavL[i] for i in [16, 15, 14, 13, 12, 11, 10]]
    dl = catmull(domeR + [(500 + shift * 0.3, 815)] + domeL, False, 5)
    dpoly = LineString([(x, y + 14) for x, y in dl]).buffer(15, cap_style=1)
    ids['diaph'] = draw_poly(s, F, dpoly, vshade(C_MUSCLE, 0.3, 0.3), (darken(C_MUSCLE, 0.5), 1.25), nm('Diafragma'), eff('Diafragma'))
    # clavículas
    cl = [catmull([(470, 95), (380, 80), (290, 92), (200, 120)], False, 5), catmull([(530, 95), (620, 80), (710, 92), (800, 120)], False, 5)]
    g = s.group_start(nm('Clavículas'))
    draw_lines(s, F, cl, darken(C_BONE, 0.45), 14)
    draw_lines(s, F, cl, C_BONE, 10)
    ids['clav'] = s.group_end()
    # puntos de anclaje útiles (en pulgadas)
    A = {}
    def cen(g):
        c = g.representative_point() if g is not None and not g.is_empty else Point(0, 0)
        return F.p(c.x, c.y)
    A['lungR'] = cen(LR); A['lungL'] = cen(LL)
    A['hilR'] = F.p(*hilum('R', st)); A['hilL'] = F.p(*hilum('L', st))
    A['heart'] = F.p(hc[0], hc[1]); A['trachea'] = F.p(500 + shift * 0.3, 160)
    A['svc'] = F.p(458 + shift * 0.6, 330); A['ivc'] = F.p(472 + shift * 0.8, 880)
    A['diaphR'] = F.p(cavR[13][0], cavR[13][1] + 18); A['diaphL'] = F.p(cavL[13][0], cavL[13][1] + 18)
    A['cpR'] = F.p(*cavR[10]); A['cpL'] = F.p(*cavL[10])
    A['parR'] = F.p(cavR[6][0], cavR[6][1]); A['parL'] = F.p(cavL[6][0], cavL[6][1])
    lx = LR.bounds
    A['viscR'] = F.p(lx[0], (lx[1] + lx[3]) / 2)
    A['apexR'] = F.p((LR.bounds[0] + LR.bounds[2]) / 2, LR.bounds[1])
    A['latR'] = F.p(cavR[5][0] + 30, cavR[5][1])
    A['latL'] = F.p(cavL[5][0] - 30, cavL[5][1])
    A['F'] = F
    A['ids'] = ids
    A['cavR'] = cavR; A['cavL'] = cavL
    A['fluidR'] = F.p(cavR[8][0] + 60, fluid_level('R', st, cavR) + 20) if st.get('fluidR') else None
    A['airR'] = F.p(cavR[3][0] + 25, cavR[3][1] + 30)
    return A
