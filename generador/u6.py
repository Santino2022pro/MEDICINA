# -*- coding: utf-8 -*-
"""UNIDAD VI — Casos clínicos y sistematización; resumen final; bibliografía"""
from base import *

U = 6
CSTEPS = ['Presentación', 'Datos', 'Problema', 'Mecanismo', 'Hormonas', 'Órganos', 'Consecuencias', 'Resolución']


def ctrack(s, active):
    g = s.group_start('!!Etapas caso')
    for i, t in enumerate(CSTEPS):
        on = i + 1 in active
        s.shape(0.4 + i * 1.57, 6.78, 1.5, 0.34, 'roundRect', TAG if on else 'FFFFFF', (INK, 1.0 if on else 0.5), False,
                '%d · %s' % (i + 1, t), 10.5, F_HEAD, INK if on else '7F8C8D', True, 'c', 'm', (0.02, 0, 0.02, 0), fit=False, adj={'adj': 40000})
    return s.group_end()


def div(D):
    def art(s):
        person(s, 8.6, 1.0, 2.6, name='Arte paciente 1')
        person(s, 10.9, 1.5, 2.2, name='Arte paciente 2', fill='F5CBA7', color='A04000')
        liver(s, 8.4, 4.1, 2.6, name='Arte hígado'); kidney(s, 11.3, 4.0, 1.1, name='Arte riñón')
        mol(s, 11.0, 6.2, 'glc', d=0.6); mol(s, 11.7, 6.2, 'cc', d=0.6); mol(s, 12.4, 6.2, 'urate', d=0.6)
    divider(D, U, 'VI', 'CASOS CLÍNICOS Y\nSISTEMATIZACIÓN', 'Aplicar la integración a situaciones reales',
            ['Caso A · 12 h de ayuno y AG libres elevados', 'Caso B · Diabetes, TAG altos y esteatosis', 'Caso C · Hipoglucemia con cetonas bajas',
             'Caso D · Cirrosis, sarcopenia y encefalopatía', 'Caso E · Ejercicio extenuante y ácido úrico', 'Caso F · TG extremos y dolor abdominal',
             'Enzimas reguladoras · errores frecuentes · mapa final'], art,
            'Unidad VI. Cada caso se desarrolla en ocho etapas: presentación, datos clínicos y bioquímicos, identificación del '
            'problema fisiológico, mecanismo molecular, respuesta hormonal, adaptaciones de los órganos, consecuencias clínicas y '
            'resolución fisiopatológica. Los datos se presentan de forma cualitativa (sin cifras inventadas).')


def case(D, code, ttl, pat, data, problem, mech, horm, organs, cons, resol, notconc, notes, icons=('liver',)):
    # --- diapositiva 1: presentación, datos, problema
    s = new(D, U, 'Caso %s · %s' % (code, ttl), 'CASO %s · PRESENTACIÓN' % code)
    ctrack(s, [1, 2, 3])
    pa = s.group_start('Paciente')
    s.shape(0.4, 1.1, 4.2, 5.5, 'rect', CREAM, (INK, 1.25), SHD)
    person(s, 1.3, 1.3, 2.6, name='Silueta')
    s.text(0.55, 3.95, 3.9, 2.55, pat, 14.5, F_BODY, INK, False, 'l', 't')
    s.group_end()
    rows = [['Dato', 'Hallazgo']] + data
    t, H = table(s, 4.9, 1.1, 8.0, rows, [3.6, 4.4], size=14.5, rowh=0.5, name='Datos del caso')
    q = s.shape(4.9, 1.3 + H, 8.0, 0.6, 'rect', TAG, (INK, 1.25), SHD, '¿Cuál es el problema fisiológico?', 16, F_HEAD, INK, True, 'c', 'm', name='Pregunta')
    pr = card(s, 4.9, 2.05 + H, 8.0, 6.6 - (2.05 + H), problem, LBLUE, 14.5, name='Problema')
    s.step(fade(pa)); s.step(fade(t)); s.step(zoom(q)); s.step(fade(pr))
    s.note(notes[0])
    # --- diapositiva 2: mecanismo, hormonas, órganos
    s = new(D, U, 'Caso %s · Mecanismo y respuesta' % code, 'CASO %s · FISIOPATOLOGÍA' % code)
    ctrack(s, [4, 5, 6])
    fl = flow(s, mech, 0.4, 1.1, 6.3, 5.5, [LSALMON, YEL, PINK, LBLUE, MINT, RED][:len(mech)], 13.5, 0.2, 'v', INK)
    h = card(s, 7.0, 1.1, 5.9, 2.4, horm, LILAC, 14, head='Respuesta hormonal')
    o = card(s, 7.0, 3.7, 5.9, 2.9, organs, MINT, 13.5, head='Adaptaciones de los órganos')
    flow_anim(s, fl)
    s.step(fade(h)); s.step(fade(o))
    s.note(notes[1])
    # --- diapositiva 3: consecuencias y resolución
    s = new(D, U, 'Caso %s · Consecuencias y resolución' % code, 'CASO %s · RESOLUCIÓN' % code)
    ctrack(s, [7, 8])
    for i, k in enumerate(icons):
        organ_icon(s, k, 0.5 + i * 1.3, 1.15, 1.15)
    c = card(s, 0.4, 2.5, 6.1, 4.1, cons, LSALMON, 14, head='Consecuencias clínicas')
    r = card(s, 6.8, 1.1, 6.1, 3.6, resol, MINT, 14, head='Resolución fisiopatológica', headfill=ACT)
    n = note_box(s, 6.8, 4.9, 6.1, 1.7, notconc, 13.5)
    s.step(fade(c)); s.step(fade(r)); s.step(fade(n))
    s.note(notes[2])


