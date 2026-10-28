# -*- coding: utf-8 -*-
"""UNIDAD II (parte 1): termodinámica, reacciones acopladas (Morph), sistemas y reacciones redox."""
from plantillas import *


def divisor_u2(D):
    def arte(s):
        g = s.group_start('Arte unidad II')
        mitocondria_grande(s, 6.9, 0.5, 6.1, 3.4, name='Mitocondria div')
        enzima_globular(s, 8.3, 1.4, 1.2, 1.1, 'E59866', 'E1', 'E1 div', size=14)
        enzima_globular(s, 9.4, 1.9, 1.3, 1.2, '82E0AA', 'E2', 'E2 div', size=14, seed=3)
        enzima_globular(s, 10.6, 1.4, 1.2, 1.1, '85C1E9', 'E3', 'E3 div', size=14, seed=5)
        molecula3d(s, 7.0, 4.2, 2.6, 'piruvato', name='Piruvato div')
        molecula3d(s, 10.0, 4.1, 2.9, 'atp', name='ATP div')
        s.group_end()
        return g
    divisor(D, 2, 'II', 'Termodinámica, reacciones redox y metabolismo intermedio',
            'Cómo se transfiere la energía y cómo el piruvato se convierte en acetil-CoA',
            ['Entalpía, entropía y ΔG', 'Reacciones acopladas', 'Sistemas termodinámicos', 'Óxido-reducción y potencial redox', 'NAD^{+} y FAD',
             'Catabolismo y anabolismo', 'Regulación metabólica', 'Acetil-CoA', 'Piruvato', 'Complejo PDH y su regulación'], arte,
            src=['TM 1 Termodinámica'])


