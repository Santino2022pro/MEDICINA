# -*- coding: utf-8 -*-
"""UNIDAD XII (neumotórax), XIII (semiología comparada) y XIV (ecografía pleural)."""
from base import *


def div12(D):
    def art(s):
        chest(s, 7.0, 0.6, 6.0, 5.9, {'airR': 0.6, 'shift': 20})
    divider(D, 'XII', 'Neumotórax', 'Aire en el espacio pleural',
            ['Definición y presiones', 'Formación del neumotórax (secuencia)', 'Clasificación etiológica', 'Cuadro clínico',
             'Vigilancia hemodinámica', 'Relación con el derrame'], art, src=['T6.1', 'T6.2', 'P3.1', 'P3.5'])


def definicion(D):
    s = new(D, 'Neumotórax', 'Definición: aire entre las hojas pleurales', 'azul', src=['T6.1', 'P3.1'])
    A = chest(s, 0.3, 0.95, 6.0, 5.9, {'airR': 0.45, 'hl': {'AirePleuralD'}})
    co = callout(s, [A['airR'], (6.6, 1.3)], 'AIRE en el espacio pleural', 6.6, 1.0, 3.4, 0.6, C_AIR, 15)
    cs = two_cards(s, [('Definición', 'Presencia de **aire en la cavidad pleural**, entre la pleura parietal y la visceral, con **colapso pulmonar total o parcial**.', CEL),
                       ('Mecanismo', 'El aire **rompe la presión negativa** que mantenía el pulmón expandido: el pulmón colapsa por su **elasticidad intrínseca**.', GREEN),
                       ('Relación con el derrame', 'Derrame paraneumónico y neumotórax pueden ser **eventos paralelos** o depender del **mismo foco** neumónico.', GOLD)],
                   6.6, 1.8, 6.4, 5.15, 0.15, 15)
    w = box(s, 10.2, 1.0, 2.8, 0.6, 'No es aire en el parénquima', RED, 12, name='No parénquima')
    s.step(fade(co), pulse(A['ids']['airR'], after=True))
    reveal(s, cs, 1)
    s.step(fade(w))


def manometro(s, x, y, h, val, name='!!Manometro'):
    """barra de presión pleural: val -1 (negativa normal) … 0 (atmosférica) … +1 (positiva)"""
    g = s.group_start(name)
    s.shape(x, y, 0.75, h, 'rect', ('lin', [(0, 'E74C3C'), (50, 'F9E79F'), (100, '5DADE2')], 90), BORDER, False)
    for v, t in ((1, '+'), (0, '0 atm'), (-1, '−')):
        yy = y + h * (1 - (v + 1) / 2)
        s.arrow([(x - 0.12, yy), (x + 0.87, yy)], INK, 1.5, tail=None)
        label(s, x + 0.9, yy - 0.17, 0.9, 0.34, t, 13, align='l')
    label(s, x - 0.35, y - 0.5, 1.6, 0.45, 'P. pleural', 14)
    s.group_end()
    yy = y + h * (1 - (val + 1) / 2)
    return s.shape(x - 0.3, yy - 0.16, 0.42, 0.32, 'rightArrow', INK, None, False, name='!!AgujaPresion')