def cases(D):
    case(D, 'A', '12 h de ayuno, glucemia normal y AG libres elevados',
         'Persona sana, sin ingesta durante la noche (alrededor de 12 h). Se obtiene una muestra de sangre en ayunas.',
         [['Tiempo de ayuno', '~12 h'], ['Glucemia', 'Dentro del rango normal'], ['AG libres plasmáticos', '**Elevados** respecto del posprandial'], ['Contexto', 'Sin enfermedad conocida']],
         'Una glucemia normal **no prueba** que el hígado esté «inactivo»: la estabilidad depende de que la **producción hepática** compense la falta de **absorción intestinal**, mientras el adiposo libera AG.',
         ['↓ insulina → se libera el freno antilipolítico', 'Adiposo: ↑ AG y glicerol', 'Hígado: β-oxidación de AG → ATP', 'Glucogenólisis + gluconeogénesis compensan la falta de absorción'],
         '- **Insulina** relativamente menor que en el posprandial.\n- **Glucagón** relativo mayor.\n- Relación glucagón/insulina ↑.',
         '- **Hígado**: ↓ malonil-CoA → **CPT1** y β-oxidación más activas; glucógeno todavía relevante.\n- **Adiposo**: lipólisis moderada.\n- **Músculo**: mezcla de AG y glucosa.',
         '- **AG libres ↑** con glucemia estable: patrón **fisiológico** del ayuno nocturno.\n- Sin síntomas.',
         '- Ayuno posabsortivo **normal**: la glucemia se sostiene por **flujos hepáticos** (glucogenólisis + GNG), con **AG** como combustible alternativo.',
         'Qué **no** concluir: cetosis elevada obligatoria ni agotamiento completo del glucógeno a las 12 h.',
         ['Caso A, presentación. Interpretación: una glucemia dentro de rango no prueba que el hígado esté inactivo. Se presentan '
          'los datos de forma cualitativa.', 'Caso A, mecanismo: la caída de insulina reduce el freno lipolítico adiposo → aumentan '
          'AG y glicerol; el hígado β-oxida AG para obtener ATP, mientras la glucogenólisis y la gluconeogénesis compensan la falta '
          'de absorción intestinal. Predicción: insulina relativamente menor que en el posprandial, glucagón relativo mayor, '
          'malonil-CoA hepático menor, CPT1 y β-oxidación más activos.', 'Caso A, resolución: es el patrón fisiológico del ayuno '
          'nocturno. Qué no concluir: cetosis elevada obligatoria ni agotamiento completo del glucógeno a las 12 h.'], ('liver', 'adipose'))
    case(D, 'B', 'Diabetes con hiperglucemia, TAG altos y esteatosis',
         'Adulto con diabetes tipo 2 conocida. En el control se observan hiperglucemia, triglicéridos elevados y grasa hepática en la imagen.',
         [['Glucosa / HbA1c', '**Elevadas**'], ['TAG plasmáticos', '**Elevados**'], ['Colesterol no-HDL / ApoB', 'A correlacionar'], ['Transaminasas', 'Pueden ser normales'], ['Imagen hepática', '**Esteatosis**']],
         'Coexisten **resistencia insulínica** muscular, hepática y adiposa: la glucosa no se capta ni se suprime su producción, y llegan **más AG al hígado**.',
         ['Músculo: ↓ captación de glucosa estimulada por insulina', 'Hígado: producción de glucosa no suprimida → glucemia ↑', 'Adiposo resistente a la antilipólisis → ↑ AG al hígado', 'AG + DNL (+ genética) → reesterificación → TAG hepático y VLDL ↑'],
         '- **Insulina** puede estar alta, pero con **menor acción** en los tejidos (insulina plasmática ≠ sensibilidad).\n- Señal antilipolítica ineficaz.',
         '- **Hígado**: esteatosis y ↑ secreción de **VLDL**.\n- **Adiposo**: lipólisis mal suprimida.\n- **Músculo**: menor sumidero de glucosa.',
         '- **Hiperglucemia** (HbA1c ↑).\n- **Hipertrigliceridemia** (VLDL, remanentes).\n- **Esteatosis** (MASLD) y riesgo cardiometabólico.',
         '- Integrar **glucosa/HbA1c**, **TAG**, **no-HDL/ApoB**, transaminasas (normales **no descartan** esteatosis), contexto antropométrico y clínica.',
         'Punto fino: el hígado graso **no se explica solo por grasa ingerida**: participan AG del adiposo y DNL.',
         ['Caso B, presentación: diabetes con hiperglucemia, TAG altos y grasa hepática. Datos cualitativos.',
          'Caso B, mecanismo: el músculo capta menos glucosa estimulada por insulina y la producción hepática no se suprime → '
          'glucemia elevada. El adiposo resistente a la acción antilipolítica envía más AG al hígado; junto con la lipogénesis de '
          'novo y factores genéticos se favorece la reesterificación a TAG y la secreción de VLDL. Distinción: insulina plasmática '
          'frente a sensibilidad tisular.', 'Caso B, resolución: correlacionar glucosa/HbA1c, TAG, colesterol no-HDL/ApoB, '
          'transaminasas (normales no descartan esteatosis), contexto antropométrico y clínica. El hígado graso no se explica solo '
          'por grasa ingerida.'], ('liver', 'adipose', 'muscle'))
    case(D, 'C', 'Niño con vómitos, ayuno, hipoglucemia y cetonas bajas',
         'Niño con un cuadro intercurrente con vómitos que impide la alimentación. Consulta por decaimiento.',
         [['Ingesta', 'Ayuno por vómitos'], ['Glucemia', '**Baja** (hipoglucemia)'], ['Cuerpos cetónicos', '**Inapropiadamente bajos**'], ['Estado neurológico', 'Letargo']],
         'En una hipoglucemia **ordinaria** se espera contrarregulación **y cetonas**; si están inadecuadamente **bajas**, falla el acceso a los AG/cetogénesis (**CPT1/carnitina**, β-oxidación) o hay **inhibición por insulina** (hiperinsulinismo), entre otras causas.',
         ['Ayuno → AG llegan al hígado', 'Defecto de importación/oxidación (o insulina inapropiada)', '↓ cetogénesis y ↓ soporte energético de la GNG', 'Cerebro: menos glucosa y menos cetonas'],
         '- **Esperable**: ↑ glucagón, catecolaminas, cortisol y GH.\n- Si hay **hiperinsulinismo**: insulina **inapropiadamente presente** que frena lipólisis y cetogénesis.',
         '- **Hígado**: no logra oxidar AG ni producir cetonas suficientes.\n- **Adiposo**: libera AG (salvo inhibición por insulina).\n- **Cerebro**: déficit energético.',
         '- **Hipoglucemia hipocetósica**, letargo, posible convulsión o encefalopatía.\n- Posible hepatomegalia e hiperamonemia en defectos de oxidación.',
         '- **Emergencia metabólica**: requiere atención urgente.\n- Estudio dirigido: **perfil de acilcarnitinas**, insulina y genética según orientación.',
         'Seguridad: **no** es un ejercicio de ayuno voluntario; evitar ayunos prolongados.',
         ['Caso C, presentación: niño con vómitos, ayuno, hipoglucemia y cetonas bajas.', 'Caso C, mecanismo: sospecha de '
          'defecto de oxidación de AG/carnitina/CPT1 o hiperinsulinismo, entre otras causas. En hipoglucemia ordinaria se espera '
          'contrarregulación y cetonas; si son inadecuadamente bajas, falla el acceso a AG/cetogénesis o existe inhibición por '
          'insulina. Mecanismo cerebral: menos glucosa y menos cetonas → déficit energético neurológico.', 'Caso C, resolución: se '
          'trata de una emergencia metabólica que requiere atención urgente, no de un ejercicio de ayuno voluntario.'], ('liver', 'brain'))
    case(D, 'D', 'Cirrosis, sarcopenia y encefalopatía',
         'Adulto con cirrosis avanzada, pérdida de masa muscular y episodios de confusión.',
         [['Función hepática', '**Insuficiente** (cirrosis)'], ['Masa muscular', '**Sarcopenia**'], ['Estado mental', '**Encefalopatía** episódica'], ['Amonio', 'Puede estar elevado']],
         'El amonio se depura **menos**: el hígado produce menos urea, hay **derivaciones portosistémicas**, el **intestino** genera amonio y el **músculo sarcopénico** capta menos NH_{4}^{+} como glutamina.',
         ['Intestino: producción de NH_{3}', 'Derivación portosistémica: evita el primer paso', 'Hepatocitos: ↓ urea', 'Músculo sarcopénico: ↓ glutamina sintetasa efectiva', 'Cerebro: glutamina astroglial ↑ → encefalopatía'],
         '- Estado **catabólico**: cortisol, inflamación.\n- Resistencia insulínica frecuente en cirrosis.',
         '- **Músculo**: pierde su papel de sumidero de amonio.\n- **Riñón**: participa en el manejo del amonio.\n- **Astrocito**: acumula glutamina.',
         '- **Encefalopatía** hepática.\n- **Sarcopenia** progresiva.\n- La **restricción proteica crónica** agravaría la pérdida muscular.',
         '- Enfoque contemporáneo: **tratar precipitantes**, **lactulosa**, **rifaximina** según indicación y **objetivos proteicos adecuados**.',
         'Diferencial conceptual: explicar la vieja regla de restricción y **corregirla** con la evidencia actual.',
         ['Caso D, presentación: cirrosis, sarcopenia y encefalopatía.', 'Caso D, mecanismo: los hepatocitos depuran menos NH4+ '
          'como urea, las derivaciones portosistémicas evitan el primer paso, el intestino genera amonio y el músculo sarcopénico '
          'pierde capacidad de incorporar NH4+ a glutamina.', 'Caso D, resolución: restricción proteica crónica agravaría la '
          'pérdida muscular. Enfoque contemporáneo: tratamiento de precipitantes, lactulosa, rifaximina según indicación y '
          'objetivos nutricionales proteicos adecuados.'], ('liver', 'muscle', 'brain'))
    case(D, 'E', 'Deportista con ácido úrico transitoriamente alto',
         'Deportista evaluado poco después de un ejercicio extenuante; se detecta uricemia elevada en un control.',
         [['Momento', 'Poco después del esfuerzo'], ['Ácido úrico', '**Elevado** (transitorio)'], ['Lactato', 'Puede estar elevado'], ['Hidratación', 'Posible depleción de volumen']],
         'La **degradación acelerada de nucleótidos de adenina** en el músculo y la **menor excreción renal** transitoria elevan el urato.',
         ['Consumo de ATP ↑ → ADP/AMP ↑', 'AMPD1: AMP → IMP', 'IMP → hipoxantina → urato', 'Lactato y deshidratación ↓ excreción renal'],
         '- **Catecolaminas** ↑ durante el esfuerzo.\n- Señales de déficit energético (AMP, AMPK).',
         '- **Músculo**: adenilato cinasa y AMPD sostienen el ATP a costa del pool de adenilatos.\n- **Riñón**: excreción de urato transitoriamente reducida.',
         '- **Hiperuricemia transitoria**; habitualmente sin síntomas.\n- No equivale necesariamente a **gota** crónica.',
         '- Evaluar **tiempo** desde el esfuerzo, **volumen**, **función renal**, **fármacos** y **síntomas**.',
         'Integra ejercicio, nucleótidos y ácido úrico: no rotular como enfermedad sin contexto.',
         ['Caso E, presentación: deportista luego de ejercicio extenuante con uricemia transitoriamente alta.', 'Caso E, mecanismo: '
          'consumo de ATP aumentado → ADP/AMP aumentados → AMPD1 forma IMP; el IMP se degrada a hipoxantina y urato; el aumento de '
          'lactato y la deshidratación reducen la excreción.', 'Caso E, resolución: evaluar tiempo desde el esfuerzo, volumen, '
          'función renal, fármacos y síntomas. La cadena conecta ejercicio, nucleótidos y ácido úrico.'], ('muscle', 'kidney'))
    case(D, 'F', 'Triglicéridos extremadamente altos y dolor abdominal',
         'Adulto que consulta por dolor abdominal intenso; el suero se observa lechoso y los TG están extremadamente elevados.',
         [['Síntoma', '**Dolor abdominal**'], ['Aspecto del suero', 'Lechoso'], ['Triglicéridos', '**Extremadamente altos**'], ['Sospecha', 'Pancreatitis']],
         'Hipótesis: **hiperquilomicronemia** con posible **pancreatitis**: exceso de QM/VLDL por **producción** aumentada y/o **aclaramiento** insuficiente.',
         ['Producción ↑ y/o depuración ↓ de QM/VLDL', 'TAG plasmáticos extremos', 'Lipólisis local de TAG por lipasas en el páncreas', 'Efectos inflamatorios → lesión pancreática'],
         '- Puede asociarse a **descontrol glucémico**, **alcohol**, hipotiroidismo o causas **genéticas** (LPL, ApoC-II, GPIHBP1, APOA5).',
         '- **Intestino**: QM tras comidas grasas.\n- **Hígado**: VLDL (↑ con azúcares y alcohol).\n- **Páncreas**: lesión inflamatoria.',
         '- **Pancreatitis** aguda (urgencia).\n- Riesgo creciente con TAG muy altos.',
         '- **Evaluación clínica urgente**.\n- Concepto nutricional: AG **C8/C10** disminuyen la carga sobre QM frente a cadenas largas, **preservando AG esenciales**.',
         'No reducir la interpretación de TAG altos a «riesgo de infarto»: aquí el problema inmediato es el **páncreas**.',
         ['Caso F, presentación: TG extremadamente altos y dolor abdominal.', 'Caso F, mecanismo: exceso de QM/VLDL por producción o '
          'aclaramiento insuficiente; la lipólisis local de TAG por lipasas y los efectos inflamatorios contribuyen a la lesión '
          'pancreática.', 'Caso F, resolución: evaluación clínica urgente; los AG C8/C10 disminuyen la carga sobre QM respecto de '
          'cadenas largas, pero deben preservarse los AG esenciales.'], ('pancreas', 'intestine', 'liver'))


