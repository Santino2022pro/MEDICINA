# -*- coding: utf-8 -*-
"""Capa de estilo «INTEGRACIÓN METABÓLICA»: fondos geométricos multicolores, títulos negros de pincel,
recuadros amarillos con borde negro y texto rojo, flechas negras y mapas bioquímicos animables."""
from lib import *
from ui import *
from ill import *
from mol3d import *

# ---------------------------------------------------------------- paleta de la referencia
CYAN = '00B0F0'
REDBG = 'C00000'
GREENBG = '92D050'
PEACHBG = 'F8CBAD'
BLUEBG2 = 'BDD7EE'
PINKBG = 'FF8B8B'
SALBG = 'F4B6A6'
YELBG2 = 'FFE699'
LIME = 'C5E0B4'
BOX = 'FFC000'
BOXT = 'C00000'
SALBOX = 'F4877F'
GRNBOX = '92D050'
LBOX = 'FFF2CC'

SCHEMES = {
    'cover': [(CYAN, 0, 0, .19, 1), (WHITE, .19, 0, .8, 1), (REDBG, .8, 0, 1, 1)],
    'cyan': [(CYAN, 0, 0, .54, 1), (WHITE, .54, 0, 1, 1), (PINKBG, .54, 0, 1, .16)],
    'cyanR': [(WHITE, 0, 0, .46, 1), (CYAN, .46, 0, 1, 1), (PINKBG, 0, .84, .46, 1)],
    'green': [(GREENBG, 0, 0, .44, 1), (WHITE, .44, 0, 1, 1), (PINKBG, .44, .82, 1, 1)],
    'greenR': [(WHITE, 0, 0, .56, 1), (GREENBG, .56, 0, 1, 1), (PINKBG, 0, 0, .56, .14)],
    'peach': [(PEACHBG, 0, 0, .5, 1), (BLUEBG2, .5, 0, 1, 1)],
    'peachW': [(PEACHBG, 0, 0, .34, 1), (BLUEBG2, .34, 0, 1, 1)],
    'blue': [(BLUEBG2, 0, 0, .62, 1), (PEACHBG, .62, 0, 1, 1)],
    'pink': [(SALBG, 0, 0, .5, 1), (WHITE, .5, 0, 1, 1), (CYAN, .5, .86, 1, 1)],
    'yellow': [(YELBG2, 0, 0, .4, 1), (WHITE, .4, 0, 1, 1), (CYAN, .4, 0, 1, .14)],
    'lime': [(LIME, 0, 0, .5, 1), (PEACHBG, .5, 0, 1, 1)],
    'white': [(WHITE, 0, 0, 1, 1), (CYAN, 0, 0, .07, 1), (REDBG, .93, 0, 1, 1)],
    'band': [(CYAN, 0, 0, 1, .5), (PEACHBG, 0, .5, 1, 1)],
}

UNITS = {
    0: ('DIABETES · OBESIDAD · TEJIDO ADIPOSO', ['cyan', 'peach', 'green']),
    1: ('UNIDAD I · BASES BIOQUÍMICAS', ['cyan', 'peach', 'green', 'blue']),
    2: ('UNIDAD II · CETOACIDOSIS (CASO 11)', ['peach', 'cyanR', 'pink', 'green']),
    3: ('UNIDAD III · EHH (CASO 12)', ['blue', 'cyan', 'peachW', 'greenR']),
    4: ('UNIDAD IV · CAD FRENTE A EHH', ['band', 'peach', 'cyan']),
    5: ('UNIDAD V · TEJIDO ADIPOSO', ['green', 'peach', 'yellow', 'cyanR']),
    6: ('UNIDAD VI · APETITO Y GASTO', ['cyan', 'pink', 'lime', 'blue']),
    7: ('UNIDAD VII · OBESIDAD (CASO 20)', ['peach', 'green', 'cyanR', 'yellow']),
    8: ('UNIDAD VIII · TRATAMIENTO', ['greenR', 'peachW', 'cyan', 'pink']),
    9: ('UNIDAD IX · SÍNDROME METABÓLICO', ['pink', 'blue', 'green', 'cyan']),
    10: ('UNIDAD X · PRÁCTICA APLICADA', ['yellow', 'peach', 'cyanR', 'lime']),
    11: ('CIERRE E INTEGRACIÓN', ['cyan', 'peach', 'green']),
}
_CYCLE = {}

GLOWW = '<a:effectLst><a:glow rad="101600"><a:srgbClr val="FFFFFF"><a:alpha val="70000"/></a:srgbClr></a:glow></a:effectLst>'


