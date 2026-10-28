# -*- coding: utf-8 -*-
"""UNIDAD III (parte 1): definición, hemoglobina, volumen plasmático (Morph), manifestaciones, severidad,
índices hematimétricos, clasificaciones morfológica y fisiopatológica."""
from plantillas import *
from u1 import persona_ico


def falciforme(s, x, y, w, name='Drepanocito'):
    h = w * 0.55
    return s.free(x, y, w, h, 'M 0 600 C 150 100 850 100 1000 600 C 800 350 200 350 0 600 Z', ('lin', [(0, 'E57373'), (100, 'B03A2E')], 90), ('6E1A12', 1.25),
                  name=name)


def divisor_u3(D):
    def arte(s):
        g = s.group_start('Arte unidad III')
        vessel(s, 6.8, 0.6, 6.3, 1.3, name='Vaso div', rbcs=8)
        for k, (kind, d) in enumerate((('normal', 1.6), ('hipo', 1.3), ('esfero', 1.1), ('reti', 1.4))):
            eritrocito(s, 7.0 + k * 1.55, 2.4, d, kind, name='GR div %d' % k)
        hemoglobina(s, 7.0, 4.3, 2.0, name='Hb div')
        medula_osea(s, 9.4, 4.2, 3.6, 2.5, name='Médula div', celulas=14)
        s.group_end()
        return g
    divisor(D, 3, 'III', 'Bioquímica clínica de las anemias', 'Del transporte de oxígeno a la lectura del hemograma',
            ['Definición y hemoglobina', 'Volumen plasmático', 'Manifestaciones clínicas', 'Severidad', 'Índices hematimétricos', 'Clasificación morfológica',
             'Reticulocitos y clasificación fisiopatológica', 'Anemia megaloblástica y vitamina B_{12}', 'Biomarcadores: LDH, bilirrubina, Coombs, VSG', 'Casos clínicos'], arte,
            src=['AN 1 Definición'])


def definicion(D):
    s = nueva(D, 3, 'Anemia: una masa eritrocitaria insuficiente', src=['AN 1 Definición'], tipo='der', c1=ROJO, c2=ROSA)
    pul = s.group_start('!!Pulmones')
    for x in (0.45, 1.75):
        s.free(x, 1.5, 1.2, 2.0, smooth([(500, 0), (900, 200), (1000, 700), (700, 1000), (200, 950), (0, 500), (200, 100)]), shade('F1948A', 0.4, 0.25), ('922B21', 1.5))
    texto(s, 0.45, 3.55, 2.5, 0.4, 'pulmones', 14, '922B21', True, 'c')
    s.group_end()
    vas = vessel(s, 3.1, 2.1, 3.6, 0.9, name='!!Vaso sanguíneo', rbcs=3)
    tej = s.group_start('!!Tejidos')
    for k in range(6):
        s.shape(6.95 + (k % 3) * 0.6, 1.6 + (k // 3) * 0.75, 0.55, 0.7, 'hexagon', shade('F5CBA7', 0.4, 0.2), ('A04000', 1.0), False, adj={'adj': 25000, 'vf': 115470})
    texto(s, 6.9, 3.15, 1.9, 0.4, 'tejidos', 14, 'A04000', True, 'c')
    s.group_end()
    o2s = [ficha(s, 3.3 + k * 1.1, 1.55, 'O_{2}', '5DADE2', w=0.7, h=0.4, size=12, name='O2 %d' % k) for k in range(3)]
    d = caja(s, 0.45, 4.2, 8.3, 1.4, 'Síndrome clínico caracterizado por el **descenso de la masa eritrocitaria circulante**, de forma que resulta **insuficiente para sustentar el transporte de O_{2}** a los tejidos.',
             AMA, 16, name='Definición anemia')
    sd = caja(s, 0.45, 5.8, 8.3, 1.25, 'Es un **síndrome**, no una enfermedad en sí misma: un conjunto de signos y síntomas con **múltiples causas** posibles.', BLANCO, 16, name='Síndrome')
    c = caja(s, 9.35, 1.2, 3.7, 3.3, 'La anemia se **define y diagnostica** por los valores de **hemoglobina**.', BLANCO, 17, head='Concepto clave', anchor='m', name='Concepto Hb')
    hb = hemoglobina(s, 10.2, 4.75, 2.1, name='!!Hemoglobina')
    s.step(fade(pul), fade(vas, after=True), fade(tej, after=True))
    s.step(*[fade(o, after=(k > 0)) for k, o in enumerate(o2s)], *[path(o, 3.8 - k * 1.1, 0.3, after=(k == 0), dur=1000) for k, o in enumerate(o2s)])
    s.step(fade(d))
    s.step(fade(sd))
    s.step(fade(c), zoom(hb, after=True))


def por_que_hb(D):
    s = nueva(D, 3, '¿Por qué hemoglobina y no hematocrito ni recuento?', src=['AN 1 Concepto clave'], tipo='bandas', c1=ROSA, c2=CREMA)
    a = caja(s, 3.55, 1.2, 6.5, 1.45, '**Hemoglobina**: criterio que **define y diagnostica** la anemia.', 'EAF5EA', 18, anchor='m', name='Criterio Hb')
    b = caja(s, 3.55, 2.85, 6.5, 1.45, '**Hematocrito**: no se usa como criterio diagnóstico porque **varía con el estado de hidratación**.', ROSA, 16, anchor='m', name='No Hto')
    c = caja(s, 3.55, 4.5, 6.5, 1.45, '**Recuento de glóbulos rojos**: puede haber eritrocitos disminuidos sin anemia y viceversa.', ROSA, 16, anchor='m', name='No recuento')
    e = caja(s, 3.55, 6.1, 6.5, 0.95, 'Ejemplo: en la **talasemia** puede haber recuento normal con **Hb baja → anemia**.', AMA, 15.5, anchor='m', name='Talasemia ejemplo')
    t1 = tubo(s, 0.6, 1.4, 0.7, 2.8, [(0.45, 'B3261E', 'r1'), (0.37, 'F7DC6F', 'p1')], tapa='8E44AD', name='Tubo Hto', grupo='Tubo hematocrito')
    hb = hemoglobina(s, 1.6, 1.5, 1.4, name='Hb criterio')
    gr = s.group_start('Recuento')
    for k in range(6):
        eritrocito(s, 0.45 + (k % 3) * 0.85, 4.6 + (k // 3) * 0.85, 0.75, 'hipo' if k % 2 else 'normal', name='GR talasemia %d' % k)
    s.group_end()
    r_ = rigor(s, 10.3, 1.2, 2.75, 5.85, 'En la talasemia es frecuente que el recuento sea **normal o incluso alto**, con eritrocitos **microcíticos** y Hb baja: por eso el recuento no define la anemia.',
               13.5, name='Rigor talasemia')
    s.step(zoom(hb), fade(a, after=True))
    s.step(fade(t1), fade(b, after=True))
    s.step(fade(gr), fade(c, after=True))
    s.step(fade(e))
    s.step(fade(r_))


def valores_hb(D):
    s = nueva(D, 3, 'Valores de hemoglobina por debajo de los cuales hay anemia', src=['AN 1.1 Valores de referencia de Hb', 'REV AN 1.1'], tipo='izq', c1=ROSA, c2=BLANCO)
    rows = [['Grupo / condición', 'Anemia si Hb (g/dL)'], ['Hombre adulto', '< 13'], ['Mujer adulta', '< 12'], ['Embarazada / hemodilución', '< 11'], ['Recién nacido', '< 13,5'],
            ['Hasta 3 meses de vida', '< 9,5'], ['Niños hasta la pubertad (~12 años)', '< 11']]
    ids, H = tabla_filas(s, 5.0, 1.2, [4.6, 3.4], rows, rowh=0.58, size=16, name='Tabla Hb')
    sil = s.group_start('Siluetas')
    for k, (hh, c) in enumerate(((2.2, '5D6D7E'), (2.0, 'C0392B'), (2.0, 'AF7AC5'), (0.8, 'F5B041'), (1.0, '58D68D'), (1.5, '2E86C1'))):
        persona_ico(s, 0.45 + (k % 3) * 1.45, 1.4 + (k // 3) * 2.55 + (2.2 - hh), hh, c, name='Silueta %d' % k)
    s.group_end()
    n = caja(s, 0.4, 6.15, 4.3, 0.9, 'Los intervalos abarcan al **95 %** de los sanos.', AMA, 15, anchor='m', name='Nota 95')
    r_ = rigor(s, 5.0, 1.4 + H, 8.0, 6.95 - (1.4 + H), 'Son **umbrales de referencia**: un único valor no diagnostica todas las situaciones; se interpretan con la edad, el sexo, el embarazo, la altitud y el volumen plasmático.',
               13.5, name='Rigor umbrales')
    s.step(fade(sil), fade(ids[0], after=True))
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids[1:3])])
    s.step(fade(ids[3]))
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids[4:])])
    s.step(fade(n))
    s.step(fade(r_))