def enzymes(D):
    rows = [['Enzima / proteína', 'Señal clave', 'Vía / efecto'],
            ['**Glucocinasa**', 'Glucosa alta; regulación por GKRP', 'Sensor β pancreático; captura hepática'],
            ['**Glucógeno fosforilasa**', 'PKA → fosforilasa cinasa; AMP muscular', 'Glucogenólisis'],
            ['**Glucógeno sintasa**', 'Desfosforilación; G6P', 'Glucogenogénesis'],
            ['**PFK-1**', 'AMP y F2,6BP (+); ATP/citrato (−)', 'Glucólisis'],
            ['**PFK-2/FBPasa-2 hepática**', 'PKA fosforila → F2,6BP ↓', 'Ayuno: GNG ↑; glucólisis ↓'],
            ['**PDH**', 'PDP activa; PDK inhibe', 'Piruvato → acetil-CoA'],
            ['**Piruvato carboxilasa**', 'Acetil-CoA (+); biotina', 'Piruvato → oxaloacetato (GNG)'],
            ['**ACC1/ACC2**', 'Citrato e insulina (+); AMPK (−)', 'Malonil-CoA: síntesis/oxidación de AG'],
            ['**CPT1**', 'Malonil-CoA (−)', 'Entrada de AG largos a β-oxidación'],
            ['**HMGCS2**', 'Programa de ayuno, PPARα', 'Cetogénesis'],
            ['**SCOT/OXCT1**', 'Presente extrahepáticamente', 'Cetólisis; ausente en hígado'],
            ['**HMGCR**', 'SREBP-2 (+); AMPK (−); esteroles (−)', 'Síntesis de colesterol'],
            ['**CPS1**', 'N-acetilglutamato obligatorio (+)', 'Ureogénesis mitocondrial'],
            ['**GS (glutamina sintetasa)**', 'Disponibilidad de NH_{4}^{+}/glutamato', 'Captura de amonio perivenosa/astrocitos'],
            ['**AMPK**', 'AMP/ADP ↑, Thr172', 'Ahorro de ATP / movilización de energía'],
            ['**LPL**', 'ApoC-II (+); ApoC-III (−) y moduladores', 'Liberación de AG desde TAG de QM/VLDL']]
    for part, sl in ((1, rows[:9]), (2, [rows[0]] + rows[9:])):
        s = new(D, U, 'Red de enzimas reguladoras (%d/2)' % part, 'SISTEMATIZACIÓN')
        t, H = table(s, 0.4, 1.1, 12.5, sl, [3.4, 4.6, 4.5], size=15, rowh=0.66, name='Tabla enzimas %d' % part)
        s.step(fade(t))
        s.note('Red de enzimas de alta rentabilidad para examen oral o de opción múltiple: para cada enzima, la señal clave que la '
               'regula y la vía o efecto que controla. Relacionar cada fila con la escala de regulación (alostérica, covalente o '
               'génica) y con el estado nutricional.')


