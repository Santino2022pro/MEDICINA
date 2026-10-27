# -*- coding: utf-8 -*-
"""UNIDAD III — Caso 12: estado hiperglucémico hiperosmolar"""
from base import *

U = 3


def div(D):
    def art(s):
        s.pic('brain-2', 10.7, 0.6, 2.4, name='Cerebro')
        s.pic('kidney-1', 11.3, 3.4, 1.3, name='Riñón')
        model(s, 'glucosa', 0.2, 1.2, 2.3, name='Glucosa 3D')
        model(s, 'h2o', 0.6, 4.6, 1.2, name='Agua 3D', label='H₂O')
    divider(D, U, 'III', 'CASO 12: ESTADO\nHIPERGLUCÉMICO HIPEROSMOLAR', 'Insulina residual, agua perdida y neuronas deshidratadas',
            ['Presentación y laboratorio', '¿Por qué no hay cetonas?', 'Ejemplo 4: de la glucosuria al coma', 'Tonicidad y movimiento de agua',
             'Osmolalidad total, efectiva y Na⁺ corregido', 'Vías alteradas y riesgos de corrección', 'Dieta, glibenclamida y ejercicio'], art,
            'Unidad III. Caso clínico 12: varón de 53 años con obesidad, hipertensión y alteración grave de la conciencia por un estado '
            'hiperglucémico hiperosmolar. El eje conceptual es la insulina residual: suficiente para limitar la cetogénesis, '
            'insuficiente para evitar la hiperglucemia extrema y la deshidratación.')


def case(D):
    s = new(D, U, 'Caso 12 · presentación clínica', 'blue')
    s.pic('obese-man', 0.5, 1.15, h=5.8, name='Paciente caso 12')
    ps = [('VARÓN DE 53 AÑOS', 'Obesidad · HTA · tabaquismo · sedentarismo · estrés psicosocial (despido laboral)', 'y'),
          ('CONCIENCIA', 'Alteración aguda: **Glasgow 7/15**', 'r'),
          ('HEMODINAMIA', 'Hipotensión **90/55 mmHg** · taquicardia **120 lpm**', 's'),
          ('DESHIDRATACIÓN', 'Mucosas secas · **signo del pliegue** positivo', 'g'),
          ('ANTECEDENTES', '**No** se informa diabetes previa ni medicación hipoglucemiante', 'b')]
    ids = []
    for i, (h, t, k) in enumerate(ps):
        y = 1.15 + i * 1.15
        g = s.group_start('Dato ' + h)
        mbox(s, 4.0, y, 3.0, 0.95, h, k, 14)
        tbox(s, 7.15, y, 5.8, 0.95, t, 15, anchor='m')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Caso 12. Varón de 53 años con obesidad, hipertensión, tabaquismo, sedentarismo y estrés psicosocial, que presenta '
           'alteración aguda de la conciencia (Glasgow 7), hipotensión 90/55 mmHg, taquicardia 120 lpm y signos de deshidratación '
           '(mucosas secas, signo del pliegue positivo). No se informa diabetes previa ni medicación hipoglucemiante.')


