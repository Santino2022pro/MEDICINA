# -*- coding: utf-8 -*-
"""UNIDAD IX (criterios de Light), X (análisis del líquido) y XI (paraneumónico y empiema)."""
from base import *


def div9(D):
    def art(s):
        tube(s, 7.6, 1.2, 1.2, 3.8, 'F9E79F', 'Líquido pleural', 'clear', name='Arte pleural')
        tube(s, 10.4, 1.2, 1.2, 3.8, 'B03A2E', 'Sangre (suero)', 'clear', name='Arte sangre')
        s.shape(9.0, 2.6, 1.2, 0.8, 'leftRightArrow', GOLD, BORDER, False, name='Arte comparación')
    divider(D, 'IX', 'Criterios de Light', 'Comparar el líquido con la sangre',
            ['Proteínas pleurales / séricas', 'LDH pleural / sérica', 'LDH pleural frente al límite superior normal',
             'Regla de interpretación', 'Signos > y ≥: diferencias entre fuentes', 'Limitaciones y gradiente de albúmina'], art,
            src=['T4.2', 'P2.11'])


def light(D):
    s = new(D, 'Criterios de Light', 'Trasudado o exudado: los tres criterios', 'mesotelio', src=['T4.2', 'P2.11', 'T9.2'])
    t1 = tube(s, 0.4, 1.05, 0.85, 2.6, 'F9E79F', 'Líquido pleural', 'clear', name='Muestra pleural')
    t2 = tube(s, 1.85, 1.05, 0.85, 2.6, 'B03A2E', 'Sangre', 'clear', name='Muestra sangre')
    cmp_ = s.shape(0.45, 4.25, 2.35, 0.9, 'rect', GOLD, BORDER, False, 'Proteínas y LDH:\n¿cuánto pasó al líquido?', 13, F_HEAD, INK,
                   True, 'c', 'm', name='Comparación', minsize=9)
    rows = [['CRITERIO', 'FÓRMULA', 'UMBRAL', 'RESULTADO', 'INTERPRETACIÓN'],
            ['1 · Proteínas', 'Proteínas pleura / proteínas suero', '> 0,5', 'Positivo si lo supera', 'La barrera dejó pasar **proteínas**'],
            ['2 · LDH relativa', 'LDH pleura / LDH suero', '> 0,6', 'Positivo si lo supera', '**Inflamación / daño** celular local'],
            ['3 · LDH absoluta', 'LDH pleural vs. límite superior normal de LDH sérica', '> 2/3 (o ≥ 2/3)', 'Positivo si lo alcanza', 'Producción **local** de LDH']]
    ids, h = gtable(s, 3.05, 1.05, 9.95, rows, [1.15, 1.9, 0.95, 1.2, 1.75], 14, head_fill=GOLD, fill_to=5.15)
    # resaltados de umbral (columna 3)
    cw = [1.15, 1.9, 0.95, 1.2, 1.75]; tot = sum(cw)
    ux = 3.05 + 9.95 * (cw[0] + cw[1]) / tot; uw = 9.95 * cw[2] / tot
    hh = (5.15 - 1.05) / 4
    hl = [s.shape(ux, 1.05 + hh * k, uw, hh, 'rect', None, ('FF0000', 4.5), False, name='Umbral %d' % k) for k in (1, 2, 3)]
    rule = box(s, 0.45, 5.35, 8.0, 1.6, '**≥ 1 criterio positivo → EXUDADO**\n**Ningún criterio → TRASUDADO**', RED, 19, name='Regla')
    auth = box(s, 8.65, 5.35, 4.35, 1.6, 'Algunos autores exigen **dos** criterios como mínimo.', WHITE, 14, name='Dos criterios', bold=False)
    s.step(fade(t1))                                   # 1 muestra pleural
    s.step(fade(t2))                                   # 2 muestra de sangre
    s.step(zoom(cmp_), fade(ids[0], after=True))       # 3 se comparan las proteínas
    s.step(wipe(ids[1], 'l'))                          # 4 primera relación
    s.step(fade(hl[0]), pulse(hl[0], after=True))      # 5 umbral 1
    s.step(wipe(ids[2], 'l'))                          # 6 relación LDH
    s.step(fade(hl[1]), pulse(hl[1], after=True))      # 7 umbral 2
    s.step(wipe(ids[3], 'l'), fade(hl[2], after=True))  # 8 tercer criterio
    s.step(zoom(rule))                                 # 9 regla de interpretación
    s.step(fade(auth))                                 # 10 matiz del material
    s.note('El material no incluye un caso numérico resuelto: el ejemplo de aplicación se omite para no introducir datos ajenos a las '
           'fuentes. Los tres criterios comparan el líquido con el suero: si la barrera pleural está dañada, pasan proteínas y la '
           'LDH (enzima de células lesionadas) aumenta en el líquido.')
    s = new(D, 'Criterios de Light', 'Signos > y ≥: lo que dicen las fuentes', 'mesotelio', src=['T4.2', 'P2.11', 'T9.3'])
    rows = [['CRITERIO', 'FORMULACIÓN 1', 'FORMULACIÓN 2', 'ESTADO'],
            ['Proteínas pl/sér', '> 0,5 exudado · ≤ 0,5 trasudado', '> 0,5', 'Coinciden'],
            ['LDH pl/sér', '> 0,6 exudado · ≤ 0,6 trasudado', '> 0,6', 'Coinciden'],
            ['LDH absoluta', '**≥ 2/3** del límite superior normal', '**> 2/3** del límite superior normal', '**Difieren**: verificar'],
            ['Número de criterios', '≥ 1 → exudado', '1 basta; algunos autores exigen 2', 'Matiz']]
    ids, h = gtable(s, 0.4, 1.0, 12.6, rows, [1.2, 2, 2, 1.3], 15, head_fill=GOLD, fill_to=5.5,
                    col_fills=[None, None, None, 'FADBD8'])
    w = box(s, 0.4, 5.7, 12.6, 1.25, 'Hasta resolver la diferencia, la presentación muestra **ambas formulaciones** sin alterar ningún umbral.',
            RED, 16, name='Sin alterar')
    table_anim(s, ids, 1)
    s.step(fade(w))
    s = new(D, 'Criterios de Light', 'Limitaciones de la clasificación', 'torax', src=['T4.2', 'P2.11', 'P2.6'])
    cs = [box(s, 0.4, 1.0, 6.1, 2.85, 'Los criterios clasifican erróneamente ~**25 %** de los **trasudados** como exudados (falsos positivos).',
              ORANGE, 15.5, head='Falsos exudados', headfill=WHITE, bold=False),
          box(s, 6.85, 1.0, 6.15, 2.85, 'Si la **clínica** apunta a trasudado (p. ej., ICC tratada con diuréticos), solicitar el **gradiente de '
              'albúmina suero–pleura**. Su umbral no se especifica aquí.', GOLD, 15, head='Gradiente de albúmina', headfill=WHITE, bold=False),
          box(s, 0.4, 4.05, 6.1, 2.9, 'Criterios adicionales mencionados: **colesterol pleural > 45 mg/dl** y **proteínas pleurales > 3 g/dl**.',
              CEL, 15.5, head='Otros criterios', headfill=WHITE, bold=False),
          box(s, 6.85, 4.05, 6.15, 2.9, 'Buscar siempre datos que **refuten** la clasificación única. La interpretación del colesterol como dato '
              '«sistémico» que invalida el exudado se registra para **revisión**.', RED, 14.5, head='Nunca es solo uno', headfill=WHITE, bold=False)]
    reveal(s, cs, 1)


