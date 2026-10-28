# -*- coding: utf-8 -*-
"""UNIDAD I (parte 1): variables bioquímicas, composición de la sangre, unidades y líquidos biológicos."""
from plantillas import *


def persona_ico(s, x, y, h, fill, name='Persona', line=INK):
    g = s.group_start(name)
    s.shape(x + h * 0.18, y, h * 0.34, h * 0.34, 'ellipse', fill, (line, 1.0), False)
    s.shape(x, y + h * 0.38, h * 0.7, h * 0.62, 'flowChartDelay', fill, (line, 1.0), False, rot=-90)
    return s.group_end()


def tiroides(s, x, y, w, name='!!Tiroides'):
    h = w * 0.7
    pts = [(500, 420), (420, 200), (300, 60), (150, 80), (60, 300), (80, 650), (220, 900), (400, 880), (500, 700), (600, 880), (780, 900),
           (920, 650), (940, 300), (850, 80), (700, 60), (580, 200)]
    return s.free(x, y, w, h, smooth(pts, True, 0.6), shade('C0392B', 0.45, 0.3), ('641E16', 1.75), SH_I, name=name)


def ion(s, x, y, d, txt, col, name):
    return s.shape(x, y, d, d, 'ellipse', shade(col, 0.45, 0.25), (darken(col, 0.5), 1.5), SH_I, txt, d * 22, F_HEAD,
                   BLANCO, True, 'c', 'm', (0, 0, 0, 0), name=name, fit=False)


def divisor_u1(D):
    def arte(s):
        g = s.group_start('Arte unidad I')
        brazo(s, 6.8, 0.6, 4.2, name='Brazo div')
        jeringa(s, 9.6, 0.75, 3.0, name='Jeringa div')
        for i, (col, f) in enumerate((('8E44AD', 0.5), ('C0392B', 0.5), ('27AE60', 0.45), ('F1C40F', 0.55))):
            tubo(s, 7.2 + i * 1.05, 3.0, 0.6, 2.6, [(f, 'B3261E', 'R%d' % i), (0.82 - f, 'F9E79F', 'P%d' % i)] if i % 2 == 0 else [(0.82, 'B3261E', 'R%d' % i)],
                 tapa=col, name='Tubo div %d' % i)
        centrifuga(s, 11.4, 3.2, 1.6, name='Centrífuga div')
        gi, hits = diana(s, 11.5, 5.4, 1.5, [(0.05, -0.04), (-0.06, 0.05), (0.03, 0.06)], name='Diana div')
        molecula3d(s, 6.8, 5.7, 1.5, 'glucosa', name='Glucosa div')
        s.group_end()
        return g
    divisor(D, 1, 'I', 'Variables bioquímicas y fundamentos del laboratorio clínico',
            'Qué se mide, en qué muestra, con qué unidad y cómo se interpreta',
            ['Variables bioquímicas', 'Composición de la sangre', 'Unidades de medida', 'Suero y plasma',
             'Sensibilidad y especificidad', 'Valores predictivos', 'Precisión y exactitud', 'Intervalos de referencia', 'Control de calidad'], arte,
            src=['VB 1 Variables bioquímicas'])


def definicion(D):
    s = nueva(D, 1, 'Variable bioquímica: definición', src=['VB 1.1 Definición'], tipo='izq', c1=CELESTE, c2=BLANCO)
    # ilustración: paciente → tubo → número
    h = human(s, 0.4, 1.2, 4.6, name='!!Organismo')
    sang = vessel(s, 1.0, 3.3, 3.2, 0.55, name='Vaso', rbcs=7)
    t = tubo(s, 2.95, 1.35, 0.55, 2.0, [(0.5, 'B3261E', 'Rojo def'), (0.32, 'F9E79F', 'Plasma def')], name='!!TuboMuestra')
    mol_ = molecula3d(s, 0.25, 5.8, 1.35, 'glucosa', name='Analito')
    d = caja(s, 5.05, 1.15, 7.9, 1.25, 'Cantidad o **concentración de una sustancia presente en un fluido biológico** que se utiliza para evaluar si un paciente '
             'está sano o enfermo.', AMA, 18, name='Definición')
    conds = [('Unidades estandarizadas', 'mg/dL, mmol/L, UI/L… permiten comparar resultados entre laboratorios.', CELESTE),
             ('Valor de referencia', 'Establecido estadísticamente a partir de una **población sana**.', CREMA),
             ('Significado clínico', 'Refleja un proceso **fisiológico o patológico** determinado: medir sin información clínica asociada no sirve.', 'EAF5EA')]
    ids = []
    for i, (hd, tx, f) in enumerate(conds):
        ids.append(caja(s, 5.05 + i * 2.67, 2.75, 2.5, 3.0, tx, f, 16, head=hd, name='Condición %d' % (i + 1)))
    p = caja(s, 5.05, 6.05, 7.9, 0.95, 'Las **tres condiciones** deben cumplirse para que un parámetro sea una variable bioquímica válida.', NAVY, 16,
             anchor='m', name='Síntesis')
    s.step(fade(h), fade(sang), fade(t['vidrio'], after=True), fade(t['Rojo def']), fade(t['Plasma def']))
    s.step(zoom(mol_), fade(d, after=True))
    for g in ids:
        s.step(fade(g))
    s.step(wipe(p, 'l'))
    s.note('Una variable bioquímica une tres elementos: una unidad estandarizada, un intervalo de referencia y un significado clínico.')


