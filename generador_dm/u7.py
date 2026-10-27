# -*- coding: utf-8 -*-
"""UNIDAD VII — Caso 20: obesidad clase III y sus complicaciones"""
from base import *

U = 7


def div(D):
    def art(s):
        s.pic('obese-man', 10.75, 0.45, h=3.2, name='Paciente')
        s.pic('heart-front', 11.0, 3.9, 1.6, name='Corazón')
        s.pic('healthy_liver', 0.25, 1.5, 2.2, name='Hígado')
        s.pic('bile-lithiasis-big-calculi', 0.6, 4.2, 1.4, name='Vesícula')
    divider(D, U, 'VII', 'CASO 20: OBESIDAD\nCLASE III', 'Cálculos, mecanismos y complicaciones',
            ['Presentación y laboratorio', 'Definición y clasificación', 'IMC y cintura', 'Gasto energético (Mifflin–St Jeor)',
             'Descenso 170 → 140 kg', 'Adipocito, apetito y DM2', 'HTA, dislipidemia, MASLD', 'Litiasis, pancreatitis, AOS'], art,
            'Unidad VII. Caso clínico 20: varón de 40 años con obesidad clase III. Se desarrollan los cálculos de IMC, gasto energético y '
            'descenso ponderal, la interpretación del laboratorio y cada complicación desde sus mecanismos fisiológicos, bioquímicos y '
            'celulares, con lenguaje no estigmatizante.')


def case(D):
    s = new(D, U, 'Caso 20 · presentación clínica', 'peach')
    s.pic('obese-man', 0.4, 1.1, h=5.8, name='Paciente caso 20')
    data = [('ANTROPOMETRÍA', '**170 kg** · talla **1,70 m** · cintura **124 cm**', 'y'),
            ('PRESIÓN ARTERIAL', '**160/100 mmHg** · ECG con **Sokolow–Lyon positivo**', 'r'),
            ('HÁBITOS', 'Sedentarismo extremo · alimentos hiperpalatables frecuentes · **tabaquismo 40 cigarrillos/día**', 's'),
            ('SUEÑO', '**Ronquidos intensos** y **somnolencia diurna**', 'b'),
            ('PSICOSOCIAL', 'Dificultades físicas y psicosociales · desempleo · aislamiento · **juego patológico**', 'g'),
            ('ANTECEDENTES', '**Pancreatitis biliar** · **hernia inguinal bilateral**', 'w')]
    ids = []
    for i, (h, t, k) in enumerate(data):
        y = 1.15 + i * 0.95
        g = s.group_start('Dato ' + h)
        mbox(s, 3.9, y, 2.6, 0.8, h, k, 13.5)
        tbox(s, 6.6, y, 6.35, 0.8, t, 14, anchor='m')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Caso 20. Varón de 40 años, 170 kg, talla 1,70 m, cintura 124 cm, TA 160/100 mmHg, sedentarismo extremo, ingesta frecuente de '
           'alimentos hiperpalatables, tabaquismo de 40 cigarrillos por día, ronquidos intensos y somnolencia diurna, dificultades '
           'físicas y psicosociales, juego patológico, antecedente de pancreatitis biliar y hernia inguinal bilateral. ECG con índice de '
           'Sokolow–Lyon positivo.')


def labs(D):
    s = new(D, U, 'Caso 20 · laboratorio y problemas identificables', 'green')
    rows = [['Analito', 'Valor', 'Lectura'], ['Glucosa', '145 mg/dL', 'Ayuno no especificado'], ['Colesterol total', '250 mg/dL', 'Elevado'],
            ['LDL-C', '183 mg/dL', 'Elevado (método no indicado)'], ['HDL-C', '30 mg/dL', 'Bajo'], ['Triglicéridos', '185 mg/dL', 'Elevados'],
            ['AST', '29 U/L', '«Normal»'], ['Función renal / iones', 'Normales', 'No excluye daño temprano']]
    table(s, 0.4, 1.15, 6.6, rows, [2.3, 1.6, 2.7], size=13.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Lab caso 20')
    probs = ['Obesidad clase III', 'Adiposidad central', 'HTA en cifras elevadas', 'Dislipidemia aterogénica', 'Hiperglucemia a confirmar',
             'Alta sospecha de AOS', 'Riesgo cardiometabólico', 'Tabaquismo', 'Movilidad e impacto psicosocial']
    ids = []
    for i, t in enumerate(probs):
        c = i % 2; r = i // 2
        ids.append(mbox(s, 7.3 + c * 2.85, 1.15 + r * 0.72, 2.75, 0.6, t, 'y' if i < 5 else 's', 12.5, caps=False, name='Problema %d' % i))
    p = pearl(s, 0.4, 5.25, 12.55, 1.6, 'Somnolencia y disnea exigen buscar **AOS**, **síndrome de hipoventilación por obesidad**, **EPOC** por tabaquismo y otros diagnósticos, **sin atribuir todo automáticamente a la obesidad**. Sokolow–Lyon orienta a HVI, **no la confirma**.', 14.5)
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids)])
    s.step(zoom(p))
    s.note('Laboratorio: glucosa 145 mg/dL (ayuno no especificado), colesterol total 250, LDL 183, HDL 30 y TG 185 mg/dL; AST 29 U/L; '
           'función renal e iones normales. Problemas clínicos identificables: obesidad clase III, adiposidad central, HTA en cifras '
           'elevadas, dislipidemia aterogénica, hiperglucemia a confirmar, muy alta sospecha de apnea obstructiva del sueño, riesgo '
           'cardiometabólico significativo, tabaquismo, dificultades de movilidad e impacto psicosocial. El índice ECG orienta a posible '
           'hipertrofia ventricular izquierda pero no la confirma; la ecocardiografía puede ser apropiada.')