def labs(D):
    s = new(D, U, 'Caso 12 · laboratorio y criterios', 'cyan')
    rows = [['Variable', 'Valor', 'Inferencia'],
            ['Glucemia', '683 mg/dL', 'Hiperglucemia extrema'],
            ['Glucosuria', '+++', 'Gran carga de glucosa urinaria'],
            ['Cetonemia / cetonuria', 'Negativas', 'Sin cetosis significativa detectada'],
            ['Osmolalidad plasmática', '325 mOsm/kg', 'Hiperosmolalidad; no se aclara si total o efectiva'],
            ['pH', '7,41', 'Sin acidemia'],
            ['HCO₃⁻', '23 mEq/L', 'Normal-bajo, sin acidosis importante'],
            ['pCO₂', '39 mmHg', 'Aproximadamente normal'],
            ['Glasgow', '7/15', 'Compromiso neurológico grave']]
    table(s, 0.4, 1.15, 7.4, rows, [2.2, 1.6, 3.6], size=13.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla caso 12')
    rows2 = [['Criterio EHH (consenso 2024)', 'Caso 12'], ['Glucosa ≥ 600 mg/dL', '683 → sí'], ['Osm. efectiva > 300 o total > 320', '325 (tipo no aclarado)'],
             ['β-OHB < 3,0 mmol/L', 'Cetonas negativas (cualitativo)'], ['pH ≥ 7,3 y HCO₃⁻ ≥ 15', '7,41 · 23 → sí']]
    t2, H = table(s, 8.1, 1.15, 4.85, rows2, [2.6, 2.25], size=12.5, head_fill=SALBOX, fills=(WHITE, 'FDE2E2'), name='Criterios EHH')
    p = pearl(s, 8.1, 1.25 + H + 0.2, 4.85, 1.6, 'Patrón **altamente sugerente de EHH** (HHS), frecuente en **DM2 no diagnosticada** o descompensada. La gravedad neurológica y hemodinámica exige atención crítica.', 13.5)
    s.step(fade(t2)); s.step(zoom(p))
    s.note('Pregunta 1. La glucosa supera 600 mg/dL, la osmolalidad informada supera 320 mOsm/kg, hay glucosuria intensa y no se '
           'aprecia cetosis ni acidosis metabólica: patrón altamente sugerente de estado hiperglucémico hiperosmolar, frecuente en '
           'DM2 no diagnosticada o descompensada. El consenso 2024 utiliza glucosa ≥600, osmolalidad efectiva >300 o total >320 '
           'mOsm/kg, ausencia de cetonemia significativa (β-OHB <3,0 mmol/L) y ausencia de acidosis importante (pH ≥7,3 y HCO₃⁻ '
           '≥15). La osmolalidad 325 no especifica si es total o efectiva: esa incertidumbre se mantiene.')


def no_ketones(D):
    s = new(D, U, 'Pregunta 2 · ¿por qué cetonemia y cetonuria negativas?', 'peachW')
    cats = ['0', '5', '10', '20', '40', '80', '160']
    cid = chart_line(s, 0.4, 1.15, 7.6, 4.3, cats,
                     [('Inhibición de la lipólisis', [0, 45, 70, 88, 96, 99, 100]),
                      ('Supresión de producción hepática de glucosa', [0, 10, 22, 45, 70, 88, 96]),
                      ('Captación muscular de glucosa', [0, 3, 8, 20, 42, 68, 88])],
                     ['C00000', '7030A0', '1F4E9A'], title_txt='Efecto (% del máximo) según concentración de insulina — esquema', xtitle='Insulina (unidades arbitrarias)',
                     size=11, name='Dosis-respuesta')
    zone = s.shape(2.15, 1.75, 1.35, 3.0, 'rect', ('a', 'FFC000', 35), ('C00000', 2.0, 'dash'), False, name='Zona insulina residual')
    zl = lab(s, 3.55, 3.75, 2.0, 0.5, '← insulina residual\nen el EHH', 12, INH, align='l')
    st = steps_panel(s, 8.3, 1.15, 4.65, ['Persiste **secreción endógena**: insuficiente para la euglucemia…',
                                          '…pero suficiente para **frenar la lipólisis** y limitar la cetogénesis.',
                                          'El umbral antilipolítico es **menor** que el necesario para normalizar captación y producción de glucosa.',
                                          'Contribuyen glucagón, disponibilidad de AG, función renal y **duración** del proceso.'], 13.5, anim=False)[0]
    p = pearl(s, 0.4, 5.75, 12.55, 1.1, 'No es una regla absoluta: existen **cuadros mixtos CAD/EHH** con cetosis importante e hiperosmolalidad.', 16)
    s.step(zoom(zone), fade(zl, after=True))
    for g in st:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Pregunta 2. En muchos pacientes con EHH persiste cierta secreción endógena de insulina, insuficiente para mantener la '
           'euglucemia pero bastante para inhibir la lipólisis y, con ello, limitar la cetogénesis. La concentración de insulina que '
           'frena la lipólisis puede ser inferior a la necesaria para normalizar la captación periférica y la producción hepática de '
           'glucosa: el gráfico (curvas dosis-respuesta conceptuales, no datos medidos) lo muestra con la curva de lipólisis '
           'desplazada a la izquierda. También influyen el glucagón, la disponibilidad de ácidos grasos, la función renal y la '
           'duración del proceso. No es una regla absoluta: hay cuadros mixtos CAD/EHH.')


def example4(D):
    s = new(D, U, 'Ejemplo 4 · de la insulina residual al coma', 'greenR')
    items = [('ins', 'Insulina residual (cetogénesis limitada)', 's'), ('ri', 'Resistencia insulínica', 's'), ('hg', 'Hiperglucemia extrema (683)', 'y'),
             ('gu', 'Glucosuria', 'Y'), ('w', 'Pérdidas urinarias de agua', 'Y'), ('osm', 'Hiperosmolalidad', 'y'),
             ('cv', 'Salida de agua celular · volumen neuronal ↓', 'Y'), ('neu', 'Alteraciones neurológicas (Glasgow 7)', 'r')]
    nodes = {'ins': (0.4, 1.3, 3.2, 0.7, items[0][1], 's', 13), 'ri': (0.4, 2.3, 3.2, 0.7, items[1][1], 's', 14),
             'hg': (4.2, 1.8, 3.0, 0.7, items[2][1], 'y', 14), 'gu': (7.8, 1.8, 2.3, 0.7, items[3][1], 'Y', 14),
             'w': (10.6, 1.8, 2.35, 0.7, items[4][1], 'Y', 13), 'osm': (10.6, 3.3, 2.35, 0.7, items[5][1], 'y', 14),
             'cv': (6.4, 3.3, 3.7, 0.7, items[6][1], 'Y', 13), 'neu': (2.2, 3.3, 3.7, 0.7, items[7][1], 'r', 13),
             'hd': (10.6, 4.7, 2.35, 0.75, 'Hipovolemia · hipotensión', 'r', 13)}
    edges = [('ins', 'hg', {'pts': [(3.65, 1.65), (4.15, 2.0)]}), ('ri', 'hg', {'pts': [(3.65, 2.65), (4.15, 2.3)]}), ('hg', 'gu'), ('gu', 'w'), ('w', 'osm'),
             ('osm', 'cv'), ('cv', 'neu'), ('w', 'hd', {'pts': [(12.95, 2.15), (13.1, 2.15), (13.1, 5.05), (12.97, 5.05)]})]
    graph(s, nodes, edges, [['ins', 'ri'], ['ins>hg', 'ri>hg', 'hg'], ['hg>gu', 'gu', 'gu>w', 'w'], ['w>osm', 'osm'], ['osm>cv', 'cv', 'cv>neu', 'neu'], ['w>hd', 'hd']])
    t = tbox(s, 0.4, 4.6, 9.9, 2.3, '- La evolución hacia EHH suele requerir **días**: el déficit de agua aumenta gradualmente.\n- La pérdida relativa de **agua libre** respecto de solutos favorece la hiperosmolalidad.\n'
             '- La DM2 descompensada **no** es ausencia completa de insulina: el freno de la lipólisis puede conservarse más que el control glucémico.', 14.5, head='Claves')
    s.step(fade(t))
    s.note('Ejemplo 4 de animación: insulina residual suficiente para limitar la cetogénesis marcada + resistencia insulínica → '
           'hiperglucemia extrema → glucosuria → pérdidas urinarias de agua → hiperosmolalidad → cambios en el volumen celular → '
           'alteraciones neurológicas; en paralelo, la pérdida de agua produce hipovolemia e hipotensión. La evolución suele requerir '
           'días, con aumento gradual del déficit de agua [C24].')