def seq_formacion(D):
    Q = Seq(D, 'Formación del neumotórax (Unidad XII)', '!!PulmonDerecho, !!PleuraVisceralD, !!PleuraParietalD, !!AirePleuralD, !!Bulas, '
            '!!AgujaPresion, !!Leyenda', 'El MISMO pulmón se retrae hacia el hilio a medida que el aire ocupa el espacio pleural; la aguja del '
            'manómetro sube de presión negativa hacia la atmosférica.')
    st = [({'blebs': 1}, -0.8, 'Pulmón expandido', 'El pulmón llena su hemitórax gracias a la **presión pleural negativa**.', ('Estado basal', 'Pulmón expandido; bulas subpleurales apicales.', CEL)),
          ({'blebs': 1, 'hl': {'PleuraVisceralD', 'PleuraParietalD'}}, -0.8, 'Pleuras normalmente relacionadas', 'Las dos hojas están **en contacto**, separadas solo por el líquido.',
           ('Hojas acopladas', 'Parietal (verde azulada) y visceral (morada) se mueven juntas.', TURQ)),
          ({'blebs': 1, 'airR': 0.06, 'hl': {'Bulas'}}, -0.6, 'Entrada de aire al espacio pleural', 'Rotura de una **bula subpleural** (o lesión de la pared): el aire **entra al espacio pleural**.',
           ('Puerta de entrada', 'Desde el pulmón (bulas) o desde el exterior (trauma, procedimientos).', ORANGE)),
          ({'blebs': 1, 'airR': 0.18}, -0.45, 'Separación de las superficies', 'El aire **separa** la hoja visceral de la parietal.', ('Separación', 'El espacio virtual se hace **real**.', CEL)),
          ({'blebs': 1, 'airR': 0.28, 'hl': {'AirePleuralD'}}, -0.2, 'Modificación de la presión pleural', 'La presión pleural **deja de ser negativa** y se acerca a la atmosférica.',
           ('Presión', 'Se pierde la fuerza que mantenía el pulmón expandido.', GOLD)),
          ({'blebs': 1, 'airR': 0.4}, -0.08, 'Retracción pulmonar', 'Libre de la tracción de la pared, el pulmón se **retrae por su elasticidad**.', ('Retracción', 'Fuerza elástica hacia el **hilio**.', GREEN)),
          ({'blebs': 1, 'airR': 0.55}, 0, 'Colapso parcial', 'Colapso **parcial**: predominio **apical** en el paciente erguido.', ('Colapso parcial', 'El borde pulmonar se aleja de la pared.', LBLUE)),
          ({'blebs': 1, 'airR': 0.85}, 0, 'Colapso extenso', 'Colapso **extenso**: el pulmón queda como un **muñón** hacia el hilio.', ('Colapso extenso', 'Signo del **muñón** en la radiografía (Unidad XV).', ORANGE)),
          ({'blebs': 1, 'airR': 0.85}, 0, 'Repercusión ventilatoria', 'Menos pulmón ventilado → **disnea**, taquipnea; posible **hipoxemia** (SpO_{2} < 90 %).', ('Ventilación', 'La gravedad depende del **tamaño** y de la **reserva pulmonar**.', RED)),
          ({'blebs': 1, 'airR': 0.85}, 0, 'Hallazgos clínicos', 'Dolor pleurítico · disnea · tos seca; hipersonoridad y ausencia de murmullo (Unidad XIII).', ('Clínica', 'Tríada clásica del neumotórax simple.', TURQ))]
    for i, (cst, pv, ttl, cap, card) in enumerate(st):
        s = new(D, 'Neumotórax', ttl, 'azul', morph=i > 0, src=['T6.1', 'P3.1'])
        A = chest(s, 0.3, 0.95, 6.3, 6.15, cst)
        step_badge(s, i + 1, len(st))
        ag = manometro(s, 7.05, 1.6, 4.1, pv)
        c = box(s, 9.0, 1.0, 4.0, 2.7, card[1], card[2], 16, head=card[0], headfill=WHITE, bold=False)
        lg = legend(s, cap, 9.0, 3.9, 4.0, h=1.9, size=15)
        if i == 2:
            hx, hy = A['apexR']
            ar = s.arrow([(hx + 0.1, hy + 0.35), (hx - 0.35, hy + 0.25)], RED, 4, name='Fuga aérea')
            s.step(wipe(ar, 'r'), fade(A['ids']['airR'], after=True))
        if i == 5:
            F = A['F']
            ars = [s.arrow([F.p(200, 400), F.p(290, 430)], C_VISCERAL, 5, name='Retracción %d' % k) if k == 0 else
                   s.arrow([F.p(260, 700), F.p(330, 620)], C_VISCERAL, 5, name='Retracción %d' % k) for k in range(2)]
            s.step(*[wipe(a, 'l', after=bool(k)) for k, a in enumerate(ars)])
        if i == 8:
            sp = box(s, 9.0, 6.0, 4.0, 0.95, 'SpO_{2} < 90 % = hipoxemia significativa', RED, 14, name='SpO2')
            s.step(zoom(sp))
        s.step(fade(c))
    Q.close()