def familias(D):
    s = nueva(D, 1, 'Cuatro familias de variables bioquímicas', src=['VB 1.2 Tipos de variables'], tipo='bandas', c1=CREMA, c2=CELESTE)
    q = [('Metabolitos', 'Productos de un metabolismo: su cantidad informa el estado de esa vía.', 'F5B041'),
         ('Electrolitos', 'Cationes y aniones minerales: Na^{+}, K^{+}, Cl^{-}, Ca^{2+}.', '5DADE2'),
         ('Enzimas', 'Catalizadores biológicos: su elevación en sangre puede indicar daño de un órgano.', 'E59866'),
         ('Hormonas', 'Mensajeros endocrinos: informan sobre la comunicación celular.', 'BB8FCE')]
    ids = []
    for i, (t, d, c) in enumerate(q):
        x = 0.55 + (i % 2) * 6.2; y = 1.2 + (i // 2) * 2.95
        g = s.group_start('Familia ' + t)
        caja(s, x, y, 5.9, 2.7, '', BLANCO, 14, lw=2.0)
        if i == 0:
            molecula3d(s, x + 0.15, y + 0.2, 2.2, 'glucosa', name='Ícono glucosa')
        elif i == 1:
            for k, (tx, cc) in enumerate((('Na^{+}', '2E86C1'), ('K^{+}', '8E44AD'), ('Cl^{-}', '27AE60'), ('Ca^{2+}', 'E67E22'))):
                ion(s, x + 0.2 + (k % 2) * 1.05, y + 0.3 + (k // 2) * 1.05, 0.95, tx, cc, 'Ion %d' % k)
        elif i == 2:
            enzima_globular(s, x + 0.25, y + 0.4, 1.9, 1.7, c, 'Enzima', 'Ícono enzima', size=15)
        else:
            tiroides(s, x + 0.2, y + 0.55, 2.0, name='Ícono tiroides')
        manuscrito(s, x + 2.4, y + 0.2, 3.4, 0.7, t, 24, TBLUE, 'l')
        texto(s, x + 2.4, y + 0.95, 3.35, 1.6, d, 17)
        s.group_end(); ids.append(g)
    for g in ids:
        s.step(fade(g))


def metabolitos(D):
    s = nueva(D, 1, 'Metabolitos: el estado de cada metabolismo', src=['VB 1.2 A Metabolitos'], tipo='der', c1=AMA, c2=BLANCO)
    rows = [['Metabolito', 'Información que aporta', 'Metabolismo evaluado'],
            ['Glucosa', 'Estado del metabolismo de los carbohidratos', 'Hidratos de carbono'],
            ['Urea', 'Metabolismo de las proteínas', 'Proteínas / función renal'],
            ['Creatinina', 'Función renal (excreción de productos de desecho)', 'Renal'],
            ['Ácido úrico', 'Metabolismo de las bases púricas', 'Purinas']]
    ids, H = tabla_filas(s, 0.45, 1.3, [2.0, 3.9, 2.5], rows, rowh=0.75, size=16, name='Tabla metabolitos')
    mol1 = molecula3d(s, 9.4, 1.0, 1.9, 'glucosa', name='Molécula glucosa')
    mol2 = molecula3d(s, 11.3, 1.2, 1.6, 'urea', name='Molécula urea')
    k = kidney(s, 9.9, 3.2, 1.3, name='!!Riñón')
    lv = liver(s, 11.2, 3.5, 1.9, name='Hígado met')
    c = caja(s, 9.35, 5.55, 3.7, 1.5, 'La cuantificación del metabolito **informa sobre el estado de ese metabolismo**.', BLANCO, 15, name='Idea metabolitos')
    nota = caja(s, 0.45, 5.6, 8.4, 1.4, 'Ejemplo: la **creatinina** se interpreta como dato de **función renal**, porque su concentración depende de la excreción de productos de desecho.',
                CREMA, 16, name='Ejemplo creatinina')
    s.step(fade(ids[0]))
    for i, r in enumerate(ids[1:]):
        extra = [zoom(mol1, after=True)] if i == 0 else ([zoom(mol2, after=True), fade(lv, after=True)] if i == 1 else ([fade(k, after=True)] if i == 2 else []))
        s.step(fade(r), *extra)
    s.step(fade(c), fade(nota, after=True))


def electrolitos(D):
    s = nueva(D, 1, 'Electrolitos: cationes y aniones con significado clínico', src=['VB 1.2 B Electrolitos'], tipo='izq', c1=CELESTE, c2=BLANCO)
    data = [('Na^{+}', '2E86C1', 'Sodio', 'Estado de **hidratación** del paciente: normal, deshidratado o sobrehidratado.'),
            ('K^{+}', '8E44AD', 'Potasio', 'Evalúa la **excitabilidad** neuronal (transmisión sináptica correcta).'),
            ('Cl^{-}', '27AE60', 'Cloro', 'Informa sobre el **equilibrio ácido-base**: crisis de acidosis o alcalosis.'),
            ('Ca^{2+}', 'E67E22', 'Calcio', 'Evalúa la **función muscular** y el **sistema de coagulación**.')]
    ids = []
    for i, (sym, col, nm, tx) in enumerate(data):
        y = 1.15 + i * 1.45
        g = s.group_start('Electrolito ' + nm)
        ion(s, 0.9, y, 1.25, sym, col, '!!Ion ' + nm)
        manuscrito(s, 2.3, y + 0.25, 2.2, 0.7, nm, 22, TBLUE, 'l')
        caja(s, 4.95, y + 0.05, 5.0, 1.2, tx, BLANCO, 17, anchor='m')
        s.group_end(); ids.append(g)
    cap = capilar(s, 10.3, 1.3, 2.7, 1.0, name='Capilar iones')
    io = s.group_start('Iones decorativos')
    random.seed(5)
    for k in range(10):
        sym, col = random.choice((('Na^{+}', '2E86C1'), ('K^{+}', '8E44AD'), ('Cl^{-}', '27AE60'), ('Ca^{2+}', 'E67E22')))
        ion(s, 10.4 + random.random() * 2.3, 2.5 + random.random() * 1.6, 0.45, sym, col, 'Ion deco %d' % k)
    s.group_end()
    r = rigor(s, 10.15, 4.6, 3.0, 2.45, 'Cada ion participa en varios procesos; estas asociaciones son puntos de partida y se interpretan siempre junto con la clínica.', 13)
    s.step(fade(cap), fade(io, after=True))
    for g in ids:
        s.step(fade(g))
    s.step(fade(r))


def enzimas(D):
    s = nueva(D, 1, 'Enzimas: catalizadores que revelan qué órgano se dañó', src=['VB 1.2 C Enzimas'], tipo='der', c1=VERDE_CL, c2=BLANCO)
    hep = hepatocyte(s, 0.4, 1.35, 3.4, name='!!Hepatocito')
    vas = vessel(s, 0.2, 4.4, 8.6, 0.8, name='!!Vaso sanguíneo', rbcs=9)
    enzs = [s.shape(1.4 + k * 0.55, 2.4 + (k % 2) * 0.4, 0.32, 0.32, 'ellipse', shade('E59866', 0.4, 0.2), ('784212', 1.0), False, name='!!Enzima %d' % k)
            for k in range(4)]
    lab = texto(s, 3.9, 1.4, 4.9, 0.9, 'Lesión de la membrana → las enzimas intracelulares **pasan a la sangre**.', 17, name='Rótulo liberación')
    rows = [['Enzima', 'Origen', 'Significado de su elevación'], ['GPT (ALT)', 'Hígado (específica)', 'Daño hepático'],
            ['GOT (AST)', 'Hígado y músculo', 'Daño hepático o muscular'], ['Creatinquinasa (CK)', 'Músculos (principalmente)', 'Daño muscular'],
            ['LDH', 'Mayoría de las células', 'Necrosis celular']]
    ids, H = tabla_filas(s, 0.45, 5.35, [2.4, 2.6, 3.4], rows, rowh=0.33, size=13.5, name='Tabla enzimas')
    c = caja(s, 9.35, 1.2, 3.7, 2.4, 'Proteínas que **aceleran reacciones químicas**. Algunas predominan en determinados órganos: su aumento en sangre **orienta** al órgano dañado.',
             BLANCO, 15, head='Concepto', name='Concepto enzimas')
    r = rigor(s, 9.35, 3.85, 3.7, 3.2, 'La especificidad de órgano es **relativa**: la ALT predomina en hígado, pero existen otras fuentes; por eso las enzimas se piden e interpretan **en conjunto** (Unidad V).', 13.5)
    s.step(fade(hep), fade(vas, after=True), *[fade(e, after=(k == 0)) for k, e in enumerate(enzs)])
    s.step(fade(lab), *[path(e, 0.9 + k * 0.4, 2.55 - (k % 2) * 0.4, after=(k == 0), delay=0 if k == 0 else 120) for k, e in enumerate(enzs)])
    s.step(fade(c))
    for rr in ids:
        s.step(fade(rr)) if rr == ids[0] else s.anim[-1].append(fade(rr, after=True))
    s.step(fade(r))


def hormonas(D):
    s = nueva(D, 1, 'Hormonas: mensajeros de la comunicación celular', src=['VB 1.2 D Hormonas'], tipo='bandas', c1=LAVANDA, c2=CREMA)
    pan = pancreas(s, 0.3, 1.5, 2.9, name='Páncreas hormonas')
    ins = ficha(s, 0.8, 2.9, 'Insulina', '1F618D', w=1.7, name='Ficha insulina')
    clk = clock(s, 0.8, 4.0, 1.4, hours=8, name='Reloj cortisol')
    tir = tiroides(s, 0.6, 5.7, 2.0, name='Tiroides')
    items = [('Insulina', 'Evalúa el **control del metabolismo de los hidratos de carbono**.', CELESTE),
             ('Cortisol', 'Indica el **nivel de estrés** del organismo. Presenta ritmo circadiano: más alto a la mañana.', CREMA),
             ('T3, T4 y TSH', 'Evalúan la **función tiroidea** y el **metabolismo basal**.', ROSA)]
    ids = []
    for i, (t, d, f) in enumerate(items):
        ids.append(caja(s, 3.6, 1.2 + i * 1.95, 6.3, 1.75, d, f, 18, head=t, name='Hormona ' + t))
    m = molecula3d(s, 10.6, 1.0, 2.4, 'aa', name='Molécula decorativa')
    c = caja(s, 10.45, 3.9, 2.65, 3.1, 'Su medición informa sobre el **estado de la comunicación celular** del sistema endocrino.', BLANCO, 15, name='Síntesis hormonas')
    s.step(fade(pan), fade(ins, after=True), fade(ids[0], after=True))
    s.step(fade(clk), fade(ids[1], after=True))
    s.step(fade(tir), fade(ids[2], after=True))
    s.step(fade(m), fade(c, after=True))


def utilidad(D):
    s = nueva(D, 1, 'Utilidad clínica de las variables bioquímicas', src=['VB 1.3 Utilidad clínica', 'VB 8.1 Utilidad general'], tipo='izq', c1=CREMA, c2=BLANCO)
    # línea temporal de la enfermedad
    ej = ejes(s, 0.6, 1.6, 7.8, 3.1, 'tiempo', 'intensidad del proceso', name='Ejes evolución')
    cur = curva(s, 0.6, 1.6, 7.8, 3.1, [(0, 950), (250, 900), (450, 800), (600, 600), (750, 350), (1000, 120)], ROJO, 5, name='Curva enfermedad')
    umbral = s.arrow([(0.6, 3.0), (8.4, 3.0)], '5D6D7E', 2, tail=None, dash='dash', name='Umbral de síntomas')
    lbl1 = rotulo(s, 1.0, 4.85, 'Etapa subclínica: sin síntomas', CELESTE, 14, name='Etapa subclínica')
    lbl2 = rotulo(s, 5.4, 2.45, 'Aparecen los síntomas', SALM, 14, name='Etapa clínica')
    tb = tubo(s, 2.8, 3.35, 0.38, 1.3, [(0.5, 'B3261E', 'R ut'), (0.3, 'F9E79F', 'P ut')], name='Tubo', grupo='Tubo detección')
    cards = [('Detectar', 'Enfermedades en **etapas tempranas**, incluso antes de los síntomas.', CELESTE),
             ('Evaluar', 'La **función de los órganos**.', CREMA),
             ('Monitorizar', 'La **evolución** de una patología o la **respuesta a un tratamiento**.', 'EAF5EA'),
             ('Además', 'Confirmar diagnósticos, estimar **pronóstico** y aportar datos **epidemiológicos**.', ROSA)]
    ids = [caja(s, 9.0, 1.15 + i * 1.5, 4.05, 1.35, d, f, 15.5, head=t, name='Utilidad ' + t) for i, (t, d, f) in enumerate(cards)]
    nota = caja(s, 0.6, 5.5, 7.8, 1.5, 'En la etapa subclínica el laboratorio puede mostrar alteraciones **antes** de que el paciente perciba la enfermedad.',
                AMA, 16, name='Nota subclínica')
    s.step(fade(ej), wipe(cur, 'l', after=True, dur=1000))
    s.step(fade(umbral), fade(lbl1, after=True), fade(lbl2, after=True))
    s.step(zoom(tb), fade(nota, after=True))
    for g in ids:
        s.step(fade(g))


# ---------------------------------------------------------------- composición de la sangre
def sangre(D):
    s = nueva(D, 1, 'La sangre: una suspensión que puede separarse', src=['VB 2 Composición de la sangre'], tipo='der', c1=ROJO, c2=BLANCO)
    t = tubo(s, 1.0, 1.25, 1.6, 5.6, [(0.45, 'B3261E', '!!Elementos formes'), (0.55, 'F9E79F', '!!Plasma')], tapa='8E44AD', name='!!TuboMuestra')
    b1 = s.arrow([(2.75, 2.3), (3.6, 2.3)], INK, 2.5, name='Flecha plasma')
    l1 = caja(s, 3.7, 1.55, 5.0, 1.55, '**55 % plasma**\nComponente líquido o acuoso.', AMA, 18, name='Rótulo plasma')
    b2 = s.arrow([(2.75, 5.5), (3.6, 5.5)], INK, 2.5, name='Flecha formes')
    l2 = caja(s, 3.7, 4.75, 5.0, 1.55, '**45 % elementos formes**\nComponente celular: eritrocitos, leucocitos y plaquetas.', SALM, 18, name='Rótulo formes')
    c = caja(s, 9.35, 1.2, 3.7, 2.7, 'Tejido derivado del **tejido conectivo**. Fisicoquímicamente es una **mezcla heterogénea (suspensión)**: células suspendidas en un líquido.',
             BLANCO, 15, head='Concepto', name='Concepto sangre')
    cel = s.group_start('Células suspendidas')
    for k in range(5):
        eritrocito(s, 9.5 + (k % 3) * 1.15, 4.3 + (k // 3) * 1.1, 0.95, name='GR deco %d' % k)
    leucocito(s, 11.85, 5.4, 1.0, 'neutrofilo', name='Leucocito deco')
    plaqueta(s, 10.2, 6.6, 0.5, name='Plaqueta deco')
    s.group_end()
    s.step(fade(t['vidrio']), fade(t['!!Elementos formes'], after=True), fade(t['!!Plasma']))
    s.step(wipe(b1, 'l'), fade(l1, after=True))
    s.step(wipe(b2, 'l'), fade(l2, after=True))
    s.step(fade(c), fade(cel, after=True))


def plasma(D):
    s = nueva(D, 1, 'Plasma: composición de la fase líquida', src=['VB 2.1 Plasma'], tipo='bandas', c1=CREMA, c2=AMA)
    # barra apilada
    x0, y0, W = 0.6, 1.5, 0.0
    segs = [('Agua ~90 %', 0.90, '5DADE2'), ('Proteínas ~7 %', 0.07, 'F5B041'), ('Metabolitos, electrolitos, hormonas ~1–3 %', 0.03, 'E74C3C')]
    g = s.group_start('!!Barra plasma')
    yy = 1.3
    hh = 5.6
    for nm, fr, col in segs:
        h_ = max(hh * fr, 0.28)
        s.shape(x0, yy, 2.0, h_, 'rect', ('lin', [(0, lighten(col, 0.3)), (100, col)], 0), (INK, 1.5), False, name='Barra ' + nm)
        yy += h_
    s.group_end()
    cards = [('Agua ~90 %', 'Componente mayoritario. Mantiene el **estado líquido** de la sangre.', CELESTE, 1.3),
             ('Proteínas plasmáticas ~7 %', '**Principal soluto** sanguíneo. Mantienen la **osmolaridad (presión osmótica)** y evitan edemas.', CREMA, 3.15),
             ('Metabolitos, electrolitos, hormonas ~1–3 %', 'Componentes minoritarios: son **los analitos que se miden** habitualmente en el laboratorio.', ROSA, 5.0)]
    ids = []
    for t, d, f, y in cards:
        gg = s.group_start('Plasma ' + t[:12])
        s.arrow([(2.7, y + 0.75), (3.55, y + 0.75)], INK, 2.25)
        caja(s, 3.6, y, 6.4, 1.6, d, f, 17, head=t)
        ids.append(s.group_end())
    mols = s.group_start('Moléculas plasma')
    molecula3d(s, 10.55, 1.2, 2.3, 'glucosa', name='Glucosa plasma')
    molecula3d(s, 10.7, 3.7, 2.0, 'urea', name='Urea plasma')
    s.group_end()
    tb = tubo(s, 11.1, 5.5, 0.4, 1.6, [(0.45, 'B3261E', 'R pl'), (0.4, 'F9E79F', 'P pl')], name='Tubo plasma mini')
    s.step(wipe(g, 'b'))
    for i in ids:
        s.step(fade(i))
    s.step(fade(mols), fade(tb['vidrio'], after=True), fade(tb['R pl']), fade(tb['P pl']))


def osmotica(D):
    s = nueva(D, 1, 'Proteínas plasmáticas y presión osmótica', src=['VB 2.1 Proteínas plasmáticas'], tipo='der', c1=AZUL_M, c2=BLANCO)
    tej = s.shape(0.3, 1.2, 8.5, 5.8, 'roundRect', ('a', 'FAD7A0', 45), ('B9770E', 1.25, 'dash'), False, name='Intersticio', adj={'adj': 6000})
    tlab = texto(s, 0.5, 6.4, 3.0, 0.4, 'Intersticio (tejidos)', 14, '7E5109', True)
    cap = capilar(s, 0.6, 2.7, 7.9, 1.7, name='!!Capilar')
    albs = [proteina_bola(s, 1.2 + k * 1.15, 3.2 + (k % 2) * 0.35, 0.45, 'F4D03F', 'Alb', name='!!Albúmina %d' % k) for k in range(6)]
    aguas = []
    for k in range(5):
        aguas.append(s.shape(1.6 + k * 1.4, 1.75, 0.38, 0.38, 'ellipse', shade('5DADE2', 0.4, 0.2), ('1B4F72', 1.0), False, 'H_{2}O', 9, F_HEAD, INK,
                             True, 'c', 'm', (0, 0, 0, 0), name='!!Agua %d' % k, fit=False))
    c1 = caja(s, 9.35, 1.2, 3.7, 2.5, 'Las proteínas **atraen el agua**: por su poder osmótico, el agua **permanece dentro de los capilares** en lugar de escaparse hacia los tejidos.',
              BLANCO, 15, head='Mecanismo', name='Mecanismo osmótico')
    c2 = caja(s, 9.35, 4.0, 3.7, 3.0, 'Si un paciente **pierde proteínas** (síndrome nefrótico, desnutrición), la capacidad osmótica **disminuye** y el agua escapa hacia los tejidos → **edema**.',
              ROJO, 15, head='Edema', headfill=AMA2, name='Edema')
    s.step(fade(tej), fade(tlab, after=True), fade(cap, after=True))
    s.step(*[zoom(a, after=(k > 0), delay=0) for k, a in enumerate(albs)])
    s.step(*[fade(a, after=(k == 0)) for k, a in enumerate(aguas)])
    s.step(*[path(a, 0, 1.75, after=(k == 0), dur=900) for k, a in enumerate(aguas)], fade(c1, after=True))
    s.step(*[out(a, after=(k == 0)) for k, a in enumerate(albs[1::2])], *[path(a, 0, 1.6 if k % 2 else 3.3, after=(k == 0), dur=900) for k, a in enumerate(aguas)],
           fade(c2, after=True))
    s.note('Primero el agua es retenida en la luz capilar por las proteínas; al disminuir las proteínas, el agua migra al intersticio (edema).')


def proteinas(D):
    s = nueva(D, 1, 'Las tres proteínas plasmáticas más importantes', src=['VB 2.1 Proteínas plasmáticas'], tipo='bandas', c1=CELESTE, c2=CREMA)
    # albúmina transportadora
    g1 = s.group_start('!!Albúmina')
    enzima_globular(s, 0.7, 1.4, 2.2, 1.9, 'F4D03F', 'Albúmina', 'Albúmina forma', size=16, seed=4)
    for k, (tx, c) in enumerate((('fármaco', 'AF7AC5'), ('toxina', '5D6D7E'), ('metabolito', 'E67E22'))):
        ficha(s, 0.35 + k * 1.05, 3.45, tx, c, w=1.0, h=0.34, size=11, name='Carga ' + tx)
    s.group_end()
    c1 = caja(s, 3.55, 1.3, 6.4, 1.7, '**≈ 50 % de las proteínas totales**: la más abundante. Función principal: **transportadora (carrier)** de metabolitos, fármacos y toxinas.',
              AMA, 16, head='Albúmina', name='Caja albúmina')
    # anticuerpo
    g2 = s.group_start('!!Globulinas')
    s.arrow([(1.8, 5.0), (1.8, 4.3)], '2E86C1', 9, tail=None)
    s.arrow([(1.8, 4.3), (1.15, 3.75)], '2E86C1', 9, tail=None)
    s.arrow([(1.8, 4.3), (2.45, 3.75)], '2E86C1', 9, tail=None)
    s.group_end()
    c2 = caja(s, 3.55, 3.35, 6.4, 1.6, 'Clases **alfa, beta y gamma**. Las **gamma-globulinas son los anticuerpos** (inmunoglobulinas), fundamentales para el sistema inmune.',
              CELESTE, 16, head='Globulinas', name='Caja globulinas')
    g3 = s.group_start('!!Fibrinógeno')
    for k in range(6):
        s.arrow([(0.5 + k * 0.45, 5.4), (0.9 + k * 0.45, 6.8)], 'C0392B', 2.25, tail=None)
        s.arrow([(0.4, 5.6 + k * 0.22), (3.2, 5.9 + k * 0.18)], 'C0392B', 2.25, tail=None)
    s.group_end()
    c3 = caja(s, 3.55, 5.3, 6.4, 1.75, 'Principal proteína de la **coagulación**: se convierte en **fibrina** durante la formación del coágulo. Presente en el **plasma**, ausente en el **suero**.',
              ROSA, 16, head='Fibrinógeno', name='Caja fibrinógeno')
    m = molecula3d(s, 10.5, 1.4, 2.5, 'aa', name='Aminoácido deco')
    pr = caja(s, 10.4, 4.3, 2.75, 2.75, 'Las tres sostienen la **presión osmótica** del plasma.', BLANCO, 16, name='Síntesis proteínas')
    s.step(fade(g1), fade(c1, after=True))
    s.step(fade(g2), fade(c2, after=True))
    s.step(wipe(g3, 'l'), fade(c3, after=True))
    s.step(fade(m), fade(pr, after=True))


def eritrocito_s(D):
    s = nueva(D, 1, 'Eritrocito: disco bicóncavo sin núcleo', src=['VB 2.2 A Glóbulos rojos'], tipo='der', c1=ROJO, c2=ROSA)
    e = eritrocito(s, 0.6, 1.25, 3.3, name='!!Eritrocito')
    p = eritrocito_perfil(s, 0.5, 4.9, 3.6, name='!!Eritrocito perfil')
    lp = texto(s, 0.5, 6.35, 3.6, 0.5, 'Corte: ancho en los bordes, fino en el centro', 13, '6E1A12', True, 'c')
    hb = hemoglobina(s, 4.55, 1.35, 2.4, name='!!Hemoglobina')
    hbl = caja(s, 4.3, 3.95, 4.4, 1.45, '**Hemoglobina**: 4 cadenas de globina + 4 grupos **hemo**; cada hemo tiene **un átomo de hierro** que une O_{2}.', BLANCO, 15,
               name='Rótulo hemoglobina')
    o2 = ficha(s, 7.2, 1.5, 'O_{2}', '5DADE2', w=0.8, name='!!O2')
    co2 = ficha(s, 7.2, 2.6, 'CO_{2}', '95A5A6', w=0.9, name='!!CO2')
    fun = caja(s, 4.3, 5.65, 4.4, 1.4, 'Transporta **O_{2} de los pulmones a los tejidos** y **CO_{2} de los tejidos a los pulmones**.', AMA, 15, name='Función')
    c = caja(s, 9.35, 1.2, 3.7, 2.6, '- Componente celular **más abundante**\n- **Anucleado** (solo sus precursores, los eritroblastos, tienen núcleo)\n- Molécula principal: **hemoglobina**',
             BLANCO, 15, head='Características', name='Características GR')
    v = caja(s, 9.35, 4.15, 3.7, 1.5, '**4,5 – 6 millones / mm^{3}**', AMA, 20, head='Valor de referencia', anchor='m', name='VR GR')
    m = molecula3d(s, 10.4, 5.75, 1.5, 'hemo', name='Grupo hemo deco')
    s.step(fade(e), fade(p, after=True), fade(lp, after=True))
    s.step(zoom(hb), fade(hbl, after=True))
    s.step(fade(o2), path(o2, -1.6, 0.4, after=True), fade(co2), path(co2, -1.4, -0.4, after=True))
    s.step(fade(fun))
    s.step(fade(c), fade(v, after=True), fade(m, after=True))


def deformabilidad(D):
    s = nueva(D, 1, 'Membrana eritrocitaria: flexibilidad y hemólisis', src=['VB 2.2 A Membrana plasmática'], tipo='izq', c1=ROSA, c2=BLANCO)
    cap = s.group_start('!!Capilar estrecho')
    s.free(0.3, 1.5, 12.7, 2.1, 'M 0 0 L 380 0 C 450 0 470 330 540 330 L 760 330 C 830 330 850 0 920 0 L 1000 0 L 1000 1000 L 920 1000 C 850 1000 830 670 760 670 L 540 670 C 470 670 450 1000 380 1000 L 0 1000 Z',
           ('lin', [(0, 'F5B7B1'), (50, 'FDEDEC'), (100, 'F5B7B1')], 90), ('922B21', 2.0))
    s.group_end()
    g = eritrocito_perfil(s, 0.7, 2.15, 1.9, name='!!Eritrocito sano')
    lab1 = caja(s, 0.4, 4.0, 6.0, 1.6, 'Membrana **versátil y flexible**: el eritrocito se **deforma** para atravesar capilares más estrechos que él y luego **recupera su forma**.',
                'EAF5EA', 16, head='Membrana sana', name='Membrana sana')
    g2 = eritrocito_perfil(s, 0.7, 2.15, 1.9, name='!!Eritrocito dañado')
    frag = s.group_start('Fragmentos')
    for k in range(5):
        s.shape(5.9 + k * 0.32, 2.2 + (k % 2) * 0.55, 0.3, 0.22, 'ellipse', 'C0392B', ('6E1A12', 0.75), False)
    s.group_end()
    lab2 = caja(s, 6.8, 4.0, 6.2, 1.6, 'Si la membrana **se deteriora**, el glóbulo rojo **se rompe** al intentar pasar por los capilares → **hemólisis**.',
                ROJO, 16, head='Membrana deteriorada', headfill=AMA2, name='Membrana dañada')
    p = perla(s, 0.4, 5.85, 12.6, 1.2, 'La **membrana plasmática** es el elemento más importante del glóbulo rojo: de ella depende su supervivencia en la microcirculación.', 16)
    s.step(fade(cap), fade(g, after=True))
    s.step(path(g, 10.0, 0, dur=1200, pts=[(4.2, 0), (5.6, 0)]), fade(lab1, after=True))
    s.step(fade(g2), path(g2, 4.6, 0, after=True, dur=900), out(g2, after=True), fade(frag, after=True), fade(lab2, after=True))
    s.step(fade(p))


def leucocitos(D):
    s = nueva(D, 1, 'Leucocitos: el componente celular inmunológico', src=['VB 2.2 B Leucocitos'], tipo='bandas', c1=LAVANDA, c2=CELESTE)
    tipos = [('neutrofilo', 'Neutrófilo', 'pH neutro · bacterias'), ('eosinofilo', 'Eosinófilo', 'pH ácido · parásitos'),
             ('basofilo', 'Basófilo', 'pH básico · inflamación'), ('linfocito', 'Linfocito', 'virus · fabrica anticuerpos'),
             ('monocito', 'Monocito', 'fagocita patógenos y detritos')]
    ids = []
    for i, (k, n, d) in enumerate(tipos):
        x = 0.45 + i * 2.5
        g = s.group_start('!!' + n)
        leucocito(s, x + 0.35, 1.5, 1.6, k, name='Célula ' + n)
        rotulo(s, x + 0.1, 3.25, n, NAVY, 15, w=2.2)
        texto(s, x + 0.05, 3.8, 2.3, 0.75, d, 14.5, INK, False, 'c')
        s.group_end(); ids.append(g)
    br1 = caja(s, 0.45, 4.75, 7.2, 1.25, '**Granulocitos (polimorfonucleares)**: gránulos visibles y núcleos de formas variadas; se nombran por su **afinidad tintorial**.',
               CREMA, 15, name='Granulocitos')
    br2 = caja(s, 7.85, 4.75, 5.0, 1.25, '**Mononucleares (agranulares)**: linfocitos y monocitos.', 'EAF5EA', 15, name='Mononucleares')
    v = caja(s, 0.45, 6.15, 12.4, 0.9, '**4.000 – 11.000 leucocitos / mm^{3}** · hay unas **100 veces menos** leucocitos que eritrocitos.', AMA, 17, anchor='m',
             name='VR leucocitos')
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids[:3])], fade(br1, after=True))
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids[3:])], fade(br2, after=True))
    s.step(fade(v))