def five_q(D):
    s = new(D, U, 'Esquema oral: cinco preguntas maestras', 'SISTEMATIZACIÓN')
    qs = [('¿Cuál es la señal?', 'Insulina, glucagón, catecolaminas, cortisol, carga de sustratos, AMP, acetil-CoA, malonil-CoA, O_{2}', 'ins'),
          ('¿Dónde ocurre?', 'Órgano, célula y compartimento: citosol, mitocondria, RE, peroxisoma o sangre', 'glc'),
          ('¿Qué enzima decide?', 'Paso regulador; control alostérico, covalente o génico', 'atp'),
          ('¿A dónde va el C o el N?', 'Glucosa, lactato, CO_{2}, acetil-CoA, cuerpos cetónicos, urea y NH_{4}^{+}', 'nh4'),
          ('¿Qué problema resuelve y qué pasa si falla?', 'Hipoglucemia, acidosis, hiperamonemia, esteatosis, hipertrigliceridemia o déficit de ATP', 'cc')]
    ids = []
    for i, (q, d, k) in enumerate(qs):
        y = 1.1 + i * 1.18
        g = s.group_start('Pregunta %d' % (i + 1))
        badge(s, 0.45, y + 0.2, i + 1, 0.65)
        s.shape(1.3, y, 11.6, 1.05, 'rect', [LBLUE, MINT, YEL, LSALMON, PINK][i], (INK, 1.25), SHD)
        s.text(1.45, y + 0.05, 4.2, 0.95, q, 17, F_HEAD, INK, True, 'l', 'm')
        s.text(5.7, y + 0.05, 6.4, 0.95, d, 14, F_BODY, INK, False, 'l', 'm')
        mol(s, 12.25, y + 0.3, k, d=0.48)
        s.group_end(); ids.append(g)
    for g in ids:
        s.step(fade(g))
    s.note('Esquema oral de cinco preguntas maestras para cualquier situación metabólica: 1) ¿cuál es la señal?; 2) ¿dónde '
           'ocurre?; 3) ¿qué enzima decide y con qué tipo de control?; 4) ¿a dónde va el carbono o el nitrógeno?; 5) ¿qué problema '
           'resuelve y qué pasa si falla? Secuencia sugerida para exponer: primero señal → receptor; después enzima activada o '
           'inhibida; después flujo metabólico; por último el cambio plasmático o el síntoma.')