def clasificacion(D):
    s = new(D, 'Neumotórax', 'Clasificación: espontáneo', 'mesotelio', src=['T6.2', 'P3.5'])
    a = chest(s, 0.3, 1.0, 3.6, 3.5, {'blebs': 1, 'airR': 0.3}, names=False)
    b = chest(s, 0.3, 4.55, 2.5, 2.45, {'airR': 0.3, 'lungcolR': 'D5A6BD', 'lungcolL': 'D5A6BD'}, names=False)
    p = box(s, 4.2, 1.0, 4.3, 3.5, '**Sin enfermedad pulmonar** clínica aparente.\nRotura de **bulas (blebs) subpleurales**.\nPerfil: **varón joven, alto, delgado**, '
            'a menudo fumador.', CEL, 15, head='Espontáneo primario', headfill=WHITE, bold=False, align='l')
    q = box(s, 4.2, 4.65, 4.3, 2.3, '**Con enfermedad pulmonar**: EPOC/enfisema (bulas enfisematosas), asma grave, TBC, fibrosis quística, neumonía por '
            'Pneumocystis, EPID.', ORANGE, 13.5, head='Espontáneo secundario', headfill=WHITE, bold=False, align='l')
    r = box(s, 8.8, 1.0, 4.2, 3.5, 'El **secundario** es **más grave** que el primario: el paciente tiene **menor reserva pulmonar**.', RED, 16,
            name='Gravedad secundario', bold=False)
    t = box(s, 8.8, 4.65, 4.2, 2.3, 'Las bulas también se denominan «ámpulas» en algunos textos.', WHITE, 14, name='Terminología', bold=False)
    s.step(fade(p))
    s.step(fade(q))
    s.step(fade(r))
    s.step(fade(t))
    s = new(D, 'Neumotórax', 'Clasificación: traumático e iatrogénico', 'mesotelio', src=['T6.2', 'P3.5'])
    cards = [('Traumático penetrante (abierto)', 'Arma de fuego, arma blanca, objeto punzante. **Hemotórax** asociado frecuente.', ORANGE, {'airR': 0.4, 'fluidR': 0.12, 'blood': 1}),
             ('Traumático cerrado', 'Contusión: accidente de tránsito (tórax contra el volante), caída. **Fractura costal** que lacera la pleura.', GOLD, {'airR': 0.35}),
             ('Iatrogénico', 'Catéter en **vena subclavia** · aspiración transtorácica (biopsia) · **toracocentesis** o biopsia pleural · **barotrauma** '
              '(ventilación con presión positiva). El más frecuente en el hospital.', LBLUE, {'airR': 0.3})]
    ids = []
    for i, (h, t, c, st) in enumerate(cards):
        x = 0.4 + i * 4.25
        g = s.group_start('Tipo ' + h)
        chest(s, x + 0.6, 1.0, 2.9, 2.8, st, names=False)
        box(s, x, 3.95, 4.05, 3.0, t, c, 14, head=h, headfill=WHITE, bold=False)
        ids.append(s.group_end())
    reveal(s, ids, 1)


def clinica(D):
    s = new(D, 'Neumotórax', 'Cuadro clínico del neumotórax simple', 'torax', src=['T6.3', 'P3.2'])
    A = chest(s, 0.3, 1.0, 4.6, 4.5, {'airR': 0.5})
    cs = [box(s, 5.2, 1.0, 3.8, 3.0, 'Puntada de costado; aumenta con la tos. Es el síntoma **más frecuente e inmediato**.\n**No siempre** es pleurítico: '
              'puede ser **opresivo** o **leve**.', ORANGE, 13.5, head='Dolor', headfill=WHITE, bold=False, align='l'),
          box(s, 9.2, 1.0, 3.8, 3.0, 'Variable según la **magnitud**: mínima en el pequeño; en el grande, **disnea intensa**, musculatura accesoria, '
              'taquipnea, cianosis.', CEL, 13.5, head='Disnea', headfill=WHITE, bold=False, align='l'),
          box(s, 5.2, 4.2, 3.8, 2.75, '**Tos seca** irritativa: puede estar o no.', TURQ, 15, head='Tos', headfill=WHITE, bold=False),
          box(s, 9.2, 4.2, 3.8, 2.75, 'La **inflamación** pleural (pleuritis; antes «pleuresía») produce dolor pleurítico **sin perforación**.',
              GOLD, 14, head='Dolor sin aire', headfill=WHITE, bold=False)]
    n = box(s, 0.3, 5.7, 4.6, 1.25, 'Disnea **pleural** frente a disnea **pulmonar**: distinguir su origen.', WHITE, 14, name='Disnea tipos', bold=False)
    reveal(s, cs, 1)
    s.step(fade(n))
    s = new(D, 'Neumotórax', 'Vigilancia hemodinámica: nunca solo la imagen', 'azul', src=['P3.4', 'P3.11'])
    mon = s.group_start('!!Monitor')
    s.shape(0.4, 1.0, 6.4, 4.4, 'roundRect', '1C2833', BORDER, False, adj={'adj': 6000})
    vit = [('FR', 'taquipnea', '58D68D'), ('FC', 'taquicardia', 'F4D03F'), ('TA', 'hipotensión = shock', 'EC7063'), ('SpO_{2}', '< 90 % = hipoxemia', '5DADE2')]
    for i, (k, t, c) in enumerate(vit):
        y = 1.2 + i * 1.02
        s.shape(0.65, y, 1.3, 0.85, 'rect', None, (c, 2), False, k, 22, F_HEAD, c, True, 'c', 'm', fit=False)
        s.free(2.1, y + 0.1, 2.6, 0.65, 'M 0 500 L 150 500 L 220 100 L 300 900 L 380 500 L 600 500 L 670 150 L 750 850 L 820 500 L 1000 500',
               None, (c, 2.25))
        label(s, 4.8, y, 1.9, 0.85, t, 13, c, align='l')
    s.group_end()
    cs = two_cards(s, [('Controlar siempre', 'FR · FC · TA · SpO_{2} en **todo** paciente con neumotórax.', CEL),
                       ('Disnea oculta', 'El paciente puede **no parecer disneico** y tener SpO_{2} < 90 %: a menudo «se automejora» ante el médico.', ORANGE),
                       ('Conducta', 'Integrar el **tamaño** del neumotórax con la **estabilidad**: nunca decidir solo por la imagen.', GREEN)],
                   7.1, 1.0, 5.9, 5.95, 0.15, 15)
    n = box(s, 0.4, 5.6, 6.4, 1.35, 'Al retirarse de la cama, **seguir observando** al paciente.', RED, 16, name='Observar')
    s.step(fade(mon))
    reveal(s, cs, 1)
    s.step(fade(n))


