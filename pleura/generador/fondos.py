# -*- coding: utf-8 -*-
"""Fondos anatómicos desenfocados (PNG 1600×900) al estilo de la referencia:
estructuras grandes parcialmente visibles, formas orgánicas en los bordes."""
import os, math, random
from PIL import Image, ImageDraw, ImageFilter
from anat import catmull, CAV_R, CAV_L, WALL, VESS_R, mirror

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'fondos')
Wd, Ht = 1600, 900


def hx(c, a=255):
    return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), a)


def tf(pts, ox, oy, k):
    return [(ox + x * k, oy + y * k) for x, y in pts]


def thorax_layer(ox, oy, k, lung='F2A0A8', alpha=255, bone='F3E6C4', skin='F5CBA7'):
    im = Image.new('RGBA', (Wd, Ht), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.polygon(tf(catmull(WALL, True, 6), ox, oy, k), fill=hx(skin, alpha))
    for k2 in range(9):
        y0 = 150 + k2 * 78
        for sg in (-1, 1):
            pts = catmull([(500 + sg * 30, y0), (500 + sg * 150, y0 - 30), (500 + sg * 300, y0 + 10), (500 + sg * 410, y0 + 90), (500 + sg * 440, y0 + 170)], False, 6)
            d.line(tf(pts, ox, oy, k), fill=hx(bone, alpha), width=int(10 * k))
    for cav in (CAV_R, CAV_L):
        d.polygon(tf(catmull(cav, True, 6), ox, oy, k), fill=hx(lung, alpha), outline=hx('8E44AD', alpha))
    for v in VESS_R + mirror(VESS_R):
        d.line(tf(v, ox, oy, k), fill=hx('C0606A', alpha), width=max(2, int(3 * k)))
    hp = [(470, 560), (520, 528), (590, 540), (650, 575), (695, 640), (712, 720), (690, 790), (625, 810), (540, 800), (472, 772), (448, 700), (450, 620)]
    d.polygon(tf(catmull(hp, True, 6), ox, oy, k), fill=hx('C0392B', alpha))
    d.line(tf([(458, 215), (462, 400), (468, 560)], ox, oy, k), fill=hx('2F6DB5', alpha), width=int(30 * k))
    d.line(tf([(530, 560), (522, 330), (560, 268), (612, 300), (606, 420), (600, 870)], ox, oy, k), fill=hx('D63A3A', alpha), width=int(34 * k))
    return im


def blob_pts(cx, cy, r, n=40, amp=0.06, seed=1, frill=0):
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r * (1 + amp * math.sin(3 * a + seed) + (frill * (1 if i % 2 else -1)))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def make():
    os.makedirs(OUT, exist_ok=True)
    # 1 · azul medio con pulmón gigante y membranas (páginas 9-30 de la referencia)
    im = Image.new('RGBA', (Wd, Ht), hx('6F93D2'))
    d = ImageDraw.Draw(im)
    lay = Image.new('RGBA', (Wd, Ht), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.ellipse((1050, 250, 2350, 1550), fill=hx('5B7FC0'))
    dl.ellipse((1120, 320, 2280, 1480), fill=hx('7FA2DD'))
    for i in range(14):
        a = math.radians(150 + i * 9)
        x = 1700 + 640 * math.cos(a); y = 900 + 640 * math.sin(a)
        dl.ellipse((x - 26, y - 26, x + 26, y + 26), fill=hx('4E70B0'))
    dl.ellipse((-300, 700, 500, 1300), fill=hx('5B7FC0'))
    lay = lay.filter(ImageFilter.GaussianBlur(3))
    im = Image.alpha_composite(im, lay)
    im.convert('RGB').save(os.path.join(OUT, 'azul.png'))
    # 2 · tórax colorido desenfocado (páginas 2-8: anatomía grande desenfocada)
    im = Image.new('RGBA', (Wd, Ht), hx('F7E1D7'))
    lay = thorax_layer(250, -120, 1.25)
    lay = lay.filter(ImageFilter.GaussianBlur(14))
    im = Image.alpha_composite(im, lay)
    veil = Image.new('RGBA', (Wd, Ht), (255, 255, 255, 110))
    im = Image.alpha_composite(im, veil)
    im.convert('RGB').save(os.path.join(OUT, 'torax.png'))
    # 3 · mesotelio (celeste con células en empedrado en los bordes)
    im = Image.new('RGBA', (Wd, Ht), hx('D6E9F8'))
    lay = Image.new('RGBA', (Wd, Ht), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    rnd = random.Random(4)
    for gy in range(-1, 12):
        for gx in range(-1, 20):
            cx = gx * 90 + (gy % 2) * 45 + rnd.randint(-10, 10); cy = gy * 80 + rnd.randint(-10, 10)
            edge = min(cx, Wd - cx, cy, Ht - cy)
            if edge > 170:
                continue
            dl.polygon(blob_pts(cx, cy, 44, 8, 0.12, gx * 31 + gy), fill=hx('9CC9EC'), outline=hx('3E7CB1'))
            dl.ellipse((cx - 13, cy - 8, cx + 13, cy + 8), fill=hx('5B4B9A'))
    lay = lay.filter(ImageFilter.GaussianBlur(2.5))
    im = Image.alpha_composite(im, lay)
    im.convert('RGB').save(os.path.join(OUT, 'mesotelio.png'))
    # 4 · blanco con formas orgánicas azules (página 20)
    im = Image.new('RGBA', (Wd, Ht), hx('FFFFFF'))
    lay = Image.new('RGBA', (Wd, Ht), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    pts = [(0, 900), (0, 760)] + [(x, 760 + 50 * math.sin(x / 120) - 40 * math.sin(x / 47)) for x in range(0, 1601, 20)] + [(1600, 900)]
    dl.polygon(pts, fill=hx('8FB3E3'))
    pts = [(0, 900)] + [(x, 830 + 30 * math.sin(x / 90 + 1)) for x in range(0, 1601, 20)] + [(1600, 900)]
    dl.polygon(pts, fill=hx('6F93D2'))
    dl.ellipse((1380, -220, 1900, 300), fill=hx('C9DBF2'))
    dl.ellipse((-260, -260, 220, 220), fill=hx('C9DBF2'))
    lay = lay.filter(ImageFilter.GaussianBlur(2))
    im = Image.alpha_composite(im, lay)
    im.convert('RGB').save(os.path.join(OUT, 'blanco.png'))
    # 5 · parénquima rosado (páginas 37-43)
    im = Image.new('RGBA', (Wd, Ht), hx('E9B4B9'))
    lay = Image.new('RGBA', (Wd, Ht), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    for gy in range(-1, 13):
        for gx in range(-1, 22):
            cx = gx * 80 + (gy % 2) * 40; cy = gy * 75
            dl.ellipse((cx - 34, cy - 32, cx + 34, cy + 32), fill=hx('FBE7EA'), outline=hx('B5656E'), width=3)
    dl.line([(0, 600), (500, 520), (900, 560), (1600, 420)], fill=hx('C0392B'), width=26)
    dl.line([(0, 250), (600, 330), (1100, 260), (1600, 300)], fill=hx('2F6DB5'), width=22)
    lay = lay.filter(ImageFilter.GaussianBlur(9))
    im = Image.alpha_composite(im, lay)
    im = Image.alpha_composite(im, Image.new('RGBA', (Wd, Ht), (255, 255, 255, 70)))
    im.convert('RGB').save(os.path.join(OUT, 'rosa.png'))
    # 6 · portada: blanco con pulmón azul de borde orgánico (página 1)
    im = Image.new('RGBA', (Wd, Ht), hx('FFFFFF'))
    lay = Image.new('RGBA', (Wd, Ht), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    dl.polygon(blob_pts(560, 450, 430, 90, 0.03, 2, 0.035), fill=hx('8FB3E3'), outline=hx('2F5597'))
    dl.polygon(blob_pts(560, 450, 330, 60, 0.02, 3), fill=hx('6F93D2'))
    for i in range(26):
        a = 2 * math.pi * i / 26
        x = 560 + 400 * math.cos(a); y = 450 + 400 * math.sin(a)
        dl.ellipse((x - 18, y - 18, x + 18, y + 18), fill=hx('C9DBF2'), outline=hx('2F5597'), width=3)
    lay = lay.filter(ImageFilter.GaussianBlur(1.2))
    im = Image.alpha_composite(im, lay)
    im.convert('RGB').save(os.path.join(OUT, 'portada.png'))


BG = {k: os.path.join(OUT, k + '.png') for k in ('azul', 'torax', 'mesotelio', 'blanco', 'rosa', 'portada')}

if __name__ == '__main__':
    make()