def background(s, scheme):
    for i, (c, x0, y0, x1, y1) in enumerate(SCHEMES[scheme]):
        s.shape(x0 * SW, y0 * SH, (x1 - x0) * SW, (y1 - y0) * SH, 'rect', c, None, False, name='!!Fondo %d' % (i + 1))


def upg(text):
    """mayúsculas sin tocar letras griegas, sub/superíndices ni unidades protegidas"""
    out = []
    for tok in re.split(r'(\^\{[^}]*\}|_\{[^}]*\}|\bmTORC\d\b|\bmV\b|\bmg/dL\b|\bkg/m²\b|\bpH\b|\bpCO₂\b|\bHbA1c\b|\bmOsm/kg\b|\bmEq/L\b|\bmmHg\b)', text):
        if not tok or tok.startswith('^{') or tok.startswith('_{') or re.fullmatch(r'mTORC\d|mV|mg/dL|kg/m²|pH|pCO₂|HbA1c|mOsm/kg|mEq/L|mmHg', tok):
            out.append(tok)
        else:
            out.append(''.join(c if c in 'αβγδεκλμπστφωₐ₀₁₂₃₄₅₆₇₈₉⁺⁻²³' else c.upper() for c in tok))
    return ''.join(out)


def btitle(s, text, size=34, y=0.1, x=0.35, w=None, color=INK, name='Título', align='c'):
    """título negro de pincel (Permanent Marker) con halo blanco, como la referencia"""
    w = w or (SW - 2 * x)
    t = upg(text)
    sz = size
    while max(text_w(plain(l), F_TITLE, False, sz) for l in t.split('\n')) > w - 0.2 and sz > 22:
        sz -= 1
    lines = wrap_lines(t, w - 0.2, sz, F_TITLE, False)
    h = sz / 72 * 1.3 * lines + 0.12
    return s.shape(x, y, w, h, 'rect', None, None, False, t, sz, F_TITLE, color, False, align, 'm', (0.05, 0, 0.05, 0),
                   name=name, reff=GLOWW, fit=True, minsize=18, lnspc=0.92)


def utag(s, text):
    s.shape(0.18, SH - 0.38, text_w(text, F_HEAD, True, 9.5) + 0.3, 0.26, 'rect', BOX, (INK, 1.0), False, text, 9.5, F_HEAD, INK, True,
            'c', 'm', (0.03, 0, 0.03, 0), name='Etiqueta sección', fit=False)


def pnum(s, n):
    s.shape(SW - 0.62, SH - 0.4, 0.44, 0.28, 'rect', WHITE, (INK, 1.0), False, str(n), 10, F_HEAD, INK, True, 'c', 'm',
            (0, 0, 0, 0), name='Número', fit=False)


def new(D, unit, ttl, scheme=None, morph=False, tsize=34):
    lab, cyc = UNITS[unit]
    if scheme is None:
        k = _CYCLE.get(unit, 0)
        scheme = cyc[k % len(cyc)]
        _CYCLE[unit] = k + 1
    s = D.new(WHITE)
    s.unit = unit
    s.morph = morph
    s.scheme = scheme
    background(s, scheme)
    if ttl:
        btitle(s, ttl, tsize)
    utag(s, lab)
    return s


# ---------------------------------------------------------------- recuadros metabólicos
KINDS = {
    'y': (BOX, BOXT), 'Y': (BOX, INK), 's': (SALBOX, INK), 'g': (GRNBOX, INK), 'w': (WHITE, INK), 'b': ('9DC3E6', INK),
    'r': ('C00000', WHITE), 'k': ('262626', WHITE), 'l': (LBOX, INK), 'p': ('D9C3E9', INK), 'c': ('A9E3F7', INK),
}


def mbox(s, x, y, w, h, text, kind='y', size=15, name=None, bold=True, align='c', anchor='m', lw=2.0, shadow=SHD, caps=None,
         minsize=10, geom='rect', spc=2):
    f, tc = KINDS[kind]
    if caps is None:
        caps = kind in ('y',) and len(plain(text)) < 40
    t = smart_upper(text) if caps else text
    return s.shape(x, y, w, h, geom, f, (INK, lw), shadow, t, size, F_HEAD, tc, bold, align, anchor, (0.07, 0.03, 0.07, 0.03),
                   name=name or ('Recuadro ' + plain(text)[:22]), minsize=minsize, spc=spc)


