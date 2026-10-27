# -*- coding: utf-8 -*-
"""UNIDAD II (a) — Caso 11: presentación, datos, vías alteradas, Mapa 3 y Secuencia C (Morph) de la cetogénesis"""
from base import *

U = 2


def div(D):
    def art(s):
        s.pic('healthy-lung', 10.65, 0.5, 2.5, name='Pulmón')
        model(s, 'bhb', 10.9, 3.6, 2.0, name='β-OHB 3D')
        model(s, 'acetoacetato', 0.2, 1.3, 2.2, name='AcAc 3D', label='Acetoacetato')
        s.pic('adipocyte-1', 0.1, 4.9, 2.2, name='Adipocitos')
    divider(D, U, 'II', 'CASO 11: CETOACIDOSIS\nDIABÉTICA Y NEUMONÍA', 'Insulinopenia + estrés infeccioso = catabolismo extremo',
            ['Presentación y datos del caso', 'Vías metabólicas en insulinopenia', 'Secuencia C: de la lipólisis a la acidemia',
             'Riñón: SGLT2, glucosuria y diuresis osmótica', 'Potasio, infección y circuito integrado', 'Verificación de la gasometría',
             'Evolución a 24 h y tratamiento conceptual'], art,
            'Unidad II. Caso clínico 11: persona de 24 años con DM1 y neumonía neumocócica que desarrolla cetoacidosis diabética. '
            'Se integran los mecanismos de insulinopenia, cetogénesis, equilibrio ácido-base, riñón, potasio y respuesta al estrés, '
            'con una verificación crítica de la gasometría informada.')


def case(D):
    s = new(D, U, 'Caso 11 · presentación clínica', 'peach')
    s.pic('patient', 0.5, 1.15, h=5.7, name='Paciente caso 11')
    s.pic('healthy-lung', 2.6, 1.3, 2.6, name='Pulmón caso 11')
    cons = s.shape(4.1, 2.9, 0.85, 0.75, 'ellipse', ('a', 'FFFFFF', 55), ('C00000', 3), False, name='Consolidación basal derecha')
    lab(s, 2.45, 4.0, 3.0, 0.6, 'Consolidación basal\nderecha (Rx)', 12.5, INH)
    data = [('PERSONA DE 24 AÑOS CON DM1', 'NPH **35 UI** matinales y **10 UI** nocturnas · HbA1c **12 %**', 'y'),
            ('SÍNTOMAS', 'Náuseas, vómitos, tos productiva, **fiebre 38,7 °C**', 's'),
            ('SIGNOS', '**Hipotensión** 90/50 · **taquicardia** 120 · **taquipnea** 32 · somnolencia y desorientación', 'r'),
            ('MICROBIOLOGÍA', 'Hemocultivos positivos para **neumococo** (*Streptococcus pneumoniae*)', 'g')]
    ids = []
    for i, (h, t, k) in enumerate(data):
        y = 1.2 + i * 1.42
        g = s.group_start('Dato ' + h)
        mbox(s, 5.6, y, 7.3, 0.48, h, k, 14)
        tbox(s, 5.6, y + 0.52, 7.3, 0.75, t.replace('*Streptococcus pneumoniae*', 'Streptococcus pneumoniae'), 15, anchor='m')
        ids.append(s.group_end())
    s.step(zoom(cons))
    for g in ids:
        s.step(fade(g))
    s.note('Caso 11. Persona de 24 años con DM1 tratada con insulina NPH 35 UI por la mañana y 10 UI por la noche, HbA1c 12 %. '
           'Consulta por náuseas, vómitos, tos productiva y fiebre; presenta hipotensión, taquicardia, taquipnea, somnolencia y '
           'desorientación. La radiografía muestra consolidación basal derecha y luego los hemocultivos resultan positivos para '
           'neumococo. La pregunta conductora: ¿cómo una infección transforma la falta de insulina en una emergencia metabólica?')


