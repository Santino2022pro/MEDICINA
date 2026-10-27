# -*- coding: utf-8 -*-
"""UNIDAD I (d) — Mapas 1 y 2 (alimentado / ayuno), tabla por órganos, diagnóstico, HbA1c, glucotoxicidad y complicaciones"""
from base import *

U = 1

ORG = [('small-intestine', 0.45, 1.1, 1.6, 'INTESTINO', 0.5, 2.75),
       ('pancreas', 4.6, 1.05, 2.6, 'PÁNCREAS', 5.25, 2.15),
       ('healthy_liver', 0.4, 3.9, 2.4, 'HÍGADO', 0.85, 5.65),
       ('muscle-fiber', 5.0, 5.0, 2.4, 'MÚSCULO', 5.6, 6.2),
       ('adipocyte-1', 10.7, 4.1, 1.8, 'TEJIDO ADIPOSO', 10.55, 5.95),
       ('brain-2', 11.0, 1.0, 1.35, 'CEREBRO', 11.05, 2.4)]


def map_fed(D):
    stages = [
        [('a', [(2.1, 1.7), (4.55, 1.65)], 'glucosa · AA · QM', INK, (2.45, 1.2)),
         ('b', 2.2, 2.3, 2.1, 0.45, 'Incretinas GLP-1/GIP', 's', 12.5),
         ('b', 7.55, 1.3, 2.6, 0.55, 'INSULINA ↑ · glucagón ↓', 'y', 13)],
        [('a', [(5.4, 2.1), (2.75, 4.0)], 'insulina portal', ACT),
         ('t', 2.95, 4.1, 2.0, 1.3, '**Hígado**: glucógeno ↑, glucólisis ↑, lipogénesis ↑, **PHG ↓**', 11.5),
         ('a', [(6.0, 2.2), (6.0, 4.95)], 'GLUT4', ACT),
         ('t', 7.55, 5.25, 2.6, 1.05, '**Músculo**: captación ↑, glucógeno ↑, síntesis proteica ↑', 11.5),
         ('a', [(7.2, 1.95), (10.75, 4.3)], 'GLUT4 · LPL', ACT),
         ('t', 8.45, 4.15, 2.15, 1.0, '**Adiposo**: TAG ↑, **lipólisis ↓**', 11.5),
         ('a', [(10.2, 1.55), (10.95, 1.5)], 'glucosa', INK, (10.15, 1.9))],
    ]
    map_series(D, U, 'Mapa 1 · estado alimentado', 'green', ORG, stages,
               ['Mapa 1, etapa 1. Tras una comida el intestino absorbe glucosa, aminoácidos y lípidos (quilomicrones). La glucosa y las '
                'incretinas GLP-1 y GIP estimulan la célula β: sube la insulina y baja el glucagón.',
                'Mapa 1, etapa 2. La insulina llega primero al hígado por la vena porta y suprime la producción hepática de glucosa (PHG), '
                'aumenta glucógeno, glucólisis y lipogénesis. En músculo y adiposo transloca GLUT4; en el adiposo favorece la '
                'esterificación (LPL capilar) e inhibe la lipólisis. El cerebro sigue utilizando glucosa como sustrato principal.'],
               'Mapa 1 completo: páncreas → insulina → hígado, músculo y adipocito → captación, utilización y almacenamiento energético. '
               'Es el estado de referencia que se pierde en la diabetes.',
               (0.4, 6.63, 12.5, 0.42, '**Insulina = señal de abundancia**: captar, utilizar y almacenar.', 14),
               ['ingesta e insulina', 'acción en tejidos'])