def tbox(s, x, y, w, h, text, size=15, fill=WHITE, head=None, hkind='y', name=None, minsize=11, anchor='t', lw=1.5, spc=4):
    """cuadro de texto explicativo (borde negro) con cabecera opcional amarilla"""
    if head:
        g = s.group_start(name or ('Cuadro ' + plain(head)[:22]))
        s.shape(x, y + 0.22, w, h - 0.22, 'rect', fill, (INK, lw), SHD, text, size, F_BODY, INK, False, 'l', anchor,
                (0.14, 0.3, 0.14, 0.08), minsize=minsize, spc=spc)
        hf, ht = KINDS[hkind]
        hw = min(text_w(plain(smart_upper(head)), F_HEAD, True, 14) + 0.4, w - 0.2)
        s.shape(x + 0.15, y, hw, 0.42, 'rect', hf, (INK, 1.5), False, smart_upper(head), 14, F_HEAD, ht, True, 'c', 'm',
                (0.05, 0, 0.05, 0), minsize=9)
        return s.group_end()
    return s.shape(x, y, w, h, 'rect', fill, (INK, lw), SHD, text, size, F_BODY, INK, False, 'l', anchor, (0.14, 0.08, 0.14, 0.08),
                   name=name, minsize=minsize, spc=spc)


def pearl(s, x, y, w, h, text, size=15, name='Perla clínica'):
    return s.shape(x, y, w, h, 'rect', 'C00000', (INK, 2.0), SHD, text, size, F_BODY, WHITE, False, 'l', 'm',
                   (0.15, 0.06, 0.15, 0.06), name=name, minsize=11)


def formula(s, x, y, w, h, text, size=24, name='Fórmula', fill=WHITE, color=INK):
    return s.shape(x, y, w, h, 'rect', fill, (INK, 2.5), SHD, text, size, F_HEAD, color, True, 'c', 'm', (0.1, 0.03, 0.1, 0.03),
                   name=name, minsize=12)


def lab(s, x, y, w, h, text, size=13, color=INK, bold=True, align='c', anchor='m', name=None, glow=True):
    return s.shape(x, y, w, h, 'rect', None, None, False, text, size, F_HEAD, color, bold, align, anchor, (0, 0, 0, 0),
                   name=name, reff=GLOWW if glow else '', minsize=9)


def elabel(s, x, y, text, size=11.5, fill='FCE4D6', name=None, w=None):
    """rótulo de flecha (enzima/proceso) estilo referencia: recuadro pequeño con borde"""
    w = w or (text_w(plain(text), F_HEAD, True, size) + 0.24)
    return s.shape(x, y, w, size / 72 * 1.55, 'rect', fill, (INK, 0.75), False, text, size, F_HEAD, INK, True, 'c', 'm',
                   (0.03, 0, 0.03, 0), name=name or ('Rótulo ' + plain(text)[:18]), minsize=8, fit=False)


# ---------------------------------------------------------------- mapas animables
def _anchor(a, b):
    ax, ay, aw, ah = a; bx, by, bw, bh = b
    acx, acy = ax + aw / 2, ay + ah / 2; bcx, bcy = bx + bw / 2, by + bh / 2
    dx, dy = bcx - acx, bcy - acy
    if abs(dy) > 0.01 and (abs(dx) < (aw + bw) / 2 * 0.9 or abs(dy) * 1.6 > abs(dx)) and not (by < ay + ah and by + bh > ay):
        if dy > 0:
            return (acx + min(max(dx * 0.25, -aw / 3), aw / 3), ay + ah + 0.04), (bcx - min(max(dx * 0.25, -bw / 3), bw / 3), by - 0.04), 't'
        return (acx + min(max(dx * 0.25, -aw / 3), aw / 3), ay - 0.04), (bcx - min(max(dx * 0.25, -bw / 3), bw / 3), by + bh + 0.04), 'b'
    if dx > 0:
        return (ax + aw + 0.04, acy), (bx - 0.04, bcy), 'l'
    return (ax - 0.04, acy), (bx + bw + 0.04, bcy), 'r'