def definition(D):
    s = new(D, U, 'Pregunta 1 · definición y clasificación de la obesidad', 'cyanR')
    d = tbox(s, 0.4, 1.15, 6.4, 2.7, 'Enfermedad **crónica, recidivante y multifactorial** caracterizada por **exceso de adiposidad que compromete la salud**, con factores **biológicos, ambientales, conductuales, psicológicos, sociales y económicos**.', 16, head='Definición')
    rows = [['Clasificación adulta por IMC', 'kg/m²'], ['Normopeso convencional', '18,5–24,9'], ['Sobrepeso', '25,0–29,9'],
            ['Obesidad clase I', '30,0–34,9'], ['Obesidad clase II', '35,0–39,9'], ['Obesidad clase III', '≥ 40,0']]
    t, H = table(s, 7.1, 1.15, 5.85, rows, [3.6, 2.25], size=15, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla IMC')
    hl = s.shape(7.06, 1.15 + H - H / 6 - 0.02, 5.93, H / 6 + 0.04, 'rect', None, ('C00000', 4), False, name='Marca clase III')
    c = tbox(s, 0.4, 4.1, 6.4, 1.6, 'El IMC **no mide** composición corporal, distribución de grasa ni el compromiso clínico: se complementa con **cintura, complicaciones, antecedentes y evaluación funcional**.', 14.5)
    p = pearl(s, 0.4, 5.95, 12.55, 0.9, 'Preferir «obesidad clase III con complicaciones» a términos históricos como «obesidad mórbida»: evitar expresiones **estigmatizantes**.', 15)
    s.step(fade(t), zoom(hl, after=True)); s.step(fade(c)); s.step(zoom(p))
    s.note('Pregunta 1. La obesidad es una enfermedad crónica, recidivante y multifactorial caracterizada por exceso de adiposidad que '
           'compromete la salud. El IMC es una aproximación antropométrica ampliamente utilizada; no mide composición corporal, '
           'distribución de grasa ni por sí solo el compromiso clínico. Los términos históricos «obesidad mórbida» o «superobesidad» '
           'aparecen en la literatura; es preferible obesidad clase III con complicaciones o especificar IMC y riesgo.')


def bmi(D):
    s = new(D, U, 'Pregunta 2 · cálculo del IMC', 'yellow')
    f = formula(s, 0.4, 1.2, 6.4, 0.9, 'IMC = masa (kg) / talla (m)²', 24)
    c1 = formula(s, 0.4, 2.3, 6.4, 0.75, '1,70² = 2,89 m²', 20, fill='FFF2CC')
    c2 = formula(s, 0.4, 3.25, 6.4, 0.75, '170 / 2,89', 20, fill='FFF2CC')
    c3 = formula(s, 0.4, 4.2, 6.4, 0.95, '= 58,82 kg/m²', 30, fill=BOX, color=BOXT)
    sc = s.group_start('Escala IMC')
    cats = [('18,5', 'C5E0B4', 1.3), ('25', 'FFE699', 1.0), ('30', 'F8CBAD', 1.0), ('35', 'F4B183', 1.0), ('40+', 'E06666', 2.4)]
    x = 7.2
    for t, c, w in cats:
        s.shape(x, 2.2, w, 0.7, 'rect', c, (INK, 1.0), False, t, 13, F_HEAD, INK, True, 'c', 'm')
        x += w
    lab(s, 7.2, 1.7, 6.7, 0.4, 'IMC (kg/m²) · normopeso → clase III', 13)
    s.group_end()
    mk = s.group_start('Marca 58,8')
    s.arrow([(12.4, 3.6), (12.4, 2.95)], 'C00000', 5)
    lab(s, 11.3, 3.6, 2.0, 0.4, '58,82', 18, INH)
    s.group_end()
    t = tbox(s, 7.2, 4.35, 5.75, 1.6, 'Clasificación: **obesidad clase III**. El valor por sí solo no describe composición ni distribución de la grasa.', 15, anchor='m')
    s.step(fade(c1)); s.step(fade(c2)); s.step(zoom(c3)); s.step(fade(sc), fade(mk, after=True)); s.step(fade(t))
    s.note('Pregunta 2. IMC = masa / talla² = 170 / 1,70² = 170 / 2,89 = 58,82 kg/m², obesidad clase III. Animación: cada paso del '
           'cálculo aparece por clic y luego se ubica el resultado en la escala de clases (la escala es ilustrativa, no proporcional).')


def waist(D):
    s = new(D, U, 'Cintura 124 cm: adiposidad central', 'peach')
    s.pic('excess-weight-male-clothed', 0.6, 1.1, h=5.8, name='Cintura figura')
    cin = s.shape(0.45, 3.35, 2.35, 0.45, 'ellipse', None, ('C00000', 4), False, name='Marca cintura')
    rows = [['Umbral (hombres)', 'Valor', 'Caso 20'], ['NCEP/ATP III clásico', 'más de 102 cm', '124 → excede'], ['IDF (poblaciones latinoamericanas)', '≥ 90 cm', '124 → excede']]
    t, H = table(s, 3.3, 1.2, 9.65, rows, [4.6, 2.0, 3.05], size=15, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Umbrales cintura')
    c = tbox(s, 3.3, 1.4 + H, 9.65, 1.9, 'La cintura **estima** adiposidad central; **no mide** directamente grasa visceral. La clasificación de riesgo depende de **población, sexo, etnicidad** y perfil cardiometabólico.', 15)
    p = pearl(s, 3.3, 3.55 + H, 9.65, 1.2, 'Siempre **nombrar la definición** usada: no mezclar umbrales entre consensos.', 16)
    s.step(zoom(cin)); s.step(fade(t)); s.step(fade(c)); s.step(zoom(p))
    s.note('La cintura de 124 cm excede tanto el umbral clásico NCEP/ATP III para hombres (102 cm) como el usado frecuentemente en '
           'criterios IDF para poblaciones latinoamericanas (90 cm): indica adiposidad central importante. Estima adiposidad central '
           'pero no mide grasa visceral.')


def mifflin(D):
    s = new(D, U, 'Gasto energético: ecuación de Mifflin–St Jeor', 'blue')
    f = formula(s, 0.4, 1.2, 12.55, 0.85, 'Hombres: GER = 10 × peso (kg) + 6,25 × talla (cm) − 5 × edad (años) + 5', 20)
    st = [formula(s, 0.4, 2.3, 6.1, 0.65, '10 × 170 = 1700', 18, fill='FFF2CC'),
          formula(s, 0.4, 3.05, 6.1, 0.65, '6,25 × 170 = 1062,5', 18, fill='FFF2CC'),
          formula(s, 0.4, 3.8, 6.1, 0.65, '5 × 40 = 200', 18, fill='FFF2CC'),
          formula(s, 0.4, 4.55, 6.1, 0.75, '1700 + 1062,5 − 200 + 5 = 2567,5 kcal/día', 17, fill=BOX, color=BOXT),
          formula(s, 0.4, 5.45, 6.1, 0.8, 'GET ≈ 2567,5 × 1,2 ≈ 3081 kcal/día', 19, fill=BOX, color=BOXT)]
    sup = tbox(s, 6.85, 2.3, 6.1, 3.95, '- Sexo masculino, 40 años, **peso real**.\n- Factor de actividad **1,2** por sedentarismo extremo.\n- Es un **estimador indirecto**, no calorimetría.\n'
               '- En obesidad clase III el **error puede ser sustancial**: ajustar con evolución de peso, ingesta y actividad, o **calorimetría indirecta** si está indicada.', 14.5, head='Supuestos y límites')
    for x in st:
        s.step(fade(x))
    s.step(fade(sup))
    s.note('Tasa metabólica de reposo por Mifflin–St Jeor (hombres): 10 × peso + 6,25 × talla(cm) − 5 × edad + 5. Sustitución: 10 × 170 '
           '+ 6,25 × 170 − 5 × 40 + 5 = 1700 + 1062,5 − 200 + 5 = 2567,5 kcal/día. Con factor de actividad 1,2 por sedentarismo extremo: '
           'GET ≈ 2567,5 × 1,2 = 3081 kcal/día. Es un estimador indirecto; en obesidad clase III su error puede ser sustancial.')


def methods(D):
    s = new(D, U, 'Por qué las ecuaciones no coinciden', 'cyan')
    st = steps_panel(s, 0.4, 1.2, 12.55, ['**Harris–Benedict revisada** y otras ecuaciones difieren por sus **poblaciones de derivación**.',
                                          'El gasto en reposo se vincula fuertemente a la **masa libre de grasa**, que aquí se **desconoce**.',
                                          'Usar **peso ideal** sin justificarlo puede subestimar o sobreestimar, sobre todo en obesidad grave.',
                                          'Al pedir «GET» siempre aclarar **ecuación, factor de actividad, supuestos de sexo/edad y limitaciones**.',
                                          '**No** se infiere un déficit energético seguro e individual sólo con esta estimación.'], 16, gap=0.15)
    s.note('Métodos alternativos: Harris–Benedict revisada y otras ecuaciones difieren por sus poblaciones de derivación. El gasto en '
           'reposo depende fuertemente de la masa libre de grasa, aquí desconocida; usar peso ideal sin justificarlo puede subestimar o '
           'sobreestimar. Si se solicita «GET», aclarar ecuación, factor de actividad, supuestos y limitaciones. No puede inferirse un '
           'déficit energético seguro e individual sólo con esta estimación.')


def descent(D):
    s = new(D, U, 'Descenso de 170 a 140 kg: magnitud y riesgos', 'green')
    cid = chart_line(s, 0.4, 1.15, 5.9, 3.3, ['Inicio', 'Mes 1', 'Mes 2', 'Mes 3'], [('Peso (kg)', [170, 160, 150, 140])], ['C00000'],
                     title_txt='Descenso promedio ≈ 10 kg/mes (esquema)', legend=False, size=11, smooth=False, labels=True, name='Descenso')
    st = [formula(s, 6.6, 1.2, 6.35, 0.7, 'Diferencia: 170 − 140 = 30 kg', 19, fill='FFF2CC'),
          formula(s, 6.6, 2.05, 6.35, 0.7, 'Relativo: 30 / 170 × 100 ≈ 17,65 %', 19, fill='FFF2CC'),
          formula(s, 6.6, 2.9, 6.35, 0.75, 'Nuevo IMC: 140 / 2,89 ≈ 48,44 kg/m²', 19, fill=BOX, color=BOXT)]
    c = tbox(s, 6.6, 3.85, 6.35, 1.3, 'Continúa en **obesidad clase III**, pero el beneficio clínico de ~18 % de descenso puede ser relevante.', 14.5, anchor='m')
    r = pearl(s, 0.4, 5.3, 12.55, 1.55, 'Descenso **rápido** (~10 kg/mes): interpretar según composición, hidratación y supervisión; revisar riesgo de **pérdida de masa magra**, **colelitiasis** (¡antecedente biliar!), **déficits** nutricionales y **recuperación ponderal**. El **GET debe reevaluarse**: cambió la masa y quizás la actividad.', 15)
    for x in st:
        s.step(fade(x))
    s.step(fade(c)); s.step(zoom(r))
    s.note('Bajar de 170 a 140 kg representa 30 kg, es decir 30/170 × 100 = 17,65 % del peso inicial. Nuevo IMC = 140/2,89 = 48,44 '
           'kg/m²: continúa en obesidad clase III. La pérdida promedio fue de alrededor de 10 kg/mes, considerablemente rápida: obliga a '
           'revisar el riesgo de pérdida de masa magra, colelitiasis, déficits y recuperación ponderal, especialmente con antecedente '
           'biliar. El gráfico supone un descenso lineal en tres meses sólo como esquema del promedio informado.')


def lab_interp(D):
    s = new(D, U, 'Pregunta 3 · interpretación completa del laboratorio', 'pink')
    items = [('Glucosa 145 mg/dL', 'Si fue **en ayunas** supera 126, pero sin hiperglucemia inequívoca requiere **segunda prueba**. Si no fue en ayunas, no basta. El previo **118** (si fue en ayunas) encaja con **glucosa alterada en ayunas**. Pedir **HbA1c** y confirmar.', 'y'),
             ('Lípidos', 'CT 250 ↑ · LDL 183 ↑ · HDL 30 ↓ · TG 185 ↑ → dislipidemia **mixta aterogénica**. **No-HDL = 250 − 30 = 220 mg/dL** (elevado). Con TG altos, LDL por Friedewald puede ser inexacto.', 's'),
             ('AST 29 U/L', 'Transaminasas normales **no excluyen MASLD/MASH** ni fibrosis. Estratificar (ALT/AST/plaquetas, métodos no invasivos; FIB-4 con límites < 35 años).', 'g'),
             ('Renal / iones normales', 'No excluyen daño vascular temprano: medir **TFG estimada** y **albúmina/creatinina urinaria**.', 'b'),
             ('Sokolow–Lyon +', 'Criterio de **voltaje** de posible HVI, coherente con HTA crónica; sensibilidad y especificidad **limitadas** (habitus). Complementar con ecocardiografía.', 'w')]
    ids = []
    for i, (h, t, k) in enumerate(items):
        y = 1.15 + i * 1.15
        g = s.group_start('Interp ' + h)
        mbox(s, 0.4, y, 3.0, 1.0, h, k, 14, caps=False)
        tbox(s, 3.5, y, 9.45, 1.0, t, 13, anchor='m', minsize=10)
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Pregunta 3. Glucosa 145: si está confirmada en ayunas supera el criterio diagnóstico (≥126), pero sin hiperglucemia '
           'inequívoca se necesita una segunda prueba; si no fue en ayunas no basta. El valor previo de 118 mg/dL, si fue en ayunas, '
           'encaja con alteración de la glucosa en ayunas. Lípidos: perfil compatible con resistencia insulínica y dislipidemia mixta '
           'aterogénica; no-HDL = 250 − 30 = 220 mg/dL. AST normal no excluye MASLD/MASH. Función renal normal no excluye albuminuria. '
           'Sokolow–Lyon: criterio de voltaje con sensibilidad y especificidad limitadas.')


def endocrine(D):
    s = new(D, U, 'Pregunta 4 · papel endocrino del tejido adiposo en el caso', 'cyanR')
    s.pic('adipocyte-1', 0.4, 1.2, 2.4, name='Adipocito endocrino')
    nodes = {
        'a': (3.1, 1.3, 3.0, 0.6, 'Adipocito hipertrofiado', 'y', 15),
        'l': (6.6, 1.2, 3.0, 0.55, 'Leptina ↑ con señal central ineficiente', 'Y', 12),
        'ad': (6.6, 1.85, 3.0, 0.55, 'Adiponectina ↓', 'Y', 13.5),
        'c': (6.6, 2.5, 3.0, 0.55, 'TNF-α · IL-6 · PAI-1 ↑', 'Y', 13.5),
        'f': (6.6, 3.15, 3.0, 0.55, 'Salida de AGNE ↑', 'Y', 13.5),
        'ri': (10.0, 1.6, 2.95, 0.9, 'Resistencia insulínica + estado protrombótico', 'r', 12.5),
        'o': (10.0, 2.85, 2.95, 0.85, 'DM2 · HTA · aterosclerosis', 'r', 14),
    }
    edges = [('a', 'l', {'pts': [(6.15, 1.55), (6.55, 1.45)]}), ('a', 'ad', {'pts': [(6.15, 1.65), (6.55, 2.1)]}), ('a', 'c', {'pts': [(6.15, 1.75), (6.55, 2.75)]}),
             ('a', 'f', {'pts': [(6.15, 1.85), (6.55, 3.4)]}), ('c', 'ri', {'pts': [(9.65, 2.7), (9.95, 2.2)]}), ('f', 'ri', {'pts': [(9.65, 3.4), (9.95, 2.4)]}), ('ri', 'o')]
    graph(s, nodes, edges, [['a'], ['a>l', 'l', 'a>ad', 'ad', 'a>c', 'c', 'a>f', 'f'], ['c>ri', 'f>ri', 'ri'], ['ri>o', 'o']])
    t = tbox(s, 0.4, 4.1, 12.55, 2.75, '- **Hipotálamo**: hambre y gasto (leptina).\n- **Hígado**: síntesis de glucosa y TAG.\n- **Endotelio**: vasodilatación/inflamación.\n- **Sistema inmune**: inflamación crónica.\n'
             '- Angiotensinógeno: sistema renina–angiotensina local.', 14.5, head='Interacciones')
    s.step(fade(t))
    s.note('Pregunta 4. El adipocito libera leptina (informa reservas al hipotálamo), adiponectina (oxidación lipídica, sensibilidad '
           'insulínica), angiotensinógeno y otros mediadores; las células inmunes y estromales secretan TNF-α, IL-6, quimiocinas y '
           'factores profibróticos. Cadena didáctica: adipocito hipertrofiado → leptina ↑ con señal central ineficiente; adiponectina '
           '↓; TNF-α/IL-6/PAI-1 ↑ y salida de AGNE ↑ → resistencia a insulina + estado protrombótico → DM2/HTA/aterosclerosis [T][S].')


def perpetuate(D):
    s = new(D, U, 'Pregunta 5 · alteraciones que causan y perpetúan la obesidad', 'yellow')
    import math
    items = [('Más almacenamiento', 'Ingesta > gasto sostenida; AG de QM/VLDL; esterificación'), ('Expansión celular', 'Hipertrofia, hiperplasia; hipoxia/fibrosis en exceso'),
             ('Resistencia adiposa a insulina', 'Antilipólisis insuficiente → AGNE ↑'), ('Resistencia central a leptina', 'El SNC no compensa la gran reserva'),
             ('Inflamación y lipotoxicidad', 'Adiponectina ↓, depósitos ectópicos'), ('Gasto modificado', 'Sedentarismo, NEAT bajo, capacidad funcional ↓')]
    cx, cy, R = 4.0, 4.0, 2.35
    ids = []
    for i, (h, t) in enumerate(items):
        a = -math.pi / 2 + i * 2 * math.pi / 6
        x = cx + R * math.cos(a) - 1.25; y = cy + R * math.sin(a) - 0.5
        g = s.group_start('Ciclo %d' % i)
        s.shape(x, y, 2.5, 1.0, 'rect', BOX if i % 2 == 0 else SALBOX, (INK, 1.5), SHD, '**%s**\n%s' % (h, t), 11, F_BODY, INK, False, 'c', 'm', (0.05, 0.03, 0.05, 0.03), minsize=8.5)
        ids.append(s.group_end())
    ring = s.shape(cx - 1.0, cy - 1.0, 2.0, 2.0, 'ellipse', ('a', 'FFFFFF', 60), ('C00000', 3, 'dash'), False, 'Causa y\nconsecuencia', 13, F_HEAD, INH, True, 'c', 'm', name='Centro ciclo')
    t = tbox(s, 7.6, 1.2, 5.35, 3.55, '«Las alteraciones del adipocito **producen** obesidad» es incompleto: pueden ser **consecuencia** de la expansión y **factores de retroalimentación** que dificultan la regulación y generan complicaciones.', 15, head='Precisión causal')
    p = pearl(s, 7.6, 5.0, 5.35, 1.85, 'Circuitos **hedónicos**, **entorno** alimentario y factores **psicosociales** son componentes adicionales indispensables.', 15)
    s.step(*[fade(g, after=i > 0, dur=250) for i, g in enumerate(ids)])
    s.step(zoom(ring)); s.step(fade(t)); s.step(zoom(p))
    s.note('Pregunta 5. Alteraciones adiposas que causan y perpetúan la obesidad: aumento del almacenamiento (ingesta sostenidamente '
           'mayor que el gasto, aporte de AG desde QM/VLDL, esterificación), expansión celular (hipertrofia, hiperplasia; en exceso '
           'hipoxia, fibrosis, inflamación), resistencia adiposa a la insulina (AGNE elevados), resistencia central a la leptina, '
           'inflamación y lipotoxicidad (adiponectina ↓, depósitos ectópicos) y modificación del gasto (sedentarismo, NEAT bajo). Son '
           'simultáneamente consecuencia y factores de retroalimentación; los circuitos hedónicos, el entorno y los factores '
           'psicosociales son indispensables.')


def appetite_case(D):
    s = new(D, U, 'Pregunta 6 · regulación del apetito aplicada al paciente', 'peach')
    lay = ['Señales de adiposidad **altas** con menor **eficacia central** (leptina/insulina).', 'Desequilibrio **POMC/CART** frente a **NPY/AgRP/GABA**.',
           'Hiperrespuesta aprendida a **pistas palatables**; recompensa **VTA–accumbens**.', 'Ejes de **estrés** (CRH–ACTH–cortisol), **sueño** y ánimo.',
           'Saciedad de corto plazo (**CCK/GLP-1/PYY**) insuficiente para frenar la búsqueda sostenida.', 'Endocannabinoides (**AEA/2-AG–CB1**), **5-HT2C**, oxitocina, orexinas.']
    steps_panel(s, 0.4, 1.2, 7.4, lay, 13.5, gap=0.1)
    w = pearl(s, 8.1, 1.2, 4.85, 2.9, '**No hacer inferencias excesivas**: el caso **no informa** leptina, grelina, ACTH, cortisol ni dopamina. No se puede afirmar un déficit bioquímico específico.', 14.5)
    t = tbox(s, 8.1, 4.35, 4.85, 2.5, 'No diagnosticar atracón, depresión o hipercortisolismo **sólo por el relato**. Explorar conducta alimentaria, ánimo, seguridad alimentaria, sustancias, sueño y salud mental con entrevista **no estigmatizante**.', 13.5)
    s.step(zoom(w)); s.step(fade(t))
    s.note('Pregunta 6. El relato sugiere ingesta repetida de sándwiches y dulces, aislamiento social, desempleo y juego patológico. '
           'Pueden superponerse seis capas: señales de adiposidad altas con menor eficacia central; desequilibrio POMC/CART frente a '
           'NPY/AgRP/GABA; hiperrespuesta aprendida a pistas palatables y recompensa dopaminérgica; ejes de estrés, sueño y ánimo; '
           'señales de saciedad de corto plazo insuficientes; sistema endocannabinoide y circuitos serotoninérgicos, oxitocinérgicos y '
           'orexinérgicos. El juego patológico sugiere explorar impulsividad y reforzadores, sin concluir que todo se explique por una '
           'sola alteración dopaminérgica. El caso no informa concentraciones hormonales ni marcadores: no se inventan.')


def to_dm2(D):
    s = new(D, U, '7a · obesidad y diabetes tipo 2', 'green')
    nodes = {
        'v': (0.4, 1.3, 3.2, 0.65, 'Adiposidad visceral y ectópica', 'y', 14),
        'm': (4.1, 1.2, 4.3, 0.6, 'AGNE · DAG · ceramidas · JNK/IKKβ', 'Y', 13),
        'a': (4.1, 1.95, 4.3, 0.6, 'Adiponectina ↓ · inflamación', 'Y', 13.5),
        'ri': (8.9, 1.5, 4.05, 0.7, 'RESISTENCIA A INSULINA', 'r', 14),
        'b': (8.9, 2.55, 4.05, 0.6, 'Hiperinsulinemia compensadora', 'Y', 13.5),
        'f': (8.9, 3.3, 4.05, 0.6, 'Genética + gluco/lipotoxicidad → capacidad β ↓', 'Y', 12),
        'h': (4.1, 3.3, 4.3, 0.6, 'Hígado produce glucosa · músculo capta menos', 'w', 12.5),
        'd': (4.1, 4.15, 8.85, 0.65, 'DM2 (confirmar la glucemia 145 con criterios adecuados)', 'y', 14),
    }
    edges = [('v', 'm', {'pts': [(3.65, 1.6), (4.05, 1.5)]}), ('v', 'a', {'pts': [(3.65, 1.7), (4.05, 2.25)]}), ('m', 'ri', {'pts': [(8.45, 1.5), (8.85, 1.75)]}),
             ('a', 'ri', {'pts': [(8.45, 2.25), (8.85, 2.0)]}), ('ri', 'b'), ('b', 'f'), ('f', 'h'), ('h', 'd')]
    graph(s, nodes, edges, [['v'], ['v>m', 'm', 'v>a', 'a'], ['m>ri', 'a>ri', 'ri'], ['ri>b', 'b', 'b>f', 'f'], ['f>h', 'h', 'h>d', 'd']])
    p = pearl(s, 0.4, 5.1, 12.55, 1.75, 'Descenso de peso, actividad física y terapias apropiadas pueden mejorar la sensibilidad y, en algunos pacientes, inducir **remisión** de la DM2, **sin equivaler a curación permanente**.', 15.5)
    s.step(zoom(p))
    s.note('Pregunta 7a. La adiposidad visceral y ectópica origina resistencia a insulina por AGNE/DAG/ceramidas, JNK/IKKβ, adiponectina '
           'baja e inflamación. El páncreas compensa con hiperinsulinemia; con el tiempo, factores genéticos y glucolipotoxicidad '
           'limitan la capacidad β; el hígado mantiene producción glucémica inapropiada y el músculo capta menos glucosa. El paciente '
           'tiene riesgo alto de DM2; si su glucosa 145 fuese en ayunas, debería confirmarse. La remisión es posible pero no equivale a '
           'curación permanente.')


def to_hta(D):
    s = new(D, U, '7b · obesidad e hipertensión arterial', 'cyan')
    s.pic('kidney-2', 5.3, 2.25, 2.4, name='Riñón HTA')
    mech = [('Actividad simpática ↑', 0.4, 1.2), ('SRAA (renal y adiposo) ↑', 0.4, 2.15), ('Compresión renal por grasa perirrenal/sinusal', 0.4, 3.1),
            ('Reabsorción tubular de Na⁺ ↑', 0.4, 4.05), ('Hiperinsulinemia', 8.4, 1.2), ('Endotelio: NO ↓ · estrés oxidativo', 8.4, 2.15),
            ('Inflamación', 8.4, 3.1), ('Apnea obstructiva del sueño', 8.4, 4.05)]
    ids = []
    for t, x, y in mech:
        g = s.group_start('Mec ' + t)
        mbox(s, x, y, 4.5, 0.75, t, 's' if x < 1 else 'g', 13.5, caps=False)
        if x < 1:
            s.arrow([(4.95, y + 0.37), (5.6, 3.2)], INK, 2)
        else:
            s.arrow([(8.35, y + 0.37), (7.5, 3.2)], INK, 2)
        ids.append(s.group_end())
    o = mbox(s, 4.9, 5.05, 3.5, 0.75, 'Volumen ↑ + resistencia vascular ↑', 'r', 14, caps=False)
    p = tbox(s, 0.4, 6.0, 12.55, 0.85, 'TA 160/100 requiere **confirmación y evaluación** según síntomas/riesgo; no atribuirla sólo al estrés. Tratar AOS, peso y sodio **complementa** los antihipertensivos.', 13.5, anchor='m')
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids[:4])])
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids[4:])])
    s.step(zoom(o)); s.step(fade(p))
    s.note('Pregunta 7b. Mecanismos superpuestos: mayor actividad simpática renal y sistémica, activación del sistema '
           'renina–angiotensina–aldosterona, compresión renal por grasa perirrenal y del seno, mayor reabsorción tubular de sodio, '
           'hiperinsulinemia, disfunción endotelial con menor señal de NO, estrés oxidativo, inflamación y AOS. La combinación aumenta '
           'el volumen circulante y la resistencia vascular. El circuito reno-adiposo explica por qué tratar AOS, peso y sodio puede '
           'complementar a los antihipertensivos.')


