# -*- coding: utf-8 -*-
"""Identidad gráfica de la serie (modelo «Ontogenia»): etiqueta blanca de
sección, barra de título celeste con viñeta, recuadros planos de colores
intensos con borde negro, rótulos manuscritos y tablas construidas con
formas (para revelarlas fila por fila)."""
from lib import *
import math

# ---------------------------------------------------------------- paleta de la referencia
BLUEMID = '6F93D2'    # azul medio de fondo
PALE = 'DCE6F2'       # celeste pálido (barra de título)
CEL = '00B0F0'        # celeste intenso
TURQ = '33CCCC'       # turquesa
GREEN = '00B050'      # verde brillante
LGREEN = '92D050'     # verde claro
RED = 'FF0000'        # rojo
YELLOW = 'FFFF00'     # amarillo
GOLD = 'FFC000'       # amarillo dorado
ORANGE = 'F79646'     # naranja
LBLUE = 'BDD7EE'      # azul claro
WHITE = 'FFFFFF'
INK = '000000'
LILAC = 'CCC0DA'
PINKB = 'F4B6C2'
CREAM = 'FFF2CC'

# código anatómico (constante en toda la presentación)
C_PARIETAL = '009E9E'   # pleura parietal (verde azulado)
C_VISCERAL = '8E44AD'   # pleura visceral (morado)
C_LUNG = 'F2A0A8'       # parénquima pulmonar
C_FLUID = '7CC8F0'      # líquido seroso / trasudado
C_EXUD = 'E9C46A'       # exudado (ámbar turbio)
C_PUS = 'E2C85A'        # pus
C_BLOOD = 'B22222'      # hemorrágico
C_AIR = 'F7FCFF'        # aire pleural
C_LYMPH = '3BAA4A'      # linfático
C_ART = 'D63A3A'        # arterial / capilar
C_VEN = '2F6DB5'        # venoso
C_BONE = 'F3E6C4'       # hueso
C_MUSCLE = 'C4554D'     # músculo
C_SKIN = 'F5CBA7'       # piel / partes blandas


def lighten(c, f):
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    return '%02X%02X%02X' % tuple(int(v + (255 - v) * f) for v in (r, g, b))


def darken(c, f):
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    return '%02X%02X%02X' % tuple(int(v * (1 - f)) for v in (r, g, b))


def shade(c, hl=0.5, dk=0.28, focus=(32, 28)):
    """volumen suave: degradado radial claro-medio-oscuro"""
    return ('rad', [(0, lighten(c, hl)), (55, c), (100, darken(c, dk))], focus)


def vshade(c, hl=0.35, dk=0.3, ang=90):
    """sombreado cilíndrico (tubos, vasos, costillas)"""
    return ('lin', [(0, darken(c, dk)), (30, lighten(c, hl)), (55, c), (100, darken(c, dk))], ang)



# ---------------------------------------------------------------- mayúsculas seguras
GREEK = set('αβγδεζηθικλμνξοπρστυφχψωµ')
UNITS = {'pH', 'mg/dl', 'ml/kg', 'pg/ml', 'g/dl', 'mg', 'dl', 'ml', 'kg', 'cm', 'mm', 'h', 'SpO', 'U/L', 'pl/sér'}


def smart_upper(text):
    """mayúsculas que respetan letras griegas (π, σ), sub/superíndices (P_{c}) y unidades (mg/dl, pH)"""
    out = []
    for tok in re.split(r'(\^\{[^}]*\}|_\{[^}]*\}|\*\*)', text):
        if not tok or tok.startswith('^{') or tok.startswith('_{') or tok == '**':
            out.append(tok)
            continue
        for part in re.split(r'([A-Za-zÁÉÍÓÚÜÑáéíóúüñ/]+)', tok):
            if part in UNITS:
                out.append(part)
            else:
                out.append(''.join(c if c in GREEK else c.upper() for c in part))
    return ''.join(out)


BORDER = (INK, 2.25)
THIN = (INK, 1.25)


def dark_fill(f):
    return f in (RED, GREEN, '1F4E79', C_VISCERAL, C_PARIETAL, '7030A0', C_BLOOD)


# ---------------------------------------------------------------- encabezado
def header(s, tag, ttl, tsize=24):
    """etiqueta de sección (izquierda, blanca) + barra de título (derecha, celeste) con viñeta"""
    tsz = 18
    tw = min(text_w(plain(smart_upper(tag)), F_HEAD, True, tsz) + 0.42, 4.2)
    s.shape(0.18, 0.14, tw, 0.56, 'rect', WHITE, BORDER, False, smart_upper(tag), tsz, F_HEAD, INK, True, 'c', 'm',
            (0.08, 0.02, 0.08, 0.02), name='Etiqueta sección', minsize=11)
    x0 = 0.18 + tw + 0.22
    maxw = SW - 0.18 - x0
    t = '• ' + smart_upper(ttl)
    sz = tsize
    while text_w(plain(t), F_HEAD, True, sz) + 0.4 > maxw and sz > 19:
        sz -= 0.5
    one = text_w(plain(t), F_HEAD, True, sz) + 0.4 <= maxw
    w = min(max(text_w(plain(t), F_HEAD, True, sz) + 0.5, 4.5), maxw) if one else maxw
    h = 0.64 if one else 0.98
    x = SW - 0.18 - w
    return s.shape(x, 0.1, w, h, 'rect', PALE, BORDER, False, t, sz, F_HEAD, INK, True, 'c', 'm',
                   (0.12, 0.02, 0.12, 0.02), name='Título', minsize=16, lnspc=0.92)