def ph_normal(D):
    s = new(D, U, 'Pregunta 3 · ¿por qué el pH es normal?', 'cyan')
    l = s.group_start('CAD balanza')
    mbox(s, 0.5, 1.25, 5.9, 0.6, 'CAD: CETOÁCIDOS ↑↑ → HCO₃⁻ CONSUMIDO', 'r', 14)
    for i in range(6):
        mol(s, 0.8 + i * 0.9, 2.1, 'cc', d=0.5, text='CC', name='CC CAD %d' % i)
    for i in range(2):
        s.shape(1.6 + i * 2.4, 2.9, 1.0, 0.45, 'roundRect', '9DC3E6', (INK, 1.0), False, 'HCO₃⁻', 12, F_HEAD, INK, True, 'c', 'm', fit=False)
    s.group_end()
    r = s.group_start('EHH balanza')
    mbox(s, 6.9, 1.25, 6.0, 0.6, 'EHH: SIN CARGA CETOÁCIDA IMPORTANTE', 'g', 14)
    mol(s, 7.3, 2.1, 'cc', d=0.5, text='CC', name='CC EHH')
    for i in range(5):
        s.shape(8.2 + i * 0.95, 2.1, 0.88, 0.45, 'roundRect', '9DC3E6', (INK, 1.0), False, 'HCO₃⁻', 12, F_HEAD, INK, True, 'c', 'm', fit=False)
    formula(s, 7.6, 2.85, 4.6, 0.6, 'pH 7,41 · HCO₃⁻ 23 · pCO₂ 39', 17)
    s.group_end()
    st = steps_panel(s, 0.4, 3.85, 12.55, ['El sistema tampón y la regulación respiratoria/renal **sostienen el pH**; la gasometría es globalmente compatible con ausencia de acidosis relevante.',
                                           'La **hiperosmolalidad no produce por sí sola acidemia**.',
                                           'Infección, hipoperfusión prolongada o lesión renal podrían **añadir después** acidosis láctica u otro componente.'], 14.5, anim=False)[0]
    s.step(fade(l)); s.step(fade(r))
    for g in st:
        s.step(fade(g))
    s.note('Pregunta 3. Al no generarse cantidades elevadas de cetoácidos no se consume bicarbonato masivamente como en la CAD. El '
           'sistema tampón y la regulación respiratoria y renal sostienen el pH. La gasometría (7,41 / 39 / 23) es globalmente '
           'compatible con ausencia de una acidosis relevante, aunque su consistencia exacta debe interpretarse con la incertidumbre '
           'de muestras redondeadas (Henderson–Hasselbalch con 23 y 39 da ≈7,39). La hiperosmolalidad no produce por sí sola '
           'acidemia; una infección, hipoperfusión prolongada o lesión renal podría añadir luego acidosis láctica u otro componente.')


def dehydration(D):
    s = new(D, U, 'Pregunta 4 · ¿qué explica la deshidratación?', 'peachW')
    s.pic('obese-man', 0.4, 1.15, h=5.7, name='Paciente deshidratado')
    sg = [(3.2, 1.55, 'Mucosas secas'), (3.2, 2.55, 'Signo del pliegue +'), (3.2, 3.55, 'Taquicardia 120'), (3.2, 4.55, 'Hipotensión 90/55')]
    ids = [mbox(s, x, y, 2.3, 0.55, t, 's', 13.5, caps=False) for x, y, t in sg]
    ch = [mbox(s, 6.0, 1.2, 6.95, 0.55, 'Glucemia 683 → filtración masiva de glucosa', 'Y', 14, caps=False),
          mbox(s, 6.0, 1.95, 6.95, 0.55, 'Glucosuria +++ → diuresis osmótica', 'Y', 14, caps=False),
          mbox(s, 6.0, 2.7, 6.95, 0.55, 'Pierde más agua de la que repone → hipovolemia', 'Y', 14, caps=False),
          mbox(s, 6.0, 3.45, 6.95, 0.55, 'Pérdida de agua libre > solutos → hiperosmolalidad', 'y', 14, caps=False)]
    t = tbox(s, 6.0, 4.35, 6.95, 2.5, 'La hiperosmolalidad **extrae agua intracelular** y afecta especialmente a las **neuronas**. Pliegue y mucosas apoyan el déficit hídrico, pero **ningún signo aislado lo cuantifica** con precisión ni sustituye la valoración clínica.', 15, head='Interpretación')
    for c in ch:
        s.step(fade(c))
    s.step(*[zoom(g, after=i > 0, dur=250) for i, g in enumerate(ids)])
    s.step(fade(t))
    s.note('Pregunta 4. Glucemia 683 → filtración masiva de glucosa → glucosuria +++ → diuresis osmótica. El paciente pierde más agua '
           'de la que repone: hipovolemia, hipotensión, taquicardia, menor turgencia cutánea y mucosas secas. La pérdida relativa de '
           'agua libre respecto de solutos favorece la hiperosmolalidad, que extrae agua intracelular y afecta especialmente a las '
           'neuronas. Ningún signo aislado cuantifica con precisión el déficit ni sustituye la valoración clínica.')