def plaquetas(D):
    s = nueva(D, 1, 'Plaquetas: fragmentos de megacariocito', src=['VB 2.2 C Plaquetas'], tipo='der', c1=VERDE_CL, c2=BLANCO)
    mo = medula_osea(s, 0.3, 1.2, 4.2, 3.0, name='!!MedulaOsea', celulas=8)
    mk = megacariocito(s, 1.3, 1.75, 1.9, name='!!Megacariocito')
    pls = [plaqueta(s, 3.0 + k * 0.05, 2.4 + (k % 3) * 0.3, 0.42, name='!!Plaqueta %d' % k) for k in range(5)]
    l1 = caja(s, 0.3, 4.5, 4.2, 1.2, 'No son células: son **fragmentos del citoplasma** del megacariocito, que emite seudópodos que se fragmentan.', CREMA, 14,
              name='Origen plaquetas')
    vas = s.shape(5.0, 1.3, 3.8, 3.9, 'roundRect', ('lin', [(0, 'F5B7B1'), (100, 'FADBD8')], 90), ('922B21', 2.0), False, name='!!Vaso lesionado', adj={'adj': 8000})
    les = s.shape(6.4, 4.6, 1.0, 0.6, 'triangle', 'FFFFFF', ('922B21', 2.0), False, name='Lesión vascular')
    mesh = s.group_start('Malla de fibrina')
    for k in range(7):
        s.arrow([(5.9 + k * 0.25, 3.7), (6.2 + k * 0.2, 4.8)], 'C0392B', 1.75, tail=None)
        s.arrow([(5.8, 3.9 + k * 0.13), (7.8, 4.0 + k * 0.12)], 'C0392B', 1.75, tail=None)
    s.group_end()
    l2 = caja(s, 5.0, 5.4, 3.8, 1.65, 'Lesión vascular → plaquetas **activadas** (seudópodos) → malla plaquetaria + **fibrina** → **tapón plaquetario**.', ROSA, 14,
              name='Hemostasia')
    c = caja(s, 9.35, 1.2, 3.7, 2.4, 'Función principal: **hemostasia y coagulación**.', BLANCO, 17, head='Función', anchor='m', name='Función plaquetas')
    v = caja(s, 9.35, 3.95, 3.7, 1.6, '**150.000 – 400.000 / mm^{3}**', AMA, 19, head='Valor de referencia', anchor='m', name='VR plaquetas')
    s.step(fade(mo), fade(mk, after=True))
    s.step(*[path(p, 3.0 - k * 0.05 + (k % 2) * 0.3, 1.4 + (k % 3) * 0.15, after=(k > 0), dur=900) for k, p in enumerate(pls)], fade(l1, after=True))
    s.step(fade(vas), fade(les, after=True))
    s.step(wipe(mesh, 't'), fade(l2, after=True))
    s.step(fade(c), fade(v, after=True))