def pagenum(s, n):
    s.shape(SW - 0.58, SH - 0.38, 0.44, 0.28, 'rect', WHITE, THIN, False, str(n), 10, F_HEAD, INK, True, 'c', 'm',
            (0, 0, 0, 0), name='Número')


# ---------------------------------------------------------------- recuadros
def box(s, x, y, w, h, text, fill=WHITE, size=15, name=None, align='c', anchor='m', bold=True, minsize=10.5,
        color=None, line=BORDER, head=None, headfill=None, spc=3, lnspc=0.95, ins=(0.1, 0.06, 0.1, 0.06), grow=True):
    """recuadro plano con borde negro; texto manuscrito negro (como la referencia)"""
    col = color or (WHITE if dark_fill(fill) else INK)
    # crecimiento automático: aprovecha el recuadro sin superar el 82 % del alto útil
    hh0 = 0.42 if head else 0
    iw = w - ins[0] - ins[2]; ih = h - hh0 - ins[1] - ins[3]
    sz = size
    while grow and sz < size + 5 and sz < 24 and fits(text, iw, ih * 0.82, sz + 0.5, F_BODY, bold, spc, lnspc):
        sz += 0.5
    size = sz
    if head:
        g = s.group_start(name or ('Recuadro ' + plain(head)[:24]))
        hh = 0.42
        s.shape(x, y + hh - 0.02, w, h - hh + 0.02, 'rect', fill, line, False, text, size, F_BODY, col, bold, align, anchor,
                ins, minsize=minsize, spc=spc, lnspc=lnspc)
        hf = headfill or WHITE
        s.shape(x, y, w, hh, 'rect', hf, line, False, smart_upper(head), min(size + 1.5, 17), F_HEAD,
                WHITE if dark_fill(hf) else INK, True, 'c', 'm', (0.06, 0, 0.06, 0), minsize=10)
        return s.group_end()
    return s.shape(x, y, w, h, 'rect', fill, line, False, text, size, F_BODY, col, bold, align, anchor, ins,
                   name=name, minsize=minsize, spc=spc, lnspc=lnspc)


def tag(s, x, y, text, fill=WHITE, size=13, w=None, h=None, name=None, line=THIN, bold=True):
    """rótulo pequeño (como «Procesos que ocurren»)"""
    tw = w or (text_w(plain(text), F_HEAD, bold, size) + 0.3)
    hh = h or size / 72 * 1.75
    return s.shape(x, y, tw, hh, 'rect', fill, line, False, text, size, F_HEAD, WHITE if dark_fill(fill) else INK, bold,
                   'c', 'm', (0.05, 0, 0.05, 0), name=name, minsize=8.5)


def label(s, x, y, w, h, text, size=13, color=INK, bold=True, align='c', name=None, anchor='m', bg=None):
    if bg:
        return s.shape(x, y, w, h, 'rect', bg, None, False, text, size, F_HEAD, color, bold, align, anchor,
                       (0.03, 0, 0.03, 0), name=name, minsize=8)
    return s.text(x, y, w, h, text, size, F_HEAD, color, bold, align, anchor, name=name, minsize=8)


def badge(s, x, y, n, d=0.42, fill=GOLD, name=None):
    return s.shape(x, y, d, d, 'ellipse', fill, BORDER, False, str(n), 15 if d >= 0.4 else 11, F_HEAD, INK, True, 'c', 'm',
                   (0, 0, 0, 0), name=name or ('Paso %s' % n), fit=False)


def callout(s, pts, text, x, y, w, h, fill=WHITE, size=12.5, name=None, color=INK, lw=1.75):
    """rótulo con línea indicadora hacia una estructura"""
    g = s.group_start(name or ('Rótulo ' + plain(text)[:22]))
    s.arrow(pts, color, lw, tail='oval')
    box(s, x, y, w, h, text, fill, size, line=THIN, ins=(0.05, 0.02, 0.05, 0.02))
    return s.group_end()


def arrow_lbl(s, pts, text=None, color=INK, w=3, size=12.5, lx=None, ly=None, lw=1.6, curve=False, dash=None, name=None,
              lcolor=None, lbg=None):
    if not text:
        return s.arrow(pts, color, w, curve=curve, dash=dash, name=name)
    g = s.group_start(name or ('Flecha ' + plain(text)[:18]))
    s.arrow(pts, color, w, curve=curve, dash=dash)
    if lx is None:
        mx = sum(p[0] for p in pts) / len(pts); my = sum(p[1] for p in pts) / len(pts)
        lx, ly = mx - lw / 2, my - 0.34
    nl = wrap_lines(text, lw, size, F_HEAD, True)
    hh = nl * size * 1.2 / 72 + 0.06
    label(s, lx, ly, lw, hh, text, size, lcolor or color, bg=lbg)
    return s.group_end()


