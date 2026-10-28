# -*- coding: utf-8 -*-
"""UNIDAD V (parte 2): amilasa, lipasa, zimógenos, pancreatitis aguda (Morph), etiología, clínica, laboratorio,
casos 3 y 4, diagnóstico diferencial, anatomía de la obstrucción e integración."""
from plantillas import *
from u1 import persona_ico


def amilasa(D):
    s = nueva(D, 5, 'Amilasa sérica', src=['PA 3.1 Amilasa sérica'], tipo='der', c1=NARANJA, c2=BLANCO)
    rx = s.group_start('Reacción amilasa')
    for k in range(7):
        s.shape(0.5 + k * 0.42, 1.5 + (k % 2) * 0.2, 0.42, 0.42, 'hexagon', shade('F4D03F', 0.35, 0.2), ('9A7D0A', 1.0), False, adj={'adj': 28000, 'vf': 115470})
    texto(s, 0.4, 2.15, 3.2, 0.35, 'almidón', 13, '7D6608', True, 'c')
    enzima_globular(s, 3.6, 1.3, 1.5, 1.1, 'F5B041', 'Amilasa', 'Amilasa forma', size=14, seed=6)
    s.arrow([(5.2, 1.85), (5.8, 1.85)], INK, 3)
    for k in range(3):
        s.shape(5.95 + k * 0.95, 1.6, 0.42, 0.42, 'hexagon', shade('F4D03F', 0.35, 0.2), ('9A7D0A', 1.0), False, adj={'adj': 28000, 'vf': 115470})
        s.shape(6.33 + k * 0.95, 1.6, 0.42, 0.42, 'hexagon', shade('F4D03F', 0.35, 0.2), ('9A7D0A', 1.0), False, adj={'adj': 28000, 'vf': 115470})
    texto(s, 5.8, 2.15, 3.0, 0.35, 'disacáridos / maltosa', 13, '7D6608', True, 'c')
    s.group_end()
    rows = [['Propiedad', 'Descripción'], ['Origen', 'Páncreas exocrino + **glándulas salivales**'], ['Especificidad pancreática', '**Moderada**: también la produce la parótida'],
            ['Elevación no pancreática', 'Parotitis (paperas): amilasa salival ↑ sin problema pancreático'], ['Cinética', 'Inicio 6–12 h · pico 24 h · normalización 48–72 h'],
            ['Diagnóstico', 'Elevación > 3 veces el VN → altamente sugestiva de pancreatitis'], ['Amilasuria', 'Se eleva después que la sérica y dura más: útil si el paciente llega tarde']]
    ids, H = tabla_filas(s, 0.4, 2.75, [2.8, 5.6], rows, rowh=0.55, size=13.5, name='Tabla amilasa')
    par = s.group_start('Parótida')
    s.free(9.9, 1.3, 1.6, 1.6, smooth([(500, 0), (900, 200), (1000, 600), (700, 1000), (300, 900), (100, 500)]), shade('F5CBA7', 0.4, 0.25), ('A0522D', 1.5))
    texto(s, 9.6, 2.95, 2.2, 0.35, 'glándula parótida', 12.5, 'A0522D', True, 'c')
    s.group_end()
    pa = pancreas(s, 9.6, 3.6, 3.2, name='Páncreas amilasa')
    c = caja(s, 9.35, 5.0, 3.7, 2.05, 'Hidroliza el **almidón** (polisacáridos) a disacáridos y maltosa.', AMA, 15, name='Función amilasa')
    s.step(fade(rx), fade(c, after=True))
    s.step(fade(ids[0]), fade(ids[1], after=True), fade(par, after=True), fade(pa, after=True))
    for r in ids[2:]:
        s.step(fade(r))


def lipasa(D):
    s = nueva(D, 5, 'Lipasa sérica: más específica y más duradera', src=['PA 3.2 Lipasa sérica', 'REV PA 3.2'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    rx = s.group_start('Reacción lipasa')
    s.shape(0.6, 1.4, 0.35, 1.5, 'rect', shade('F2B90F', 0.3, 0.2), (INK, 1.0), False)
    for k in range(3):
        ag_chain(s, 0.95, 1.5 + k * 0.5, 1.8, 0.25, name='AG %d' % k)
    enzima_globular(s, 1.0, 3.1, 1.6, 1.1, 'F39C12', 'Lipasa', 'Lipasa forma', size=14, seed=9)
    texto(s, 0.4, 4.3, 4.0, 0.7, 'triglicéridos → ácidos grasos + glicerol', 14, INK, True, 'c')
    s.group_end()
    rows = [['Propiedad', 'Descripción'], ['Origen', '**Páncreas exocrino**'], ['Especificidad', '**Muy alta** para páncreas'], ['Inicio', 'Similar o levemente posterior a la amilasa'],
            ['Pico', '24 h'], ['Normalización', '**3–5 días** (dura más que la amilasa)'], ['Ventajas', 'Más específica; útil si el paciente llega tarde (> 48 h)']]
    ids, H = tabla_filas(s, 5.0, 1.2, [2.3, 5.75], rows, rowh=0.55, size=14, name='Tabla lipasa')
    reg = caja(s, 0.4, 5.2, 4.3, 1.85, '**Amilasa + lipasa siempre juntas**: la amilasa aparece antes; la lipasa es más específica y dura más.', AMA, 15, name='Siempre juntas')
    r_ = rigor(s, 5.0, 1.4 + H, 8.05, 6.95 - (1.4 + H), 'La lipasa no es **absolutamente** exclusiva: puede elevarse, en menor grado, en insuficiencia renal, perforación o isquemia intestinal y otras '
               'situaciones abdominales. Por eso se interpreta con el umbral (> 3 × VN) y la clínica.', 13.5, name='Rigor lipasa')
    s.step(fade(rx))
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r)) if r in (ids[1], ids[3], ids[6]) else s.anim[-1].append(fade(r, after=True))
    s.step(fade(reg))
    s.step(fade(r_))