def graph(s, nodes, edges, order=None, anim='fade', first_step=None):
    """nodes: {k: (x, y, w, h, texto, kind[, size])}; edges: [(a, b, {opts})]
    opts: lab, col, inh, pts, curve, w, dash, lx, ly, both.
    order: lista de pasos; cada paso es lista de tokens 'k' (nodo) o 'a>b' (arista). Devuelve dict de ids."""
    ids = {}
    geo = {}
    for k, v in nodes.items():
        x, y, w, h, t, kind = v[:6]
        size = v[6] if len(v) > 6 else 14
        geo[k] = (x, y, w, h)
    eids = {}
    for a, b, *o in edges:
        o = o[0] if o else {}
        col = o.get('col', INK)
        if o.get('pts'):
            pts = o['pts']; d = o.get('dir', 'l')
        else:
            p1, p2, d = _anchor(geo[a], geo[b])
            pts = [p1, p2]
            if o.get('mid'):
                pts = [p1, o['mid'], p2]
        name = 'Flecha %s→%s' % (a, b)
        if o.get('inh'):
            eid = s.inhib(pts, o.get('col', INH), o.get('w', 2.75), name=name)
        elif o.get('lab'):
            g = s.group_start(name)
            s.arrow(pts, col, o.get('w', 2.25), curve=o.get('curve', False), dash=o.get('dash'), head='triangle' if o.get('both') else None)
            lw = text_w(plain(o['lab']), F_HEAD, True, o.get('ls', 11)) + 0.24
            mx = sum(p[0] for p in pts) / len(pts); my = sum(p[1] for p in pts) / len(pts)
            elabel(s, o.get('lx', mx - lw / 2 + o.get('ox', 0)), o.get('ly', my - 0.14 + o.get('oy', 0)), o['lab'], o.get('ls', 11),
                   fill=o.get('lf', 'FCE4D6'))
            eid = s.group_end()
        else:
            eid = s.arrow(pts, col, o.get('w', 2.25), curve=o.get('curve', False), dash=o.get('dash'),
                          head='triangle' if o.get('both') else None, name=name)
        eids['%s>%s' % (a, b)] = (eid, d)
    for k, v in nodes.items():
        x, y, w, h, t, kind = v[:6]
        size = v[6] if len(v) > 6 else 14
        if kind == 'img':
            ids[k] = s.pic(t, x, y, w, h, name='Ícono ' + k)
        elif kind == 'lab':
            ids[k] = lab(s, x, y, w, h, t, size, name='Rótulo ' + k)
        else:
            ids[k] = mbox(s, x, y, w, h, t, kind, size, name='Nodo ' + k)
    ids.update({k: v[0] for k, v in eids.items()})
    if order:
        for st in order:
            effs = []
            for i, tok in enumerate(st):
                if '>' in tok:
                    eid, d = eids[tok]
                    effs.append(wipe(eid, d, after=bool(effs), dur=500))
                else:
                    f = zoom if anim == 'zoom' else fade
                    effs.append(f(ids[tok], after=bool(effs) and not ('>' in st[i - 1] and False), dur=400))
            s.step(*effs)
    return ids


def steps_panel(s, x, y, w, items, size=14, gap=0.1, kinds=None, h=None, name='Paso', numbered=True, fill=WHITE, anim=True):
    """lista vertical de recuadros numerados que se revelan uno por clic"""
    ids = []
    hh = h
    cy = y
    for i, t in enumerate(items):
        if h is None:
            hh = text_h(t, w - 0.75, size, F_BODY, False) + 0.18
            hh = max(hh, 0.5)
        g = s.group_start('%s %d' % (name, i + 1))
        s.shape(x, cy, w, hh, 'rect', (kinds[i] if kinds else fill), (INK, 1.25), SHD, t, size, F_BODY, INK, False, 'l', 'm',
                (0.6 if numbered else 0.12, 0.04, 0.1, 0.04), minsize=10)
        if numbered:
            s.shape(x + 0.1, cy + hh / 2 - 0.19, 0.38, 0.38, 'ellipse', BOX, (INK, 1.25), False, str(i + 1), 13, F_HEAD, INK, True,
                    'c', 'm', (0, 0, 0, 0), fit=False)
        ids.append(s.group_end())
        cy += hh + gap
    if anim:
        for g in ids:
            s.step(fade(g))
    return ids, cy


