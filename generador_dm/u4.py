# -*- coding: utf-8 -*-
"""UNIDAD IV — Integración CAD frente a EHH"""
from base import *

U = 4


def div(D):
    def art(s):
        model(s, 'bhb', 10.9, 0.7, 2.0, name='BHB')
        model(s, 'glucosa', 10.7, 3.3, 2.3, name='Glc')
        s.pic('kidney-2', 0.5, 4.6, 1.5, name='Riñón')
        model(s, 'acetona', 0.4, 1.4, 1.6, name='Acetona', label='Acetona')
    divider(D, U, 'IV', 'CAD FRENTE A EHH', 'Una misma red metabólica, dos desenlaces',
            ['Mapa que se bifurca', 'Comparación mecanística', 'DM1 frente a DM2', 'Algoritmo del laboratorio de emergencias',
             'Reglas de alto rendimiento', 'Fórmulas razonadas'], art,
            'Unidad IV. Integra los casos 11 y 12. El mensaje central: el grado de acción insulínica residual decide si la red '
            'metabólica se dirige a la cetoacidosis o a la hiperglucemia hiperosmolar sin cetosis marcada, sin que DM1 y DM2 '
            'equivalgan siempre a CAD y EHH respectivamente.')


def bifurcation(D):
    s = new(D, U, 'Un mapa, dos caminos: la acción insulínica residual decide', 'band', tsize=30)
    nodes = {
        'st': (3.9, 1.15, 5.5, 0.6, 'Déficit de acción insulínica + hormonas contrarreguladoras', 's', 13.5),
        'hg': (3.9, 2.0, 5.5, 0.6, 'PHG ↑ + captación ↓ → HIPERGLUCEMIA', 'y', 14),
        'L0': (0.4, 2.9, 4.3, 0.6, 'INSULINOPENIA MARCADA', 'r', 15),
        'L1': (0.4, 3.75, 4.3, 0.55, 'Lipólisis sin freno → AGNE ↑↑', 'Y', 13.5),
        'L2': (0.4, 4.5, 4.3, 0.55, 'β-oxidación → cetogénesis (HMGCS2)', 'Y', 13),
        'L3': (0.4, 5.25, 4.3, 0.55, 'Cetoácidos → HCO₃⁻ ↓ → acidemia', 'Y', 13),
        'L4': (0.4, 6.1, 4.3, 0.7, 'CETOACIDOSIS DIABÉTICA', 'y', 18),
        'R0': (8.65, 2.9, 4.3, 0.6, 'ACCIÓN INSULÍNICA RESIDUAL', 'g', 15),
        'R1': (8.65, 3.75, 4.3, 0.55, 'Lipólisis frenada → cetogénesis limitada', 'Y', 12.5),
        'R2': (8.65, 4.5, 4.3, 0.55, 'Hiperglucemia prolongada (días) · glucosuria', 'Y', 12.5),
        'R3': (8.65, 5.25, 4.3, 0.55, 'Pérdida de agua libre → hiperosmolalidad', 'Y', 12.5),
        'R4': (8.65, 6.1, 4.3, 0.7, 'EHH SIN CETOSIS MARCADA', 'y', 17),
        'mx': (5.1, 4.3, 3.15, 1.6, 'Formas MIXTAS: cetosis + hiperosmolalidad', 'b', 13.5),
    }
    edges = [('st', 'hg'), ('hg', 'L0', {'pts': [(4.6, 2.62), (3.0, 2.86)]}), ('hg', 'R0', {'pts': [(8.7, 2.62), (10.3, 2.86)]}),
             ('L0', 'L1'), ('L1', 'L2'), ('L2', 'L3'), ('L3', 'L4'), ('R0', 'R1'), ('R1', 'R2'), ('R2', 'R3'), ('R3', 'R4'),
             ('L2', 'mx', {'dash': 'dash', 'col': TRN}), ('R3', 'mx', {'dash': 'dash', 'col': TRN})]
    graph(s, nodes, edges, [['st', 'st>hg', 'hg'], ['hg>L0', 'L0', 'hg>R0', 'R0'], ['L0>L1', 'L1', 'L1>L2', 'L2', 'L2>L3', 'L3', 'L3>L4', 'L4'],
                            ['R0>R1', 'R1', 'R1>R2', 'R2', 'R2>R3', 'R3', 'R3>R4', 'R4'], ['L2>mx', 'R3>mx', 'mx']])
    s.note('Animación de bifurcación: un mismo mapa (déficit de acción insulínica + contrarreguladoras → producción hepática de '
           'glucosa aumentada y captación disminuida → hiperglucemia) se divide según la acción insulínica residual. Rama izquierda: '
           'insulinopenia marcada → lipólisis sin freno → β-oxidación y cetogénesis → consumo de bicarbonato → cetoacidosis. Rama '
           'derecha: acción insulínica residual → lipólisis frenada → cetogénesis limitada → hiperglucemia prolongada, glucosuria y '
           'pérdida de agua libre → EHH sin cetosis marcada. Centro: formas mixtas. No presentar DM1 y DM2 como entidades que '
           'siempre desarrollan exclusivamente CAD o EHH: la DM2 también puede presentar CAD y existen cuadros mixtos.')