def to_lipids(D):
    s = new(D, U, '7c · obesidad y dislipemias', 'pink')
    s.pic('healthy_liver', 0.4, 1.2, 2.6, name='Hígado lip')
    s.pic('vldl-1', 3.3, 1.25, 1.2, name='VLDL img')
    s.pic('ldl-1', 8.2, 3.2, 1.0, name='LDL img')
    s.pic('lipid-hdl-1', 8.25, 4.55, 0.95, name='HDL img')
    nodes = {
        'a': (0.4, 3.3, 3.0, 0.6, 'AGNE ↑ al hígado', 'Y', 14),
        'v': (4.7, 1.4, 3.2, 0.65, 'VLDL rica en TAG ↑', 'y', 14),
        'c': (4.7, 2.6, 3.2, 0.6, 'CETP: intercambia TAG ⇄ CE', 'g', 12.5),
        'l': (4.7, 3.45, 3.2, 0.6, 'Lipasa hepática remodela', 'g', 13),
        'ld': (9.45, 3.3, 3.5, 0.65, 'LDL pequeñas y densas', 'r', 13.5),
        'hd': (9.45, 4.6, 3.5, 0.65, 'HDL pequeñas: catabolismo ↑ → HDL ↓', 'r', 12),
    }
    edges = [('a', 'v', {'pts': [(3.45, 3.5), (4.65, 1.8)]}), ('v', 'c'), ('c', 'l'), ('l', 'ld', {'pts': [(7.95, 3.75), (9.4, 3.62)]}), ('l', 'hd', {'pts': [(7.95, 3.9), (9.4, 4.9)]})]
    graph(s, nodes, edges, [['a', 'a>v', 'v'], ['v>c', 'c', 'c>l', 'l'], ['l>ld', 'ld', 'l>hd', 'hd']])
    p = pearl(s, 0.4, 5.45, 12.55, 1.4, 'Patrón: **TG ↑ + HDL ↓ + LDL aterogénicas**. El LDL-C no siempre está muy alto (aquí **183**). La aterosclerosis depende de la **retención de partículas ApoB** en la íntima y de la **inflamación**, no sólo de «grasas en sangre».', 14.5)
    s.step(zoom(p))
    s.note('Pregunta 7c. La resistencia adiposa a la insulina aumenta el flujo de AGNE al hígado: más síntesis y secreción de VLDL rica en '
           'TAG. La CETP facilita el intercambio de lípidos entre lipoproteínas; la lipasa hepática remodela las partículas dando LDL '
           'pequeñas y densas y HDL de menor tamaño con catabolismo acelerado. Patrón habitual: TG altos + HDL bajo + partículas LDL '
           'aterogénicas. La aterosclerosis depende de la retención de partículas con ApoB en la íntima y de la inflamación.')


