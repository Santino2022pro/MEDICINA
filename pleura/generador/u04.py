# -*- coding: utf-8 -*-
"""UNIDAD VI — Semiología del derrame pleural."""
from base import *


def div6(D):
    def art(s):
        A = chest(s, 7.0, 0.6, 6.0, 5.9, {'fluidR': 0.5})
        hand(s, 6.6, 3.9, 1.5, name='Arte mano')
        stetho(s, 11.6, 1.6, 0.6, name='Arte estetoscopio')
    divider(D, 'VI', 'Semiología del derrame pleural', 'Cada signo, explicado por la anatomía que lo produce',
            ['Síntomas según el volumen', 'Dificultad respiratoria: nivel anatómico', 'Inspección y palpación',
             'Vibraciones vocales (frémito)', 'Percusión: matidez', 'Auscultación e integración de hallazgos'], art,
            src=['T3.1', 'T3.2', 'P2.7', 'P2.8'])


def sintomas(D):
    s = new(D, 'Semiología', 'Los síntomas dependen del grado del derrame', 'torax', src=['T3.1', 'P3.2'])
    a = chest(s, 0.3, 1.0, 3.8, 3.7, {'fluidR': 0.13})
    b = chest(s, 0.3, 4.75, 2.55, 2.45, {'fluidR': 0.55}, names=False)
    t1 = box(s, 4.3, 1.0, 3.7, 2.4, '**Asintomático**. No comprime el pulmón de forma significativa: **hallazgo incidental** en la radiografía.',
             C_FLUID, 15, head='Grado leve (pequeño)', headfill=WHITE, bold=False)
    cards = [('Disnea', 'Cuando el derrame ocupa **más de 1/3** del hemitórax: menos pulmón disponible para ventilar.', CEL),
             ('Dolor pleurítico', '**Puntada de costado** que aumenta con la **inspiración** y la **tos**: inflamación de la hoja **parietal** (inervada).', ORANGE),
             ('Tos seca', 'Irritativa, sin expectoración: irritación de **receptores pleurales**.', TURQ),
             ('Trepopnea', 'Disnea que **mejora en decúbito lateral** sobre el **lado del derrame**.', GOLD)]
    cs = [box(s, 8.25 + (i % 2) * 2.45, 1.0 + (i // 2) * 2.0, 2.35, 1.9, t, c, 13, head=h, headfill=WHITE, bold=False) for i, (h, t, c) in enumerate(cards)]
    t2 = box(s, 4.3, 3.6, 3.7, 1.0, 'GRADO MODERADO – GRAVE →', ORANGE, 16, name='Moderado grave')
    w = box(s, 3.0, 5.0, 10.0, 1.95, 'El **origen de la tos** (hoja visceral o receptores de la parietal) y el **mecanismo de la trepopnea** están '
            '**en revisión** (Auditoría científica).',
            RED, 13.5, name='Revisión síntomas', bold=False)
    s.step(fade(t1))
    s.step(fade(t2))
    reveal(s, cs, 1)
    s.step(fade(w))


def dificultad(D):
    s = new(D, 'Semiología', 'Dificultad respiratoria: ¿en qué nivel anatómico?', 'rosa', src=['P2.9'])
    A = chest(s, 0.3, 0.95, 5.6, 5.5, {})
    F = A['F']
    Z = pleura_zoom(s, 6.1, 4.3, 2.6, 2.7, {'gap': 0.05})
    lv = [('Vía aérea alta', 'laringe, tráquea, cuerdas vocales', F.p(500, 90)), ('Bronquios', 'principales o secundarios', F.p(445, 395)),
          ('Bronquiolo', 'dificultad de ingreso de aire', F.p(260, 380)), ('Membrana alvéolo-capilar', 'intercambio gaseoso', F.p(230, 560)),
          ('Alvéolo', 'el espacio aéreo propiamente dicho', F.p(200, 650))]
    ids = []
    for i, (h, t, pt) in enumerate(lv):
        y = 1.0 + i * 0.66
        g = s.group_start('Nivel %d' % (i + 1))
        badge(s, 6.15, y + 0.05, i + 1, 0.48)
        box(s, 6.75, y, 6.25, 0.58, '**%s** · %s' % (h, t), [WHITE, PALE][i % 2], 14, bold=False, align='l')
        s.arrow([(6.15, y + 0.29), pt], '1F4E79', 1.75, tail='oval')
        ids.append(s.group_end())
    w = box(s, 8.95, 4.4, 4.05, 2.55, '«Dificultad respiratoria» sin nivel anatómico es una descripción incompleta: hay que **ubicarla**.',
            GOLD, 15, name='Ubicar', bold=False)
    reveal(s, ids, 1)
    s.step(fade(w))


def seq_exploracion(D):
    Q = Seq(D, 'Exploración física del derrame: del tórax normal a la integración de hallazgos (Unidad VI)',
            '!!ParedToracica, !!PulmonDerecho, !!LiquidoPleuralD, !!PleuraParietalD, !!Mediastino, !!Leyenda, !!Mano…, !!Ondas…, !!Estetoscopio',
            'El líquido aparece y sube; el pulmón se comprime; luego las manos, las ondas y el estetoscopio se superponen al mismo tórax.')
    TOT = 10
    X, Y, W, H = 0.3, 0.95, 6.5, 6.3
    def base(i, ttl, st, src):
        s = new(D, 'Exploración', ttl, 'azul', morph=i > 1, src=src)
        A = chest(s, X, Y, W, H, st)
        step_badge(s, i, TOT)
        return s, A
    # 1 normal
    s, A = base(1, 'Tórax normal: el punto de partida', {}, ['T3.2'])
    cs = two_cards(s, [('Expansión', 'Simétrica en ambos hemitórax.', CEL), ('Vibraciones', 'Se transmiten por el parénquima aireado.', GREEN),
                       ('Percusión', '**Sonoridad** pulmonar.', GOLD), ('Auscultación', '**Murmullo vesicular** conservado.', TURQ)], 7.1, 1.0, 5.9, 5.9, 0.15, 15)
    reveal(s, cs, 2)
    # 2 aparición del líquido
    s, A = base(2, 'Aparece líquido en el espacio pleural', {'fluidR': 0.15, 'hl': {'LiquidoPleuralD'}}, ['T3.2'])
    b = box(s, 7.1, 1.0, 5.9, 2.6, 'El líquido se deposita primero en las zonas **declives**: el seno costofrénico.', C_FLUID, 16, name='Declive', bold=False)
    lg = legend(s, 'Un volumen pequeño puede no dar síntomas ni signos.', 7.1, 3.8, 5.9, h=1.2)
    s.step(fade(A['ids']['fluidR']), fade(b, after=True))
    # 3 compresión
    s, A = base(3, 'El líquido comprime el pulmón', {'fluidR': 0.5}, ['T3.2', 'P2.3'])
    b = box(s, 7.1, 1.0, 5.9, 2.6, 'El pulmón subyacente queda **comprimido** y desplazado hacia el hilio; su parte superior conserva aire.',
            ORANGE, 16, name='Compresión', bold=False)
    lg = legend(s, 'En el borde superior del derrame el parénquima comprimido se **condensa**.', 7.1, 3.8, 5.9, h=1.4)
    s.step(fade(b))
    # 4 disminución de la expansión
    s, A = base(4, 'Disminución de la expansión del hemitórax', {'fluidR': 0.5}, ['T3.2'])
    F = A['F']
    ar = [arrow_lbl(s, [F.p(170, 560), F.p(110, 560)], 'poca', RED, 6, 14, name='Expansión derecha', lbg=WHITE),
          arrow_lbl(s, [F.p(780, 560), F.p(990, 560)], 'normal', '1E8449', 9, 14, name='Expansión izquierda', lbg=WHITE)]
    b = box(s, 7.1, 1.0, 5.9, 2.6, 'El lado afectado **se mueve menos**: el líquido limita la expansión pulmonar.', CEL, 16, name='Menos movimiento', bold=False)
    s.step(wipe(ar[1], 'l'), wipe(ar[0], 'r', after=True))
    s.step(fade(b))
    # 5 inspección
    s, A = base(5, 'Inspección', {'fluidR': 0.55, 'widenR': 0.6}, ['T3.2'])
    rows = [['INSPECCIÓN', 'MECANISMO'], ['**Taquipnea**; respiración superficial', 'Menor volumen ventilable'],
            ['**Abombamiento** del hemitórax afectado', 'El líquido ocupa volumen'], ['↓ **movimientos** respiratorios del lado afectado', 'Expansión limitada'],
            ['**Facie ansiosa**', 'Disnea']]
    ids, h = gtable(s, 7.1, 1.0, 5.9, rows, [1.2, 1], 14, head_fill=TURQ, first_fill=None, first_bold=False, fill_to=5.6)
    w = box(s, 7.1, 5.75, 5.9, 1.2, 'El término «batipnea» para la respiración superficial está **en revisión**.', RED, 13, name='Batipnea')
    table_anim(s, ids, 2)
    s.step(fade(w))
    # 6 palpación
    s, A = base(6, 'Palpación: expansión y vibraciones', {'fluidR': 0.55}, ['T3.2'])
    F = A['F']
    h1 = hand(s, F.p(60, 0)[0], F.p(0, 560)[1], 1.9, name='!!ManoDerecha')
    h2 = hand(s, F.p(940, 0)[0] - 1.9, F.p(0, 560)[1], 1.9, name='!!ManoIzquierda', flip=True)
    b = box(s, 7.1, 1.0, 5.9, 2.4, 'Manos apoyadas simétricamente: el pulgar del lado afectado **se separa menos** de la línea media.',
            TURQ, 15, name='Palpación técnica', bold=False)
    lg = legend(s, 'A continuación: se pide al paciente que **vocalice** («treinta y tres»).', 7.1, 3.6, 5.9, h=1.2)
    s.step(fade(h1), fade(h2))
    s.step(path(h1, -0.06, 0, dur=700), path(h2, 0.3, 0, dur=700))
    s.step(fade(b))
    # 7 vibraciones vocales
    s, A = base(7, 'Transmisión de las vibraciones vocales', {'fluidR': 0.55}, ['T3.2', 'P2.7'])
    F = A['F']
    w1 = waves(s, *F.p(500, 60), 0.15, 3, 0.13, '1F4E79', 4, (55, 125), name='!!OndasLaringe')
    w2 = waves(s, *F.p(440, 390), 0.2, 3, 0.18, '1F4E79', 4, (145, 235), name='!!OndasBronquio')
    w3 = waves(s, *F.p(330, 330), 0.35, 4, 0.2, '1E8449', 5, (155, 215), name='!!OndasAumentadas')
    w4 = waves(s, *F.p(380, 660), 0.4, 3, 0.2, '922B21', 4, (160, 200), name='!!OndasAtenuadas', dash='dash', fade_k=0.3)
    x = s.shape(*F.p(40, 600), 0.7, 0.7, 'mathMultiply', RED, (INK, 1.5), False, name='!!Abolición')
    cs = two_cards(s, [('Origen', 'Las **cuerdas vocales** vibran; la onda viaja por el **árbol bronquial**.', WHITE),
                       ('Por encima del derrame', '**Aumento** de vibraciones: el pulmón comprimido (condensado) conduce mejor.', LGREEN),
                       ('Sobre el derrame', '**Abolición**: el líquido actúa como **amortiguador** acústico.', RED)], 7.1, 1.0, 5.9, 5.9, 0.15, 14.5)
    s.step(fade(w1), fade(cs[0], after=True))
    s.step(wipe(w2, 'r'))
    s.step(wipe(w3, 'r'), fade(cs[1], after=True))
    s.step(wipe(w4, 'r'), zoom(x, after=True), fade(cs[2], after=True))
    # 8 percusión
    s, A = base(8, 'Percusión: sonoridad arriba, matidez sobre el líquido', {'fluidR': 0.55}, ['T3.2', 'P2.8'])
    F = A['F']
    px1, py1 = F.p(60, 300); px2, py2 = F.p(60, 690)
    pl1 = hand(s, px1, py1 - 0.35, 1.35, name='!!ManoPlexímetro1')
    st1 = hand(s, px1 - 0.25, py1 - 1.25, 1.0, rot=35, name='!!ManoPercutora1')
    pl2 = hand(s, px2, py2 - 0.35, 1.35, name='!!ManoPlexímetro2')
    st2 = hand(s, px2 - 0.25, py2 - 1.25, 1.0, rot=35, name='!!ManoPercutora2')
    so = waves(s, px1 + 1.35, py1 + 0.05, 0.2, 4, 0.2, '1E8449', 5, (-45, 45), name='!!OndasSonoridad')
    ma = waves(s, px2 + 1.35, py2 + 0.05, 0.15, 1, 0.1, '922B21', 4, (-25, 25), name='!!OndasMatidez')
    l1 = tag(s, px1 + 2.15, py1 - 0.15, 'SONORO', LGREEN, 15, name='Rótulo sonoro')
    l2 = tag(s, px2 + 1.75, py2 - 0.15, 'MATE', RED, 15, name='Rótulo mate')
    cs = two_cards(s, [('Matidez hídrica', 'El líquido es **denso** y no vibra como el pulmón aireado: el golpe produce **matidez**.', RED),
                       ('Signo de Koranyi', 'Columna **mate** a los lados de la columna vertebral.', ORANGE),
                       ('Signo del desnivel', 'En derrames **libres** la matidez **cambia con la posición** del paciente.', GOLD)], 7.1, 1.0, 5.9, 5.9, 0.15, 14.5)
    s.step(fade(pl1), fade(st1))
    s.step(path(st1, 0.3, 0.45, dur=350), fade(so, after=True), fade(l1, after=True))
    s.step(fade(pl2), fade(st2))
    s.step(path(st2, 0.3, 0.45, dur=350), fade(ma, after=True), fade(l2, after=True))
    reveal(s, cs, 1)
    # 9 auscultación
    s, A = base(9, 'Auscultación', {'fluidR': 0.55}, ['T3.2', 'P2.7'])
    F = A['F']
    e1 = stetho(s, *F.p(150, 300), 0.55, name='!!EstetoscopioArriba')
    e2 = stetho(s, *F.p(150, 660), 0.55, name='!!EstetoscopioAbajo')
    cs = two_cards(s, [('Sobre el derrame', '**Disminución o abolición del murmullo vesicular**: el líquido interpuesto atenúa los sonidos.', RED),
                       ('Borde superior', '**Soplo tubario**: el parénquima comprimido (condensado) transmite el sonido bronquial.', GOLD),
                       ('Columna e hilio', 'Murmullo **presente**.', LGREEN)], 7.1, 1.0, 5.9, 5.9, 0.15, 14.5)
    s.step(fade(e2), fade(cs[0], after=True))
    s.step(fade(e1), fade(cs[1], after=True))
    s.step(fade(cs[2]))
    # 10 integración
    s, A = base(10, 'Integración: el síndrome de ocupación pleural líquida', {'fluidR': 0.55}, ['T3.2', 'P2.7'])
    tri = [box(s, 7.1, 1.0 + i * 1.25, 5.9, 1.1, t, c, 17, name='Tríada %d' % i) for i, (t, c) in
           enumerate([('↓ / abolición del FRÉMITO', TURQ), ('MATIDEZ a la percusión', RED), ('↓ RUIDOS respiratorios', CEL)])]
    m = box(s, 7.1, 4.85, 5.9, 2.1, 'Tres hallazgos, **un solo mecanismo**: líquido interpuesto entre el pulmón y la pared → '
            '**síndrome** de derrame pleural.', GOLD, 15, name='Un mecanismo', bold=False)
    reveal(s, tri, 1)
    s.step(zoom(m))
    Q.close()


def matidez(D):
    s = new(D, 'Semiología', 'La matidez no es exclusiva del derrame', 'mesotelio', src=['P2.8'])
    sts = [({'fluidR': 0.45}, 'Derrame pleural', 'Líquido en el espacio pleural'),
           ({'lungcolR': 'B03A2E'}, 'Consolidación', 'Bloque neumónico: alvéolos ocupados'),
           ({'mass': (250, 450, 90)}, 'Masa tumoral', 'Tejido sólido'),
           ({'shift': -45, 'flatR': -0.7, 'lungcolR': '9E4A5A'}, 'Atelectasia', 'Colapso pulmonar sin aire')]
    gs = []
    for i, (st, h1, h2) in enumerate(sts):
        x = 0.3 + i * 3.2
        g = s.group_start('Matidez ' + h1)
        chest(s, x, 1.0, 3.0, 2.95, st, names=False)
        box(s, x, 4.05, 3.0, 0.55, h1, [C_FLUID, 'F1948A', LILAC, 'D7BDE2'][i], 16)
        box(s, x, 4.65, 3.0, 0.6, h2, WHITE, 13, bold=False)
        gs.append(s.group_end())
    w = box(s, 0.3, 5.5, 12.8, 1.45, 'Cualquiera de estas causas de matidez puede acompañarse de **derrame como complicación**: '
            'el hallazgo exige integrar frémito, auscultación e imágenes.', GOLD, 16, name='Coexistencia', bold=False)
    reveal(s, gs, 1)
    s.step(fade(w))


def tabla_examen(D):
    s = new(D, 'Semiología', 'Examen físico del derrame pleural: síntesis', 'mesotelio', src=['T3.2'])
    rows = [['MÉTODO', 'HALLAZGO', 'EXPLICACIÓN'],
            ['Síntomas', 'Disnea, tos seca, dolor en puntada de costado, trepopnea', 'El líquido comprime el pulmón y la pleura'],
            ['Inspección', 'Taquipnea, abombamiento, ↓ movimientos del lado afectado, facie ansiosa', 'Desplaza el pulmón y limita la expansión'],
            ['Palpación', '↑ VV **por encima**; **abolición** de VV sobre el derrame', 'El líquido atenúa las vibraciones de las cuerdas vocales'],
            ['Percusión', '**Matidez hídrica**; signo de Koranyi; signo del desnivel', 'El líquido es denso: matidez en lugar de sonoridad'],
            ['Auscultación', '↓ o abolición del MV; **soplo tubario** por encima; MV en columna e hilio', 'El líquido interpuesto atenúa los sonidos']]
    ids, h = gtable(s, 0.35, 1.0, 12.65, rows, [1.1, 2.6, 2.3], 14, head_fill=TURQ, fill_to=6.95)
    table_anim(s, ids, 1)


def build(D):
    unit_start(D, 'VI', 'Semiología del derrame')
    div6(D)
    sintomas(D)
    dificultad(D)
    seq_exploracion(D)
    matidez(D)
    tabla_examen(D)
    unit_end(D, 'VI')