def abundancia(D):
    s = nueva(D, 1, 'Orden de abundancia celular en la sangre', src=['VB 2.2 Orden de abundancia', 'VB Anexo Valores de referencia'], tipo='izq', c1=CREMA, c2=BLANCO)
    data = [('Glóbulos rojos', 'millones / mm^{3}', '4,5 – 6 millones', ROJO, 3, 'gr'), ('Plaquetas', 'cientos de miles / mm^{3}', '150.000 – 400.000', '8E44AD', 2, 'pl'),
            ('Leucocitos', 'miles / mm^{3}', '4.000 – 11.000', '2E86C1', 1, 'lc')]
    ids = []
    for i, (n, u, v, col, lvl, k) in enumerate(data):
        y = 1.3 + i * 1.95
        g = s.group_start('Fila ' + n)
        for j in range(lvl * 4):
            xx = 0.5 + (j % 6) * 0.62; yy = y + (j // 6) * 0.62
            if k == 'gr':
                eritrocito(s, xx, yy, 0.55, name='GR %d' % j)
            elif k == 'pl':
                plaqueta(s, xx, yy + 0.1, 0.52, name='Pl %d' % j)
            else:
                leucocito(s, xx, yy, 0.55, 'neutrofilo', name='Lc %d' % j)
        caja(s, 4.6, y, 4.4, 1.6, '**%s**\n%s' % (n, u), BLANCO, 18, anchor='m')
        rotulo(s, 9.3, y + 0.5, v, col, 18, w=3.7, h=0.65)
        s.group_end(); ids.append(g)
    sig = s.group_start('Desigualdades')
    texto(s, 10.6, 2.95, 1.2, 0.5, '>', 36, INK, True, 'c', 'm')
    texto(s, 10.6, 4.9, 1.2, 0.5, '>', 36, INK, True, 'c', 'm')
    s.group_end()
    for g in ids:
        s.step(fade(g))
    s.step(zoom(sig))


# ---------------------------------------------------------------- unidades de medida
def unidades_por_que(D):
    s = nueva(D, 1, 'Unidades estandarizadas: un idioma común', src=['VB 3 Unidades de medida'], tipo='der', c1=AZUL_M, c2=BLANCO)
    labs = []
    for i, (x, y, n) in enumerate(((0.7, 1.5, 'Laboratorio A'), (5.4, 1.5, 'Laboratorio B'), (3.05, 4.3, 'Laboratorio C'))):
        g = s.group_start('!!' + n)
        s.shape(x, y, 2.9, 1.9, 'roundRect', BLANCO, (INK, 1.75), SH_I, adj={'adj': 10000})
        s.shape(x + 0.4, y - 0.5, 2.1, 0.6, 'triangle', NAVY, (INK, 1.5), False)
        tubo(s, x + 0.25, y + 0.35, 0.32, 1.25, [(0.5, 'B3261E', 'r%d' % i), (0.3, 'F9E79F', 'p%d' % i)], name='Tubo ' + n)
        texto(s, x + 0.75, y + 0.45, 2.05, 1.0, '**%s**\nglucosa: 90 mg/dL' % n, 14)
        labs.append(s.group_end())
    flech = s.group_start('Red de comparación')
    s.arrow([(3.65, 2.45), (5.35, 2.45)], ACT, 3, head='triangle')
    s.arrow([(2.2, 3.45), (3.5, 4.25)], ACT, 3, head='triangle')
    s.arrow([(6.8, 3.45), (5.6, 4.25)], ACT, 3, head='triangle')
    s.group_end()
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Las unidades estandarizadas permiten **comparar resultados entre laboratorios, regiones y países**, evitando errores diagnósticos.',
             BLANCO, 15.5, head='Por qué', name='Por qué unidades')
    c2 = caja(s, 9.35, 4.7, 3.7, 2.35, 'Facilitan la construcción de una **red global de datos bioquímicos**.', AMA, 16, name='Red global')
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(labs)])
    s.step(wipe(flech, 'l'), fade(c, after=True))
    s.step(fade(c2))


