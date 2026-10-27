# -*- coding: utf-8 -*-
from base import *


def cover(D):
    s = D.new(PEACH); s.unit = 0
    # decoración en esquinas (eritrocitos, mitocondrias, adipocitos, fibras) como en la serie
    for i, (x, y, d) in enumerate(((-0.25, -0.2, 0.9), (0.55, 0.15, 0.6), (0.2, 0.75, 0.55), (1.1, -0.15, 0.5))):
        rbc(s, x, y, d, name='Deco eritrocito %d' % i)
    mito(s, 1.5, 0.45, 0.9, rot=20, name='Deco mitocondria')
    muscle_fiber(s, -0.4, 6.35, 3.2, 0.5, name='Deco fibra 1')
    muscle_fiber(s, -0.2, 6.85, 3.6, 0.5, name='Deco fibra 2')
    adipocyte_white(s, 2.9, 6.55, 1.2, name='Deco adipocito')
    s.text(0.6, 1.25, 7.6, 0.45, 'FISIOLOGÍA · BIOQUÍMICA · ENZIMAS · HORMONAS', 16, F_HEAD, '7A3B12', True, 'l', 'm')
    big_title(s, 0.5, 1.75, 7.8, 2.3, 'INTEGRACIÓN\nMETABÓLICA', 64, align='l')
    s.text(0.6, 4.15, 7.4, 1.0, 'Del estado alimentado a la inanición y la enfermedad', 26, F_HEAD, INK, True, 'l', 't')
    chip(s, 0.6, 5.2, 'Metabolismo interorgánico · Fisiopatología', TAG, 16, h=0.5, shadow=SHD, name='Subtítulo')
    # organismo con órganos (inicio de la secuencia Morph 1)
    human(s, 8.6, 0.55, 6.6, name='!!Organismo')
    brain(s, 10.05, 0.72, 0.6, name='!!Cerebro')
    liver(s, 9.85, 2.45, 0.85, name='!!Hígado')
    pancreas(s, 10.55, 2.85, 0.55, name='!!Páncreas')
    kidney(s, 10.85, 2.55, 0.26, name='!!Riñón')
    intestine(s, 10.1, 3.05, 0.75, name='!!Intestino')
    muscle(s, 9.75, 4.25, 0.9, name='!!Músculo', fibers=2)
    adipocyte_white(s, 11.0, 3.55, 0.45, name='!!Adipocito')
    heart(s, 10.45, 1.85, 0.38, name='!!Corazón')
    s.note('Portada. La clase recorre cómo un aporte discontinuo de alimentos se transforma en una provisión continua de ATP '
           'y cómo se coordinan intestino, hígado, tejido adiposo, músculo, cerebro, riñón y sangre en el estado alimentado, '
           'el ayuno de duración creciente y diversas situaciones patológicas.\n'
           'Estructura: seis unidades (fundamentos y estado alimentado; ayuno y ciclos interorgánicos; lípidos, colesterol y control '
           'génico; nitrógeno, riñón y homeostasis energética; integración en patología; casos clínicos y sistematización).')
    return s


