# -*- coding: utf-8 -*-
"""UNIDAD I (parte 2): suero y plasma (secuencia Morph), sensibilidad, especificidad, valores predictivos,
precisión, exactitud, intervalos de referencia y control de calidad."""
from plantillas import *
from u1 import persona_ico


# ================================================================ SUERO Y PLASMA (Morph)
def fibrina(s, x, y, w, h, name='!!FibrinaB'):
    random.seed(11)
    paths = []
    for k in range(9):
        y0 = random.randint(50, 950); y1 = random.randint(50, 950)
        paths.append('M 60 %d C 300 %d 600 %d 940 %d' % (y0, random.randint(0, 1000), random.randint(0, 1000), y1))
    return s.free(x, y, w, h, [(p, False, True) for p in paths], None, ('F9E79F', 1.5), name=name)


SP_POS = {
    # etapa: (tubo A (x,y,w,h), tubo B, jeringa (x,y,w) o None, brazo (x,y,w) o None, centrífuga (x,y,d) o None)
    1: (None, None, (6.0, 2.15, 3.2), (0.3, 1.5, 6.6), None),
    2: ((4.3, 2.0, 1.1, 4.2), (7.2, 2.0, 1.1, 4.2), (0.9, 1.3, 2.6), (-2.2, 5.6, 3.6), None),
    3: ((4.3, 2.0, 1.1, 4.2), (7.2, 2.0, 1.1, 4.2), (3.55, 1.12, 2.6), None, None),
    4: ((4.3, 2.0, 1.1, 4.2), (7.2, 2.0, 1.1, 4.2), (6.45, 1.12, 2.6), None, None),
    5: ((4.55, 2.75, 0.42, 1.6), (6.45, 2.75, 0.42, 1.6), None, None, (3.95, 2.0, 3.6)),
    6: ((4.3, 2.0, 1.1, 4.2), (7.2, 2.0, 1.1, 4.2), None, None, (0.4, 5.1, 1.5)),
    7: ((2.2, 1.25, 1.5, 5.6), (0.45, 4.7, 0.55, 2.1), None, None, None),
    8: ((0.45, 4.7, 0.55, 2.1), (2.2, 1.25, 1.5, 5.6), None, None, None),
    9: ((1.3, 1.6, 1.0, 4.0), (5.3, 1.6, 1.0, 4.0), None, None, None),
}

SP_TXT = {
    1: 'Obtención de la muestra de sangre',
    2: 'Dos tubos: con y sin anticoagulante',
    3: 'Muestra con anticoagulante: la sangre no coagula',
    4: 'Muestra sin anticoagulante: coagulación espontánea',
    5: 'Centrifugación',
    6: 'Separación de capas',
    7: 'Obtención de plasma',
    8: 'Obtención de suero',
    9: 'Suero y plasma: comparación de componentes',
}


def escena_sp(D, st):
    s = nueva(D, 1, SP_TXT[st], tipo='izq', c1=CELESTE, c2=BLANCO, morph=st > 1,
              src=['VB 5 Suero vs plasma', 'VB 5.1 Obtención'], tw=8.6)
    A, B, J, BR, C = SP_POS[st]
    ids = {}
    if BR:
        ids['brazo'] = brazo(s, BR[0], BR[1], BR[2], name='!!Brazo')
    if C:
        ids['cen'] = centrifuga(s, C[0], C[1], C[2], name='!!Centrifuga')
    if A:
        capA = [] if st < 3 else ([(0.82, 'B3261E', '!!SangreA')] if st < 6 else [(0.42, 'B3261E', '!!SangreA'), (0.05, 'F2F3F4', '!!BuffyA'), (0.35, 'F7DC6F', '!!PlasmaA')])
        ids['A'] = tubo(s, A[0], A[1], A[2], A[3], capA, tapa='8E44AD', name='!!TuboA')
    if B:
        capB = [] if st < 4 else ([(0.82, '9B1C14', '!!SangreB')] if st < 6 else [(0.44, '7B1712', '!!SangreB'), (0.38, 'FCF3CF', '!!SueroB')])
        ids['B'] = tubo(s, B[0], B[1], B[2], B[3], capB, tapa='C0392B', name='!!TuboB')
        if st >= 4:
            fh = B[3] * 0.84 * (0.82 if st < 6 else 0.44)
            ids['fib'] = fibrina(s, B[0] + B[2] * 0.08, B[1] + B[3] * 0.98 - fh, B[2] * 0.84, fh * 0.92)
    if J:
        ids['jer'] = jeringa(s, J[0], J[1], J[2], name='!!Jeringa', lleno=0.75 if st < 4 else 0.3)
    return s, ids


