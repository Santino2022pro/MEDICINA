# -*- coding: utf-8 -*-
"""UNIDAD II (b) — Secuencia D (riñón, Morph), potasio, infección, circuito integrado, cetonas, gasometría, evolución y tratamiento"""
from base import *

U = 2
SQ = 'cyanR'


# ---------------------------------------------------------------- Secuencia D
def d1(D):
    s = new(D, U, 'Secuencia D · 1 · sangre y arteria renal', SQ)
    vessel(s, 0.3, 1.25, 12.7, 1.0, name='!!Aorta D', rbcs=12)
    lab(s, 0.45, 2.3, 3.0, 0.35, 'AORTA ABDOMINAL', 12.5, align='l')
    art = s.arrow([(6.5, 2.25), (6.5, 3.15)], 'C0392B', 9, name='!!Arteria renal')
    lab(s, 6.7, 2.45, 2.0, 0.35, 'ARTERIA RENAL', 12.5, align='l')
    k = s.pic('kidney-2', 5.4, 3.15, 2.2, name='!!Riñón D')
    gl = [mol(s, 0.8 + i * 0.75, 1.5, 'glc', d=0.45, name='Glc sangre %d' % i) for i in range(7)]
    t = tbox(s, 8.6, 3.2, 4.35, 2.8, 'El riñón recibe ~20 % del gasto cardíaco. Con glucemia de **390 mg/dL** cada mililitro de plasma filtrado lleva más del doble de glucosa que en ayunas normal.', 15, head='Llegada al riñón')
    s.step(*[fade(g_, after=i > 0, dur=150) for i, g_ in enumerate(gl)])
    s.step(*[path(g_, 6.3 - (0.8 + i * 0.75), 0.0, dur=1300, delay=i * 120) for i, g_ in enumerate(gl[:4])])
    s.step(fade(t))
    s.note('Secuencia D (Morph): sangre → arteria renal → glomérulo → túbulo proximal → SGLT2 → glucosuria → diuresis osmótica. '
           'Primer paso: la sangre hiperglucémica llega al riñón por la arteria renal (el riñón recibe alrededor de una quinta parte '
           'del gasto cardíaco, ampliación bibliográfica). Las fichas de glucosa recorren la aorta hacia la arteria renal.')


def d2(D):
    s = new(D, U, 'Secuencia D · 2 · glomérulo y carga filtrada', SQ, morph=True)
    s.pic('kidney-2', 3.55, 4.75, 0.95, name='!!Riñón D')
    s.pic('nephron_2d', 0.6, 1.1, h=5.8, name='!!Nefrona D')
    gl = s.shape(1.25, 1.45, 1.35, 1.2, 'ellipse', None, ('C00000', 3.5), False, name='!!Lupa glomérulo')
    lab(s, 0.4, 6.55, 4.0, 0.35, 'NEFRONA (esquema)', 12)
    f = formula(s, 5.0, 1.3, 7.9, 0.9, 'Carga filtrada de glucosa = FG × glucemia', 22)
    e1 = tbox(s, 5.0, 2.45, 7.9, 1.65, 'Requiere **unidades compatibles** (mg/mL × mL/min = mg/min). Ejemplo didáctico con un FG **supuesto** de 120 mL/min (el FG del paciente no se informó): '
              '390 mg/dL = 3,9 mg/mL → 3,9 × 120 ≈ **468 mg/min**.', 14.5, head='Cálculo')
    e2 = tbox(s, 5.0, 4.35, 7.9, 1.55, 'La glucosa filtra libremente en el glomérulo: la carga filtrada **crece linealmente** con la glucemia. La reabsorción, en cambio, tiene **capacidad máxima**.', 15, head='Idea clave')
    s.step(zoom(gl)); s.step(fade(f)); s.step(fade(e1)); s.step(fade(e2))
    s.note('Paso 2: acercamiento Morph del riñón a la nefrona. La glucosa se filtra libremente; la carga filtrada es el producto del '
           'filtrado glomerular por la glucemia, con unidades compatibles. El FG de este paciente no fue informado: el cálculo con '
           '120 mL/min es sólo didáctico y está rotulado como supuesto. Con 390 mg/dL (3,9 mg/mL) × 120 mL/min = 468 mg/min. La '
           'carga filtrada crece linealmente con la glucemia, mientras que la reabsorción tubular es saturable.')


def tub_scene(s, k):
    s.shape(0.35, 1.15, 8.0, 1.05, 'rect', ('lin', [(0, 'FFF9E1'), (100, 'FCE9A8')], 90), (INK, 1.0), False, name='!!Luz tubular')
    lab(s, 0.45, 1.18, 3.0, 0.35, 'LUZ TUBULAR (ORINA PRIMARIA)', 12, align='l', name='!!Rótulo luz')
    tubule_cell(s, 0.35, 2.05, 3.9, 2.9, name='!!Célula TP 1')
    tubule_cell(s, 4.45, 2.05, 3.9, 2.9, name='!!Célula TP 2')
    vessel(s, 0.35, 5.3, 8.0, 0.85, name='!!Capilar peritubular', rbcs=7, seed=5)
    glut(s, 1.6, 2.06, 0.55, name='!!SGLT2', color='E67E22', text='SGLT2 · S1–S2')
    glut(s, 6.0, 2.06, 0.55, name='!!SGLT1', color='D35400', text='SGLT1 · S3')
    glut(s, 2.4, 4.6, 0.5, name='!!GLUT2 baso', color='5DADE2', text='')
    lab(s, 2.95, 4.62, 1.0, 0.3, 'GLUT2', 11, name='!!Rótulo GLUT2')
    s.shape(5.5, 4.55, 0.65, 0.42, 'roundRect', shade('58D68D', 0.4, 0.3), ('1D8348', 1.2), False, 'Na⁺/K⁺', 9.5, F_HEAD, INK, True, 'c', 'm',
            (0, 0, 0, 0), fit=False, name='!!Bomba NaK')


def d3(D):
    s = new(D, U, 'Secuencia D · 3 · túbulo proximal: SGLT2 y SGLT1', SQ, morph=True)
    tub_scene(s, 0)
    t = tbox(s, 8.65, 1.15, 4.3, 4.95, '- **SGLT2** (segmentos iniciales): reabsorbe la mayor parte, acoplado a Na⁺.\n- **SGLT1** (porción más distal): completa la reabsorción.\n'
             '- Salida **basolateral** por **GLUT**.\n- La **Na⁺/K⁺-ATPasa** mantiene el gradiente de Na⁺ que impulsa el cotransporte.', 14.5, head='Reabsorción normal')
    gl = [mol(s, 1.0 + i * 0.6, 1.5, 'glc', d=0.4, name='Glc luz %d' % i) for i in range(4)]
    s.step(*[fade(g_, after=i > 0, dur=150) for i, g_ in enumerate(gl)])
    s.step(*[path(g_, 1.75 - (1.0 + i * 0.6), 4.0, pts=[(1.75 - (1.0 + i * 0.6), 0.7), (2.55 - (1.0 + i * 0.6), 3.2)], dur=2200, delay=i * 300)
             for i, g_ in enumerate(gl)])
    s.note('Paso 3: el túbulo proximal. La reabsorción de glucosa ocurre mediante SGLT2 en los segmentos iniciales (cotransporte '
           'Na⁺:glucosa 1:1, de alta capacidad) y SGLT1 en la porción más distal (2:1, alta afinidad); la salida basolateral es por '
           'GLUT. La Na⁺/K⁺-ATPasa basolateral mantiene el gradiente de sodio que impulsa el cotransporte (estequiometrías: '
           'ampliación bibliográfica). Animación: las fichas de glucosa entran por SGLT2, atraviesan la célula y salen por GLUT2 '
           'hacia el capilar peritubular: en condiciones normales casi toda la glucosa filtrada se recupera.')