def neuron_scene(s, state, title_txt):
    """state: 0 isotónico · 1 hipertónico (célula contraída) · 2 corrección brusca (tumefacción)"""
    sz = {0: 3.0, 1: 2.1, 2: 3.6}[state]
    cx, cy = 3.6, 3.95
    s.shape(0.4, 1.15, 6.6, 5.7, 'rect', ('a', 'FFFFFF', 40) if state == 0 else (('a', 'FFC000', 30) if state == 1 else ('a', '9DC3E6', 40)), (INK, 1.5), False,
            name='!!Medio extracelular')
    lab(s, 0.55, 1.2, 6.3, 0.4, title_txt, 13.5, name='!!Rótulo medio')
    s.shape(cx - sz / 2, cy - sz / 2, sz, sz, 'ellipse', shade('C39BD3', 0.45, 0.25), ('5B2C6F', 2.5), SHD, 'NEURONA', 14, F_HEAD, INK, True, 'c', 'm',
            fit=False, name='!!Neurona osm')
    # agua
    pos_in = [(cx - 0.8, cy - 0.7), (cx + 0.3, cy - 0.8), (cx - 0.6, cy + 0.45), (cx + 0.45, cy + 0.4), (cx - 0.1, cy + 0.9), (cx - 1.0, cy - 0.1)]
    pos_out = [(0.8, 1.9), (6.2, 2.0), (0.9, 5.9), (6.1, 5.8), (5.9, 3.9), (1.0, 4.0)]
    for i in range(6):
        if state == 1 and i < 4:
            x, y = pos_out[i]
        elif state == 2:
            x, y = pos_in[i]
        else:
            x, y = pos_in[i] if i < 4 else pos_out[i]
        s.shape(x, y, 0.4, 0.4, 'ellipse', '5DADE2', ('1F618D', 1.0), False, 'H₂O', 8, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                name='!!Agua osm %d' % i)
    # glucosa extracelular
    n = {0: 3, 1: 9, 2: 3}[state]
    gp = [(1.0, 2.6), (5.8, 2.7), (1.5, 5.3), (5.6, 5.1), (2.0, 1.85), (5.1, 1.85), (0.9, 3.3), (6.1, 3.2), (3.4, 6.2)]
    for i in range(9):
        x, y = gp[i]
        if i < n:
            mol(s, x, y, 'glc', d=0.42, name='!!Glc osm %d' % i)


def tonicity(D):
    s = new(D, U, 'Tonicidad · 1 · neurona en medio isotónico', 'blue')
    neuron_scene(s, 0, 'PLASMA ISOTÓNICO (~285–295 mOsm/kg)')
    t = tbox(s, 7.3, 1.15, 5.65, 3.0, '- El agua cruza libremente las membranas por **acuaporinas**.\n- Se mueve hacia donde hay **más solutos efectivos** (que no atraviesan la membrana).\n'
             '- En equilibrio, la osmolalidad intracelular = extracelular: el **volumen neuronal** es estable.', 15, head='Principio')
    s.step(fade(t))
    s.note('Tonicidad, paso 1 (Morph en tres diapositivas). En condiciones isotónicas el agua entra y sale de la neurona sin cambio '
           'neto de volumen. El intervalo de osmolalidad plasmática normal (~285–295 mOsm/kg) es ampliación bibliográfica.')


def tonicity2(D):
    s = new(D, U, 'Tonicidad · 2 · hiperglucemia: el agua sale de la neurona', 'blue', morph=True)
    neuron_scene(s, 1, 'PLASMA HIPERTÓNICO: GLUCOSA ↑↑ (soluto efectivo)')
    t = tbox(s, 7.3, 1.15, 5.65, 3.4, '- La glucosa, sin insulina eficaz en muchos tejidos, actúa como **soluto efectivo** extracelular.\n- El agua **sale** de las células → **deshidratación neuronal**.\n'
             '- Resultado clínico: **somnolencia, confusión, coma** (Glasgow 7).', 15, head='Hipertonicidad')
    p = pearl(s, 7.3, 4.8, 5.65, 1.4, 'El daño depende de la **tonicidad** (osmolalidad efectiva), no de la osmolalidad total.', 15)
    s.step(fade(t)); s.step(zoom(p))
    s.note('Tonicidad, paso 2. Por Morph la neurona se contrae y las fichas de agua migran al compartimiento extracelular mientras '
           'aumentan las fichas de glucosa: la hiperglucemia eleva la tonicidad y extrae agua intracelular, con disfunción del '
           'sensorio. Las neuronas desarrollan con el tiempo osmolitos adaptativos (ampliación bibliográfica), lo que explica el '
           'riesgo de la diapositiva siguiente.')