def suero_plasma(D):
    ini = len(D.slides) + 1
    # 1 extracción
    s, i = escena_sp(D, 1)
    c = caja(s, 9.35, 1.15, 3.7, 2.6, 'La muestra se obtiene en tubos que se procesan de forma distinta según se busque **suero** o **plasma**.', AMA, 16,
             head='Punto de partida', name='Caja etapa 1')
    c2 = caja(s, 9.35, 4.0, 3.7, 3.05, 'Concepto clave para toda la carrera: conocer la diferencia entre suero y plasma y **saber cuándo usar cada uno**.', BLANCO, 15,
              name='Caja concepto')
    ruta = caja(s, 0.4, 5.05, 8.4, 2.0, '**Secuencia**: 1 obtención → 2 tubos → 3 con anticoagulante → 4 sin anticoagulante → 5 centrifugación → 6 capas → 7 plasma → 8 suero → 9 comparación.',
                CREMA, 16, name='Hoja de ruta')
    s.step(fade(i['brazo']), fade(i['jer'], after=True))
    s.step(fade(c))
    s.step(fade(ruta))
    s.step(fade(c2))
    # 2 tubos
    s, i = escena_sp(D, 2)
    la = rotulo(s, 3.65, 6.4, 'CON anticoagulante', '8E44AD', 15, w=2.45, name='Rótulo tubo A')
    lb = rotulo(s, 6.55, 6.4, 'SIN anticoagulante', 'C0392B', 15, w=2.45, name='Rótulo tubo B')
    ac = ficha(s, 5.6, 2.5, 'Anticoagulante', 'D2B4DE', w=1.55, h=0.4, size=12, name='!!Anticoagulante')
    c = caja(s, 9.35, 1.15, 3.7, 3.0, '**Tubo con anticoagulante** → destinado a **plasma**.\n**Tubo sin anticoagulante** → destinado a **suero**.', AMA, 16, head='Dos caminos',
             name='Caja etapa 2')
    s.step(fade(i['A']['vidrio']), fade(la, after=True))
    s.step(fade(i['B']['vidrio']), fade(lb, after=True))
    s.step(zoom(ac), fade(c, after=True))
    # 3 con anticoagulante
    s, i = escena_sp(D, 3)
    ac = ficha(s, 4.7, 2.9, 'Anticoagulante', 'D2B4DE', w=1.55, h=0.4, size=12, name='!!Anticoagulante')
    gota = s.shape(4.75, 1.85, 0.22, 0.3, 'teardrop', 'B3261E', ('6E1A12', 1.0), False, name='Gota A', rot=135)
    c = caja(s, 9.35, 1.15, 3.7, 3.0, 'Se agrega un **anticoagulante** a la sangre **antes de centrifugar**: la muestra **permanece líquida** y conserva los factores de coagulación.',
             'EAF5EA', 15.5, head='Plasma: paso 1', name='Caja etapa 3')
    s.step(fade(gota), path(gota, 0, 1.6, after=True, dur=700), out(gota, after=True), fade(i['A']['!!SangreA'], after=True))
    s.step(fade(c))
    # 4 sin anticoagulante
    s, i = escena_sp(D, 4)
    ac = ficha(s, 4.7, 2.9, 'Anticoagulante', 'D2B4DE', w=1.55, h=0.4, size=12, name='!!Anticoagulante')
    gota = s.shape(7.65, 1.85, 0.22, 0.3, 'teardrop', '9B1C14', ('6E1A12', 1.0), False, name='Gota B', rot=135)
    fl = rotulo(s, 6.55, 6.4, 'fibrinógeno → fibrina', ROSA, 13, w=2.45, name='Rótulo fibrina')
    c = caja(s, 9.35, 1.15, 3.7, 3.4, 'Sin anticoagulante la sangre **coagula espontáneamente**: el fibrinógeno forma **fibrina** y los factores de coagulación **se consumen** en el coágulo.',
             ROSA, 15.5, head='Suero: paso 1', name='Caja etapa 4')
    s.step(fade(gota), path(gota, 0, 1.6, after=True, dur=700), out(gota, after=True), fade(i['B']['!!SangreB'], after=True))
    s.step(wipe(i['fib'], 't'), fade(fl, after=True))
    s.step(fade(c))
    # 5 centrifugación
    s, i = escena_sp(D, 5)
    gi = giro(s, 7.75, 1.4, 1.0, name='Giro rotor')
    c = caja(s, 9.35, 1.15, 3.7, 3.0, 'Ambos tubos se **centrifugan**: la fuerza centrífuga separa los componentes de la suspensión.', AMA, 16, head='Centrifugación',
             name='Caja etapa 5')
    s.step(fade(gi), spin(i['cen'], after=True, dur=1200))
    s.step(fade(c))
    # 6 separación
    s, i = escena_sp(D, 6)
    l1 = rotulo(s, 3.4, 6.4, 'Tubo con anticoagulante', '8E44AD', 13.5, w=2.9, name='Rótulo A6')
    l2 = rotulo(s, 6.3, 6.4, 'Tubo sin anticoagulante', 'C0392B', 13.5, w=2.9, name='Rótulo B6')
    c = caja(s, 9.35, 1.15, 3.7, 3.2, 'Tras la centrifugación cada tubo muestra **capas**: lo que queda arriba es la fase líquida que se envía a analizar.', AMA, 16,
             head='Resultado', name='Caja etapa 6')
    s.step(fade(l1), fade(l2, after=True))
    s.step(pulse(i['A']['!!PlasmaA']), pulse(i['B']['!!SueroB'], after=True), fade(c, after=True))
    # 7 plasma
    s, i = escena_sp(D, 7)
    A = SP_POS[7][0]
    tops = A[1] + A[3] - A[3] * 0.02
    hh = A[3] * 0.84
    yR = tops - hh * 0.42 / 2; yBuf = tops - hh * 0.445; yP = tops - hh * (0.47 + 0.35 / 2)
    lab = []
    for (yy, t, f, nm) in ((yP, '**Plasma** (arriba): todos los componentes líquidos, **incluidos los factores de coagulación**', 'F7DC6F', 'Rótulo plasma'),
                           (yBuf, '**Buffy coat** (medio): glóbulos blancos y plaquetas', 'F2F3F4', 'Rótulo buffy'),
                           (yR, '**Glóbulos rojos** (abajo)', 'F5B7B1', 'Rótulo GR')):
        g = s.group_start(nm)
        s.arrow([(A[0] + A[2] + 0.1, yy), (4.3, yy)], INK, 2)
        caja(s, 4.35, yy - 0.5, 4.5, 1.0, t, f, 15, anchor='m')
        lab.append(s.group_end())
    c = caja(s, 9.35, 1.15, 3.7, 2.7, '**Plasma** = sangre **con anticoagulante** centrifugada.', 'EAF5EA', 17, head='Definición', name='Caja etapa 7')
    for g in lab:
        s.step(fade(g))
    s.step(fade(c))
    # 8 suero
    s, i = escena_sp(D, 8)
    Bp = SP_POS[8][1]
    tops = Bp[1] + Bp[3] - Bp[3] * 0.02
    hh = Bp[3] * 0.84
    yC = tops - hh * 0.44 / 2; yS = tops - hh * (0.44 + 0.38 / 2)
    lab = []
    for (yy, t, f, nm) in ((yS, '**Suero** (arriba): parte líquida **SIN factores de coagulación** (fueron utilizados en la coagulación)', 'FCF3CF', 'Rótulo suero'),
                           (yC, '**Coágulo** (abajo): glóbulos rojos, blancos, plaquetas y factores de coagulación **atrapados**', 'F5B7B1', 'Rótulo coágulo')):
        g = s.group_start(nm)
        s.arrow([(Bp[0] + Bp[2] + 0.1, yy), (4.3, yy)], INK, 2)
        caja(s, 4.35, yy - 0.6, 4.5, 1.2, t, f, 15, anchor='m')
        lab.append(s.group_end())
    c = caja(s, 9.35, 1.15, 3.7, 2.7, '**Suero** = sangre **sin anticoagulante**, coagulada y centrifugada.', ROSA, 17, head='Definición', name='Caja etapa 8')
    for g in lab:
        s.step(fade(g))
    s.step(fade(c))
    # 9 comparación
    s, i = escena_sp(D, 9)
    la = rotulo(s, 0.85, 5.75, 'PLASMA', '8E44AD', 16, w=1.9, name='Rótulo plasma 9')
    lb = rotulo(s, 4.85, 5.75, 'SUERO', 'C0392B', 16, w=1.9, name='Rótulo suero 9')
    chA = s.group_start('Contenido plasma')
    for k, (t, f) in enumerate((('Fibrinógeno: presente', 'EAF5EA'), ('Factores: presentes', 'EAF5EA'))):
        rotulo(s, 2.45, 2.0 + k * 0.7, t, f, 13, w=2.5, name='Plasma comp %d' % k)
    s.group_end()
    chB = s.group_start('Contenido suero')
    for k, (t, f) in enumerate((('Fibrinógeno: ausente', ROSA), ('Factores: ausentes', ROSA))):
        rotulo(s, 6.45, 2.0 + k * 0.7, t, f, 13, w=2.5, name='Suero comp %d' % k)
    s.group_end()
    c = caja(s, 9.35, 1.15, 3.7, 4.2, 'La diferencia esencial: el **plasma conserva el fibrinógeno y los factores de coagulación**; el **suero no**, porque se consumieron al formarse el coágulo.',
             AMA, 16, head='Diferencia clave', name='Caja etapa 9')
    s.step(fade(la), fade(lb, after=True))
    s.step(fade(chA))
    s.step(fade(chB))
    s.step(fade(c))
    registrar_morph(D, ini, len(D.slides), 'Obtención de suero y plasma: extracción → tubos → con/sin anticoagulante → centrifugación → capas → plasma → suero → comparación',
                    ['!!Brazo', '!!Jeringa', '!!TuboA', '!!TuboB', '!!SangreA', '!!SangreB', '!!PlasmaA', '!!BuffyA', '!!SueroB', '!!FibrinaB', '!!Centrifuga', '!!Anticoagulante'],
                    'Desplazamiento de la jeringa hacia cada tubo; llenado de los tubos; los tubos se reducen y entran al rotor; '
                    'la columna de sangre se acorta y aparecen las capas; ampliación alternada del tubo de plasma y del de suero.')


def tabla_sp(D):
    s = nueva(D, 1, 'Suero y plasma: tabla comparativa', src=['VB 5.2 Tabla comparativa'], tipo='der', c1=AMA, c2=BLANCO)
    rows = [['Característica', 'Suero', 'Plasma'], ['Factores de coagulación', 'Ausentes (ya coaguló)', 'Presentes'], ['Fibrinógeno', 'Ausente', 'Presente'],
            ['Obtención', 'Sin anticoagulante', 'Con anticoagulante'], ['Cantidad obtenida', 'Menor', 'Mayor'],
            ['Pureza', 'Más puro (sin alteraciones artificiales)', 'Alterado por el anticoagulante']]
    ids, H = tabla_filas(s, 0.45, 1.3, [2.9, 2.85, 2.85], rows, rowh=0.8, size=17, name='Tabla suero plasma', col_fills=[None, 'FCE4EC', 'EDE7F6'])
    ta = tubo(s, 9.7, 1.3, 0.85, 3.4, [(0.42, 'B3261E', 'Rojos tp'), (0.05, 'F2F3F4', 'Buffy tp'), (0.35, 'F7DC6F', 'Plasma tp')], tapa='8E44AD', name='Tubo plasma tp',
              etiqueta='Plasma', grupo='Tubo plasma (tabla)')
    tb = tubo(s, 11.6, 1.3, 0.85, 3.4, [(0.44, '7B1712', 'Coágulo tp'), (0.38, 'FCF3CF', 'Suero tp')], tapa='C0392B', name='Tubo suero tp', etiqueta='Suero',
              grupo='Tubo suero (tabla)')
    c = caja(s, 9.35, 5.3, 3.7, 1.75, 'Leé la tabla **de arriba hacia abajo**: cada diferencia deriva de **haber coagulado o no**.', BLANCO, 15, name='Lectura tabla')
    s.step(fade(ids[0]), fade(ta, after=True), fade(tb, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))