# ------------------------------------------------------------------ UNIDAD XIII
def div13(D):
    def art(s):
        for i, st in enumerate(({}, {'fluidR': 0.5}, {'airR': 0.6})):
            chest(s, 6.9 + i * 2.1, 2.0, 2.0, 2.0, st, names=False)
    divider(D, 'XIII', 'Semiología del neumotórax', 'Normal · derrame · neumotórax: la misma exploración, tres respuestas',
            ['Inspección', 'Palpación y frémito', 'Percusión: sonoridad, matidez, hipersonoridad', 'Auscultación', 'Síntesis comparativa',
             'Enfisema subcutáneo'], art, src=['T6.4', 'P3.3'])


def comparativa(D):
    sts = [({}, 'NORMAL', WHITE), ({'fluidR': 0.5}, 'DERRAME', C_FLUID), ({'airR': 0.6}, 'NEUMOTÓRAX', C_AIR)]
    pages = [('Inspección y palpación', [
        ('Expansión simétrica · frémito transmitido', '↓ movimientos, abombamiento · **frémito abolido** sobre el líquido',
         'Asimetría: hemitórax afectado **más expandido** y menos móvil · **frémito ↓/abolido** · posible **enfisema subcutáneo** (crepitación)')],
              'El aire, como el líquido, **atenúa** las vibraciones vocales: el frémito no distingue entre ambos.'),
             ('Percusión', [('**Sonoridad**', '**MATIDEZ** hídrica (líquido = mate)', '**HIPERSONORIDAD** / timpanismo (aire)')],
              'La percusión es la **diferencia fundamental**: matidez en el derrame, hipersonoridad en el neumotórax.'),
             ('Auscultación', [('**Murmullo vesicular** normal', '↓ o abolición del MV · **soplo tubario** por encima',
                                '**Ausencia** de MV · soplo **anfórico**')],
              'El aire interpuesto **impide** la conducción del sonido: ruidos muy disminuidos o abolidos.')]
    for k, (ttl, rows, concl) in enumerate(pages):
        s = new(D, 'Semiología comparada', ttl + ': normal, derrame y neumotórax', 'azul', src=['T6.4', 'P3.3', 'T3.2'])
        cols = []
        for i, (st, h, c) in enumerate(sts):
            x = 0.35 + i * 4.25
            g = s.group_start('Columna ' + h)
            A = chest(s, x + 0.45, 0.95, 3.2, 3.1, st, names=False)
            F = A['F']
            if k == 0:
                waves(s, *F.p(260, 330), 0.15, 3 if i == 0 else 1, 0.14, '1E8449' if i == 0 else '922B21', 3, (150, 210), name='Ondas %d' % i,
                      dash=None if i == 0 else 'dash')
            elif k == 1:
                hand(s, F.p(40, 0)[0], F.p(0, 620)[1], 0.9, name='Mano %d' % i)
                waves(s, F.p(40, 0)[0] + 0.95, F.p(0, 640)[1], 0.12, [3, 1, 4][i], 0.13, ['1E8449', '922B21', '1F618D'][i], 3, (-40, 40), name='Sonido %d' % i)
            else:
                stetho(s, *F.p(170, 560), 0.4, name='Estetoscopio %d' % i)
            box(s, x, 4.15, 4.05, 0.5, h, c, 16)
            box(s, x, 4.7, 4.05, 1.25, rows[0][i], c, 13.5, bold=False)
            cols.append(s.group_end())
        n = box(s, 0.35, 6.1, 12.6, 0.9, concl, GOLD, 15, name='Conclusión', bold=False)
        reveal(s, cols, 1)
        s.step(fade(n))
    s = new(D, 'Semiología comparada', 'Síntesis: derrame pleural frente a neumotórax', 'mesotelio', src=['T6.4', 'P3.3'])
    rows = [['MÉTODO', 'DERRAME PLEURAL', 'NEUMOTÓRAX'],
            ['Inspección', 'Abombamiento, ↓ movimientos', 'Cianosis, dificultad respiratoria, abombamiento, facie ansiosa, asimetría'],
            ['Palpación', 'Abolición de VV sobre el derrame', '↓ expansión · abolición de VV · crepitación si hay enfisema subcutáneo'],
            ['Percusión', '**MATIDEZ** hídrica', '**HIPERSONORIDAD** / timpanismo'],
            ['Auscultación', '↓ o abolición MV · **soplo tubario**', '**Ausencia** de MV · soplo **anfórico**']]
    ids, h = gtable(s, 0.4, 1.0, 12.6, rows, [1, 2, 2.4], 15, head_fill=[TURQ, C_FLUID, C_AIR], fill_to=6.95)
    table_anim(s, ids, 1)