# ------------------------------------------------------------------ UNIDAD X
def div10(D):
    def art(s):
        for i, (c, k) in enumerate((('F7E7A6', 'clear'), ('B22222', 'blood'), ('F4F1E6', 'milky'), ('E2C85A', 'pus'), ('C9B07A', 'viscous'))):
            tube(s, 7.2 + i * 1.18, 1.6, 0.8, 3.4, c, None, k, name='Arte tubo %d' % i)
    divider(D, 'X', 'Análisis del líquido pleural', 'Aspecto, bioquímica, células y microbiología',
            ['Aspecto macroscópico', 'Glucosa y pH', 'ADA y linfocitos', 'Recuento celular', 'Amilasa, triglicéridos y otros marcadores',
             'Citología y microbiología'], art, src=['T4.3', 'T4.4', 'P2.12'])


def aspecto(D):
    sets = [[('F7E7A6', 'clear', 'Seroso / serohemático', 'El más frecuente; **sin significado específico** por sí solo.', C_FLUID),
             ('B22222', 'blood', 'Hemorrágico', '**Traumatismo o malignidad** (>50 % de los tumores). Pleurocrito > 50 % del Hto = **hemotórax**.', 'F1948A'),
             ('F4F1E6', 'milky', 'Lechoso', '**Quilotórax** (TG > 110 mg/dl) · pseudoquilotórax (colesterol > 200 mg/dl) · empiema.', WHITE),
             ('E2C85A', 'pus', 'Purulento', '**Empiema** (pus).', C_PUS)],
            [('1C1C1C', 'clear', 'Negro', 'Infección por **hongos** (muy infrecuente).', 'BFBFBF'),
             ('B7C24A', 'turbid', 'Amarillo verdoso', '**Artritis reumatoidea**.', 'D4E157'),
             ('C9B07A', 'viscous', 'Viscoso', '**Mesotelioma**.', LILAC)]]
    for k, items in enumerate(sets):
        s = new(D, 'Análisis del líquido', 'Aspecto macroscópico (%d/2)' % (k + 1), 'mesotelio', src=['T4.3'])
        ids = []
        n = len(items)
        cw = 12.6 / n
        for i, (c, kind, h, t, f) in enumerate(items):
            x = 0.4 + i * cw
            g = s.group_start('Aspecto ' + h)
            tube(s, x + cw / 2 - 0.5, 1.05, 1.0, 3.0, c, None, kind, name='Tubo ' + h)
            box(s, x + 0.05, 4.4, cw - 0.15, 2.0, t, f, 14, head=h, headfill=WHITE, bold=False)
            ids.append(s.group_end())
        reveal(s, ids, 1)
        if k == 1:
            w = box(s, 0.4, 6.45, 12.6, 0.55, 'El aspecto **orienta**, pero **no es un diagnóstico etiológico definitivo**: siempre confirmar con el laboratorio.',
                    RED, 14, name='No definitivo')
            s.step(zoom(w))