def compare(D):
    s = new(D, U, 'Comparación mecanística CAD frente a EHH', 'peach')
    rows = [['Dimensión', 'CAD (caso 11)', 'EHH (caso 12)'],
            ['Déficit de insulina', 'Absoluto o casi absoluto', 'Relativo: secreción residual insuficiente'],
            ['Producción hepática de glucosa', '↑↑ (glucagón, estrés)', '↑↑ (resistencia hepática)'],
            ['Lipólisis', 'Sin freno → AGNE ↑↑', 'Relativamente frenada'],
            ['Cetogénesis', 'Marcada (β-OHB ↑↑)', 'Limitada (β-OHB < 3,0 mmol/L)'],
            ['Acidosis metabólica', 'Sí: pH y HCO₃⁻ bajos, AG ↑', 'Ausente o leve (pH ≥ 7,3)'],
            ['Glucosuria / diuresis osmótica', 'Sí', 'Sí, prolongada (días)'],
            ['Déficit hídrico', 'Importante', 'Suele ser muy intenso'],
            ['Hiperosmolalidad', 'Variable', 'Marcada (efectiva > 300)'],
            ['Conciencia', 'Variable: acidosis, volumen, osmolalidad', 'Compromiso frecuente por hipertonía'],
            ['Potasio', 'Sérico normal/alto; total ↓', 'Sérico variable; total ↓'],
            ['Compensación', 'Kussmaul (pCO₂ ↓)', 'Sin necesidad ventilatoria importante'],
            ['Formas mixtas', 'Existen: cetosis + hiperosmolalidad', 'Existen']]
    table(s, 0.4, 1.15, 12.55, rows, [3.4, 4.6, 4.55], size=12.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla CAD EHH', heights=[0.42] + [0.44] * 12)
    s.note('Comparación mecanística. CAD: deficiencia absoluta o casi absoluta de insulina, producción hepática de glucosa aumentada, '
           'lipólisis sin freno, cetogénesis marcada, acidosis metabólica con anion gap elevado, glucosuria y déficit hídrico '
           'importante, osmolalidad variable, compromiso de conciencia según acidosis, volumen y osmolalidad, potasio sérico normal o '
           'alto con déficit total, compensación ventilatoria de Kussmaul. EHH: déficit relativo con secreción residual, lipólisis '
           'relativamente frenada, cetogénesis limitada, acidosis ausente o leve, diuresis osmótica prolongada con déficit hídrico '
           'muy intenso, hiperosmolalidad marcada y compromiso de conciencia frecuente. Existen formas mixtas. Algunas filas '
           '(potasio en EHH, compensación) son ampliación bibliográfica coherente con el consenso 2024.')


def dm1dm2(D):
    s = new(D, U, 'DM1 típica frente a DM2 típica', 'cyan')
    rows = [['Dimensión', 'DM1 típica', 'DM2 típica'],
            ['Etiología', 'Autoinmunidad β; susceptibilidad HLA y ambiente', 'Resistencia insulínica + falla β progresiva; genética, adiposidad, edad'],
            ['Insulina endógena', 'Marcadamente baja/ausente en etapa establecida', 'Inicialmente normal/alta, luego insuficiente'],
            ['Autoanticuerpos', 'Frecuentes', 'Usualmente negativos'],
            ['Péptido C', 'Habitualmente bajo; depende de etapa y estímulo', 'Variable: alto precozmente, bajo tardíamente'],
            ['Ácido-base en crisis', 'CAD: HCO₃⁻ y pH bajos, β-OHB ↑', 'EHH: osmolalidad alta, acidosis ausente o leve'],
            ['Cetosis', 'Riesgo alto si falta insulina', 'Usualmente menor, pero puede aparecer CAD'],
            ['Glucosa en crisis', 'Habitualmente > 200; no excluye CAD euglucémica', 'En EHH con frecuencia ≥ 600'],
            ['Tratamiento basal', 'Insulina imprescindible', 'Individual; a veces insulina imprescindible'],
            ['Daño crónico', 'Retinopatía, nefropatía, neuropatía, ECV', 'Mismos órganos; HTA/dislipidemia/obesidad agravan']]
    table(s, 0.4, 1.15, 12.55, rows, [2.6, 4.9, 5.05], size=12.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla DM1 DM2')
    s.note('Comparación avanzada DM1 frente a DM2 (formas típicas). Complicaciones agudas compartidas: hipoglucemia farmacológica, '
           'descompensaciones hiperglucémicas mixtas, deshidratación, injuria renal y trastornos electrolíticos. Complicaciones '
           'crónicas compartidas: microvasculares (retina, riñón, nervios) y macrovasculares (corazón, cerebro, extremidades), '
           'además de infecciones y trastornos de cicatrización.')


def algorithm(D):
    s = new(D, U, 'Algoritmo integrador del laboratorio de emergencias', 'green')
    steps = [('A', 'Confirmar glucosa', 'síntomas, signos vitales, volumen, estado mental'), ('B', 'Buscar acidosis', 'pH, HCO₃⁻, pCO₂ y controles cruzados'),
             ('C', 'Buscar cetonas', 'preferentemente β-OHB sanguíneo'), ('D', 'Evaluar tonicidad', 'Na⁺, glucosa, osmolalidad, urea → osmolalidad efectiva'),
             ('E', 'Gravedad y causa', 'perfusión, K⁺, función renal, lactato, foco infeccioso, ECG; diagnósticos alternativos'),
             ('F', 'Tratar y monitorizar', 'volumen, K⁺, insulina, desencadenante, nutrición, transición y educación')]
    ids = []
    for i, (l, h, t) in enumerate(steps):
        y = 1.15 + i * 0.97
        g = s.group_start('Paso ' + l)
        s.shape(0.5, y, 0.8, 0.8, 'ellipse', BOX, (INK, 2), SHD, l, 24, F_POP, BOXT, False, 'c', 'm', (0, 0, 0, 0), fit=False)
        mbox(s, 1.5, y + 0.06, 3.4, 0.68, h, 'y', 15)
        tbox(s, 5.05, y + 0.06, 7.9, 0.68, t, 14.5, anchor='m')
        if i < 5:
            s.arrow([(0.9, y + 0.82), (0.9, y + 0.95)], INK, 2.5)
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Algoritmo integrador [C24]. A: confirmar glucosa y evaluar síntomas, signos vitales, volumen y estado mental. B: buscar '
           'acidosis con pH, HCO₃⁻, pCO₂ y controles cruzados (Henderson–Hasselbalch). C: buscar cetonas, preferentemente '
           'β-hidroxibutirato sanguíneo. D: evaluar tonicidad con Na⁺, glucosa, osmolalidad y urea; calcular la osmolalidad '
           'efectiva. E: gravedad y causa (perfusión, K⁺, función renal, lactato, foco infeccioso, ECG; descartar diagnósticos '
           'alternativos). F: tratar y monitorizar secuencialmente volumen, potasio, insulina, desencadenante, nutrición, transición '
           'y educación.')


def rules(D):
    s = new(D, U, 'Reglas de alto rendimiento', 'pink')
    rr = ['**AG elevado** = aniones no medidos, no identifica la causa: en CAD pensar cetonas; con sepsis/shock, lactato.',
          '**pCO₂ baja** puede ser compensatoria: el trastorno mixto se diagnostica comparando con lo esperado **y** verificando coherencia.',
          '**Glucosa alta ≠ cetonas altas**: deciden la insulina residual y la relación glucagón/insulina.',
          '**Osmolalidad total** incluye urea; la **efectiva** la excluye: no intercambiarlas.',
          '**K⁺ sérico ≠ reserva corporal total**: puede caer rápido al corregir la insulinopenia.',
          '**Corregir el pH ≠ corregir la causa**: la cetogénesis se detiene con acción insulínica y control del disparador.']
    steps_panel(s, 0.4, 1.2, 12.55, rr, 15.5, gap=0.14)
    s.note('Reglas de alto rendimiento: el anion gap elevado indica aniones no medidos pero no su causa; la pCO₂ baja puede '
           'ser compensatoria y sólo se diagnostica trastorno mixto comparándola con la esperada y verificando la coherencia; glucosa '
           'elevada no implica cetonas elevadas; la osmolalidad total incluye urea y la efectiva la excluye; potasio sérico no es '
           'reserva corporal total; corrección del pH no es corrección del proceso causal.')


def formulas(D):
    s = new(D, U, 'Fórmulas razonadas para la clase', 'yellow')
    rows = [['Cálculo', 'Fórmula', 'Interpretación o limitación'],
            ['Anion gap', 'Na⁺ − (Cl⁻ + HCO₃⁻)', 'Requiere Na/Cl; sumar ≈ 2,5 mEq/L por cada 1 g/dL de albúmina bajo 4'],
            ['pCO₂ de Winter', '1,5 × HCO₃⁻ + 8 ± 2', 'Compensación esperada en acidosis metabólica'],
            ['Henderson–Hasselbalch', '6,1 + log[HCO₃⁻ / (0,03 × pCO₂)]', 'Prueba la coherencia de pH, HCO₃⁻ y pCO₂'],
            ['Osmolalidad total', '2 Na + glucosa/18 + BUN/2,8', 'Na en mmol/L; glucosa/BUN en mg/dL'],
            ['Osmolalidad efectiva', '2 Na + glucosa/18', 'Tonicidad: movimientos sostenidos de agua celular'],
            ['Sodio corregido', 'Na medido + factor × (glucosa − 100)/100', 'Factor ≈ 1,6 o 2,4; requiere sodio medido'],
            ['eAG desde HbA1c', '28,7 × A1c − 46,7', 'Estimación poblacional; no reemplaza automonitoreo'],
            ['Carga filtrada de glucosa', 'FG × glucemia', 'Convertir a unidades compatibles']]
    table(s, 0.4, 1.15, 12.55, rows, [2.9, 4.4, 5.25], size=13.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla fórmulas')
    s.note('Tabla de fórmulas razonadas con su interpretación o limitación. Todas se aplican en los ejercicios de la Unidad X.')


def worked(D):
    s = new(D, U, 'Ejemplo resuelto con una gasometría coherente', 'cyanR')
    d = mbox(s, 0.4, 1.15, 12.55, 0.6, 'PACIENTE DISTINTO: pH 7,20 · HCO₃⁻ 10 mEq/L · pCO₂ 26 mmHg · Na⁺ 134 · Cl⁻ 100', 'y', 15)
    st = [formula(s, 0.4, 2.0, 6.1, 0.75, 'HH: 6,1 + log(10/0,78) ≈ 7,21 → coherente', 16, fill='FFF2CC'),
          formula(s, 0.4, 2.95, 6.1, 0.75, 'Winter: 1,5 × 10 + 8 = 23 ± 2', 17, fill='FFF2CC'),
          formula(s, 0.4, 3.9, 6.1, 0.75, 'AG = 134 − (100 + 10) = 24 mEq/L', 17, fill=BOX, color=BOXT)]
    it = [tbox(s, 6.85, 2.0, 6.1, 0.75, 'Tríada **coherente**: puede interpretarse.', 14.5, anchor='m'),
          tbox(s, 6.85, 2.95, 6.1, 0.75, 'Medida 26 > 25 → compensación **insuficiente** / posible acidosis respiratoria agregada.', 13.5, anchor='m'),
          tbox(s, 6.85, 3.9, 6.1, 0.75, 'AG **elevado**: aniones no medidos.', 14.5, anchor='m')]
    p = pearl(s, 0.4, 4.95, 12.55, 1.1, 'Nunca atribuir el AG **exclusivamente a cetonas** sin conocer **lactato, función renal y tóxicos** cuando corresponde. Cotejar y repetir según la situación clínica.', 15)
    for a, b in zip(st, it):
        s.step(fade(a), fade(b, after=True))
    s.step(zoom(p))
    s.note('Ejercicio adicional con datos coherentes (paciente distinto): pH 7,20; HCO₃⁻ 10; pCO₂ 26. Henderson–Hasselbalch: 0,03 × '
           '26 = 0,78; 10/0,78 = 12,8; log = 1,108; pH ≈ 7,21 (coherente). Winter predice 23 ± 2; la medida 26 es algo mayor → '
           'compensación insuficiente o posible acidosis respiratoria agregada; cotejar y repetir según la clínica. Con Na 134 y Cl '
           '100: AG = 134 − (100 + 10) = 24 mEq/L, elevado. Nunca atribuirlo exclusivamente a cetonas sin conocer lactato, función '
           'renal y tóxicos.')


def build(D):
    div(D)
    bifurcation(D)
    compare(D)
    dm1dm2(D)
    algorithm(D)
    rules(D)
    formulas(D)
    worked(D)