def masa_molar(D):
    s = nueva(D, 1, 'Concentraciones de masa y concentraciones molares', src=['VB 3.1 Concentraciones de masa', 'VB 3.2 Concentraciones molares'],
              tipo='bandas', c1=CELESTE, c2=CREMA)
    gA = s.group_start('Columna masa')
    manuscrito(s, 0.4, 1.15, 6.0, 0.6, 'Masa / volumen', 24, TBLUE, 'l')
    rows = [['Unidad', 'Uso', 'Ejemplos del material'], ['mg/dL', 'La más usada', 'Glucosa, colesterol'], ['g/dL', 'Sustancias en mayor concentración', 'Proteínas totales, hemoglobina'],
            ['µg/mL', 'Cantidades muy pequeñas', '—']]
    tabla_filas(s, 0.4, 1.85, [1.3, 2.6, 2.2], rows, rowh=0.55, size=14.5, name='Tabla masa')
    s.group_end()
    gB = s.group_start('Columna molar')
    manuscrito(s, 6.75, 1.15, 6.0, 0.6, 'Moles / volumen', 24, TBLUE, 'l')
    rows = [['Unidad', 'Uso', 'Ejemplos del material'], ['mmol/L', 'Analitos en mayor cantidad', 'Sodio, potasio'], ['µmol/L', 'Analitos en pequeña cantidad', 'Creatinina'],
            ['nmol/L', 'Cantidades muy pequeñas', '—']]
    tabla_filas(s, 6.75, 1.85, [1.3, 2.6, 2.2], rows, rowh=0.55, size=14.5, name='Tabla molar')
    s.group_end()
    mol_ = caja(s, 6.75, 4.6, 6.1, 1.0, '1 mol = **6,02 × 10^{23}** partículas', AMA, 20, anchor='m', align='c', name='Mol')
    esq = s.group_start('Relación masa-mol')
    caja(s, 0.4, 4.6, 6.1, 2.45, 'Una **concentración de masa** expresa cuántos gramos (o sus fracciones) hay por volumen; una **concentración molar**, cuántas partículas (moles). '
         'La elección depende de la magnitud del analito y de la convención del laboratorio.', BLANCO, 15)
    s.group_end()
    m = molecula3d(s, 7.4, 5.65, 1.4, 'urea', name='Urea deco')
    m2 = molecula3d(s, 10.9, 5.6, 1.5, 'glucosa', name='Glucosa deco')
    s.step(fade(gA))
    s.step(fade(gB))
    s.step(zoom(mol_), fade(m, after=True), fade(m2, after=True))
    s.step(fade(esq))