def errors(D):
    err = [('«El hígado quema sus propias cetonas»', 'Carece de **SCOT/OXCT1** funcional.'),
           ('«El músculo libera glucosa de su glucógeno al plasma»', 'No posee capacidad relevante de **G6Pasa**.'),
           ('«El eritrocito usa cetonas y β-oxidación en ayuno»', 'No tiene **mitocondrias**.'),
           ('«El glucagón siempre baja después de comer proteína»', 'Una comida proteica puede estimular **insulina y glucagón**.'),
           ('«El lactato es desperdicio exclusivamente anaeróbico»', 'También es **combustible**, precursor de glucosa y metabolito señal.'),
           ('«Toda la fructosa se convierte en grasa»', 'Muchos destinos; la DNL puede aumentar con **altas cargas**.'),
           ('«La urea aumenta sin límite cuanto más dura la inanición»', 'La adaptación cetónica **ahorra proteína**.'),
           ('«HDL-C alto necesariamente evita la aterosclerosis»', 'Concentración ≠ **funcionalidad**; la retención de **ApoB** es causal.'),
           ('«MCT sirve para reemplazar todas las grasas»', 'Se precisan **AG esenciales** y vitaminas liposolubles.'),
           ('«En encefalopatía conviene siempre bajar proteína a 0,8 g/kg»', 'No es recomendación general **actual**.'),
           ('«AMPK es una enzima que fabrica ATP»', 'Es **sensor** y regulador que redirige flujos.'),
           ('«PYY y polipéptido pancreático son lo mismo»', 'Son **distintos**, aunque de una familia de péptidos afines.')]
    for part in (1, 2):
        s = new(D, U, 'Errores conceptuales frecuentes (%d/2)' % part, 'SISTEMATIZACIÓN')
        ids = []
        for i, (e, c) in enumerate(err[(part - 1) * 6: part * 6]):
            y = 1.1 + i * 0.95
            g = s.group_start('Error %d' % i)
            s.shape(0.4, y, 6.5, 0.82, 'rect', LSALMON, (INK, 1.25), SHD, '✗  ' + e, 14, F_BODY, INK, False, 'l', 'm', (0.15, 0, 0.1, 0))
            s.arrow([(6.95, y + 0.41), (7.35, y + 0.41)], ACT, 3)
            s.shape(7.4, y, 5.5, 0.82, 'rect', MINT, (INK, 1.25), SHD, '✓  ' + c, 14, F_BODY, INK, False, 'l', 'm', (0.15, 0, 0.1, 0))
            s.group_end(); ids.append(g)
        for g in ids:
            s.step(fade(g))
        s.note('Errores conceptuales especialmente frecuentes: cada afirmación incorrecta (izquierda, rojo) aparece con su '
               'corrección fisiológica (derecha, verde). Usar como ejercicio de discusión: mostrar primero el error y pedir a los '
               'estudiantes que lo corrijan antes del siguiente clic.')