# ------------------------------------------------------------------ UNIDAD XIV
def div14(D):
    def art(s):
        probe(s, 7.6, 1.0, 0.8, name='Arte transductor')
        bmode(s, 8.8, 0.9, 4.2, 3.0, {'pattern': 'A'}, prefix='Arte B')
        mmode(s, 7.2, 4.1, 2.8, 2.7, 'playa', prefix='Arte M1')
        mmode(s, 10.2, 4.1, 2.8, 2.7, 'codigo', prefix='Arte M2')
    divider(D, 'XIV', 'Ecografía pleural', 'Ver el deslizamiento de las hojas',
            ['Principio físico: emisión y eco', 'Deslizamiento pleural (secuencia)', 'Líneas A y líneas B', 'Modo M: playa y código de barras',
             'Punto pulmonar', 'Trilogía diagnóstica y límites de interpretación'], art, src=['P3.6', 'P3.7'])


def principio(D):
    s = new(D, 'Ecografía', 'Principio: el transductor emite y escucha', 'azul', src=['P3.6'])
    Z = pleura_zoom(s, 0.3, 1.9, 7.4, 5.05, {'gap': 0.05})
    p = probe(s, 2.6, 0.95, 0.7)
    pul = s.shape(2.82, 2.1, 0.26, 0.26, 'ellipse', 'F1C40F', (INK, 1), False, name='!!PulsoUltrasonido')
    ech = s.shape(4.0, 4.0, 0.22, 0.22, 'ellipse', '5DADE2', (INK, 1), False, name='!!Eco')
    steps = [('1', 'El **transductor** emite la onda sonora.'), ('2', 'La onda **choca** con estructuras de distinta densidad.'),
             ('3', 'El mismo transductor **capta el eco** (rebote).'), ('4', 'Lo convierte en imagen en **escala de grises**.'),
             ('5', 'La **ecogenicidad** depende de la **densidad** del tejido.')]
    ids = []
    for i, (n_, t) in enumerate(steps):
        g = s.group_start('Principio %s' % n_)
        badge(s, 8.0, 1.0 + i * 1.18, n_, 0.5)
        box(s, 8.6, 0.95 + i * 1.18, 4.4, 1.05, t, WHITE, 15, bold=False)
        ids.append(s.group_end())
    s.step(fade(p), fade(ids[0], after=True))
    s.step(fade(pul), path(pul, 0, 2.15, after=True, dur=900), fade(ids[1], after=True))
    s.step(fade(ech), path(ech, -1.1, -1.75, after=True, dur=900), fade(ids[2], after=True))
    s.step(fade(ids[3]))
    s.step(fade(ids[4]))
    s = new(D, 'Ecografía', 'Cono de sombra: confirmar lo muy denso', 'azul', src=['P3.6'])
    e = bmode(s, 0.4, 1.0, 6.0, 4.6, {'pattern': 'normal'})
    co1 = callout(s, [e['F'].p(160, 330), (6.8, 1.3)], 'Costilla: blanca (hiperecoica)', 6.8, 1.0, 3.8, 0.6, WHITE, 14)
    co2 = callout(s, [e['F'].p(160, 700), (6.8, 2.1)], 'Cono de sombra posterior (negro)', 6.8, 1.8, 3.8, 0.6, '7F8C8D', 14)
    cs = two_cards(s, [('Regla', 'Nunca afirmar «es un **cálculo**» por su brillo: **confirmar el cono de sombra** posterior.', RED),
                       ('Grises', 'Más negro: líquido · gris: tejidos intermedios · más blanco: tejido más denso.', GOLD)], 6.8, 2.7, 6.2, 4.25, 0.18, 15)
    s.step(fade(co1))
    s.step(fade(co2))
    reveal(s, cs, 1)