def to_masld(D):
    s = new(D, U, '7d · esteatosis y esteatohepatitis metabólica', 'lime')
    s.pic('healthy_liver', 0.4, 1.2, 3.2, name='Hígado MASLD')
    nom = tbox(s, 3.9, 1.2, 9.05, 1.35, '**MASLD**: enfermedad hepática esteatósica asociada a disfunción metabólica · **MASH**: forma con inflamación/lesión hepatocitaria. Literatura previa: NAFLD/NASH; el caso dice «esteatohepatitis no alcohólica».', 13.5, head='Nomenclatura actual')
    mech = ['Entrada hepática de **AGNE**', '**Lipogénesis de novo** (carbohidratos/insulina)', '**Oxidación** insuficiente para la carga', '**Estrés oxidativo** e inflamación', 'Microbiota e inmunidad']
    ids = [mbox(s, 3.9 + (i % 3) * 3.05, 2.85 + (i // 3) * 0.75, 2.95, 0.62, t, 'Y', 12.5, caps=False, name='MASLD mec %d' % i) for i, t in enumerate(mech)]
    pr = s.group_start('Progresión')
    for i, (t, k) in enumerate([('Esteatosis', 'y'), ('MASH', 's'), ('Fibrosis', 'r'), ('Cirrosis', 'r'), ('Carcinoma hepatocelular', 'k')]):
        mbox(s, 0.4 + i * 2.55, 4.6, 2.3, 0.6, t, k, 13, caps=False)
        if i:
            s.arrow([(0.4 + i * 2.55 - 0.22, 4.9), (0.4 + i * 2.55 - 0.03, 4.9)], INK, 2.5)
    s.group_end()
    p = pearl(s, 0.4, 5.5, 12.55, 1.35, '**Transaminasas normales no excluyen MASLD/MASH.** Con obesidad grave, DM2 probable y dislipidemia corresponde **valorar riesgo hepático** (fibrosis).', 15)
    s.step(fade(nom)); s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids)]); s.step(wipe(pr, 'l', dur=1200)); s.step(zoom(p))
    s.note('Pregunta 7d. La nomenclatura actual utiliza MASLD y MASH. Fisiopatología: entrada hepática de AGNE, lipogénesis de novo '
           'estimulada por carbohidratos e insulina, oxidación insuficiente para la carga recibida, estrés oxidativo, inflamación e '
           'interacción con microbiota e inmunidad. La progresión puede llevar a fibrosis, cirrosis y carcinoma hepatocelular. Las '
           'transaminasas normales no excluyen MASLD/MASH.')