# ---------------------------------------------------------------- volumen plasmático (Morph)
VP = {1: ('Volumen plasmático normal', 3.6, 'Hb medida: referencia'), 2: ('Embarazo: hemodilución fisiológica', 5.3, 'Hb aparentemente baja'),
      3: ('Deshidratación: hemoconcentración', 2.5, 'Hb falsamente elevada')}


def escena_vp(D, st):
    t, alto, lect = VP[st]
    s = nueva(D, 3, t, tipo='der', c1=ROJO, c2=ROSA, morph=st > 1, src=['AN 1.2 Condiciones que falsean la Hb'], tw=8.7)
    ids = {}
    base = 6.7
    ids['vaso'] = s.shape(1.0, base - alto, 4.2, alto, 'roundRect', ('lin', [(0, 'FCF3CF'), (100, 'F9E79F')], 90), ('B7950B', 2.0), False, name='!!Volumen plasmático',
                          adj={'adj': 8000})
    random.seed(3)
    for k in range(12):
        fx_ = 0.12 + (k % 4) * 0.21; fy = 0.15 + (k // 4) * 0.28
        ids['gr%d' % k] = eritrocito(s, 1.0 + 4.2 * fx_, base - alto + alto * fy, 0.55, name='!!Eritrocito %d' % (k + 1))
    ids['lbl'] = rotulo(s, 1.4, base + 0.12, lect, ROJO if st > 1 else VERDE_OSC, 15, w=3.4, name='!!Lectura Hb')
    ids['gauge'] = s.group_start('!!Medidor Hb')
    s.shape(6.0, 1.4, 0.8, 5.3, 'roundRect', BLANCO, (INK, 1.75), False, adj={'adj': 50000})
    lvl = {1: 0.55, 2: 0.35, 3: 0.75}[st]
    s.shape(6.08, 1.4 + 5.3 * (1 - lvl), 0.64, 5.3 * lvl - 0.08, 'roundRect', ('lin', [(0, 'E74C3C'), (100, '922B21')], 90), None, False, adj={'adj': 50000})
    texto(s, 5.7, 6.8, 1.4, 0.35, 'Hb', 15, INK, True, 'c')
    s.group_end()
    return s, ids


def volumen_plasmatico(D):
    ini = len(D.slides) + 1
    s, i = escena_vp(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'La Hb es una **concentración**: depende de la masa de eritrocitos **y del volumen de plasma** en que están diluidos.', BLANCO, 15.5, head='Concentración',
             name='Caja VP1')
    s.step(fade(i['vaso']), *[fade(i['gr%d' % k], after=(k == 0)) for k in range(12)])
    s.step(fade(i['gauge']), fade(i['lbl'], after=True))
    s.step(fade(c))
    s, i = escena_vp(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.3, '**Mayor volumen plasmático** → los mismos eritrocitos quedan más diluidos → Hb **aparentemente baja** (umbral en embarazo: < 11 g/dL).', 'FDEBD0', 15,
             head='Embarazo', name='Caja VP2')
    s.step(fade(c))
    s, i = escena_vp(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, '**Menor volumen plasmático** (síndrome diarreico, diálisis) → Hb **falsamente elevada**: puede **enmascarar** una anemia real.', ROSA, 15,
             head='Deshidratación', headfill=ROJO, name='Caja VP3')
    s.step(fade(c))
    registrar_morph(D, ini, len(D.slides), 'Efecto del volumen plasmático sobre la concentración de hemoglobina (normal → hemodilución → hemoconcentración)',
                    ['!!Volumen plasmático'] + ['!!Eritrocito %d' % k for k in range(1, 13)] + ['!!Medidor Hb', '!!Lectura Hb'],
                    'El recipiente de plasma se alarga o acorta mientras los 12 eritrocitos (siempre los mismos) se separan o se aprietan; el medidor de Hb baja o sube.')


def otras_condiciones(D):
    s = nueva(D, 3, 'Otras condiciones que modifican la hemoglobina medida', src=['AN 1.2 Condiciones que falsean la Hb'], tipo='izq', c1=CREMA, c2=BLANCO)
    items = [('Embarazo', 'Mayor volumen plasmático → hemodilución → Hb aparentemente baja.', 'FDEBD0'),
             ('Deshidratación', 'Síndrome diarreico, diálisis: menor volumen → Hb falsamente elevada.', CELESTE),
             ('Insuficiencia renal aguda o cardíaca congestiva', 'Modifican el volumen plasmático.', LAVANDA),
             ('Hemorragia aguda, neoplasias, edema', 'Alteran la concentración de Hb en sangre.', ROSA)]
    ids = []
    for k, (t, d, f) in enumerate(items):
        x = 0.45 + (k % 2) * 4.35; y = 1.25 + (k // 2) * 2.95
        ids.append(caja(s, x, y, 4.15, 2.7, d, f, 17, head=t, name='Condición %s' % t[:12]))
    k_ = kidney(s, 9.5, 1.3, 1.3, name='Riñón cond')
    h_ = corazon_anat(s, 11.15, 1.25, 1.7, name='Corazón cond')
    c = caja(s, 9.2, 4.3, 3.85, 2.75, 'Antes de rotular una anemia, preguntá **cómo está el volumen plasmático** del paciente.', AMA, 16, name='Pregunta volumen')
    for g in ids:
        s.step(fade(g))
    s.step(fade(k_), fade(h_['g'], after=True), fade(h_['ci']), fade(h_['cd']), fade(c, after=True))


def instalacion(D):
    s = nueva(D, 3, 'La velocidad de instalación define la intensidad de los síntomas', src=['AN 2 Manifestaciones clínicas'], tipo='der', c1=ROJO, c2=BLANCO)
    X, Y, W, H = 0.8, 1.6, 7.8, 4.3
    ej = ejes(s, X, Y, W, H, 'tiempo', 'hemoglobina (g/dL)', name='Ejes instalación')
    def yv(v):
        return int((1 - v / 16) * 1000)
    lenta = curva(s, X, Y, W, H, [(0, yv(14)), (300, yv(12)), (600, yv(7)), (1000, yv(3.5))], NAVY, 4.5, name='Instalación lenta')
    aguda = curva(s, X, Y, W, H, [(0, yv(14)), (80, yv(13.8)), (150, yv(6)), (220, yv(6))], ROJO, 4.5, name='Instalación aguda')
    l1 = rotulo(s, 5.9, 4.6, 'lenta (crónica): 3–4 g/dL', NAVY, 14, name='Rótulo lenta')
    l2 = rotulo(s, 2.0, 3.6, 'aguda: 14 → 6 g/dL', ROJO, 14, name='Rótulo aguda')
    c1 = caja(s, 9.35, 1.2, 3.7, 2.8, '**Instalación lenta**: el organismo **compensa** progresivamente; un paciente puede caminar y hablar con Hb de **3–4 g/dL**.', CELESTE, 15,
              head='Crónica', headfill=NAVY, name='Lenta')
    c2 = caja(s, 9.35, 4.25, 3.7, 2.8, '**Instalación aguda**: síntomas **dramáticos**; una caída brusca de **14 a 6 g/dL** genera todas las manifestaciones posibles.', ROSA, 15,
              head='Aguda', headfill=ROJO, name='Aguda')
    n = caja(s, 0.6, 6.25, 8.0, 0.8, 'La anemia es uno de los síndromes con **mayor variedad** de manifestaciones clínicas.', AMA, 15, anchor='m', name='Variedad')
    s.step(fade(ej))
    s.step(wipe(lenta, 'l', dur=1100), fade(l1, after=True), fade(c1, after=True))
    s.step(wipe(aguda, 'l', dur=600), fade(l2, after=True), fade(c2, after=True))
    s.step(fade(n))


def manifestaciones(D, parte):
    if parte == 1:
        t = 'Manifestaciones clínicas (I): oxígeno y compensación'
        items = [('Astenia / adinamia', 'Falta de O_{2} para el metabolismo energético celular', (3.2, 2.6)),
                 ('Disnea', 'Hipoxia tisular y compensación ventilatoria', (3.0, 2.2)), ('Taquicardia', 'El corazón compensa bombeando más flujo', (3.1, 2.75)),
                 ('Hipotensión (en hemorragias)', 'Pérdida de volumen sanguíneo', (3.1, 3.0)), ('Mareos y vértigo', 'El cerebro es el primero en resentir la hipoxia', (3.0, 1.45)),
                 ('Somnolencia, confusión, irritabilidad', 'Hipoxia cerebral', (3.0, 1.5))]
    else:
        t = 'Manifestaciones clínicas (II): redistribución y hemólisis'
        items = [('Palidez de piel y mucosas', 'Vasoconstricción periférica y menos Hb visible', (2.95, 1.75)), ('Manos frías', 'Redistribución del flujo hacia órganos vitales', (2.3, 4.2)),
                 ('Uñas frágiles, pelo seco', 'Déficit crónico de O_{2} y nutrientes periféricos', (2.2, 4.4)), ('Menor diuresis', 'Reducción del flujo renal por hipoperfusión', (3.1, 3.5)),
                 ('Dolor torácico · menor deseo sexual', 'Estrés cardiorrespiratorio · hipoxia y redistribución del flujo', (3.1, 2.7)),
                 ('Ictericia · esplenomegalia (hemólisis)', 'Aumento de bilirrubina · hipertrofia del bazo por mayor destrucción', (3.4, 3.2))]
    s = nueva(D, 3, t, src=['AN 2.1 Síntomas y signos'], tipo='bandas', c1=ROSA, c2=SALM)
    hu = human(s, 4.9, 1.1, 5.9, name='!!Paciente')
    ids = []
    for k, (n, m, (px, py)) in enumerate(items):
        izq = k % 2 == 0
        y = 1.2 + (k // 2) * 1.95
        x = 0.35 if izq else 8.4
        g = s.group_start('Manifestación %d' % (k + 1))
        caja(s, x, y, 4.55, 1.75, '**%s**\n%s' % (n, m), BLANCO, 15)
        tx = 6.4 + (px - 3.1) * 0.6 * (1 if izq else 1)
        ty = 1.1 + py * 0.95
        s.arrow([(x + 4.55 if izq else x, y + 0.85), (tx, ty)], ROJO, 1.75)
        s.shape(tx - 0.09, ty - 0.09, 0.18, 0.18, 'ellipse', ROJO, None, False)
        ids.append(s.group_end())
    s.step(fade(hu))
    for k in range(0, len(ids), 2):
        s.step(fade(ids[k]), fade(ids[k + 1], after=True))


def severidad(D):
    s = nueva(D, 3, 'Severidad de la anemia y transfusión', src=['AN 3 Clasificación por severidad', 'REV AN 3'], tipo='izq', c1=ROSA, c2=BLANCO)
    esc = [('≥ 12', 'Normal (ref. mujer adulta)', 'D5F5E3'), ('9,5 – 11,9', 'Leve', 'FCF3CF'), ('8 – 9,4', 'Moderada', 'FAD7A0'), ('6,5 – 7,9', 'Severa', 'F1948A'),
           ('< 6,5', 'Grave / compromiso vital', 'C0392B')]
    ids = []
    for k, (v, t, f) in enumerate(esc):
        y = 1.25 + k * 0.95
        g = s.group_start('Grado %d' % k)
        s.shape(0.45, y, 1.95, 0.85, 'rect', f, (INK, 1.5), False, v, 17, F_HEAD, BLANCO if f == 'C0392B' else INK, True, 'c', 'm')
        s.shape(2.4, y, 3.0, 0.85, 'rect', f, (INK, 1.5), False, t, 15, F_HEAD, BLANCO if f == 'C0392B' else INK, True, 'c', 'm')
        ids.append(s.group_end())
    un = texto(s, 0.45, 6.05, 4.95, 0.4, 'valores de Hb en g/dL', 13, '5D6D7E', True, 'c', name='Unidad severidad')
    tr = caja(s, 5.75, 1.2, 3.4, 2.55, 'Indicación de transfusión cuando la Hb cae **por debajo de 7 g/dL**. Cada unidad eleva la Hb ≈ **1 g/dL** y el hematocrito ≈ **3 %**.', AMA, 14.5,
              head='Transfusión', name='Transfusión')
    ht = caja(s, 5.75, 4.0, 3.4, 2.0, '**Hto ≈ Hb × 3**\nHb 7 → Hto ≈ 21 % (normal ~45 %).', BLANCO, 16, anchor='m', name='Hto Hb')
    bolsa = s.group_start('Bolsa de sangre')
    s.shape(6.6, 6.1, 1.5, 0.95, 'roundRect', shade('C0392B', 0.35, 0.3), ('641E16', 1.5), False, 'GR', 14, F_HEAD, BLANCO, True, 'c', 'm', adj={'adj': 25000})
    s.group_end()
    r_ = rigor(s, 9.4, 1.2, 3.65, 5.85, 'El umbral de 7 g/dL es una **estrategia restrictiva** para pacientes **estables**; la decisión de transfundir se individualiza (enfermedad cardiovascular, sangrado activo, síntomas). '
               'Las escalas de severidad varían según la fuente (p. ej., OMS).', 13.5, name='Rigor transfusión')
    for g in ids:
        s.step(fade(g, after=False)) if g == ids[0] else s.anim[-1].append(fade(g, after=True))
    s.anim[-1].append(fade(un, after=True))
    s.step(fade(tr), fade(bolsa, after=True))
    s.step(fade(ht))
    s.step(fade(r_))


# ---------------------------------------------------------------- índices hematimétricos
def contador(D):
    s = nueva(D, 3, 'Contador hematológico: eritrocitos de a uno frente al láser', src=['AN 4 Índices hematimétricos'], tipo='der', c1=AZUL, c2=LAVANDA)
    canal = s.shape(0.5, 3.0, 8.2, 0.9, 'roundRect', ('lin', [(0, 'EAF2F8'), (100, 'D6EAF8')], 90), ('1F618D', 2.0), False, name='Canal de flujo', adj={'adj': 50000})
    las = s.group_start('Láser')
    s.shape(4.2, 1.0, 1.0, 0.8, 'rect', shade('7F8C8D', 0.3, 0.3), (INK, 1.5), False)
    s.arrow([(4.7, 1.8), (4.7, 3.2)], 'E74C3C', 5, tail=None)
    s.group_end()
    det = s.group_start('Detector')
    s.shape(4.2, 4.5, 1.0, 0.7, 'rect', shade('34495E', 0.3, 0.3), (INK, 1.5), False, 'detector', 11, F_HEAD, BLANCO, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    grs = [eritrocito(s, 0.7 + k * 0.05, 3.15, 0.6, 'normal' if k != 2 else 'hipo', name='GR flujo %d' % k) for k in range(4)]
    c1 = caja(s, 0.5, 5.45, 8.2, 1.6, 'Por **impedancia eléctrica** o **citometría de flujo**, el equipo hace pasar los glóbulos rojos **uno a uno**; la distorsión de la luz indica el tamaño. Calcula promedios con **millones de células por segundo**.',
              BLANCO, 14.5, name='Principio contador')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.4, 'Los **índices hematimétricos** son parámetros calculados automáticamente que describen la **morfología** de los eritrocitos y permiten **clasificar** la anemia.',
              BLANCO, 15, head='Índices', name='Def índices')
    lst = caja(s, 9.35, 4.85, 3.7, 2.2, '**VCM · HCM · CHCM · RDW** (y el hematocrito calculado)', AMA, 17, anchor='m', name='Lista índices')
    s.step(fade(canal), fade(las, after=True), fade(det, after=True))
    s.step(*[path(g, 7.3 - k * 0.6, 0, after=(k > 0), delay=0, dur=1100) for k, g in enumerate(grs)])
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(lst))


def vcm(D):
    s = nueva(D, 3, 'VCM: el tamaño promedio del eritrocito', src=['AN 4.1 VCM'], tipo='bandas', c1=ROSA, c2=CREMA)
    sizes = [('Microcítico', '< 80 fL', 1.2, 'hipo'), ('Normocítico', '80 – 100 fL', 1.6, 'normal'), ('Macrocítico', '> 100 fL', 2.1, 'normal')]
    ids = []
    for k, (t, v, d, kd) in enumerate(sizes):
        cx = 4.3 + k * 2.2
        g = s.group_start('VCM ' + t)
        eritrocito(s, cx - d / 2, 3.0 - d / 2, d, kd, name='GR ' + t)
        rotulo(s, cx - 1.0, 4.2, t, [CELESTE, 'D5F5E3', ROSA][k], 15, w=2.0)
        texto(s, cx - 1.0, 4.75, 2.0, 0.45, v, 17, INK, True, 'c')
        ids.append(s.group_end())
    esc = s.group_start('Escala fL')
    s.shape(3.3, 5.55, 6.6, 0.35, 'rect', ('lin', [(0, CELESTE), (50, 'D5F5E3'), (100, ROSA)], 0), (INK, 1.25), False)
    for v, x in (('80', 5.4), ('100', 7.6)):
        s.arrow([(x, 5.45), (x, 6.0)], INK, 2.5, tail=None)
        texto(s, x - 0.4, 6.0, 0.8, 0.35, v, 14, INK, True, 'c')
    s.group_end()
    d = caja(s, 0.35, 1.2, 2.75, 3.0, '**Volumen corpuscular medio**: volumen promedio de los eritrocitos.', AMA, 15.5, name='Def VCM')
    u = caja(s, 0.35, 4.45, 2.75, 2.6, 'Unidad: **fentolitros (fL)**\n1 fL = 10^{−15} L\n(pico → femto → atto)', BLANCO, 15, name='Unidad fL')
    n = caja(s, 10.35, 1.2, 2.7, 5.85, 'Normal: **80 – 100 fL**.\nEl VCM ordena la anemia en **micro**, **normo** o **macrocítica** y orienta el estudio siguiente.', BLANCO, 15, name='Normal VCM')
    s.step(fade(d), fade(u, after=True))
    s.step(fade(ids[1]))
    s.step(fade(ids[0]))
    s.step(fade(ids[2]))
    s.step(wipe(esc, 'l'), fade(n, after=True))


def hcm_chcm(D):
    s = nueva(D, 3, 'HCM y CHCM: contenido y concentración de hemoglobina', src=['AN 4.2 HCM', 'AN 4.3 CHCM'], tipo='der', c1=ROJO, c2=BLANCO)
    a = eritrocito(s, 0.8, 1.5, 2.2, 'normal', name='GR normocrómico')
    al = rotulo(s, 0.7, 3.85, 'normocrómico 27–32 pg', 'D5F5E3', 14, w=2.4, name='Rótulo normocrómico')
    b = eritrocito(s, 3.6, 1.5, 2.2, 'hipo', name='GR hipocrómico')
    bl = rotulo(s, 3.5, 3.85, 'hipocrómico < 27 pg', CELESTE, 14, w=2.4, name='Rótulo hipocrómico')
    hb_ = [s.shape(1.3 + (k % 3) * 0.45, 1.9 + (k // 3) * 0.5, 0.28, 0.28, 'diamond', '922B21', None, False, name='Hb punto %d' % k) for k in range(6)]
    hcm = caja(s, 0.5, 4.5, 4.1, 2.55, '**HCM**: cantidad promedio de Hb **dentro de cada** eritrocito. Unidad: **picogramos (pg)**. Normal **27–32 pg**; < 27 → **hipocrómica** (pálida); > 32 → hipercrómica (rara).',
              ROSA, 14, name='Def HCM')
    ch = caja(s, 4.85, 4.5, 4.0, 2.55, '**CHCM**: concentración de Hb **en relación al volumen** del eritrocito (g de Hb por dL de eritrocitos). Normal **32–36 g/dL**.', CREMA, 14.5,
              name='Def CHCM')
    dif = caja(s, 9.35, 1.2, 3.7, 3.0, 'Diferencia clave: el **HCM expresa gramos**; el **CHCM relaciona gramos con volumen**.', AMA, 16, head='Diferencia', name='Diferencia HCM CHCM')
    m = molecula3d(s, 10.2, 4.5, 2.2, 'hemo', name='Hemo deco')
    s.step(fade(a), fade(al, after=True), *[fade(h, after=(k == 0)) for k, h in enumerate(hb_)])
    s.step(fade(b), fade(bl, after=True), fade(hcm, after=True))
    s.step(fade(ch))
    s.step(fade(dif), fade(m, after=True))


def esferocitosis(D):
    s = nueva(D, 3, 'CHCM elevada: el caso de la esferocitosis hereditaria', src=['AN 4.3 CHCM', 'REV AN 4.3'], tipo='izq', c1=ROSA, c2=BLANCO)
    d1 = eritrocito(s, 0.6, 1.4, 2.4, 'normal', name='!!Eritrocito disco')
    p1 = eritrocito_perfil(s, 0.5, 4.1, 2.6, name='Perfil disco')
    d2 = eritrocito(s, 3.0, 4.0, 1.6, 'esfero', name='!!Esferocito')
    lb = rotulo(s, 2.85, 5.75, 'esferocito', ROJO, 14, w=1.9, name='Rótulo esferocito')
    c1 = caja(s, 5.0, 1.2, 8.05, 1.6, 'En la **esferocitosis hereditaria** los eritrocitos son **esféricos** en lugar de discos bicóncavos.', AMA, 17, anchor='m', name='Esfera')
    c2 = caja(s, 5.0, 3.0, 8.05, 1.7, 'Al ser esféricos tienen **menor volumen**: la misma cantidad de Hb queda **concentrada en menos espacio** → **CHCM aumentada**. Además, mayor **fragilidad osmótica**.',
              BLANCO, 16, name='Mecanismo esfero')
    r_ = rigor(s, 5.0, 4.95, 8.05, 2.1, 'La CHCM elevada es el hallazgo **clásico** de la esferocitosis, pero **no exclusivo**: también aparece en otras situaciones (p. ej., ciertas hemoglobinopatías, aglutininas frías o '
               'interferencias como la lipemia). No conviene usarla como regla absoluta.', 13.5, name='Rigor CHCM')
    s.step(fade(d1), fade(p1, after=True))
    s.step(fade(d2), fade(lb, after=True), fade(c1, after=True))
    s.step(fade(c2))
    s.step(fade(r_))


def rdw(D):
    s = nueva(D, 3, 'RDW: la dispersión del tamaño eritrocitario', src=['AN 4.4 RDW'], tipo='der', c1=ROJO, c2=ROSA)
    X, Y, W, H = 0.7, 1.4, 7.9, 3.0
    ej = ejes(s, X, Y, W, H, 'volumen eritrocitario', 'n.º de células', name='Ejes RDW')
    ang = curva(s, X, Y, W, H, gauss_path(480, 70, 1000, 80), VERDE_OSC, 4.5, name='Curva angosta')
    anc = curva(s, X, Y, W, H, [(p[0], int(1000 - (1000 - p[1]) * 0.55)) for p in gauss_path(500, 200, 1000, 80)], ROJO, 4.5, name='Curva ancha')
    hom = s.group_start('Homogénea')
    for k in range(5):
        eritrocito(s, 0.8 + k * 0.75, 5.05, 0.62, name='GR hom %d' % k)
    s.group_end()
    het = s.group_start('Heterogénea')
    for k, d in enumerate((0.42, 0.9, 0.55, 1.05, 0.48)):
        eritrocito(s, 4.9 + k * 0.78, 5.0 + (1.0 - d) / 2, d, 'normal' if k % 2 else 'hipo', name='GR het %d' % k)
    s.group_end()
    l1 = rotulo(s, 0.8, 6.15, 'RDW normal → homogénea', 'D5F5E3', 14, w=3.6, name='Rótulo homogénea')
    l2 = rotulo(s, 4.9, 6.15, 'RDW elevado → anisocitosis', ROSA, 14, w=3.8, name='Rótulo heterogénea')
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Mide la **variabilidad** del tamaño de los glóbulos rojos: índice estadístico de dispersión (coeficiente de variación). Normal **12–14 %**.', BLANCO, 15,
             head='Definición', name='Def RDW')
    c2 = caja(s, 9.35, 4.85, 3.7, 2.2, 'Curva **angosta**: tamaños similares. Curva **amplia**: coexisten eritrocitos muy grandes y muy pequeños.', AMA, 14.5, name='Curvas RDW')
    s.step(fade(ej), fade(c, after=True))
    s.step(wipe(ang, 'l'), fade(hom, after=True), fade(l1, after=True))
    s.step(wipe(anc, 'l'), fade(het, after=True), fade(l2, after=True))
    s.step(fade(c2))


def hematocrito(D):
    s = nueva(D, 3, 'Hematocrito: porcentaje de la sangre ocupado por eritrocitos', src=['AN 4.6 El hematocrito', 'REV AN 4.6'], tipo='bandas', c1=CREMA, c2=ROSA)
    cap = s.group_start('!!Capilar de vidrio')
    s.shape(1.4, 1.3, 0.55, 5.4, 'roundRect', ('a', 'EAF2FA', 60), ('5D6D7E', 1.5), False, adj={'adj': 50000})
    s.shape(1.45, 4.3, 0.45, 2.3, 'rect', ('lin', [(0, 'E57373'), (100, '922B21')], 0), None, False)
    s.shape(1.45, 2.3, 0.45, 2.0, 'rect', ('lin', [(0, 'FCF3CF'), (100, 'F9E79F')], 0), None, False)
    s.shape(1.35, 6.45, 0.65, 0.35, 'rect', '7F8C8D', (INK, 1.0), False)
    s.group_end()
    reg = s.group_start('Regla de lectura')
    for k in range(11):
        y = 6.6 - k * 0.43
        s.arrow([(2.1, y), (2.4 if k % 5 == 0 else 2.25, y)], INK, 1.25, tail=None)
        if k % 5 == 0:
            texto(s, 2.45, y - 0.17, 0.7, 0.34, '%d %%' % (k * 10), 12, INK, True)
    s.group_end()
    l = rotulo(s, 0.35, 4.0, '~45 %', ROJO, 16, w=0.95, name='Rótulo 45')
    c1 = caja(s, 3.55, 1.2, 6.5, 1.7, 'Porcentaje de la sangre total que corresponde a los glóbulos rojos (**~45 %**).', AMA, 17, anchor='m', name='Def Hto')
    c2 = caja(s, 3.55, 3.1, 6.5, 1.9, '**Gold standard**: capilar de vidrio centrifugado. La sangre asciende por capilaridad, se sella el extremo, se centrifuga a alta velocidad y se mide la columna de eritrocitos.',
              BLANCO, 15, name='Gold standard')
    c3 = caja(s, 3.55, 5.2, 6.5, 1.85, 'Cálculo del equipo: **Hto = recuento de eritrocitos × VCM** (con un factor según las unidades).\nRegla práctica: **Hto ≈ Hb × 3**.', CELESTE, 15,
              name='Cálculo Hto')
    r_ = rigor(s, 10.3, 1.2, 2.75, 5.85, 'Con eritrocitos en millones/µL y VCM en fL: **Hto (%) = GR × VCM / 10** (p. ej., 4,5 × 90 / 10 = 40,5 %). El divisor depende de las unidades usadas.',
               13, name='Rigor fórmula Hto')
    s.step(fade(cap), fade(reg, after=True), fade(l, after=True))
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(c3))
    s.step(fade(r_))


def resumen_indices(D):
    s = nueva(D, 3, 'Resumen de los índices hematimétricos', src=['AN 4.5 Resumen de índices'], tipo='izq', c1=ROSA, c2=BLANCO)
    rows = [['Índice', 'Valor normal', '↓ Disminuido', '↑ Aumentado'], ['VCM', '80–100 fL', 'Microcítica', 'Macrocítica'], ['HCM', '27–32 pg', 'Hipocrómica', 'Hipercrómica (rara)'],
            ['CHCM', '32–36 g/dL', 'Hipocrómica', 'Esferocitosis hereditaria (hallazgo clásico)'], ['RDW', '12–14 %', 'Sin relevancia clínica', 'Anemia heterogénea / anisocitosis']]
    ids, H = tabla_filas(s, 4.95, 1.25, [1.4, 1.9, 2.3, 2.5], rows, rowh=0.95, size=16, name='Tabla índices')
    gr = s.group_start('Eritrocitos resumen')
    eritrocito(s, 0.5, 1.5, 1.1, 'hipo', name='GR r1'); eritrocito(s, 1.8, 1.4, 1.45, name='GR r2'); eritrocito(s, 3.35, 1.3, 1.25, 'esfero', name='GR r3')
    eritrocito_perfil(s, 0.6, 3.3, 3.5, name='Perfil r')
    s.group_end()
    c = caja(s, 0.4, 5.2, 4.3, 1.85, 'Tamaño (**VCM**), contenido (**HCM**), concentración (**CHCM**) y dispersión (**RDW**).', AMA, 15.5, name='Cuatro preguntas')
    s.step(fade(gr), fade(ids[0], after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))


# ---------------------------------------------------------------- clasificación morfológica
def morfologica(D):
    s = nueva(D, 3, 'Clasificación morfológica: comparación a escala', src=['AN 5 Clasificación morfológica'], tipo='der', c1=ROJO, c2=ROSA)
    data = [('Microcítica hipocrómica', 'VCM < 80 fL · HCM < 27 pg', 1.35, 'hipo', CELESTE, 'Síntesis **deficiente de hemoglobina**'),
            ('Normocítica normocrómica', 'VCM 80–100 fL', 1.75, 'normal', 'D5F5E3', 'Tamaño normal; menos eritrocitos o menos Hb'),
            ('Macrocítica', 'VCM > 100 fL', 2.25, 'normal', ROSA, '**Maduración nuclear** defectuosa')]
    ids = []
    for k, (t, v, d, kd, f, m) in enumerate(data):
        x = 0.4 + k * 2.95
        g = s.group_start('Morfología %d' % k)
        caja(s, x, 1.2, 2.8, 5.85, '', BLANCO, 12, lw=2.0)
        eritrocito(s, x + 1.4 - d / 2, 2.8 - d / 2, d, kd, name='GR morf %d' % k)
        rotulo(s, x + 0.1, 4.15, t, f, 13.5, w=2.6, h=0.8)
        texto(s, x + 0.1, 5.05, 2.6, 0.5, v, 14, INK, True, 'c')
        texto(s, x + 0.15, 5.6, 2.5, 1.3, m, 14.5, INK, False, 'c')
        s.group_end(); ids.append(g)
    esc = rotulo(s, 0.5, 1.35, 'misma escala', NAVY, 12, name='Rótulo escala')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Se basa en el **tamaño** (VCM) y el **contenido de Hb** (HCM): cada categoría sugiere un **mecanismo** y un estudio siguiente.', BLANCO, 15,
             head='Criterio', name='Criterio morfológico')
    for g in ids:
        s.step(fade(g))
    s.step(fade(esc), fade(c, after=True))


def microciticas(D):
    s = nueva(D, 3, 'Anemias microcíticas: la guía es el hierro', src=['AN 5.1 Anemias microcíticas'], tipo='bandas', c1=ROSA, c2=CELESTE)
    top = caja(s, 3.55, 1.2, 6.5, 1.0, 'VCM < 80 fL · HCM < 27 pg → síntesis **deficiente de hemoglobina**', AMA, 16, align='c', anchor='m', name='Microcítica raíz')
    fe = rotulo(s, 5.55, 2.55, 'Ferremia', NAVY, 18, w=2.5, h=0.65, name='Ferremia')
    ram = []
    for k, (t, d, f, x) in enumerate((('Baja', '**Anemia ferropénica**: deficiencia de hierro; la más frecuente del mundo.', CELESTE, 3.55),
                                      ('Normal', '**Talasemia**: defecto genético en la síntesis de cadenas de globina.', CREMA, 5.75),
                                      ('Alta', '**Anemia sideroblástica**: falla en la incorporación del hierro al hemo.', ROSA, 7.95))):
        g = s.group_start('Rama ' + t)
        s.arrow([(6.8, 3.25), (x + 1.05, 3.85)], INK, 2.5)
        rotulo(s, x + 0.25, 3.9, t, [AZUL, AMA2, ROJO][k], 15, w=1.6)
        caja(s, x, 4.5, 2.1, 2.55, d, f, 14)
        ram.append(s.group_end())
    gr = s.group_start('GR microcíticos')
    for k in range(6):
        eritrocito(s, 0.45 + (k % 2) * 1.35, 1.4 + (k // 2) * 1.6, 1.0, 'hipo', name='GR micro %d' % k)
    s.group_end()
    tal = caja(s, 10.3, 1.2, 2.75, 5.85, '**Talasemia**: defectos en los genes de las cadenas **alfa o beta**. Muy prevalente en La Rioja; muchas personas no lo saben.', BLANCO, 14.5,
               name='Nota talasemia')
    s.step(fade(gr), fade(top, after=True))
    s.step(zoom(fe))
    for g in ram:
        s.step(fade(g))
    s.step(fade(tal))


def macro_normo(D):
    s = nueva(D, 3, 'Anemias macrocíticas y normocíticas', src=['AN 5.2 Anemias macrocíticas', 'AN 5.3 Anemias normocíticas'], tipo='izq', c1=ROSA, c2=BLANCO)
    ma = s.group_start('Rama macrocítica')
    caja(s, 0.4, 1.2, 6.05, 1.35, '**Macrocítica** (VCM > 100 fL): **maduración nuclear defectuosa**; déficit de cofactores de la síntesis de ADN (B_{12} y ácido fólico).', ROSA, 14.5)
    s.arrow([(1.9, 2.6), (1.9, 3.0)], INK, 2.5); s.arrow([(5.0, 2.6), (5.0, 3.0)], INK, 2.5)
    caja(s, 0.4, 3.05, 3.0, 2.0, '**Con megaloblastos**: déficit de B_{12} o ácido fólico → anemia **megaloblástica / perniciosa**.', 'FDEBD0', 14)
    caja(s, 3.55, 3.05, 2.9, 2.0, '**Sin megaloblastos**: hipotiroidismo, hepatopatías, alcoholismo, drogas.', CREMA, 14)
    s.group_end()
    mg = megaloblasto(s, 1.6, 5.3, 1.6, name='Megaloblasto rama')
    no = s.group_start('Rama normocítica')
    caja(s, 6.85, 1.2, 6.2, 1.35, '**Normocítica** (VCM 80–100 fL): tamaño normal; disminución del número o de la Hb. Clave: **reticulocitos**.', 'D5F5E3', 14.5)
    s.arrow([(8.4, 2.6), (8.4, 3.0)], INK, 2.5); s.arrow([(11.5, 2.6), (11.5, 3.0)], INK, 2.5)
    caja(s, 6.85, 3.05, 3.0, 2.0, 'Reticulocitos **aumentados**: hemorragia aguda o hemólisis → **regenerativa**.', 'EAF5EA', 14)
    caja(s, 10.0, 3.05, 3.05, 2.0, 'Reticulocitos **normales/bajos**: insuficiencia renal, enfermedad crónica, falla medular → **arregenerativa**.', ROSA, 14)
    s.group_end()
    rt = reticulocito(s, 8.5, 5.3, 1.5, name='Reticulocito rama')
    c = caja(s, 3.4, 5.35, 4.8, 1.7, 'El VCM decide la rama; luego el **dato bioquímico** (megaloblastos, reticulocitos) afina el diagnóstico.', AMA, 15, name='Síntesis ramas')
    s.step(fade(ma), fade(mg, after=True))
    s.step(fade(no), fade(rt, after=True))
    s.step(fade(c))


def reticulocitos(D):
    s = nueva(D, 3, 'Reticulocitos: la respuesta de la médula', src=['AN 6.1 Los Reticulocitos'], tipo='der', c1=ROJO, c2=BLANCO)
    mo = medula_osea(s, 0.3, 1.3, 4.0, 3.0, name='!!MedulaOsea', celulas=12)
    vas = vessel(s, 4.9, 2.3, 4.0, 1.0, name='!!Vaso sanguíneo', rbcs=3)
    rt = reticulocito(s, 3.0, 2.3, 0.85, name='!!Reticulocito')
    c1 = caja(s, 0.3, 4.6, 4.3, 2.45, 'Eritrocitos **inmaduros** que aún contienen **ARN ribosómico** y material genético residual (coloraciones especiales). Estadio previo al eritrocito maduro.',
              BLANCO, 14.5, name='Def reticulocito')
    rows = [['Grupo', 'Reticulocitos'], ['Adultos', '0,5 – 2 %'], ['Niños y jóvenes', '0,5 – 2,2 %'], ['Recién nacidos', '2,5 – 6 %']]
    ids, H = tabla_filas(s, 4.85, 3.65, [2.3, 1.75], rows, rowh=0.5, size=15, name='Tabla reticulocitos')
    t = caja(s, 4.85, 3.85 + H, 4.05, 6.95 - (3.85 + H), 'Maduración normal: **3,5 días**. En la anemia la médula la acelera y libera reticulocitos en **1–2 días**.', AMA, 14, name='Maduración')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.3, 'El **porcentaje de reticulocitos** en sangre periférica indica si la **médula responde** ante la anemia o si el problema reside en ella.', BLANCO, 15,
              head='Parámetro clave', name='Clave reticulocitos')
    c3 = caja(s, 9.35, 4.75, 3.7, 2.3, 'En el recién nacido el estrés oxidativo del nacimiento genera hemólisis fisiológica: más reticulocitos.', CREMA, 14, name='RN reticulocitos')
    s.step(fade(mo), fade(vas, after=True))
    s.step(zoom(rt), path(rt, 2.3, 0.05, after=True, dur=900), fade(c1, after=True))
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids)])
    s.step(fade(t))
    s.step(fade(c2))
    s.step(fade(c3))