def d4(D):
    s = new(D, U, 'Secuencia D · 4 · saturación y glucosuria', SQ, morph=True)
    tub_scene(s, 1)
    cid = chart_line(s, 8.6, 1.1, 4.4, 3.4, ['0', '100', '200', '300', '400', '500', '600'],
                     [('Filtrada', [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), ('Reabsorbida', [0, 1.0, 1.95, 2.6, 2.75, 2.75, 2.75]),
                      ('Excretada', [0, 0, 0.05, 0.4, 1.25, 2.25, 3.25])], ['1F4E9A', '00A651', 'C00000'],
                     title_txt='Titulación de glucosa (esquema)', xtitle='Glucemia (mg/dL)', size=10.5, name='Curva de titulación')
    gl = [mol(s, 0.8 + i * 0.55, 1.5, 'glc', d=0.4, name='Glc exceso %d' % i) for i in range(10)]
    t = tbox(s, 8.6, 4.65, 4.35, 1.6, 'Umbral clínico aproximado **~180 mg/dL**, con gran variación (embarazo, función renal, diabetes crónica, iSGLT2). Con 390 la glucosuria es **muy esperable**, aunque **no fue informada** en el caso 11.', 12.5)
    s.step(*[fade(g_, after=i > 0, dur=100) for i, g_ in enumerate(gl)])
    s.step(*[path(g_, 0.0, 0.0, pts=[(0.3, 0.0)], dur=600) for g_ in gl[:2]], *[path(g_, 4.5, 0.0, dur=1800, delay=300) for g_ in gl[2:]])
    s.step(fade(t))
    s.note('Paso 4. Cuando la carga filtrada supera progresivamente la capacidad de reabsorción, la glucosa sobrante permanece en la '
           'luz y aparece en la orina: glucosuria. La curva de titulación (esquema conceptual) muestra la carga filtrada lineal, la '
           'reabsorción que se satura y la excreción que comienza en el umbral. El umbral clínico se sitúa cerca de 180 mg/dL, con '
           'gran variación individual (embarazo, función renal, diabetes de larga evolución, inhibidores SGLT2). Con 390 mg/dL la '
           'glucosuria es muy esperable, aunque no fue informada en el análisis del caso: no se inventa el dato.')


def d5(D):
    s = new(D, U, 'Secuencia D · 5 · diuresis osmótica', SQ, morph=True)
    tub_scene(s, 2)
    gl = [mol(s, 0.8 + i * 0.75, 1.5, 'glc', d=0.4, name='Glc luz osm %d' % i) for i in range(10)]
    w = [s.shape(1.1 + i * 0.75, 1.75, 0.34, 0.34, 'ellipse', '5DADE2', ('1F618D', 1.0), False, 'H₂O', 7.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                 name='Agua %d' % i) for i in range(9)]
    ions = s.group_start('Electrolitos perdidos')
    for i, t in enumerate(['Na⁺', 'K⁺', 'Cl⁻', 'Mg²⁺', 'PO₄³⁻']):
        s.shape(0.6 + i * 0.85, 1.85, 0.7, 0.3, 'roundRect', BOX, (INK, 1.0), False, t, 9.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    st = steps_panel(s, 8.6, 1.15, 4.35, ['La glucosa en la luz **eleva los osmoles** y retiene agua.', '**Poliuria** con pérdida de Na⁺, K⁺, Cl⁻, Mg²⁺ y fosfato.',
                                          '**Deshidratación**: polidipsia, hipotensión, taquicardia.', '**FG ↓** → menor depuración de glucosa y cetonas: se agrava el cuadro.'], 13.5, anim=False)[0]
    s.step(*[fade(x, after=i > 0, dur=80) for i, x in enumerate(w)], fade(st[0], after=True))
    s.step(*[path(x, 0.0, 5.0, dur=1500) for x in w[:5]], fade(ions, after=True), fade(st[1], after=True))
    s.step(fade(st[2]))
    s.step(fade(st[3]))
    s.note('Paso 5. La glucosa no reabsorbida aumenta la osmolalidad del líquido tubular y dificulta la reabsorción de agua: diuresis '
           'osmótica. Resultado: poliuria, polidipsia, deshidratación, hipotensión, taquicardia, menor filtración renal y, con ella, '
           'menor depuración de glucosa (círculo vicioso). Se pierden sodio, potasio, cloro, magnesio y fosfato. Las fichas de agua '
           'abandonan el túbulo hacia la orina arrastradas por la glucosa.')


def potassium(D):
    s = new(D, U, 'Potasio: sérico normal ≠ potasio corporal normal', 'peach')
    s.shape(0.4, 1.2, 6.0, 4.3, 'roundRect', ('lin', [(0, 'FDEDEC'), (100, 'F5B7B1')], 90), ('B03A2E', 3.0), SHD, adj={'adj': 10000}, name='Célula K')
    lab(s, 0.6, 1.3, 3.0, 0.35, 'INTRACELULAR (≈98 % del K⁺)', 12.5, align='l')
    ks = [mol(s, 0.9 + (i % 6) * 0.85, 2.0 + (i // 6) * 0.6, 'k', d=0.42, name='K intra %d' % i) for i in range(18)]
    causes = [('Insulinopenia', 'Na⁺/K⁺-ATPasa menos estimulada'), ('Acidosis', 'intercambio H⁺/K⁺ (más en acidosis mineral)'), ('Hiperosmolalidad', 'salida de agua arrastra K⁺')]
    cid = []
    for i, (h, t) in enumerate(causes):
        g = s.group_start('Causa ' + h)
        mbox(s, 6.75, 1.2 + i * 1.0, 2.1, 0.45, h, 's', 13.5, caps=False)
        s.text(8.95, 1.15 + i * 1.0, 4.0, 0.55, t, 13, F_BODY, INK, False, 'l', 'm')
        cid.append(s.group_end())
    ur = mbox(s, 6.75, 4.25, 6.2, 0.6, 'ORINA (diuresis osmótica) + vómitos: K⁺ TOTAL ↓', 'r', 14)
    ins = mbox(s, 0.4, 5.75, 6.0, 0.55, 'Al reponer insulina: K⁺ ENTRA RÁPIDO A LA CÉLULA', 'y', 14)
    pr = pearl(s, 6.75, 5.1, 6.2, 1.3, 'Riesgo de **hipopotasemia grave** y arritmias: el K⁺ sérico inicial puede ser **normal o alto** pese a un déficit corporal total importante.', 14)
    s.step(*[fade(c, after=i > 0) for i, c in enumerate(cid)], *[path(k_, 6.6 - (0.9 + (i % 6) * 0.85), 0.0, dur=1200, delay=i * 120) for i, k_ in enumerate(ks[:5])])
    s.step(zoom(ur), *[out(k_, dur=400) for k_ in ks[:5]])
    s.step(fade(ins), *[path(k_, 0.0, 0.0, pts=[(0.2, 0.0)], dur=300) for k_ in ks[5:8]])
    s.step(zoom(pr))
    s.note('Potasio sérico frente a potasio corporal total. La insulinopenia (menor estímulo de la Na⁺/K⁺-ATPasa), la acidosis y la '
           'hiperosmolalidad trasladan K⁺ del intracelular al extracelular, mientras la diuresis osmótica y los vómitos eliminan '
           'grandes cantidades: la kalemia puede verse normal o elevada pese a un déficit corporal total. Al reponer insulina el K⁺ '
           'entra rápidamente a las células y aparece riesgo de hipopotasemia grave. Animación: el K⁺ sale de la célula, luego se '
           'pierde por orina, y finalmente la insulina lo reintroduce. El porcentaje intracelular (~98 %) y el matiz sobre el tipo '
           'de acidosis son ampliación bibliográfica. Ejercicio 7 de la Unidad X.')


def infection(D):
    s = new(D, U, 'Pregunta 5 · neumonía, fiebre y cetoacidosis', 'pink')
    s.pic('healthy-lung', 0.4, 1.15, 2.2, name='Pulmón infección')
    s.pic('macrophage', 0.7, 3.4, 1.6, name='Macrófago')
    nodes = {
        'inf': (2.9, 1.3, 2.9, 0.6, 'Neumococo · inmunidad innata', 's', 13.5),
        'cy': (2.9, 2.35, 2.9, 0.6, 'IL-1 · IL-6 · TNF-α', 's', 15),
        'st': (6.3, 1.3, 3.0, 0.95, 'Catecolaminas · cortisol\nglucagón · GH', 'y', 14),
        'ri': (9.8, 1.3, 3.1, 0.6, 'Resistencia insulínica ↑', 'Y', 14),
        'phg': (9.8, 2.1, 3.1, 0.6, 'Salida hepática de glucosa ↑', 'Y', 14),
        'lip': (9.8, 2.9, 3.1, 0.6, 'Lipólisis ↑ → cetogénesis ↑', 'Y', 14),
        'f': (2.9, 3.55, 2.9, 0.6, 'Fiebre: demanda metabólica ↑', 'w', 13.5),
        'v': (2.9, 4.35, 2.9, 0.6, 'Vómitos · ingesta ↓', 'w', 14),
        't': (2.9, 5.15, 2.9, 0.6, 'Taquipnea: pérdidas insensibles', 'w', 13),
        'h': (6.3, 4.35, 3.0, 0.75, 'Hidratación ↓ · volumen ↓', 'r', 14),
        'd': (9.8, 4.35, 3.1, 0.75, 'Dosis habitual de insulina\nse vuelve insuficiente', 'r', 13),
    }
    edges = [('inf', 'cy'), ('cy', 'st', {'pts': [(5.85, 2.65), (6.25, 2.0)]}), ('st', 'ri', {'pts': [(9.35, 1.6), (9.75, 1.6)]}),
             ('st', 'phg', {'pts': [(9.35, 1.9), (9.75, 2.4)]}), ('st', 'lip', {'pts': [(9.35, 2.1), (9.75, 3.2)]}),
             ('f', 'h', {'pts': [(5.85, 3.85), (6.25, 4.55)]}), ('v', 'h'), ('t', 'h', {'pts': [(5.85, 5.45), (6.25, 4.9)]}), ('ri', 'd', {'pts': [(12.95, 1.6), (13.05, 1.6), (13.05, 4.7), (12.95, 4.7)]})]
    graph(s, nodes, edges, [['inf', 'inf>cy', 'cy'], ['cy>st', 'st'], ['st>ri', 'ri', 'st>phg', 'phg', 'st>lip', 'lip'], ['f', 'v', 't'],
                            ['f>h', 'v>h', 't>h', 'h'], ['ri>d', 'd']])
    p = tbox(s, 0.4, 6.0, 12.5, 0.9, 'La hiperglucemia a su vez **deteriora funciones inmunitarias** y la perfusión microvascular. Leucocitosis aislada no confirma infección; aquí la apoyan fiebre + consolidación + hemocultivos.', 13.5, anchor='m')
    s.step(fade(p))
    s.note('Pregunta 5. La infección neumocócica activa la inmunidad innata y libera mediadores (IL-1, IL-6, TNF-α) que estimulan la '
           'respuesta de estrés: catecolaminas, cortisol, glucagón y hormona de crecimiento. Se intensifican la resistencia '
           'periférica a la insulina, la salida hepática de glucosa y la lipólisis. La fiebre aumenta las demandas metabólicas; los '
           'vómitos y la menor ingesta reducen la hidratación; la taquipnea incrementa las pérdidas insensibles. La dosis habitual '
           'de insulina puede tornarse insuficiente aun si fue administrada. La hiperglucemia a su vez deteriora funciones '
           'inmunitarias y la perfusión microvascular. La leucocitosis aislada no confirma infección, pero aquí la fiebre, la '
           'consolidación y los hemocultivos sí apoyan infección bacteriana. La taquipnea puede tener contribución mixta.')


def circuit(D):
    s = new(D, U, 'Circuito fisiopatológico integrado de la CAD', 'green')
    nodes = {
        'pn': (0.4, 1.2, 2.6, 0.6, 'Neumonía · estrés', 's', 15),
        'ins': (3.5, 1.2, 3.0, 0.6, 'Acción insulínica ↓↓', 'y', 15),
        # rama cetónica
        'l': (0.4, 2.35, 2.6, 0.5, 'Lipólisis adiposa ↑', 'Y', 13),
        'a': (0.4, 3.1, 2.6, 0.5, 'AGNE → hígado', 'Y', 13),
        'b': (0.4, 3.85, 2.6, 0.5, 'β-oxidación → acetil-CoA ↑', 'Y', 12),
        'k': (0.4, 4.6, 2.6, 0.5, 'Cetogénesis: AcAc · β-OHB', 'Y', 12),
        'h': (0.4, 5.35, 2.6, 0.5, 'HCO₃⁻ consumido → acidemia', 'r', 12),
        'kus': (0.4, 6.1, 2.6, 0.5, 'Hiperventilación (Kussmaul)', 'g', 12),
        # rama glucosa
        'g': (6.9, 2.35, 2.7, 0.5, 'Hiperglucemia', 'Y', 13),
        'gu': (6.9, 3.1, 2.7, 0.5, 'Glucosuria', 'Y', 13),
        'do': (6.9, 3.85, 2.7, 0.5, 'Diuresis osmótica', 'Y', 13),
        'dh': (6.9, 4.6, 2.7, 0.5, 'Deshidratación · hipovolemia', 'r', 12),
        'pr': (6.9, 5.35, 2.7, 0.5, 'Perfusión renal ↓ · FG ↓', 'r', 12),
        'x': (3.6, 4.6, 2.75, 1.25, 'Menor eliminación de glucosa y cetonas · más hormonas de estrés', 'k', 12.5),
        'cl': (10.0, 3.0, 2.95, 2.4, 'EMPEORA EL ESTADO METABÓLICO', 'r', 15),
    }
    edges = [('pn', 'ins'), ('ins', 'l', {'pts': [(3.6, 1.82), (2.6, 2.32)]}), ('l', 'a'), ('a', 'b'), ('b', 'k'), ('k', 'h'), ('h', 'kus'),
             ('ins', 'g', {'pts': [(6.4, 1.82), (7.6, 2.32)]}), ('g', 'gu'), ('gu', 'do'), ('do', 'dh'), ('dh', 'pr'),
             ('pr', 'x', {'pts': [(6.85, 5.6), (6.0, 5.88)]}), ('h', 'x', {'pts': [(3.05, 5.6), (3.55, 5.5)]}), ('x', 'cl', {'pts': [(5.0, 4.55), (5.0, 4.15), (9.95, 4.15)], 'col': INH}),
             ('cl', 'ins', {'pts': [(11.5, 2.95), (11.5, 1.5), (6.55, 1.5)], 'col': INH, 'dash': 'dash'})]
    order = [['pn', 'pn>ins', 'ins'],
             ['ins>l', 'l', 'l>a', 'a', 'a>b', 'b', 'b>k', 'k', 'k>h', 'h', 'h>kus', 'kus'],
             ['ins>g', 'g', 'g>gu', 'gu', 'gu>do', 'do', 'do>dh', 'dh', 'dh>pr', 'pr'],
             ['pr>x', 'h>x', 'x'], ['x>cl', 'cl', 'cl>ins']]
    ids = graph(s, nodes, edges, order)
    s.note('Ejemplo 3 de animación. Rama cetónica (izquierda): insulinopenia → lipólisis adiposa → AGNE al hígado → β-oxidación → '
           'acetil-CoA → cetogénesis → β-hidroxibutirato y acetoacetato → consumo de bicarbonato → acidemia → hiperventilación '
           'compensadora. Rama de la glucosa (derecha): hiperglucemia → glucosuria → diuresis osmótica → deshidratación → '
           'hipovolemia → menor perfusión renal. Ambas ramas se animan por separado porque ocurren en paralelo y se unen en un '
           'circuito: menor filtración y peor eliminación de glucosa y cetonas, más hormonas de estrés, mayor resistencia y '
           'empeoramiento del estado metabólico, que realimenta la falta de acción insulínica (flecha discontinua). Circuito del '
           'material de cátedra: neumonía → estrés contrarregulador → déficit de acción insulínica → hiperglucemia + lipólisis + cetogénesis → '
           'diuresis osmótica → hipovolemia → menor filtración y peor eliminación → mayor CAD.')


def ketone_tests(D):
    s = new(D, U, 'Cetonemia frente a cetonuria: qué detecta cada prueba', 'yellow')
    model(s, 'bhb', 0.4, 1.2, 2.1, label='β-hidroxibutirato')
    model(s, 'acetoacetato', 3.1, 1.2, 2.0, label='Acetoacetato')
    model(s, 'acetona', 5.7, 1.4, 1.5, label='Acetona')
    eq = s.group_start('Equilibrio')
    s.arrow([(2.65, 2.0), (3.0, 2.0)], INK, 2.5, head='triangle')
    lab(s, 2.35, 2.25, 1.0, 0.3, 'NADH', 10.5)
    s.arrow([(5.4, 2.0), (5.75, 2.0)], INK, 2.5)
    s.group_end()
    np_ = mbox(s, 3.05, 3.85, 4.15, 0.55, 'TIRA (NITROPRUSIATO): detecta AcAc (± acetona)', 'Y', 12.5)
    bh = mbox(s, 0.4, 3.85, 2.45, 0.55, 'NO detecta β-OHB', 'r', 13)
    rec = s.group_start('Recuperación')
    mbox(s, 7.6, 1.25, 5.35, 0.55, 'DURANTE EL TRATAMIENTO', 's', 15)
    tbox(s, 7.6, 1.9, 5.35, 2.3, 'Al mejorar el estado redox el **β-OHB se oxida a acetoacetato** → la tira puede **permanecer positiva o intensificarse** aunque el paciente mejore (ejercicio 8).', 15)
    s.group_end()
    p = pearl(s, 0.4, 4.6, 12.55, 0.95, 'Método preferible para diagnóstico y seguimiento: **β-hidroxibutirato sanguíneo cuantitativo**. La cetonuria puede **subestimar** la CAD al inicio.', 16)
    t = tbox(s, 0.4, 5.75, 12.55, 1.15, 'Cetosis **fisiológica** del ayuno: pH **conservado** · cetoacidosis **patológica**: producción que supera el uso y la amortiguación → **acidemia**.', 15, anchor='m')
    s.step(fade(eq)); s.step(fade(np_), fade(bh, after=True)); s.step(fade(rec)); s.step(zoom(p)); s.step(fade(t))
    s.note('Limitación técnica: la prueba urinaria con nitroprusiato detecta principalmente acetoacetato (y algo de acetona), no '
           'β-hidroxibutirato; puede subestimar la CAD al inicio, cuando predomina β-OHB por el estado redox (NADH elevado), y '
           'permanecer positiva o intensificarse transitoriamente al mejorar el estado redox, porque el β-OHB se reconvierte en '
           'acetoacetato. El método preferible para diagnóstico y seguimiento es el β-hidroxibutirato sanguíneo cuantitativo '
           '[consenso 2024]. La cetosis fisiológica del ayuno, con pH conservado, no debe confundirse con la cetoacidosis.')


def diagnosis(D):
    s = new(D, U, 'Pregunta 2 · diagnóstico sindromático y gravedad', 'peach')
    tri = s.group_start('Tríada')
    for i, (t, k) in enumerate([('Diabetes o\nhiperglucemia', 'y'), ('Cetosis', 'y'), ('Acidosis metabólica', 'y')]):
        x = 0.6 + i * 2.15
        s.shape(x, 1.3, 1.95, 1.95, 'ellipse', ('a', BOX, 30), (INK, 2), False, t, 12.5, F_HEAD, BOXT, True, 'c', 'm', (0.05, 0.1, 0.05, 0.1), fit=True)
    s.group_end()
    rows = [['Criterio (consenso 2024)', 'Umbral'], ['Glucosa', '≥ 200 mg/dL o diabetes conocida'], ['Cetonas', 'β-OHB ≥ 3,0 mmol/L o cetonas urinarias ≥ 2+'],
            ['Acidosis', 'pH < 7,30 o bicarbonato < 18 mmol/L']]
    tid, H = table(s, 7.2, 1.25, 5.75, rows, [2.1, 3.65], size=13.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Criterios CAD')
    c1 = tbox(s, 0.4, 3.55, 6.4, 1.6, 'Por pH 7,15 y HCO₃⁻ 13 sería **CAD moderada**, pero somnolencia/confusión, hipotensión, posible **sepsis** y neumonía justifican **cuidados intensivos** por riesgo clínico.', 14.5, head='Gravedad')
    c2 = tbox(s, 7.2, 3.55, 5.75, 1.6, 'La cetonemia **+++** es **cualitativa**: no equivale a una concentración medida, aunque junto a la clínica su fuerza diagnóstica es alta.', 14.5, head='Cetonemia cualitativa')
    c3 = tbox(s, 0.4, 5.4, 12.55, 1.5, '**pO₂ 99 mmHg con aire ambiente** no coincide de manera simple con **SpO₂ 90 %**: lecturas o momentos distintos, error instrumental o mala perfusión. «FIO₂ 0,21 %» debe leerse **FiO₂ = 0,21 (21 %)**. Verificar gasometría, oximetría y estado respiratorio.', 14, head='Otras inconsistencias')
    s.step(fade(tri)); s.step(fade(tid)); s.step(fade(c1)); s.step(fade(c2)); s.step(fade(c3))
    s.note('Pregunta 2. Sospecha: cetoacidosis diabética precipitada por neumonía adquirida en la comunidad, con hipovolemia importante '
           'y alteración del sensorio. Tríada conceptual: diabetes/hiperglucemia + cetosis + acidosis metabólica. El consenso 2024 '
           'utiliza glucosa ≥200 mg/dL o diabetes conocida; β-hidroxibutirato ≥3,0 mmol/L o cetonas urinarias ≥2+; y pH <7,30 o '
           'bicarbonato <18 mmol/L. La cetonemia +++ es cualitativa. Según pH y bicarbonato sería CAD moderada, pero el compromiso '
           'del sensorio, la hipotensión, la posible sepsis y la neumonía justifican cuidados intensivos. La pO₂ de 99 mmHg con aire '
           'ambiente no coincide de manera simple con una saturación de 90 %; la expresión «FIO₂ 0,21 %» se interpreta como FiO₂ = '
           '0,21.')


def gas_check(D):
    s = new(D, U, 'Verificación de la gasometría: Henderson–Hasselbalch', 'blue')
    f = formula(s, 0.4, 1.2, 8.0, 0.85, 'pH = 6,1 + log₁₀ ( [HCO₃⁻] / (0,03 × pCO₂) )', 22)
    d = mbox(s, 8.7, 1.2, 4.25, 0.85, 'DATOS: HCO₃⁻ 13 · pCO₂ 24 · pH informado 7,15', 'y', 13)
    st = [formula(s, 0.4, 2.35, 8.0, 0.7, '0,03 × 24 = 0,72 mmol/L de CO₂ disuelto', 18, fill='FFF2CC'),
          formula(s, 0.4, 3.2, 8.0, 0.7, '13 / 0,72 = 18,06', 18, fill='FFF2CC'),
          formula(s, 0.4, 4.05, 8.0, 0.7, 'log₁₀ 18,06 = 1,257', 18, fill='FFF2CC'),
          formula(s, 0.4, 4.9, 8.0, 0.85, 'pH calculado = 6,1 + 1,257 ≈ 7,36', 22, fill=BOX, color=BOXT)]
    cmp_ = pearl(s, 8.7, 2.35, 4.25, 2.1, '**7,36 calculado ≠ 7,15 informado**: la tríada no es internamente consistente.', 17)
    nx = tbox(s, 8.7, 4.65, 4.25, 2.25, '- Repetir la gasometría.\n- Verificar si los valores provienen de **momentos o muestras distintos**.\n- Medir **β-hidroxibutirato**.', 14.5, head='Conducta')
    t = tbox(s, 0.4, 5.95, 8.0, 0.95, 'El diagnóstico sindromático de CAD **sigue siendo muy probable** (hiperglucemia + cetosis + HCO₃⁻ bajo + clínica).', 14, anchor='m')
    s.step(fade(d))
    for x in st:
        s.step(fade(x))
    s.step(zoom(cmp_)); s.step(fade(nx)); s.step(fade(t))
    s.note('Diapositiva de verificación. Henderson–Hasselbalch: pH = 6,1 + log10([HCO₃⁻]/(0,03 × pCO₂)). Con HCO₃⁻ = 13 mEq/L y '
           'pCO₂ = 24 mmHg: 0,03 × 24 = 0,72; 13/0,72 = 18,06; log10(18,06) = 1,257; pH = 6,1 + 1,257 ≈ 7,36, no 7,15. La tríada '
           'pH–HCO₃⁻–pCO₂ no es internamente consistente. La interpretación sindromática de cetoacidosis sigue siendo muy probable '
           '(hiperglucemia + cetosis + bicarbonato reducido + clínica), pero un análisis riguroso exige repetir la gasometría, '
           'verificar si los valores provienen de momentos o muestras distintos y medir β-hidroxibutirato. No se deben forzar '
           'ecuaciones sobre una tríada discordante ni inventar el valor «correcto».')


def gas_alt(D):
    s = new(D, U, '¿Qué valor podría estar equivocado?', 'blue')
    a = s.group_start('Hipótesis A')
    mbox(s, 0.4, 1.2, 6.0, 0.6, 'SI pH 7,15 Y pCO₂ 24 FUERAN CORRECTOS', 's', 14)
    formula(s, 0.4, 1.95, 6.0, 0.7, 'HCO₃⁻ = 0,03 × 24 × 10^(7,15 − 6,1)', 17)
    formula(s, 0.4, 2.8, 6.0, 0.7, '= 0,72 × 11,22 ≈ 8,1 mEq/L', 19, fill=BOX, color=BOXT)
    s.group_end()
    b = s.group_start('Hipótesis B')
    mbox(s, 6.95, 1.2, 6.0, 0.6, 'SI pH 7,15 Y HCO₃⁻ 13 FUERAN CORRECTOS', 's', 14)
    formula(s, 6.95, 1.95, 6.0, 0.7, 'pCO₂ = 13 / (0,03 × 10^(7,15 − 6,1))', 17)
    formula(s, 6.95, 2.8, 6.0, 0.7, '= 13 / 0,337 ≈ 38,6 mmHg', 19, fill=BOX, color=BOXT)
    s.group_end()
    p = pearl(s, 0.4, 3.85, 12.55, 1.1, 'Ninguna hipótesis puede elegirse con los datos disponibles: **no se inventan valores no medidos**. Sólo una nueva muestra resuelve la discordancia.', 16)
    t = tbox(s, 0.4, 5.2, 12.55, 1.65, 'Cada hipótesis cambiaría la lectura: un HCO₃⁻ de ~8 implicaría acidosis más grave; una pCO₂ de ~39 implicaría **ausencia de compensación respiratoria** (acidosis respiratoria relativa). Por eso no se clasifica el trastorno mixto con certeza.', 14.5, head='Por qué importa')
    s.step(fade(a)); s.step(fade(b)); s.step(zoom(p)); s.step(fade(t))
    s.note('Si el pH fuese realmente 7,15 y la pCO₂ 24, el HCO₃⁻ calculado sería 0,72 × 10^1,05 = 0,72 × 11,22 ≈ 8,1 mEq/L; si pH 7,15 '
           'y HCO₃⁻ 13 fueran correctos, la pCO₂ calculada sería 13/(0,03 × 11,22) = 13/0,337 ≈ 38,6 mmHg. Con los datos del caso no '
           'puede saberse cuál valor es erróneo: no se inventan resultados no medidos. La interpretación del significado de cada '
           'hipótesis (gravedad mayor o falta de compensación) es razonamiento docente sobre valores hipotéticos.')


def winter(D):
    s = new(D, U, 'Fórmula de Winter y el falso trastorno mixto', 'cyan')
    f = formula(s, 0.4, 1.2, 6.3, 0.85, 'pCO₂ esperada ≈ 1,5 × HCO₃⁻ + 8 ± 2', 21)
    c1 = formula(s, 0.4, 2.25, 6.3, 0.7, '1,5 × 13 + 8 = 27,5', 19, fill='FFF2CC')
    c2 = formula(s, 0.4, 3.15, 6.3, 0.8, 'Banda esperada: 25,5 – 29,5 mmHg', 20, fill=BOX, color=BOXT)
    bar = s.group_start('Escala pCO2')
    s.shape(7.1, 1.6, 5.8, 0.5, 'rect', WHITE, (INK, 1.25), False)
    x0 = 7.1; k = 5.8 / 20.0  # 20 a 40 mmHg
    s.shape(x0 + (25.5 - 20) * k, 1.6, 4 * k, 0.5, 'rect', ('a', '00A651', 45), None, False)
    for v in (20, 25, 30, 35, 40):
        s.text(x0 + (v - 20) * k - 0.3, 2.12, 0.6, 0.3, str(v), 11.5, F_HEAD, INK, True, 'c', 't')
    s.group_end()
    mk = s.shape(x0 + 4 * k - 0.12, 1.32, 0.24, 1.05, 'rect', 'C00000', None, False, name='Marca pCO2 24')
    ml = lab(s, x0 + 4 * k - 0.6, 2.45, 1.4, 0.3, 'medida: 24', 12, INH)
    lab(s, 7.1, 1.15, 5.8, 0.35, 'pCO₂ (mmHg)', 12.5)
    t1 = tbox(s, 7.1, 3.0, 5.85, 1.75, '24 está **algo por debajo** de lo esperado → **podría** sugerir alcalosis respiratoria agregada (fiebre, neumonía).', 15, head='Lectura aislada')
    p = pearl(s, 0.4, 5.0, 12.55, 1.0, 'Pero la tríada es **incompatible** con Henderson–Hasselbalch: sólo se formula una **hipótesis**, no un diagnóstico de trastorno mixto.', 16)
    t2 = tbox(s, 0.4, 6.2, 12.55, 0.7, 'Regla: un trastorno mixto se diagnostica comparando con lo esperado **y** verificando la coherencia ácido-base.', 14.5, anchor='m')
    s.step(fade(c1)); s.step(fade(c2)); s.step(fade(bar), zoom(mk, after=True), fade(ml, after=True)); s.step(fade(t1)); s.step(zoom(p)); s.step(fade(t2))
    s.note('Pregunta 1b, paso 4. Ecuación de Winter: pCO₂ esperada ≈ 1,5 × HCO₃⁻ + 8 ± 2; con 13 mEq/L: 27,5 ± 2 mmHg (25,5 a 29,5). '
           'Una pCO₂ de 24 sería algo más baja que lo esperado y podría sugerir alcalosis respiratoria asociada (la fiebre y la '
           'neumonía podrían explicarla si fuera real), pero la incompatibilidad global de Henderson–Hasselbalch impide afirmar '
           'este trastorno mixto con seguridad hasta verificar los datos. Pasos de la lectura: 1) pH 7,15 → acidemia; 2) HCO₃⁻ 13 → '
           'trastorno primario metabólico; 3) pCO₂ 24 → respuesta ventilatoria (Kussmaul, aunque la neumonía también aumenta el '
           'impulso ventilatorio); 4) Winter; 5) anion gap si hubiera Na⁺ y Cl⁻.')


def anion_gap(D):
    s = new(D, U, 'Anion gap: fórmula y límite del caso', 'green')
    f = formula(s, 0.4, 1.2, 7.4, 0.85, 'AG = Na⁺ − (Cl⁻ + HCO₃⁻)', 24)
    g = s.group_start('Gamblegrama')
    x = 8.3
    s.shape(x, 1.2, 1.9, 4.6, 'rect', 'F4B183', (INK, 1.5), False, 'Na⁺', 18, F_HEAD, INK, True, 'c', 'm')
    s.shape(x + 2.0, 1.2, 1.9, 2.6, 'rect', '9DC3E6', (INK, 1.5), False, 'Cl⁻', 16, F_HEAD, INK, True, 'c', 'm')
    s.shape(x + 2.0, 3.8, 1.9, 0.6, 'rect', 'C5E0B4', (INK, 1.5), False, 'HCO₃⁻ ↓', 13, F_HEAD, INK, True, 'c', 'm')
    s.shape(x + 2.0, 4.4, 1.9, 1.4, 'rect', 'C00000', (INK, 1.5), False, 'AG ↑\ncetoaniones\n(± lactato)', 12.5, F_HEAD, WHITE, True, 'c', 'm')
    lab(s, x, 5.9, 3.9, 0.35, 'Electroneutralidad (esquema)', 12)
    s.group_end()
    c = tbox(s, 0.4, 2.3, 7.4, 1.6, 'Corrección por **hipoalbuminemia**: sumar ≈ **2,5 mEq/L** por cada **1 g/dL** de albúmina por debajo de 4.', 15, head='Corrección')
    lim = pearl(s, 0.4, 4.15, 7.4, 1.0, 'En los casos 11 y 12 **no puede calcularse**: faltan **Na⁺ y Cl⁻** (y albúmina).', 16)
    r = tbox(s, 0.4, 5.4, 7.4, 1.5, 'AG elevado = **aniones no medidos**, pero no identifica su causa. En CAD pensar cetonas; con sepsis o shock agregar **lactato**; considerar uremia y tóxicos.', 14.5, anchor='m')
    s.step(fade(g)); s.step(fade(c)); s.step(zoom(lim)); s.step(fade(r))
    s.note('Anion gap = Na⁺ − (Cl⁻ + HCO₃⁻). Requiere sodio y cloro; se corrige por hipoalbuminemia sumando aproximadamente 2,5 '
           'mEq/L por cada 1 g/dL de albúmina por debajo de 4. En la CAD suele elevarse por los aniones cetoácidos; también puede '
           'elevarlo el lactato por hipoperfusión o sepsis. En el caso 11 no puede calcularse por falta de sodio y cloro. El '
           'gamblegrama es un esquema de electroneutralidad, no valores del paciente. Ejercicio 5 de la Unidad X.')


def symptoms(D):
    s = new(D, U, 'Pregunta 4 · síntomas de la CAD y su mecanismo', 'pink')
    rows = [('Náuseas y vómitos', 'Activación gastrointestinal y respuesta central a la acidemia'),
            ('Dolor abdominal (a veces intenso)', 'Acidemia, hipoperfusión y dismotilidad'),
            ('Respiración de Kussmaul', 'Compensación ventilatoria del trastorno ácido'),
            ('Aliento afrutado', 'Acetona (descarboxilación del acetoacetato), volátil'),
            ('Deshidratación, hipotensión, taquicardia', 'Diuresis osmótica, vómitos, pérdidas insensibles'),
            ('Debilidad, cefalea, confusión → estupor/coma', 'Hipoperfusión, cambios osmóticos y acidemia; no sólo «las cetonas»')]
    ids = []
    for i, (h, t) in enumerate(rows):
        y = 1.2 + i * 0.9
        g = s.group_start('Síntoma %d' % i)
        mbox(s, 0.4, y, 4.6, 0.75, h, 'y', 14, caps=False)
        s.arrow([(5.05, y + 0.37), (5.45, y + 0.37)], INK, 2.5)
        tbox(s, 5.5, y, 7.45, 0.75, t, 14.5, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 6.65, 12.55, 0.4, 'Cetosis fisiológica del ayuno (pH conservado) ≠ cetoacidosis patológica.', 13.5)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Pregunta 4. En la CAD predominan náuseas y vómitos (activación gastrointestinal y respuesta central a la acidemia), dolor '
           'abdominal a veces intenso (acidemia, hipoperfusión y dismotilidad), respiración profunda de Kussmaul (compensación del '
           'trastorno ácido), aliento afrutado por acetona, deshidratación, hipotensión, taquicardia, debilidad, cefalea, confusión '
           'y, en casos graves, estupor o coma. La alteración del estado mental se relaciona además con hipoperfusión y cambios '
           'osmóticos: no toda confusión es consecuencia directa de las cetonas. La cetosis fisiológica del ayuno, con pH '
           'conservado, no debe confundirse con la cetoacidosis patológica.')


def evolution(D):
    s = new(D, U, 'Evolución a las 24 horas: ingreso frente a 24 h', 'peach')
    rows = [['Parámetro', 'Ingreso', '24 h', 'Interpretación'],
            ['Glucosa (mg/dL)', '390', '200', 'Mejoró; aún requiere control'],
            ['pH', '7,15', '7,37', 'Acidemia resuelta'],
            ['HCO₃⁻ (mEq/L)', '13', '22', 'Casi normal'],
            ['pCO₂ (mmHg)', '24', '37', 'Menor hiperventilación compensatoria'],
            ['Cetonemia / cetonuria', '+++ / +', 'Negativas', 'Reducción sustancial de cetonas detectables'],
            ['Exceso de base', '−8', '−3', 'Déficit residual leve'],
            ['TA / FC / FR', '90/50 · 120 · 32', '120/80 · 105 · 20', 'Recuperación hemodinámica y ventilatoria']]
    table(s, 0.4, 1.15, 7.6, rows, [2.0, 1.4, 1.5, 2.7], size=12.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla evolución')
    from pptx.chart.data import CategoryChartData
    cid = chart_line(s, 8.25, 1.15, 4.7, 2.75, ['Ingreso', '24 h'], [('HCO₃⁻', [13, 22]), ('pCO₂', [24, 37])], ['1F4E9A', 'C00000'],
                     title_txt='HCO₃⁻ y pCO₂', size=10.5, smooth=False, name='Gráfico evolución', labels=True)
    hh = formula(s, 8.25, 4.1, 4.7, 0.6, '6,1 + log(22 / (0,03 × 37)) ≈ 7,40', 15)
    t = tbox(s, 8.25, 4.85, 4.7, 2.05, 'Con 22 y 37 la ecuación predice **≈ 7,40**: diferencia pequeña frente a 7,37, atribuible a redondeo. Normalización parcial con **déficit de base leve**.', 13.5, head='Pregunta 6')
    s.step(fade(cid)); s.step(fade(hh)); s.step(fade(t))
    s.note('Evolución a las 24 h comparada con el ingreso. Pregunta 6: el estado ácido-base está casi normalizado (pH 7,37; HCO₃⁻ '
           '22; pCO₂ 37). Henderson–Hasselbalch con 22 y 37: 0,03 × 37 = 1,11; 22/1,11 = 19,8; log = 1,297; pH ≈ 7,40, una '
           'diferencia pequeña atribuible a redondeo o medición: puede describirse normalización parcial con déficit de base leve. '
           'La glucemia de 200 mg/dL supone mejoría pero no prueba resolución por sí sola. El gráfico de líneas muestra el ascenso '
           'del bicarbonato y de la pCO₂ al disminuir la necesidad de compensación.')


def resolution(D):
    s = new(D, U, 'Pregunta 7 · cómo se apagan la cetogénesis y la acidosis', 'green')
    nodes = {
        'i': (0.4, 1.3, 3.0, 0.65, 'Insulina efectiva', 'y', 17),
        'l': (4.0, 1.3, 4.1, 0.6, 'Lipólisis adiposa ↓ (PDE3B)', 'Y', 14),
        'a': (4.0, 2.2, 4.1, 0.6, 'Entrega hepática de AGNE ↓', 'Y', 14),
        'k': (4.0, 3.1, 4.1, 0.6, 'Cetogénesis ↓ (malonil-CoA ↑, CPT1 frenada)', 'Y', 12.5),
        'u': (4.0, 4.0, 4.1, 0.6, 'Utilización periférica de cetonas ↑', 'Y', 13.5),
        'h': (0.4, 3.1, 3.0, 0.65, 'Hidratación', 's', 16),
        'p': (0.4, 4.0, 3.0, 0.6, 'Perfusión y excreción ↑', 'Y', 13.5),
        'o': (8.7, 2.2, 4.25, 1.3, 'HCO₃⁻ se regenera · pH ↑ · pCO₂ ↑', 'r', 16),
    }
    edges = [('i', 'l'), ('l', 'a'), ('a', 'k'), ('k', 'u'), ('h', 'p'), ('u', 'o', {'pts': [(8.15, 4.3), (8.65, 3.2)]}), ('p', 'o', {'pts': [(3.45, 4.3), (3.7, 4.85), (10.8, 4.85), (10.8, 3.55)]})]
    graph(s, nodes, edges, [['i', 'i>l', 'l', 'l>a', 'a', 'a>k', 'k', 'k>u', 'u'], ['h', 'h>p', 'p'], ['u>o', 'p>o', 'o']])
    c = tbox(s, 0.4, 5.15, 12.55, 1.75, '- Resolución moderna: **β-OHB < 0,6 mmol/L** y **pH ≥ 7,3** o **HCO₃⁻ ≥ 18**, entre otros controles.\n- Pruebas cualitativas negativas son **consistentes** con mejoría, pero el criterio se basa en **β-OHB sanguíneo**, no en la desaparición de la cetonuria.', 14.5, head='Criterio de resolución')
    s.step(fade(c))
    s.note('Pregunta 7. Con reposición de insulina efectiva se inhibe la lipólisis adiposa, disminuye la entrega hepática de ácidos '
           'grasos, se atenúa la cetogénesis y aumenta la utilización periférica de cetonas; la hidratación mejora la perfusión y la '
           'excreción. Las pruebas cualitativas negativas son consistentes con mejoría, pero el criterio moderno de resolución se '
           'basa preferentemente en β-hidroxibutirato sanguíneo (<0,6 mmol/L) junto con pH ≥7,3 o HCO₃⁻ ≥18 [consenso 2024].')


def treatment(D):
    s = new(D, U, 'Integración terapéutica conceptual de la CAD', 'cyanR')
    pil = [('LÍQUIDOS IV', 'Restituyen volumen y perfusión; mejoran FG y la excreción de glucosa y cetonas.', 's'),
           ('INSULINA', 'Detiene lipólisis y cetogénesis; es el tratamiento **causal** de la cetoacidosis.', 'y'),
           ('POTASIO', 'Monitorizar y reponer: la insulina introduce K⁺ en las células.', 'g'),
           ('DESENCADENANTE', 'Tratar la neumonía según gravedad, microbiología y guías institucionales.', 'b')]
    ids = []
    for i, (h, t, k) in enumerate(pil):
        x = 0.4 + i * 3.17
        g = s.group_start('Pilar ' + h)
        mbox(s, x, 1.2, 3.0, 0.6, h, k, 16)
        tbox(s, x, 1.9, 3.0, 1.75, t, 14, anchor='m')
        ids.append(s.group_end())
    b = tbox(s, 0.4, 3.9, 6.15, 2.1, 'El caso informa hidratación, **80 mEq de bicarbonato IV** y ceftriaxona, pero **no informa insulina ni K⁺**. El bicarbonato **no** detiene la cetogénesis; no se recomienda de rutina: el consenso 2024 sólo plantea considerarlo con **pH < 7,0**.', 13.5, head='Análisis crítico del relato')
    d = tbox(s, 6.8, 3.9, 6.15, 2.1, 'Cuando la glucosa baja a un umbral protocolizado se **añade dextrosa** para **mantener la insulina** hasta resolver la cetosis. En la transición IV → SC se **superpone la insulina basal** varias horas.', 13.5, head='Glucosa y transición')
    p = pearl(s, 0.4, 6.2, 12.55, 0.7, 'Contenido formativo: el tratamiento real requiere **protocolos clínicos y supervisión**. Corregir pH ≠ corregir la causa.', 14)
    for g in ids:
        s.step(fade(g))
    s.step(fade(b)); s.step(fade(d)); s.step(zoom(p))
    s.note('Integración terapéutica conceptual, sin convertir la clase en una receta. Pilares: líquidos IV, insulina, '
           'monitorización/reposición de potasio y tratamiento del desencadenante. El caso informa hidratación abundante, 80 mEq '
           'de bicarbonato IV y ceftriaxona, pero no informa insulina durante la terapia intensiva ni valores de K⁺: esa omisión '
           'narrativa no debe interpretarse como que el bicarbonato cura la cetogénesis. La administración de bicarbonato de rutina '
           'no se recomienda; el consenso 2024 sólo plantea considerarlo en acidosis muy grave (pH <7,0). Con pH declarado 7,15, los '
           '80 mEq no constituyen una indicación rutinaria apoyada por guías. Cuando la glucosa disminuye a un umbral protocolizado '
           'se añade dextrosa para mantener la insulina hasta resolver la cetosis; en la transición IV → SC debe superponerse la '
           'basal varias horas. La cobertura antibiótica depende de gravedad, microbiología, epidemiología local y alergias: la '
           'ceftriaxona forma parte de la historia clínica, no de una receta estandarizada [C24, ADA26].')


def k_critical(D):
    s = new(D, U, 'Potasio crítico antes de la insulina', 'pink')
    nodes = {
        'k': (0.4, 1.3, 3.2, 0.7, 'K⁺ inicial medido', 'y', 17),
        'lo': (4.3, 1.3, 3.8, 0.7, 'K⁺ < 3,5 mmol/L', 'r', 17),
        'c': (8.8, 1.3, 4.15, 0.7, 'Corregir ANTES de iniciar insulina', 'Y', 14),
        'ok': (4.3, 2.55, 3.8, 0.7, 'K⁺ suficiente', 'g', 17),
        'm': (8.8, 2.55, 4.15, 0.7, 'Monitorizar y reponer según protocolo y función renal', 'Y', 12.5),
    }
    edges = [('k', 'lo'), ('lo', 'c'), ('k', 'ok', {'pts': [(2.0, 2.05), (2.0, 2.9), (4.25, 2.9)]}), ('ok', 'm')]
    graph(s, nodes, edges, [['k'], ['k>lo', 'lo', 'lo>c', 'c'], ['k>ok', 'ok', 'ok>m', 'm']])
    pump = s.group_start('Bomba')
    s.shape(0.4, 3.8, 6.2, 2.9, 'roundRect', ('lin', [(0, 'FDEDEC'), (100, 'F5B7B1')], 90), ('B03A2E', 2.5), SHD, adj={'adj': 10000})
    s.shape(2.7, 3.65, 1.4, 0.6, 'roundRect', shade('58D68D', 0.4, 0.3), ('1D8348', 1.2), False, 'Na⁺/K⁺-ATPasa', 11, F_HEAD, INK, True, 'c', 'm')
    lab(s, 0.6, 6.25, 5.8, 0.35, 'La insulina activa la bomba → K⁺ entra a la célula', 12.5)
    s.group_end()
    kk = [mol(s, 2.0 + i * 0.6, 3.05, 'k', d=0.4, name='K bomba %d' % i) for i in range(4)]
    ins = mol(s, 4.4, 3.0, 'ins', d=0.5, name='Insulina bomba')
    r = pearl(s, 6.9, 3.8, 6.05, 2.9, 'Si se administra insulina a una persona **muy hipopotasémica**, el K⁺ penetra en las células y puede precipitar **arritmias**. Por eso el potasio se mide **antes** y de forma **seriada**.', 16)
    s.step(fade(pump), zoom(ins, after=True))
    s.step(*[path(k_, 0.0, 1.6, dur=1200, delay=i * 150) for i, k_ in enumerate(kk)])
    s.step(zoom(r))
    s.note('Potasio crítico: si el K⁺ inicial es menor de 3,5 mmol/L se corrige antes de iniciar insulina por riesgo de arritmia; si '
           'es suficiente, se monitoriza y repone según protocolo y función renal. La insulina hace entrar potasio por activación de '
           'la Na⁺/K⁺-ATPasa (animación: las fichas de K⁺ ingresan a la célula). Razonamiento de seguridad aplicable también al EHH '
           '[C24, ADA26].')


def build(D):
    d1(D)
    d2(D)
    d3(D)
    d4(D)
    d5(D)
    potassium(D)
    infection(D)
    circuit(D)
    ketone_tests(D)
    diagnosis(D)
    gas_check(D)
    gas_alt(D)
    winter(D)
    anion_gap(D)
    symptoms(D)
    evolution(D)
    resolution(D)
    treatment(D)
    k_critical(D)