def curvas_pancreas(D):
    s = nueva(D, 5, 'Amilasa y lipasa en el tiempo', src=['PA 3.1 Amilasa sérica', 'PA 3.2 Lipasa sérica'], tipo='der', c1=NARANJA, c2=BLANCO)
    X, Y, W, H = 0.8, 1.5, 7.9, 4.2
    def tx_(t):
        return t / 132.0
    ej = s.group_start('!!Ejes páncreas')
    s.arrow([(X, Y + H), (X, Y - 0.05)], INK, 2.25)
    s.arrow([(X, Y + H), (X + W + 0.1, Y + H)], INK, 2.25)
    for t, lab in ((0, '0'), (12, '12 h'), (24, '24 h'), (48, '48 h'), (72, '72 h'), (96, '4 d'), (120, '5 d')):
        xx = X + W * tx_(t)
        s.arrow([(xx, Y + H), (xx, Y + H + 0.1)], INK, 1.25, tail=None)
        texto(s, xx - 0.4, Y + H + 0.12, 0.8, 0.3, lab, 12, INK, True, 'c')
    texto(s, X + 0.1, Y - 0.45, 5.0, 0.35, 'actividad sérica (múltiplos del VN, esquema)', 12.5, INK, True)
    s.group_end()
    umbral = s.arrow([(X, Y + H * 0.55), (X + W, Y + H * 0.55)], ROJO, 2, tail=None, dash='dash', name='Umbral 3 VN')
    ul = rotulo(s, X + W - 1.6, Y + H * 0.55 - 0.45, '3 × VN', ROJO, 13, w=1.2, name='Rótulo 3VN')
    def cur(st_, pk, en, h):
        xs = [0, st_, (st_ + pk) / 2, pk, (pk + en) / 2, en, 132]
        ys = [0.05, 0.05, h * 0.6, h, h * 0.45, 0.07, 0.05]
        return [(int(tx_(t) * 1000), int(1000 - 40 - y * 900)) for t, y in zip(xs, ys)]
    am = curva(s, X, Y, W, H, cur(8, 24, 60, 0.85), 'F5B041', 4.5, name='Curva amilasa')
    li = curva(s, X, Y, W, H, cur(10, 24, 108, 0.95), 'C0560E', 4.5, name='Curva lipasa')
    l1 = rotulo(s, X + W * 0.13, Y + 0.05, 'amilasa: 6–12 h · 24 h · 48–72 h', 'F5B041', 12, name='Rótulo amilasa')
    l2 = rotulo(s, X + W * 0.42, Y + H * 0.25, 'lipasa: pico 24 h · normaliza 3–5 d', NARANJA_OSC, 12, name='Rótulo lipasa')
    c1 = caja(s, 9.35, 1.2, 3.7, 2.8, 'Si el paciente llega **después de 48 h**, la amilasa puede haberse normalizado: la **lipasa** (y la **amilasuria**) siguen siendo útiles.', AMA, 14.5,
              head='Consulta tardía', name='Consulta tardía')
    c2 = caja(s, 9.35, 4.25, 3.7, 2.8, 'Esquema cualitativo con los tiempos del material; alturas ilustrativas.', CREMA, 14, name='Aclaración páncreas')
    s.step(fade(ej), fade(umbral, after=True), fade(ul, after=True))
    s.step(wipe(am, 'l', dur=1000), fade(l1, after=True))
    s.step(wipe(li, 'l', dur=1200), fade(l2, after=True))
    s.step(fade(c1))
    s.step(fade(c2))