def tonicity3(D):
    s = new(D, U, 'Tonicidad · 3 · corrección brusca: riesgo de edema', 'blue', morph=True)
    neuron_scene(s, 2, 'TONICIDAD CORREGIDA DEMASIADO RÁPIDO')
    t = tbox(s, 7.3, 1.15, 5.65, 3.4, '- Si glucosa y osmolalidad descienden **bruscamente**, el agua **reingresa** a células adaptadas al medio hipertónico.\n'
             '- Gradientes osmóticos peligrosos → **complicaciones neurológicas** (edema).', 15, head='Riesgo de corrección')
    p = pearl(s, 7.3, 4.8, 5.65, 1.4, 'En el EHH importa una corrección **controlada** de osmolalidad y glucosa, con monitoreo seriado.', 15)
    s.step(fade(t)); s.step(zoom(p))
    s.note('Tonicidad, paso 3. Si la tonicidad se corrige excesivamente rápido, el agua reingresa a células que se habían adaptado y '
           'aparecen gradientes osmóticos peligrosos (Morph: la neurona se hincha). Por eso en el EHH importa una corrección '
           'controlada de osmolalidad y glucosa [C24]. El tamaño de la célula es una representación didáctica.')


def osmol(D):
    s = new(D, U, 'Osmolalidad total frente a efectiva (tonicidad)', 'peachW')
    f1 = formula(s, 0.4, 1.2, 7.2, 0.8, 'Osm total ≈ 2 × Na⁺ + glucosa/18 + BUN/2,8', 20)
    f2 = formula(s, 0.4, 2.2, 7.2, 0.8, 'Osm efectiva ≈ 2 × Na⁺ + glucosa/18', 20, fill=BOX, color=BOXT)
    u = tbox(s, 7.9, 1.2, 5.05, 1.8, '- Na⁺ en **mmol/L** (×2 por sus aniones acompañantes).\n- Glucosa y BUN en **mg/dL**: /18 y /2,8 convierten a mmol/L.', 14, head='Unidades')
    urea = s.group_start('Urea membrana')
    s.shape(0.4, 3.3, 7.2, 2.15, 'rect', WHITE, (INK, 1.5), SHD)
    membrane_v(s, 3.85, 3.75, 1.15, name='Membrana urea')
    lab(s, 0.5, 3.35, 3.0, 0.35, 'EXTRACELULAR', 12); lab(s, 4.3, 3.35, 3.0, 0.35, 'INTRACELULAR', 12)
    mol(s, 1.0, 3.95, 'urea', d=0.55, name='Urea 1'); mol(s, 2.3, 4.2, 'urea', d=0.55, name='Urea 2')
    mol(s, 5.0, 4.2, 'urea', d=0.55, name='Urea 3'); mol(s, 6.3, 4.3, 'urea', d=0.55, name='Urea 4')
    s.arrow([(2.9, 4.0), (4.9, 4.0)], TRN, 3, head='triangle')
    s.text(0.5, 5.0, 7.0, 0.4, 'La urea atraviesa membranas: suma osmoles, **no** genera gradiente sostenido', 13, F_BODY, INK, False, 'c', 'm')
    s.group_end()
    c = tbox(s, 7.9, 3.3, 5.05, 2.15, 'Faltan **Na⁺ y BUN**: no puede verificarse el cálculo ni saberse cuánto de **325** corresponde a solutos efectivos.', 15, head='Caso 12')
    p = pearl(s, 0.4, 5.7, 12.55, 1.15, 'Para inferir **riesgo neurológico** y movimientos de agua celular se usa la **osmolalidad efectiva**; total y efectiva **no deben intercambiarse**.', 15)
    s.step(fade(f1)); s.step(fade(f2)); s.step(fade(u)); s.step(fade(urea)); s.step(fade(c)); s.step(zoom(p))
    s.note('Osmolalidad total aproximada (glucosa y BUN en mg/dL, Na⁺ en mmol/L): 2 × Na⁺ + glucosa/18 + BUN/2,8. Osmolalidad '
           'efectiva o tonicidad: 2 × Na⁺ + glucosa/18; la urea no contribuye sostenidamente a la tonicidad porque atraviesa las '
           'membranas. En este caso faltan Na⁺ y BUN: no puede verificarse el cálculo ni establecerse cuánta de la osmolalidad 325 '
           'corresponde a solutos efectivos. Distinguir ambas magnitudes es esencial para inferir riesgo neurológico. Ejercicio 6.')


def na_corr(D):
    s = new(D, U, 'Sodio corregido por hiperglucemia', 'greenR')
    f = formula(s, 0.4, 1.2, 12.55, 0.85, 'Na⁺ corregido ≈ Na⁺ medido + factor × (glucosa − 100) / 100', 21)
    m = tbox(s, 0.4, 2.3, 5.6, 2.3, 'La glucosa extracelular **atrae agua** desde las células y **diluye** el Na⁺ medido. El Na⁺ corregido estima el sodio que habría sin ese desplazamiento de agua.', 15, head='Por qué se corrige')
    c1 = s.group_start('Factor 1,6')
    formula(s, 6.3, 2.3, 6.65, 0.6, 'Factor 1,6: 1,6 × (683 − 100)/100', 16, fill='FFF2CC')
    formula(s, 6.3, 3.0, 6.65, 0.6, '= 1,6 × 5,83 ≈ + 9,3 mEq/L', 18, fill=BOX, color=BOXT)
    s.group_end()
    c2 = s.group_start('Factor 2,4')
    formula(s, 6.3, 3.85, 6.65, 0.6, 'Factor 2,4 (hiperglucemia grave): 2,4 × 5,83', 16, fill='FFF2CC')
    formula(s, 6.3, 4.55, 6.65, 0.6, '≈ + 14,0 mEq/L', 18, fill=BOX, color=BOXT)
    s.group_end()
    p = pearl(s, 0.4, 5.5, 12.55, 1.35, '**No se puede calcular el sodio final**: el caso 12 no informa Na⁺ medido. Sólo se conoce la magnitud de la **corrección** (+9,3 a +14,0 mEq/L).', 16)
    s.step(fade(m)); s.step(fade(c1)); s.step(fade(c2)); s.step(zoom(p))
    s.note('Sodio corregido por hiperglucemia: Na corregido ≈ Na medido + 1,6 × [(glucosa − 100)/100]; en algunas situaciones de '
           'hiperglucemia grave se emplea un factor cercano a 2,4. Con glucemia 683: (683 − 100)/100 = 5,83; × 1,6 = +9,3 mEq/L; × '
           '2,4 = +14,0 mEq/L. No puede calcularse el sodio final sin el Na medido. La corrección se debe a la transferencia osmótica '
           'de agua al espacio extracelular.')