def divider(D, unit, roman, ttl, sub, topics, art=None, notes='', scheme='cover'):
    lab_, _ = UNITS[unit]
    s = D.new(WHITE)
    s.unit = unit; s.morph = False; s.scheme = scheme
    background(s, scheme)
    s.shape(0.45, 0.35, 2.0, 0.55, 'rect', BOX, (INK, 2.0), SHD, 'UNIDAD ' + roman if roman else 'INICIO', 20, F_HEAD, BOXT, True, 'c', 'm',
            name='Etiqueta unidad', fit=False)
    btitle(s, ttl, 50, y=1.05, x=2.7, w=7.9, name='Título unidad')
    s.text(2.75, 3.15, 7.8, 0.5, sub, 19, F_HEAD, INK, True, 'c', 'm', name='Subtítulo unidad')
    n = len(topics)
    cols = 2 if n > 5 else 1
    per = (n + cols - 1) // cols
    bw = 7.6 / cols - 0.1 * (cols - 1)
    ids = []
    for i, t in enumerate(topics):
        c = i // per; r = i % per
        ids.append(mbox(s, 2.85 + c * (bw + 0.2), 3.85 + r * 0.62, bw, 0.5, t, 'y', 14, caps=False, name='Tema %d' % (i + 1)))
    if art:
        art(s)
    s.step(*[fade(g, after=i > 0, dur=250) for i, g in enumerate(ids)])
    if notes:
        s.note(notes)
    return s


def exercise(D, unit, num, ttl, datos, interp, form, calc, result, meaning, notes, scheme=None):
    """DATOS → INTERPRETACIÓN → FÓRMULA → CÁLCULO → RESULTADO → SIGNIFICADO (revelado progresivo)"""
    s = new(D, unit, 'Ejercicio %d · %s' % (num, ttl), scheme)
    blocks = [('DATOS', datos, 'y'), ('INTERPRETACIÓN', interp, 'g'), ('FÓRMULA', form, 's'), ('CÁLCULO', calc, 'b'),
              ('RESULTADO', result, 'Y'), ('SIGNIFICADO FISIOLÓGICO', meaning, 'r')]
    ids = []
    pos = [(0.4, 1.15, 6.1, 1.75), (6.85, 1.15, 6.1, 1.75), (0.4, 3.1, 6.1, 1.55), (6.85, 3.1, 6.1, 1.55), (0.4, 4.85, 6.1, 1.95),
           (6.85, 4.85, 6.1, 1.95)]
    for (h, t, k), (x, y, w, hh) in zip(blocks, pos):
        if not t:
            continue
        g = s.group_start('Bloque ' + h.lower())
        f, tc = KINDS[k]
        s.shape(x, y + 0.22, w, hh - 0.22, 'rect', WHITE if k != 'r' else 'FDE2E2', (INK, 1.5), SHD, t, 15, F_BODY, INK, False, 'l', 'm',
                (0.14, 0.26, 0.14, 0.06), minsize=10.5, spc=3)
        hw = text_w(h, F_HEAD, True, 13) + 0.4
        s.shape(x + 0.15, y, hw, 0.4, 'rect', f, (INK, 1.5), False, h, 13, F_HEAD, tc, True, 'c', 'm', (0.04, 0, 0.04, 0), fit=False)
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note(notes)
    return s