def gauge(s, x, y, h, lo, hi, marks, zones, title, unit, name):
    """escala vertical con zonas coloreadas y umbrales"""
    g = s.group_start(name)
    label(s, x - 0.15, y - 0.45, 1.2, 0.4, title, 14)
    for a, b, c in zones:
        ya = y + h * (1 - (b - lo) / (hi - lo)); yb = y + h * (1 - (a - lo) / (hi - lo))
        s.shape(x, ya, 0.8, yb - ya, 'rect', c, THIN, False)
    s.shape(x, y, 0.8, h, 'rect', None, BORDER, False)
    for v, t in marks:
        yy = y + h * (1 - (v - lo) / (hi - lo))
        s.arrow([(x - 0.15, yy), (x + 0.95, yy)], INK, 2.5, tail=None)
        label(s, x + 0.95, yy - 0.18, 1.3, 0.36, t, 12.5, align='l')
    label(s, x - 0.1, y + h + 0.03, 1.0, 0.3, unit, 11)
    return s.group_end()


def glucosa_ph(D):
    s = new(D, 'Análisis del líquido', 'Glucosa y pH: marcadores de consumo y de acidez local', 'rosa', src=['T4.4', 'P2.12', 'T5.1'])
    g1 = gauge(s, 0.9, 1.55, 4.9, 0, 120, [(60, '60'), (40, '40')], [(0, 40, 'E74C3C'), (40, 60, 'F5B041'), (60, 120, '82E0AA')],
               'GLUCOSA', 'mg/dl', 'Escala glucosa')
    g2 = gauge(s, 6.9, 1.55, 4.9, 6.9, 7.7, [(7.2, '7,20'), (7.5, '7,50–7,60 normal')], [(6.9, 7.2, 'E74C3C'), (7.2, 7.45, 'F9E79F'), (7.45, 7.7, '82E0AA')],
               'pH', '', 'Escala pH')
    a = box(s, 3.2, 1.0, 3.45, 5.95, '**Glucosa < 60 mg/dl**: TBC · paraneumónico complicado · tumor · pleuritis reumatoidea · hemotórax · LES.\n\n'
            '**< 40 mg/dl**: criterio citado para el **empiema**.', WHITE, 14, name='Glucosa texto', bold=False, align='l')
    b = box(s, 9.2, 1.0, 3.8, 5.95, '**pH < 7,20**: paraneumónico complicado · rotura esofágica · pleuritis reumatoidea · TBC · malignidad · '
            'hemotórax · acidosis sistémica · lupus.\n\nEn el paraneumónico, **pH < 7,2 → drenar**.', WHITE, 14, name='pH texto', bold=False, align='l')
    s.step(fade(g1))
    s.step(fade(a))
    s.step(fade(g2))
    s.step(fade(b))