def to_gall(D):
    s = new(D, U, '7e · hernias, litiasis biliar y pancreatitis', 'peach')
    s.pic('bile-lithiasis-big-calculi', 0.4, 1.2, h=3.4, name='Litiasis')
    s.pic('pancreas', 2.7, 3.2, 2.6, name='Páncreas pancreatitis')
    cols = [('HERNIAS', 'Adiposidad central → **presión intraabdominal** ↑ y carga sobre la pared; debilidad fascial, esfuerzos, mala cicatrización. Causalidad individual.', 's'),
            ('LITIASIS BILIAR', 'Más **colesterol biliar** → sobresaturación, **nucleación** de cristales y cálculos; importa la **motilidad vesicular**. Pérdida **muy rápida** de peso ↑ riesgo.', 'y'),
            ('PANCREATITIS BILIAR', '**Migración/obstrucción** por cálculos desencadena inflamación pancreática. El antecedente **no contraindica automáticamente** todo antidiabético, pero exige revisar riesgos.', 'r')]
    ids = []
    for i, (h, t, k) in enumerate(cols):
        y = 1.2 + i * 1.9
        g = s.group_start('Comp ' + h)
        mbox(s, 5.6, y, 7.35, 0.55, h, k, 15)
        tbox(s, 5.6, y + 0.6, 7.35, 1.15, t, 13.5, anchor='m')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Pregunta 7e. Hernias: la adiposidad central eleva la presión intraabdominal y la carga sobre la pared; pueden coexistir '
           'debilidad fascial, aumento de presión en esfuerzos y mala cicatrización. Litiasis biliar: la obesidad incrementa la '
           'secreción hepática de colesterol biliar, con sobresaturación, nucleación y cálculos; la pérdida de peso muy rápida aumenta '
           'el riesgo por movilización de colesterol y menor vaciamiento vesicular. La pancreatitis biliar ocurre cuando la migración u '
           'obstrucción por cálculos desencadena inflamación pancreática; el antecedente no contraindica automáticamente todo fármaco '
           'antidiabético, pero exige revisar riesgos individuales.')