def ui_enzimas(D):
    s = nueva(D, 1, 'Unidades Internacionales: se mide una velocidad', src=['VB 3.3 Unidades Internacionales'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    enz_ = enzima_globular(s, 2.6, 2.0, 2.4, 2.1, 'E59866', 'Enzima', '!!Enzima UI', size=18, seed=7)
    subs = [ficha(s, 0.5, 1.6 + k * 0.8, 'S', 'F5B041', w=0.55, name='!!Sustrato %d' % k) for k in range(4)]
    prods = [ficha(s, 6.3, 1.6 + k * 0.8, 'P', '58D68D', w=0.55, name='!!Producto %d' % k) for k in range(4)]
    clk = clock(s, 6.9, 4.7, 1.3, hours=2, name='Reloj 1 minuto')
    lbl = rotulo(s, 6.6, 6.1, '1 minuto', NAVY, 15, w=1.9)
    defi = caja(s, 0.4, 4.6, 5.9, 2.45, 'Las enzimas transforman sustrato en producto: lo que se mide **no es una concentración sino una velocidad de reacción**.\n'
                '**1 UI** = cantidad de enzima que cataliza la transformación de **1 µmol de sustrato en 1 minuto**.', AMA, 15.5, name='Definición UI')
    c = caja(s, 9.35, 1.2, 3.7, 2.2, 'Las enzimas se informan en **UI/L** (actividad catalítica por litro).', BLANCO, 16, head='Regla del material', name='Regla UI')
    r = rigor(s, 9.35, 3.7, 3.7, 3.35, 'UI/L identifica **actividad enzimática**, pero el símbolo «UI» no es exclusivo de las enzimas: algunas hormonas y vitaminas se expresan en '
              'UI por convención biológica. En el SI la actividad se expresa en **katal** (mol/s).', 13)
    s.step(fade(enz_))
    s.step(*[fade(x_, after=(k > 0)) for k, x_ in enumerate(subs)])
    s.step(*[path(x_, 2.6 - 0.0, 0.0 + (1.2 - k * 0.8) * 0.3, after=(k > 0), dur=700) for k, x_ in enumerate(subs)],
           *[out(x_, after=(k == 0)) for k, x_ in enumerate(subs)], *[fade(p, after=(k == 0)) for k, p in enumerate(prods)], fade(clk, after=True), fade(lbl))
    s.step(fade(defi))
    s.step(fade(c))
    s.step(fade(r))


def triada(D):
    s = nueva(D, 1, 'Analito, magnitud y unidad', src=['VB 3 Unidades de medida', 'VB 3.1 Concentraciones de masa', 'VB 3.2 Concentraciones molares'],
              tipo='izq', c1=CREMA, c2=BLANCO)
    tri = s.group_start('!!Tríada')
    for (x, y, t, f) in ((1.5, 1.3, 'ANALITO\n¿qué se mide?', 'F5B041'), (0.3, 4.3, 'MAGNITUD\n¿qué propiedad?', '85C1E9'), (2.8, 4.3, 'UNIDAD\n¿en qué escala?', '82E0AA')):
        s.shape(x, y, 1.9, 1.9, 'ellipse', shade(f, 0.4, 0.2), (INK, 1.75), SH_I, t, 13.5, F_HEAD, INK, True, 'c', 'm', (0.08, 0, 0.08, 0), minsize=10)
    s.arrow([(2.0, 3.25), (1.5, 4.25)], INK, 2.5, head='triangle')
    s.arrow([(3.0, 3.25), (3.6, 4.25)], INK, 2.5, head='triangle')
    s.arrow([(2.25, 5.25), (2.75, 5.25)], INK, 2.5, head='triangle')
    s.group_end()
    rows = [['Analito', 'Magnitud', 'Unidad'], ['Glucosa', 'Concentración de masa', 'mg/dL'], ['Hemoglobina', 'Concentración de masa', 'g/dL'],
            ['Sodio / potasio', 'Concentración molar', 'mmol/L'], ['Creatinina', 'Concentración molar', 'µmol/L'], ['GPT, CK, LDH', 'Actividad catalítica', 'UI/L'],
            ['Eritrocitos, plaquetas', 'Recuento celular', 'por mm^{3}']]
    ids, H = tabla_filas(s, 5.1, 1.2, [2.6, 3.4, 1.9], rows, rowh=0.62, size=16, name='Tabla tríada')
    r = rigor(s, 5.1, 1.35 + H, 7.9, 6.95 - (1.35 + H), 'Algunos analitos pueden informarse en más de una unidad (p. ej. masa o molar): la unidad **no define por sí sola** el tipo de analito; siempre se lee junto con el nombre del analito.', 13.5)
    s.step(fade(tri))
    for k, rr in enumerate(ids):
        s.step(fade(rr)) if k < 2 else s.step(fade(rr))
    s.step(fade(r))


def liquidos(D):
    s = nueva(D, 1, 'Líquidos biológicos utilizados en el laboratorio', src=['VB 4 Líquidos biológicos'], tipo='bandas', c1=CELESTE, c2=CREMA)
    h = human(s, 4.9, 1.05, 6.0, name='!!Organismo')
    izq = [('Líquido cefalorraquídeo (LCR)', 1.3), ('Saliva · lágrimas · humor vítreo', 2.05), ('Líquido pleural (pulmones)', 2.8), ('Líquido pericárdico (corazón)', 3.55),
           ('Líquido gástrico', 4.3), ('Líquido ascítico (abdomen)', 5.05)]
    der = [('Sangre (la más estudiada)', 1.3), ('Orina', 2.05), ('Líquido sinovial (articulaciones)', 2.8), ('Líquido periprotésico', 3.55), ('Sudor · semen · materia fecal', 4.3),
           ('Líquido amniótico', 5.05)]
    ids = []
    for k, (t, y) in enumerate(izq):
        g = s.group_start('Líquido izq %d' % k)
        rotulo(s, 0.35, y, t, BLANCO if k else AMA, 14, w=4.2, h=0.55)
        s.arrow([(4.6, y + 0.27), (6.15, 1.6 + k * 0.62)], '5D6D7E', 1.5)
        ids.append(s.group_end())
    for k, (t, y) in enumerate(der):
        g = s.group_start('Líquido der %d' % k)
        rotulo(s, 8.75, y, t, AMA if k == 0 else BLANCO, 14, w=4.2, h=0.55)
        s.arrow([(8.7, y + 0.27), (7.2, 1.6 + k * 0.62)], '5D6D7E', 1.5)
        ids.append(s.group_end())
    c = caja(s, 0.35, 5.95, 12.6, 1.1, 'Cada muestra tiene **su propia técnica de obtención**; la sangre es el componente más estudiado en bioquímica clínica.', AMA, 16, anchor='m',
             name='Nota líquidos')
    s.step(fade(h))
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids[:6])])
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids[6:])])
    s.step(fade(c))


def build(D):
    divisor_u1(D)
    definicion(D)
    familias(D)
    metabolitos(D)
    electrolitos(D)
    enzimas(D)
    hormonas(D)
    utilidad(D)
    sangre(D)
    plasma(D)
    osmotica(D)
    proteinas(D)
    eritrocito_s(D)
    deformabilidad(D)
    leucocitos(D)
    plaquetas(D)
    abundancia(D)
    unidades_por_que(D)
    masa_molar(D)
    ui_enzimas(D)
    triada(D)
    liquidos(D)