def tres_variables(D):
    s = nueva(D, 2, '¿Cuándo ocurre una reacción espontáneamente?', src=['TM 1 Termodinámica'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    rows = [['Variable', '¿Qué mide?', '¿Predice la espontaneidad?'],
            ['**Entalpía** (ΔH)', 'Calor liberado (exotérmica, ΔH < 0) o absorbido (endotérmica, ΔH > 0).', '**Insuficiente**: hay reacciones endotérmicas espontáneas.'],
            ['**Entropía** (ΔS)', 'Grado de **aleatoriedad** del sistema; el ΔS del universo tiende a aumentar.', '**Insuficiente** como variable aislada en un sistema delimitado: no considera los alrededores.'],
            ['**Energía libre de Gibbs** (ΔG)', 'Trabajo que puede realizarse durante la reacción; combina ΔH y ΔS.', '**Sí**: es el indicador de la espontaneidad.']]
    ids, H = tabla_filas(s, 0.4, 1.25, [2.2, 3.4, 3.0], rows, rowh=1.0, size=15, name='Tabla variables')
    ic = s.group_start('Íconos variables')
    flame(s, 9.6, 1.25, 0.9, name='Ícono calor')
    random.seed(3)
    for k in range(9):
        s.shape(10.9 + random.random() * 1.6, 1.3 + random.random() * 1.0, 0.25, 0.25, 'ellipse', shade('5DADE2', 0.4, 0.2), ('1B4F72', 0.75), False)
    s.group_end()
    c = caja(s, 9.35, 2.85, 3.7, 4.2, 'La termodinámica estudia **cuándo** una reacción química ocurre de forma espontánea. Se propusieron tres variables, cada una superando a la anterior: la respuesta final es **ΔG**.',
             BLANCO, 15, head='Idea', name='Idea termo')
    s.step(fade(ids[0]), fade(ic, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))


def nivel_diag(s, x, y, w, h, g1, g2, c1='5DADE2', c2='F5B041', lab1='Reactivos', lab2='Productos', name='Diagrama', hump=0.0, curve_col=INK):
    """diagrama energético: g1, g2 en fracción de la altura (0 abajo, 1 arriba). Devuelve dict de ids."""
    ids = {}
    ids['ejes'] = ejes(s, x, y, w, h, 'avance de la reacción', 'G', name=name + ' ejes')
    y1 = y + h * (1 - g1); y2 = y + h * (1 - g2)
    ids['r'] = s.shape(x + 0.25, y1 - 0.04, w * 0.28, 0.08, 'rect', c1, (INK, 1.0), False, name=name + ' nivel inicial')
    ids['rl'] = texto(s, x + 0.25, y1 - 0.48, w * 0.28, 0.4, lab1, 14, INK, True, 'c', name=name + ' rótulo inicial')
    ids['p'] = s.shape(x + w * 0.68, y2 - 0.04, w * 0.28, 0.08, 'rect', c2, (INK, 1.0), False, name=name + ' nivel final')
    ids['pl'] = texto(s, x + w * 0.68, y2 - 0.48 if g2 > g1 or True else y2 + 0.1, w * 0.28, 0.4, lab2, 14, INK, True, 'c', name=name + ' rótulo final')
    top = min(y1, y2) - h * hump
    pts = [(0, int((y1 - y) / h * 1000)), (300, int((y1 - y) / h * 1000)), (500, int((top - y) / h * 1000)), (700, int((y2 - y) / h * 1000)),
           (1000, int((y2 - y) / h * 1000))]
    ids['c'] = curva(s, x + 0.25 + w * 0.14, y, w * 0.68, h, pts, curve_col, 3, name=name + ' transformación', dash='dash')
    col = VERDE_OSC if g2 < g1 else ROJO
    ids['dg'] = s.arrow([(x + w * 0.62, y1), (x + w * 0.62, y2)], col, 4, name=name + ' ΔG')
    return ids


def entalpia(D):
    s = nueva(D, 2, 'Entalpía: calor liberado o absorbido', src=['TM 1 Termodinámica', 'TM 1.2 Exergónica vs endergónica'], tipo='bandas', c1=DURAZNO_CL, c2=CELESTE)
    a = nivel_diag(s, 0.6, 1.6, 5.6, 3.4, 0.75, 0.3, 'F5B041', 'E74C3C', 'Reactivos', 'Productos', name='Exotérmica')
    fa = flame(s, 4.1, 2.0, 0.65, name='Calor liberado')
    la = caja(s, 0.4, 5.35, 5.9, 1.7, '**Exotérmica**: ΔH < 0, la reacción **libera calor**.', 'FCE4D6', 17, anchor='m', name='Exotérmica texto')
    b = nivel_diag(s, 7.0, 1.6, 5.6, 3.4, 0.3, 0.75, '85C1E9', '5DADE2', 'Reactivos', 'Productos', name='Endotérmica')
    fb = flame(s, 9.6, 3.6, 0.65, name='Calor absorbido')
    lb = caja(s, 7.0, 5.35, 5.9, 1.7, '**Endotérmica**: ΔH > 0, la reacción **absorbe calor**. Se expresa en kcal/mol o kJ/mol.', CELESTE, 17, anchor='m', name='Endotérmica texto')
    s.step(fade(a['ejes']), fade(a['r'], after=True), fade(a['rl']), wipe(a['c'], 'l', after=True), fade(a['p'], after=True), fade(a['pl']))
    s.step(wipe(a['dg'], 't'), fade(fa, after=True), path(fa, 0.9, -0.6, after=True), fade(la, after=True))
    s.step(fade(b['ejes']), fade(b['r'], after=True), fade(b['rl']), wipe(b['c'], 'l', after=True), fade(b['p'], after=True), fade(b['pl']))
    s.step(fade(fb), path(fb, 0.3, -0.9, after=True), wipe(b['dg'], 'b', after=True), fade(lb, after=True))


def entropia(D):
    s = nueva(D, 2, 'Entropía: del orden al desorden', src=['TM 1 Termodinámica'], tipo='izq', c1=VERDE_CL, c2=BLANCO)
    caj = s.shape(0.5, 1.4, 4.3, 3.6, 'rect', ('a', 'FFFFFF', 60), (INK, 2.0), False, name='!!Sistema')
    parts = []
    for k in range(16):
        parts.append(s.shape(0.8 + (k % 4) * 0.45, 1.75 + (k // 4) * 0.45, 0.32, 0.32, 'ellipse', shade('5DADE2', 0.4, 0.2), ('1B4F72', 1.0), False,
                             name='!!Partícula %d' % k))
    random.seed(8)
    moves = [(random.uniform(0.0, 2.3) - (k % 4) * 0.45 + 0.3, random.uniform(-0.2, 2.6) - (k // 4) * 0.45) for k in range(16)]
    o = rotulo(s, 0.7, 5.2, 'Orden (baja entropía)', CELESTE, 14, name='Rótulo orden')
    d = rotulo(s, 2.9, 5.2, 'Desorden (alta entropía)', ROSA, 14, name='Rótulo desorden')
    c1 = caja(s, 5.3, 1.2, 7.7, 1.7, '**ΔS** mide el grado de **aleatoriedad** del sistema. A mayor temperatura, mayor movimiento de partículas y mayor aleatoriedad.', AMA, 16,
              name='Def entropía')
    c2 = caja(s, 5.3, 3.15, 7.7, 1.5, 'Cuando el sistema pasa **del orden al desorden** tiende a ser espontáneo; el **ΔS del universo** tiende siempre a aumentar.', BLANCO, 16,
              name='Tendencia entropía')
    c3 = caja(s, 5.3, 4.9, 7.7, 1.6, 'Como variable **aislada** no alcanza para expresar la espontaneidad de una reacción biológica dentro de un **sistema delimitado**: no considera los alrededores.',
              ROSA, 16, head='Limitación', headfill=ROJO, name='Limitación entropía')
    s.step(fade(caj), *[fade(p, after=(k == 0), dur=200) for k, p in enumerate(parts)], fade(o, after=True))
    s.step(fade(c1))
    s.step(*[path(p, mx, my, after=(k == 0), dur=1000) for k, (p, (mx, my)) in enumerate(zip(parts, moves))], fade(d, after=True), fade(c2, after=True))
    s.step(fade(c3))


def gibbs(D):
    s = nueva(D, 2, 'Energía libre de Gibbs', src=['TM 1 Termodinámica', 'TM 12 Glosario'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    f = s.group_start('!!Fórmula Gibbs')
    s.shape(0.6, 1.4, 8.0, 1.6, 'roundRect', AMA, (INK, 2.5), SH_I, 'ΔG = ΔH − T·ΔS', 50, F_BODY, INK, True, 'c', 'm', (0.1, 0, 0.1, 0), adj={'adj': 12000}, fit=False)
    s.group_end()
    t1 = caja(s, 0.6, 3.3, 2.5, 1.9, '**ΔH**\nentalpía (calor)', 'FCE4D6', 17, align='c', anchor='m', name='Término ΔH')
    t2 = caja(s, 3.35, 3.3, 2.5, 1.9, '**T**\ntemperatura absoluta', CREMA, 17, align='c', anchor='m', name='Término T')
    t3 = caja(s, 6.1, 3.3, 2.5, 1.9, '**ΔS**\nentropía (aleatoriedad)', CELESTE, 17, align='c', anchor='m', name='Término ΔS')
    flc = s.group_start('Flechas términos')
    for x in (1.85, 4.6, 7.35):
        s.arrow([(x, 3.25), (x, 3.0)], INK, 2.5)
    s.group_end()
    c = caja(s, 0.6, 5.5, 8.0, 1.55, 'La variación de energía libre permite evaluar la **favorabilidad termodinámica** de una reacción a **temperatura y presión constantes**.', BLANCO, 16,
             name='Uso ΔG')
    d = caja(s, 9.35, 1.2, 3.7, 3.0, '**Exergónica**: libera energía libre (ΔG < 0).\n**Endergónica**: consume energía libre (ΔG > 0).', BLANCO, 15.5, head='Vocabulario',
             name='Vocabulario Gibbs')
    m = molecula3d(s, 9.8, 4.5, 2.6, 'atp', name='ATP deco')
    s.step(zoom(f))
    s.step(wipe(flc, 'b'), fade(t1, after=True), fade(t2), fade(t3))
    s.step(fade(c))
    s.step(fade(d), fade(m, after=True))


def regla_dg(D):
    s = nueva(D, 2, 'La regla del ΔG', src=['TM 1.1 Regla fundamental'], tipo='bandas', c1=VERDE_CL, c2=ROSA)
    pan = []
    for i, (t, d, col, slope) in enumerate((('ΔG < 0', '**Espontánea (exergónica)**: libera energía; los productos son más estables que los reactivos.', VERDE_OSC, -1),
                                            ('ΔG > 0', '**No espontánea (endergónica)**: necesita energía del exterior; los productos tienen más energía.', ROJO, 1),
                                            ('ΔG = 0', '**Equilibrio**: no hay transformación neta.', NAVY, 0))):
        x = 0.45 + i * 4.2
        g = s.group_start('Panel ' + t)
        caja(s, x, 1.2, 3.95, 4.9, '', BLANCO, 12, lw=2.0)
        manuscrito(s, x + 0.2, 1.35, 3.55, 0.8, t, 30, col)
        if slope == -1:
            s.free(x + 0.3, 2.4, 3.35, 1.6, 'M 0 0 L 1000 1000 L 0 1000 Z', ('lin', [(0, 'A9CF86'), (100, '6CA848')], 90), (INK, 1.5))
        elif slope == 1:
            s.free(x + 0.3, 2.4, 3.35, 1.6, 'M 1000 0 L 1000 1000 L 0 1000 Z', ('lin', [(0, 'F5B7B1'), (100, 'E74C3C')], 90), (INK, 1.5))
        else:
            s.shape(x + 0.3, 3.6, 3.35, 0.4, 'rect', ('lin', [(0, CELESTE), (100, AZUL_M)], 90), (INK, 1.5), False)
            s.shape(x + 1.7, 2.6, 0.55, 1.0, 'triangle', NAVY, (INK, 1.0), False)
            s.shape(x + 0.9, 2.45, 2.15, 0.12, 'rect', NAVY, None, False)
        texto(s, x + 0.25, 4.2, 3.45, 1.8, d, 16.5, INK)
        s.group_end(); pan.append(g)
    b1 = s.shape(0.85, 1.95, 0.55, 0.55, 'ellipse', shade('F39C12', 0.4, 0.2), (INK, 1.25), False, name='Bola cuesta abajo')
    b2 = s.shape(4.7, 3.5, 0.55, 0.55, 'ellipse', shade('F39C12', 0.4, 0.2), (INK, 1.25), False, name='Bola cuesta arriba')
    cor = perla(s, 0.45, 6.3, 12.4, 0.8, 'Corolario: si una reacción es espontánea en un sentido (ΔG < 0), la **inversa** es no espontánea (mismo valor, signo opuesto).', 15,
                head='Corolario')
    s.step(fade(pan[0]), fade(b1, after=True), path(b1, 2.5, 1.45, after=True, dur=900))
    s.step(fade(pan[1]), fade(b2, after=True), path(b2, 1.2, -0.75, after=True, dur=1100, pts=[(0.6, -0.36), (0.9, -0.5)]), path(b2, -1.2, 0.75, after=True, dur=700))
    s.step(fade(pan[2]))
    s.step(fade(cor))


def grafico_g(D):
    s = nueva(D, 2, 'Gráfico de energía libre: exergónica frente a endergónica', src=['TM 1.2 Exergónica vs endergónica'], tipo='der', c1=VERDE_CL, c2=BLANCO)
    X, Y, W, H = 0.7, 1.5, 7.9, 4.7
    ej = ejes(s, X, Y, W, H, 'avance de la reacción', 'energía libre (G)', name='!!Ejes G')
    y1 = Y + H * 0.3; y2 = Y + H * 0.75
    r = s.shape(X + 0.3, y1 - 0.05, 1.9, 0.1, 'rect', '5DADE2', (INK, 1.0), False, name='Nivel reactivos A')
    rl = texto(s, X + 0.3, y1 - 0.5, 1.9, 0.4, 'Reactivos', 15, INK, True, 'c', name='Rótulo reactivos A')
    cur = curva(s, X + 2.2, Y, 3.4, H, [(0, 300), (300, 320), (600, 600), (1000, 750)], INK, 3, name='Transformación A', dash='dash', W=1000, H=1000)
    p = s.shape(X + 5.6, y2 - 0.05, 1.9, 0.1, 'rect', 'F5B041', (INK, 1.0), False, name='Nivel productos A')
    pl = texto(s, X + 5.6, y2 + 0.1, 1.9, 0.4, 'Productos', 15, INK, True, 'c', name='Rótulo productos A')
    dg = s.arrow([(X + 6.55, y1), (X + 6.55, y2 - 0.08)], VERDE_OSC, 5, name='Flecha ΔG A')
    dgl = rotulo(s, X + 6.75, (y1 + y2) / 2 - 0.25, 'ΔG < 0', VERDE_OSC, 18, name='Rótulo ΔG A')
    # comparación: endergónica
    r2 = s.shape(X + 0.3, y2 - 0.05, 1.9, 0.1, 'rect', '85C1E9', (ROJO, 1.0, 'dash'), False, name='Nivel reactivos B')
    p2 = s.shape(X + 5.6, Y + H * 0.12 - 0.05, 1.9, 0.1, 'rect', 'F1948A', (ROJO, 1.0, 'dash'), False, name='Nivel productos B')
    dg2 = s.arrow([(X + 3.2, y2), (X + 3.2, Y + H * 0.12)], ROJO, 5, name='Flecha ΔG B')
    dgl2 = rotulo(s, X + 3.4, Y + H * 0.3, 'ΔG > 0', ROJO, 18, name='Rótulo ΔG B')
    c1 = caja(s, 9.35, 1.2, 3.7, 2.6, '**Exergónica**: los productos tienen **menos** energía; la diferencia se libera. Como un objeto que **rueda cuesta abajo**.', 'EAF5EA', 15,
              head='Signo negativo', name='Interp A')
    c2 = caja(s, 9.35, 4.05, 3.7, 3.0, '**Endergónica**: los productos tienen **más** energía; el exterior debe aportarla. Como **empujar un objeto cuesta arriba**.', ROSA, 15,
              head='Comparación', headfill=ROJO, name='Interp B')
    s.step(fade(ej))
    s.step(fade(r), fade(rl, after=True))
    s.step(wipe(cur, 'l', dur=900))
    s.step(fade(p), fade(pl, after=True))
    s.step(wipe(dg, 't'), zoom(dgl, after=True))
    s.step(fade(c1))
    s.step(fade(r2), fade(p2, after=True), wipe(dg2, 'b', after=True), zoom(dgl2, after=True), fade(c2, after=True))


def exo_vs_exer(D):
    s = nueva(D, 2, 'Exotérmica no es lo mismo que exergónica', src=['TM 1.2 Exergónica vs endergónica'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    a = caja(s, 0.45, 1.3, 4.0, 2.6, '**Exotérmica / endotérmica**\nSe refieren al **calor** (ΔH).', 'FCE4D6', 19, align='c', anchor='m', name='Calor')
    fl = flame(s, 1.95, 4.3, 1.0, name='Llama')
    b = caja(s, 4.9, 1.3, 4.0, 2.6, '**Exergónica / endergónica**\nSe refieren a la **energía libre** (ΔG): el trabajo disponible.', 'EAF5EA', 19, align='c', anchor='m', name='Trabajo')
    ba = s.group_start('Balanza')
    s.shape(6.6, 5.4, 0.6, 0.9, 'triangle', NAVY, (INK, 1.0), False)
    s.shape(5.3, 5.25, 3.2, 0.13, 'rect', NAVY, None, False)
    s.shape(5.1, 4.6, 0.9, 0.62, 'ellipse', shade('F5B041', 0.4, 0.2), (INK, 1.0), False, 'ΔH', 13, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.shape(7.8, 4.6, 0.9, 0.62, 'ellipse', shade('5DADE2', 0.4, 0.2), (INK, 1.0), False, 'TΔS', 13, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    c = caja(s, 9.3, 1.3, 3.75, 3.0, 'ΔG combina ambos términos: una reacción puede absorber calor y aun así ser espontánea si el término **T·ΔS** compensa.', AMA, 15.5,
             name='Combinación')
    m = molecula3d(s, 9.9, 4.6, 2.4, 'glucosa', name='Glucosa deco 2')
    s.step(fade(a), fade(fl, after=True))
    s.step(fade(b), fade(ba, after=True))
    s.step(fade(c), fade(m, after=True))


def inversa(D):
    s = nueva(D, 2, 'Una reacción y su inversa', src=['TM 1.1 Regla fundamental'], tipo='bandas', c1=VERDE_CL, c2=ROSA)
    l = s.group_start('Lado izquierdo')
    ficha(s, 3.5, 2.0, 'Oxalacetato', 'F5B041', w=2.0, name='OAA')
    ficha(s, 3.5, 2.6, 'NADH', '1F618D', w=2.0, name='NADH inv')
    s.group_end()
    rr = s.group_start('Lado derecho')
    ficha(s, 8.1, 2.0, 'Malato', '58D68D', w=2.0, name='Malato')
    ficha(s, 8.1, 2.6, 'NAD^{+}', '85C1E9', w=2.0, name='NAD inv')
    s.group_end()
    f1 = s.arrow([(5.7, 2.35), (7.9, 2.35)], VERDE_OSC, 4, name='Directa')
    l1 = rotulo(s, 5.75, 1.45, 'ΔG = −7,1 kcal/mol', VERDE_OSC, 15, w=2.1, name='ΔG directa')
    f2 = s.arrow([(7.9, 3.5), (5.7, 3.5)], ROJO, 4, name='Inversa', dash='dash')
    l2 = rotulo(s, 5.75, 3.75, 'ΔG = +7,1 kcal/mol', ROJO, 15, w=2.1, name='ΔG inversa')
    c1 = caja(s, 3.5, 4.75, 4.2, 2.3, 'Oxalacetato + NADH → malato + NAD^{+}: **espontánea**.', 'EAF5EA', 17, anchor='m', name='Explicación directa')
    c2 = caja(s, 7.95, 4.75, 2.1, 2.3, 'Malato → oxalacetato: **necesita energía**.', ROSA, 15, anchor='m', name='Explicación inversa')
    m1 = molecula3d(s, 0.3, 1.5, 2.7, 'aa', name='Deco inv 1')
    m2 = molecula3d(s, 10.5, 1.4, 2.6, 'piruvato', name='Deco inv 2')
    p = caja(s, 0.35, 4.75, 2.9, 2.3, 'Mismo valor absoluto, **signo opuesto**.', AMA, 18, anchor='m', name='Regla inversa')
    s.step(fade(m1), fade(m2, after=True), fade(l, after=True))
    s.step(wipe(f1, 'l'), fade(rr, after=True), fade(l1, after=True), fade(c1, after=True))
    s.step(wipe(f2, 'r'), fade(l2, after=True), fade(c2, after=True))
    s.step(zoom(p))


def velocidad(D):
    s = nueva(D, 2, 'Favorable no significa rápida', src=['REV TM 1', 'VB 1.2 C Enzimas'], tipo='der', c1=AZUL_M, c2=BLANCO)
    X, Y, W, H = 0.7, 1.5, 7.8, 4.4
    ej = ejes(s, X, Y, W, H, 'avance de la reacción', 'G', name='Ejes velocidad')
    r = s.shape(X + 0.3, Y + H * 0.35 - 0.05, 1.7, 0.1, 'rect', '5DADE2', (INK, 1.0), False, name='Nivel R v')
    p = s.shape(X + 5.8, Y + H * 0.75 - 0.05, 1.7, 0.1, 'rect', 'F5B041', (INK, 1.0), False, name='Nivel P v')
    alta = curva(s, X + 2.0, Y, 3.8, H, [(0, 350), (250, 330), (500, 40), (750, 600), (1000, 750)], ROJO, 3.5, name='Barrera alta')
    baja = curva(s, X + 2.0, Y, 3.8, H, [(0, 350), (250, 340), (500, 230), (750, 640), (1000, 750)], VERDE_OSC, 3.5, name='Barrera con enzima')
    dg = s.arrow([(X + 6.65, Y + H * 0.35), (X + 6.65, Y + H * 0.75 - 0.08)], NAVY, 4, name='ΔG v')
    dgl = rotulo(s, X + 6.85, Y + H * 0.5, 'ΔG (igual)', NAVY, 14, name='Rótulo ΔG v')
    lab1 = rotulo(s, X + 2.9, Y - 0.05, 'barrera sin catalizador', ROSA, 13, name='Rótulo barrera alta')
    lab2 = rotulo(s, X + 2.6, Y + H * 0.2, 'enzima: barrera menor', 'D5F5E3', 13, name='Rótulo barrera baja')
    c1 = caja(s, 0.6, 6.15, 8.0, 0.9, 'El **signo de ΔG** indica si la reacción es favorable; **no** dice con qué velocidad ocurre.', AMA, 16, anchor='m', name='Idea velocidad')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'La **velocidad** depende de la barrera energética que debe superarse. Las **enzimas aceleran** las reacciones (son catalizadores biológicos) '
               'disminuyendo esa barrera, **sin cambiar el ΔG** ni el sentido favorable de la reacción.', 14.5, name='Rigor velocidad')
    s.step(fade(ej), fade(r, after=True), fade(p, after=True))
    s.step(wipe(alta, 'l'), fade(lab1, after=True), wipe(dg, 't', after=True), fade(dgl, after=True))
    s.step(fade(c1))
    s.step(wipe(baja, 'l'), fade(lab2, after=True))
    s.step(fade(r_))


# ================================================================ reacciones acopladas (Morph)
AC_TXT = {1: 'Reacción desfavorable: glucosa → glucosa-6-fosfato', 2: 'Hidrólisis del ATP', 3: 'Acoplamiento de ambas reacciones',
          4: 'Suma de las variaciones de energía libre', 5: 'Reacción global acoplada', 6: 'Interpretación termodinámica del acoplamiento'}


def escena_ac(D, st):
    s = nueva(D, 2, AC_TXT[st], tipo='der', c1=VERDE_OSC, c2=BLANCO, morph=st > 1, src=['TM 2 Reacciones acopladas'], tw=8.7)
    ids = {}
    # eje de energía (escala vertical: 1 kcal/mol = 0.36")
    X0, Y0 = 0.9, 4.3   # cero
    k = 0.36
    ids['eje'] = s.group_start('!!Eje energía')
    s.arrow([(X0, 6.95), (X0, 1.25)], INK, 2.25)
    s.arrow([(X0, Y0), (8.7, Y0)], '7F8C8D', 1.5, tail=None, dash='dash')
    texto(s, X0 + 0.1, 1.2, 2.6, 0.35, 'ΔG (kcal/mol)', 13, INK, True)
    texto(s, X0 - 0.75, Y0 - 0.18, 0.6, 0.36, '0', 14, INK, True, 'r')
    s.group_end()
    # barras
    def barra(nm, x, val, col, txt, show):
        if not show:
            return None
        y = Y0 - val * k if val > 0 else Y0
        return s.shape(x, y, 0.95, abs(val) * k, 'rect', ('lin', [(0, lighten(col, 0.35)), (100, col)], 0), (INK, 1.5), False, txt, 15, F_HEAD,
                       INK, True, 'c', 'm', (0, 0, 0, 0), name=nm, fit=False)
    bx = {1: (1.6, 3.0, 6.2), 2: (1.6, 3.0, 6.2), 3: (1.6, 3.0, 6.2), 4: (1.6, 2.55, 6.2), 5: (1.6, 2.55, 6.2), 6: (1.6, 2.55, 6.2)}[st]
    if st >= 4:
        # barras apiladas: +3,3 desde 0, luego −7,3 desde +3,3
        ids['b1'] = s.shape(bx[0], Y0 - 3.3 * k, 0.95, 3.3 * k, 'rect', ('lin', [(0, 'F5B7B1'), (100, 'E74C3C')], 0), (INK, 1.5), False, '+3,3', 15, F_HEAD, INK, True,
                            'c', 'm', (0, 0, 0, 0), name='!!Barra glucosa', fit=False)
        ids['b2'] = s.shape(bx[1], Y0 - 3.3 * k, 0.95, 7.3 * k, 'rect', ('lin', [(0, 'A9DFBF'), (100, '27AE60')], 0), (INK, 1.5), False, '−7,3', 15, F_HEAD, INK, True,
                            'c', 'm', (0, 0, 0, 0), name='!!Barra ATP', fit=False)
        if st >= 5:
            ids['b3'] = s.shape(bx[2], Y0, 0.95, 4.0 * k, 'rect', ('lin', [(0, 'AED6F1'), (100, '2E86C1')], 0), (INK, 2.0), False, '−4,0', 16, F_HEAD, INK, True,
                                'c', 'm', (0, 0, 0, 0), name='!!Barra total', fit=False)
    else:
        ids['b1'] = barra('!!Barra glucosa', bx[0], 3.3, 'E74C3C', '+3,3', True)
        ids['b2'] = barra('!!Barra ATP', bx[1], -7.3, '27AE60', '−7,3', st >= 2)
    # reacciones (fichas)
    if st == 1:
        ids['glc'] = ficha(s, 3.2, 1.5, 'Glucosa', '3B82C4', w=1.7, name='!!Glucosa')
        ids['g6p'] = ficha(s, 6.3, 1.5, 'Glucosa-6-P', 'AF7AC5', w=1.9, name='!!G6P')
        ids['f1'] = s.arrow([(5.0, 1.71), (6.2, 1.71)], ROJO, 3, name='!!Flecha R1', dash='dash')
    elif st == 2:
        ids['glc'] = ficha(s, 3.2, 1.5, 'Glucosa', '3B82C4', w=1.7, name='!!Glucosa')
        ids['g6p'] = ficha(s, 6.3, 1.5, 'Glucosa-6-P', 'AF7AC5', w=1.9, name='!!G6P')
        ids['f1'] = s.arrow([(5.0, 1.71), (6.2, 1.71)], ROJO, 3, name='!!Flecha R1', dash='dash')
        ids['atp'] = ficha(s, 4.3, 5.0, 'ATP', 'FFC000', w=1.1, name='!!ATP')
        ids['adp'] = ficha(s, 6.6, 5.0, 'ADP', 'F8C471', w=1.1, name='!!ADP')
        ids['pi'] = ficha(s, 7.8, 5.0, 'P_{i}', 'F39C12', w=0.75, name='!!Pi')
        ids['f2'] = s.arrow([(5.45, 5.21), (6.5, 5.21)], VERDE_OSC, 3, name='!!Flecha R2')
    elif st >= 3:
        y = 1.5
        ids['glc'] = ficha(s, 2.9 if st < 6 else 2.9, y, 'Glucosa', '3B82C4', w=1.5, name='!!Glucosa')
        ids['atp'] = ficha(s, 4.55, y, 'ATP', 'FFC000', w=0.9, name='!!ATP')
        ids['f1'] = s.arrow([(5.55, y + 0.21), (6.35, y + 0.21)], VERDE_OSC if st >= 5 else NAVY, 3, name='!!Flecha R1')
        ids['g6p'] = ficha(s, 6.45, y, 'Glucosa-6-P', 'AF7AC5', w=1.6, name='!!G6P')
        ids['adp'] = ficha(s, 8.15, y, 'ADP', 'F8C471', w=0.8, name='!!ADP')
    return s, ids


def acopladas(D):
    ini = len(D.slides) + 1
    # 1
    s, i = escena_ac(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.3, 'Glucosa → glucosa-6-fosfato\n**ΔG = +3,3 kcal/mol**\nLa glucosa **no se fosforila sola**: la reacción es no espontánea.', ROSA, 16,
             head='Reacción 1', headfill=ROJO, name='Caja R1')
    r_ = rigor(s, 9.35, 4.8, 3.7, 2.25, 'Los valores corresponden a **condiciones estándar** (ΔG°′); en la célula el ΔG real depende de las concentraciones.', 13.5, name='Rigor estándar')
    s.step(fade(i['eje']))
    s.step(fade(i['glc']), wipe(i['f1'], 'l', after=True), fade(i['g6p'], after=True))
    s.step(wipe(i['b1'], 'b'), fade(c, after=True))
    s.step(fade(r_))
    # 2
    s, i = escena_ac(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'ATP → ADP + P_{i}\n**ΔG = −7,3 kcal/mol**\nLa hidrólisis del ATP es **muy espontánea**.', 'EAF5EA', 16, head='Reacción 2', headfill=VERDE_OSC,
             name='Caja R2')
    s.step(fade(i['atp']), wipe(i['f2'], 'l', after=True), fade(i['adp'], after=True), fade(i['pi'], after=True))
    s.step(wipe(i['b2'], 't'), fade(c, after=True))
    # 3
    s, i = escena_ac(D, 3)
    eng = s.group_start('Engranajes')
    s.shape(3.9, 2.4, 1.0, 1.0, 'gear6', shade('F5B041', 0.4, 0.2), (INK, 1.25), False)
    s.shape(4.75, 2.85, 0.8, 0.8, 'gear6', shade('58D68D', 0.4, 0.2), (INK, 1.25), False)
    s.group_end()
    c = caja(s, 9.35, 1.2, 3.7, 3.6, 'Las células realizan reacciones **desfavorables** acoplándolas a reacciones **muy favorables**: el fosfato terminal del ATP pasa a la glucosa en una **única reacción**.',
             AMA, 15.5, head='Acoplamiento', name='Caja R3')
    s.step(fade(eng), spin(eng, after=True, dur=900))
    s.step(fade(c))
    # 4
    s, i = escena_ac(D, 4)
    sm = caja(s, 3.9, 4.6, 4.8, 1.0, '(+3,3) + (−7,3) = **−4,0** kcal/mol', BLANCO, 20, align='c', anchor='m', name='Suma')
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Las variaciones de energía libre **se suman**: la barra verde «paga» la roja y aún sobra energía.', AMA, 16, head='Suma', name='Caja R4')
    s.step(fade(sm))
    s.step(fade(c))
    # 5
    s, i = escena_ac(D, 5)
    lb = rotulo(s, 4.6, 6.2, 'ΔG total = −4,0 kcal/mol', VERDE_OSC, 17, name='ΔG total')
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Glucosa + ATP → glucosa-6-fosfato + ADP\n**ΔG total = −4,0 kcal/mol → espontánea**.', 'EAF5EA', 16, head='Reacción global',
             headfill=VERDE_OSC, name='Caja R5')
    s.step(wipe(i['b3'], 't'), zoom(lb, after=True))
    s.step(fade(c))
    # 6
    s, i = escena_ac(D, 6)
    c = caja(s, 9.35, 1.2, 3.7, 2.7, 'La suma total del ΔG de todas las reacciones del proceso debe ser **negativa**.', AMA, 16, head='Regla', name='Regla acoplamiento')
    c2 = caja(s, 9.35, 4.15, 3.7, 2.9, 'Por eso el ATP es la **moneda energética** de la célula: su hidrólisis es tan exergónica que «paga» reacciones desfavorables.', BLANCO, 15,
              head='Moneda energética', name='Moneda')
    m = molecula3d(s, 3.4, 4.75, 2.4, 'atp', name='ATP 3D')
    s.step(fade(c))
    s.step(fade(m), fade(c2, after=True))
    registrar_morph(D, ini, len(D.slides), 'Reacción acoplada: fosforilación de la glucosa con hidrólisis de ATP',
                    ['!!Eje energía', '!!Barra glucosa', '!!Barra ATP', '!!Barra total', '!!Glucosa', '!!G6P', '!!ATP', '!!ADP', '!!Pi', '!!Flecha R1', '!!Flecha R2'],
                    'Las fichas de las dos reacciones convergen en una sola ecuación; la barra del ATP se desplaza y se apila sobre la de glucosa; aparece la barra del ΔG total.')


def punto_control(D):
    s = nueva(D, 2, 'La reacción con el ΔG más negativo controla la vía', src=['TM 2 Reacciones acopladas', 'TM 7.1 Reversibilidad', 'REV TM 2'], tipo='izq', c1=VERDE_CL, c2=BLANCO)
    pasos = s.group_start('!!Escalera de la vía')
    ys = [1.5, 1.9, 2.25, 4.4, 4.7, 5.0]
    for k in range(5):
        x = 0.5 + k * 1.75
        col = ROJO if k == 2 else NAVY
        s.shape(x, ys[k], 1.4, 0.12, 'rect', col, None, False)
        if k < 4:
            s.arrow([(x + 1.45, ys[k] + 0.06), (x + 1.75, ys[k + 1] + 0.06)], col if k == 2 else INK, 4.5 if k == 2 else 2)
    s.group_end()
    big = rotulo(s, 4.2, 3.0, 'ΔG muy negativo', ROJO, 16, name='Paso clave')
    c1 = caja(s, 0.4, 5.55, 8.6, 1.5, 'Una vez que esa reacción ocurre, el proceso **no puede detenerse**: es la que el organismo **regula**; si se controla ese paso, se controla **toda la vía**.',
              AMA, 15.5, name='Control vía')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'Los pasos regulados suelen ser los **irreversibles**, lejos del equilibrio, como el primero comprometido de cada vía. No todos los pasos de ΔG negativo son reguladores: '
               'la regulación depende de las **enzimas** que catalizan esos pasos.', 14, name='Rigor punto control')
    s.step(wipe(pasos, 'l', dur=900))
    s.step(zoom(big))
    s.step(fade(c1))
    s.step(fade(r_))


def sistemas(D):
    s = nueva(D, 2, 'Sistemas termodinámicos: los seres vivos son abiertos', src=['TM 3 Sistemas termodinámicos'], tipo='bandas', c1=CELESTE, c2=VERDE_CL)
    pan = []
    for i, (t, en, ma, f) in enumerate((('AISLADO', 'NO', 'NO', CELESTE), ('CERRADO', 'SÍ', 'NO', CREMA), ('ABIERTO', 'SÍ', 'SÍ', 'EAF5EA'))):
        x = 0.45 + i * 4.2
        g = s.group_start('Sistema ' + t)
        caja(s, x, 1.2, 3.95, 5.85, '', f, 12, lw=2.0)
        manuscrito(s, x + 0.2, 1.3, 3.55, 0.7, t, 26, TBLUE)
        if i == 0:
            s.shape(x + 1.3, 2.1, 1.35, 2.4, 'can', shade('95A5A6', 0.4, 0.3), (INK, 1.5), SH_I)
            s.shape(x + 1.45, 1.95, 1.05, 0.35, 'roundRect', '34495E', (INK, 1.0), False)
            ej = 'Termo'
        elif i == 1:
            s.shape(x + 0.75, 2.8, 2.45, 1.4, 'can', shade('7F8C8D', 0.4, 0.3), (INK, 1.5), SH_I)
            s.shape(x + 0.6, 2.55, 2.75, 0.35, 'roundRect', '2C3E50', (INK, 1.0), False)
            flame(s, x + 1.65, 4.25, 0.6, name='Fuego')
            ej = 'Olla con tapa'
        else:
            human(s, x + 1.35, 2.0, 2.6, name='Ser vivo')
            ej = 'Seres vivos'
        texto(s, x + 0.25, 4.75, 3.45, 0.45, 'Ejemplo: **%s**' % ej, 16, INK, False, 'c')
        texto(s, x + 0.25, 5.3, 3.45, 0.45, 'Energía: **%s**' % en, 18, VERDE_OSC if en == 'SÍ' else ROJO, False, 'c')
        texto(s, x + 0.25, 5.85, 3.45, 0.45, 'Materia: **%s**' % ma, 18, VERDE_OSC if ma == 'SÍ' else ROJO, False, 'c')
        s.group_end(); pan.append(g)
    fl = []
    calor = s.arrow([(5.1, 3.4), (4.6, 2.6)], 'E67E22', 3.5, name='Calor sale')
    for k, (p1, p2, col) in enumerate((((9.4, 2.6), (10.3, 3.0), 'E67E22'), ((11.6, 3.0), (12.6, 2.5), 'E67E22'), ((9.3, 4.2), (10.25, 4.0), '27AE60'), ((11.7, 4.0), (12.65, 4.4), '7F8C8D'))):
        fl.append(s.arrow([p1, p2], col, 3.5, name='Intercambio %d' % k))
    s.step(fade(pan[0]))
    s.step(fade(pan[1]), wipe(calor, 'b', after=True))
    s.step(fade(pan[2]), *[wipe(f, 'l', after=(k == 0)) for k, f in enumerate(fl)])
    s.note('Abierto: intercambia materia (nutrientes, desechos, gases) y energía (calor, trabajo) con el entorno de forma permanente.')


def homeostasis(D):
    s = nueva(D, 2, 'Homeostasis, estado estacionario, regulación y control', src=['TM 3 Sistemas termodinámicos'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    tq = s.group_start('!!Tanque estacionario')
    s.shape(2.5, 1.9, 3.0, 3.2, 'rect', ('a', 'FFFFFF', 50), (INK, 2.0), False)
    s.shape(2.53, 3.1, 2.94, 1.97, 'rect', ('lin', [(0, '85C1E9'), (100, '2E86C1')], 90), None, False)
    s.group_end()
    ent = s.arrow([(0.7, 2.3), (2.45, 2.3)], VERDE_OSC, 5, name='Entrada')
    sal = s.arrow([(5.55, 4.6), (7.4, 4.6)], ROJO, 5, name='Salida')
    le = rotulo(s, 0.5, 1.6, 'entrada de materia y energía', 'EAF5EA', 13, name='Rótulo entrada')
    ls = rotulo(s, 5.5, 4.95, 'salida', ROSA, 13, name='Rótulo salida')
    est = caja(s, 5.9, 1.3, 2.9, 2.6, '**Estado estacionario**: lo que entra se equilibra con lo que sale; el nivel se mantiene aunque el flujo continúe.', CREMA, 14.5,
               name='Estado estacionario')
    c1 = caja(s, 0.5, 5.55, 8.2, 1.5, '**Homeostasis**: equilibrio interno de los seres vivos como sistemas abiertos; no podemos «dar todo ni tomar todo»: **equilibrio dinámico** con el medio.',
              AMA, 15.5, name='Homeostasis')
    c2 = caja(s, 9.35, 1.2, 3.7, 2.7, '**Regulación metabólica**: mantiene el **estado estacionario** del flujo de metabolitos.', BLANCO, 16, head='Regulación', name='Regulación')
    c3 = caja(s, 9.35, 4.2, 3.7, 2.85, '**Control metabólico**: influencia sobre **enzimas específicas** (puntos de control) para **alterar el flujo** ante señales externas.', CREMA, 16,
              head='Control', name='Control')
    s.step(fade(tq), wipe(ent, 'l', after=True), fade(le, after=True), wipe(sal, 'l', after=True), fade(ls, after=True))
    s.step(fade(est))
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(c3))


# ================================================================ REDOX
def redox_concepto(D):
    s = nueva(D, 2, 'Reacciones redox: transferencia de electrones', src=['TM 4.1 Concepto fundamental'], tipo='izq', c1=CELESTE, c2=BLANCO)
    a = enzima_globular(s, 0.6, 2.0, 2.3, 2.0, 'F5B041', 'Dador\n(se oxida)', '!!Reductor', size=15, seed=2)
    b = enzima_globular(s, 5.8, 2.0, 2.3, 2.0, '85C1E9', 'Aceptor\n(se reduce)', '!!Oxidante', size=15, seed=6)
    es = [s.shape(2.4, 2.4 + k * 0.55, 0.42, 0.42, 'ellipse', shade('F4D03F', 0.45, 0.2), ('7D6608', 1.25), False, 'e^{−}', 12, F_HEAD, INK, True, 'c', 'm',
                  (0, 0, 0, 0), name='!!Electrón %d' % k, fit=False) for k in range(2)]
    arc = s.arrow([(2.9, 2.0), (4.3, 1.4), (5.8, 2.0)], NAVY, 3, curve=True, name='Trayecto electrones')
    c = caja(s, 0.5, 4.65, 7.8, 2.4, 'Una reacción redox **siempre involucra transferencia de electrones** entre dos especies químicas. **No puede haber oxidación sin reducción** simultánea: si alguien pierde, otro gana.',
              AMA, 16, name='Concepto redox')
    t1 = caja(s, 8.8, 1.2, 4.25, 2.7, '**OXIDACIÓN**\nPérdida de electrones → el número de oxidación **aumenta**.', ROSA, 16, name='Def oxidación')
    t2 = caja(s, 8.8, 4.2, 4.25, 2.85, '**REDUCCIÓN**\nGanancia de electrones → el número de oxidación **disminuye**.', 'EAF5EA', 16, name='Def reducción')
    s.step(fade(a), fade(b, after=True))
    s.step(*[fade(e, after=(k > 0)) for k, e in enumerate(es)])
    s.step(wipe(arc, 'l'), *[path(e, 3.55, -0.2 - k * 0.55 + 0.4, after=(k == 0), dur=1100, pts=[(1.7, -1.0)]) for k, e in enumerate(es)], colorear(a, 'F9E79F', after=True),
           colorear(b, '2E86C1'))
    s.step(fade(t1))
    s.step(fade(t2))
    s.step(fade(c))


def agentes(D):
    s = nueva(D, 2, 'Agente oxidante y agente reductor', src=['TM 4.1 Concepto fundamental'], tipo='bandas', c1=ROSA, c2='EAF5EA')
    rows = [['Término', 'Definición'], ['Oxidación', '**Pérdida** de electrones: el número de oxidación **aumenta** (queda con carga más positiva).'],
            ['Reducción', '**Ganancia** de electrones: el número de oxidación **disminuye** (queda con carga más negativa).'],
            ['Agente reductor', 'La especie que **se oxida** (pierde e^{−}) y, al hacerlo, **reduce** a la otra.'],
            ['Agente oxidante', 'La especie que **se reduce** (gana e^{−}) y, al hacerlo, **oxida** a la otra.']]
    ids, H = tabla_filas(s, 3.55, 1.25, [2.2, 4.4], rows, rowh=0.95, size=16, name='Tabla redox')
    mn = caja(s, 0.4, 1.25, 2.9, 5.8, 'Los electrones son **negativos**:\n- quien **gana** e^{−} gana carga negativa → su número de oxidación **baja** → se **reduce**;\n- quien **pierde** e^{−} → su número **sube** → se **oxida**.',
              AMA, 15, head='Mnemotecnia', name='Mnemotecnia')
    cruz = s.group_start('Cruce de roles')
    caja(s, 10.45, 1.25, 2.55, 2.6, '**Oxidante**\n= el que **se reduce**', 'EAF5EA', 17, align='c', anchor='m')
    caja(s, 10.45, 4.45, 2.55, 2.6, '**Reductor**\n= el que **se oxida**', ROSA, 17, align='c', anchor='m')
    s.arrow([(11.7, 3.9), (11.7, 4.4)], INK, 3, head='triangle')
    s.group_end()
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(mn))
    s.step(fade(cruz))


def organica(D):
    s = nueva(D, 2, 'Redox en química orgánica: hidrógenos y oxígenos', src=['TM 4.2 Química orgánica', 'REV TM 4.2'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    rows = [['Proceso', 'Indicador en química orgánica'], ['Reducción (gana e^{−})', '**Gana hidrógenos** o **pierde oxígenos**'],
            ['Oxidación (pierde e^{−})', '**Pierde hidrógenos** o **gana oxígenos**']]
    ids, H = tabla_filas(s, 0.4, 1.25, [3.4, 5.2], rows, rowh=0.75, size=17, name='Tabla orgánica')
    A = caja(s, 0.4, 3.85, 4.15, 1.6, 'Molécula A: **C_{6}H_{12}O_{6}**\n6 oxígenos → **más oxidada**', ROSA, 17, align='c', anchor='m', name='Molécula A')
    B = caja(s, 4.85, 3.85, 4.15, 1.6, 'Molécula B: **C_{6}H_{12}O_{2}**\n2 oxígenos → **más reducida**', 'EAF5EA', 17, align='c', anchor='m', name='Molécula B')
    c = caja(s, 0.4, 5.7, 8.6, 1.35, 'Cuanto **más reducida** está una molécula (más H, menos O), **más energía potencial** tiene para ceder: los sustratos reducidos son la «moneda» del catabolismo.',
             AMA, 15.5, name='Corolario orgánica')
    r_ = rigor(s, 9.35, 1.2, 3.7, 3.4, 'En las oxidaciones biológicas no se transfiere un protón aislado: se transfieren **átomos de hidrógeno** (H^{+} + e^{−}) o un **ion hidruro** (H^{−}: 2 e^{−} + H^{+}), como en el NADH.',
               13.5, name='Rigor hidrógeno')
    m = molecula3d(s, 9.9, 4.85, 2.3, 'glucosa', name='Glucosa ox')
    s.step(fade(ids[0]), fade(ids[1], after=True), fade(ids[2], after=True))
    s.step(fade(A))
    s.step(fade(B))
    s.step(fade(c))
    s.step(fade(r_), fade(m, after=True))


def potencial(D):
    s = nueva(D, 2, 'Potencial redox: la tendencia a ganar o ceder electrones', src=['TM 5 Potencial redox'], tipo='izq', c1=VERDE_CL, c2=BLANCO)
    c1 = caja(s, 0.4, 1.2, 4.0, 2.5, 'Cuantifica la tendencia de una sustancia a **ganar o perder electrones**. Se mide en **voltios (V)**.', AMA, 17, head='Definición', name='Def potencial')
    pos = caja(s, 4.75, 1.2, 4.0, 2.9, 'Mayor tendencia a **aceptar** electrones: se **reduce** y actúa como **agente oxidante**.\nEjemplo: **O_{2} (+0,82 V)**.', 'EAF5EA', 15.5,
               head='Valor positivo', headfill=VERDE_OSC, name='Positivo')
    neg = caja(s, 9.05, 1.2, 4.0, 2.9, 'Mayor tendencia a **ceder** electrones: se **oxida** y actúa como **agente reductor**.\nEjemplo: **NADH (≈ −0,32 V)**.', ROSA, 15.5,
               head='Valor negativo', headfill=ROJO, name='Negativo')
    o2 = s.group_start('O2 agua')
    ficha(s, 4.9, 4.6, 'O_{2}', '5DADE2', w=1.0, name='O2 p')
    s.arrow([(6.0, 4.81), (6.8, 4.81)], INK, 2.5)
    ficha(s, 6.9, 4.6, 'H_{2}O', '85C1E9', w=1.1, name='H2O p')
    s.group_end()
    c2 = caja(s, 4.75, 5.35, 8.3, 1.7, 'El **oxígeno** es el aceptor final de la cadena respiratoria: tiene el potencial **más positivo**, acepta los electrones, se reduce y forma **H_{2}O**. Por eso respiramos oxígeno.',
              BLANCO, 15.5, name='Oxígeno aceptor')
    r_ = rigor(s, 0.4, 3.95, 4.0, 3.1, 'Notación: el valor de cada par es su **potencial de reducción estándar (E°′)**; **ΔE°′** es la **diferencia** entre el aceptor y el dador.', 14,
               name='Rigor notación')
    s.step(fade(c1))
    s.step(fade(pos))
    s.step(fade(neg))
    s.step(fade(o2), fade(c2, after=True))
    s.step(fade(r_))


def escala(D):
    s = nueva(D, 2, 'Escala de potenciales: la caída de los electrones', src=['TM 5 Potencial redox', 'TM 5.1 Relación ΔG y ΔE'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    top, bot = 1.35, 6.85
    def Y(v):
        return top + (v + 0.45) / (0.85 + 0.45) * (bot - top)
    esc = s.group_start('!!Escala redox')
    s.shape(1.0, top, 0.5, bot - top, 'rect', ('lin', [(0, 'F5B7B1'), (50, 'FDFEFE'), (100, 'A9DFBF')], 90), (INK, 1.5), False)
    texto(s, 0.05, top - 0.05, 0.95, 0.6, 'más\nreductor', 12, ROJO, True, 'c')
    texto(s, 0.05, bot - 0.55, 0.95, 0.6, 'más\noxidante', 12, VERDE_OSC, True, 'c')
    s.group_end()
    pares = [('H_{2} / H^{+}', -0.42, 'D5DBDB'), ('NADH / NAD^{+}', -0.32, '1F618D'), ('FADH_{2} / FAD', -0.18, 'F4D03F'), ('Citocromo c', 0.23, 'E59866'),
             ('O_{2} / H_{2}O', 0.82, '5DADE2')]
    ids = []
    for k, (t, v, col) in enumerate(pares):
        y = Y(v)
        g = s.group_start('Par ' + plain(t))
        s.arrow([(1.5, y), (2.0, y)], INK, 2, tail=None)
        ficha(s, 2.05, y - 0.23, t, col, w=2.3, h=0.46, size=14)
        texto(s, 4.45, y - 0.2, 1.3, 0.4, ('%+.2f V' % v).replace('.', ','), 15, INK, True)
        ids.append(s.group_end())
    gap = s.shape(1.55, Y(0.0) - 0.18, 0.4, 0.36, 'rect', None, None, False, '⋮', 18, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), name='Pares intermedios', fit=False)
    e = s.shape(5.9, Y(-0.32) - 0.22, 0.44, 0.44, 'ellipse', shade('F4D03F', 0.45, 0.2), ('7D6608', 1.25), False, 'e^{−}', 12, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
                name='!!Electrones', fit=False)
    caida = s.arrow([(6.12, Y(-0.32) + 0.25), (6.12, Y(0.82) - 0.25)], NAVY, 4, name='Caída de energía')
    lab = caja(s, 6.6, 3.2, 2.3, 1.9, 'Los e^{−} fluyen del **más negativo** al **más positivo** y liberan energía.', AMA, 14, name='Flujo e')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Mayor tendencia a **ceder**: H_{2} > NADH > FADH_{2} > succinato/fumarato > …\nMayor tendencia a **aceptar**: … > citocromo c > **O_{2}**.', BLANCO, 14.5,
             head='Jerarquía', name='Jerarquía')
    c2 = caja(s, 9.35, 4.45, 3.7, 2.6, 'El **O_{2}** (+0,82 V) es el mayor aceptor: recibe los electrones al final de la cadena respiratoria.', 'EAF5EA', 15, name='O2 mayor aceptor')
    s.step(fade(esc))
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids)], fade(gap, after=True))
    s.step(fade(c))
    s.step(zoom(e), path(e, 0, Y(0.82) - Y(-0.32), after=True, dur=1200), wipe(caida, 't'), fade(lab, after=True))
    s.step(fade(c2))


def dg_de(D):
    s = nueva(D, 2, 'ΔG y ΔE°′: la conexión termodinámica', src=['TM 5.1 Relación ΔG y ΔE'], tipo='bandas', c1=VERDE_CL, c2=CREMA)
    f = s.group_start('!!Fórmula Faraday')
    s.shape(0.6, 1.3, 8.6, 1.5, 'roundRect', AMA, (INK, 2.5), SH_I, 'ΔG°′ = − n · F · ΔE°′', 44, F_BODY, INK, True, 'c', 'm', (0.1, 0, 0.1, 0), adj={'adj': 12000}, fit=False)
    s.group_end()
    terms = [('n', 'número de electrones transferidos', 'FCE4D6'), ('F', 'constante de Faraday: 96 500 C/mol', CELESTE),
             ('ΔE°′', 'diferencia de potencial entre oxidante y reductor', 'EAF5EA')]
    ids = [caja(s, 0.6 + i * 2.9, 3.05, 2.75, 1.75, '**%s**: %s' % (t, d), f_, 15, anchor='m', name='Término ' + t) for i, (t, d, f_) in enumerate(terms)]
    sig = caja(s, 0.6, 5.05, 8.6, 0.95, 'ΔE°′ > 0 → ΔG°′ < 0 → la reacción redox es **espontánea**; cuanto mayor el ΔE°′, **más energía** se libera.', 'EAF5EA', 16, anchor='m', name='Signo')
    ej = caja(s, 0.6, 6.15, 8.6, 0.9, 'Ejemplo: la oxidación del **NADH por O_{2}** tiene el mayor ΔE°′ de la cadena respiratoria → libera la mayor cantidad de energía.', BLANCO, 15,
              anchor='m', name='Ejemplo NADH')
    calc = caja(s, 9.55, 1.3, 3.5, 5.75, '**Cálculo con los valores de la escala**\nΔE°′ = (+0,82) − (−0,32) = **1,14 V**\nΔG°′ = −2 × 96 500 × 1,14\n≈ **−220 kJ/mol**\n(≈ −52,6 kcal/mol)',
                CREMA, 15.5, head='Aplicación', name='Cálculo')
    s.step(zoom(f))
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids)])
    s.step(fade(sig))
    s.step(fade(ej))
    s.step(fade(calc))
    s.note('El cálculo usa exclusivamente los potenciales listados (O2 +0,82 V; NADH −0,32 V) y F = 96 500 C/mol, con n = 2 electrones.')


def nad_fad(D):
    s = nueva(D, 2, 'NAD^{+}/NADH y FAD/FADH_{2}: transportadores de electrones', src=['TM 4.2 Química orgánica', 'TM 5.2 NAD vs FAD'], tipo='izq', c1=CELESTE, c2=BLANCO)
    n1 = s.group_start('!!NAD+')
    s.shape(0.7, 1.6, 1.3, 1.3, 'hexagon', shade('AED6F1', 0.4, 0.2), ('1B4F72', 1.5), False, 'N^{+}', 18, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
            adj={'adj': 28000, 'vf': 115470}, fit=False)
    texto(s, 0.4, 3.0, 1.9, 0.45, 'NAD^{+}', 20, NAVY, True, 'c')
    s.group_end()
    hid = s.shape(2.6, 1.95, 0.6, 0.6, 'ellipse', shade('F4D03F', 0.45, 0.2), ('7D6608', 1.25), False, 'H^{−}', 14, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
                  name='!!Hidruro', fit=False)
    n2 = s.group_start('!!NADH')
    s.shape(4.4, 1.6, 1.3, 1.3, 'hexagon', shade('1F618D', 0.3, 0.2), ('0B2545', 1.5), False, 'N–H', 17, F_HEAD, BLANCO, True, 'c', 'm', (0, 0, 0, 0),
            adj={'adj': 28000, 'vf': 115470}, fit=False)
    texto(s, 4.1, 3.0, 1.9, 0.45, 'NADH', 20, NAVY, True, 'c')
    s.group_end()
    fl1 = s.arrow([(2.1, 2.25), (4.3, 2.25)], INK, 3, name='Reducción NAD')
    f1 = s.group_start('!!FAD')
    s.shape(0.7, 4.2, 1.6, 1.0, 'roundRect', shade('F4D03F', 0.4, 0.2), ('7D6608', 1.5), False, 'FAD', 18, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False, adj={'adj': 30000})
    s.group_end()
    hs = [s.shape(2.55, 4.25 + k * 0.5, 0.42, 0.42, 'ellipse', shade('F9E79F', 0.45, 0.2), ('7D6608', 1.25), False, 'H', 12, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
                  name='!!H FAD %d' % k, fit=False) for k in range(2)]
    f2 = s.group_start('!!FADH2')
    s.shape(4.25, 4.2, 1.6, 1.0, 'roundRect', shade('D4AC0D', 0.3, 0.2), ('7D6608', 1.5), False, 'FADH_{2}', 18, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
            adj={'adj': 30000})
    s.group_end()
    fl2 = s.arrow([(2.4, 4.7), (4.15, 4.7)], INK, 3, name='Reducción FAD')
    c1 = caja(s, 6.4, 1.2, 6.65, 2.25, '**NAD^{+} → NADH**: el NADH tiene más energía que el NAD^{+} porque lleva **2 electrones** en forma de **hidruro (H^{−})**.', 'EAF2F8', 16,
              head='NAD', headfill=NAVY, name='Caja NAD')
    c2 = caja(s, 6.4, 3.75, 6.65, 2.0, '**FAD → FADH_{2}**: acepta dos electrones (con dos protones); puede cederlos **de a uno**.', CREMA, 16, head='FAD', headfill=AMA2, name='Caja FAD')
    c3 = caja(s, 0.4, 5.95, 12.65, 1.1, 'Las **coenzimas reducidas** (NADH, FADH_{2}) son la moneda energética del catabolismo: transportan electrones hacia la cadena respiratoria.', AMA, 16,
              anchor='m', name='Coenzimas reducidas')
    s.step(fade(n1), fade(hid, after=True))
    s.step(path(hid, 1.8, 0.0, dur=800), wipe(fl1, 'l', after=True), out(hid, after=True), fade(n2, after=True), fade(c1, after=True))
    s.step(fade(f1), *[fade(h, after=True) for h in hs])
    s.step(*[path(h, 1.6, -0.25 + k * -0.25, after=(k > 0), dur=800) for k, h in enumerate(hs)], wipe(fl2, 'l', after=True), *[out(h, after=(k == 0)) for k, h in enumerate(hs)],
           fade(f2, after=True), fade(c2, after=True))
    s.step(fade(c3))


def nad_vs_fad(D):
    s = nueva(D, 2, '¿Por qué el NADH rinde más energía que el FADH_{2}?', src=['TM 5.2 NAD vs FAD', 'TM 5.1 Relación ΔG y ΔE', 'REV TM 5.2'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    top, bot = 1.4, 6.4
    def Y(v):
        return top + (v + 0.45) / (0.85 + 0.45) * (bot - top)
    esc = s.group_start('Escala NAD FAD')
    s.shape(0.8, top, 0.45, bot - top, 'rect', ('lin', [(0, 'F5B7B1'), (50, 'FDFEFE'), (100, 'A9DFBF')], 90), (INK, 1.5), False)
    ficha(s, 1.4, Y(-0.32) - 0.23, 'NADH −0,32 V', '1F618D', w=2.3, h=0.46, size=14)
    ficha(s, 1.4, Y(-0.18) - 0.23 + 0.15, 'FADH_{2} −0,18 V', 'F4D03F', w=2.3, h=0.46, size=14)
    ficha(s, 1.4, Y(0.82) - 0.23, 'O_{2} +0,82 V', '5DADE2', w=2.3, h=0.46, size=14)
    s.group_end()
    b1 = s.arrow([(4.1, Y(-0.32)), (4.1, Y(0.82))], NAVY, 6, name='ΔE NADH')
    b2 = s.arrow([(4.9, Y(-0.18) + 0.15), (4.9, Y(0.82))], 'B7950B', 6, name='ΔE FADH2')
    l1 = rotulo(s, 3.5, Y(0.82) + 0.15, 'mayor ΔE°′', NAVY, 13, name='Rótulo ΔE NADH')
    c1 = caja(s, 5.5, 1.3, 3.5, 2.75, 'Los electrones del **NADH** parten de un potencial **más negativo** que los del FADH_{2}: su caída hasta el O_{2} es mayor y libera **más energía**.',
              AMA, 14.5, name='Explicación ΔE')
    c2 = caja(s, 5.5, 4.3, 3.5, 2.75, 'Modelo clásico de rendimiento: **3 ATP por NADH** y **2 ATP por FADH_{2}** en la cadena respiratoria.', BLANCO, 14.5, name='Rendimiento clásico')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'Estimaciones actuales: **≈ 2,5 ATP/NADH** y **≈ 1,5 ATP/FADH_{2}**. La diferencia se explica por el **potencial** y el **punto de ingreso** de los electrones a la cadena, '
               'no por ceder los electrones «de golpe» o «de a uno».', 14, name='Rigor rendimiento')
    s.step(fade(esc))
    s.step(wipe(b1, 't'), fade(l1, after=True), wipe(b2, 't', after=True), fade(c1, after=True))
    s.step(fade(c2))
    s.step(fade(r_))


def build(D):
    divisor_u2(D)
    tres_variables(D)
    entalpia(D)
    entropia(D)
    gibbs(D)
    regla_dg(D)
    grafico_g(D)
    exo_vs_exer(D)
    inversa(D)
    velocidad(D)
    acopladas(D)
    punto_control(D)
    sistemas(D)
    homeostasis(D)
    redox_concepto(D)
    agentes(D)
    organica(D)
    potencial(D)
    escala(D)
    dg_de(D)
    nad_fad(D)
    nad_vs_fad(D)