def cuando_usar(D):
    s = nueva(D, 1, '¿Cuándo usar suero y cuándo plasma?', src=['VB 5.3 Cuándo usar cada uno'], tipo='bandas', c1=ROSA, c2=LAVANDA)
    a = caja(s, 0.45, 1.2, 6.0, 2.6, '- **Hormonas**: los anticoagulantes interfieren con la medición hormonal.\n- **Pruebas serológicas** (antígenos y anticuerpos): el anticoagulante altera su morfología y las técnicas de detección.',
             ROSA, 15.5, head='Suero (obligatorio)', headfill=ROJO, name='Usos suero')
    b = caja(s, 6.85, 1.2, 6.0, 2.6, '- **Coagulación y fibrinógeno**: requieren factores intactos.\n- **Hematología** (recuento de GR, GB y plaquetas).\n- La mayoría de los analitos que no exigen suero.',
             LAVANDA, 15.5, head='Plasma', headfill='8E44AD', name='Usos plasma')
    # interferencias
    g1 = s.group_start('Heparina sódica')
    tubo(s, 0.7, 4.15, 0.55, 2.3, [(0.42, 'B3261E', 'R hep'), (0.35, 'F7DC6F', 'P hep')], tapa='27AE60', name='Tubo heparina')
    for k in range(5):
        s.shape(1.45 + (k % 3) * 0.42, 4.4 + (k // 3) * 0.45, 0.38, 0.38, 'ellipse', shade('2E86C1', 0.4, 0.2), ('1B4F72', 1.0), False, 'Na^{+}', 9, F_HEAD, BLANCO, True,
                'c', 'm', (0, 0, 0, 0), fit=False)
    caja(s, 2.9, 4.15, 3.55, 2.85, 'Si el anticoagulante es **heparina de sodio**, **no se puede medir sodio**: el propio anticoagulante aporta Na^{+}.', BLANCO, 15)
    s.group_end()
    g2 = s.group_start('EDTA')
    tubo(s, 7.1, 4.15, 0.55, 2.3, [(0.42, 'B3261E', 'R edta'), (0.35, 'F7DC6F', 'P edta')], tapa='8E44AD', name='Tubo EDTA')
    ed = s.shape(7.85, 4.45, 1.1, 1.1, 'ellipse', ('a', 'D2B4DE', 70), ('6C3483', 1.5, 'dash'), False, 'EDTA', 12, F_HEAD, INK, True, 'c', 't', (0, 0.08, 0, 0), fit=False)
    s.shape(8.2, 4.85, 0.42, 0.42, 'ellipse', shade('E67E22', 0.4, 0.2), ('873600', 1.0), False, 'Ca^{2+}', 9, F_HEAD, BLANCO, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    caja(s, 9.3, 4.15, 3.55, 2.85, 'El **EDTA secuestra calcio**: si se mide calcio en ese plasma, el resultado aparece **falsamente muy bajo**.', BLANCO, 15)
    s.group_end()
    s.step(fade(a))
    s.step(fade(b))
    s.step(fade(g1))
    s.step(fade(g2))


# ================================================================ SENSIBILIDAD / ESPECIFICIDAD
def grilla(s, x, y, n, cols, fill, name, h=0.55, gap=0.12, marks=None):
    ids = []
    for k in range(n):
        xx = x + (k % cols) * (h * 0.75 + gap); yy = y + (k // cols) * (h + gap)
        ids.append(persona_ico(s, xx, yy, h, fill, name='%s %d' % (name, k + 1)))
    return ids


def sensibilidad(D):
    s = nueva(D, 1, 'Sensibilidad: detectar a quien está enfermo', src=['VB 6.1 Sensibilidad'], tipo='izq', c1=ROSA, c2=BLANCO)
    manuscrito(s, 0.35, 1.05, 4.0, 0.5, 'Personas enfermas', 18, ROJO, 'l', name='Rótulo enfermos')
    enf = grilla(s, 0.45, 1.65, 12, 4, 'E74C3C', 'Enfermo', h=0.95)
    pos = [s.shape(0.45 + (k % 4) * (0.95 * 0.75 + 0.12) + 0.45, 1.65 + (k // 4) * 1.07 - 0.05, 0.36, 0.36, 'ellipse', ACT, (BLANCO, 1.0), False, '+', 14, F_HEAD,
                   BLANCO, True, 'c', 'm', (0, 0, 0, 0), name='Test + %d' % k, fit=False) for k in range(11)]
    fn = s.shape(0.45 + 3 * (0.95 * 0.75 + 0.12) + 0.45, 1.65 + 2 * 1.07 - 0.05, 0.36, 0.36, 'ellipse', '7F8C8D', (BLANCO, 1.0), False, '−', 14, F_HEAD, BLANCO, True,
                 'c', 'm', (0, 0, 0, 0), name='Falso negativo', fit=False)
    fnl = rotulo(s, 1.8, 5.1, 'falso negativo', '7F8C8D', 13, name='Rótulo FN')
    d = caja(s, 5.0, 1.15, 8.0, 1.5, 'Capacidad de un método de **detectar correctamente a los individuos que realmente tienen la enfermedad**: si el paciente está enfermo, la prueba debe dar positivo.',
             AMA, 16, name='Definición S')
    f = caja(s, 5.0, 2.9, 8.0, 1.25, 'Sensibilidad = VP / (VP + FN)', BLANCO, 24, align='c', anchor='m', name='Fórmula S', bold=True)
    fnx = caja(s, 5.0, 4.4, 3.9, 2.65, '**Falso negativo**: paciente **enfermo** cuya prueba dio **negativo**. Una prueba muy sensible **minimiza los falsos negativos**.', ROSA, 15,
               name='FN')
    sc = caja(s, 9.1, 4.4, 3.9, 2.65, 'Se necesita en el **screening (tamizaje)**: si da **negativo**, hay seguridad de que no tiene la enfermedad; el **positivo requiere confirmación**.',
              CELESTE, 15, head='Uso', name='Uso S')
    s.step(*[fade(e, after=(k > 0), dur=200) for k, e in enumerate(enf)])
    s.step(fade(d))
    s.step(*[zoom(p, after=(k > 0), dur=200) for k, p in enumerate(pos)], zoom(fn, after=True), fade(fnl, after=True))
    s.step(fade(f))
    s.step(fade(fnx))
    s.step(fade(sc))
    s.note('Esquema ilustrativo: los íconos no representan datos de un estudio, solo la lógica de verdaderos positivos y falsos negativos.')


def especificidad(D):
    s = nueva(D, 1, 'Especificidad: reconocer a quien está sano', src=['VB 6.2 Especificidad'], tipo='izq', c1='EAF5EA', c2=BLANCO)
    manuscrito(s, 0.35, 1.05, 4.0, 0.5, 'Personas sanas', 18, VERDE_OSC, 'l', name='Rótulo sanos')
    san = grilla(s, 0.45, 1.65, 12, 4, '58D68D', 'Sano', h=0.95)
    neg = [s.shape(0.45 + (k % 4) * (0.95 * 0.75 + 0.12) + 0.45, 1.65 + (k // 4) * 1.07 - 0.05, 0.36, 0.36, 'ellipse', '7F8C8D', (BLANCO, 1.0), False, '−', 14, F_HEAD,
                   BLANCO, True, 'c', 'm', (0, 0, 0, 0), name='Test − %d' % k, fit=False) for k in range(11)]
    fp = s.shape(0.45 + 3 * (0.95 * 0.75 + 0.12) + 0.45, 1.65 + 2 * 1.07 - 0.05, 0.36, 0.36, 'ellipse', ROJO, (BLANCO, 1.0), False, '+', 14, F_HEAD, BLANCO, True,
                 'c', 'm', (0, 0, 0, 0), name='Falso positivo', fit=False)
    fpl = rotulo(s, 1.8, 5.1, 'falso positivo', ROJO, 13, name='Rótulo FP')
    d = caja(s, 5.0, 1.15, 8.0, 1.5, 'Capacidad de un método de **identificar correctamente a los individuos que NO tienen la enfermedad**: si el paciente está sano, la prueba debe dar negativo.',
             AMA, 16, name='Definición E')
    f = caja(s, 5.0, 2.9, 8.0, 1.25, 'Especificidad = VN / (VN + FP)', BLANCO, 24, align='c', anchor='m', name='Fórmula E', bold=True)
    fpx = caja(s, 5.0, 4.4, 3.9, 2.65, '**Falso positivo**: paciente **sano** cuya prueba dio **positivo**. Una prueba muy específica **minimiza los falsos positivos**.', 'EAF5EA', 15,
               name='FP')
    sc = caja(s, 9.1, 4.4, 3.9, 2.65, 'Se necesita en las **pruebas confirmatorias**: tras un screening positivo, asegura que el resultado sea verdadero.', LAVANDA, 15,
              head='Uso', name='Uso E')
    s.step(*[fade(e, after=(k > 0), dur=200) for k, e in enumerate(san)])
    s.step(fade(d))
    s.step(*[zoom(p, after=(k > 0), dur=200) for k, p in enumerate(neg)], zoom(fp, after=True), fade(fpl, after=True))
    s.step(fade(f))
    s.step(fade(fpx))
    s.step(fade(sc))


def contingencia(D):
    s = nueva(D, 1, 'Tabla de contingencia 2 × 2', src=['VB 6.1 Sensibilidad', 'VB 6.2 Especificidad', 'VB 7 Valores predictivos'], tipo='der', c1=AZUL_M, c2=BLANCO)
    x0, y0, cw, ch = 2.6, 2.0, 2.75, 1.55
    hdr = s.group_start('Encabezados')
    rotulo(s, x0, y0 - 0.65, 'ENFERMO', ROJO, 16, w=cw, h=0.55)
    rotulo(s, x0 + cw, y0 - 0.65, 'SANO', VERDE_OSC, 16, w=cw, h=0.55)
    rotulo(s, x0 - 2.1, y0 + 0.5, 'Prueba +', NAVY, 16, w=2.0, h=0.55)
    rotulo(s, x0 - 2.1, y0 + ch + 0.5, 'Prueba −', NAVY, 16, w=2.0, h=0.55)
    s.group_end()
    cells = {}
    for (k, r, c, f, t) in (('VP', 0, 0, 'F5B7B1', '**VP**\nverdadero positivo'), ('FP', 0, 1, 'FADBD8', '**FP**\nfalso positivo'),
                            ('FN', 1, 0, 'D5DBDB', '**FN**\nfalso negativo'), ('VN', 1, 1, 'D5F5E3', '**VN**\nverdadero negativo')):
        cells[k] = caja(s, x0 + c * cw, y0 + r * ch, cw, ch, t, f, 19, align='c', anchor='m', geom='rect', name='Celda ' + k)
    colS = s.shape(x0 - 0.06, y0 - 0.06, cw + 0.12, 2 * ch + 0.12, 'rect', None, (ROJO, 4.5), False, name='Marco sensibilidad')
    colE = s.shape(x0 + cw - 0.06, y0 - 0.06, cw + 0.12, 2 * ch + 0.12, 'rect', None, (VERDE_OSC, 4.5), False, name='Marco especificidad')
    rowP = s.shape(x0 - 0.06, y0 - 0.06, 2 * cw + 0.12, ch + 0.12, 'rect', None, (AZUL, 4.5, 'dash'), False, name='Marco VPP')
    rowN = s.shape(x0 - 0.06, y0 + ch - 0.06, 2 * cw + 0.12, ch + 0.12, 'rect', None, (AZUL, 4.5, 'dash'), False, name='Marco VPN')
    fS = caja(s, 0.4, 5.4, 4.2, 0.75, 'Sensibilidad = VP / (VP + FN)', 'F5B7B1', 16, anchor='m', bold=True, name='Fórmula S tabla')
    fE = caja(s, 4.75, 5.4, 4.15, 0.75, 'Especificidad = VN / (VN + FP)', 'D5F5E3', 16, anchor='m', bold=True, name='Fórmula E tabla')
    fP = caja(s, 0.4, 6.3, 4.2, 0.75, 'VPP = VP / (VP + FP)', CELESTE, 16, anchor='m', bold=True, name='Fórmula VPP')
    fN = caja(s, 4.75, 6.3, 4.15, 0.75, 'VPN = VN / (VN + FN)', CELESTE, 16, anchor='m', bold=True, name='Fórmula VPN')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, '**Columnas** (estado real): sensibilidad y especificidad evalúan el **desempeño de la prueba**.', BLANCO, 15, head='Lectura vertical',
             name='Lectura columnas')
    c2 = caja(s, 9.35, 4.45, 3.7, 2.6, '**Filas** (resultado): los valores predictivos informan la **probabilidad real de enfermedad** según el resultado obtenido.', AMA, 15,
              head='Lectura horizontal', name='Lectura filas')
    s.step(fade(hdr))
    s.step(*[zoom(cells[k], after=(i > 0)) for i, k in enumerate(('VP', 'FP', 'FN', 'VN'))])
    s.step(fade(colS), fade(fS, after=True), out(colS, after=True, delay=600))
    s.step(fade(colE), fade(fE, after=True), out(colE, after=True, delay=600), fade(c, after=True))
    s.step(fade(rowP), fade(fP, after=True), out(rowP, after=True, delay=600))
    s.step(fade(rowN), fade(fN, after=True), out(rowN, after=True, delay=600), fade(c2, after=True))


def screening(D):
    s = nueva(D, 1, 'Screening frente a prueba confirmatoria', src=['VB 6.5 Esquema resumen', 'VB 6.1 Sensibilidad', 'VB 6.2 Especificidad'], tipo='bandas', c1=ROSA, c2='EAF5EA')
    # embudo
    emb = s.group_start('!!Embudo diagnóstico')
    s.free(3.6, 1.2, 6.1, 3.0, 'M 0 0 L 1000 0 L 650 1000 L 350 1000 Z', ('lin', [(0, CELESTE), (100, AZUL_M)], 90), (INK, 2.0), False)
    s.group_end()
    pobl = grilla(s, 3.9, 1.35, 14, 14, 'AEB6BF', 'Población', h=0.55, gap=0.0)
    l1 = caja(s, 0.4, 1.2, 3.0, 2.6, '**Screening**\nAlta **sensibilidad**: garantiza que el **negativo** sea verdaderamente negativo.', ROSA, 15, name='Rótulo screening')
    conf = caja(s, 5.55, 4.45, 2.2, 0.9, 'Positivos', AMA, 16, align='c', anchor='m', name='Positivos screening')
    l2 = caja(s, 9.9, 1.2, 3.0, 2.6, '**Confirmatoria**\nAlta **especificidad**: garantiza que el **positivo** sea verdaderamente positivo.', 'EAF5EA', 15, name='Rótulo confirmatoria')
    rows = [['', 'Alta sensibilidad', 'Alta especificidad'], ['Uso', 'Screening / tamizaje', 'Prueba confirmatoria'], ['Minimiza', 'Falsos negativos', 'Falsos positivos'],
            ['Ejemplos', 'Test rápido de VIH, test de embarazo, tamizaje neonatal, troponina', 'Western Blot VIH, PCR para patógeno específico']]
    ids, H = tabla_filas(s, 0.4, 5.45, [1.7, 5.4, 5.4], rows, rowh=0.38, size=13.5, name='Tabla S vs E')
    s.step(fade(emb), *[fade(p, after=(k == 0), dur=150) for k, p in enumerate(pobl)])
    s.step(fade(l1))
    s.step(zoom(conf), fade(l2, after=True))
    for r in ids:
        s.step(fade(r))
    s.note('Ejemplo de baja especificidad del material: los anticuerpos para dengue reaccionan en forma cruzada con Zika, Chikungunya y fiebre amarilla.')


def acepciones(D):
    s = nueva(D, 1, 'Segunda acepción: sensibilidad y especificidad analíticas', src=['VB 6.1 Segunda acepción', 'VB 6.2 Especificidad analítica'], tipo='der', c1=VERDE_CL, c2=BLANCO)
    cinta = s.group_start('!!Cinta métrica')
    s.shape(0.5, 1.6, 5.0, 0.6, 'rect', AMA2, (INK, 1.5), False)
    for k in range(21):
        s.arrow([(0.5 + k * 0.25, 1.6), (0.5 + k * 0.25, 1.6 + (0.3 if k % 5 == 0 else 0.16))], INK, 1.0, tail=None)
    s.group_end()
    cal = s.group_start('!!Calibre')
    s.shape(0.5, 3.05, 5.0, 0.42, 'rect', ('lin', [(0, 'D5DBDB'), (100, '909497')], 90), (INK, 1.25), False)
    s.shape(0.5, 3.05, 0.42, 1.3, 'rect', ('lin', [(0, 'D5DBDB'), (100, '909497')], 0), (INK, 1.25), False)
    s.shape(2.2, 3.05, 0.42, 1.3, 'rect', ('lin', [(0, 'D5DBDB'), (100, '909497')], 0), (INK, 1.25), False)
    for k in range(51):
        s.arrow([(0.95 + k * 0.08, 3.05), (0.95 + k * 0.08, 3.05 + (0.18 if k % 5 == 0 else 0.09))], INK, 0.6, tail=None)
    s.group_end()
    t1 = caja(s, 5.8, 1.35, 3.0, 1.2, 'La cinta **no detecta** diferencias de micras.', ROSA, 14, anchor='m', name='Cinta texto')
    t2 = caja(s, 5.8, 2.85, 3.0, 1.2, 'El calibre **sí**: es más **sensible**.', 'EAF5EA', 14, anchor='m', name='Calibre texto')
    c1 = caja(s, 0.5, 4.75, 8.3, 1.05, '**Sensibilidad analítica**: capacidad del método de detectar la **mínima variación** de un analito.', AMA, 16, anchor='m',
              name='S analítica')
    c2 = caja(s, 0.5, 6.0, 8.3, 1.05, '**Especificidad analítica**: capacidad del método de medir **solo el analito** para el que fue diseñado, sin medir sustancias similares.',
              CELESTE, 16, anchor='m', name='E analítica')
    llave = s.group_start('Llave y cerradura')
    enzima_globular(s, 9.6, 1.4, 2.0, 1.7, '85C1E9', 'Método', 'Método forma', size=14, seed=3)
    ficha(s, 11.6, 1.9, 'Analito', 'F5B041', w=1.25, name='Analito ok')
    ficha(s, 11.6, 3.3, 'Similar', 'D5DBDB', w=1.25, name='Analito similar')
    s.inhib([(11.55, 3.5), (11.0, 3.2)], name='No se mide')
    s.group_end()
    n = caja(s, 9.35, 4.45, 3.7, 2.6, 'Estas acepciones describen al **método analítico**; las de las diapositivas previas describen el desempeño **diagnóstico** de la prueba.',
             BLANCO, 14, name='Diferencia acepciones')
    s.step(fade(cinta), fade(t1, after=True))
    s.step(fade(cal), fade(t2, after=True))
    s.step(fade(c1))
    s.step(fade(llave), fade(c2, after=True))
    s.step(fade(n))


def predictivos(D):
    s = nueva(D, 1, 'Valores predictivos positivo y negativo', src=['VB 7 Valores predictivos', 'VB 7.1 VPP', 'VB 7.2 VPN', 'REV VB 7'], tipo='izq', c1=CELESTE, c2=BLANCO)
    a = caja(s, 0.4, 1.2, 4.1, 2.5, 'Probabilidad de que un individuo con **resultado positivo realmente tenga** la enfermedad.', ROSA, 16, head='VPP', headfill=ROJO, name='VPP')
    fa = caja(s, 0.4, 3.85, 4.1, 0.9, 'VPP = VP / (VP + FP)', BLANCO, 19, align='c', anchor='m', bold=True, name='Fórmula VPP2')
    b = caja(s, 0.4, 4.95, 4.1, 2.1, 'Probabilidad de que un individuo con **resultado negativo realmente NO tenga** la enfermedad.', 'EAF5EA', 16, head='VPN', headfill=VERDE_OSC,
             name='VPN')
    fb = caja(s, 4.9, 4.95, 4.0, 0.9, 'VPN = VN / (VN + FN)', BLANCO, 19, align='c', anchor='m', bold=True, name='Fórmula VPN2')
    c = caja(s, 4.9, 1.2, 4.0, 3.5, 'Sensibilidad y especificidad evalúan el **desempeño de la prueba**; los valores predictivos responden la pregunta del paciente: **«con este resultado, ¿qué probabilidad tengo?»**',
             AMA, 16, name='Diferencia VP')
    r = rigor(s, 9.25, 1.2, 3.8, 5.85, 'Relación correcta con el desempeño de la prueba:\n- Más **especificidad** → menos FP → **mayor VPP**.\n- Más **sensibilidad** → menos FN → **mayor VPN**.\n'
              '- Ambos valores dependen además de la **prevalencia** de la enfermedad en la población estudiada.', 14.5, name='Rigor VP')
    m = molecula3d(s, 5.6, 6.0, 1.1, 'aa', name='Deco VP')
    s.step(fade(a), fade(fa, after=True))
    s.step(fade(b), fade(fb, after=True))
    s.step(fade(c))
    s.step(fade(r), fade(m, after=True))


def precision_exactitud(D):
    s = nueva(D, 1, 'Precisión y exactitud: cuatro combinaciones', src=['VB 6.3 Precisión', 'VB 6.4 Exactitud'], tipo='bandas', c1=CREMA, c2=CELESTE)
    conf = [('Alta precisión\nAlta exactitud', [(0.03, -0.02), (-0.03, 0.03), (0.02, 0.04), (-0.02, -0.03)], 'EAF5EA'),
            ('Alta precisión\nBaja exactitud', [(0.48, -0.42), (0.53, -0.38), (0.45, -0.36), (0.5, -0.46)], CREMA),
            ('Baja precisión\nAlta exactitud', [(0.35, 0.1), (-0.3, 0.25), (0.05, -0.4), (-0.15, -0.05)], CELESTE),
            ('Baja precisión\nBaja exactitud', [(0.55, 0.3), (-0.2, 0.62), (0.62, -0.15), (0.2, 0.7)], ROSA)]
    ids = []
    for i, (t, hits, f) in enumerate(conf):
        x = 0.45 + i * 3.15
        g = s.group_start('Diana %d' % (i + 1))
        caja(s, x, 1.2, 2.95, 4.3, '', f, 12)
        gi, hh = diana(s, x + 0.3, 1.4, 2.35, hits, name='Blanco %d' % (i + 1))
        texto(s, x + 0.1, 3.95, 2.75, 1.4, t, 17, INK, True, 'c', 'm')
        s.group_end(); ids.append(g)
    p = caja(s, 0.45, 5.75, 6.15, 1.3, '**Precisión**: menor variabilidad entre resultados repetidos de la misma muestra (**reproducibilidad**): impactos **agrupados**.', AMA, 15,
             name='Def precisión')
    e = caja(s, 6.75, 5.75, 6.1, 1.3, '**Exactitud**: cercanía entre el valor medido y el **valor real** del analito: impactos **en el centro**.', CELESTE, 15, name='Def exactitud')
    for g in ids:
        s.step(fade(g))
    s.step(fade(p))
    s.step(fade(e))


def precision_seguimiento(D):
    s = nueva(D, 1, 'Precisión en el seguimiento, exactitud con suero control', src=['VB 6.3 Precisión', 'VB 6.4 Exactitud'], tipo='der', c1=AZUL_M, c2=BLANCO)
    ej = ejes(s, 0.8, 1.6, 7.6, 3.4, 'mediciones repetidas', 'glucemia (mg/dL)', name='Ejes precisión')
    ref = s.arrow([(0.8, 1.6 + 3.4 * (1 - 80 / 170)), (8.4, 1.6 + 3.4 * (1 - 80 / 170))], VERDE_OSC, 2.5, tail=None, dash='dash', name='Valor real 80')
    rl = rotulo(s, 6.9, 1.6 + 3.4 * (1 - 80 / 170) - 0.5, 'valor real: 80', VERDE_OSC, 13, name='Rótulo valor real')
    pts = []
    for k, v in enumerate((80, 150, 70, 120)):
        px = 1.6 + k * 1.75; py = 1.6 + 3.4 * (1 - v / 170)
        g = s.group_start('Medición %d' % (k + 1))
        s.shape(px - 0.17, py - 0.17, 0.34, 0.34, 'ellipse', ROJO, (INK, 1.25), False)
        texto(s, px - 0.5, py - 0.6, 1.0, 0.4, str(v), 16, ROJO, True, 'c')
        pts.append(s.group_end())
    c1 = caja(s, 0.6, 5.35, 8.0, 1.7, 'Una muestra de **80 mg/dL** que al repetirse da **80, 150, 70 y 120**: método **impreciso**, no válido para el seguimiento. La precisión se prioriza en el **seguimiento de patologías crónicas** (diabetes, hipertensión).',
              ROSA, 14.5, name='Ejemplo imprecisión')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.4, 'Cada mañana, **antes de analizar pacientes**, se procesa un **suero control** de concentración conocida. Si el resultado no coincide (margen **±2 DE**), el método se **calibra**.',
              BLANCO, 15, head='Control de exactitud', name='Control exactitud')
    tb = tubo(s, 10.2, 4.85, 0.45, 1.7, [(0.6, 'F7DC6F', 'Control líquido')], tapa='2E86C1', name='Tubo control', grupo='Suero control')
    tl = rotulo(s, 10.8, 5.5, 'suero control', NAVY, 13, name='Rótulo control')
    s.step(fade(ej), wipe(ref, 'l', after=True), fade(rl, after=True))
    s.step(*[zoom(p, after=(k > 0), delay=0) for k, p in enumerate(pts)])
    s.step(fade(c1))
    s.step(fade(c2), fade(tb, after=True), fade(tl, after=True))


def dx_pronostico(D):
    s = nueva(D, 1, 'Diagnóstico, pronóstico y seguimiento', src=['VB 8.2 Diagnóstico', 'VB 8.3 Pronóstico', 'VB 8.4 Seguimiento', 'REV VB 8.2'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    d = caja(s, 0.4, 1.2, 4.1, 3.4, 'El análisis bioquímico, **combinado con la clínica**, permite determinar que el paciente tiene una patología específica.\nEjemplos del material: β-hCG (embarazo), PCR para COVID-19, Western Blot VIH, glucemia en ayunas ≥ 126 mg/dL en **dos ocasiones**.',
             BLANCO, 14, head='Diagnóstico', name='Diagnóstico')
    p = caja(s, 0.4, 4.85, 4.1, 2.2, 'Predicción de la **evolución, duración y desenlace** probable; p. ej., marcadores tumorales que indican remisión o no.', BLANCO, 14.5,
             head='Pronóstico', name='Pronóstico')
    hb = s.group_start('HbA1c')
    eritrocito(s, 5.0, 1.4, 2.0, name='GR glicado')
    for k in range(6):
        a = 2 * math.pi * k / 6
        s.shape(5.85 + 1.05 * math.cos(a), 2.25 + 1.05 * math.sin(a), 0.32, 0.32, 'hexagon', shade('3B82C4', 0.35, 0.2), ('1B4F72', 1.0), False, adj={'adj': 28000, 'vf': 115470})
    s.group_end()
    sg = caja(s, 7.5, 1.2, 5.55, 2.9, 'Monitoreo de la evolución y del tratamiento. En el paciente diabético se mide la glucemia y la **HbA1c**, que refleja la **glucemia promedio de los últimos 3 meses** (la glucosa en exceso se une a la hemoglobina).',
             CELESTE, 14.5, head='Seguimiento', name='Seguimiento')
    w = caja(s, 4.9, 4.35, 8.15, 1.15, 'En la mayoría de los casos **no es posible diagnosticar con un único análisis**: historia clínica, examen físico, laboratorio, imágenes y evolución.',
             AMA, 15, name='Advertencia único análisis')
    r = rigor(s, 4.9, 5.7, 8.15, 1.35, 'El material menciona la troponina elevada como diagnóstica de IAM: el diagnóstico exige además **ascenso y/o descenso** de troponina con contexto **clínico o ECG** de isquemia (Unidad IV).',
              13.5, name='Rigor troponina')
    s.step(fade(d))
    s.step(fade(p))
    s.step(fade(hb), fade(sg, after=True))
    s.step(fade(w))
    s.step(fade(r))


def gauss_slide(D):
    s = nueva(D, 1, 'Intervalo de referencia: la campana de la población sana', src=['VB 9.1 Definición', 'VB 9.2 Cómo se establecen'], tipo='der', c1=AMA, c2=BLANCO)
    X, Y, W, H = 0.6, 1.4, 8.0, 4.4
    ej = ejes(s, X, Y, W, H, 'concentración del analito', 'n.º de individuos sanos', name='Ejes gauss')
    pts = gauss_path(500, 160, 1000, 60)
    cur = curva(s, X, Y, W, H, pts, NAVY, 4.5, name='!!Curva gaussiana')
    zona = curva(s, X + W * 0.18, Y, W * 0.64, H, [p for p in [(int((px - 180) / 0.64), py) for px, py in pts if 180 <= px <= 820]], NAVY, 0.5, fill=('a', '58D68D', 55),
                 name='Área ±2 DE')
    med = s.arrow([(X + W / 2, Y + H), (X + W / 2, Y + 0.05)], ROJO, 2.5, tail=None, dash='dash', name='Media')
    ml = rotulo(s, X + W / 2 - 0.5, Y - 0.35, 'media', ROJO, 13, w=1.0, name='Rótulo media')
    l1 = s.arrow([(X + W * 0.18, Y + H + 0.05), (X + W * 0.18, Y + H - 1.4)], INK, 2, tail=None, name='Límite inferior')
    l2 = s.arrow([(X + W * 0.82, Y + H + 0.05), (X + W * 0.82, Y + H - 1.4)], INK, 2, tail=None, name='Límite superior')
    r1 = rotulo(s, X + W * 0.18 - 0.75, Y + H + 0.3, '−2 DE (p 2,5)', BLANCO, 12.5, w=1.5, name='Rótulo −2DE')
    r2 = rotulo(s, X + W * 0.82 - 0.75, Y + H + 0.3, '+2 DE (p 97,5)', BLANCO, 12.5, w=1.5, name='Rótulo +2DE')
    p95 = texto(s, X + W / 2 - 1.2, Y + H * 0.55, 2.4, 0.6, '95 %', 30, VERDE_OSC, True, 'c', 'm', name='95 por ciento', glow=True)
    t1 = texto(s, X + 0.2, Y + H - 0.85, 1.3, 0.4, '2,5 %', 15, ROJO, True, 'c', name='Cola inferior')
    t2 = texto(s, X + W - 1.5, Y + H - 0.85, 1.3, 0.4, '2,5 %', 15, ROJO, True, 'c', name='Cola superior')
    c = caja(s, 9.35, 1.2, 3.7, 2.9, 'Rangos de concentración establecidos en **individuos sanos**. Se toman los valores dentro de **±2 desvíos estándar** de la media: **95 %** de la población sana.',
             BLANCO, 14.5, head='Definición', name='Def intervalo')
    w = caja(s, 9.35, 4.35, 3.7, 2.7, 'El **5 % restante** de la población sana puede quedar **fuera del intervalo sin estar enfermo**. «Valores normales» es un término en desuso.',
             ROJO, 14.5, head='Atención', headfill=AMA2, name='Cinco por ciento')
    s.step(fade(ej))
    s.step(wipe(cur, 'l', dur=1000))
    s.step(fade(med), fade(ml, after=True))
    s.step(fade(l1), fade(l2, after=True), fade(r1, after=True), fade(r2, after=True), fade(zona, after=True), zoom(p95, after=True))
    s.step(fade(c))
    s.step(fade(t1), fade(t2, after=True), fade(w, after=True))


def como_establecer(D):
    s = nueva(D, 1, 'Cómo se establece un intervalo de referencia', src=['VB 9.2 Cómo se establecen'], tipo='bandas', c1=CELESTE, c2=AMA)
    pasos = ['Seleccionar una **muestra representativa** de individuos sanos con **criterios de exclusión** rigurosos (no fumadores, sin enfermedades, sin embarazo).',
             'Medir la variable bioquímica en **todos** esos individuos.', 'Los datos se distribuyen según una **curva gaussiana** alrededor de la media.',
             'Tomar los valores dentro de **±2 DE** de la media (95 % de los sanos).', 'El intervalo abarca los **percentiles 2,5 a 97,5** de la distribución.']
    ids = []
    for i, p in enumerate(pasos):
        y = 1.2 + i * 1.02
        g = s.group_start('Paso IR %d' % (i + 1))
        num(s, 3.55, y + 0.2, i + 1)
        caja(s, 4.15, y, 5.9, 0.9, p, BLANCO, 14.5, anchor='m')
        ids.append(s.group_end())
    pob = s.group_start('!!Población y muestra')
    s.shape(0.3, 1.4, 2.8, 2.8, 'ellipse', ('a', 'AEB6BF', 40), (INK, 1.5, 'dash'), False)
    for k in range(16):
        persona_ico(s, 0.55 + (k % 4) * 0.6, 1.65 + (k // 4) * 0.6, 0.5, 'AEB6BF' if k % 3 else '58D68D', name='p%d' % k)
    s.group_end()
    pl = caja(s, 0.3, 4.4, 2.85, 2.65, '**Población**: total de individuos de una zona. **Muestra**: subconjunto representativo, calculado estadísticamente para poder extrapolar.',
              BLANCO, 13.5, name='Población vs muestra')
    gm = s.group_start('Mini campana')
    curva(s, 10.45, 1.5, 2.6, 1.8, gauss_path(500, 170, 1000, 80), NAVY, 3.5, name='Campana mini')
    s.group_end()
    s.step(fade(pob), fade(pl, after=True))
    for k, g in enumerate(ids):
        s.step(fade(g)) if k != 2 else s.step(fade(g), wipe(gm, 'l', after=True))


def factores(D):
    s = nueva(D, 1, 'Factores que modifican los valores de referencia', src=['VB 9.3 Variables que modifican'], tipo='der', c1=VERDE_CL, c2=BLANCO)
    rows = [['Factor', 'Variable afectada', 'Explicación'], ['Edad', 'Hb, fosfatasa alcalina, creatinina, bilirrubina', 'Cambian desde el nacimiento hasta la adultez.'],
            ['Sexo', 'Hb, creatinina, ácido úrico', 'Las hormonas sexuales influyen en la masa muscular y la producción de GR.'],
            ['Embarazo', 'Hb, glucosa, fosfatasa alcalina', 'Dilución por mayor volumen plasmático; resistencia fisiológica a la insulina.'],
            ['Ritmo circadiano', 'Cortisol, hormonas', 'Cortisol más alto a la mañana: análisis estandarizados en ayunas a la mañana.'],
            ['Actividad física', 'CK, mioglobina, hematuria', 'El ejercicio intenso eleva la CK y puede producir hematuria no patológica.'],
            ['Altitud', 'Hb, hematocrito', 'Menor presión de O_{2} → más hemoglobina (compensación).'],
            ['Dieta y ayuno prolongado', 'Cuerpos cetónicos en orina', 'Un ayuno > 12 h puede elevarlos sin diabetes.']]
    ids, H = tabla_filas(s, 0.4, 1.2, [1.85, 2.9, 3.85], rows, rowh=0.55, size=13.5, name='Tabla factores')
    ill = s.group_start('Íconos factores')
    clock(s, 9.6, 1.3, 1.2, hours=7, name='Reloj circadiano')
    human(s, 11.2, 1.1, 2.6, name='Silueta factores')
    s.group_end()
    c = caja(s, 9.35, 3.95, 3.7, 3.1, 'Los valores de referencia **no son universales**: antes de rotular un resultado como patológico hay que conocer quién es el paciente y cómo se tomó la muestra.',
             AMA, 15, name='No universales')
    s.step(fade(ids[0]), fade(ill, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))


def fuera_rango(D):
    s = nueva(D, 1, 'Interpretación de un resultado fuera de rango', src=['VB 9.4 Interpretación'], tipo='izq', c1=CREMA, c2=BLANCO)
    barra = s.group_start('!!Escala de referencia')
    s.shape(0.6, 2.4, 3.0, 0.9, 'rect', CELESTE, (INK, 1.5), False, 'HIPO', 18, F_HEAD, NAVY, True, 'c', 'm')
    s.shape(3.6, 2.4, 5.0, 0.9, 'rect', 'D5F5E3', (INK, 1.5), False, 'Intervalo de referencia', 18, F_HEAD, VERDE_OSC, True, 'c', 'm')
    s.shape(8.6, 2.4, 3.0, 0.9, 'rect', ROSA, (INK, 1.5), False, 'HIPER', 18, F_HEAD, ROJO, True, 'c', 'm')
    s.group_end()
    m1 = s.group_start('Marcador dentro')
    s.shape(5.9, 1.55, 0.4, 0.75, 'downArrow', VERDE_OSC, (INK, 1.0), False)
    s.group_end()
    m2 = s.group_start('Marcador hiper')
    s.shape(10.0, 1.55, 0.4, 0.75, 'downArrow', ROJO, (INK, 1.0), False)
    s.group_end()
    m3 = s.group_start('Marcador hipo')
    s.shape(1.9, 1.55, 0.4, 0.75, 'downArrow', AZUL, (INK, 1.0), False)
    s.group_end()
    c1 = caja(s, 3.6, 3.6, 5.0, 1.2, 'Dentro del rango → **probablemente sano** para esa variable.', 'D5F5E3', 15, anchor='m', name='Dentro')
    c2 = caja(s, 8.6, 3.6, 4.4, 1.55, 'Por encima → **hiper**: p. ej., hiperglucemia si glucosa en ayunas > 100 mg/dL.', ROSA, 15, name='Hiper')
    c3 = caja(s, 0.4, 3.6, 3.0, 1.95, 'Por debajo → **hipo**: p. ej., anemia si Hb < 12 g/dL en mujeres.', CELESTE, 15, name='Hipo')
    w = perla(s, 0.4, 5.75, 12.6, 1.3, 'Antes de interpretar: **edad, sexo, estado fisiológico, condiciones de la toma de muestra** y toda la variabilidad biológica.', 16,
              head='Siempre considerar')
    s.step(fade(barra))
    s.step(zoom(m1), fade(c1, after=True))
    s.step(zoom(m2), fade(c2, after=True))
    s.step(zoom(m3), fade(c3, after=True))
    s.step(fade(w))


def cci(D):
    s = nueva(D, 1, 'Control de calidad interno: la carta control', src=['VB 10.1 Control interno'], tipo='der', c1=AZUL_M, c2=BLANCO)
    X, Y, W, H = 0.8, 1.5, 7.8, 3.9
    ej = ejes(s, X, Y, W, H, 'días', 'resultado del suero control', name='Ejes carta')
    lines = s.group_start('Límites ±2 DE')
    for v, col, lab, dsh in ((0.5, VERDE_OSC, 'media', None), (0.18, ROJO, '+2 DE', 'dash'), (0.82, ROJO, '−2 DE', 'dash'), (0.34, 'F39C12', '+1 DE', 'sysDot'),
                             (0.66, 'F39C12', '−1 DE', 'sysDot')):
        s.arrow([(X, Y + H * v), (X + W, Y + H * v)], col, 2, tail=None, dash=dsh)
        texto(s, X + W + 0.05, Y + H * v - 0.17, 0.85, 0.34, lab, 12, col, True)
    s.group_end()
    vals = [0.52, 0.45, 0.6, 0.4, 0.55, 0.47, 0.62, 0.36, 0.5, 0.1]
    pts = []
    for k, v in enumerate(vals):
        px = X + 0.4 + k * 0.75; py = Y + H * v
        pts.append(s.shape(px - 0.13, py - 0.13, 0.26, 0.26, 'ellipse', NAVY if k < 9 else ROJO, (INK, 1.0), False, name='Control día %d' % (k + 1)))
    poly = s.arrow([(X + 0.4 + k * 0.75, Y + H * v) for k, v in enumerate(vals)], '5D6D7E', 1.25, tail=None, name='Trazo carta')
    fuera = rotulo(s, X + 0.4 + 9 * 0.75 - 1.6, Y + H * 0.1 - 0.75, 'fuera de límites', ROJO, 13, name='Fuera de límites')
    flujo = s.group_start('Decisión diaria')
    caja(s, 0.5, 5.75, 2.6, 1.3, 'Suero control (p. ej., 90 mg/dL de glucosa)', CREMA, 13.5, anchor='m')
    s.arrow([(3.15, 6.4), (3.6, 6.4)], INK, 2.5)
    caja(s, 3.65, 5.75, 2.4, 1.3, '¿Dentro de ±2 DE?', AMA, 15, anchor='m', align='c')
    s.arrow([(6.1, 6.1), (6.55, 5.95)], ACT, 2.5)
    s.arrow([(6.1, 6.7), (6.55, 6.85)], INH, 2.5)
    rotulo(s, 6.6, 5.7, 'Sí → pacientes', 'D5F5E3', 13, w=2.1)
    rotulo(s, 6.6, 6.6, 'No → calibrar', ROSA, 13, w=2.1)
    s.group_end()
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Lo realiza **el propio laboratorio** sobre sus métodos. Los resultados diarios del control se registran en una **carta control**.', BLANCO, 15,
             head='Qué es', name='Qué es CCI')
    o = caja(s, 9.35, 4.45, 3.7, 2.6, 'Objetivo: verificar la **precisión y estabilidad** del método, detectar errores y asegurar que el sistema funciona correctamente.', AMA, 15,
             head='Objetivo', name='Objetivo CCI')
    s.step(fade(ej), fade(lines, after=True))
    s.step(*[zoom(p, after=(k > 0), dur=250) for k, p in enumerate(pts[:9])], wipe(poly, 'l', after=True))
    s.step(zoom(pts[9]), pulse(pts[9], after=True), fade(fuera, after=True))
    s.step(fade(flujo))
    s.step(fade(c))
    s.step(fade(o))


def errores_cce(D):
    s = nueva(D, 1, 'Causas de error y control de calidad externo', src=['VB 10.1 Control interno', 'VB 10.2 Control externo', 'VB 10.3 Importancia'], tipo='bandas', c1=ROSA, c2=CELESTE)
    errs = [('Reactivos', 'vencidos o contaminados'), ('Equipo', 'lámpara, detector, espectrofotómetro, láser'), ('Procedimiento', 'error en el proceso analítico')]
    ids = []
    for i, (t, d) in enumerate(errs):
        ids.append(caja(s, 0.35, 1.2 + i * 1.3, 2.75, 1.15, '**%s**: %s' % (t, d), BLANCO, 13.5, anchor='m', name='Error ' + t))
    org = s.group_start('Circuito CCE')
    caja(s, 3.6, 1.2, 2.9, 1.3, '**Organismo externo** envía muestras de concentración **desconocida**', AMA, 14, anchor='m')
    s.arrow([(6.55, 1.85), (7.2, 1.85)], INK, 2.5)
    caja(s, 7.25, 1.2, 2.75, 1.3, 'El laboratorio las procesa **como pacientes**', CREMA, 14, anchor='m')
    s.arrow([(8.6, 2.55), (8.6, 3.05)], INK, 2.5)
    caja(s, 7.25, 3.1, 2.75, 1.3, 'Devuelve los **resultados**', CREMA, 14, anchor='m')
    s.arrow([(7.2, 3.75), (6.55, 3.75)], INK, 2.5)
    caja(s, 3.6, 3.1, 2.9, 1.3, 'Se comparan con los **valores reales** → desempeño', 'D5F5E3', 14, anchor='m')
    s.group_end()
    obj = caja(s, 3.6, 4.65, 6.4, 1.0, 'Objetivo del CCE: **comparar el desempeño** con otros laboratorios y garantizar estándares nacionales e internacionales.', BLANCO, 14,
               anchor='m', name='Objetivo CCE')
    imp = caja(s, 0.35, 5.85, 9.65, 1.2, 'Importancia: **confiabilidad** de los resultados, **seguridad del paciente**, comparación entre laboratorios y **respaldo legal y profesional**.',
               NAVY, 15, anchor='m', name='Importancia CC')
    gl = s.group_start('Mundo de laboratorios')
    for k in range(4):
        a = 2 * math.pi * k / 4
        tubo(s, 11.45 + 0.95 * math.cos(a), 2.6 + 0.95 * math.sin(a), 0.32, 1.1, [(0.5, 'B3261E', 'r%d' % k), (0.3, 'F9E79F', 'p%d' % k)], name='Tubo red %d' % k)
    s.shape(11.35, 2.75, 0.75, 0.75, 'ellipse', shade(NAVY, 0.3, 0.3), (INK, 1.5), False, 'CCE', 12, F_HEAD, BLANCO, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids)])
    s.step(fade(gl), wipe(org, 'l', after=True, dur=900))
    s.step(fade(obj))
    s.step(fade(imp))


def anexo(D):
    s = nueva(D, 1, 'Valores de referencia frecuentes', src=['VB Anexo Valores de referencia'], tipo='izq', c1=CREMA, c2=BLANCO)
    rows = [['Variable', 'Valor de referencia', 'Unidad'], ['Glucemia en ayunas', '70 – 100', 'mg/dL'], ['Glucemia alterada en ayunas', '100 – 125', 'mg/dL'],
            ['Diabetes (diagnóstico)', '≥ 126 (en 2 ocasiones)', 'mg/dL'], ['Hemoglobina (varón adulto)', '13 – 17', 'g/dL'], ['Hemoglobina (mujer adulta)', '12 – 16', 'g/dL'],
            ['Glóbulos rojos', '4,5 – 6', 'millones por mm^{3}'], ['Leucocitos', '4.000 – 11.000', 'por mm^{3}'], ['Plaquetas', '150.000 – 400.000', 'por mm^{3}']]
    ids, H = tabla_filas(s, 0.45, 1.2, [3.7, 2.9, 2.3], rows, rowh=0.6, size=16, name='Tabla anexo')
    deco = s.group_start('Deco anexo')
    tubo(s, 9.9, 1.3, 0.6, 2.4, [(0.42, 'B3261E', 'ra'), (0.05, 'F2F3F4', 'ba'), (0.35, 'F7DC6F', 'pa')], tapa='8E44AD', name='Tubo anexo')
    eritrocito(s, 10.9, 1.5, 1.3, name='GR anexo'); leucocito(s, 11.6, 2.8, 1.1, 'linfocito', name='Lc anexo'); plaqueta(s, 10.7, 3.2, 0.6, name='Pl anexo')
    molecula3d(s, 10.1, 4.0, 1.6, 'glucosa', name='Glc anexo')
    s.group_end()
    c = caja(s, 9.35, 5.75, 3.7, 1.3, 'Todos se leen con la **variabilidad biológica** en mente.', AMA, 15, anchor='m', name='Nota anexo')
    s.step(fade(ids[0]), fade(deco, after=True))
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids[1:4])])
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids[4:6])])
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids[6:])])
    s.step(fade(c))