def to_osa(D):
    s = new(D, U, '7f · apnea obstructiva del sueño y respiración', 'blue')
    s.pic('healthy-lung', 0.4, 1.2, 2.6, name='Pulmón AOS')
    nodes = {
        'g': (3.3, 1.25, 3.6, 0.65, 'Grasa cervical y faríngea', 'y', 14),
        'c': (3.3, 2.15, 3.6, 0.6, 'Calibre de vía aérea ↓ · colapsabilidad ↑', 'Y', 12),
        'a': (3.3, 3.0, 3.6, 0.6, 'Apneas/hipopneas en el sueño', 'Y', 13),
        'h': (7.4, 1.25, 2.6, 0.6, 'Hipoxemia intermitente', 's', 12.5),
        'd': (7.4, 2.0, 2.6, 0.6, 'Despertares', 's', 13.5),
        'sy': (7.4, 2.75, 2.6, 0.6, 'Activación simpática', 's', 13),
        'o': (10.35, 1.25, 2.6, 2.1, 'HTA · arritmias · resistencia insulínica · somnolencia · accidentes', 'r', 13),
    }
    edges = [('g', 'c'), ('c', 'a'), ('a', 'h', {'pts': [(6.95, 3.2), (7.35, 1.55)]}), ('a', 'd', {'pts': [(6.95, 3.25), (7.35, 2.3)]}),
             ('a', 'sy', {'pts': [(6.95, 3.3), (7.35, 3.05)]}), ('h', 'o', {'pts': [(10.05, 1.55), (10.3, 1.55)]}), ('sy', 'o', {'pts': [(10.05, 3.05), (10.3, 3.05)]})]
    graph(s, nodes, edges, [['g', 'g>c', 'c', 'c>a', 'a'], ['a>h', 'h', 'a>d', 'd', 'a>sy', 'sy'], ['h>o', 'sy>o', 'o']])
    d = tbox(s, 0.4, 3.9, 6.2, 2.95, 'Cuadro **muy sugestivo** de AOS, pero el diagnóstico requiere evaluación y típicamente **polisomnografía**. Con IMC ~59 y disnea, investigar también **síndrome de hipoventilación por obesidad** (hipercapnia diurna), que **no es sinónimo** de AOS.', 14, head='Diagnóstico')
    o = tbox(s, 6.85, 3.9, 6.1, 2.95, 'Osteoartrosis y dolor de rodillas · enfermedad venosa · limitación funcional · hipogonadismo funcional · infertilidad · ECV · cánceres asociados a adiposidad · **salud mental**. No usar la lista para atribuir diagnósticos sin evaluación.', 13.5, head='Otras consecuencias')
    s.step(fade(d)); s.step(fade(o))
    s.note('Pregunta 7f. La grasa cervical y faríngea, la reducción del calibre de la vía aérea superior y la alteración de fuerzas '
           'mecánicas favorecen la colapsabilidad faríngea durante el sueño: apneas e hipopneas repetidas, hipoxemia intermitente, '
           'despertares, somnolencia diurna y activación simpática, con riesgo de HTA, arritmias, resistencia insulínica y accidentes. '
           'El diagnóstico requiere evaluación y típicamente polisomnografía. Con IMC cercano a 59 y disnea debe investigarse el '
           'síndrome de hipoventilación por obesidad. Otras consecuencias: osteoartrosis, enfermedad venosa, limitación funcional, '
           'hipogonadismo funcional, infertilidad, enfermedad cardiovascular, cánceres asociados a adiposidad y salud mental.')