def seq_deslizamiento(D):
    Q = Seq(D, 'Deslizamiento pleural ecográfico: normal y con aire (Unidad XIV)', '!!PielPared, !!Costillas, !!PleuraParietal, !!PleuraVisceral, '
            '!!Alveolos, !!AirePleural, !!TransductorEcografico, !!EcoPantalla, !!ModoMPantalla, !!Leyenda', 'Del tórax al corte de las hojas bajo '
            'el transductor; la hoja visceral se desliza (normal) o queda separada por aire (neumotórax); aparecen modo B y modo M correspondientes.')
    TOT = 10
    # 1 tórax
    s = new(D, 'Ecografía', 'Tórax: el transductor sobre la pared anterior', 'azul', src=['P3.7'])
    A = chest(s, 0.3, 0.95, 6.3, 6.15, {})
    step_badge(s, 1, TOT)
    p = probe(s, A['F'].p(250, 0)[0], A['F'].p(0, 230)[1], 0.6)
    b = box(s, 7.0, 1.0, 6.0, 2.6, 'El transductor apoyado entre dos costillas «mira» la **interfaz pleural**: el límite entre pared y pulmón.',
            CEL, 16, name='Interfaz', bold=False)
    s.step(fade(p))
    s.step(fade(b))
    # 2-6 corte
    data = [('Acercamiento a las pleuras', {'gap': 0.05}, 'Bajo el transductor: pared, costillas y las dos hojas.', None),
            ('Identificación de la pleura parietal', {'gap': 0.05, 'hl': {'PleuraParietal'}}, 'La **parietal** queda fija a la pared.', 'par'),
            ('Identificación de la pleura visceral', {'gap': 0.05, 'hl': {'PleuraVisceral'}}, 'La **visceral** acompaña al pulmón.', 'visc'),
            ('Movimiento respiratorio', {'gap': 0.05}, 'Con cada respiración el pulmón se desplaza…', 'mov'),
            ('Deslizamiento pleural', {'gap': 0.05}, '…y la visceral **se desliza** sobre la parietal: es el **sliding**.', 'slide')]
    for k, (ttl, st, cap, mk) in enumerate(data):
        s = new(D, 'Ecografía', ttl, 'azul', morph=True, src=['P3.7'])
        Z = pleura_zoom(s, 0.3, 1.85, 6.5, 5.1, st)
        step_badge(s, k + 2, TOT)
        p = probe(s, 3.2, 0.95, 0.6)
        lg = legend(s, cap, 7.1, 1.0, 5.9, h=1.4, size=16)
        E = bmode(s, 7.1, 2.6, 5.9, 3.05, {'pattern': 'A', 'hlpl': mk in ('par', 'visc', 'slide')})
        tag(s, 7.1, 5.72, 'MODO B: la interfaz pleural es la línea brillante', WHITE, 12.5, w=5.9)
        if mk == 'par':
            c = callout(s, [Z['par_pt'], (7.1, 6.5)], 'PLEURA PARIETAL', 7.1, 6.25, 3.2, 0.55, C_PARIETAL, 15)
            s.step(fade(c), pulse(Z['par'], after=True))
        if mk == 'visc':
            c = callout(s, [Z['visc_pt'], (7.1, 6.5)], 'PLEURA VISCERAL', 7.1, 6.25, 3.2, 0.55, C_VISCERAL, 15)
            s.step(fade(c), pulse(Z['visc'], after=True))
        if mk in ('mov', 'slide'):
            s.step(path(Z['visc'], 0.5, 0, dur=900), path(Z['alv'], 0.5, 0, dur=900))
            s.step(path(Z['visc'], -0.5, 0, dur=900), path(Z['alv'], -0.5, 0, dur=900))
        if mk == 'slide':
            b = box(s, 7.1, 6.2, 5.9, 0.78, 'En tiempo real: **«centelleo»** de la línea pleural.', GREEN, 15, name='Centelleo', bold=False)
            s.step(fade(b), pulse(E['pline'], after=True))
    # 7 representación normal
    s = new(D, 'Ecografía', 'Representación ecográfica normal', 'azul', morph=True, src=['P3.7'])
    Z = pleura_zoom(s, 0.3, 1.85, 4.0, 5.1, {'gap': 0.05})
    step_badge(s, 7, TOT)
    p = probe(s, 1.95, 0.95, 0.45)
    E = bmode(s, 4.6, 0.95, 4.2, 3.0, {'pattern': 'A'})
    M = mmode(s, 4.6, 4.1, 4.2, 2.85, 'playa')
    cs = two_cards(s, [('Modo B', 'Línea pleural brillante entre costillas; **líneas A** horizontales.', LBLUE),
                       ('Modo M', '**Signo de la playa**: «olas» arriba (pared quieta) y **«arena»** abajo (pulmón que se desliza).', GREEN)], 9.0, 0.95, 4.0, 6.0, 0.18, 15)
    reveal(s, cs, 1)
    # 8 aire pleural
    s = new(D, 'Ecografía', 'Situación con aire en el espacio pleural', 'azul', morph=True, src=['P3.7'])
    Z = pleura_zoom(s, 0.3, 1.85, 4.0, 5.1, {'gap': 0.35, 'kind': 'air'})
    step_badge(s, 8, TOT)
    p = probe(s, 1.95, 0.95, 0.45)
    b = box(s, 4.6, 0.95, 8.4, 2.5, 'El **aire** se interpone entre las hojas: el haz ultrasónico **se refleja** en la interfaz y **no llega** a la hoja visceral.',
            ORANGE, 16, name='Aire interpuesto', bold=False)
    c = box(s, 4.6, 3.65, 8.4, 3.3, 'Debajo del transductor ya **no hay pulmón en contacto** con la pared: lo que se mueve no se ve.', WHITE, 16,
            name='Sin contacto', bold=False)
    s.step(fade(b))
    s.step(fade(c))
    # 9 alteración del deslizamiento
    s = new(D, 'Ecografía', 'Alteración del deslizamiento', 'azul', morph=True, src=['P3.7'])
    Z = pleura_zoom(s, 0.3, 1.85, 4.0, 5.1, {'gap': 0.35, 'kind': 'air'})
    step_badge(s, 9, TOT)
    p = probe(s, 1.95, 0.95, 0.45)
    x = s.shape(1.9, 3.3, 0.8, 0.8, 'mathMultiply', RED, (INK, 1.5), False, name='!!SinDeslizamiento')
    b = box(s, 4.6, 0.95, 8.4, 2.5, '**Ausencia de deslizamiento**: la línea pleural queda **estática**.', RED, 18, name='Ausencia sliding', bold=False)
    c = box(s, 4.6, 3.65, 8.4, 3.3, 'Hallazgo **compatible** con aire pleural, pero **por sí solo no es diagnóstico definitivo**: debe integrarse con los '
            'demás signos (trilogía y punto pulmonar).', GOLD, 15, name='No aislado', bold=False)
    s.step(zoom(x), fade(b, after=True))
    s.step(fade(c))
    # 10 representación con aire
    s = new(D, 'Ecografía', 'Representación ecográfica con aire pleural', 'azul', morph=True, src=['P3.7'])
    Z = pleura_zoom(s, 0.3, 1.85, 4.0, 5.1, {'gap': 0.35, 'kind': 'air'})
    step_badge(s, 10, TOT)
    p = probe(s, 1.95, 0.95, 0.45)
    E = bmode(s, 4.6, 0.95, 4.2, 3.0, {'pattern': 'A'})
    M = mmode(s, 4.6, 4.1, 4.2, 2.85, 'codigo')
    cs = two_cards(s, [('Modo B', 'Línea pleural **sin centelleo**; **líneas A** presentes; **sin líneas B**.', LBLUE),
                       ('Modo M', '**Código de barras** (signo de la estratósfera): líneas horizontales en toda la profundidad.', RED)], 9.0, 0.95, 4.0, 6.0, 0.18, 15)
    reveal(s, cs, 1)
    Q.close()


