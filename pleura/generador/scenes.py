# -*- coding: utf-8 -*-
"""Escenas ilustradas paramétricas (formas nativas editables, nombres «!!»
estables para Morph): ampliación de las hojas pleurales, capilar de
Starling, radiografía esquemática, ecografía, drenaje con sello de agua,
tubos de laboratorio, manos del examinador, órganos abdominales."""
from anat import *
import random


def smooth_path(pts, t=1.0):
    """Catmull-Rom cerrado -> Bézier cúbicas (trazado de forma libre)"""
    n = len(pts)
    d = 'M %d %d ' % pts[0]
    for i in range(n):
        p0 = pts[(i - 1) % n]; p1 = pts[i]; p2 = pts[(i + 1) % n]; p3 = pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6 * t, p1[1] + (p2[1] - p0[1]) / 6 * t)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6 * t, p2[1] - (p3[1] - p1[1]) / 6 * t)
        d += 'C %d %d %d %d %d %d ' % (c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
    return d + 'Z'


def circ(cx, cy, r, ry=None):
    ry = ry or r
    k = 0.5523
    return ('M %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d C %d %d %d %d %d %d Z' % (
        cx + r, cy, cx + r, cy + ry * k, cx + r * k, cy + ry, cx, cy + ry,
        cx - r * k, cy + ry, cx - r, cy + ry * k, cx - r, cy,
        cx - r, cy - ry * k, cx - r * k, cy - ry, cx, cy - ry,
        cx + r * k, cy - ry, cx + r, cy - ry * k, cx + r, cy))


def circles(s, F, cs, fill, line=None, name=None, shadow=False):
    """muchos círculos (coordenadas locales) como una forma"""
    if not cs:
        return None
    x0 = min(c[0] - c[2] for c in cs); x1 = max(c[0] + c[2] for c in cs)
    y0 = min(c[1] - (c[3] if len(c) > 3 else c[2]) for c in cs); y1 = max(c[1] + (c[3] if len(c) > 3 else c[2]) for c in cs)
    bw = max(x1 - x0, 1); bh = max(y1 - y0, 1)
    d = ' '.join(circ((c[0] - x0) * 10, (c[1] - y0) * 10, c[2] * 10, (c[3] if len(c) > 3 else c[2]) * 10) for c in cs)
    X, Y = F.p(x0, y0)
    return s.free(X, Y, F.sx(bw), F.sy(bh), d, fill, line, shadow, name=name, W=int(bw * 10), H=int(bh * 10))


def rect_l(s, F, x0, y0, x1, y1, fill, line=None, name=None, geom='rect', shadow=False, adj=None):
    X, Y = F.p(x0, y0)
    return s.shape(X, Y, F.sx(x1 - x0), F.sy(y1 - y0), geom, fill, line, shadow, name=name, adj=adj)


def wavy(x0, x1, y, amp, n, phase=0):
    return [(x0 + (x1 - x0) * k / (n * 8), y + amp * math.sin(phase + 2 * math.pi * k / 8)) for k in range(n * 8 + 1)]


# =============================================================== HOJAS PLEURALES AMPLIADAS
def pleura_zoom(s, X, Y, W, H, st=None):
    """corte de la pared torácica y ambas hojas (de arriba abajo: piel, músculo intercostal con
    costillas y paquete vasculonervioso, pleura parietal, espacio pleural, pleura visceral, alvéolos).
    st: gap 0..1 · kind ser|exud|pus|blood|air · lymph ok|sat|block · inflam · septa · cells n ·
        tumor meso|meta|tfs · dx (deslizamiento horizontal de la hoja visceral) · hl"""
    st = st or {}
    F = Frame(X, Y, W, H)
    hl = st.get('hl', set())
    rnd = random.Random(7)
    A = {'F': F}
    def eff(n, d=False):
        return GLOW if n in hl else d
    # pared
    g = s.group_start('!!PielPared')
    rect_l(s, F, 0, 0, 1000, 45, vshade(C_SKIN, 0.3, 0.25), (darken(C_SKIN, 0.5), 1))
    rect_l(s, F, 0, 45, 1000, 125, ('lin', [(0, 'FBEBB0'), (100, 'F1D27A')], 90), None)
    circles(s, F, [(25 + 50 * k + (k % 2) * 20, 85, 22, 18) for k in range(20)], 'FFF3C9', ('E0B94F', 0.75))
    A['skin'] = s.group_end()
    g = s.group_start('!!MusculoIntercostal')
    rect_l(s, F, 0, 125, 1000, 335, vshade(C_MUSCLE, 0.25, 0.25), (darken(C_MUSCLE, 0.5), 1))
    draw_lines(s, F, [[(x, 130), (x + 60, 330)] for x in range(-40, 1000, 34)], darken(C_MUSCLE, 0.3), 1)
    A['musc'] = s.group_end()
    g = s.group_start('!!Costillas')
    for cx in (230, 770):
        circles(s, F, [(cx, 222, 120, 88)], shade(C_BONE, 0.4, 0.25), (darken(C_BONE, 0.55), 2))
        circles(s, F, [(cx, 222, 82, 54)], ('rad', [(0, 'F7D9B5'), (100, 'D9A273')], (50, 50)), None)
    A['ribs'] = s.group_end()
    g = s.group_start('!!PaqueteVN')
    # corte sagital: izquierda = craneal, derecha = caudal. Surco subcostal = borde INFERIOR (caudal) de cada costilla
    for cx in (230, 770):
        circles(s, F, [(cx + 112, 262, 13)], C_VEN, (INK, 0.75))
        circles(s, F, [(cx + 120, 290, 11)], C_ART, (INK, 0.75))
        circles(s, F, [(cx + 124, 316, 9)], 'FFE066', (INK, 0.75))
    A['nvb'] = s.group_end()
    A['nvb_pt'] = F.p(350, 290); A['rib_pt'] = F.p(230, 160); A['rib2'] = F.p(770, 160)
    A['upper_border'] = F.p(655, 222)   # borde superior (craneal) de la costilla inferior
    if st.get('axis'):
        label(s, *F.p(10, 2), F.sx(980), F.sy(40), '◄ CRANEAL                                    CAUDAL ►', 11, '5D4037', name='Orientación')
    # pleura parietal: tejido submesotelial + mesotelio
    gap = 22 + 330 * st.get('gap', 0)
    yP = 345
    infl = st.get('inflam')
    tumor = st.get('tumor')
    g = s.group_start('!!PleuraParietal')
    rect_l(s, F, 0, yP, 1000, yP + 68, ('a', 'FCE4EC' if not infl else 'F8B7B7', 100), None)
    meso_y = yP + 58
    cells = [(k * 50 + 25, meso_y + 6, 26, 9) for k in range(20)]
    circles(s, F, cells, C_PARIETAL if 'PleuraParietal' not in hl else lighten(C_PARIETAL, 0.2), (darken(C_PARIETAL, 0.5), 1))
    circles(s, F, [(c[0], c[1], 7, 4) for c in cells], darken(C_PARIETAL, 0.55), None)
    A['par'] = s.group_end()
    A['par_pt'] = F.p(500, meso_y + 6)
    # capilar sistémico y linfático (pleura parietal)
    capw = 14 * (1.6 if infl else 1)
    s.free(*F.p(0, yP + 18), F.sx(1000), F.sy(capw * 2), 'M 0 0 L 1000 0 L 1000 1000 L 0 1000 Z',
           vshade(C_ART, 0.35, 0.3), (darken(C_ART, 0.5), 1), eff('CapilarSistemico'), name='!!CapilarSistemico')
    A['cap_pt'] = F.p(150, yP + 18 + capw)
    lym = st.get('lymph', 'ok')
    lcol = C_LYMPH if lym != 'block' else '8A8A8A'
    g = s.group_start('!!VasoLinfatico')
    rect_l(s, F, 520, yP + 4, 1000, yP + 34, vshade(lcol, 0.4, 0.3), (darken(lcol, 0.5), 1))
    # estomas hacia el espacio pleural
    for sx in (600, 760, 900):
        rect_l(s, F, sx - 9, yP + 30, sx + 9, meso_y + 14, lcol if lym != 'block' else '6E6E6E', (darken(lcol, 0.5), 0.75))
    if lym == 'block':
        circles(s, F, [(700, yP + 19, 26, 18), (850, yP + 19, 24, 17)], shade('7D3C98', 0.3, 0.3), ('4A235A', 1.25))
    A['lym'] = s.group_end()
    A['lym_pt'] = F.p(820, yP + 19); A['stoma'] = F.p(760, meso_y + 10)
    # espacio pleural / líquido
    kind = st.get('kind', 'ser')
    y0 = meso_y + 15; y1 = y0 + gap
    col = {'ser': C_FLUID, 'exud': C_EXUD, 'pus': C_PUS, 'blood': C_BLOOD, 'air': C_AIR, 'chyle': 'F4F1E6'}[kind]
    nm = '!!AirePleural' if kind == 'air' else '!!LiquidoPleural'
    A['fluid'] = rect_l(s, F, 0, y0, 1000, y1, ('a', col, 92 if kind != 'air' else 96), ('7FB3D5', 1, 'dash') if kind == 'air' else None,
           nm, shadow=eff(nm[2:]))
    A['space'] = F.p(500, (y0 + y1) / 2); A['space_y'] = (y0, y1)
    if tumor == 'meso':
        bumps = [(60 + 95 * k + rnd.randint(-15, 15), meso_y + 22 + rnd.randint(0, 20), rnd.randint(40, 62), rnd.randint(30, 52)) for k in range(10)]
        A['tum'] = circles(s, F, bumps, shade('8E44AD', 0.3, 0.3), ('4A235A', 1.75), '!!TumorParietal')
    # contenido celular
    nc = st.get('cells', 0)
    if nc and kind != 'air':
        cs = [(rnd.randint(30, 970), rnd.randint(int(y0 + 12), int(max(y0 + 13, y1 - 12))), 11) for _ in range(nc)]
        g = s.group_start('!!Leucocitos')
        circles(s, F, cs, 'F5F5F5', ('7D7D7D', 0.75))
        circles(s, F, [(c[0] + 3, c[1] + 2, 5) for c in cs], '6C3483', None)
        A['wbc'] = s.group_end()
    if st.get('prot') and kind != 'air':
        cs = [(rnd.randint(30, 970), rnd.randint(int(y0 + 8), int(max(y0 + 9, y1 - 8))), 6) for _ in range(st['prot'])]
        A['prot'] = circles(s, F, cs, 'F1C40F', ('9A7D0A', 0.5), '!!Proteinas')
    if st.get('bact') and kind != 'air':
        bs = [(rnd.randint(30, 970), rnd.randint(int(y0 + 10), int(max(y0 + 11, y1 - 10)))) for _ in range(st['bact'])]
        A['bact'] = draw_lines(s, F, [[(x, y), (x + 16, y + 6)] for x, y in bs], '512E5F', 4, '!!Bacterias')
    if st.get('septa') and gap > 120:
        sl = [[(x, y0), (x + 40, (y0 + y1) / 2), (x - 10, y1)] for x in (180, 430, 690, 880)]
        A['septa'] = draw_lines(s, F, sl, 'F8F1D0', 5, '!!Tabiques')
    if kind == 'air' and st.get('bubbles', True):
        bs = [(rnd.randint(60, 940), rnd.randint(int(y0 + 10), int(max(y0 + 11, y1 - 10))), rnd.randint(7, 14)) for _ in range(int(6 + gap / 15))]
        circles(s, F, bs, None, ('5DADE2', 1.25), '!!BurbujasAire')
    # pleura visceral + pulmón (se desplazan juntos: deslizamiento)
    dx = st.get('dx', 0)
    yv = y1
    g = s.group_start('!!PleuraVisceral')
    cells = [(k * 50 + 25 + dx, yv + 8, 26, 9) for k in range(-1, 21)]
    rect_l(s, F, -60 + dx, yv, 1060 + dx, yv + 52, ('a', 'EBDEF0', 100), None)
    circles(s, F, cells, C_VISCERAL, (darken(C_VISCERAL, 0.5), 1))
    circles(s, F, [(c[0], c[1], 7, 4) for c in cells], darken(C_VISCERAL, 0.55), None)
    if tumor == 'meso':
        circles(s, F, [(110 + 120 * k + dx, yv - 4, 34, 22) for k in range(8)], shade('8E44AD', 0.3, 0.3), ('4A235A', 1.5))
    A['visc'] = s.group_end()
    A['visc_pt'] = F.p(500 + dx, yv + 8)
    s.free(*F.p(-60 + dx, yv + 28), F.sx(1120), F.sy(18), 'M 0 0 L 1000 0 L 1000 1000 L 0 1000 Z',
           vshade('C0392B', 0.4, 0.25), (darken('C0392B', 0.5), 0.75), name='!!CapilarPulmonar')
    ya = yv + 60
    alv = []
    for r in range(12):
        cy = ya + 55 + r * 100
        if cy + 44 > 1000:
            break
        for k in range(0, 11):
            alv.append((k * 95 + 25 + (r % 2) * 48 + dx, cy, 46, 44))
    g = s.group_start('!!Alveolos')
    rect_l(s, F, -60 + dx, ya, 1060 + dx, max(ya + 20, 1000), shade(C_LUNG, 0.3, 0.2), None)
    circles(s, F, alv, ('rad', [(0, 'FFFFFF'), (100, 'FBE3E6')], (40, 40)), (darken(C_LUNG, 0.4), 1.25))
    A['alv'] = s.group_end()
    A['alv_pt'] = F.p(500 + dx, ya + 55)
    # tumores focales
    if tumor == 'meta':
        g = s.group_start('!!Nodulos')
        circles(s, F, [(180, meso_y + 30, 40, 30), (560, meso_y + 32, 32, 26), (420, yv - 10, 36, 28), (850, yv - 8, 44, 32)],
                shade('A569BD', 0.35, 0.3), ('4A235A', 1.5))
        A['tum'] = s.group_end()
    if tumor == 'tfs':
        g = s.group_start('!!TumorFibroso')
        draw_lines(s, F, [[(520 + dx, yv), (520 + dx, yv - 40)]], 'C9A27E', 6)
        circles(s, F, [(520 + dx, yv - 110, 120, 80)], shade('E8D3B0', 0.4, 0.25), ('8B6B47', 2))
        draw_lines(s, F, [[(450 + dx, yv - 140), (590 + dx, yv - 90)], [(460 + dx, yv - 90), (580 + dx, yv - 130)]], 'C9A27E', 1.25)
        A['tum'] = s.group_end()
    return A


# =============================================================== CAPILAR (STARLING)
def starling(s, X, Y, W, H, st=None):
    """capilar pleural (arriba), compartimento intersticial/espacio pleural (abajo) y linfático (derecha).
    st: pc 0..2 · onc 0..2 · alb n · perm 0..1 · lymph ok|block|sat · acc 0..1 (líquido acumulado) ·
        show: conjunto de flechas a mostrar (pc, onc, net, lym) · prot (proteínas que salen) · wbc"""
    st = st or {}
    F = Frame(X, Y, W, H)
    rnd = random.Random(11)
    hl = st.get('hl', set())
    A = {'F': F}
    # compartimento inferior
    acc = st.get('acc', 0)
    A['inter'] = rect_l(s, F, 0, 360, 1000, 1000, ('lin', [(0, 'F4FAFD'), (100, 'D6EAF8')], 90), (INK, 1.5), '!!Intersticio')
    fib = [wavy(20, 820, y, 14, 9, ph) for y, ph in ((470, 0), (600, 1.3), (730, 2.1), (860, 0.7))]
    A['fib'] = draw_lines(s, F, fib, 'E3C9B5', 3, '!!FibrasColageno')
    fbl = [(120, 535, 40, 14), (470, 665, 40, 14), (690, 520, 38, 13), (260, 795, 40, 14), (600, 920, 36, 13)]
    g = s.group_start('!!Fibroblastos')
    circles(s, F, fbl, shade('D7BDE2', 0.3, 0.2), ('8E44AD', 0.75))
    circles(s, F, [(c[0], c[1], 14, 7) for c in fbl], '6C3483', None)
    s.group_end()
    if W > 4.5:
        label(s, *F.p(25, 380), F.sx(560), F.sy(55), 'INTERSTICIO SUBPLEURAL → ESPACIO PLEURAL', 12, '5D6D7E', align='l', name='Rótulo compartimento')
    lvl = 1000 - acc * 520
    if acc > 0:
        A['acc'] = s.free(*F.p(0, lvl), F.sx(1000), F.sy(1000 - lvl),
                          'M 0 60 C 250 0 500 120 750 50 C 850 25 950 40 1000 60 L 1000 1000 L 0 1000 Z',
                          ('a', C_EXUD if st.get('prot') else C_FLUID, 85), (darken(C_FLUID, 0.4), 1.25), name='!!LiquidoAcumulado',
                          shadow=GLOW if 'LiquidoAcumulado' in hl else False)
    # capilar
    g = s.group_start('!!Capilar')
    rect_l(s, F, 0, 40, 1000, 330, ('lin', [(0, 'F9D5D3'), (50, 'FDEDEC'), (100, 'F9D5D3')], 90), None)
    perm = st.get('perm', 0)
    for yy in (40, 290):
        cells = []
        k = 0
        x = 0
        while x < 1000:
            w = 110
            gapw = (26 * perm if (yy == 290 and k % 2 == 1) else 0)
            cells.append((x + gapw, x + w - 4))
            x += w; k += 1
        for a, b in cells:
            rect_l(s, F, a, yy, b, yy + 40, shade('E59866', 0.35, 0.25), (darken('E59866', 0.5), 1), geom='roundRect', adj={'adj': 40000})
            circles(s, F, [((a + b) / 2, yy + 20, 20, 9)], '7D3C98', None)
    rb = [(80 + 150 * k + rnd.randint(-20, 20), 140 + (k % 2) * 80, 42, 30) for k in range(7)]
    circles(s, F, rb, ('rad', [(0, 'E06A5F'), (60, 'C9372C'), (100, '7B1F17')], (50, 50)), ('6E1A12', 0.75))
    A['cap'] = s.group_end()
    nalb = st.get('alb', 26)
    al = [(rnd.randint(40, 960), rnd.randint(95, 275), 11) for _ in range(nalb)]
    A['alb'] = circles(s, F, al, shade('F4D03F', 0.4, 0.2), ('9A7D0A', 0.75), '!!Albumina',
                       GLOW if 'Albumina' in hl else False)
    A['alb_pt'] = F.p(al[0][0], al[0][1]) if al else F.p(500, 180)
    # flechas de fuerzas
    pc = st.get('pc', 1); onc = st.get('onc', 1)
    show = st.get('show', set())
    if 'pc' in show:
        A['f_pc'] = arrow_lbl(s, [F.p(300, 200), F.p(300, 520 + 60 * (pc - 1))], 'P_{c}', C_ART, 4 + 4 * pc, 24,
                              lx=F.p(325, 0)[0], ly=F.p(0, 430)[1], lw=0.75, name='!!FlechaPc', lbg=WHITE)
    if 'onc' in show:
        A['f_onc'] = arrow_lbl(s, [F.p(520, 500 - 40 * (onc - 1)), F.p(520, 200)], 'π_{c}', C_VEN, 3 + 4 * onc, 24,
                               lx=F.p(545, 0)[0], ly=F.p(0, 430)[1], lw=0.75, name='!!FlechaOnc', lbg=WHITE)
    if 'net' in show:
        net = pc - onc + 0.4 * perm + 0.3
        A['f_net'] = arrow_lbl(s, [F.p(150, 330), F.p(150, 600 + 120 * max(0, net - 0.3))], 'Filtración neta', '1F4E79',
                               3 + 5 * max(0.2, net), 15, lx=F.p(20, 0)[0], ly=F.p(0, 640 + 120 * max(0, net - 0.3))[1], lw=1.3, name='!!FlechaNeta', lbg=WHITE)
    # vaso linfático
    lym = st.get('lymph', 'ok')
    lc = C_LYMPH if lym != 'block' else '8A8A8A'
    g = s.group_start('!!VasoLinfatico')
    rect_l(s, F, 840, 420, 950, 1000, vshade(lc, 0.4, 0.3, 0), (darken(lc, 0.5), 1.5), geom='roundRect', adj={'adj': 30000})
    for vy in (560, 760):
        draw_lines(s, F, [[(850, vy + 40), (895, vy), (940, vy + 40)]], darken(lc, 0.5), 2.5)
    if lym == 'block':
        circles(s, F, [(895, 650, 50, 60)], shade('7D3C98', 0.3, 0.3), ('4A235A', 1.5))
    A['lym'] = s.group_end()
    A['lym_pt'] = F.p(895, 700)
    if 'lym' in show and lym != 'block':
        g = s.group_start('!!FlechaLinfa')
        s.arrow([F.p(895, 960), F.p(895, 440)], 'FFFFFF', 4)
        for yy in (560, 760, 900):
            s.arrow([F.p(660, yy), F.p(830, yy)], '0B5345', 4)
        label(s, *F.p(640, yy - 85), F.sx(200), F.sy(60), 'reabsorción', 13, '0B5345', bg=WHITE)
        A['f_lym'] = s.group_end()
    if st.get('prot'):
        A['prot'] = circles(s, F, [(rnd.randint(60, 780), rnd.randint(420, 940), 11) for _ in range(st['prot'])],
                            shade('F4D03F', 0.4, 0.2), ('9A7D0A', 0.75), '!!ProteinasFuga')
    if st.get('wbc'):
        cs = [(rnd.randint(60, 780), rnd.randint(430, 930), 22) for _ in range(st['wbc'])]
        g = s.group_start('!!Leucocitos')
        circles(s, F, cs, 'F2F3F4', ('7D7D7D', 1))
        circles(s, F, [(c[0] + 5, c[1] + 3, 10, 8) for c in cs], '6C3483', None)
        A['wbc'] = s.group_end()
    # gotas de filtrado
    nd = int(4 + 22 * acc)
    if st.get('drops', True):
        A['drops'] = circles(s, F, [(rnd.randint(40, 800), rnd.randint(400, 940), 9, 12) for _ in range(nd)],
                             ('a', '5DADE2', 80), ('2E86C1', 0.75), '!!GotasFiltrado')
    return A


# =============================================================== RADIOGRAFÍA ESQUEMÁTICA
def rx(s, X, Y, W, H, st=None, prefix='!!Rx', frame=True):
    """radiografía frontal esquemática construida con LA MISMA geometría del tórax (coherencia
    anatomía-imagen). Blanco = radiopaco (líquido, hueso, partes blandas); negro = aire."""
    st = st or {}
    F = Frame(X, Y, W, H)
    A = {'F': F}
    shift = st.get('shift', 0)
    if frame:
        A['bg'] = s.shape(X - 0.05, Y - 0.05, W + 0.1, H + 0.1, 'rect', '0B0B0B', ('5A5A5A', 2.5), False, name=prefix + 'Placa')
    cavR = side_pts('R', st); cavL = side_pts('L', st)
    PR = Polygon(catmull(cavR, True, 6)).buffer(0); PL = Polygon(catmull(cavL, True, 6)).buffer(0)
    wall = Polygon(catmull(WALL, True, 6))
    A['soft'] = draw_poly(s, F, wall, ('lin', [(0, '7A7A7A'), (50, '5C5C5C'), (100, '7A7A7A')], 0), None, prefix + 'PartesBlandas')
    # campos pulmonares (oscuros) con trama vascular
    LR, tfR = lung_geom('R', st, cavR); LL, tfL = lung_geom('L', st, cavL)
    LR = biggest(LR.intersection(PR.buffer(-3))) or LR; LL = biggest(LL.intersection(PL.buffer(-3))) or LL
    for side, P, L, tf, D in (('R', PR, LR, tfR, 'D'), ('L', PL, LL, tfL, 'I')):
        atel = st.get('atel' + side)
        g = s.group_start(prefix + 'Pulmon' + D)
        if atel:
            draw_poly(s, F, P, ('rad', [(0, 'E8E8E8'), (100, 'BDBDBD')], (50, 50)), None)
        else:
            draw_poly(s, F, P, ('rad', [(0, '3A3A3A'), (100, '262626')], (50, 40)), None)
            draw_poly(s, F, L, ('rad', [(0, '4A4A4A'), (100, '2E2E2E')], (60, 50)), None)
            vs = VESS_R if side == 'R' else mirror(VESS_R)
            vl = []
            for v in vs:
                vl += geom_lines(LineString([tf(x, y) for x, y in v]).intersection(L.buffer(-6)))
            draw_lines(s, F, vl, '9A9A9A', 1.75)
        A['lung' + side] = s.group_end()
    # costillas
    ribs = []
    for k in range(9):
        y0 = 150 + k * 78
        for sgn in (-1, 1):
            pts = [(500 + sgn * 30, y0), (500 + sgn * 150, y0 - 30 + k * 2), (500 + sgn * 300, y0 + 10), (500 + sgn * 410, y0 + 90), (500 + sgn * 440, y0 + 170)]
            ribs.append(catmull(pts, False, 6))
    A['ribs'] = draw_lines(s, F, ribs, ('a', 'D0D0D0', 55) and 'B5B5B5', 4.5, prefix + 'Costillas')
    # mediastino + corazón (blanco)
    inner = wall.buffer(-38)
    med = biggest(inner.difference(PR.buffer(4)).difference(PL.buffer(4)).intersection(sbox(330, 95, 670, 830)))
    hk = 1 - 0.18 * st.get('heart', 0)
    hp = [(470, 560), (520, 528), (590, 540), (650, 575), (695, 640), (712, 720), (690, 790), (625, 810), (540, 800), (472, 772), (448, 700), (450, 620)]
    hp = [(545 + shift + (x - 545) * hk, 660 + (y - 660) * hk) for x, y in hp]
    medall = unary_union([med, Polygon(catmull(hp, True, 6))]) if med is not None else Polygon(catmull(hp, True, 6))
    A['med'] = draw_poly(s, F, medall, ('rad', [(0, 'F2F2F2'), (100, 'C8C8C8')], (50, 60)), None, prefix + 'Mediastino')
    # tráquea (columna aérea oscura)
    tr = [(500 + shift * 0.15, 40), (500 + shift * 0.45, 200), (500 + shift * 0.75, 340)]
    A['trachea'] = draw_lines(s, F, [catmull(tr, False, 6)], '2A2A2A', 9, prefix + 'Traquea')
    # líquido (opacidad homogénea) y aire (hiperclaridad sin trama) — misma geometría que la ilustración
    for side, P, L, cav, D in (('R', PR, LR, cavR, 'D'), ('L', PL, LL, cavL, 'I')):
        f = st.get('fluid' + side, 0); a = st.get('air' + side, 0)
        if f > 0:
            lvl = fluid_level(side, st, cav)
            if st.get('hydro' + side):
                region = P.intersection(sbox(0, lvl, 1000, 1100))
            else:
                region = P.intersection(meniscus_poly(side, cav, lvl, min(110, 40 + 260 * f))).difference(L.buffer(2))
            A['fluid' + side] = draw_poly(s, F, region, ('lin', [(0, 'D9D9D9'), (100, 'F2F2F2')], 90), None, prefix + 'Opacidad' + D)
        if a > 0:
            region = P.difference(L.buffer(2))
            if f > 0:
                region = region.difference(P.intersection(sbox(0, fluid_level(side, st, cav) - 1, 1000, 1100)))
            A['air' + side] = draw_poly(s, F, region, '050505', None, prefix + 'Aire' + D)
            A['line' + side] = draw_lines(s, F, ring_line(L), 'FFFFFF', 1.5, prefix + 'LineaPleural' + D)
    # diafragma (borde superior de las cúpulas, blanco abajo)
    domeR = [cavR[i] for i in [10, 11, 12, 13, 14, 15, 16]]
    domeL = [cavL[i] for i in [16, 15, 14, 13, 12, 11, 10]]
    dl = catmull(domeR + [(500 + shift * 0.3, 815)] + domeL, False, 5)
    belly = Polygon(dl + [(870, 990), (130, 990)]).buffer(0)
    A['diaph'] = draw_poly(s, F, belly.intersection(wall), ('lin', [(0, 'EDEDED'), (100, 'BFBFBF')], 90), None, prefix + 'Diafragma')
    cl = [catmull([(470, 95), (380, 80), (290, 92), (200, 120)], False, 5), catmull([(530, 95), (620, 80), (710, 92), (800, 120)], False, 5)]
    A['clav'] = draw_lines(s, F, cl, 'E0E0E0', 6, prefix + 'Clavículas')
    if st.get('nodules'):
        rnd = random.Random(5)
        cs = []
        for L in (LR, LL):
            b = L.bounds
            k = 0
            while k < 7:
                x = rnd.uniform(b[0] + 20, b[2] - 20); y = rnd.uniform(b[1] + 40, b[3] - 20)
                if L.contains(Point(x, y).buffer(30)):
                    cs.append((x, y, rnd.randint(14, 34))); k += 1
        A['nod'] = circles(s, F, cs, ('rad', [(0, 'F5F5F5'), (100, 'BDBDBD')], (40, 40)), None, prefix + 'Nodulos')
    A['cavR'] = cavR; A['cavL'] = cavL
    A['pt'] = lambda x, y: F.p(x, y)
    return A


# =============================================================== ECOGRAFÍA
def probe(s, x, y, w, rot=0, name='!!TransductorEcografico'):
    """transductor lineal"""
    h = w * 1.6
    g = s.group_start(name)
    s.shape(x + w * 0.38, y - h * 0.35, w * 0.24, h * 0.4, 'rect', '505A63', (INK, 1), False, rot=rot)
    s.shape(x, y, w, h * 0.75, 'roundRect', vshade('D5DBDB', 0.4, 0.3, 0), (INK, 1.75), False, adj={'adj': 30000}, rot=rot)
    s.shape(x + w * 0.05, y + h * 0.68, w * 0.9, h * 0.1, 'rect', '2E4053', (INK, 1), False, rot=rot)
    return s.group_end()


def bmode(s, X, Y, W, H, st=None, prefix='!!Eco'):
    """imagen ecográfica en modo B esquemática: partes blandas, costillas con sombra acústica,
    línea pleural hiperecoica; patrón inferior: 'A' (líneas A), 'B' (líneas B), 'liq' (anecoico)."""
    st = st or {}
    F = Frame(X, Y, W, H)
    rnd = random.Random(3)
    A = {'F': F}
    A['bg'] = s.shape(X, Y, W, H, 'rect', '0A0A0A', ('5A5A5A', 2), False, name=prefix + 'Pantalla')
    sp = []
    for _ in range(420):
        sp.append((rnd.uniform(5, 995), rnd.uniform(5, 330), rnd.uniform(2, 5)))
    A['soft'] = circles(s, F, sp, '8C8C8C', None, prefix + 'PartesBlandas')
    g = s.group_start(prefix + 'Costillas')
    for cx in (160, 840):
        s.free(*F.p(cx - 120, 330), F.sx(240), F.sy(670), 'M 0 0 L 1000 0 L 1000 1000 L 0 1000 Z', '000000', None)
        s.free(*F.p(cx - 120, 300), F.sx(240), F.sy(60), 'M 0 1000 C 200 0 800 0 1000 1000 Z', 'EDEDED', None)
    A['ribs'] = s.group_end()
    pat = st.get('pattern', 'A')
    # línea pleural
    A['pline'] = s.free(*F.p(280, 352), F.sx(440), F.sy(16), 'M 0 0 L 1000 0 L 1000 1000 L 0 1000 Z', 'FFFFFF', None,
                        GLOW if st.get('hlpl') else False, name=prefix + 'LineaPleural')
    if pat == 'A':
        A['pat'] = draw_lines(s, F, [[(290, y), (710, y)] for y in (520, 690, 860)], 'C8C8C8', 3, prefix + 'LineasA')
    elif pat == 'B':
        g = s.group_start(prefix + 'LineasB')
        for x in (380, 520, 640):
            s.free(*F.p(x - 14, 360), F.sx(28), F.sy(640), 'M 300 0 L 700 0 L 1000 1000 L 0 1000 Z',
                   ('lin', [(0, 'FFFFFF'), (100, 'BFBFBF', 40)], 90), None)
        A['pat'] = s.group_end()
    elif pat == 'liq':
        A['pat'] = rect_l(s, F, 285, 375, 715, 760, '000000', None, prefix + 'Anecoico')
        circles(s, F, [(rnd.uniform(300, 700), rnd.uniform(780, 990), rnd.uniform(3, 6)) for _ in range(120)], '9A9A9A', None, prefix + 'PulmonCompr')
    else:
        A['pat'] = circles(s, F, [(rnd.uniform(285, 715), rnd.uniform(375, 995), rnd.uniform(2, 5)) for _ in range(200)], '7A7A7A', None, prefix + 'Parenquima')
    return A


def mmode(s, X, Y, W, H, kind='playa', prefix='!!ModoM'):
    """modo M: 'playa' (olas arriba + arena abajo), 'codigo' (código de barras/estratósfera),
    'punto' (alternancia playa/código: punto pulmonar)"""
    F = Frame(X, Y, W, H)
    rnd = random.Random(9)
    A = {'F': F}
    A['bg'] = s.shape(X, Y, W, H, 'rect', '0A0A0A', ('5A5A5A', 2), False, name=prefix + 'Pantalla')
    top = [[(0, y), (1000, y)] for y in range(40, 330, 38)]
    A['top'] = draw_lines(s, F, top, 'A6A6A6', 2.5, prefix + 'Superficie')
    A['pl'] = draw_lines(s, F, [[(0, 350), (1000, 350)]], 'FFFFFF', 4.5, prefix + 'LineaPleural')
    if kind == 'playa':
        A['bot'] = circles(s, F, [(rnd.uniform(5, 995), rnd.uniform(375, 995), rnd.uniform(3, 7)) for _ in range(650)], '9C9C9C', None, prefix + 'Arena')
    elif kind == 'codigo':
        A['bot'] = draw_lines(s, F, [[(0, y), (1000, y)] for y in range(385, 1000, 30)], '9C9C9C', 2, prefix + 'Barras')
    else:
        segs = []
        cs = []
        for k in range(4):
            x0 = k * 250
            if k % 2 == 0:
                cs += [(rnd.uniform(x0 + 5, x0 + 245), rnd.uniform(375, 995), rnd.uniform(3, 7)) for _ in range(170)]
            else:
                segs += [[(x0, y), (x0 + 250, y)] for y in range(385, 1000, 30)]
        g = s.group_start(prefix + 'PuntoPulmonar')
        circles(s, F, cs, '9C9C9C', None)
        draw_lines(s, F, segs, '9C9C9C', 2)
        A['bot'] = s.group_end()
    return A


# =============================================================== DRENAJE CON SELLO DE AGUA
def water_seal(s, X, Y, W, H, st=None):
    """frasco con doble tubuladura: tubo largo sumergido bajo el agua (sello) y tubo corto
    de abocamiento al exterior. st: bubbles · osc (-1..1 desplazamiento del nivel en el tubo) · hl"""
    st = st or {}
    F = Frame(X, Y, W, H)
    A = {'F': F}
    hl = st.get('hl', set())
    g = s.group_start('!!Frasco')
    rect_l(s, F, 120, 230, 880, 1000, ('a', 'EAF2F8', 70), (INK, 2.5), geom='roundRect', adj={'adj': 9000})
    rect_l(s, F, 230, 150, 770, 240, vshade('7F8C8D', 0.4, 0.3), (INK, 2))
    A['frasco'] = s.group_end()
    A['agua'] = rect_l(s, F, 128, 600, 872, 992, ('lin', [(0, '85C1E9'), (100, '2E86C1')], 90), None, '!!SelloAgua',
                       shadow=GLOW if 'SelloAgua' in hl else False)
    osc = st.get('osc', 0)
    # tubo largo (del paciente) sumergido
    A['tubo'] = s.shape(*F.p(380, 0), F.sx(70), F.sy(820), 'rect', ('a', 'F8F9F9', 60), (INK, 2), False, name='!!TuboSumergido')
    A['col'] = rect_l(s, F, 386, 600 - 120 * osc, 444, 812, ('lin', [(0, '85C1E9'), (100, '2E86C1')], 90), None, '!!ColumnaAgua')
    # tubo corto: abocamiento al exterior
    A['vent'] = s.shape(*F.p(600, 20), F.sx(60), F.sy(300), 'rect', ('a', 'F8F9F9', 60), (INK, 2), False, name='!!Ventilacion')
    if st.get('bubbles'):
        rnd = random.Random(2)
        A['bub'] = circles(s, F, [(415 + rnd.randint(-35, 35), 790 - k * 50, rnd.randint(14, 24)) for k in range(4)],
                           ('a', 'FFFFFF', 70), ('1B4F72', 1.25), '!!Burbujas')
    A['pt_tube_top'] = F.p(415, 0); A['pt_vent'] = F.p(630, 20); A['pt_tip'] = F.p(415, 820); A['pt_water'] = F.p(700, 780)
    return A


# =============================================================== LABORATORIO
def tube(s, x, y, w, h, color, label=None, kind='clear', name=None, fill=0.62, cap='C0392B'):
    """tubo de ensayo con tapa; kind: clear · turbid · milky · blood · pus · viscous"""
    TUBE = 'M 0 0 L 1000 0 L 1000 820 C 1000 1090 0 1090 0 820 Z'
    g = s.group_start(name or ('Tubo ' + (label or '')))
    s.shape(x - w * 0.06, y, w * 1.12, h * 0.1, 'rect', vshade(cap, 0.3, 0.3, 0), (INK, 1.5), False)
    by = y + h * 0.1; bh = h * 0.9
    ly = by + bh * (1 - fill)
    s.free(x + w * 0.07, ly, w * 0.86, by + bh - ly - h * 0.015, 'M 0 0 L 1000 0 L 1000 780 C 1000 1080 0 1080 0 780 Z',
           ('lin', [(0, lighten(color, 0.2)), (100, darken(color, 0.12))], 90), None)
    s.shape(x + w * 0.07, ly - h * 0.015, w * 0.86, h * 0.035, 'ellipse', lighten(color, 0.3), (darken(color, 0.3), 0.75), False)
    rnd = random.Random(len(label or '') * 7 + 3)
    if kind in ('turbid', 'pus', 'milky'):
        dd = ' '.join(circ(rnd.randint(150, 850), rnd.randint(80, 920), rnd.randint(30, 60)) for _ in range(14))
        s.free(x + w * 0.12, ly + h * 0.04, w * 0.76, (by + bh - ly) * 0.8, dd, ('a', 'FFFFFF', 50), None)
    if kind == 'viscous':
        s.free(x + w * 0.25, ly - h * 0.12, w * 0.5, h * 0.2, 'M 300 0 C 250 400 150 700 200 1000 L 800 1000 C 850 700 750 400 700 0 Z',
               ('a', lighten(color, 0.15), 90), (darken(color, 0.3), 0.75))
    s.free(x, by, w, bh, TUBE, ('a', 'FFFFFF', 18), (INK, 2.25))
    s.shape(x + w * 0.16, by + bh * 0.08, w * 0.12, bh * 0.6, 'roundRect', ('a', 'FFFFFF', 60), None, False, adj={'adj': 50000})
    if label:
        s.shape(x - 0.3, y + h + 0.06, w + 0.6, 0.4, 'rect', WHITE, THIN, False, label, 11.5, F_HEAD, INK, True, 'c', 'm',
                (0.03, 0, 0.03, 0), minsize=8)
    return s.group_end()


# =============================================================== MANOS Y ONDAS
HAND = [(80, 420), (180, 330), (300, 300), (420, 260), (560, 250), (700, 260), (850, 280), (955, 320), (960, 380),
        (860, 400), (700, 410), (690, 470), (830, 500), (900, 560), (880, 610), (700, 610), (650, 680), (760, 720),
        (770, 780), (620, 790), (520, 760), (480, 840), (360, 850), (220, 760), (120, 640), (60, 520)]


def hand(s, x, y, w, rot=0, name='!!Mano', flip=False, color='F0C8A0'):
    """mano estilizada (dedos extendidos hacia la derecha)"""
    d = smooth_path(HAND if not flip else [(1000 - a, b) for a, b in HAND])
    return s.free(x, y, w, w * 0.62, d, shade(color, 0.35, 0.2), (darken(color, 0.55), 1.75), SOFT, name=name, rot=rot)


def waves(s, cx, cy, r0, n=3, dr=0.18, color='1F4E79', w=3, ang=(-50, 50), name='!!Ondas', dash=None, fade_k=0.0):
    """arcos concéntricos de propagación (vibración / sonido)"""
    g = s.group_start(name)
    for k in range(n):
        r = r0 + k * dr
        a0, a1 = math.radians(ang[0]), math.radians(ang[1])
        pts = [(cx + r * math.cos(a0 + (a1 - a0) * t / 12), cy + r * math.sin(a0 + (a1 - a0) * t / 12)) for t in range(13)]
        s.arrow(pts, color if not fade_k else lighten(color, min(0.8, fade_k * k)), max(1, w - k * fade_k * 1.2), tail=None, dash=dash)
    return s.group_end()


# =============================================================== ABDOMEN (hidrotórax hepático)
def abdomen(s, X, Y, W, H, st=None):
    """corte coronal esquemático del hemitórax derecho y el abdomen superior.
    st: asc 0..1 (ascitis) · defect · pass (flechas de paso) · pfl 0..1 (líquido pleural) · hl"""
    st = st or {}
    F = Frame(X, Y, W, H)
    hl = st.get('hl', set())
    A = {'F': F}
    def eff(n):
        return GLOW if n in hl else False
    A['wall'] = draw_poly(s, F, Polygon(catmull([(80, 20), (920, 20), (960, 500), (930, 980), (70, 980), (40, 500)], True, 6)),
                          shade(C_SKIN, 0.3, 0.15, (50, 30)), (darken(C_SKIN, 0.5), 2), '!!ParedToracica', SOFT)
    cav = Polygon(catmull([(330, 45), (520, 70), (610, 180), (650, 330), (600, 420), (420, 405), (230, 440), (140, 420), (130, 260), (200, 110)], True, 6))
    A['cav'] = draw_poly(s, F, cav, ('a', 'EAF6FB', 90), None, '!!EspacioPleuralD')
    pfl = st.get('pfl', 0)
    lung = Polygon(catmull([(330, 62), (510, 85), (595, 190), (632, 330), (585, 405), (420, 390), (235, 422), (150, 405), (145, 265), (210, 122)], True, 6)).buffer(-8)
    if pfl:
        lung = Polygon([(x, 85 + (y - 85) * (1 - 0.55 * pfl)) for x, y in lung.exterior.coords])
        lvl = 440 - 300 * pfl
        fl = cav.intersection(sbox(0, lvl, 1000, 1000)).difference(lung)
        A['pfl'] = draw_poly(s, F, fl, ('a', C_FLUID, 88), (darken(C_FLUID, 0.4), 1.5), '!!LiquidoPleuralD', eff('LiquidoPleuralD'))
    g = s.group_start('!!PulmonDerecho')
    draw_poly(s, F, lung, shade(C_LUNG, 0.45, 0.22, (40, 30)), (C_VISCERAL, 2.5), None, SOFT)
    A['lung'] = s.group_end()
    A['par'] = draw_lines(s, F, ring_line(cav), C_PARIETAL, 3, '!!PleuraParietalD')
    # diafragma con defecto
    dl = catmull([(110, 470), (300, 430), (520, 445), (660, 400), (900, 470)], False, 6)
    dp = LineString(dl).buffer(20, cap_style=1)
    if st.get('defect'):
        dp = dp.difference(Point(300, 433).buffer(26))
    A['diaph'] = draw_poly(s, F, dp, vshade(C_MUSCLE, 0.3, 0.3), (darken(C_MUSCLE, 0.5), 1.25), '!!Diafragma', eff('Diafragma'))
    A['defect_pt'] = F.p(300, 433)
    liv = Polygon(catmull([(130, 490), (320, 465), (540, 480), (700, 450), (820, 520), (700, 640), (480, 700), (260, 740), (140, 650)], True, 6))
    loops = []
    for k in range(6):
        cx = 220 + (k % 3) * 220; cy = 830 + (k // 3) * 80 - 40
        loops.append((cx, cy, 95, 45))
    asc = st.get('asc', 0)
    if asc:
        cavab = Polygon(catmull([(95, 500), (500, 470), (905, 500), (930, 760), (880, 960), (500, 975), (120, 960), (70, 760)], True, 6))
        lvl = 975 - 520 * asc
        region = cavab.intersection(sbox(0, lvl, 1000, 1000))
        A['asc'] = draw_poly(s, F, region, ('lin', [(0, 'F3EBB5'), (100, 'DCCB72')], 90), (darken('E8DFA0', 0.45), 1.25), '!!Ascitis', eff('Ascitis'))
    A['liver'] = draw_poly(s, F, liv, shade('8E3B2F', 0.35, 0.3, (40, 30)), (darken('8E3B2F', 0.5), 2), '!!Higado', eff('Higado'))
    A['bowel'] = circles(s, F, loops, shade('F5B7B1', 0.35, 0.2), (darken('F5B7B1', 0.5), 1.5), '!!Intestino', eff('Intestino'))
    A['pt_liver'] = F.p(450, 590); A['pt_asc'] = F.p(830, 760); A['pt_pleura'] = F.p(260, 380)
    return A


# =============================================================== RIÑÓN / GLOMÉRULO
def glomerulus(s, X, Y, W, H, st=None):
    """glomérulo con cápsula de Bowman y túbulo; st: leak (proteínas que pasan a la orina)"""
    st = st or {}
    F = Frame(X, Y, W, H)
    rnd = random.Random(4)
    A = {'F': F}
    g = s.group_start('!!Glomerulo')
    circles(s, F, [(430, 480, 380, 370)], ('a', 'FDF2E9', 100), ('A04000', 3))
    circles(s, F, [(430, 480, 300, 290)], ('a', 'FBEEE6', 100), ('C0392B', 1.5))
    loops = [(330 + 90 * math.cos(a) * 1.6, 470 + 90 * math.sin(a) * 1.6, 90, 70) for a in [k * math.pi / 3 for k in range(6)]]
    circles(s, F, loops, shade('E74C3C', 0.35, 0.25), ('922B21', 1.5))
    A['glom'] = s.group_end()
    A['art'] = draw_lines(s, F, [[(0, 300), (180, 380)], [(0, 640), (200, 560)]], C_ART, 14, '!!Arteriolas')
    A['tub'] = draw_poly(s, F, LineString(catmull([(780, 600), (880, 700), (930, 860), (980, 990)], False, 6)).buffer(40),
                         ('a', 'FCF3CF', 100), ('B7950B', 2), '!!Tubulo')
    n = st.get('leak', 0)
    if n:
        A['prot'] = circles(s, F, [(rnd.randint(600, 760), rnd.randint(300, 700), 16) for _ in range(n // 2)] +
                            [(rnd.randint(820, 960), rnd.randint(650, 980), 16) for _ in range(n // 2)],
                            shade('F4D03F', 0.4, 0.2), ('9A7D0A', 0.75), '!!ProteinasOrina')
    return A


def vein_dvt(s, X, Y, W, H, st=None):
    """vena profunda de la pierna con trombo y émbolo"""
    st = st or {}
    F = Frame(X, Y, W, H)
    A = {'F': F}
    A['leg'] = draw_poly(s, F, Polygon(catmull([(300, 0), (720, 0), (680, 500), (640, 1000), (380, 1000), (330, 500)], True, 6)),
                         shade(C_SKIN, 0.3, 0.2), (darken(C_SKIN, 0.5), 2), '!!Pierna', SOFT)
    A['vein'] = draw_poly(s, F, LineString([(520, 0), (510, 500), (500, 1000)]).buffer(55, cap_style=2),
                          vshade(C_VEN, 0.35, 0.3, 0), (darken(C_VEN, 0.5), 1.5), '!!VenaProfunda')
    if st.get('clot'):
        A['clot'] = circles(s, F, [(510, 620, 45, 140)], shade('6E1A12', 0.3, 0.3), ('3B0D08', 1.5), '!!Trombo')
    if st.get('emb'):
        A['emb'] = circles(s, F, [(515, 250, 35, 55)], shade('6E1A12', 0.3, 0.3), ('3B0D08', 1.5), '!!Embolo')
    return A


# =============================================================== PACIENTE (silueta)
def patient_back(s, x, y, h, name='!!Paciente'):
    """paciente sentado de espaldas, inclinado hacia adelante con brazos apoyados"""
    F = Frame(x, y, h * 0.9, h)
    g = s.group_start(name)
    circles(s, F, [(500, 120, 105, 115)], shade('E0AC80', 0.3, 0.2), ('8E5B3A', 2))
    torso = Polygon(catmull([(330, 250), (670, 250), (820, 330), (800, 700), (740, 980), (260, 980), (200, 700), (180, 330)], True, 6))
    draw_poly(s, F, torso, shade(C_SKIN, 0.3, 0.2, (50, 30)), ('8E5B3A', 2.5))
    draw_lines(s, F, [catmull([(500, 260), (505, 600), (500, 960)], False, 5)], 'C9915F', 2.5, dash='dash')
    draw_lines(s, F, [catmull([(340, 300), (300, 420), (330, 560)], False, 5), catmull([(660, 300), (700, 420), (670, 560)], False, 5)],
               'C9915F', 2)
    return s.group_end(), F




# =============================================================== ESTETOSCOPIO
def stetho(s, x, y, d, name='!!Estetoscopio'):
    g = s.group_start(name)
    s.arrow([(x + d * 0.5, y + d * 0.1), (x + d * 0.9, y - d * 0.6), (x + d * 1.4, y - d * 0.9)], '2C3E50', 4.5, tail=None, curve=True)
    s.shape(x, y, d, d, 'ellipse', vshade('BDC3C7', 0.4, 0.3), (INK, 2), SOFT)
    s.shape(x + d * 0.18, y + d * 0.18, d * 0.64, d * 0.64, 'ellipse', 'ECF0F1', ('7F8C8D', 1.5), False)
    return s.group_end()


# =============================================================== TAC AXIAL ESQUEMÁTICA
def ct_axial(s, X, Y, W, H, st=None, prefix='!!TAC'):
    """corte axial esquemático (paciente en decúbito supino: anterior arriba; derecha del paciente a la izquierda).
    st: fluidR (0..1 semiluna posterior declive) · loc (tabicado) · airR (aire anterior) · hydroR (nivel) ·
        pneumoperi · thick (engrosamiento nodular) · nodules"""
    st = st or {}
    F = Frame(X, Y, W, H)
    A = {'F': F}
    A['bg'] = s.shape(X, Y, W, H, 'rect', '0B0B0B', ('5A5A5A', 2), False, name=prefix + 'Pantalla')
    body = Polygon(catmull([(500, 90), (760, 130), (920, 300), (950, 520), (880, 760), (700, 900), (500, 920), (300, 900), (120, 760), (50, 520), (80, 300), (240, 130)], True, 6))
    A['body'] = draw_poly(s, F, body, ('rad', [(0, '8A8A8A'), (100, '6E6E6E')], (50, 50)), None, prefix + 'Cuerpo')
    lr = Polygon(catmull([(380, 230), (440, 330), (450, 560), (400, 790), (280, 820), (170, 700), (150, 480), (210, 290)], True, 6)).buffer(0)
    ll = Polygon(catmull([(620, 230), (700, 290), (810, 470), (820, 700), (720, 820), (610, 800), (570, 640), (600, 460)], True, 6)).buffer(0)
    L = lr
    c = st.get('airR', 0)
    lungR = lr
    if c:
        lungR = Polygon([(420 + (x - 420) * (1 - 0.6 * c), 800 + (y - 800) * (1 - 0.55 * c)) for x, y in lr.exterior.coords]).buffer(0)
    for nm_, P in (('PulmonD', lungR), ('PulmonI', ll)):
        g = s.group_start(prefix + nm_)
        draw_poly(s, F, P, ('rad', [(0, '262626'), (100, '1A1A1A')], (50, 50)), None)
        rnd = random.Random(len(nm_))
        b = P.bounds
        pts = []
        for _ in range(28):
            px = rnd.uniform(b[0], b[2]); py = rnd.uniform(b[1], b[3])
            if P.contains(Point(px, py).buffer(8)):
                pts.append((px, py, rnd.uniform(3, 6)))
        circles(s, F, pts, '7A7A7A', None)
        A[nm_] = s.group_end()
    A['heart'] = draw_poly(s, F, Polygon(catmull([(470, 330), (600, 360), (640, 470), (580, 560), (460, 540), (420, 430)], True, 6)),
                           ('rad', [(0, 'B5B5B5'), (100, '9A9A9A')], (50, 50)), None, prefix + 'Corazon')
    if st.get('pneumoperi'):
        hp = Polygon(catmull([(470, 330), (600, 360), (640, 470), (580, 560), (460, 540), (420, 430)], True, 6))
        A['peri'] = draw_poly(s, F, hp.buffer(22).difference(hp.buffer(4)), '000000', ('D0D0D0', 1.25), prefix + 'Neumopericardio')
    A['spine'] = circles(s, F, [(500, 770, 70, 65)], ('rad', [(0, 'FFFFFF'), (100, 'D9D9D9')], (50, 50)), None, prefix + 'Vertebra')
    A['aorta'] = circles(s, F, [(560, 640, 38)], 'A6A6A6', None, prefix + 'Aorta')
    f = st.get('fluidR', 0)
    if c:
        air = lr.buffer(10).difference(lungR.buffer(2))
        if st.get('hydroR'):
            air = air.difference(sbox(0, 640, 1000, 1000))
        A['air'] = draw_poly(s, F, air, '000000', None, prefix + 'Aire')
        A['line'] = draw_lines(s, F, ring_line(biggest(lungR)), 'E0E0E0', 1.5, prefix + 'LineaPleural')
    if f:
        y0 = 820 - 520 * f
        cres = lr.buffer(26).difference(lr.buffer(-4)).union(lr.buffer(22).intersection(sbox(0, y0 + 60, 1000, 1000))).intersection(sbox(0, y0, 1000, 1000))
        cres = cres.intersection(body.buffer(-25))
        if st.get('hydroR'):
            cres = lr.buffer(10).intersection(sbox(0, 640, 1000, 1000))
        A['fluid'] = draw_poly(s, F, cres, ('lin', [(0, 'C9C9C9'), (100, 'E6E6E6')], 90), None, prefix + 'Liquido')
        if st.get('loc'):
            sl = [[(200, 640), (250, 700)], [(300, 760), (320, 820)], [(420, 700), (450, 760)]]
            A['septa'] = draw_lines(s, F, sl, 'FFFFFF', 2.5, prefix + 'Tabiques')
    if st.get('thick'):
        bumps = [(x, y, 22, 18) for x, y in list(lr.buffer(14).exterior.coords)[::14]]
        A['thick'] = circles(s, F, bumps, ('rad', [(0, 'F0F0F0'), (100, 'BDBDBD')], (50, 50)), None, prefix + 'Engrosamiento')
    A['ptR'] = F.p(230, 720); A['ptAir'] = F.p(300, 260); A['ptHeart'] = F.p(530, 450)
    label(s, *F.p(20, 20), F.sx(300), F.sy(60), 'ANTERIOR', 10, 'BFBFBF', align='l', name=prefix + 'Rótulo')
    return A