def hub(D):
    s = new(D, U, 'Complicaciones integradas del caso 20', 'green')
    c = s.pic('obese-man', 5.65, 1.6, h=4.2, name='Centro paciente')
    import math
    items = [('Resistencia insulínica · DM2', 'langerhans-islet-pancreas'), ('HTA', 'kidney-2'), ('Dislipidemia', 'ldl-1'), ('MASLD/MASH', 'healthy_liver'),
             ('Riesgo cardiovascular', 'heart-front'), ('AOS', 'healthy-lung'), ('Osteoarticular · mecánica', 'muscle-2'), ('Litiasis · pancreatitis', 'bile-lithiasis-big-calculi'),
             ('Psicológica y social', 'brain-2')]
    ids = []
    for i, (t, img) in enumerate(items):
        a = -math.pi / 2 + i * 2 * math.pi / len(items)
        x = 6.55 + 4.9 * math.cos(a) - 1.15; y = 3.95 + 2.45 * math.sin(a) - 0.4
        g = s.group_start('Hub %d' % i)
        s.arrow([(6.67 + 1.3 * math.cos(a), 3.7 + 1.5 * math.sin(a)), (6.67 + 3.4 * math.cos(a), 3.85 + 1.9 * math.sin(a))], INK, 2)
        fitpic(s, img, x, y - 0.05, 0.6, 0.7)
        mbox(s, x + 0.65, y, 2.0, 0.6, t, 'y', 11.5, caps=False)
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g, dur=300))
    s.note('Mapa de complicaciones integradas del caso 20: resistencia insulínica y DM2, HTA, dislipidemia, esteatosis hepática '
           'metabólica, riesgo cardiovascular, apnea obstructiva del sueño, alteraciones osteoarticulares y mecánicas, litiasis y '
           'pancreatitis según los antecedentes, y consecuencias psicológicas y sociales. Cada una se explicó en las diapositivas '
           'anteriores desde sus mecanismos.')


def build(D):
    div(D)
    case(D)
    labs(D)
    definition(D)
    bmi(D)
    waist(D)
    mifflin(D)
    methods(D)
    descent(D)
    lab_interp(D)
    endocrine(D)
    perpetuate(D)
    appetite_case(D)
    to_dm2(D)
    to_hta(D)
    to_lipids(D)
    to_masld(D)
    to_gall(D)
    to_osa(D)
    hub(D)