def mcq(D, unit, qs, scheme=None, title='Preguntas de opción múltiple'):
    """qs: [(n, enunciado, [A,B,C,D], idx_correcta, razonamiento)] – 2 por diapositiva; respuesta revelada por clic"""
    s = new(D, unit, title, scheme)
    y = 1.15
    hq = (SH - 1.6) / len(qs)
    notes = []
    for n, q, opts, ok, why in qs:
        g = s.group_start('Pregunta %d' % n)
        s.shape(0.4, y, 0.6, 0.6, 'ellipse', BOX, (INK, 2), SHD, str(n), 20, F_POP, BOXT, False, 'c', 'm', (0, 0, 0, 0), fit=False)
        s.shape(1.15, y, 11.8, 0.62, 'rect', WHITE, (INK, 1.5), SHD, q, 15.5, F_BODY, INK, True, 'l', 'm', (0.12, 0.02, 0.12, 0.02), minsize=11)
        s.group_end()
        oid = []
        for i, o in enumerate(opts):
            ox = 1.15 + (i % 2) * 5.95; oy = y + 0.75 + (i // 2) * 0.55
            oid.append(s.shape(ox, oy, 5.85, 0.48, 'rect', LBOX, (INK, 1.0), False, '%s) %s' % ('ABCD'[i], o), 13.5, F_BODY, INK, False,
                               'l', 'm', (0.1, 0.02, 0.1, 0.02), minsize=10, name='Opción %d%s' % (n, 'ABCD'[i])))
        okx = 1.15 + (ok % 2) * 5.95; oky = y + 0.75 + (ok // 2) * 0.55
        mark = s.shape(okx - 0.04, oky - 0.04, 5.93, 0.56, 'rect', None, ('00A651', 4.0), False, name='Marca correcta %d' % n)
        wy = y + 1.88
        why_id = s.shape(1.15, wy, 11.8, hq - 2.05, 'rect', 'E2F0D9', (INK, 1.0), False, '**Respuesta %s.** %s' % ('ABCD'[ok], why), 13.5,
                         F_BODY, INK, False, 'l', 'm', (0.12, 0.02, 0.12, 0.02), minsize=10, name='Razonamiento %d' % n)
        s.step(zoom(mark), fade(why_id, after=True))
        notes.append('Pregunta %d: respuesta %s. %s' % (n, 'ABCD'[ok], why))
        y += hq
    s.note('Cada clic marca la opción correcta y muestra el razonamiento. ' + ' '.join(notes))
    return s


def organ_pic(s, key, x, y, w=None, h=None, name=None):
    return s.pic(key, x, y, w, h, name=name)


def fitpic(s, key, x, y, w, h, name=None):
    """imagen centrada dentro de la caja (x, y, w, h) sin deformar"""
    from PIL import Image
    fn = os.path.join(IMGDIR, key + '.png')
    iw, ih = Image.open(fn).size
    k = min(w / iw, h / ih)
    ww, hh = iw * k, ih * k
    return s.pic(key, x + (w - ww) / 2, y + (h - hh) / 2, ww, hh, name=name)


# ---------------------------------------------------------------- mapas fisiológicos por etapas (Morph) + sistema completo
def _map_elem(s, e, idx):
    kind = e[0]
    if kind == 'a':      # ('a', pts, label, color, (lx, ly) | None, dash)
        _, pts, txt, col = e[:4]
        lpos = e[4] if len(e) > 4 else None
        dash = e[5] if len(e) > 5 else None
        g = s.group_start('!!Mapa elemento %d' % idx)
        if col == INH:
            s.inhib(pts)
        else:
            s.arrow(pts, col, 3.0, dash=dash)
        if txt:
            if lpos is None:
                mx = sum(p[0] for p in pts) / len(pts); my = sum(p[1] for p in pts) / len(pts)
                lw = text_w(plain(txt), F_HEAD, True, 11.5) + 0.24
                lpos = (mx - lw / 2, my - 0.15)
            elabel(s, lpos[0], lpos[1], txt, 11.5, fill=WHITE)
        return s.group_end()
    if kind == 'b':      # ('b', x, y, w, h, text, kind[, size])
        _, x, y, w, h, t, k = e[:7]
        return mbox(s, x, y, w, h, t, k, e[7] if len(e) > 7 else 13, caps=False, name='!!Mapa elemento %d' % idx, minsize=9)
    if kind == 't':      # ('t', x, y, w, h, text[, size])
        _, x, y, w, h, t = e[:6]
        return tbox(s, x, y, w, h, t, e[6] if len(e) > 6 else 13, name='!!Mapa elemento %d' % idx, anchor='m', minsize=9)
    raise ValueError(e)


def map_series(D, unit, title, scheme, organs, stages, notes, final_note, concl, stage_titles=None):
    """organs: [(img, x, y, w, rótulo, lx, ly)]; stages: [[elementos]]; genera una diapositiva por etapa (Morph) y una final"""
    n = len(stages)
    out = []
    for k in range(n + 1):
        final = k == n
        st = (stage_titles[k] if stage_titles and not final else ('sistema completo' if final else 'etapa %d' % (k + 1)))
        s = new(D, unit, '%s · %s' % (title, st), scheme, morph=k > 0)
        for i, (img, x, y, w, l, lx, ly) in enumerate(organs):
            s.pic(img, x, y, w, name='!!Órgano %s' % l)
            mbox(s, lx, ly, text_w(l, F_HEAD, True, 12.5) + 0.32, 0.38, l, 'y', 12.5, name='!!Rótulo órgano %s' % l)
        idx = 0
        for j, stage in enumerate(stages):
            if j > k:
                break
            for e in stage:
                el = _map_elem(s, e, idx)
                idx += 1
                if j == k and not final:
                    if e[0] == 'a':
                        s.step(fade(el, dur=500))
                    else:
                        s.step(zoom(el))
        if final:
            p = pearl(s, concl[0], concl[1], concl[2], concl[3], concl[4], concl[5] if len(concl) > 5 else 15, name='!!Conclusión mapa')
            s.step(zoom(p))
            s.note(final_note)
        else:
            s.note(notes[k])
        out.append(s)
    return out