def labs(D):
    s = new(D, U, 'Caso 11 · laboratorio al ingreso', 'cyanR')
    rows = [['Variable', 'Resultado', 'Lectura inicial'],
            ['Glucosa', '390 mg/dL', 'Hiperglucemia marcada'],
            ['pH', '7,15', 'Acidemia'],
            ['HCO₃⁻', '13 mEq/L', 'Disminuido: componente metabólico ácido'],
            ['pCO₂', '24 mmHg', 'Hipocapnia: hiperventilación'],
            ['Cetonemia', '+++', 'Producción importante de cuerpos cetónicos, no cuantificada'],
            ['Cetonuria', '+', 'Excreción de cetonas'],
            ['Base excess', '−8', 'Déficit de base: acidosis metabólica'],
            ['Leucocitos', '15.000/mm³', 'Leucocitosis: inflamación/infección probable'],
            ['TA / FC / FR', '90/50 · 120 · 32', 'Hipovolemia/hipoperfusión, estrés y compensación ventilatoria'],
            ['Temperatura', '38,7 °C', 'Síndrome febril con neumonía']]
    table(s, 0.4, 1.15, 8.3, rows, [1.6, 1.8, 4.9], size=13, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla caso 11', heights=[0.44] * 11)
    hl = s.shape(0.36, 1.98, 8.38, 1.36, 'rect', None, ('C00000', 4.0), False, name='Marco tríada')
    al = pearl(s, 9.0, 1.2, 3.95, 2.3, '**Alerta de calidad analítica**: el trío pH 7,15 – HCO₃⁻ 13 – pCO₂ 24 **no es internamente consistente**. Se verifica más adelante con Henderson–Hasselbalch.', 14.5)
    fal = tbox(s, 9.0, 3.75, 3.95, 3.15, '- Na⁺, K⁺, Cl⁻ · urea · creatinina\n- Mg²⁺ · fósforo · lactato\n- **β-hidroxibutirato** cuantitativo\n- Osmolalidad · anion gap\n- ECG · diuresis · cultivos', 14.5, head='Datos no aportados')
    s.step(zoom(hl), fade(al, after=True))
    s.step(fade(fal))
    s.note('Datos al ingreso y su lectura inicial. Glucosa 390 mg/dL; pH 7,15; HCO₃⁻ 13 mEq/L; pCO₂ 24 mmHg; cetonemia +++ (no '
           'cuantificada); cetonuria +; exceso de base −8; leucocitos 15.000/mm³; TA 90/50, FC 120, FR 32; temperatura 38,7 °C. '
           'El marco rojo resalta la tríada gasométrica, que no es internamente consistente: se analizará con Henderson–Hasselbalch '
           'y sin forzar conclusiones. Faltan pruebas esenciales: electrolitos (Na, K, Cl), urea, creatinina, magnesio, fósforo, '
           'lactato, β-hidroxibutirato cuantitativo, osmolalidad, anion gap, ECG, diuresis y cultivos según criterio clínico. No se '
           'deben inventar los valores ausentes.')


def glucose390(D):
    s = new(D, U, 'Pregunta 1a · ¿qué significa una glucemia de 390 mg/dL?', 'pink')
    nodes = {
        'ins': (0.5, 1.3, 3.3, 0.6, 'Insulinopenia (DM1)', 's', 15),
        'st': (0.5, 2.4, 3.3, 0.85, 'Estrés: catecolaminas · cortisol\nglucagón · citocinas', 's', 13),
        'phg': (4.6, 1.3, 3.6, 0.6, 'Producción hepática de glucosa ↑', 'Y', 14),
        'cap': (4.6, 2.55, 3.6, 0.6, 'Captación periférica ↓ (GLUT4)', 'Y', 14),
        'g': (9.0, 1.85, 3.9, 0.9, 'GLUCEMIA 390 mg/dL', 'y', 20),
    }
    edges = [('ins', 'phg'), ('ins', 'cap', {'pts': [(3.85, 1.75), (4.55, 2.75)]}), ('st', 'phg', {'pts': [(3.85, 2.65), (4.55, 1.75)]}), ('st', 'cap'),
             ('phg', 'g'), ('cap', 'g')]
    graph(s, nodes, edges, [['ins', 'st'], ['ins>phg', 'st>phg', 'phg', 'ins>cap', 'st>cap', 'cap'], ['phg>g', 'cap>g', 'g']])
    t1 = tbox(s, 0.5, 3.75, 6.1, 2.25, 'La glucosa **por sí sola no determina la gravedad** de la CAD: son imprescindibles **pH, β-hidroxibutirato, bicarbonato, osmolalidad, hidratación y estado de conciencia**.', 15.5, head='Gravedad')
    t2 = tbox(s, 6.85, 3.75, 6.05, 2.25, 'Puede existir **CAD euglucémica**: por ejemplo con **inhibidores SGLT2** o en el **embarazo**. Glucemia «no tan alta» no descarta cetoacidosis.', 15.5, head='CAD euglucémica')
    s.step(fade(t1)); s.step(fade(t2))
    s.note('Pregunta 1a. 390 mg/dL es una hiperglucemia grave para una persona con DM1 y síntomas de descompensación. Refleja la '
           'combinación de mayor producción hepática de glucosa (glucogenólisis y gluconeogénesis) y menor captación periférica '
           'dependiente de insulina, exacerbada por catecolaminas, cortisol, citocinas y glucagón ante la neumonía. La glucosa no '
           'determina por sí sola la gravedad: deben valorarse pH, β-hidroxibutirato, bicarbonato, osmolalidad, hidratación y '
           'estado de conciencia. Existe CAD euglucémica, por ejemplo con inhibidores SGLT2 o en el embarazo [consenso 2024].')


def pathways(D):
    s = new(D, U, 'Pregunta 3 · vías comprometidas por la insulinopenia', 'green')
    c = mbox(s, 4.4, 1.15, 4.5, 0.65, 'INSULINOPENIA', 'y', 22)
    items = [('Captación de glucosa ↓', 'GLUT4 muscular/adiposo en membrana ↓ → glucemia ↑', 'muscle-fiber'),
             ('Producción hepática de glucosa ↑', 'Glucogenólisis y gluconeogénesis (lactato, alanina, glicerol)', 'healthy_liver'),
             ('Lipólisis ↑', 'Catecolaminas/PKA, perilipina, ATGL y HSL → AGNE y glicerol', 'adipocyte-1'),
             ('β-oxidación ↑', 'CPT1 menos restringida por malonil-CoA; alto flujo de AGNE', 'mitochondrium-1'),
             ('Cetogénesis ↑', 'HMGCS2 → acetoacetato y β-hidroxibutirato', None),
             ('Lipogénesis y esterificación ↓', 'Se pierde la señal anabólica; distribución de TAG alterada', None),
             ('Proteólisis ↑', 'Aminoácidos para gluconeogénesis; pérdida de masa muscular', 'muscle-1'),
             ('Glucogenosíntesis ↓', 'La glucosa no se deposita eficientemente', None),
             ('Balance hidroelectrolítico alterado', 'Glucosuria, natriuresis y kaliuresis', 'kidney-1')]
    ids = []
    for i, (h, t, img) in enumerate(items):
        col = i % 3; row = i // 3
        x = 0.4 + col * 4.2; y = 2.05 + row * 1.65
        g = s.group_start('Vía %d' % (i + 1))
        s.shape(x, y, 4.0, 1.5, 'rect', WHITE, (INK, 1.5), SHD)
        s.shape(x + 0.08, y + 0.08, 0.42, 0.42, 'ellipse', BOX, (INK, 1.2), False, str(i + 1), 13, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
        s.text(x + 0.6, y + 0.05, 3.3, 0.5, h, 14.5, F_HEAD, BOXT, True, 'l', 'm')
        s.text(x + 0.15, y + 0.6, 2.85 if img else 3.7, 0.85, t, 13, F_BODY, INK, False, 'l', 't')
        if img:
            fitpic(s, img, x + 3.05, y + 0.6, 0.85, 0.82)
        ids.append(s.group_end())
    s.step(zoom(c))
    s.step(*[fade(g, after=i > 0, dur=300) for i, g in enumerate(ids[:3])])
    s.step(*[fade(g, after=i > 0, dur=300) for i, g in enumerate(ids[3:6])])
    s.step(*[fade(g, after=i > 0, dur=300) for i, g in enumerate(ids[6:])])
    s.note('Pregunta 3. Vías comprometidas por la insulinopenia: 1) captación de glucosa disminuida por menos GLUT4 en membrana; '
           '2) producción hepática de glucosa aumentada (glucogenólisis y gluconeogénesis con lactato, alanina y glicerol); 3) '
           'lipólisis aumentada (catecolaminas/PKA, perilipina, ATGL y HSL liberan AGNE y glicerol); 4) β-oxidación aumentada '
           '(CPT1 menos restringida por malonil-CoA y alto flujo de AGNE); 5) cetogénesis aumentada (HMGCS2); 6) lipogénesis y '
           'esterificación disminuidas; 7) proteólisis aumentada; 8) glucogenosíntesis disminuida; 9) balance hidroelectrolítico '
           'alterado (glucosuria, natriuresis y kaliuresis). Se revelan en tres bloques: glucosa, lípidos y consecuencias.')


ORG3 = [('pancreas', 4.75, 1.05, 2.3, 'PÁNCREAS', 5.25, 2.0),
        ('healthy_liver', 0.4, 3.0, 2.5, 'HÍGADO', 0.85, 4.85),
        ('adipocyte-1', 10.9, 1.05, 1.8, 'ADIPOSO', 11.0, 2.9),
        ('muscle-fiber', 10.5, 3.6, 2.4, 'MÚSCULO', 11.0, 4.75),
        ('kidney-1', 5.25, 4.3, 0.85, 'RIÑÓN', 5.15, 5.85),
        ('healthy-lung', 0.55, 0.95, 1.6, 'PULMÓN', 0.6, 2.45)]


def map3(D):
    stages = [
        [('b', 7.4, 1.25, 3.2, 0.55, 'INSULINA ≈ 0 · glucagón ↑ · estrés ↑', 'y', 12),
         ('a', [(10.85, 1.8), (2.95, 3.35)], 'AGNE · glicerol', TRN, (6.0, 2.25), 'dash'),
         ('a', [(10.45, 4.2), (2.95, 3.9)], 'alanina', TRN, (6.9, 3.65), 'dash'),
         ('t', 3.1, 3.05, 2.0, 0.75, 'Glucosa ↑↑ · cetonas ↑↑', 12.5)],
        [('a', [(2.9, 4.2), (5.2, 4.75)], 'glucosa · cetonas', INK),
         ('t', 6.35, 4.3, 3.6, 0.95, '**Glucosuria → diuresis osmótica**: pérdida de agua, Na⁺, K⁺ → hipovolemia', 12.5),
         ('t', 2.25, 1.0, 2.4, 1.0, '**Kussmaul**: CO₂ ↓ compensa la acidemia', 12.5),
         ('b', 0.4, 5.5, 4.4, 0.55, 'CETOÁCIDOS + H⁺ consumen HCO₃⁻ → ACIDEMIA', 'r', 12.5),
         ('b', 6.35, 5.45, 3.6, 0.5, 'K⁺ sale de la célula · K⁺ total ↓', 's', 12.5)],
    ]
    map_series(D, U, 'Mapa 3 · DM1 descompensada', 'blue', ORG3, stages,
               ['Mapa 3, etapa 1. Con insulina prácticamente ausente y hormonas de estrés elevadas, el tejido adiposo libera AGNE y glicerol '
                'y el músculo aminoácidos: el hígado produce glucosa y cuerpos cetónicos en exceso.',
                'Mapa 3, etapa 2. El riñón recibe una carga filtrada de glucosa que supera su reabsorción: glucosuria y diuresis osmótica con '
                'pérdida de agua, sodio y potasio (hipovolemia). Los cetoácidos consumen bicarbonato (acidemia) y el pulmón compensa con '
                'hiperventilación (Kussmaul). El potasio sale de las células aunque el total corporal disminuye.'],
               'Mapa 3 completo: insulinopenia → hiperglucemia + cetogénesis → alteraciones renales, hidroelectrolíticas y ácido-base. '
               'Los detalles moleculares de cada flecha se desarrollan en las secuencias C (cetogénesis) y D (riñón).',
               (0.4, 6.35, 12.5, 0.65, 'Insulinopenia → **hiperglucemia + cetogénesis** → riñón, agua/electrolitos y ácido-base.', 15),
               ['sustratos hacia el hígado', 'riñón, pulmón y electrolitos'])


# ---------------------------------------------------------------- Secuencia C: cetogénesis (Morph)
SC = ['Lipólisis', 'AGNE en sangre', 'Hepatocito', 'Mitocondria', 'Cetogénesis', 'Ácido-base']


def c_scene(s, k):
    """panorama común: adipocito · sangre · hepatocito/mitocondria · pulmón"""
    # adipocito con gota que se reduce
    s.shape(0.35, 1.25, 2.9, 2.9, 'ellipse', shade('F6D7B0', 0.4, 0.25), ('8C5A2B', 2.0), SHD, name='!!Adipocito C')
    d = [2.55, 2.2, 1.95, 1.8, 1.7, 1.65][k]
    off = (2.9 - d) / 2
    s.shape(0.35 + off, 1.25 + off, d, d, 'ellipse', ('rad', [(0, 'FFF8D0'), (50, 'F7DC6F'), (100, 'D4AC0D')], (35, 30)), ('B7950B', 1.25), False,
            'TAG', 16, F_HEAD, '7D6608', True, 'c', 'm', fit=False, name='!!Gota lipídica C')
    mbox(s, 0.6, 4.25, 2.4, 0.4, 'ADIPOCITO', 'y', 12.5, name='!!Rótulo adipocito C')
    # hepatocito + mitocondria grande
    s.shape(3.65, 1.15, 4.75, 3.55, 'roundRect', shade('E8A08A', 0.45, 0.25), ('8E3B2A', 2.0), SHD, adj={'adj': 20000}, name='!!Hepatocito C')
    mbox(s, 3.85, 1.3, 1.9, 0.4, 'HEPATOCITO', 'y', 12.5, name='!!Rótulo hepatocito C')
    mito(s, 4.6, 2.2, 3.55, 2.1, name='!!Mitocondria C')
    lab(s, 5.4, 4.3, 2.0, 0.3, 'MITOCONDRIA', 11.5, name='!!Rótulo mito C')
    # sangre
    vessel(s, 0.3, 5.0, 12.7, 1.15, name='!!Sangre C', rbcs=10)
    mbox(s, 0.4, 6.25, 1.4, 0.4, 'SANGRE', 'y', 12.5, name='!!Rótulo sangre C')
    # pulmón
    s.pic('healthy-lung', 10.85, 1.0, 1.9, name='!!Pulmón C')
    # progreso
    g = s.group_start('!!Progreso C')
    for i, t in enumerate(SC):
        s.shape(2.05 + i * 1.55, 6.3, 1.5, 0.42, 'rect', BOX if i == k else (WHITE if i > k else 'FFE699'), (INK, 1.0), False, t, 11.5, F_HEAD,
                BOXT if i == k else INK, True, 'c', 'm', (0.02, 0, 0.02, 0), minsize=8)
    s.group_end()


def c_panel(s, head, text):
    return tbox(s, 8.65, 3.05, 4.3, 1.85, text, 13.5, head=head, name='!!Panel C')


def seqC1(D):
    s = new(D, U, 'Secuencia C · 1 · insulinopenia y lipólisis', 'peach', morph=False)
    c_scene(s, 0)
    c_panel(s, 'Freno liberado', 'Sin insulina, **PKA** activa (catecolaminas) fosforila **perilipina 1** y **HSL**; **ATGL** (con CGI-58) inicia la hidrólisis del TAG.')
    ag = [mol(s, 1.0 + i * 0.45, 2.3 + (i % 2) * 0.35, 'ag', d=0.38, name='!!AG %d' % i) for i in range(4)]
    gl = mol(s, 2.3, 3.2, 'gly', d=0.4, name='!!Glicerol C')
    s.step(*[zoom(a, after=i > 0, dur=250) for i, a in enumerate(ag)], zoom(gl, after=True))
    s.note('Secuencia C, paso 1 (Morph a lo largo de seis diapositivas). La disminución de la señal insulínica reduce la inhibición '
           'de la lipólisis adipocitaria: la PKA (activada por catecolaminas) fosforila perilipina 1 y la lipasa sensible a hormonas, '
           'y la ATGL con su coactivador CGI-58 inicia la hidrólisis del triacilglicerol. Aparecen ácidos grasos y glicerol; en las '
           'diapositivas siguientes la gota lipídica se reduce progresivamente mientras sus productos viajan.')


def seqC2(D):
    s = new(D, U, 'Secuencia C · 2 · AGNE en circulación', 'peach', morph=True)
    c_scene(s, 1)
    c_panel(s, 'Transporte', 'Los **AGNE** viajan unidos a **albúmina**; el **glicerol**, hidrosoluble, va al hígado como sustrato **gluconeogénico**.')
    ag = [mol(s, 1.1 + i * 0.6, 5.35, 'ag', d=0.38, name='!!AG %d' % i) for i in range(4)]
    alb = [s.shape(1.0 + i * 0.6, 5.55, 0.55, 0.3, 'roundRect', 'D6EAF8', ('2E86C1', 1.0), False, 'Alb', 9, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                   name='!!Albúmina %d' % i) for i in range(4)]
    gl = mol(s, 3.6, 5.3, 'gly', d=0.4, name='!!Glicerol C')
    s.step(*[path(a, 3.0, 0.0, dur=1500, delay=i * 150) for i, a in enumerate(ag + alb)])
    s.note('Paso 2. Los ácidos grasos no esterificados salen del adipocito y circulan unidos a albúmina (fichas «Alb»); el glicerol, '
           'hidrosoluble, llega al hígado como sustrato de la gluconeogénesis. La trayectoria de movimiento muestra el flujo hacia el '
           'hígado.')


def seqC3(D):
    s = new(D, U, 'Secuencia C · 3 · entrada al hepatocito y CPT1', 'peach', morph=True)
    c_scene(s, 2)
    c_panel(s, 'Puerta abierta', 'Acil-CoA → **CPT1**: con malonil-CoA **bajo** (ACC poco activa sin insulina) la lanzadera de **carnitina** introduce los AG en la mitocondria.')
    ag = [mol(s, 4.0 + (i % 2) * 0.45, 1.85 + (i // 2) * 0.4, 'ag', d=0.38, name='!!AG %d' % i) for i in range(4)]
    cpt = mbox(s, 4.5, 2.85, 0.9, 0.42, 'CPT1', 'g', 12, name='!!CPT1')
    mal = mbox(s, 5.9, 1.55, 1.9, 0.4, 'Malonil-CoA ↓', 'w', 12, caps=False, name='!!Malonil')
    s.step(pulse(mal), pulse(cpt, after=True))
    s.step(*[path(a, 1.1 - (i % 2) * 0.3, 1.0 - (i // 2) * 0.25, dur=1200, delay=i * 200) for i, a in enumerate(ag)])
    s.note('Paso 3. Los ácidos grasos ingresan al hepatocito, se activan a acil-CoA y atraviesan la membrana mitocondrial interna '
           'mediante la lanzadera de carnitina regulada por CPT1. Sin insulina la acetil-CoA carboxilasa es poco activa y el '
           'malonil-CoA disminuye: el freno de CPT1 desaparece y la entrada a la mitocondria se acelera.')


def seqC4(D):
    s = new(D, U, 'Secuencia C · 4 · β-oxidación y acetil-CoA ↑', 'peach', morph=True)
    c_scene(s, 3)
    c_panel(s, 'Exceso de acetil-CoA', '**β-oxidación** → acetil-CoA + NADH ↑. El **oxalacetato** se desvía a **gluconeogénesis**: el ciclo de Krebs no puede absorber toda la acetil-CoA.')
    ac = [s.shape(5.0 + (i % 4) * 0.65, 2.65 + (i // 4) * 0.55, 0.6, 0.4, 'roundRect', 'B7950B', ('7D6608', 1.0), False, 'Ac-CoA', 9.5, F_HEAD, WHITE, True,
                  'c', 'm', (0, 0, 0, 0), fit=False, name='!!AcCoA %d' % i) for i in range(8)]
    oaa = mbox(s, 3.85, 3.85, 1.2, 0.4, 'OAA →', 'w', 11.5, caps=False, name='!!OAA')
    gng = mbox(s, 3.85, 1.8, 1.6, 0.4, 'Gluconeogénesis', 'Y', 11, caps=False, name='!!GNG')
    s.step(*[zoom(a, after=i > 0, dur=180) for i, a in enumerate(ac)])
    s.step(fade(oaa), path(oaa, 0.0, -1.5, dur=1000), fade(gng, after=True))
    s.note('Paso 4. En la matriz mitocondrial la β-oxidación genera acetil-CoA y NADH en exceso. La acetil-CoA activa la piruvato '
           'carboxilasa e inhibe la PDH; el oxalacetato se desvía hacia la gluconeogénesis (la ficha OAA sale de la mitocondria), de '
           'modo que disminuye el oxalacetato disponible para condensarse con acetil-CoA en el ciclo de Krebs. El excedente de '
           'acetil-CoA queda disponible para la cetogénesis.')


def seqC5(D):
    s = new(D, U, 'Secuencia C · 5 · HMGCS2 → acetoacetato → β-hidroxibutirato', 'peach', morph=True)
    c_scene(s, 4)
    c_panel(s, 'Cetogénesis', '2 Ac-CoA → acetoacetil-CoA → **HMGCS2** → HMG-CoA → liasa → **acetoacetato**. El NADH/NAD⁺ alto favorece **β-hidroxibutirato**. El hígado **no** los oxida (sin SCOT).')
    hm = mbox(s, 4.95, 3.0, 1.3, 0.42, 'HMG-CoA', 'y', 12, name='!!HMG')
    aa = model(s, 'acetoacetato', 6.55, 2.3, 1.25, name='!!AcAc 3D', label='AcAc', lsize=10)
    bh = model(s, 'bhb', 6.55, 3.25, 1.25, name='!!BHB 3D', label='β-OHB', lsize=10)
    cc = [mol(s, 4.4 + i * 0.75, 4.75, 'cc', d=0.4, name='!!CC %d' % i, text='CC') for i in range(5)]
    s.step(zoom(hm), fade(aa, after=True), fade(bh, after=True))
    s.step(*[fade(c, after=i > 0, dur=150) for i, c in enumerate(cc)])
    s.step(*[path(c, 0.4 + i * 0.3, 0.7, dur=1100, delay=i * 150) for i, c in enumerate(cc)])
    s.note('Paso 5. Dos acetil-CoA forman acetoacetil-CoA; la HMG-CoA sintasa mitocondrial (HMGCS2, enzima regulada de la vía) '
           'produce HMG-CoA y la HMG-CoA liasa libera acetoacetato. Con relación NADH/NAD⁺ elevada, la β-hidroxibutirato '
           'deshidrogenasa favorece la formación de β-hidroxibutirato. Los modelos 3D muestran ambas moléculas. Como el hepatocito '
           'carece de SCOT (OXCT1) no puede oxidarlos: los cuerpos cetónicos (CC) salen a la sangre. Cuando la producción supera el '
           'uso periférico y la eliminación aparece cetonemia; las cetonas filtradas producen cetonuria.')


def seqC6(D):
    s = new(D, U, 'Secuencia C · 6 · cetoácidos, bicarbonato y Kussmaul', 'peach', morph=True)
    c_scene(s, 5)
    c_panel(s, 'Tampón bicarbonato', 'H⁺ + HCO₃⁻ ⇌ H₂CO₃ ⇌ CO₂ + H₂O. El **HCO₃⁻ se consume**; el **CO₂** se elimina por **hiperventilación** (Kussmaul) para limitar la caída del pH.')
    cc = [mol(s, 4.8 + i * 0.75 + 0.4 + i * 0.3, 5.45, 'cc', d=0.4, name='!!CC %d' % i, text='CC') for i in range(5)]
    hp = [s.shape(4.6 + i * 1.3, 5.15, 0.36, 0.36, 'ellipse', 'C00000', (INK, 1.0), False, 'H⁺', 10, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                  name='H %d' % i) for i in range(4)]
    hc = [s.shape(4.9 + i * 1.3, 5.6, 0.62, 0.36, 'roundRect', '9DC3E6', (INK, 1.0), False, 'HCO₃⁻', 9.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                  name='HCO3 %d' % i) for i in range(4)]
    co2 = [mol(s, 9.0 + i * 0.5, 5.2, 'co2', d=0.42, name='CO2 %d' % i) for i in range(3)]
    s.step(*[zoom(h, after=i > 0, dur=200) for i, h in enumerate(hp)])
    s.step(*[out(h, dur=300) for h in hp] + [out(h, dur=300) for h in hc])
    s.step(*[fade(c, after=i > 0, dur=150) for i, c in enumerate(co2)])
    s.step(*[path(c, 2.2 - i * 0.4, -3.2, dur=1500, delay=i * 200) for i, c in enumerate(co2)])
    s.note('Paso 6. A pH fisiológico el acetoacetato y el β-hidroxibutirato circulan como aniones: su formación libera protones '
           '(fichas H⁺). El sistema tampón bicarbonato los neutraliza: H⁺ + HCO₃⁻ ⇌ H₂CO₃ ⇌ CO₂ + H₂O, de modo que el HCO₃⁻ '
           'desaparece (las fichas se desvanecen) y el CO₂ resultante se elimina por el pulmón con respiración profunda y rápida '
           '(Kussmaul). Además, la orina pierde aniones cetónicos junto con Na⁺ y K⁺ y, con ellos, potencial de regeneración de '
           'bicarbonato. La caída de bicarbonato no significa sólo «que el riñón lo elimine»: predomina una carga ácida que '
           'excede la amortiguación y la excreción renal disponibles.')


def build(D):
    div(D)
    case(D)
    labs(D)
    glucose390(D)
    pathways(D)
    map3(D)
    seqC1(D)
    seqC2(D)
    seqC3(D)
    seqC4(D)
    seqC5(D)
    seqC6(D)