def integracion_a(D):
    s = nueva(D, 1, 'Integración A: de la variable a la interpretación', src=['VB 1 Variables bioquímicas', 'VB 6 Sensibilidad y especificidad', 'VB 9 Valores de referencia',
                                                                              'VB 10 Control de calidad'], tipo='bandas', c1=CELESTE, c2=AMA)
    pasos = [('Variable bioquímica', 'Unidad + valor de referencia + significado clínico', CELESTE),
             ('Muestra correcta', 'Suero o plasma según el analito; cuidado con el anticoagulante', LAVANDA),
             ('Medición confiable', 'Precisión, exactitud, control interno y externo', 'EAF5EA'),
             ('Desempeño de la prueba', 'Sensibilidad, especificidad, VPP y VPN', ROSA),
             ('Interpretación', 'Intervalo de referencia + factores biológicos + clínica', AMA)]
    ids = []
    for i, (t, d, f) in enumerate(pasos):
        x = 0.4 + i * 2.55
        g = s.group_start('Integración A %d' % (i + 1))
        num(s, x + 0.95, 1.2, i + 1)
        caja(s, x, 1.8, 2.3, 2.6, '**%s**\n%s' % (t, d), f, 15, spc=4)
        if i < 4:
            s.arrow([(x + 2.32, 3.1), (x + 2.53, 3.1)], INK, 3)
        ids.append(s.group_end())
    il = s.group_start('Ilustración integración A')
    tubo(s, 0.7, 4.75, 0.5, 2.1, [(0.42, 'B3261E', 'ri'), (0.05, 'F2F3F4', 'bi'), (0.35, 'F7DC6F', 'pi')], tapa='8E44AD', name='Tubo int')
    centrifuga(s, 1.6, 4.9, 1.5, name='Centrífuga int')
    gi, hh = diana(s, 3.6, 4.85, 1.7, [(0.03, -0.02), (-0.03, 0.03), (0.02, 0.04)], name='Diana int')
    curva(s, 5.6, 4.9, 2.6, 1.7, gauss_path(500, 160, 1000, 80), NAVY, 3.5, name='Campana int')
    s.group_end()
    c = caja(s, 8.5, 4.75, 4.4, 2.3, 'Un dato de laboratorio solo es útil si cada eslabón es correcto: **muestra, método, desempeño e interpretación** en contexto.', NAVY, 15.5,
             name='Síntesis integración A')
    for g in ids:
        s.step(fade(g))
    s.step(fade(il))
    s.step(zoom(c))


def build(D):
    suero_plasma(D)
    tabla_sp(D)
    cuando_usar(D)
    sensibilidad(D)
    especificidad(D)
    contingencia(D)
    screening(D)
    acepciones(D)
    predictivos(D)
    precision_exactitud(D)
    precision_seguimiento(D)
    dx_pronostico(D)
    gauss_slide(D)
    como_establecer(D)
    factores(D)
    fuera_rango(D)
    cci(D)
    errores_cce(D)
    anexo(D)
    integracion_a(D)