def map_fast(D):
    stages = [
        [('b', 7.55, 1.3, 2.6, 0.55, 'INSULINA ↓ · GLUCAGÓN ↑', 'y', 13),
         ('a', [(5.4, 2.1), (2.75, 4.0)], 'glucagón portal', INK),
         ('t', 2.95, 3.2, 2.0, 1.05, '**Hígado**: glucogenólisis → **gluconeogénesis** ↑', 11.5)],
        [('a', [(10.65, 4.5), (2.85, 4.5)], 'AGNE · glicerol', TRN, (5.4, 4.05), 'dash'),
         ('a', [(10.65, 4.8), (7.45, 5.15)], 'AG', TRN, (8.7, 4.72), 'dash'),
         ('t', 7.55, 5.3, 2.7, 1.0, '**Músculo**: oxida AG; proteólisis → alanina', 11.5),
         ('a', [(5.0, 5.75), (2.85, 5.05)], 'alanina', INK),
         ('a', [(2.0, 3.85), (2.6, 2.95), (10.95, 1.95)], 'glucosa · (cetonas en ayuno prolongado)', INK, (6.0, 2.6)),
         ('b', 2.2, 2.3, 2.3, 0.45, 'Riñón: gluconeogénesis', 'g', 12)],
    ]
    map_series(D, U, 'Mapa 2 · ayuno', 'peach', ORG, stages,
               ['Mapa 2, etapa 1. Al bajar la insulina y subir la relación glucagón/insulina, el hígado pasa de almacenar a producir '
                'glucosa: primero por glucogenólisis y, a medida que el ayuno se prolonga, por gluconeogénesis.',
                'Mapa 2, etapa 2. El adipocito libera ácidos grasos no esterificados (AGNE, unidos a albúmina) y glicerol, sustrato de '
                'la gluconeogénesis. El músculo recurre más a la oxidación de lípidos y aporta aminoácidos (alanina). El encéfalo '
                'puede utilizar cuerpos cetónicos en ayuno prolongado; los eritrocitos siempre dependen de glucosa. El riñón también '
                'contribuye a la gluconeogénesis.'],
               'Mapa 2 completo: disminución de insulina → lipólisis y producción hepática de glucosa → cambio de utilización de '
               'sustratos. En la DM1 sin insulina estas adaptaciones de ayuno se exacerban de forma patológica hasta la cetoacidosis.',
               (0.4, 6.63, 12.5, 0.42, 'En la **DM1 sin insulina** este programa se exagera hasta la **cetoacidosis**.', 14),
               ['cambio hormonal', 'movilización de sustratos'])