def distinctions(D):
    dd = [('Estado alimentado', 'Estado posabsortivo', 'Absorción activa e insulina alta frente a producción endógena de glucosa sin aporte intestinal.'),
          ('Cetosis fisiológica', 'Cetoacidosis', 'Insulina residual y pH conservado frente a insulinopenia, producción > utilización y acidosis.'),
          ('Glucogenólisis', 'Gluconeogénesis', 'Moviliza glucosa almacenada (horas iniciales) frente a síntesis nueva desde lactato, AA y glicerol (consume ATP/GTP).'),
          ('Oxidación lipídica', 'Lipogénesis', 'Mitocondria, CPT1 libre (malonil ↓) frente a citosol, ACC/FASN y malonil-CoA ↑.'),
          ('Insulina plasmática', 'Sensibilidad tisular', 'Cuánta hormona hay frente a cuánta acción produce en cada tejido.'),
          ('Glucemia', 'Flujo de glucosa', 'Concentración frente a velocidad de producción y utilización.'),
          ('Lipoproteínas', 'AG libres', 'TAG esterificados en partículas (QM, VLDL) frente a AG unidos a albúmina.'),
          ('Acumulación de TAG', 'Intermediarios lipotóxicos', 'Gotas relativamente inertes frente a DAG/ceramidas que alteran la señal de insulina.'),
          ('Ureogénesis', 'Amoniogénesis', 'Hígado → urea frente a riñón → NH_{4}^{+} urinario y HCO_{3}^{−} nuevo.'),
          ('Glutaminasa', 'Glutamina sintetasa', 'Libera NH_{4}^{+} frente a lo captura gastando ATP.'),
          ('Contracción muscular', 'Consumo energético', 'Ca^{2+} y AMP activan glucogenólisis, GLUT4 y AMPK; la intensidad define el combustible.'),
          ('Regulación alostérica', 'Fosforilación / regulación génica', 'Segundos (efectores) frente a minutos (PKA, Akt, AMPK) frente a horas–días (CREB, FOXO1, SREBP).')]
    for part in (1, 2):
        s = new(D, U, 'Distinciones que deben resistir un examen (%d/2)' % part, 'SISTEMATIZACIÓN')
        ids = []
        for i, (a, b, d) in enumerate(dd[(part - 1) * 6: part * 6]):
            x = 0.4 + (i % 2) * 6.35; y = 1.1 + (i // 2) * 1.85
            g = s.group_start('Distinción %s' % a)
            s.shape(x, y, 6.15, 1.7, 'rect', CREAM, (INK, 1.25), SHD)
            chip(s, x + 0.12, y + 0.12, a, TAG, 13.5, h=0.42)
            s.text(x + 0.25 + chipw(a, 13.5), y + 0.12, 0.5, 0.42, 'vs', 13.5, F_HEAD, INH, True, 'c', 'm')
            chip(s, x + 0.8 + chipw(a, 13.5), y + 0.12, b, LBLUE, 13.5, h=0.42)
            s.text(x + 0.15, y + 0.65, 5.85, 1.0, d, 13.5, F_BODY, INK, False, 'l', 'm')
            s.group_end(); ids.append(g)
        for g in ids:
            s.step(fade(g))
        s.note('Distinciones conceptuales verificadas a lo largo de la clase. Cada par resume la diferencia esencial; las '
               'diapositivas de cada tema desarrollan el mecanismo correspondiente.')


def final_map(D):
    s = new(D, U, 'Resumen visual integrador: órganos, hormonas y combustibles', 'MAPA FINAL')
    ids = organ_map(s)
    fed = s.group_start('Capa alimentado')
    for pts in (((1.8, 4.45), (1.8, 4.1)), ((2.4, 3.5), (2.4, 3.1)), ((10.4, 3.5), (10.4, 2.85)), ((9.4, 4.1), (9.4, 4.55)), ((6.4, 3.5), (6.4, 2.7))):
        s.arrow(list(pts), TRN, 4)
    mol(s, 1.95, 3.98, 'glc', d=0.36); mol(s, 2.55, 3.05, 'glc', d=0.36); mol(s, 9.55, 4.15, 'glc', d=0.36); mol(s, 6.55, 2.95, 'glc', d=0.36)
    chip(s, 3.75, 0.98, 'ALIMENTADO: insulina ↑', LBLUE, 13, name='Etiqueta alimentado')
    s.group_end()
    fst = s.group_start('Capa ayuno')
    for pts in (((10.9, 2.85), (10.9, 3.5)), ((3.0, 3.1), (3.0, 3.5)), ((8.9, 4.55), (8.9, 4.1)), ((7.0, 3.5), (7.0, 2.7)), ((5.9, 4.45), (5.9, 4.1))):
        s.arrow(list(pts), '8E44AD', 4)
    ag_chain(s, 11.05, 3.0, 0.7, 0.16); mol(s, 3.15, 3.05, 'glc', d=0.36); mol(s, 8.25, 4.15, 'ala', d=0.36); mol(s, 7.15, 2.95, 'cc', d=0.36); mol(s, 6.0, 4.1, 'glc', d=0.34)
    chip(s, 3.75, 1.45, 'AYUNO: glucagón/insulina ↑', LILAC, 13, name='Etiqueta ayuno')
    s.group_end()
    hor = s.group_start('Capa hormonas')
    for t, k, x, y in (('Insulina', 'ins', 3.45, 2.1), ('Glucagón', 'gcg', 4.55, 2.1), ('Cortisol', 'chol', 6.3, 4.95), ('Adrenalina', 'gcg', 6.3, 5.5), ('Leptina', 'gly', 8.0, 2.95), ('T3', 'atp', 7.0, 6.55)):
        mol(s, x, y, k, t, d=0.45, w=1.05, size=11)
    s.group_end()
    tx = card(s, 3.05, 5.2, 1.9, 1.85, '**Azul**: alimentado\n**Violeta**: ayuno\nFichas: combustibles\nPíldoras: hormonas', CREAM, 12, name='Leyenda final', grow=False)
    s.step(wipe(ids['vessel'], 'l'))
    s.step(fade(fed))
    s.step(out(fed), fade(fst, after=True))
    s.step(fade(hor), fade(tx))
    s.step(fade(fed))
    s.note('Gran esquema final: todos los órganos conectados por la sangre. Primer clic: la circulación. Segundo: la capa del '
           'estado alimentado (flechas azules: glucosa desde el intestino al hígado, músculo, adiposo y cerebro). Tercero: se '
           'reemplaza por la capa del ayuno (flechas violetas: AG y glicerol desde el adiposo, glucosa desde hígado y riñón, alanina '
           'desde el músculo, cuerpos cetónicos hacia el cerebro). Cuarto: las hormonas que gobiernan los cambios (insulina, '
           'glucagón, cortisol, adrenalina, leptina, T3). Quinto: superposición de ambas capas para cerrar con la idea de '
           'alternancia: abundancia y carencia se suceden y cada tejido determina lo que queda disponible para el resto.')


def biblio(D):
    s = new(D, U, 'Bibliografía', 'REFERENCIAS')
    l = card(s, 0.4, 1.1, 6.1, 5.95, '- Nelson DL, Cox MM. **Lehninger. Principios de bioquímica**. 8.ª ed. Omega/Macmillan.\n- Rodwell VW, et al. **Harper. Bioquímica ilustrada**. 32.ª ed. McGraw-Hill.\n- Ferrier DR. **Lippincott. Bioquímica**. 8.ª ed. Wolters Kluwer.\n- Hall JE, Hall ME. **Guyton y Hall. Tratado de fisiología médica**. 14.ª ed. Elsevier.\n- Devlin TM. **Bioquímica con aplicaciones clínicas**. Reverté.', CREAM, 13.5, head='Textos de referencia')
    r = card(s, 6.8, 1.1, 6.1, 5.95, '- Goldberg D, Goldstein I. Endocrine regulation of the hepatic fasting response. Nat Rev Endocrinol. 2026.\n- Vallon V, Wewer Albrechtsen NJ. Liver–kidney crosstalk and glucagon. Nat Rev Nephrol. 2026.\n- de Graaf et al. Metabolite transport across liver zones. Acta Physiol. 2024.\n- ACG Clinical Guideline: Hepatic Encephalopathy. Am J Gastroenterol. 2026.\n- Lee K et al. CPT1A deficiency. GeneReviews, 2025.\n- Approach to the adult patient with chylomicronemia. J Clin Endocrinol Metab. 2026.\n- Geidl-Flueck B, Gerber PA. Fructose and de novo lipogenesis. J Endocrinol. 2023.\n- ACC Expert Consensus on persistent hypertriglyceridemia. JACC. 2021.\n- Brain glucose metabolism. Physiol Rev. · Fasting physiology: Cell Metab 2014; Physiol Rev 2022.', LBLUE, 11.5, head='Revisiones y guías', minsize=10)
    s.step(fade(l)); s.step(fade(r))
    s.note('Referencias completas y enlaces (para consulta del docente):\n'
           'Goldberg D, Goldstein I. Endocrine regulation of the hepatic fasting response. Nature Reviews Endocrinology. 2026. '
           'https://www.nature.com/articles/s41574-025-01228-3\n'
           'From starvation to time-restricted eating: a review of fasting physiology (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC12455479/\n'
           'Complex physiology and clinical implications of time-restricted eating. Physiological Reviews. 2022. https://journals.physiology.org/doi/full/10.1152/physrev.00006.2022\n'
           'Vallon V, Wewer Albrechtsen NJ. Metabolic control by liver–kidney crosstalk and glucagon in health and disease. Nature Reviews Nephrology. 2026. https://www.nature.com/articles/s41581-026-01111-y\n'
           'de Graaf et al. Getting in the zone: Metabolite transport across liver zones. Acta Physiologica. 2024. https://onlinelibrary.wiley.com/doi/10.1111/apha.14239\n'
           'ACG Clinical Guideline: Hepatic Encephalopathy. Am J Gastroenterol. 2026. https://doi.org/10.14309/ajg.0000000000003899\n'
           'AASLD Practice Guidance on Acute-on-Chronic Liver Failure. Hepatology. https://doi.org/10.1097/hep.0000000000000671\n'
           'Lee K et al. Carnitine Palmitoyltransferase 1A Deficiency. GeneReviews, actualización 2025. https://www.ncbi.nlm.nih.gov/books/NBK1527/\n'
           'Approach to the Adult Patient with Chylomicronemia. J Clin Endocrinol Metab. 2026. https://academic.oup.com/jcem/article/111/3/845/8407532\n'
           'Geidl-Flueck B, Gerber PA. Fructose drives de novo lipogenesis affecting metabolic health. J Endocrinol. 2023. https://pubmed.ncbi.nlm.nih.gov/36753292/\n'
           'ACC Expert Consensus Decision Pathway on Persistent Hypertriglyceridemia. JACC. 2021. https://www.jacc.org/doi/10.1016/j.jacc.2021.06.011\n'
           'Brain Glucose Metabolism: Integration of Energetics with Function. Physiological Reviews. https://doi.org/10.1152/PHYSREV.00062.2017\n'
           'Fasting: Molecular Mechanisms and Clinical Applications. Cell Metabolism. 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC3946160/\n'
           'Criterio: el contenido de las diapositivas sigue el material de estudio de Integración Metabólica (43 consignas) y se '
           'amplía con los textos de referencia citados; las ampliaciones bibliográficas se indican en las notas de cada '
           'diapositiva. Los ejemplos numéricos son aproximaciones fisiológicas, no algoritmos de manejo; el acoplamiento '
           'lactato astrocito–neurona y la magnitud precisa de flujos en ayuno tienen variabilidad y debate.')


def closing(D):
    s = D.new(PEACH); s.unit = 6
    for i, (x, y, d) in enumerate(((11.6, -0.3, 1.2), (12.4, 0.7, 0.8), (10.9, 0.6, 0.6))):
        rbc(s, x, y, d, name='Deco eritrocito %d' % i)
    muscle_fiber(s, 9.5, 6.35, 4.2, 0.5, name='Deco fibra 1'); muscle_fiber(s, 9.9, 6.85, 3.8, 0.5, name='Deco fibra 2')
    adipocyte_white(s, -0.3, 5.8, 1.6, name='Deco adipocito'); mito(s, 1.3, 6.4, 1.2, name='Deco mito')
    big_title(s, 0.6, 1.6, 12.1, 2.0, '¡GRACIAS!', 80, color=RED, name='Gracias')
    s.text(1.5, 3.7, 10.3, 0.7, 'INTEGRACIÓN METABÓLICA · Del estado alimentado a la inanición y la enfermedad', 20, F_HEAD, INK, True, 'c', 'm')
    q = chip(s, 4.4, 4.7, 'Preguntas y discusión', TAG, 20, h=0.7, shadow=SHD, name='Preguntas')
    s.note('Cierre. Proponer a los estudiantes resolver un caso nuevo aplicando las cinco preguntas maestras.')


def build(D):
    div(D)
    cases(D)
    enzymes(D); five_q(D); errors(D); distinctions(D)
    final_map(D); biblio(D); closing(D)
