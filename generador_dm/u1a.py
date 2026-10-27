# -*- coding: utf-8 -*-
"""UNIDAD I (a) — Definición, clasificación, DM1/DM2, biosíntesis de insulina"""
from base import *

U = 1


def div(D):
    def art(s):
        model(s, 'glucosa', 10.75, 0.6, 2.3, name='Glucosa 3D')
        s.pic('langerhans-islet-pancreas', 10.6, 3.0, 2.5, name='Islote')
        s.pic('pancreas', 0.1, 5.3, 2.4, name='Páncreas')
        model(s, 'g6p', 0.2, 1.4, 2.2, hs=False, name='G6P 3D', label='Glucosa-6-P')
    divider(D, U, 'I', 'BASES BIOQUÍMICAS\nDE LA DIABETES', 'Insulina, señalización y metabolismo intermedio',
            ['Definición y clasificación', 'Biosíntesis y secreción de insulina', 'Receptor e IRS–PI3K–Akt / Ras–MAPK',
             'Hormonas contrarreguladoras', 'Estado alimentado, ayuno y déficit de insulina', 'Diagnóstico y HbA1c',
             'Glucotoxicidad, AGE/RAGE y complicaciones'], art,
            'Unidad I. Construye el lenguaje molecular necesario para entender los tres casos clínicos: qué es la diabetes, '
            'cómo se fabrica y se secreta la insulina, cómo transduce su señal, qué hormonas se le oponen, cómo cambia el '
            'metabolismo de cada órgano entre la comida y el ayuno, cómo se diagnostica y por qué la hiperglucemia crónica daña '
            'vasos y nervios.')


def definition(D):
    s = new(D, U, 'Diabetes mellitus: definición')
    s.pic('pancreas', 0.5, 1.35, 3.6, name='Páncreas def')
    hyp = mbox(s, 4.75, 1.3, 3.8, 0.85, 'HIPERGLUCEMIA CRÓNICA', 'y', 22, name='Hiperglucemia crónica')
    a = mbox(s, 0.5, 3.35, 3.7, 0.95, 'Deficiencia en la SECRECIÓN de insulina', 's', 16, caps=False)
    b = mbox(s, 4.8, 3.35, 3.7, 0.95, 'Disminución de su ACCIÓN en tejidos diana', 's', 16, caps=False)
    c = mbox(s, 9.1, 3.35, 3.7, 0.95, 'Ambas (lo más frecuente en DM2)', 's', 16, caps=False)
    ea = s.arrow([(2.35, 3.3), (5.2, 2.2)], INK, 2.5); eb = s.arrow([(6.65, 3.3), (6.65, 2.2)], INK, 2.5); ec = s.arrow([(10.9, 3.3), (8.1, 2.2)], INK, 2.5)
    met = tbox(s, 0.5, 4.75, 6.2, 1.75, 'La hiperglucemia prolongada modifica el metabolismo de **carbohidratos, lípidos y proteínas**. '
               'No equivale a una única etiología: es un **conjunto heterogéneo** de enfermedades.', 16, head='Consecuencia metabólica')
    org = s.group_start('Órganos blanco')
    for i, (img, t) in enumerate([('diabetic-retinopathy-eye', 'Retina'), ('kidney-1', 'Riñón'), ('Pyramidal_Neuron', 'Nervios'),
                                  ('heart-front', 'Corazón'), ('vein-crossection-3d', 'Vasos')]):
        fitpic(s, img, 7.0 + i * 1.2, 4.85, 1.05, 1.15)
        lab(s, 7.0 + i * 1.2, 6.05, 1.05, 0.35, t, 12.5)
    s.group_end()
    s.step(zoom(hyp))
    s.step(wipe(ea, 'b'), fade(a, after=True), wipe(eb, 'b'), fade(b, after=True), wipe(ec, 'b'), fade(c, after=True))
    s.step(fade(met), fade(org, after=True))
    s.note('Definición [ADA 2026]: la diabetes mellitus es un conjunto heterogéneo de enfermedades metabólicas caracterizadas '
           'por hiperglucemia crónica, originada por deficiencia en la secreción de insulina, disminución de su acción en los '
           'tejidos diana o ambas. La hiperglucemia prolongada altera el metabolismo de carbohidratos, lípidos y proteínas y daña '
           'vasos, retina, riñones, nervios y corazón. Animación: primero el eje común (hiperglucemia crónica), luego los tres '
           'mecanismos que pueden originarla y finalmente sus consecuencias en órganos blanco.')