def organ_table(D):
    s = new(D, U, 'Metabolismo por órganos: alimentado, ayuno y déficit de insulina', 'blue', tsize=30)
    rows = [['Órgano', 'Bajo insulina posprandial', 'Ayuno / déficit de insulina', 'Consecuencia clínica'],
            ['Hígado', 'Glucógeno ↑, glucólisis ↑, lipogénesis ↑; producción neta de glucosa ↓', 'Glucogenólisis y gluconeogénesis ↑; β-oxidación ↑ y, si el contexto lo permite, cetogénesis ↑', 'Glucosa plasmática ↑; cetonas ↑ en DM1'],
            ['Músculo', 'GLUT4 en membrana; glucógeno y síntesis proteica ↑', 'Captación de glucosa ↓; uso de ácidos grasos ↑; proteólisis en déficit grave', 'Debilidad, pérdida de masa magra'],
            ['Tejido adiposo blanco', 'GLUT4 y esterificación ↑; lipólisis ↓', 'ATGL/HSL ↑, liberación de ácidos grasos y glicerol', 'Sustrato hepático para cetonas y gluconeogénesis'],
            ['Páncreas', 'Secreción β estimulada por glucosa/incretinas', 'Predomina relación glucagón/insulina elevada', 'Cambio sistémico a estado catabólico'],
            ['Riñón', 'Reabsorción habitual de glucosa', 'Hiperglucemia sobrecarga SGLT2/SGLT1 → glucosuria; contribución a gluconeogénesis', 'Diuresis osmótica y deshidratación'],
            ['SNC / eritrocitos', 'Glucosa como sustrato central; eritrocitos glucolíticos', 'Encéfalo puede usar cetonas en ayuno prolongado; eritrocitos siempre glucosa', 'Vulnerabilidad del sensorio a hiperosmolalidad / hipoperfusión']]
    tid, H = table(s, 0.4, 1.2, 12.5, rows, [1.6, 3.4, 4.0, 3.0], size=12.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla órganos')
    s.note('Tabla por órganos (alimentado frente a ayuno o déficit de insulina) con su consecuencia clínica. Leerla por filas '
           'permite anticipar los hallazgos de la cetoacidosis: hiperglucemia por producción hepática y menor captación, cetonas por '
           'β-oxidación y cetogénesis, pérdida de masa magra por proteólisis, sustrato adiposo para el hígado, predominio de '
           'glucagón, glucosuria y diuresis osmótica, y vulnerabilidad del sensorio a la hiperosmolalidad y la hipoperfusión.')


def diag(D):
    s = new(D, U, 'Diagnóstico bioquímico: criterios ADA 2026', 'cyan')
    rows = [['Prueba (personas no embarazadas)', 'Diabetes', 'Prediabetes (riesgo elevado)'],
            ['Glucemia plasmática en ayunas (≥ 8 h)', '≥ 126 mg/dL', '100–125 mg/dL'],
            ['Glucemia 2 h tras 75 g (PTOG)', '≥ 200 mg/dL', '140–199 mg/dL'],
            ['HbA1c estandarizada NGSP/DCCT', '≥ 6,5 %', '5,7–6,4 %'],
            ['Glucemia al azar + síntomas clásicos o crisis hiperglucémica', '≥ 200 mg/dL', 'No se define prediabetes con este criterio']]
    tid, H = table(s, 0.4, 1.2, 8.2, rows, [3.8, 1.8, 2.6], size=14, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla criterios')
    steps_panel(s, 8.9, 1.2, 4.05, ['Sin hiperglucemia inequívoca: **dos resultados anormales** (misma prueba repetida o dos pruebas distintas).',
                                     'Si son **discordantes**, se repite la prueba situada sobre el umbral.',
                                     'Un valor aislado de **145 mg/dL** no demuestra diabetes sin saber si fue en ayunas, el contexto y la confirmación.'], 14)
    s.note('Criterios diagnósticos ADA 2026 en personas no embarazadas: glucemia plasmática en ayunas ≥126 mg/dL (prediabetes '
           '100–125), glucemia a las 2 h de una PTOG con 75 g ≥200 mg/dL (prediabetes 140–199), HbA1c estandarizada NGSP/DCCT '
           '≥6,5 % (prediabetes 5,7–6,4 %) o glucemia al azar ≥200 mg/dL con síntomas clásicos o crisis hiperglucémica. '
           'Confirmación: si no existe hiperglucemia inequívoca se necesitan dos resultados anormales, de la misma prueba repetida '
           'o de dos pruebas distintas; si son discordantes se repite la prueba que está sobre el umbral. Un valor aislado de 145 '
           'mg/dL (como el del caso 20) no demuestra diabetes sin conocer si fue en ayunas, el contexto y una confirmación.')


def hba1c(D):
    s = new(D, U, 'HbA1c: glucación no enzimática de la hemoglobina', 'peach')
    for i in range(5):
        rbc(s, 0.4 + (i % 3) * 1.0, 1.25 + (i // 3) * 0.75, 0.9, name='Eritrocito %d' % i)
    nodes = {
        'hb': (3.9, 1.3, 2.6, 0.6, 'Hb: valina N-terminal\nde la cadena β (–NH₂)', 'g', 12.5),
        'gl': (7.0, 1.3, 1.6, 0.6, 'GLUCOSA', 'y', 15),
        'sb': (3.9, 2.55, 4.7, 0.6, 'Base de Schiff (aldimina) · reversible', 'w', 14),
        'am': (3.9, 3.7, 4.7, 0.6, 'Reordenamiento de Amadori · cetoamina estable', 'w', 13.5),
        'a1c': (3.9, 4.85, 4.7, 0.65, 'HbA1c', 'y', 20),
    }
    edges = [('hb', 'sb'), ('gl', 'sb'), ('sb', 'am', {'lab': 'horas', 'ls': 10.5, 'ox': 0.6}), ('am', 'a1c', {'lab': 'días · irreversible', 'ls': 10.5, 'ox': 0.95})]
    graph(s, nodes, edges, [['hb', 'gl'], ['hb>sb', 'gl>sb', 'sb'], ['sb>am', 'am'], ['am>a1c', 'a1c']])
    model(s, 'glucosa', 7.25, 0.55, 1.15, name='Glucosa 3D A1c')
    tl = s.group_start('Ventana temporal')
    lab(s, 9.0, 1.25, 3.9, 0.35, 'EXPOSICIÓN QUE REFLEJA', 13)
    for i, (w, c) in enumerate([(0.9, 'F8CBAD'), (0.9, 'F4B183'), (0.9, 'ED7D31'), (1.1, 'C55A11')]):
        s.shape(9.0 + sum([0.9, 0.9, 0.9, 1.1][:i]) + i * 0.03, 1.7, w, 0.45, 'rect', c, (INK, 1.0), False)
    s.text(9.0, 2.2, 3.9, 0.6, '≈ 8–12 semanas · mayor peso de las semanas **recientes**', 13, F_BODY, INK, False, 'c', 't')
    s.group_end()
    p = pearl(s, 9.0, 3.0, 3.95, 1.5, 'Glucación (no enzimática, depende de concentración y tiempo) **≠ glucosilación** (enzimática).', 14)
    t = tbox(s, 0.4, 5.75, 12.55, 1.15, 'La HbA1c es un **promedio ponderado** de semanas: una glucemia aislada es una instantánea. Su interpretación depende de la **vida media eritrocitaria**.', 15, anchor='m')
    s.step(fade(tl)); s.step(zoom(p)); s.step(fade(t))
    s.note('HbA1c. La glucosa reacciona de manera no enzimática con grupos amino libres de la hemoglobina, principalmente la valina '
           'N-terminal de la cadena β: primero forma una base de Schiff (aldimina) reversible y luego, por reordenamiento de '
           'Amadori, una cetoamina estable (HbA1c). La velocidad depende de la concentración de glucosa y del tiempo de exposición, '
           'por eso refleja aproximadamente 8–12 semanas, con mayor ponderación de las semanas recientes. No es lo mismo que la '
           'glucosilación enzimática de proteínas. Los tiempos «horas/días» son orientativos (ampliación bibliográfica).')


def hba1c_bias(D):
    s = new(D, U, 'HbA1c: sesgos y glucemia promedio estimada', 'green')
    rows = [['Situación', 'Mecanismo del sesgo'],
            ['Anemia ferropénica', 'Eritrocitos más longevos → tiende a sobrestimar'],
            ['Hemólisis · transfusiones', 'Población eritrocitaria joven o ajena → subestima'],
            ['Embarazo avanzado', 'Recambio eritrocitario aumentado'],
            ['Enfermedad renal · eritropoyetina', 'Vida eritrocitaria y reticulocitosis alteradas'],
            ['Hemoglobinopatías', 'Interferencia analítica o vida media distinta']]
    table(s, 0.4, 1.2, 6.3, rows, [2.5, 3.8], size=13.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla sesgos')
    f = formula(s, 7.1, 1.25, 5.85, 0.9, 'eAG (mg/dL) = 28,7 × HbA1c (%) − 46,7', 20)
    c1 = formula(s, 7.1, 2.4, 5.85, 0.75, '28,7 × 12 − 46,7 = 344,4 − 46,7', 18, fill='FFF2CC')
    c2 = formula(s, 7.1, 3.35, 5.85, 0.8, '≈ 297,7 mg/dL', 26, fill=BOX, color=BOXT)
    t = tbox(s, 7.1, 4.4, 5.85, 2.45, 'Caso 11: HbA1c **12 %** → promedio ≈ **298 mg/dL**, pese a una glucemia en ayunas aislada de **160 mg/dL**. '
             'Explicaciones: picos posprandiales, variabilidad, subregistro, cambios recientes o problemas de medición. Indica **control marcadamente insuficiente**.', 14.5, head='Interpretación')
    p = tbox(s, 0.4, 5.15, 6.3, 1.7, 'En esas situaciones puede preferirse la **glucosa plasmática** o marcadores alternativos validados.', 15, anchor='m')
    s.step(fade(p)); s.step(fade(f)); s.step(fade(c1)); s.step(zoom(c2)); s.step(fade(t))
    s.note('La duración y el recambio eritrocitario modifican la interpretación de la HbA1c: anemia ferropénica, hemólisis, '
           'transfusiones, embarazo avanzado, enfermedad renal, hemoglobinopatías y uso de eritropoyetina pueden sesgarla; en esas '
           'situaciones puede preferirse la glucosa plasmática o marcadores alternativos validados (la dirección del sesgo en cada '
           'fila es ampliación bibliográfica). Glucemia promedio estimada: eAG = 28,7 × HbA1c − 46,7. Para HbA1c 12 %: 28,7 × 12 = '
           '344,4; 344,4 − 46,7 = 297,7 mg/dL. En el paciente del caso 11, con DM1, este valor indica control marcadamente '
           'insuficiente aunque una glucemia basal aislada fuera 160 mg/dL.')


def glucotox(D):
    s = new(D, U, 'Glucotoxicidad: cinco vías bioquímicas convergentes', 'cyanR')
    c = mbox(s, 4.9, 1.25, 3.55, 0.7, 'HIPERGLUCEMIA SOSTENIDA', 'y', 16)
    paths = [('AGE', 'Glucación avanzada\n(productos finales)', 0.4), ('RAGE', 'Unión a RAGE →\nNF-κB · citocinas', 2.95), ('PKC', 'DAG de novo →\nactivación de PKC', 5.5),
             ('POLIOLES', 'Aldosa reductasa:\nsorbitol · NADPH ↓', 8.05), ('HEXOSAMINAS', 'Fructosa-6-P →\nUDP-GlcNAc', 10.6)]
    ids = []
    for h, t, x in paths:
        g = s.group_start('Vía ' + h)
        s.arrow([(6.67, 1.98), (x + 1.17, 2.55)], INK, 2.25)
        mbox(s, x, 2.6, 2.35, 0.5, h, 's', 15)
        tbox(s, x, 3.15, 2.35, 0.95, t, 13, anchor='m')
        ids.append(s.group_end())
    ros = mbox(s, 3.2, 4.45, 6.95, 0.62, 'ESPECIES REACTIVAS DE OXÍGENO · ESTRÉS ENDOTELIAL', 'r', 15)
    out = s.group_start('Convergencia')
    for i, t in enumerate(['Fibrosis', 'Matriz extracelular alterada', 'Inflamación', 'Disfunción vascular']):
        mbox(s, 0.4 + i * 3.15, 5.45, 2.95, 0.6, t, 'g', 14, caps=False)
    s.group_end()
    dm = tbox(s, 0.4, 6.25, 12.55, 0.65, 'Daño **renal, nervioso y retiniano** (microangiopatía) y aceleración de la aterosclerosis (macroangiopatía).', 15, anchor='m')
    s.step(zoom(c))
    for g in ids:
        s.step(fade(g))
    s.step(zoom(ros)); s.step(fade(out)); s.step(fade(dm))
    s.note('Mecanismos bioquímicos de glucotoxicidad. La hiperglucemia sostenida incrementa la formación de productos finales de '
           'glicación avanzada (AGE) y su interacción con el receptor RAGE, especies reactivas de oxígeno, activación de PKC, flujo '
           'por la vía de los polioles (aldosa reductasa) y por la vía de las hexosaminas, y estrés endotelial. Los efectos '
           'convergen en fibrosis, alteración de la matriz extracelular, inflamación, disfunción vascular y daño renal, nervioso y '
           'retiniano. Los detalles moleculares de cada vía (DAG de novo, consumo de NADPH, UDP-GlcNAc, NF-κB) son ampliación '
           'bibliográfica; las vías se animan en paralelo porque operan simultáneamente.')


def age_rage(D):
    s = new(D, U, 'AGE y RAGE: del azúcar al daño endotelial', 'pink')
    s.pic('vein-crossection-3d', 0.3, 1.2, 4.2, name='Vaso AGE')
    nodes = {
        'p': (4.9, 1.3, 2.6, 0.55, 'Proteínas de larga vida\n(colágeno, matriz)', 'w', 12.5),
        'age': (8.0, 1.3, 2.0, 0.55, 'AGE', 'y', 18),
        'x': (10.6, 1.3, 2.35, 0.55, 'Entrecruzamiento:\nrigidez de matriz', 'Y', 12.5),
        'r': (8.0, 2.55, 2.0, 0.55, 'RAGE', 'g', 18),
        'ros': (4.9, 3.75, 2.6, 0.6, 'NADPH oxidasa → ROS', 's', 14),
        'nf': (8.0, 3.75, 2.0, 0.6, 'NF-κB', 's', 17),
        'cy': (10.6, 3.75, 2.35, 0.6, 'Citocinas · moléculas\nde adhesión', 's', 12.5),
        'no': (4.9, 5.0, 8.05, 0.65, 'Menor biodisponibilidad de NO · permeabilidad ↑ · procoagulación', 'r', 14.5),
    }
    edges = [('p', 'age'), ('age', 'x'), ('age', 'r'), ('r', 'ros', {'pts': [(7.95, 2.85), (6.2, 2.85), (6.2, 3.7)]}), ('r', 'nf'), ('nf', 'cy'),
             ('ros', 'nf', {'col': ACT}), ('ros', 'no', {'pts': [(6.2, 4.4), (6.2, 4.95)]}), ('cy', 'no', {'pts': [(11.8, 4.4), (11.8, 4.95)]})]
    graph(s, nodes, edges, [['p', 'p>age', 'age'], ['age>x', 'x'], ['age>r', 'r'], ['r>ros', 'ros', 'r>nf', 'nf', 'ros>nf'], ['nf>cy', 'cy'], ['ros>no', 'cy>no', 'no']])
    t = tbox(s, 0.4, 5.9, 12.55, 1.0, 'Los AGE se acumulan en proteínas de recambio lento: el daño **persiste** aunque la glucemia mejore («memoria metabólica», ampliación).', 14.5, anchor='m')
    s.step(fade(t))
    s.note('AGE y RAGE. Las proteínas de vida media larga (colágeno, matriz) sufren glicación avanzada; los AGE producen '
           'entrecruzamientos que rigidizan la matriz y se unen a RAGE en endotelio y macrófagos, activando NADPH oxidasa (especies '
           'reactivas de oxígeno) y NF-κB (citocinas y moléculas de adhesión). El resultado es menor biodisponibilidad de óxido '
           'nítrico, mayor permeabilidad y un ambiente procoagulante: disfunción endotelial. El material de cátedra enuncia AGE, RAGE, ROS, '
           'PKC y estrés endotelial; el detalle de NADPH oxidasa, NF-κB y «memoria metabólica» es ampliación bibliográfica.')


def micro(D):
    s = new(D, U, 'Complicaciones microvasculares', 'yellow')
    cols = [('diabetic-retinopathy-eye', 'RETINOPATÍA', 'Microaneurismas, hemorragias, edema macular y neovascularización.'),
            ('kidney-1', 'ENFERMEDAD RENAL DIABÉTICA', 'Albuminuria y/o disminución de la TFG; hiperfiltración inicial.'),
            ('Pyramidal_Neuron', 'NEUROPATÍA', 'Periférica (dolor, pérdida de sensibilidad protectora) y autonómica (gastroparesia, disfunción CV y sexual).')]
    ids = []
    for i, (img, h, t) in enumerate(cols):
        x = 0.4 + i * 4.2
        g = s.group_start('Micro ' + h)
        fitpic(s, img, x + 0.6, 1.2, 2.9, 2.5)
        mbox(s, x, 3.85, 4.0, 0.55, h, 'y', 14)
        tbox(s, x, 4.5, 4.0, 1.45, t, 14.5, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 6.15, 12.55, 0.75, 'Prevención integral: control glucémico **individualizado**, presión, lípidos, función renal, retina, pies, tabaquismo y vacunación.', 15)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Microangiopatía: retinopatía (microaneurismas, hemorragias, edema macular y neovascularización), enfermedad renal '
           'diabética (albuminuria y/o disminución de la tasa de filtración glomerular; la hiperglucemia puede generar '
           'hiperfiltración inicial y luego daño glomerular) y neuropatía periférica y autonómica (dolor, pérdida de sensibilidad '
           'protectora, gastroparesia, disfunción cardiovascular y sexual). La prevención requiere control glucémico '
           'individualizado y abordar presión, lípidos, función renal, retina, pies, tabaquismo y vacunación; no basta con '
           'normalizar una glucemia aislada.')


def macro_acute(D):
    s = new(D, U, 'Macroangiopatía y daño agudo por hiperglucemia', 'peach')
    l = s.group_start('Macro')
    mbox(s, 0.4, 1.2, 6.1, 0.55, 'MACROANGIOPATÍA (LARGO PLAZO)', 'y', 15)
    fitpic(s, 'heart-front', 0.5, 1.9, 1.6, 1.9); fitpic(s, 'brain-2', 2.3, 2.0, 1.7, 1.7); fitpic(s, 'aorta-body', 4.4, 1.85, 1.9, 2.0)
    tbox(s, 0.4, 4.0, 6.1, 1.65, 'Enfermedad **coronaria**, **cerebrovascular** y **arterial periférica**. La aterosclerosis surge de la hiperglucemia **y** de factores acompañantes: LDL, HTA, inflamación, tabaquismo.', 14.5, anchor='m')
    tbox(s, 0.4, 5.8, 6.1, 1.1, 'Otras: pie diabético, infecciones, periodontitis, esteatosis hepática, complicaciones sexuales.', 14, anchor='m')
    s.group_end()
    r = s.group_start('Agudo')
    mbox(s, 6.85, 1.2, 6.1, 0.55, 'CORTO PLAZO', 's', 15)
    steps_panel(s, 6.85, 1.9, 6.1, ['Poliuria y deshidratación por glucosuria; trastornos de Na⁺/K⁺.', 'Hipotensión, lesión renal prerrenal; CAD, EHH o formas mixtas.',
                                    'Alteración del sensorio; trombosis por hemoconcentración.', 'Visión borrosa por cambios osmóticos del cristalino; infecciones y mala cicatrización.'], 14, anim=False)
    pearl(s, 6.85, 5.9, 6.1, 1.0, 'No todo coma en diabetes es hiperglucémico: evaluar **hipoglucemia, sepsis, ACV** y causas tóxico-metabólicas.', 14)
    s.group_end()
    s.step(fade(l)); s.step(fade(r))
    s.note('Pregunta 8 del caso 11 (daño agudo y crónico). A corto plazo: poliuria y deshidratación por glucosuria; trastornos de '
           'sodio y potasio; hipotensión y lesión renal prerrenal; CAD, EHH o formas mixtas; alteración del sensorio; trombosis '
           'favorecida por hemoconcentración; cambios de visión por variación osmótica del cristalino; infecciones y mala '
           'cicatrización. La glucemia extremadamente alta puede asociarse a coma, pero no todo coma en diabetes es '
           'hiperglucémico. A largo plazo, además de la microangiopatía: enfermedad coronaria, cerebrovascular y arterial '
           'periférica, donde la aterosclerosis surge de la hiperglucemia y de factores acompañantes (LDL, HTA, inflamación, '
           'tabaquismo); pie diabético, infecciones, enfermedad periodontal, esteatosis hepática y complicaciones sexuales.')


def build(D):
    map_fed(D)
    map_fast(D)
    organ_table(D)
    diag(D)
    hba1c(D)
    hba1c_bias(D)
    glucotox(D)
    age_rage(D)
    micro(D)
    macro_acute(D)