def flow(s, items, x, y, w, h, fills=None, size=14, gap=0.32, dir='h', names=None, minsize=10.5, acolor=INK):
    """cadena de recuadros conectados; devuelve [(caja, flecha_entrante)]"""
    n = len(items); res = []
    if dir == 'h':
        bw = (w - gap * (n - 1)) / n
        for i, t in enumerate(items):
            bx = x + i * (bw + gap)
            f = (fills[i] if isinstance(fills, list) else fills) or WHITE
            a = s.arrow([(bx - gap + 0.03, y + h / 2), (bx - 0.03, y + h / 2)], acolor, 3) if i else None
            b = box(s, bx, y, bw, h, t, f, size, name=(names[i] if names else None), minsize=minsize)
            res.append((b, a))
    else:
        bh = (h - gap * (n - 1)) / n
        for i, t in enumerate(items):
            by = y + i * (bh + gap)
            f = (fills[i] if isinstance(fills, list) else fills) or WHITE
            a = s.arrow([(x + w / 2, by - gap + 0.03), (x + w / 2, by - 0.03)], acolor, 3) if i else None
            b = box(s, x, by, w, bh, t, f, size, name=(names[i] if names else None), minsize=minsize)
            res.append((b, a))
    return res


def flow_anim(s, res, per=1, dir='h'):
    k = 0
    cur = []
    for b, a in res:
        if a:
            cur += [wipe(a, 'l' if dir == 'h' else 't', after=bool(cur)), fade(b, after=True)]
        else:
            cur += [fade(b, after=bool(cur))]
        k += 1
        if k % per == 0:
            s.step(*cur); cur = []
    if cur:
        s.step(*cur)


# ---------------------------------------------------------------- tabla de formas (animable por filas)
def gtable(s, x, y, w, rows, colw=None, size=13, head_fill=CEL, fills=(WHITE, 'EAF2FB'), first_fill=PALE,
           rowh=0.42, name='Tabla', col_fills=None, heights=None, hsize=None, align='l', minsize=9.5, first_bold=True, fill_to=None):
    """tabla hecha de rectángulos; devuelve (ids_de_fila_agrupados, alto_total).
    Cada fila es un grupo para revelarla con un clic; la fila 0 es el encabezado."""
    ncol = len(rows[0])
    colw = colw or [1] * ncol
    tot = sum(colw); colw = [c * w / tot for c in colw]
    hs = hsize or size + 0.5
    hts = []
    for r, row in enumerate(rows):
        hh = rowh
        for c, cell in enumerate(row):
            sz = hs if r == 0 else size
            th = text_h(cell, colw[c] - 0.18, sz, F_BODY, r == 0 or (c == 0 and first_bold), 2, 0.95) + 0.14
            hh = max(hh, th)
        hts.append(hh)
    if heights:
        hts = [max(a, b) for a, b in zip(hts, heights)]
    if fill_to and sum(hts) < fill_to - y:
        extra = (fill_to - y - sum(hts)) / len(hts)
        hts = [h_ + extra for h_ in hts]
    ids = []
    yy = y
    for r, row in enumerate(rows):
        g = s.group_start('%s fila %d' % (name, r) if r else '%s encabezado' % name)
        xx = x
        for c, cell in enumerate(row):
            if r == 0:
                f = head_fill if not isinstance(head_fill, list) else head_fill[c]
                b = True; sz = hs; al = 'c'
            else:
                f = (col_fills[c] if col_fills and col_fills[c] else
                     (first_fill if (c == 0 and first_fill) else fills[(r - 1) % len(fills)]))
                b = (c == 0 and first_bold); sz = size; al = 'c' if c == 0 else align
            s.shape(xx, yy, colw[c], hts[r], 'rect', f, (INK, 1.5), False, cell, sz, F_BODY,
                    WHITE if dark_fill(f) else INK, b, al, 'm', (0.08, 0.04, 0.08, 0.04), minsize=minsize, spc=2, lnspc=0.95)
            xx += colw[c]
        ids.append(s.group_end())
        yy += hts[r]
    if yy > SH - 0.1:
        WARN.append('TABLA desborda: %s hasta %.2f' % (name, yy))
    return ids, yy - y


def table_anim(s, ids, per=1, first_with=None):
    """encabezado en un clic; luego filas de a 'per' por clic"""
    s.step(*([fade(ids[0])] + ([fade(first_with, after=True)] if first_with else [])))
    rest = ids[1:]
    for i in range(0, len(rest), per):
        grp = rest[i:i + per]
        s.step(*[wipe(g, 'l', after=bool(k), dur=450) for k, g in enumerate(grp)])