def index(D):
    s = D.new(PEACH); s.unit = 0
    title(s, 'Recorrido de la clase', 'ÍNDICE VISUAL')
    units = [
        ('I', 'FUNDAMENTOS Y ESTADO ALIMENTADO', 'Alimentación, nutrición y metabolismo · ciclo alimentación–ayuno · insulina y glucagón · destino posprandial de nutrientes', PEACH, 'pan'),
        ('II', 'AYUNO Y CICLOS INTERORGÁNICOS', 'Glucogenólisis · gluconeogénesis · Cori y glucosa–alanina · astrocito–neurona · reservas a 8–12 h, 24–48 h y >3 días', 'F6B8AF', 'liv'),
        ('III', 'LÍPIDOS, COLESTEROL Y CONTROL', 'Malonil-CoA · β-oxidación · lipoproteínas · AMPK · colesterol · cetogénesis · CREB/FOXO1/ChREBP/SREBP · estrés', YELBG, 'adi'),
        ('IV', 'NITRÓGENO, RIÑÓN Y HOMEOSTASIS', 'Zonación hepática · ciclo de la urea · glutamina · riñón · AMP desaminasa · tejido adiposo · hipotálamo', BLUEBG, 'kid'),
        ('V', 'INTEGRACIÓN EN PATOLOGÍA', 'Insuficiencia hepática · fructosa · CPT1/carnitina · MCT · aterogénesis · hipertrigliceridemia · encefalopatía · hiperuricemia', 'F8C1C8', 'art'),
        ('VI', 'CASOS CLÍNICOS Y SISTEMATIZACIÓN', 'Seis casos integradores · enzimas reguladoras · comparación de estados · errores frecuentes · mapa final', CREAMBG, 'per'),
    ]
    ids = []
    for i, (r, t, sub, col, art) in enumerate(units):
        cx = 0.45 + (i % 3) * 4.2; cy = 1.15 + (i // 3) * 3.05
        g = s.group_start('Unidad %s' % r)
        s.shape(cx, cy, 3.95, 2.8, 'rect', col, (INK, 1.5), SHD)
        badge(s, cx + 0.15, cy + 0.15, r, 0.62)
        s.text(cx + 0.9, cy + 0.12, 2.95, 0.7, t, 16, F_HEAD, INK, True, 'l', 'm')
        s.text(cx + 0.18, cy + 0.9, 2.35, 1.8, sub, 12.5, F_BODY, '3A2A20', False, 'l', 't')
        if art == 'pan':
            pancreas(s, cx + 2.55, cy + 1.25, 1.3, name='Ícono páncreas')
            mol(s, cx + 2.9, cy + 1.95, 'glc', d=0.42)
            mol(s, cx + 3.35, cy + 2.05, 'ins', d=0.42)
        elif art == 'liv':
            liver(s, cx + 2.5, cy + 1.2, 1.35, name='Ícono hígado')
            clock(s, cx + 3.05, cy + 2.0, 0.6, 8)
        elif art == 'adi':
            adipocyte_white(s, cx + 2.55, cy + 1.05, 0.85, name='Ícono adipocito')
            mito(s, cx + 2.9, cy + 2.05, 0.9, name='Ícono mitocondria')
        elif art == 'kid':
            kidney(s, cx + 2.7, cy + 0.95, 0.6, name='Ícono riñón')
            brain(s, cx + 3.05, cy + 2.05, 0.8, name='Ícono cerebro')
        elif art == 'art':
            heart(s, cx + 2.75, cy + 0.98, 0.75, name='Ícono corazón')
            liver(s, cx + 2.6, cy + 1.95, 1.15, name='Ícono hígado 2')
        else:
            person(s, cx + 2.75, cy + 0.95, 1.6, name='Ícono paciente')
        ids.append(s.group_end())
    for k, g in enumerate(ids):
        s.step(fade(g)) if k == 0 else s.anim[-1].append(fade(g, after=True, delay=50))
    s.note('Índice visual. Las unidades siguen una lógica fisiológica: primero la abundancia (estado alimentado), luego la carencia '
           'progresiva (ayuno), después los grandes ejes del metabolismo lipídico y nitrogenado, y finalmente su ruptura en la '
           'enfermedad y en casos clínicos. Los 43 temas se distribuyen en estas seis unidades sin omitir contenidos.')
    return s


def general_map(D):
    s = D.new(PEACH); s.unit = 0
    title(s, 'Mapa general: órganos, sangre y combustibles', 'MAPA METABÓLICO')
    ids = organ_map(s)
    # flujos (aparecen por clic)
    A = []
    A.append(arrow_lbl(s, [(1.9, 4.45), (1.9, 4.1)], None, TRN, 3, name='Flecha intestino-sangre'))
    m1 = mol(s, 1.75, 4.0, 'glc', d=0.38, name='Glc intestino')
    m2 = mol(s, 2.2, 4.0, 'aa', d=0.38, name='AA intestino')
    a2 = s.arrow([(2.6, 3.5), (2.6, 3.1)], TRN, 3, name='Flecha sangre-hígado')
    m3 = mol(s, 2.75, 3.0, 'glc', 'Glc', d=0.38, name='Glc hígado')
    a3 = s.arrow([(10.6, 2.85), (10.6, 3.5)], TRN, 3, name='Flecha adiposo-sangre')
    m4 = ag_chain(s, 10.75, 3.0, 0.75, 0.18, name='AG adiposo')
    m5 = mol(s, 11.6, 2.95, 'gly', d=0.38, name='Glicerol')
    a4 = s.arrow([(10.2, 4.1), (10.2, 4.55)], TRN, 3, name='Flecha sangre-músculo')
    m6 = mol(s, 9.55, 4.12, 'lac', d=0.38, name='Lactato')
    m7 = mol(s, 9.98, 4.12, 'ala', d=0.38, name='Alanina')
    a5 = s.arrow([(6.6, 3.5), (6.6, 2.7)], TRN, 3, name='Flecha sangre-cerebro')
    m8 = mol(s, 6.75, 2.95, 'cc', d=0.38, name='Cuerpos cetónicos')
    a6 = s.arrow([(5.6, 4.1), (5.6, 4.5)], TRN, 3, name='Flecha sangre-riñón')
    m9 = mol(s, 4.95, 4.12, 'gln', d=0.38, name='Glutamina')
    m10 = mol(s, 6.25, 4.6, 'urea', d=0.42, name='Urea')
    leg = card(s, 2.95, 5.15, 1.95, 1.95, '[b]Azul[/]: transporte\nGlc · AA · AG · Gli\nLac · Ala · Gln\nCC · Urea', CREAM, 12.5, name='Leyenda mapa')
    s.step(wipe(ids['vessel'], 'l'), fade(ids['vessel_lab'], after=True))
    s.step(wipe(A[0], 'b'), fade(m1, after=True), fade(m2), wipe(a2, 'b', after=True), fade(m3, after=True))
    s.step(wipe(a3, 't'), fade(m4, after=True), fade(m5))
    s.step(wipe(a4, 't'), fade(m6, after=True), fade(m7))
    s.step(wipe(a5, 'b'), fade(m8, after=True))
    s.step(wipe(a6, 't'), fade(m9, after=True), fade(m10), fade(leg, after=True))
    s.note('Mapa general. La integración metabólica consiste en el intercambio continuo de sustratos a través de la sangre: '
           'glucosa y aminoácidos llegan desde el intestino por la vena porta; el hígado almacena, transforma y exporta; el tejido '
           'adiposo libera ácidos grasos y glicerol cuando cae la insulina; el músculo intercambia lactato, alanina y glutamina; el '
           'cerebro consume glucosa y, en ayuno prolongado, cuerpos cetónicos; el riñón filtra urea, produce glucosa y amonio.\n'
           'Clave didáctica: el tejido que usa un combustible determina qué queda disponible para el resto. Distinguir siempre '
           'carbono (glucosa, lactato, glicerol, acetil-CoA, cuerpos cetónicos) de nitrógeno (alanina, glutamina, NH4+, urea).')
    return s


def legend(D):
    s = D.new(PEACH); s.unit = 0
    title(s, 'Código visual de la presentación', 'CÓMO LEER LOS ESQUEMAS')
    y0 = 1.3
    rows = [
        ('act', 'ACTIVACIÓN', 'Flecha o signo verde: la señal estimula una enzima, transportador o vía.'),
        ('inh', 'INHIBICIÓN', 'Trazo rojo terminado en barra perpendicular o signo rojo: freno de la actividad.'),
        ('trn', 'TRANSPORTE', 'Flecha azul: desplazamiento de metabolitos entre compartimentos u órganos.'),
        ('ene', 'INTERMEDIARIOS ENERGÉTICOS', 'Amarillo: ATP, GTP, NADH, FADH_{2}, NADPH y acetil-CoA.'),
        ('enz', 'ENZIMAS', 'Píldora blanca con borde azul oscuro: enzima o complejo enzimático regulador.'),
    ]
    ids = []
    for i, (k, t, d) in enumerate(rows):
        y = y0 + i * 1.08
        g = s.group_start('Código ' + t.lower())
        if k == 'act':
            s.arrow([(0.7, y + 0.35), (2.3, y + 0.35)], ACT, 4); sign(s, 2.45, y + 0.2, '+')
        elif k == 'inh':
            s.inhib([(0.7, y + 0.35), (2.3, y + 0.35)]); sign(s, 2.45, y + 0.2, '−')
        elif k == 'trn':
            s.arrow([(0.7, y + 0.35), (2.3, y + 0.35)], TRN, 4)
        elif k == 'ene':
            mol(s, 0.7, y + 0.12, 'atp', 'ATP', 0.5, w=0.8); mol(s, 1.6, y + 0.12, 'atp', 'NADH', 0.5, w=0.9)
        else:
            enz(s, 0.7, y + 0.18, 'CPT1'); enz(s, 1.5, y + 0.18, 'PFK-1')
        chip(s, 3.0, y + 0.12, t, TAG, 14, h=0.45)
        s.text(3.1 + chipw(t, 14), y + 0.0, 9.1 - (3.1 + chipw(t, 14)), 0.7, d, 14, F_BODY, INK, False, 'l', 'm')
        ids.append(s.group_end())
    # moléculas
    mg = s.group_start('Fichas moleculares')
    s.shape(9.35, 1.25, 3.65, 5.75, 'rect', CREAM, (INK, 1.25), SHD)
    s.text(9.5, 1.32, 3.4, 0.4, 'FICHAS MOLECULARES', 15, F_HEAD, INK, True, 'c', 'm')
    keys = [('glc', 'Glucosa'), ('lac', 'Lactato'), ('ala', 'Alanina'), ('gly', 'Glicerol'), ('cc', 'Cuerpos cetónicos'),
            ('gln', 'Glutamina'), ('nh4', 'Amonio (NH_{4}^{+})'), ('urea', 'Urea'), ('aa', 'Aminoácidos'), ('ins', 'Insulina'), ('gcg', 'Glucagón')]
    for i, (k, t) in enumerate(keys):
        yy = 1.8 + i * 0.41
        mol(s, 9.6, yy, k, d=0.36)
        s.text(10.1, yy - 0.02, 2.8, 0.4, t, 13.5, F_BODY, INK, False, 'l', 'm')
    ag_chain(s, 11.75, 6.38, 0.8, 0.18, name='AG ficha')
    s.text(9.6, 6.3, 2.0, 0.35, 'Ácido graso (AG)', 13.5, F_BODY, INK, False, 'l', 'm')
    s.group_end()
    s.step(*[fade(g, after=(i > 0)) for i, g in enumerate(ids)])
    s.step(fade(mg))
    s.note('Código visual. Se mantiene en todas las diapositivas: verde = activación, rojo = inhibición, azul = transporte, '
           'amarillo = intermediarios energéticos. Las moléculas conservan siempre el mismo color para poder seguirlas entre órganos '
           '(por ejemplo, el lactato es siempre violeta y la glutamina verde azulado). Las enzimas reguladoras aparecen como píldoras '
           'blancas, de modo que el estudiante pueda localizar el paso que "decide" el flujo.')
    return s


def build(D):
    cover(D)
    index(D)
    legend(D)
    general_map(D)