def classification(D):
    s = new(D, U, 'Clasificación: cuatro grandes grupos')
    cards = [
        ('DM1', 'langerhans-islet-pancreas', 'Destrucción **autoinmunitaria** de células β (anti-GAD65, IA-2, ZnT8, antiinsulina). Déficit insulínico **marcado o absoluto**; riesgo de cetogénesis **elevado**. Cualquier edad.', 'y'),
        ('DM2', 'obese-man', '**Resistencia** a la insulina (hígado, músculo, adiposo) + **incapacidad progresiva** de células β para compensarla. Al comienzo puede haber hiperinsulinemia.', 's'),
        ('GESTACIONAL', 'excess-weight-male-clothed', 'Hiperglucemia diagnosticada por primera vez en el **2.º o 3.er trimestre**, sin diabetes manifiesta previa. Mediadores placentarios aumentan la resistencia insulínica.', 'g'),
        ('OTROS TIPOS', 'pancreas-2', '**Monogénica** (MODY, neonatal) · **páncreas exocrino** (pancreatitis, fibrosis quística, pancreatectomía) · **endocrinopatías** (Cushing, acromegalia, glucagonoma) · **fármacos** (glucocorticoides, inmunosupresores, antipsicóticos).', 'b'),
    ]
    ids = []
    for i, (h, img, t, k) in enumerate(cards):
        x = 0.4 + i * 3.17
        g = s.group_start('Tipo ' + h)
        mbox(s, x, 1.25, 3.0, 0.62, h, k, 20)
        if img != 'excess-weight-male-clothed':
            fitpic(s, img, x + 0.4, 1.95, 2.2, 1.55)
        else:
            mbox(s, x + 0.35, 2.0, 2.3, 0.55, 'Placenta: mediadores', 's', 13, caps=False)
            s.arrow([(x + 1.5, 2.6), (x + 1.5, 2.9)], INK, 2.5)
            mbox(s, x + 0.35, 2.95, 2.3, 0.55, 'Resistencia insulínica ↑', 'g', 13, caps=False)
        tbox(s, x, 3.6, 3.0, 2.75, t, 14.5)
        ids.append(s.group_end())
    p = pearl(s, 0.4, 6.5, 12.55, 0.6, 'Distinguir de la **hiperglucemia transitoria por estrés agudo**, que no es diabetes por sí misma.', 14.5)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Clasificación [ADA 2026]. DM1: en la mayoría, destrucción autoinmunitaria de células β con autoanticuerpos anti-GAD65, '
           'IA-2, ZnT8 y, en ciertos contextos, antiinsulina; déficit marcado o absoluto de insulina; una minoría corresponde a '
           'otras formas de déficit grave no necesariamente autoinmunes. DM2: interacción de resistencia insulínica hepática, '
           'muscular y adiposa con incapacidad progresiva de la célula β; la obesidad visceral suele contribuir, pero existe DM2 '
           'sin obesidad. Gestacional: hiperglucemia detectada por primera vez en el segundo o tercer trimestre; la resistencia '
           'insulínica aumenta por mediadores placentarios y puede desenmascarar disfunción β. Otros tipos específicos: '
           'monogénicos, enfermedad del páncreas exocrino, endocrinopatías, fármacos, síndromes genéticos e infecciones. Deben '
           'diferenciarse de la hiperglucemia transitoria por estrés agudo.')