def signos(D):
    s = new(D, 'Ecografía', 'Signos ecográficos (1/2)', 'mesotelio', src=['P3.7'])
    rows = [['SIGNO', 'DESCRIPCIÓN', 'SIGNIFICADO'],
            ['Líneas B', 'Artefactos **verticales**, hiperecoicos, en cola de cometa, que nacen de la pleura', 'Su **presencia descarta** neumotórax en ese punto (pulmón en contacto)'],
            ['Líneas A', 'Artefactos **horizontales**', 'Con ausencia de deslizamiento → **patrón A**: compatible con neumotórax'],
            ['Deslizamiento', 'Movimiento de la visceral sobre la parietal con la respiración', 'Su **ausencia** forma parte de la trilogía'],
            ['Pulso pulmonar', 'Vibración de la visceral **sincrónica con el latido**', 'Su **ausencia** completa la trilogía']]
    ids, h = gtable(s, 0.4, 1.0, 8.4, rows, [1.1, 2.2, 2.2], 13.5, head_fill=LBLUE, fill_to=6.95)
    e1 = bmode(s, 9.1, 1.0, 3.9, 2.85, {'pattern': 'B'}, prefix='SigB ')
    e2 = bmode(s, 9.1, 4.1, 3.9, 2.85, {'pattern': 'A'}, prefix='SigA ')
    table_anim(s, ids, 1)
    s = new(D, 'Ecografía', 'Signos ecográficos (2/2): modo M y punto pulmonar', 'mesotelio', src=['P3.7'])
    m1 = mmode(s, 0.4, 1.0, 4.0, 2.7, 'playa', prefix='M1 ')
    m2 = mmode(s, 4.65, 1.0, 4.0, 2.7, 'codigo', prefix='M2 ')
    m3 = mmode(s, 8.9, 1.0, 4.1, 2.7, 'punto', prefix='M3 ')
    cs = [box(s, 0.4, 3.85, 4.0, 2.0, 'Imagen **dinámica**: pulmón residual que **mantiene** deslizamiento.', GREEN, 14, head='Signo de la playa', headfill=WHITE, bold=False),
          box(s, 4.65, 3.85, 4.0, 2.0, 'Imagen **rígida**, estática: donde hay aire no hay pulmón.', RED, 14, head='Código de barras', headfill=WHITE, bold=False),
          box(s, 8.9, 3.85, 4.1, 2.0, 'Encuentro playa/código de barras en tiempo real: **especificidad ~100 %**.', GOLD, 14, head='Punto pulmonar', headfill=WHITE, bold=False)]
    e = box(s, 0.4, 6.0, 12.6, 0.95, '**Líneas E**: artefactos en el tejido celular subcutáneo por **enfisema subcutáneo**; no son propias del neumotórax pleural.',
            WHITE, 14, name='Líneas E', bold=False)
    for c in cs:
        s.step(fade(c))
    s.step(fade(e))
    s = new(D, 'Ecografía', 'Trilogía diagnóstica y límites de interpretación', 'azul', src=['P3.7'])
    tri = flow(s, ['**Ausencia** de pulso pulmonar', '**Presencia** de líneas A', '**Ausencia** de deslizamiento'], 0.4, 1.0, 12.6, 1.5,
               [WHITE, LBLUE, RED], 17, 0.4)
    r = box(s, 0.4, 2.8, 6.1, 2.1, 'Los tres juntos = **neumotórax**. El **punto pulmonar** es el hallazgo más específico.', GREEN, 16, name='Trilogía resultado', bold=False)
    w = box(s, 6.8, 2.8, 6.2, 2.1, 'Un signo **aislado** (p. ej., solo la ausencia de deslizamiento) **no es concluyente**: otras causas no están '
            'desarrolladas aquí → **verificar**.', RED, 14.5, name='Límite', bold=False)
    m = box(s, 0.4, 5.1, 12.6, 1.85, 'El ecografista puede **describir** los hallazgos sin concluir: **el médico interpreta** y diagnostica integrando la clínica.',
            GOLD, 17, name='Médico interpreta', bold=False)
    flow_anim(s, tri, 1)
    s.step(fade(r))
    s.step(fade(w))
    s.step(fade(m))


def build(D):
    unit_start(D, 'XII', 'Neumotórax')
    div12(D)
    definicion(D)
    seq_formacion(D)
    clasificacion(D)
    clinica(D)
    unit_end(D, 'XII')
    unit_start(D, 'XIII', 'Semiología del neumotórax')
    div13(D)
    comparativa(D)
    unit_end(D, 'XIII')
    unit_start(D, 'XIV', 'Ecografía pleural')
    div14(D)
    principio(D)
    seq_deslizamiento(D)
    signos(D)
    unit_end(D, 'XIV')