def diag5(D):
    s = new(D, U, 'Pregunta 5 · diagnóstico presuntivo y causas', 'cyan')
    d = mbox(s, 0.4, 1.2, 12.55, 0.85, 'EHH CON DESHIDRATACIÓN GRAVE Y COMPROMISO DE CONCIENCIA — PROBABLE DM2 HASTA DEMOSTRAR LO CONTRARIO', 'y', 16)
    sup = tbox(s, 0.4, 2.3, 6.1, 2.6, '- Glucosa ≥ 600\n- Osmolalidad informada 325\n- Cetonas no detectadas\n- pH conservado\n- Glucosuria e hipovolemia intensa', 15, head='Lo sostienen')
    cau = tbox(s, 6.85, 2.3, 6.1, 2.6, 'El **despido y el estrés** pueden contribuir (ejes neuroendocrinos, conducta), pero **no reemplazan** la búsqueda de **infección, infarto, ACV, fármacos, interrupción terapéutica** o enfermedad intercurrente.', 14.5, head='Precipitante no demostrado')
    p = pearl(s, 0.4, 5.15, 12.55, 1.7, '**Glasgow 7**: asegurar evaluación de **vía aérea y ventilación** y buscar causas alternativas de coma (meningitis, ACV, intoxicación, hipoglucemia concomitante). No atribuir automáticamente el coma al EHH.', 15)
    s.step(zoom(d)); s.step(fade(sup)); s.step(fade(cau)); s.step(zoom(p))
    s.note('Pregunta 5. Diagnóstico presuntivo: estado hiperglucémico hiperosmolar con deshidratación grave y compromiso de '
           'conciencia, probablemente por DM2 hasta demostrar lo contrario. Lo sostienen glucosa ≥600, osmolalidad 325, ausencia de '
           'cetonas detectadas, pH conservado, glucosuria y signos intensos de hipovolemia. La causa precipitante no está '
           'demostrada: el despido y el estrés pueden contribuir, pero no reemplazan la búsqueda de infección, infarto, ACV, '
           'fármacos, interrupción terapéutica o enfermedad intercurrente. Con Glasgow 7 se asegura vía aérea y ventilación y se '
           'consideran causas alternativas de coma.')


def pathways(D):
    s = new(D, U, 'Pregunta 6 · vías metabólicas alteradas en el EHH', 'peachW')
    items = [('Resistencia hepática', 'FOXO1/PEPCK/G6PC mal suprimidos → producción hepática de glucosa alta', 'healthy_liver'),
             ('Resistencia muscular', 'Menor señal IRS–PI3K–Akt–GLUT4 → menor captación', 'muscle-fiber'),
             ('Secreción β insuficiente', 'Gluco/lipotoxicidad, disfunción mitocondrial, genética', 'langerhans-islet-pancreas'),
             ('Lipólisis/cetogénesis frenadas', 'La insulina residual mantiene efecto anticetogénico', 'adipocyte-1'),
             ('Riñón', 'Glucosuria, diuresis osmótica, pérdida de electrolitos, FG ↓', 'kidney-1'),
             ('Neurofisiología osmótica', 'Salida de agua intracelular → disfunción del sensorio', 'brain-2'),
             ('Catabolismo proteico y estrés', 'Más aminoácidos gluconeogénicos; menor intensidad cetogénica que la CAD', 'muscle-1')]
    ids = []
    for i, (h, t, img) in enumerate(items):
        col = i % 2; row = i // 2
        x = 0.4 + col * 6.35; y = 1.15 + row * 1.42
        if i == 6:
            x = 3.55
        g = s.group_start('Vía EHH %d' % i)
        s.shape(x, y, 6.15, 1.28, 'rect', WHITE, (INK, 1.5), SHD)
        fitpic(s, img, x + 0.1, y + 0.1, 1.05, 1.05)
        s.text(x + 1.3, y + 0.08, 4.75, 0.42, '%d · %s' % (i + 1, h), 15, F_HEAD, BOXT, True, 'l', 'm')
        s.text(x + 1.3, y + 0.52, 4.75, 0.7, t, 13.5, F_BODY, INK, False, 'l', 't')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Pregunta 6. 1) Resistencia hepática a la insulina: no se suprimen bien FOXO1/PEPCK/G6PC y persisten gluconeogénesis y '
           'glucogenólisis. 2) Resistencia muscular: menor señal IRS–PI3K–Akt–GLUT4. 3) Alteración de la secreción β: la demanda '
           'compensatoria supera la capacidad pancreática (glucotoxicidad, lipotoxicidad, disfunción mitocondrial, predisposición '
           'genética). 4) Lipólisis y cetogénesis relativamente frenadas por la insulina residual. 5) Metabolismo renal alterado. '
           '6) Neurofisiología osmótica. 7) Catabolismo proteico y respuesta de estrés, con menor intensidad cetogénica que la CAD '
           'típica. Diferencia central: la DM2 descompensada no es ausencia completa de insulina sino secreción insuficiente para '
           'vencer la resistencia.')