def dm1(D):
    s = new(D, U, 'DM1: destrucción autoinmunitaria de células β')
    isl = fitpic(s, 'langerhans-islet-pancreas', 0.45, 1.2, 3.3, 3.4, name='Islote DM1')
    # linfocitos atacando
    tc = []
    for i, (x, y) in enumerate([(3.7, 1.55), (3.9, 2.6), (3.55, 3.65), (0.25, 3.3)]):
        tc.append(sphere(s, x, y, 0.55, '6C3483', name='Linfocito T %d' % i, text='LT', size=11))
    ab = s.group_start('Autoanticuerpos')
    for i, t in enumerate(['Anti-GAD65', 'Anti-IA-2', 'Anti-ZnT8', 'Antiinsulina']):
        mbox(s, 0.45 + (i % 2) * 1.85, 5.15 + (i // 2) * 0.62, 1.75, 0.52, t, 'g', 13.5, caps=False)
    s.group_end()
    lab(s, 0.45, 4.75, 3.6, 0.38, 'MARCADORES DE AUTOINMUNIDAD', 13)
    # estadios: masa β
    st = []
    data = [('Estadio 1', 'Autoinmunidad\n≥2 autoanticuerpos\nnormoglucemia', 0.85, 'g'), ('Estadio 2', 'Autoinmunidad\ndisglucemia\npresintomática', 0.55, 'y'),
            ('Estadio 3', 'Diabetes clínica\nsíntomas\nriesgo de CAD', 0.2, 'r')]
    lab(s, 5.0, 1.2, 7.9, 0.4, 'MASA FUNCIONAL DE CÉLULAS β A LO LARGO DEL TIEMPO', 14)
    for i, (h, t, frac, k) in enumerate(data):
        x = 5.2 + i * 2.65
        g = s.group_start(h)
        s.shape(x + 0.55, 1.75 + 3.0 * (1 - frac), 1.3, 3.0 * frac, 'rect', ('lin', [(0, '5DADE2'), (100, '1F618D')], 90), (INK, 1.5), SHD,
                '%d %%' % int(frac * 100) if False else None)
        mbox(s, x, 4.85, 2.4, 0.5, h, k, 15)
        tbox(s, x, 5.45, 2.4, 1.3, t, 13.5, anchor='m')
        st.append(s.group_end())
    ax = s.arrow([(5.05, 4.8), (5.05, 1.7)], INK, 2.0)
    s.step(*[fade(t, after=i > 0, dur=300) for i, t in enumerate(tc)])
    s.step(fade(ab))
    for g in st:
        s.step(fade(g))
    s.note('DM1. La mayor parte de los casos se debe a destrucción autoinmunitaria de las células β pancreáticas mediada por '
           'linfocitos T; los autoanticuerpos (anti-GAD65, IA-2, ZnT8 y antiinsulina) son marcadores de ese proceso. La pérdida '
           'secretora es progresiva: la etapificación moderna reconoce un estadio 1 de autoinmunidad con normoglucemia, un estadio '
           '2 de disglucemia presintomática y un estadio 3 de diabetes clínica. El resultado final es un déficit insulínico '
           'marcado o absoluto: el riesgo de cetogénesis es elevado. Puede presentarse a cualquier edad. Las barras son un '
           'esquema conceptual de la masa funcional β, no valores medidos.')


def dm2(D):
    s = new(D, U, 'DM2: resistencia insulínica + fracaso β progresivo')
    cid = chart_line(s, 0.45, 1.2, 7.3, 4.6, ['Normal', 'Resistencia\ncompensada', 'Prediabetes', 'DM2\ninicial', 'DM2\navanzada'],
                     [('Secreción de insulina', [1.0, 2.1, 2.3, 1.7, 0.9]), ('Glucemia', [1.0, 1.05, 1.35, 1.9, 2.4]),
                      ('Sensibilidad insulínica', [2.2, 1.3, 1.1, 0.95, 0.9])], ['1F4E9A', 'C00000', '00A651'],
                     title_txt='Esquema conceptual (unidades arbitrarias)', size=12, name='Gráfico DM2')
    st = steps_panel(s, 8.05, 1.2, 4.9, [
        '**Resistencia** en hígado, músculo y tejido adiposo: la misma insulina produce menos efecto.',
        '**Compensación β**: hiperinsulinemia mantiene la glucemia casi normal durante años.',
        '**Fracaso relativo**: gluco/lipotoxicidad, estrés del RE, genética → la secreción ya no alcanza.',
        '**Hiperglucemia sostenida** y daño orgánico; la obesidad visceral suele contribuir, pero existe DM2 sin obesidad.'], 14.5)
    s.note('DM2: interacción de resistencia a la insulina en hígado, músculo y tejido adiposo con una incapacidad progresiva de '
           'las células β para compensarla. Al comienzo la secreción puede ser alta (hiperinsulinemia), pero relativamente '
           'insuficiente frente a la demanda. El gráfico es un esquema conceptual en unidades arbitrarias (no datos de un '
           'estudio): la sensibilidad cae primero, la secreción sube para compensar y luego declina; cuando la compensación '
           'fracasa aparece la hiperglucemia. La obesidad visceral suele contribuir, aunque existe DM2 en personas sin obesidad.')


def patterns(D):
    s = new(D, U, 'Patrones no son criterios diagnósticos')
    l = s.group_start('DM1 problema')
    mbox(s, 0.5, 1.3, 5.9, 0.7, 'DM1 = PROBLEMA DE DISPONIBILIDAD DE INSULINA', 'y', 17)
    s.pic('langerhans-islet-pancreas', 2.2, 2.15, 2.5)
    tbox(s, 0.5, 4.75, 5.9, 1.35, 'La célula β no fabrica suficiente hormona: el tejido diana podría responder, pero **no recibe la señal**.', 15, anchor='m')
    s.group_end()
    r = s.group_start('DM2 problema')
    mbox(s, 6.9, 1.3, 5.95, 0.7, 'DM2 = SENSIBILIDAD + CAPACIDAD SECRETORA', 's', 17)
    s.pic('muscle-fiber', 7.4, 2.4, 2.4); s.pic('healthy_liver', 10.1, 2.3, 2.3)
    tbox(s, 6.9, 4.75, 5.95, 1.35, 'Problema **combinado**: los tejidos responden menos y la célula β no logra compensar de forma sostenida.', 15, anchor='m')
    s.group_end()
    p = pearl(s, 0.5, 6.3, 12.35, 0.75, 'No equiparar DM1 con «joven delgado» ni DM2 con «adulto obeso»: son **patrones**, no criterios diagnósticos.', 16)
    s.step(fade(l)); s.step(fade(r)); s.step(zoom(p))
    s.note('Diferenciación útil para la clase: un paciente con DM1 tiene un problema de disponibilidad de insulina; uno con DM2 '
           'suele tener un problema combinado de sensibilidad y capacidad secretora. Los estereotipos de edad y peso son patrones '
           'epidemiológicos, no criterios diagnósticos: hay DM1 en adultos y DM2 sin obesidad.')


def biosynthesis(D):
    s = new(D, U, 'Biosíntesis: preproinsulina → insulina + péptido C')
    # barras de cadena
    def chainbar(y, segs, name):
        g = s.group_start(name)
        x = 0.6
        for t, w, c in segs:
            s.shape(x, y, w, 0.55, 'rect', c, (INK, 1.5), False, t, 13, F_HEAD, INK if c not in ('2E86C1', 'C0392B') else WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
            x += w + 0.05
        return s.group_end()
    SP, B, C, A = ('Péptido señal', 1.4, 'BFBFBF'), ('Cadena B (30 aa)', 2.4, '2E86C1'), ('Péptido C (31 aa)', 2.3, BOX), ('Cadena A (21 aa)', 1.9, 'C0392B')
    lab(s, 0.6, 1.2, 4.0, 0.38, '1 · RE RUGOSO', 15, align='l')
    pre = chainbar(1.6, [SP, B, C, A], 'Preproinsulina')
    lab(s, 9.0, 1.6, 2.6, 0.55, 'PREPROINSULINA', 14, align='l')
    lab(s, 0.6, 2.45, 6.0, 0.38, '2 · CORTE DEL PÉPTIDO SEÑAL · PLEGADO · 3 PUENTES S–S', 15, align='l')
    pro = chainbar(2.85, [B, C, A], 'Proinsulina')
    lab(s, 7.75, 2.85, 2.0, 0.55, 'PROINSULINA', 14, align='l')
    lab(s, 0.6, 3.7, 8.0, 0.38, '3 · GOLGI → GRÁNULOS: PC1/3 · PC2 · CARBOXIPEPTIDASA E', 15, align='l')
    ins = s.group_start('Insulina madura')
    s.shape(0.6, 4.15, 2.4, 0.5, 'rect', '2E86C1', (INK, 1.5), False, 'B', 14, F_HEAD, WHITE, True, 'c', 'm', fit=False)
    s.shape(0.6, 4.75, 1.9, 0.5, 'rect', 'C0392B', (INK, 1.5), False, 'A', 14, F_HEAD, WHITE, True, 'c', 'm', fit=False)
    for x in (1.05, 1.75):
        s.arrow([(x, 4.65), (x, 4.75)], 'D4AC0D', 4, tail=None)
    lab(s, 3.1, 4.3, 1.9, 0.6, 'INSULINA', 15, align='l')
    s.group_end()
    pc = s.group_start('Péptido C libre')
    s.shape(5.0, 4.45, 2.3, 0.5, 'rect', BOX, (INK, 1.5), False, 'Péptido C', 14, F_HEAD, INK, True, 'c', 'm', fit=False)
    s.group_end()
    eq = mbox(s, 7.6, 4.3, 2.0, 0.8, 'EQUIMOLAR', 'y', 15)
    im = s.group_start('Gránulos')
    s.pic('endoplasmatic-reticulum-rough-3d', 9.9, 1.2, 2.9, name='RE rugoso')
    for gx, gy in ((10.2, 3.6), (10.95, 3.85), (11.75, 3.55), (11.3, 4.4), (12.2, 4.3)):
        granule(s, gx, gy, 0.62)
    lab(s, 9.9, 4.95, 3.0, 0.35, 'GRÁNULOS DE SECRECIÓN', 12.5)
    s.group_end()
    k = tbox(s, 0.6, 5.55, 12.35, 1.35, 'El **péptido C** se secreta en cantidad equimolar con la insulina y refleja **producción endógena** (la insulina exógena no lo contiene). '
             'Ayuda a clasificar la diabetes cuando se interpreta según **glucemia y función renal**.', 15, head='Uso clínico')
    a1 = s.arrow([(5.6, 2.2), (5.6, 2.8)], INK, 2.5); a2 = s.arrow([(4.3, 3.45), (4.3, 4.1)], INK, 2.5)
    s.step(fade(pre))
    s.step(wipe(a1, 't'), fade(pro, after=True))
    s.step(wipe(a2, 't'), fade(ins, after=True), fade(pc, after=True), zoom(eq, after=True))
    s.step(fade(im))
    s.step(fade(k))
    s.note('La insulina se sintetiza en el retículo endoplásmico rugoso como preproinsulina. Tras eliminarse el péptido señal se '
           'obtiene proinsulina, que se pliega y forma tres puentes disulfuro (dos entre cadenas A y B y uno dentro de la cadena '
           'A). En el aparato de Golgi y en los gránulos inmaduros, las prohormona convertasas PC1/3 y PC2 y la carboxipeptidasa E '
           'escinden el péptido C (ampliación bibliográfica). Resultado: insulina madura (cadenas A de 21 y B de 30 aminoácidos) y '
           'péptido C en cantidades equimolares, almacenados en gránulos. El péptido C refleja producción endógena y ayuda en la '
           'clasificación de la diabetes cuando se interpreta según la glucemia y la función renal.')


def insulin3d(D):
    s = new(D, U, 'Insulina: modelo proteico', 'cyan')
    im = insulin_model(s, 0.6, 1.3, 6.8, name='Modelo insulina grande')
    ss = s.group_start('Leyenda')
    sphere(s, 7.9, 1.45, 0.42, 'E74C3C'); s.text(8.45, 1.45, 4.3, 0.42, 'Residuo de la cadena **A**', 15, F_BODY, INK, False, 'l', 'm')
    sphere(s, 7.9, 2.0, 0.42, '2E86C1'); s.text(8.45, 2.0, 4.3, 0.42, 'Residuo de la cadena **B**', 15, F_BODY, INK, False, 'l', 'm')
    sphere(s, 7.9, 2.55, 0.42, 'F4D03F'); s.text(8.45, 2.55, 4.3, 0.42, 'Cisteína (puente disulfuro)', 15, F_BODY, INK, False, 'l', 'm')
    s.group_end()
    t = tbox(s, 7.8, 3.25, 5.1, 3.6, '- **2 puentes intercatenarios**: A7–B7 y A20–B19.\n- **1 puente intracatenario**: A6–A11.\n'
             '- En los gránulos se almacena como **hexámeros con Zn²⁺**; circula y actúa como **monómero**.\n'
             '- La unión al receptor induce un **cambio conformacional** de su ectodominio.', 15, head='Estructura')
    s.step(fade(ss)); s.step(fade(t))
    s.note('Modelo esquemático de la insulina humana: dos cadenas, A (21 aminoácidos) y B (30 aminoácidos), unidas por dos puentes '
           'disulfuro intercatenarios (A7–B7 y A20–B19) y un puente intracatenario en la cadena A (A6–A11). Cada esfera '
           'representa un residuo; las amarillas son las cisteínas. En el gránulo se almacena como hexámero coordinado con zinc '
           'y, tras la exocitosis, se disocia en monómeros, la forma activa (ampliación bibliográfica). La trayectoria de las '
           'cadenas es esquemática; no pretende reproducir coordenadas cristalográficas.')


def build(D):
    div(D)
    definition(D)
    classification(D)
    dm1(D)
    dm2(D)
    patterns(D)
    biosynthesis(D)
    insulin3d(D)