def zimogenos(D):
    s = nueva(D, 5, 'Zimógenos: enzimas fabricadas inactivas', src=['PA 4 Zimógenos', 'REV PA 4'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    rows = [['Zimógeno (inactivo)', 'Enzima activa'], ['Tripsinógeno', 'Tripsina (digiere proteínas)'], ['Quimotripsinógeno', 'Quimotripsina'], ['Proelastasa', 'Elastasa'],
            ['Profosfolipasa A_{2}', 'Fosfolipasa A_{2} (digiere membranas)'], ['Prolipasa + colipasa', 'Lipasa (digiere triglicéridos)'], ['Proamilasa', 'Amilasa']]
    ids, H = tabla_filas(s, 5.0, 1.2, [3.2, 4.85], rows, rowh=0.6, size=15, name='Tabla zimógenos')
    cel = celula_acinar(s, 0.8, 1.3, 3.1, 4.1, name='Célula acinar zimógenos', granulos=8)
    d = caja(s, 0.4, 5.6, 4.3, 1.45, 'Forma **inactiva** de una enzima: el páncreas la produce así para **no autodigerirse** antes de llegar al duodeno.', AMA, 14, name='Def zimógeno')
    r_ = rigor(s, 5.0, 1.4 + H, 8.05, 6.95 - (1.4 + H), 'Precisión: la **lipasa** y la **amilasa** pancreáticas se secretan en forma **activa**; el precursor que activa la tripsina es la **procolipasa** (cofactor de la lipasa). '
               'Los zimógenos verdaderos son tripsinógeno, quimotripsinógeno, proelastasa, procarboxipeptidasas y profosfolipasa A_{2}.', 12.5, name='Rigor zimógenos')
    s.step(fade(cel['g']), *[fade(gg, after=True) for gg in cel['gr']], fade(d, after=True))
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(r_))


def activacion_normal(D):
    s = nueva(D, 5, 'Activación fisiológica: los zimógenos se activan en el duodeno', src=['PA 4.1 Activación normal'], tipo='der', c1=NARANJA, c2=BLANCO)
    duo = s.shape(0.4, 4.4, 8.4, 1.5, 'roundRect', vshade('F1948A', 0.3, 0.3), ('922B21', 2.0), False, name='!!Duodeno luz', adj={'adj': 40000})
    dl = texto(s, 0.6, 5.95, 2.5, 0.35, 'luz duodenal', 13, '922B21', True, name='Rótulo duodeno')
    cel = celula_acinar(s, 0.6, 1.2, 1.8, 2.4, name='Célula acinar activación', granulos=5)
    con = s.shape(2.4, 2.9, 2.2, 0.38, 'rect', ('lin', [(0, 'FCF3CF'), (100, 'F9E79F')], 90), ('B7950B', 1.25), False, name='Conducto pancreático')
    hor = s.group_start('Hormonas')
    ficha(s, 5.1, 1.3, 'CCK', '8E44AD', w=1.0, h=0.42, size=13)
    ficha(s, 6.2, 1.3, 'Secretina', '2E86C1', w=1.4, h=0.42, size=13)
    s.group_end()
    bolo = ficha(s, 7.2, 4.85, 'bolo', 'D7BDE2', w=1.0, h=0.5, size=13, name='Bolo alimenticio')
    tg = ficha(s, 2.9, 2.85, 'Tripsinógeno', 'F4D03F', w=1.7, h=0.45, size=12, name='Tripsinógeno')
    ek = enzima_globular(s, 4.6, 3.9, 1.3, 0.9, '58D68D', 'Entero-\nquinasa', 'Enteroquinasa', size=11, seed=2)
    tr = ficha(s, 5.0, 4.95, 'Tripsina', 'E74C3C', w=1.4, h=0.45, size=13, name='Tripsina')
    cas = s.group_start('Cascada')
    for k, (t) in enumerate(('quimotripsina', 'elastasa', 'fosfolipasa A_{2}')):
        ficha(s, 2.6 + k * 1.6, 5.35, t, 'F1948A', w=1.5, h=0.4, size=11)
    s.arrow([(5.0, 5.2), (4.1, 5.45)], INK, 2)
    s.group_end()
    c1 = caja(s, 9.35, 1.2, 3.7, 2.4, 'Los zimógenos se almacenan en **gránulos** de las células acinares.', BLANCO, 15, name='Gránulos')
    c2 = caja(s, 9.35, 3.8, 3.7, 1.55, 'El bolo en el duodeno libera **CCK y secretina** → los zimógenos salen por el conducto.', CREMA, 13.5, name='Estímulo')
    c3 = caja(s, 9.35, 5.55, 3.7, 1.5, 'La **enteroquinasa** activa el tripsinógeno → **tripsina**, que activa **en cascada** a los demás.', AMA, 13.5, name='Cascada texto')
    s.step(fade(duo), fade(dl, after=True), fade(cel['g'], after=True), *[fade(g, after=True) for g in cel['gr']], fade(con, after=True), fade(c1, after=True))
    s.step(fade(bolo), fade(hor, after=True), fade(c2, after=True))
    s.step(fade(tg), path(tg, 2.2, 1.65, after=True, dur=1100), fade(ek, after=True))
    s.step(zoom(tr), out(tg, after=True), fade(c3, after=True))
    s.step(fade(cas))


# ---------------------------------------------------------------- pancreatitis (Morph)
PC_TXT = {1: 'Páncreas: órgano exocrino y endocrino', 2: 'Acercamiento al tejido pancreático', 3: 'Células acinares', 4: 'Zimógenos en los gránulos',
          5: 'Alteración de la activación: tripsina dentro de la célula', 6: 'Autodigestión y daño celular', 7: 'Respuesta local: inflamación',
          8: 'Liberación de amilasa y lipasa a la sangre', 9: 'Cambios séricos', 10: 'Interpretación clínica'}


def escena_pc(D, st):
    s = nueva(D, 5, PC_TXT[st], tipo='der', c1=NARANJA, c2=BLANCO, morph=st > 1, src=['PA 4.2 Pancreatitis: activación prematura', 'PA 1.1 Autodigestión'], tw=8.7)
    ids = {}
    pan = {1: (0.4, 2.3, 8.3), 2: (-6.0, -2.0, 22.0), 3: (-6.0, -2.0, 22.0), 4: (6.3, 5.7, 2.4), 5: (6.3, 5.7, 2.4), 6: (6.3, 5.7, 2.4), 7: (6.3, 5.7, 2.4), 8: (6.3, 5.7, 2.4),
           9: (6.6, 1.25, 2.2), 10: (6.6, 1.25, 2.2)}[st]
    ids['pan'] = pancreas(s, pan[0], pan[1], pan[2], name='!!Pancreas')
    if st == 1:
        ids['duo'] = s.free(0.0, 2.0, 1.6, 4.0, [('M 900 0 C 300 200 200 800 900 1000', False, True)], None, ('922B21', 26), name='!!Duodeno')
    if 2 <= st <= 3:
        d = {2: (3.0, 2.2, 2.0), 3: (1.0, 1.25, 5.1)}[st]
        ids['acino'] = acino(s, d[0], d[1], d[2], name='!!Acino')
    if 4 <= st <= 8:
        dark = st >= 6
        cx, cy, cw, ch = (1.2, 1.2, 4.2, 5.0)
        ids['cel'] = celula_acinar(s, cx, cy, cw, ch, name='!!CelulaAcinar', granulos=0)['g']
        if dark:
            ids['dano'] = s.free(cx, cy, cw, ch, 'M 60 1000 L 940 1000 C 900 700 780 200 640 40 L 360 40 C 220 200 100 700 60 1000 Z', ('a', '4A235A', 50), ('1B0E24', 2.0, 'dash'),
                                 name='!!Daño celular')
        gpos = [(0.4, 0.15), (0.52, 0.22), (0.45, 0.32), (0.58, 0.36), (0.38, 0.45), (0.52, 0.5), (0.62, 0.27)]
        gr = []
        for k, (fx, fy) in enumerate(gpos):
            act = st >= 5 and k % 2 == 0
            col = ('rad', [(0, 'FADBD8'), (60, 'E74C3C'), (100, '922B21')], (35, 30)) if act else ('rad', [(0, 'FFF9C4'), (60, 'FBC02D'), (100, 'C49000')], (35, 30))
            gr.append(s.shape(cx + cw * fx, cy + ch * fy, cw * 0.13, cw * 0.13, 'ellipse', col, ('7F6000' if not act else '641E16', 1.0), False, name='!!Zimogeno %d' % (k + 1)))
        ids['gr'] = gr
    if st >= 7 and st <= 8:
        ids['inf'] = [leucocito(s, 5.6 + (k % 2) * 1.0, 1.4 + k * 0.85, 0.8, 'neutrofilo', name='!!Leucocito %d' % (k + 1)) for k in range(3)]
        ids['edema'] = s.shape(0.9, 0.95, 4.9, 5.55, 'ellipse', None, ('5DADE2', 3.0, 'dash'), False, name='!!Edema')
    if st >= 8:
        ids['cap'] = vessel(s, 0.3 if st >= 9 else 5.6, 6.35 if st < 9 else 6.25, 3.2 if st < 9 else 8.5, 0.7, name='!!Capilar', rbcs=0)
    if st == 8:
        ids['enz'] = [ficha(s, 5.8 + (k % 2) * 1.1, 4.5 + (k // 2) * 0.55, t, c, w=1.0, h=0.4, size=11, name='!!%s %d' % (t, k)) for k, (t, c) in
                      enumerate((('Amilasa', 'F5B041'), ('Lipasa', 'C0560E'), ('Amilasa', 'F5B041'), ('Lipasa', 'C0560E')))]
    if st >= 9:
        base = 5.5
        ids['ejeb'] = s.arrow([(0.6, base), (8.6, base)], INK, 2.25, tail=None, name='!!Base barras')
        ids['vn'] = s.arrow([(0.6, base - 0.6), (8.6, base - 0.6)], VERDE_OSC, 2, tail=None, dash='dash', name='!!Línea VN')
        ids['vn3'] = s.arrow([(0.6, base - 1.8), (8.6, base - 1.8)], ROJO, 2, tail=None, dash='dash', name='!!Línea 3VN')
        ids['l3'] = texto(s, 6.6, base - 2.2, 2.0, 0.35, '3 × VN', 13, ROJO, True, 'r', name='!!Rótulo 3VN')
        for k, (t, c, hh) in enumerate((('Amilasa', 'F5B041', 3.4), ('Lipasa', 'C0560E', 3.9))):
            ids['b%d' % k] = s.shape(1.6 + k * 2.6, base - hh, 1.5, hh, 'rect', ('lin', [(0, lighten(c, 0.35)), (100, c)], 90), (INK, 1.25), False, name='!!Barra ' + t)
            ids['bl%d' % k] = texto(s, 1.35 + k * 2.6, base + 0.08, 2.0, 0.4, t, 15, INK, True, 'c', name='!!Nombre ' + t)
    return s, ids


def pancreatitis_seq(D):
    ini = len(D.slides) + 1
    s, i = escena_pc(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'El páncreas produce las enzimas digestivas del **jugo pancreático** (porción exocrina) y vierte su secreción al **duodeno**.', BLANCO, 15, head='Páncreas',
             name='Caja PC1')
    s.step(fade(i['pan']), fade(i['duo'], after=True))
    s.step(fade(c))
    s, i = escena_pc(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 2.6, 'Acercamos el tejido: aparecen los **ácinos**, unidades secretoras del páncreas exocrino.', BLANCO, 15, head='Tejido', name='Caja PC2')
    s.step(zoom(i['acino']))
    s.step(fade(c))
    s, i = escena_pc(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Cada ácino está formado por **células acinares** dispuestas alrededor de una luz que drena al sistema de conductos.', BLANCO, 15, head='Células acinares',
             name='Caja PC3')
    s.step(fade(c))
    s, i = escena_pc(D, 4)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'En el polo apical, los **gránulos de zimógeno** guardan las enzimas **inactivas** (tripsinógeno y demás precursores).', AMA, 15, head='Zimógenos',
             name='Caja PC4')
    s.step(fade(i['cel']), *[zoom(g, after=True) for g in i['gr']])
    s.step(fade(c))
    s, i = escena_pc(D, 5)
    tl = rotulo(s, 5.7, 1.9, 'tripsina activa', ROJO, 14, name='Rótulo tripsina activa')
    c = caja(s, 9.35, 1.2, 3.7, 3.6, 'En la pancreatitis los zimógenos se activan **dentro del propio páncreas**, antes de llegar al duodeno. Causa descripta: **obstrucción** del conducto (litiasis, alcohol, tumor).',
             ROSA, 14.5, head='Activación prematura', headfill=ROJO, name='Caja PC5')
    s.step(*[pulse(g, after=(k > 0)) for k, g in enumerate(i['gr'][::2])], fade(tl, after=True))
    s.step(fade(c))
    s, i = escena_pc(D, 6)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Las enzimas activas digieren el propio tejido: **autodigestión → necrosis pancreática**.', ROSA, 16, head='Daño celular', headfill=ROJO, name='Caja PC6')
    s.step(fade(c))
    s, i = escena_pc(D, 7)
    c = caja(s, 9.35, 1.2, 3.7, 3.6, '**Inflamación** local: fiebre (no necesariamente infección), **edema** y paso de líquido al **tercer espacio** (taquicardia, hipotensión).', 'EAF2F8', 14.5,
             head='Respuesta local', headfill=AZUL, name='Caja PC7')
    s.step(*[fade(l, after=(k > 0)) for k, l in enumerate(i['inf'])], fade(i['edema'], after=True))
    s.step(fade(c))
    s, i = escena_pc(D, 8)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Con la necrosis, **amilasa y lipasa** pasan a la **sangre**.', AMA, 16, head='Biomarcadores', name='Caja PC8')
    s.step(fade(i['cap']), *[fade(e, after=True) for e in i['enz']])
    s.step(fade(c))
    s, i = escena_pc(D, 9)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, '**Amilasa > 3 × VN** (6–12 h; normaliza en 48–72 h) y **lipasa > 3 × VN** (se mantiene 3–5 días). Esquema de alturas ilustrativo.', AMA, 14.5,
             head='Suero', name='Caja PC9')
    s.step(fade(i['ejeb']), fade(i['vn'], after=True), fade(i['vn3'], after=True), fade(i['l3'], after=True), wipe(i['b0'], 'b', after=True), fade(i['bl0']), wipe(i['b1'], 'b', after=True),
           fade(i['bl1']))
    s.step(fade(c))
    s, i = escena_pc(D, 10)
    c = caja(s, 9.35, 1.2, 3.7, 2.9, 'Dolor epigástrico «en cinturón» + **amilasa y lipasa > 3 × VN** → pancreatitis aguda. La **lipasa** es la más específica y la más duradera.', 'EAF5EA', 14.5,
             head='Interpretación', headfill=VERDE_OSC, name='Caja PC10')
    r_ = rigor(s, 9.35, 4.35, 3.7, 2.7, 'Criterios de Atlanta revisados: **2 de 3** — dolor típico, lipasa o amilasa ≥ 3 × LSN, imagen compatible.', 13, name='Rigor Atlanta')
    s.step(fade(c))
    s.step(fade(r_))
    registrar_morph(D, ini, len(D.slides), 'Pancreatitis aguda: páncreas → tejido → ácino → célula acinar → zimógenos → activación prematura → autodigestión → inflamación → liberación de enzimas → cambios séricos → interpretación',
                    ['!!Pancreas', '!!Duodeno', '!!Acino', '!!CelulaAcinar', '!!Zimogeno 1–7', '!!Daño celular', '!!Leucocito 1–3', '!!Edema', '!!Capilar', '!!Amilasa/Lipasa', '!!Barra Amilasa',
                     '!!Barra Lipasa'],
                    'El páncreas se agranda hasta salir del cuadro (efecto de acercamiento) y luego se reduce a un ícono; el ácino crece y da paso a la célula acinar; los gránulos cambian de amarillo a rojo '
                    '(activación); la célula se oscurece; llegan leucocitos; las enzimas pasan al capilar y se convierten en barras de laboratorio.')


def etiologia(D):
    s = nueva(D, 5, 'Etiología de la pancreatitis aguda', src=['PA 5.3 Etiología'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    rows = [['Causa', 'Mecanismo / observaciones'], ['Litiasis biliar', '**Causa más frecuente**: el cálculo obstruye el conducto biliopancreático → reflujo → activación de zimógenos. Más en **mujeres**.'],
            ['Alcoholismo', 'Toxicidad directa + espasmo del **esfínter de Oddi** → obstrucción funcional. Más en **varones**.'],
            ['Hipertrigliceridemia severa (> 1000 mg/dL)', 'Los ácidos grasos libres dañan el endotelio pancreático.'], ['Traumatismo abdominal', 'Causa más frecuente en **niños**.'],
            ['Fármacos', 'Estrógenos, furosemida, sulfamidas, tetraciclinas, corticoides, algunos antibióticos.'], ['Tumores', 'Obstrucción mecánica del conducto.'],
            ['Infecciones', 'Hepatitis viral, parotitis, rubéola, CMV, Candida, Ascaris (asciende por la vía biliopancreática).'], ['Idiopática', '~20–30 % sin causa identificable.']]
    ids, H = tabla_filas(s, 0.4, 1.2, [3.4, 9.25], rows, rowh=0.62, size=13.5, name='Tabla etiología')
    s.step(fade(ids[0]))
    for k in range(1, len(ids), 2):
        s.step(fade(ids[k]), *([fade(ids[k + 1], after=True)] if k + 1 < len(ids) else []))


def clinica_pa(D):
    s = nueva(D, 5, 'Clínica de la pancreatitis aguda', src=['PA 5.4 Clínica'], tipo='bandas', c1=DURAZNO_CL, c2=NARANJA)
    hu = human(s, 4.9, 1.1, 5.9, name='!!Paciente')
    cin = s.shape(5.5, 3.0, 1.8, 0.55, 'ellipse', ('a', ROJO, 45), (ROJO, 2.5, 'dash'), False, name='Dolor en cinturón')
    gt = s.shape(6.65, 3.55, 0.45, 0.6, 'ellipse', ('a', '6C3483', 55), None, False, name='Signo Grey-Turner')
    cu = s.shape(6.25, 3.75, 0.3, 0.3, 'ellipse', ('a', '6C3483', 65), None, False, name='Signo de Cullen')
    izq = [('Dolor abdominal', 'Epigástrico, intenso, brusco; irradiación **en cinturón** hacia la espalda; empeora con alimentos o alcohol.'),
           ('Náuseas y vómitos', '~90 % de los casos; **no alivian** el dolor.'), ('Fiebre', 'Por inflamación, no necesariamente infección.')]
    der = [('Taquicardia + hipotensión', 'Dolor e **hipovolemia** (líquido al tercer espacio).'), ('Íleo paralítico', 'Catarsis ausente, ruidos hidroaéreos disminuidos.'),
           ('Grey-Turner / Cullen', 'Equimosis en flancos (pancreatitis hemorrágica grave) / periumbilical (hematoma retroperitoneal).'), ('Ictericia (variable)', 'Solo si se obstruye el colédoco.')]
    ids = []
    for k, (t, d) in enumerate(izq):
        ids.append(caja(s, 0.35, 1.2 + k * 1.95, 4.3, 1.8, '**%s**: %s' % (t, d), BLANCO, 14, name='Clínica izq %d' % k))
    for k, (t, d) in enumerate(der):
        ids.append(caja(s, 8.55, 1.2 + k * 1.47, 4.45, 1.35, '**%s**: %s' % (t, d), BLANCO, 13, name='Clínica der %d' % k))
    s.step(fade(hu), zoom(cin, after=True), fade(ids[0], after=True))
    s.step(fade(ids[1]), fade(ids[2], after=True))
    s.step(fade(ids[3]), fade(ids[4], after=True))
    s.step(fade(gt), fade(cu, after=True), fade(ids[5], after=True))
    s.step(fade(ids[6]))


def lab_pa(D):
    s = nueva(D, 5, 'Laboratorio en la pancreatitis aguda', src=['PA 5.5 Laboratorio en pancreatitis', 'REV PA 5.5'], tipo='der', c1=NARANJA, c2=BLANCO)
    rows = [['Parámetro', 'Hallazgo'], ['Amilasa', '↑↑↑ > 3 × VN (6–12 h; normaliza en 48–72 h)'], ['Lipasa', '↑↑↑ > 3 × VN, más específica y duradera (3–5 días)'],
            ['Leucocitos', '↑↑ muy elevados (inflamación severa)'], ['Hematocrito', '↑ inicial (hemoconcentración) → ↓ si hay hemorragia pancreática'],
            ['Glucemia', '↑ por daño del páncreas endocrino (menos insulina)'], ['Urea / BUN', '↑ por catabolismo aumentado y deshidratación'],
            ['PCR', '> 150 mg/L a las 48 h: pancreatitis **severa**'], ['GOT/GPT, FAL, GGT', 'Pueden elevarse si se compromete el colédoco']]
    ids, H = tabla_filas(s, 0.4, 1.2, [2.6, 5.8], rows, rowh=0.62, size=13.5, name='Tabla lab pancreatitis')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, '- La PCR > 150 mg/L a las 48 h es un **marcador de gravedad** ampliamente usado, pero la clasificación de Atlanta revisada (2012) define la gravedad por **falla orgánica** y complicaciones.\n'
               '- La hiperglucemia también responde a las **hormonas de estrés**.', 13, name='Rigor lab PA')
    s.step(fade(ids[0]))
    for k in range(1, len(ids), 2):
        s.step(fade(ids[k]), *([fade(ids[k + 1], after=True)] if k + 1 < len(ids) else []))
    s.step(fade(r_))


# ---------------------------------------------------------------- casos
def caso3(D):
    s = nueva(D, 5, 'Caso clínico 3: presentación', src=['PA 5.1 Caso 3'], tipo='der', c1=NARANJA, c2=BLANCO)
    p = caso_cabecera(s, 0.4, 1.2, 8.4, 'Mujer de 22 años', 'Dolor abdominal epigástrico 10/10 «en cinturón» (irradia a ambos costados), de aparición repentina hace 3 días.', color=NARANJA_OSC)
    sx = caja(s, 0.4, 2.95, 4.1, 1.6, 'Náuseas, vómitos y fiebre (**37,9 °C**).', BLANCO, 16, anchor='m', name='Síntomas C3')
    cat = caja(s, 4.7, 2.95, 4.1, 1.6, 'Catarsis ausente 48 h; **sin ictericia**.', BLANCO, 16, anchor='m', name='Catarsis C3')
    q = caja(s, 0.4, 4.8, 8.4, 2.25, '¿Hígado o páncreas? Antes de mirar el laboratorio, ¿qué perfil enzimático esperaríamos en cada caso?', AMA, 17, anchor='m', name='Pregunta C3')
    h = human(s, 10.1, 1.1, 5.9, name='Silueta C3', fill='FAD7A0')
    s.step(fade(p), fade(h, after=True))
    s.step(fade(sx))
    s.step(fade(cat))
    s.step(fade(q))
    s = nueva(D, 5, 'Caso clínico 3: signos vitales y antecedentes', src=['PA 5.1 Caso 3'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    sv = signos_vitales(s, 0.4, 1.3, [('TA', '90/50', True), ('FC', '120 lpm', True), ('FR', '26 rpm', True), ('SatO_{2}', '97 %', False), ('Temp.', '37,9 °C', True)],
                        w=2.35, h=1.1, gap=0.17)
    a1 = caja(s, 0.4, 2.75, 6.1, 1.6, '**Alcoholismo severo** con consumo aumentado en las **2 semanas previas**.', ROSA, 17, anchor='m', name='Alcohol C3')
    a2 = caja(s, 6.75, 2.75, 6.3, 1.6, 'Pareja **hospitalizada por hepatitis** → diagnóstico presuntivo inicial: **hepatitis infecciosa**.', CREMA, 16, anchor='m', name='Pareja C3')
    c = caja(s, 0.4, 4.6, 12.65, 2.45, 'Hipotensión y taquicardia: dolor e **hipovolemia**. El antecedente de la pareja **sesga** hacia hepatitis: el laboratorio debe decidir.', AMA, 17, anchor='m',
             name='Síntesis C3')
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(sv)])
    s.step(fade(a1))
    s.step(fade(a2))
    s.step(fade(c))
    s = nueva(D, 5, 'Caso clínico 3: laboratorio de ingreso', src=['PA 5.2 Laboratorio de ingreso'], tipo='der', c1=NARANJA, c2=BLANCO)
    rows = [['Biomarcador', 'Paciente', 'Referencia', 'Lectura'], ['Bilirrubina total', '0,8 mg/dL', '0,2–1,2 mg/dL', 'Normal'], ['Bilirrubina directa', '0,1 mg/dL', '< 0,3 mg/dL', 'Normal (BI = 0,7)'],
            ['GOT / AST', '~40 UI/L', '< 37–40 UI/L', 'Límite: sin daño activo'], ['GPT / ALT', '~35 UI/L', '< 31–40 UI/L', 'Normal: no apoya hepatitis'],
            ['LDH', 'Dentro del VN', '< 240 UI/L', 'Normal'], ['Amilasa', 'MUY ELEVADA (> 3 × VN)', '20–110 UI/L', '**Diagnóstica**'], ['Lipasa', 'MUY ELEVADA (> 3 × VN)', '< 60 UI/L', '**Diagnóstica y más específica**']]
    ids, H = tabla_filas(s, 0.4, 1.2, [2.1, 2.35, 1.75, 2.25], rows, rowh=0.62, size=13.5, name='Lab C3')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Perfil hepático **prácticamente normal**; lo elevado es **amilasa y lipasa**.', AMA, 16, name='Lectura C3')
    pa = pancreas(s, 9.5, 4.6, 3.4, name='Páncreas C3')
    s.step(fade(ids[0]))
    s.step(fade(ids[1]), fade(ids[2], after=True))
    s.step(fade(ids[3]), fade(ids[4], after=True), fade(ids[5], after=True))
    s.step(fade(ids[6]))
    s.step(fade(ids[7]))
    s.step(fade(c), fade(pa, after=True))
    s = nueva(D, 5, 'Caso clínico 3: ¿por qué no es una hepatitis?', src=['PA 5.2 Por qué no es hepatitis'], tipo='bandas', c1=DURAZNO_CL, c2=CREMA)
    rows = [['En una hepatitis viral aguda esperaríamos', 'En la paciente'], ['GPT/ALT > 400–500 UI/L (≥ 10 × VN)', '**Ausente** (~35 UI/L)'], ['GOT/AST elevada (menos que GPT)', '**Ausente** (~40 UI/L)'],
            ['Bilirrubina total aumentada (≈ 70 % de las hepatitis A)', '**Normal** (0,8 mg/dL)'], ['Ictericia', '**Ausente**']]
    ids, H = tabla_filas(s, 3.55, 1.2, [3.6, 2.9], rows, rowh=0.85, size=15, name='Comparación C3')
    hep = liver(s, 0.4, 1.6, 2.8, name='Hígado C3')
    pa = pancreas(s, 10.4, 1.9, 2.7, name='Páncreas C3b')
    c = caja(s, 3.55, 1.45 + H, 6.5, 6.95 - (1.45 + H), 'El problema es **pancreático**, no hepático: el perfil enzimático **contradice** el diagnóstico presuntivo.', AMA, 16, anchor='m', name='Conclusión parcial C3')
    s.step(fade(hep), fade(ids[0], after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(pa), fade(c, after=True))
    s = nueva(D, 5, 'Caso clínico 3: conclusión', src=['PA 5.2 Conclusión', 'PA 9 Pregunta fisiopatología alcohólica', 'REV PA 5.5'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    fl = flow(s, ['Alcohol: toxicidad + espasmo del esfínter de Oddi', 'Obstrucción funcional', 'Activación prematura de zimógenos', 'Autodigestión → necrosis', 'Amilasa y lipasa en sangre'],
              0.4, 1.3, 8.4, 5.7, fills=[ROSA, CREMA, AMA, ROSA, 'EAF5EA'], size=16, gap=0.3, dir='v')
    con = conclusion(s, 9.35, 1.2, 3.7, 3.2, '**PANCREATITIS AGUDA de origen alcohólico**: amilasa y lipasa > 3 × VN con perfil hepático normal.', title='Diagnóstico', size=15)
    r_ = rigor(s, 9.35, 4.65, 3.7, 2.4, 'Con dolor típico y lipasa > 3 × VN ya se cumplen **2 de 3** criterios de Atlanta; la imagen se reserva para dudas o complicaciones.', 12.5,
               name='Rigor C3')
    flow_anim(s, fl)
    s.step(fade(con))
    s.step(fade(r_))


def caso4(D):
    s = nueva(D, 5, 'Caso clínico 4: presentación', src=['PA 6.1 Caso 4'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    p = caso_cabecera(s, 0.4, 1.2, 8.4, 'Hombre de 31 años', 'Dolor abdominal agudo inmovilizante, vómitos y diarrea con heces claras.', color=NARANJA_OSC)
    s1 = caja(s, 0.4, 2.95, 2.7, 1.9, '**Acolia**: heces claras', CREMA, 16, anchor='m', align='c', name='Acolia C4')
    s2 = caja(s, 3.25, 2.95, 2.7, 1.9, '**Ictericia**: mucosas amarillas', AMA, 16, anchor='m', align='c', name='Ictericia C4')
    s3 = caja(s, 6.1, 2.95, 2.7, 1.9, 'Abdomen prominente: **hepatomegalia** posible', ROSA, 15, anchor='m', align='c', name='Hepatomegalia C4')
    dx = caja(s, 0.4, 5.1, 8.4, 1.95, 'Diagnóstico presuntivo: **hepatitis aguda** (ictericia + acolia + dolor abdominal).', 'EAF5EA', 18, anchor='m', name='Presuntivo C4')
    hu = human(s, 9.6, 1.1, 5.9, name='Silueta C4', fill='F7DC6F')
    s.step(fade(p), fade(hu, after=True))
    s.step(fade(s1), fade(s2, after=True), fade(s3, after=True))
    s.step(fade(dx))
    s = nueva(D, 5, 'Caso clínico 4: laboratorio esperado en la hepatitis aguda', src=['PA 6.2 Laboratorio esperado'], tipo='der', c1=NARANJA, c2=BLANCO)
    rows = [['Biomarcador', '¿Qué esperamos?'], ['Leucocitos', '↑ (proceso inflamatorio)'], ['Bilirrubina total y DIRECTA', '↑↑ muy elevadas: el hígado conjuga pero no excreta → reflujo a la sangre'],
            ['GPT / ALT (la más importante)', '↑↑↑ > 400–500 UI/L (≥ 10 × VN); **predomina** sobre la GOT (GOT/GPT < 1)'], ['GOT / AST', '↑↑ muy elevada, pero menos que la GPT (en la viral)'],
            ['FAL', 'Levemente elevada o normal'], ['GGT', '↑↑ si hay componente alcohólico'], ['Amilasa y lipasa', '**Normales**']]
    ids, H = tabla_filas(s, 0.4, 1.2, [3.0, 5.4], rows, rowh=0.72, size=14.5, name='Lab esperado C4')
    hep = hepatocyte(s, 9.6, 1.3, 3.2, name='Hepatocito C4')
    c = caja(s, 9.35, 4.3, 3.7, 2.75, 'Es el **perfil esperado** (el material no aporta valores numéricos de este paciente): ALT dominante + bilirrubina directa alta.', AMA, 14, name='Nota esperado C4')
    s.step(fade(ids[0]), fade(hep, after=True))
    for k in range(1, len(ids), 2):
        s.step(fade(ids[k]), *([fade(ids[k + 1], after=True)] if k + 1 < len(ids) else []))
    s.step(fade(c))
    s = nueva(D, 5, 'Caso clínico 4: etiologías de la hepatitis', src=['PA 6.3 Etiologías de la hepatitis', 'PA 6.4 Hepatitis viral'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    rows = [['Etiología', 'Claves diagnósticas'], ['Viral (A, B, C, D, E)', 'Transaminasas ≈ 10 × VN; serología por tipo.'], ['Alcohólica', 'GOT/GPT > 2; GGT muy elevada; GOT rara vez > 300–400 UI/L.'],
            ['Medicamentosa / tóxica', 'Paracetamol en dosis altas, AINE, estatinas, isoniazida, amoxicilina-clavulánico, anticonvulsivantes.'],
            ['Autoinmune', 'ASMA, ANA, anti-LKM1; más frecuente en mujeres jóvenes.'], ['Idiopática', 'Sin causa identificable.']]
    ids, H = tabla_filas(s, 0.4, 1.2, [2.6, 4.2], rows, rowh=0.62, size=13, name='Etiologías hepatitis')
    rows2 = [['Virus', 'Transmisión', 'Cronicidad'], ['A', 'Fecal-oral', 'No (siempre aguda)'], ['B', 'Parenteral, sexual, vertical', '~5–10 % adultos'],
             ['C', 'Parenteral', '~75–85 %'], ['D', 'Coinfección con VHB', 'Sí'], ['E', 'Fecal-oral', 'No (salvo inmunodeprimidos)']]
    ids2, H2 = tabla_filas(s, 7.35, 1.2, [0.8, 2.9, 2.0], rows2, rowh=0.62, size=13, name='Tabla virus', head_fill=NARANJA_OSC)
    c = caja(s, 0.4, 1.45 + max(H, H2), 12.65, 6.95 - (1.45 + max(H, H2)), 'El laboratorio bioquímico **ubica** el daño en el hígado; la **serología** y la historia definen la etiología.', AMA, 15.5,
             anchor='m', name='Ubicación vs etiología')
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(ids2[0]), *[fade(r, after=True) for r in ids2[1:]])
    s.step(fade(c))


def diferencial(D):
    s = nueva(D, 5, 'Diagnóstico diferencial: la tabla maestra', src=['PA 7 Tabla maestra', 'REV PA 7'], tipo='der', c1=NARANJA, c2=BLANCO)
    heads = ['Biomarcador', 'Pancreatitis aguda', 'Hepatitis aguda', 'Colecistitis', 'ITU (ref.)']
    data = [['Leucocitos', '↑↑', '↑↑', '↑↑', '↑'], ['Bilirrubina total', 'Normal o ↑ (si obstr.)', '↑↑', '↑↑', 'Normal'], ['Bilirrubina directa', 'Normal o ↑', '↑↑', '↑↑', 'Normal'],
            ['GOT / AST', 'Normal o leve ↑', '↑↑↑', 'Normal o leve ↑', 'Normal'], ['GPT / ALT', 'Normal o leve ↑', '↑↑↑ (predomina)', 'Normal o leve ↑', 'Normal'],
            ['FAL', 'Normal o leve ↑', 'Normal o leve ↑', '↑↑ muy elevada', 'Normal'], ['GGT', '↑ si alcohólica', 'Normal o ↑', '↑↑ muy elevada', 'Normal'],
            ['Amilasa', '↑↑↑ > 3 × VN', 'Normal', 'Normal', 'Normal'], ['Lipasa', '↑↑↑ (específica)', 'Normal', 'Normal', 'Normal'], ['Glucemia', '↑', 'Normal', 'Normal', 'Normal']]
    colw = [1.75, 1.75, 1.65, 1.65, 1.35]
    fills = ['FDEBD0', 'FCE4EC', 'EAF5EA', CREMA, CELESTE]
    rh = 0.5
    cols = []
    x = 0.4
    for c in range(5):
        g = s.group_start('Columna dif %s' % heads[c])
        s.shape(x, 1.2, colw[c], 0.62, 'rect', NAVY, (INK, 1.25), False, heads[c], 12.5, F_HEAD, BLANCO, True, 'c', 'm', (0.04, 0, 0.04, 0))
        for r in range(len(data)):
            s.shape(x, 1.82 + r * rh, colw[c], rh, 'rect', fills[c], (INK, 1.0), False, data[r][c], 12, F_BODY, INK, c == 0, 'c' if c else 'l', 'm', (0.05, 0, 0.05, 0), minsize=10)
        cols.append(s.group_end())
        x += colw[c]
    r_ = rigor(s, 9.35, 1.2, 3.7, 3.4, 'En la **colecistitis** aguda la obstrucción suele estar en el **cístico**: bilirrubina, FAL y GGT a menudo son **normales o poco elevadas**; '
               'elevaciones marcadas sugieren compromiso del **colédoco** (coledocolitiasis).', 12.5, name='Rigor colecistitis')
    m = caja(s, 9.35, 4.85, 3.7, 2.2, '**GPT** alta → hepatitis · **amilasa + lipasa** altas → pancreatitis · **FAL + GGT** altas → colestasis/vesícula.', AMA, 13.5, name='Mensaje dif')
    s.step(fade(cols[0]))
    for g in cols[1:]:
        s.step(wipe(g, 'l'))
    s.step(fade(m))
    s.step(fade(r_))


def anatomia_obstruccion(D):
    s = nueva(D, 5, 'Localización de la obstrucción según el perfil enzimático', src=['PA 8 Anatomía de la obstrucción', 'REV PA 8'], tipo='der', c1=NARANJA, c2=BLANCO)
    ids = arbol_biliar(s, 0.3, 1.1, 8.6, 5.9)
    W, H = 8.6, 5.9
    def P(fx, fy):
        return (0.3 + W * fx, 1.1 + H * fy)
    sitios = [('1', 0.36, 0.52, 'Conducto **cístico**: FAL y GGT muy elevadas + bilirrubina elevada; GOT/GPT y amilasa normales al inicio → **colecistitis**.', 'EAF5EA'),
              ('2', 0.415, 0.44, 'Conducto **hepático común**: bilirrubina muy elevada + ictericia + coluria + acolia; FAL/GGT elevadas.', CREMA),
              ('3', 0.72, 0.67, 'Conducto **pancreático principal**: amilasa y lipasa muy elevadas; bilirrubina **normal** → **pancreatitis**.', 'FDEBD0'),
              ('4', 0.47, 0.8, '**Ampolla de Vater** / conducto común: elevación **simultánea** de amilasa/lipasa + bilirrubina + transaminasas moderadas → patrón **mixto**.', ROSA)]
    marks = []
    cards = []
    for k, (n, fx, fy, t, f) in enumerate(sitios):
        x, y = P(fx, fy)
        marks.append(num(s, x - 0.23, y - 0.23, n, d=0.46, fill=ROJO, name='Sitio %s' % n))
        cards.append(caja(s, 9.35, 1.2 + k * 1.47, 3.7, 1.35, t, f, 11.5, name='Perfil sitio %s' % n, minsize=10))
    s.step(fade(ids['higado']), fade(ids['vesicula'], after=True), fade(ids['duodeno'], after=True), fade(ids['duo2']), fade(ids['pancreas'], after=True),
           fade(ids['hepaticos'], after=True), fade(ids['cistico']), fade(ids['coledoco']), fade(ids['wirsung']), fade(ids['ampolla']))
    for m, c in zip(marks, cards):
        s.step(zoom(m), fade(c, after=True))
    s.note('Nota de rigor (ver Revisión científica): la obstrucción aislada del cístico (colecistitis) cursa a menudo con bilirrubina y FAL normales o levemente elevadas.')


def integracion_e(D):
    s = nueva(D, 5, 'Integración E: del zimógeno al diagnóstico', src=['PA 4 Zimógenos', 'PA 4.2 Pancreatitis: activación prematura', 'PA 3 Biomarcadores pancreáticos'], tipo='bandas', c1=DURAZNO_CL,
              c2=NARANJA)
    pasos = [('Páncreas', 'Células acinares con gránulos de zimógeno.', 'pan'), ('Zimógenos', 'Normalmente se activan en el duodeno (enteroquinasa → tripsina).', 'zim'),
             ('Lesión', 'Activación prematura dentro del páncreas → autodigestión → necrosis.', 'les'), ('Liberación de enzimas', 'Amilasa y lipasa pasan a la sangre.', 'lib'),
             ('Interpretación clínica', 'Dolor en cinturón + amilasa/lipasa > 3 × VN; perfil hepático para el diferencial.', 'int')]
    ids = []
    for k, (t, d, kind) in enumerate(pasos):
        x = 0.4 + k * 2.55
        g = s.group_start('Integración E %d' % (k + 1))
        if kind == 'pan':
            pancreas(s, x + 0.05, 1.6, 2.2, name='p')
        elif kind == 'zim':
            for j in range(4):
                s.shape(x + 0.4 + (j % 2) * 0.7, 1.4 + (j // 2) * 0.6, 0.5, 0.5, 'ellipse', ('rad', [(0, 'FFF9C4'), (60, 'FBC02D'), (100, 'C49000')], (35, 30)), ('7F6000', 1.0), False)
        elif kind == 'les':
            s.shape(x + 0.6, 1.3, 1.1, 1.1, 'irregularSeal1', ('a', ROJO, 70), None, False)
        elif kind == 'lib':
            ficha(s, x + 0.2, 1.5, 'Amilasa', 'F5B041', w=1.0, h=0.42, size=11)
            ficha(s, x + 1.25, 1.5, 'Lipasa', 'C0560E', w=0.95, h=0.42, size=11)
        else:
            for j, hh in enumerate((1.0, 1.15)):
                s.shape(x + 0.6 + j * 0.65, 2.55 - hh, 0.5, hh, 'rect', ['F5B041', 'C0560E'][j], (INK, 1.0), False)
        caja(s, x, 2.85, 2.35, 2.75, '**%s**\n%s' % (t, d), BLANCO, 14)
        if k < 4:
            s.arrow([(x + 2.37, 4.2), (x + 2.53, 4.2)], INK, 3)
        ids.append(s.group_end())
    c = caja(s, 0.4, 5.85, 12.55, 1.2, 'Un perfil, no un número: **amilasa + lipasa** con **transaminasas y bilirrubina normales** ubican el daño en el **páncreas**.', NAVY, 16, anchor='m',
             name='Síntesis E')
    for g in ids:
        s.step(fade(g))
    s.step(zoom(c))


def build(D):
    amilasa(D)
    lipasa(D)
    curvas_pancreas(D)
    zimogenos(D)
    activacion_normal(D)
    pancreatitis_seq(D)
    etiologia(D)
    clinica_pa(D)
    lab_pa(D)
    caso3(D)
    caso4(D)
    diferencial(D)
    anatomia_obstruccion(D)
    integracion_e(D)