def therapy(D):
    s = new(D, U, 'Abordaje del EHH y riesgos de la corrección', 'blue')
    ax = [('VÍA AÉREA', 'y causas de coma'), ('LÍQUIDOS IV', 'perfusión, FG, glucosuria'), ('K⁺ / ELECTROLITOS', 'antes y durante'),
          ('INSULINA', 'en contexto apropiado'), ('PRECIPITANTE', 'buscar y tratar')]
    ids = []
    for i, (h, t) in enumerate(ax):
        x = 0.4 + i * 2.53
        g = s.group_start('Eje ' + h)
        mbox(s, x, 1.2, 2.4, 0.55, h, 'y', 14)
        tbox(s, x, 1.82, 2.4, 0.75, t, 13.5, anchor='m')
        ids.append(s.group_end())
    f = tbox(s, 0.4, 2.85, 6.15, 2.0, 'Los **líquidos** solos pueden reducir la glucosa por **dilución**, mejor **FG** y glucosuria, sin necesidad inmediata de dosis elevadas de insulina.', 15, head='Efecto de la rehidratación')
    m = tbox(s, 6.8, 2.85, 6.15, 2.0, 'Monitorizar **Na⁺ medido/corregido, osmolalidad, glucosa, K⁺, función renal y diuresis**; ajustar líquidos a comorbilidades **cardíacas y renales**.', 15, head='Monitoreo')
    r = s.group_start('Seguridad')
    for i, t in enumerate(['Insulina con K⁺ muy bajo → K⁺ entra a la célula → **arritmias**',
                           'Tonicidad corregida muy rápido → **gradientes osmóticos** peligrosos',
                           'Coma atribuido automáticamente al EHH → se omiten **meningitis, ACV, intoxicación, hipoglucemia**']):
        pearl(s, 0.4 + i * 4.2, 5.1, 4.0, 1.75, t, 13.5, name='Riesgo %d' % i)
    s.group_end()
    for g in ids:
        s.step(fade(g))
    s.step(fade(f)); s.step(fade(m)); s.step(fade(r))
    s.note('Abordaje conceptual del EHH: evaluar vía aérea y causas de coma, líquidos IV, potasio y electrolitos, insulina en '
           'contexto apropiado y tratamiento de la causa precipitante. La recuperación de la perfusión por líquidos puede reducir la '
           'glucosa por dilución, mejor filtrado y glucosuria. Importa una corrección controlada de osmolalidad y glucosa. Los '
           'déficits totales de potasio pueden ser importantes aun con kalemia normal. Razonamiento de seguridad: insulina con '
           'hipopotasemia → arritmias; corrección rápida de tonicidad → gradientes osmóticos; atribuir el coma al EHH → omitir '
           'diagnósticos alternativos [C24, ADA26]. Contenido formativo: no reemplaza protocolos.')


def diet(D):
    s = new(D, U, 'Pregunta 7 · objetivo de la dieta hipocalórica equilibrada', 'cyan')
    s.pic('digestive-system', 0.4, 1.15, h=5.7, name='Aparato digestivo')
    nodes = {
        'd': (2.4, 1.3, 3.5, 0.7, 'Déficit energético sostenible', 'y', 15),
        'v': (6.4, 1.3, 3.1, 0.6, 'Grasa visceral y hepática ↓', 'Y', 13.5),
        's': (6.4, 2.1, 3.1, 0.6, 'Sensibilidad insulínica ↑', 'Y', 13.5),
        'b': (6.4, 2.9, 3.1, 0.6, 'Demanda pancreática ↓', 'Y', 13.5),
        'p': (9.85, 1.3, 3.1, 0.6, 'Presión arterial ↓', 'Y', 13.5),
        't': (9.85, 2.1, 3.1, 0.6, 'Triglicéridos ↓', 'Y', 13.5),
        'i': (9.85, 2.9, 3.1, 0.6, 'Inflamación ↓', 'Y', 13.5),
    }
    edges = [('d', 'v'), ('d', 's', {'pts': [(5.95, 1.8), (6.35, 2.35)]}), ('d', 'b', {'pts': [(5.95, 1.9), (6.35, 3.15)]})]
    graph(s, nodes, edges, [['d'], ['d>v', 'v', 'd>s', 's', 'd>b', 'b'], ['p', 't', 'i']])
    q = tbox(s, 2.4, 3.8, 5.2, 3.05, '«Hipocalórica» **no** significa insuficiente: proteína adecuada, grasas saludables, **fibra**, vitaminas y minerales, patrón adaptable a **preferencias y recursos**, conservando **masa magra**.', 14.5, head='Calidad nutricional')
    w = pearl(s, 7.85, 3.8, 5.1, 3.05, 'Con hiperglucemia reciente y fármacos asociados a **hipoglucemia** (sulfonilureas), los cambios de ingesta exigen **ajustar el tratamiento**.', 15)
    s.step(fade(q)); s.step(zoom(w))
    s.note('Pregunta 7 del caso 12. La dieta hipocalórica equilibrada busca crear un déficit energético sostenible, reducir grasa '
           'visceral y hepática, mejorar la sensibilidad insulínica, disminuir los requerimientos pancreáticos, la presión, los '
           'triglicéridos y la inflamación, mientras conserva masa magra y evita carencias. Debe ofrecer proteína, grasas saludables, '
           'fibra, vitaminas y minerales y adaptarse a preferencias y recursos. Con fármacos asociados a hipoglucemia los cambios de '
           'ingesta exigen ajustar el tratamiento.')