def regla_retis(D):
    s = nueva(D, 3, 'Regenerativa o arregenerativa: la regla de los reticulocitos', src=['AN 6.1 Regla fundamental', 'AN 6 Clasificación etiopatogénica'], tipo='bandas', c1='EAF5EA', c2=ROSA)
    a = s.group_start('Médula que responde')
    medula_osea(s, 0.35, 1.3, 3.0, 2.2, name='Médula activa', celulas=18, seed=4)
    for k in range(4):
        reticulocito(s, 0.5 + k * 0.7, 3.7, 0.6, name='Reti salida %d' % k)
    s.group_end()
    b = s.group_start('Médula que no responde')
    medula_osea(s, 10.05, 1.3, 3.0, 2.2, name='Médula inactiva', celulas=5, seed=6)
    reticulocito(s, 11.2, 3.7, 0.6, name='Reti escaso')
    s.group_end()
    ra = caja(s, 3.55, 1.2, 3.1, 3.1, '**Reticulocitos > 2 %** → anemia **REGENERATIVA**: la médula responde enviando eritrocitos inmaduros.', 'EAF5EA', 15.5, name='Regenerativa regla')
    rb = caja(s, 6.85, 1.2, 3.0, 3.1, '**Reticulocitos 0,5–2 %** → anemia **ARREGENERATIVA**: la médula no responde; el problema es **central**.', ROSA, 15.5, name='Arregenerativa regla')
    p = perla(s, 0.35, 4.75, 12.7, 1.4, 'En la arregenerativa, que los reticulocitos estén «normales» **es el hallazgo patológico**: la médula debería aumentar su producción y no lo hace.', 16,
              head='Importante')
    t = caja(s, 0.35, 6.3, 12.7, 0.75, 'Periféricas (regenerativas): hemorragia y hemólisis · Centrales (arregenerativas): stem cell, desplazamiento, déficit de factores.', AMA, 14.5, anchor='m',
             name='Resumen periférica central')
    s.step(fade(a), fade(ra, after=True))
    s.step(fade(b), fade(rb, after=True))
    s.step(fade(p))
    s.step(fade(t))