def ada(D):
    s = new(D, 'Análisis del líquido', 'ADA y linfocitos: orientación hacia tuberculosis', 'rosa', src=['T4.4', 'P2.12'])
    bar = s.group_start('Escala ADA')
    label(s, 0.5, 1.0, 7.0, 0.45, 'ADA (adenosina desaminasa) · U/L', 16)
    zones = [(0, 40, '82E0AA', '< 40: NO TBC'), (40, 70, 'F9E79F', '40–70: indeterminado → biopsia'), (70, 100, 'E74C3C', '> 70: alta probabilidad de TBC')]
    for a, b, c, t in zones:
        x0 = 0.5 + 7.0 * a / 100; w = 7.0 * (b - a) / 100
        s.shape(x0, 1.55, w, 0.9, 'rect', c, BORDER, False, t, 12.5, F_HEAD, INK, True, 'c', 'm', minsize=9)
    s.group_end()
    lin = s.group_start('Linfocitos dibujados')
    import random
    r = random.Random(3)
    for k in range(18):
        cx = 0.8 + (k % 6) * 1.1 + r.uniform(-0.1, 0.1); cy = 3.0 + (k // 6) * 0.95 + r.uniform(-0.1, 0.1)
        s.shape(cx, cy, 0.6, 0.6, 'ellipse', shade('AED6F1', 0.3, 0.2), ('2E86C1', 1.25), False)
        s.shape(cx + 0.09, cy + 0.09, 0.42, 0.42, 'ellipse', '5B2C6F', None, False)
    s.group_end()
    a = box(s, 7.8, 1.0, 5.2, 2.7, '**ADA > 70 U/L**: alta probabilidad de TBC.\n**< 40**: no TBC.\n**40–70**: indeterminado → **biopsia**.',
            WHITE, 15, head='Formulación 1', headfill=GOLD, bold=False, align='l')
    b = box(s, 7.8, 3.9, 5.2, 2.0, '**ADA > 40 U/L** significativa, **siempre con linfocitosis** (linfocitos > 30–35 %) → compatible con TBC.',
            WHITE, 15, head='Formulación 2', headfill=CEL, bold=False, align='l')
    w = box(s, 0.5, 6.0, 12.5, 0.95, 'Los umbrales difieren entre fuentes: se presentan **ambos** y se registra la discrepancia.', RED, 14, name='ADA discrepancia')
    s.step(fade(bar))
    s.step(fade(lin))
    s.step(fade(a))
    s.step(fade(b))
    s.step(fade(w))


def celulas(D):
    s = new(D, 'Análisis del líquido', 'Recuento celular: qué célula predomina', 'rosa', src=['T4.4', 'P2.12'])
    items = [('Neutrófilos', 'Pleuritis **aguda**: infección bacteriana, TEP, infarto pulmonar.', 'F5B041', 'multi'),
             ('Linfocitos', '**Tumores, TBC**, linfoma, pleuritis crónica.', 'AED6F1', 'round'),
             ('Eosinófilos > 10 %', 'Reacción a **fármacos**, **vasculitis** (Churg-Strauss), **lupus**; parásitos, hongos, AR, **asbesto**.', 'F1948A', 'bilob'),
             ('Eritrocitos', '**Tumor o traumatismo**.', 'E74C3C', 'rbc')]
    ids = []
    for i, (h, t, c, kind) in enumerate(items):
        x = 0.4 + i * 3.18
        g = s.group_start('Célula ' + h)
        s.shape(x + 0.8, 1.15, 1.6, 1.6, 'ellipse', shade(c, 0.4, 0.2) if kind != 'rbc' else ('rad', [(0, 'E06A5F'), (60, 'C9372C'), (100, '7B1F17')], (50, 50)),
                (darken(c, 0.5), 2), SOFT)
        if kind == 'multi':
            for dx, dy in ((0.3, 0.35), (0.75, 0.3), (0.55, 0.8), (1.0, 0.75)):
                s.shape(x + 0.8 + dx, 1.15 + dy, 0.4, 0.4, 'ellipse', '6C3483', None, False)
        elif kind == 'round':
            s.shape(x + 1.0, 1.35, 1.2, 1.2, 'ellipse', '5B2C6F', None, False)
        elif kind == 'bilob':
            s.shape(x + 1.0, 1.6, 0.6, 0.7, 'ellipse', '6C3483', None, False)
            s.shape(x + 1.6, 1.6, 0.6, 0.7, 'ellipse', '6C3483', None, False)
        box(s, x, 3.0, 3.0, 2.6, t, WHITE, 14.5, head=h, headfill=c, bold=False)
        ids.append(s.group_end())
    n = box(s, 0.4, 5.8, 12.6, 1.15, 'Recordar la celularidad **normal**: 1.000–5.000/mm^{3} con predominio de **macrófagos** (Unidad I).', GOLD, 15, name='Normal ref')
    reveal(s, ids, 1)
    s.step(fade(n))


def otros(D):
    s = new(D, 'Análisis del líquido', 'Otros parámetros y su interpretación', 'mesotelio', src=['T4.4', 'P2.12'])
    rows = [['PARÁMETRO', 'HALLAZGO', 'ORIENTA A'],
            ['Amilasa', 'Pleura > sangre', 'Pancreatitis (derrame izquierdo) · perforación esofágica'],
            ['Triglicéridos', '> 110 mg/dl', 'Quilotórax (rotura del conducto torácico)'],
            ['Colesterol', '> 45 mg/dl', 'Criterio adicional de exudado (interpretación a revisar)'],
            ['Creatinina', 'Pleural > plasmática', 'Urinotórax'],
            ['β-2 transferrina', 'Presente', 'Fístula duro-pleural (LCR)'],
            ['ANA / FR', 'Pleura > sangre', 'LES / artritis reumatoidea'],
            ['BNP / péptido natriurético', '> 1500 pg/ml (en revisión)', 'ICC — marcador y umbral a verificar']]
    ids, h = gtable(s, 0.4, 1.0, 12.6, rows, [1.3, 1.3, 2.6], 14.5, head_fill=LBLUE, fill_to=6.95)
    table_anim(s, ids, 2)
    s = new(D, 'Análisis del líquido', 'Citología y microbiología', 'rosa', src=['T4.1', 'T5.2', 'T8.3', 'P2.12'])
    t1 = tube(s, 0.8, 1.2, 1.0, 3.0, 'E6B0AA', 'Anatomía patológica', 'clear', name='Tubo citología')
    t2 = tube(s, 0.8, 4.7, 0.9, 1.7, 'F7DC6F', 'Bacteriología', 'clear', name='Tubo bacterio')
    cs = two_cards(s, [('Citología', 'Búsqueda de **células malignas**: **citología positiva** = cáncer. En metástasis es positiva en ~**60 %**.', LILAC),
                       ('Si es negativa', 'Con alta sospecha: **biopsia pleural** (con aguja o guiada).', ORANGE),
                       ('Microbiología', '**Gram**, **cultivo** y **BAAR** (TBC). En el paraneumónico, **Gram o cultivo positivos = complicado → drenar**.', CEL)],
                   2.8, 1.0, 10.2, 5.95, 0.18, 15)
    s.step(fade(t1), fade(t2, after=True))
    reveal(s, cs, 1)


# ------------------------------------------------------------------ UNIDAD XI
def div11(D):
    def art(s):
        chest(s, 7.0, 0.6, 6.0, 5.9, {'fluidR': 0.45, 'pus': 1, 'septa': 1, 'consol': (250, 560, 110)})
    divider(D, 'XI', 'Derrame paraneumónico y empiema', 'Cuando la infección alcanza el espacio pleural',
            ['Concepto y relación con la neumonía', 'Formación del empiema (secuencia)', 'Seroso frente a purulento',
             'No complicado frente a complicado', 'Criterios de laboratorio', 'Manejo: drenaje y antibióticos'], art,
            src=['T5.1', 'P2.14'])


def seq_empiema(D):
    Q = Seq(D, 'Formación de empiema (Unidad XI)', 'Tórax: !!PulmonDerecho, !!Consolidacion, !!LiquidoPleuralD, !!Tabiques · Corte: '
            '!!PleuraParietal, !!LiquidoPleural, !!Leucocitos, !!Bacterias, !!Tabiques, !!PleuraVisceral', 'La consolidación aparece, la pleura se '
            'inflama, el líquido seroso se vuelve turbio y luego purulento con tabiques; el pulmón se comprime.')
    cons = (250, 560, 110)
    st = [({}, {'gap': 0.05}, 'Pulmón y pleura', 'Situación inicial: parénquima aireado y hojas pleurales normales.', None),
          ({'consol': cons, 'hl': {'Consolidacion'}}, {'gap': 0.05}, 'Proceso infeccioso', '**Neumonía** (bloque neumónico) adyacente a la pleura.',
           ('No todas las neumonías', 'La mayoría **no** evoluciona a empiema: es una posibilidad, no una regla.', GOLD)),
          ({'consol': cons}, {'gap': 0.06, 'inflam': 1}, 'Respuesta inflamatoria', 'La inflamación alcanza la pleura: **↑ permeabilidad**.',
           ('Mecanismo', 'Se repite el mecanismo D: exudado por pleura enferma.', GREEN)),
          ({'consol': cons, 'fluidR': 0.25, 'exud': 1}, {'gap': 0.3, 'inflam': 1, 'kind': 'exud', 'cells': 8, 'prot': 15}, 'Acumulación de líquido',
           'Derrame **paraneumónico no complicado**: exudado estéril.', ('No complicado', 'Se resuelve con el **antibiótico** de la neumonía.', C_EXUD)),
          ({'consol': cons, 'fluidR': 0.32, 'exud': 1}, {'gap': 0.38, 'inflam': 1, 'kind': 'exud', 'cells': 26, 'prot': 30, 'bact': 12},
           'Modificación de la composición', 'Ingresan **bacterias**; aumentan los PMN; cae el pH y la glucosa.', ('Complicado', 'El líquido **se infecta**: ya no se resuelve solo.', ORANGE)),
          ({'consol': cons, 'fluidR': 0.4, 'pus': 1}, {'gap': 0.45, 'inflam': 1, 'kind': 'pus', 'cells': 45, 'bact': 20}, 'Material purulento',
           'El líquido se transforma en **pus**: **empiema**.', ('Empiema', 'Pus en el espacio pleural.', C_PUS)),
          ({'consol': cons, 'fluidR': 0.42, 'pus': 1, 'septa': 1}, {'gap': 0.5, 'inflam': 1, 'kind': 'pus', 'cells': 45, 'bact': 20, 'septa': 1},
           'Tabiques y loculaciones', 'La fibrina forma **tabiques**: colecciones **loculadas** (TAC).', ('Loculación', 'Dificulta el drenaje; la TAC la detecta.', LBLUE)),
          ({'consol': cons, 'fluidR': 0.48, 'pus': 1, 'septa': 1}, {'gap': 0.5, 'inflam': 1, 'kind': 'pus', 'cells': 45, 'bact': 20, 'septa': 1},
           'Consecuencia funcional', 'Pulmón comprimido, **fiebre** persistente y riesgo de **estado séptico**.', ('Riesgo', 'Sin drenaje: empiema franco → **sepsis**.', RED)),
          ({'consol': cons, 'fluidR': 0.48, 'pus': 1, 'septa': 1}, {'gap': 0.5, 'inflam': 1, 'kind': 'pus', 'cells': 45, 'bact': 20, 'septa': 1},
           'Evaluación diagnóstica', 'Toracocentesis: aspecto, pH, glucosa, LDH, PMN, Gram y cultivo.', ('Diagnóstico', 'Ver criterios en la diapositiva siguiente.', CEL))]
    for i, (cs_, zs, ttl, cap, card) in enumerate(st):
        s = new(D, 'Empiema', ttl, 'azul', morph=i > 0, src=['T5.1', 'P2.14', 'P3.1'])
        A = chest(s, 0.25, 0.95, 4.8, 4.7, cs_)
        Z = pleura_zoom(s, 5.25, 0.95, 4.2, 4.7, zs)
        step_badge(s, i + 1, len(st))
        tag(s, 0.25, 5.75, 'TÓRAX', WHITE, 13, w=1.4); tag(s, 5.25, 5.75, 'CORTE DE LAS HOJAS', WHITE, 13, w=2.6)
        lg = legend(s, cap, 0.25, 6.25, 9.2, h=0.8, size=15)
        if card:
            c = box(s, 9.7, 0.95, 3.35, 3.0, card[1], card[2], 15, head=card[0], headfill=WHITE, bold=False)
            s.step(fade(c))
        if i >= 8:
            t = tube(s, 10.9, 4.15, 0.9, 2.4, 'E2C85A', 'Pus', 'pus', name='!!TuboEmpiema')
            s.step(fade(t))
        elif i >= 3:
            col = ['F3E5AB', 'E9C46A', 'E2C85A', 'E2C85A', 'E2C85A'][i - 3]
            t = tube(s, 10.9, 4.15, 0.9, 2.4, col, ['Turbio', 'Turbio', 'Purulento', 'Purulento', 'Purulento'][i - 3],
                     'turbid' if i < 5 else 'pus', name='!!TuboEmpiema')
        else:
            t = tube(s, 10.9, 4.15, 0.9, 2.4, 'F7E7A6', 'Seroso', 'clear', name='!!TuboEmpiema')
    Q.close()


def empiema_tabla(D):
    s = new(D, 'Empiema', 'No complicado, complicado y empiema', 'mesotelio', src=['T5.1', 'P2.14', 'T9.3'])
    rows = [['', 'NO COMPLICADO', 'COMPLICADO', 'EMPIEMA'],
            ['Concepto', 'Exudado **estéril**', 'Líquido **infectado** (bacterias)', '**Pus** en el espacio pleural'],
            ['Gram / cultivo', 'Negativos', '**Positivos** (formulación 2)', 'Frecuentemente positivos'],
            ['pH', '> 7,20', '**< 7,2**', '**< 7,20**'],
            ['Glucosa', 'Normal', '**< 60 mg/dl**', '**< 40 mg/dl** (formulación 1)'],
            ['LDH · PMN', 'LDH < 1000', '↑', 'LDH > 1000 · PMN > 50.000/mm^{3} (formulación 1)'],
            ['Aspecto', 'Seroso / turbio', 'Turbio', '**Purulento**'],
            ['Resolución', 'Espontánea con **antibióticos**', '**Requiere drenaje**', '**Drenaje obligatorio** + antibióticos']]
    ids, h = gtable(s, 0.4, 1.0, 9.3, rows, [1.15, 1.5, 1.5, 1.7], 13.5, head_fill=[WHITE, C_EXUD, ORANGE, C_PUS], fill_to=6.95)
    w = box(s, 9.95, 1.0, 3.05, 3.1, 'Los criterios de empiema como **suma obligatoria** y la equiparación «complicado» = '
            '«empiema» están **en revisión**.', RED, 13.5, name='Revisión empiema', bold=False)
    k = box(s, 9.95, 4.3, 3.05, 2.65, 'No esperar a que sea pus evidente: el complicado se **drena** para **evitar** el empiema.', GOLD,
            14, name='Drenar antes', bold=False)
    table_anim(s, ids, 2)
    s.step(fade(w))
    s.step(fade(k))
    s = new(D, 'Empiema', 'Manejo descrito: drenaje y antibióticos', 'azul', src=['T5.1', 'P2.14', 'T7.3'])
    A = chest(s, 0.3, 0.95, 5.6, 5.5, {'fluidR': 0.4, 'pus': 1, 'consol': (250, 560, 110)})
    F = A['F']
    tb = s.arrow([F.p(40, 700), F.p(200, 690)], 'D5DBDB', 9, tail=None, name='!!TuboDrenaje')
    gW = s.group_start('!!SistemaDrenaje')
    W = water_seal(s, 0.4, 4.5, 1.35, 2.5, {'bubbles': 0})
    gW = s.group_end()
    cs = two_cards(s, [('Antibióticos', 'Tratamiento de la **neumonía** de base (todos los paraneumónicos).', CEL),
                       ('Drenaje', 'Complicado / empiema: **tubo de tórax con trampa de agua**; sin drenaje **no se resuelve**.', ORANGE),
                       ('Objetivo', 'Evacuar el material infectado, **reexpandir** el pulmón y **controlar la fiebre**.', GREEN),
                       ('Seguimiento', 'Control **clínico** y **radiológico** de la reexpansión.', GOLD)], 6.2, 1.0, 6.8, 5.95, 0.15, 15)
    s.step(wipe(tb, 'l'), fade(gW, after=True))
    reveal(s, cs, 1)


def build(D):
    unit_start(D, 'IX', 'Criterios de Light')
    div9(D)
    light(D)
    unit_end(D, 'IX')
    unit_start(D, 'X', 'Análisis del líquido pleural')
    div10(D)
    aspecto(D)
    glucosa_ph(D)
    ada(D)
    celulas(D)
    otros(D)
    unit_end(D, 'X')
    unit_start(D, 'XI', 'Derrame paraneumónico y empiema')
    div11(D)
    seq_empiema(D)
    empiema_tabla(D)
    unit_end(D, 'XI')