def gliben(D):
    s = new(D, U, 'Pregunta 8 · glibenclamida: mecanismo y pertinencia', 'peachW')
    nodes = {
        'g': (0.4, 1.3, 2.8, 0.65, 'Glibenclamida', 's', 17),
        'su': (3.7, 1.3, 2.6, 0.65, 'SUR1 del K_{ATP}', 'g', 15),
        'c': (6.8, 1.3, 2.6, 0.65, 'Cierre del canal', 'Y', 15),
        'dp': (9.9, 1.3, 3.05, 0.65, 'Despolarización · Ca²⁺ ↑', 'Y', 14),
        'i': (9.9, 2.35, 3.05, 0.7, 'Secreción de insulina endógena', 'y', 14),
    }
    edges = [('g', 'su'), ('su', 'c'), ('c', 'dp'), ('dp', 'i')]
    graph(s, nodes, edges, [['g', 'g>su', 'su', 'su>c', 'c', 'c>dp', 'dp', 'dp>i', 'i']])
    cols = [('REQUISITO', 'Reserva funcional de células β. No corrige por sí misma la resistencia.', 'g'),
            ('RIESGOS', '**Hipoglucemia** (a veces prolongada: mayores, insuficiencia renal, ingesta irregular) y **aumento de peso**.', 'r'),
            ('¿Y EN DM1?', 'Con déficit absoluto **no hay secreción β que estimular**: la DM1 requiere **insulina exógena**.', 's')]
    ids = []
    for i, (h, t, k) in enumerate(cols):
        x = 0.4 + i * 4.2
        g = s.group_start('Col ' + h)
        mbox(s, x, 3.35, 4.0, 0.55, h, k, 15)
        tbox(s, x, 3.98, 4.0, 1.4, t, 14, anchor='m')
        ids.append(s.group_end())
    p = tbox(s, 0.4, 5.6, 12.55, 1.3, 'Glibenclamida 5 mg/día es la conducta **del caso docente**, no la opción preferente universal. Hoy se individualiza priorizando **peso, riesgo CV/renal, hipoglucemia, función renal, disponibilidad y costo** (metformina, GLP-1 o GIP/GLP-1, iSGLT2, otras).', 14, head='Actualización')
    for g in ids:
        s.step(fade(g))
    s.step(fade(p))
    s.note('Pregunta 8. La glibenclamida (glyburide) es una sulfonilurea: se une a la subunidad SUR1 del canal K_ATP β-pancreático, '
           'favorece su cierre independientemente de la glucosa, despolariza la membrana, abre canales de Ca²⁺ y estimula la '
           'secreción de insulina endógena. Puede reducir la glucemia en la DM2 si existe reserva β; no corrige la resistencia y '
           'puede provocar hipoglucemia (a veces prolongada, sobre todo en personas mayores, insuficiencia renal o ingesta irregular) '
           'y aumento de peso. En la DM1 con déficit absoluto no es útil: requiere insulina exógena. Indicar glibenclamida 5 mg/día '
           'es la conducta del caso docente; hoy la elección después de un EHH requiere evaluación integral [ADA26].')


def exercise_q9(D):
    s = new(D, U, 'Pregunta 9 · ¿por qué actividad física moderada?', 'greenR')
    s.pic('cyclist', 0.4, 1.2, 3.6, name='Ciclista') if False else s.pic('runner', 0.6, 1.15, h=4.6, name='Corredor q9')
    st = steps_panel(s, 3.6, 1.2, 9.35, ['Contracción → **AMPK, CaMK** y señales mecánicas → **GLUT4** aun con baja señal insulínica → glucemia ↓.',
                                         'Sostenido: **sensibilidad insulínica** y capacidad **mitocondrial** ↑.',
                                         '**Fuerza**: preserva masa magra y depósito de glucógeno · **aeróbico**: capacidad oxidativa, función endotelial, gasto.',
                                         'Beneficios en **TA, adiposidad visceral, sueño y ánimo**.'], 15)
    p = pearl(s, 3.6, 5.6, 9.35, 1.25, 'Plan **progresivo, sostenible y seguro** (evaluar riesgo CV, neuropatía, retinopatía, pies, hipoglucemia). **Nunca** se inicia ejercicio durante una crisis hiperglucémica descompensada.', 14.5)
    s.step(zoom(p))
    s.note('Pregunta 9. La contracción muscular activa AMPK, CaMK y señales mecánicas que aumentan el transporte de GLUT4 aun con baja '
           'señal insulínica: cae la glucemia y, sostenidamente, mejoran la sensibilidad a la insulina y la capacidad mitocondrial. '
           'El entrenamiento de fuerza preserva masa magra y el depósito de glucosa como glucógeno; el aeróbico incrementa la '
           'capacidad oxidativa, la función endotelial y el gasto energético. Se añaden beneficios sobre TA, adiposidad visceral, '
           'sueño y estado de ánimo. El plan debe ser progresivo y seguro, y nunca se inicia en una crisis descompensada.')


def build(D):
    div(D)
    case(D)
    labs(D)
    no_ketones(D)
    example4(D)
    ph_normal(D)
    dehydration(D)
    tonicity(D)
    tonicity2(D)
    tonicity3(D)
    osmol(D)
    na_corr(D)
    diag5(D)
    pathways(D)
    therapy(D)
    diet(D)
    gliben(D)
    exercise_q9(D)