def regenerativas(D):
    s = nueva(D, 3, 'Anemias regenerativas (periféricas)', src=['AN 6.2 Anemias regenerativas'], tipo='der', c1=ROJO, c2=ROSA)
    vas = vessel(s, 0.4, 1.4, 8.4, 1.1, name='!!Vaso sanguíneo', rbcs=9)
    gota = s.group_start('Hemorragia')
    for k in range(3):
        s.shape(2.0 + k * 0.4, 2.6 + k * 0.35, 0.3, 0.42, 'teardrop', 'B3261E', ('6E1A12', 1.0), False, rot=135)
    s.group_end()
    frag = s.group_start('Hemólisis')
    for k in range(5):
        s.shape(6.0 + (k % 3) * 0.4, 2.65 + (k // 3) * 0.35, 0.3, 0.2, 'ellipse', 'C0392B', ('6E1A12', 0.75), False)
    s.group_end()
    h = caja(s, 0.4, 3.75, 4.0, 3.3, '**Causa 1 — Hemorragia**: pérdida de sangre por traumatismo o herida, interna o externa; **aguda o crónica**.', ROSA, 15, head='Pérdida', headfill=ROJO,
             name='Hemorragia caja')
    hm = caja(s, 4.75, 3.75, 4.05, 3.3, '**Causa 2 — Hemólisis**: destrucción anormal en la periferia.\n- **Corpuscular**: membranopatías, enzimopatías, hemoglobinopatías.\n- **Extracorpuscular**: tóxicos, infecciones, mecánicas, autoinmunes.',
              CREMA, 13.5, head='Destrucción', name='Hemólisis caja')
    c = caja(s, 9.35, 1.2, 3.7, 5.85, 'La causa es **externa a la médula**: esta produce eritrocitos normalmente, pero se **pierden o destruyen** en la periferia.', BLANCO, 15.5, head='Periféricas',
             name='Def periféricas')
    s.step(fade(vas), fade(c, after=True))
    s.step(fade(gota), fade(h, after=True))
    s.step(fade(frag), fade(hm, after=True))


def arregenerativas(D):
    s = nueva(D, 3, 'Anemias arregenerativas (centrales)', src=['AN 6.3 Anemias arregenerativas'], tipo='izq', c1=ROSA, c2=BLANCO)
    cols = [('A · Stem cell hematopoyética', '- Aplasia medular global (pancitopenia)\n- Aplasias selectivas puras\n- Diseritropoyesis y síndrome mielodisplásico\n- Leucemias', LAVANDA),
            ('B · Desplazamiento de líneas', '- Carcinoma mamario con metástasis medular\n- Mieloma múltiple\n- Linfomas y leucemias\n- Infecciones crónicas severas', CREMA),
            ('C · Déficit de factores', '- Ferropenia → microcítica hipocrómica\n- Déficit de B_{12} / ácido fólico → macrocítica megaloblástica\n- Anemia perniciosa (factor intrínseco)\n- Procesos inflamatorios crónicos\n- IRC: menos eritropoyetina', ROSA)]
    ids = []
    for k, (t, d, f) in enumerate(cols):
        ids.append(caja(s, 0.4 + k * 4.25, 3.2, 4.05, 3.85, d, f, 14, head=t, name='Grupo arregenerativa %d' % k))
    mo = medula_osea(s, 0.4, 1.15, 5.5, 1.85, name='!!MedulaOsea', celulas=10)
    k_ = kidney(s, 6.4, 1.1, 0.95, name='Riñón EPO')
    ep = rotulo(s, 7.5, 1.6, 'EPO ↓', ROJO, 15, name='EPO baja')
    c = caja(s, 8.9, 1.15, 4.15, 1.85, 'El problema está **en la médula** o en los **factores** que necesita la eritropoyesis.', AMA, 15, name='Def centrales')
    s.step(fade(mo), fade(c, after=True))
    for g in ids[:2]:
        s.step(fade(g))
    s.step(fade(ids[2]), fade(k_, after=True), fade(ep, after=True))


def tabla_anemias(D):
    """tabla de anemias construida por columnas (cinco clics)"""
    s = nueva(D, 3, 'Tabla integradora de las anemias', src=['AN 12 Cuadro resumen'], tipo='der', c1=ROJO, c2=BLANCO)
    x0, y0 = 0.35, 1.2
    cats = ['Microcítica hipocrómica', 'Macrocítica (megaloblástica)', 'Normocítica regenerativa', 'Normocítica arregenerativa']
    colw = [2.35, 1.35, 1.75, 1.6, 1.85]
    rh = 1.25
    heads = ['Tipo', 'VCM (fL)', 'Problema central', 'Reticulocitos', 'Causas']
    data = [['< 80', 'Síntesis de Hb baja', 'Variables', 'Ferropenia, talasemia, sideroblástica'],
            ['> 100', 'Síntesis de ADN alterada', 'Bajos (arregenerativa)', 'Déficit B_{12}, ácido fólico, perniciosa'],
            ['80–100', 'Pérdida o destrucción', 'Elevados', 'Hemorragia aguda, hemólisis'],
            ['80–100', 'Falla medular o crónica', 'Normales', 'IR, enfermedad crónica, aplasia']]
    fills = [CELESTE, ROSA, 'EAF5EA', CREMA]
    cols = []
    x = x0
    for c in range(5):
        g = s.group_start('Columna %s' % heads[c])
        s.shape(x, y0, colw[c], 0.7, 'rect', NAVY, (INK, 1.25), False, heads[c], 14, F_HEAD, BLANCO, True, 'c', 'm', (0.05, 0, 0.05, 0))
        for r in range(4):
            txt = cats[r] if c == 0 else data[r][c - 1]
            s.shape(x, y0 + 0.7 + r * rh, colw[c], rh, 'rect', fills[r], (INK, 1.25), False, txt, 14 if c != 0 else 14.5, F_BODY, INK, c == 0, 'l', 'm',
                    (0.08, 0.03, 0.08, 0.03), minsize=11)
        cols.append(s.group_end())
        x += colw[c]
    gr = s.group_start('Eritrocitos tabla')
    eritrocito(s, 9.6, 1.4, 0.8, 'hipo', name='GR t1'); eritrocito(s, 10.6, 1.25, 1.15, name='GR t2'); reticulocito(s, 11.95, 1.35, 0.95, name='Reti t')
    s.group_end()
    c = caja(s, 9.35, 2.6, 3.7, 4.45, 'Leé por filas: el **tamaño** propone un mecanismo, la **Hb** lo confirma y los **reticulocitos** dicen si la médula responde.', AMA, 15.5,
             head='Interpretación', name='Interpretación tabla')
    note = s.group_start('Pie tabla')
    texto(s, 0.35, y0 + 0.75 + 4 * rh + 0.05, 8.9, 0.4, 'Color (HCM): la microcítica es hipocrómica; las demás, en general, normocrómicas.', 13.5, '5D6D7E', True)
    s.group_end()
    s.step(fade(cols[0]), fade(gr, after=True))            # 1 categorías
    s.step(wipe(cols[1], 'l'))                             # 2 tamaño
    s.step(wipe(cols[2], 'l'), fade(note, after=True))     # 3 color / concentración de Hb
    s.step(wipe(cols[3], 'l'))                             # 4 respuesta reticulocitaria
    s.step(wipe(cols[4], 'l'), fade(c, after=True))        # 5 interpretación


def build(D):
    divisor_u3(D)
    definicion(D)
    por_que_hb(D)
    valores_hb(D)
    volumen_plasmatico(D)
    otras_condiciones(D)
    instalacion(D)
    manifestaciones(D, 1)
    manifestaciones(D, 2)
    severidad(D)
    contador(D)
    vcm(D)
    hcm_chcm(D)
    esferocitosis(D)
    rdw(D)
    hematocrito(D)
    resumen_indices(D)
    morfologica(D)
    microciticas(D)
    macro_normo(D)
    reticulocitos(D)
    regla_retis(D)
    regenerativas(D)
    arregenerativas(D)
    tabla_anemias(D)
