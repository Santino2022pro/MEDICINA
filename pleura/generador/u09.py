# -*- coding: utf-8 -*-
"""UNIDAD XVII (tratamiento y drenaje), XVIII (tumores pleurales), XIX (integración) y cierre."""
from base import *


def div17(D):
    def art(s):
        water_seal(s, 7.2, 1.3, 2.2, 3.6, {'bubbles': 1})
        chest(s, 9.6, 1.0, 3.4, 3.3, {'airR': 0.4}, names=False)
    divider(D, 'XVII', 'Tratamiento y drenaje torácico', 'Sacar el aire o el líquido sin dejarlo volver',
            ['Conducta según tamaño y estabilidad', 'Componentes del sistema de drenaje', 'Sello (trampa) de agua: secuencia',
             'Burbujeo y oscilación', 'Control radiológico y retiro', 'Complicaciones e iatrogenia'], art, src=['T7.1', 'T7.3', 'P3.13'])


def conducta(D):
    s = new(D, 'Tratamiento', 'Conducta según el tamaño y la estabilidad', 'mesotelio', src=['T7.1', 'P3.11', 'P3.4'])
    rows = [['SITUACIÓN', 'CONDUCTA DESCRITA EN EL MATERIAL'],
            ['Grado I (≤ 20 %) · pequeño (ACCP < 3 cm / BTS < 2 cm)', '**Observación**: O_{2} a alto flujo (acelera la reabsorción) + kinesioterapia; control clínico y radiológico (se reabsorbe en 1–2 semanas)'],
            ['Grado II (20–50 %) · grande por ACCP o BTS', '**Pleurostomía** con tubo de tórax + **trampa de agua**'],
            ['Grado III (> 50 %) · signo del muñón', 'Pleurostomía + trampa de agua ± **aspiración activa**; considerar toracoscopia o cirugía si hay recidiva o pulmón atrapado'],
            ['Neumotórax a tensión', '**Descompresión inmediata** con aguja → toracostomía con tubo']]
    ids, h = gtable(s, 0.4, 1.0, 8.6, rows, [1.5, 2.6], 14, head_fill=GOLD, fill_to=6.95)
    m = s.group_start('Monitor mini')
    s.shape(9.3, 1.0, 3.7, 2.6, 'roundRect', '1C2833', BORDER, False, adj={'adj': 8000})
    for i, (k, c) in enumerate((('FR', '58D68D'), ('FC', 'F4D03F'), ('TA', 'EC7063'), ('SpO_{2}', '5DADE2'))):
        s.shape(9.5 + (i % 2) * 1.75, 1.2 + (i // 2) * 1.15, 1.55, 0.95, 'rect', None, (c, 2), False, k, 20, F_HEAD, c, True, 'c', 'm', fit=False)
    s.group_end()
    w = box(s, 9.3, 3.8, 3.7, 3.15, 'El tamaño **solo no decide**: la **estabilidad hemodinámica** (FR, FC, TA, SpO_{2}) puede indicar evacuar un neumotórax '
            'pequeño.', RED, 14, name='Estabilidad decide', bold=False)
    table_anim(s, ids, 1)
    s.step(fade(m))
    s.step(fade(w))
    s.note('Los porcentajes por grado y la indicación de kinesioterapia provienen de una de las fuentes; los criterios ACCP/BTS de la otra. '
           'Se presentan juntos sin asumir equivalencia (ver auditoría).')


def seq_sello(D):
    Q = Seq(D, 'Funcionamiento del sello de agua (Unidad XVII)', '!!PulmonDerecho, !!AirePleuralD, !!TuboDrenaje, !!Frasco, !!SelloAgua, '
            '!!TuboSumergido, !!ColumnaAgua, !!Burbujas, !!Ventilacion, !!Leyenda', 'Aparece el sistema, el aire viaja por el tubo, burbujea '
            'bajo el agua y sale al exterior; el agua sube en el tubo en inspiración (sin reentrada) y el pulmón se reexpande.')
    st = [('Espacio pleural', {'airR': 0.6, 'hl': {'AirePleuralD'}}, {}, 'Aire acumulado en el espacio pleural que hay que evacuar.', 0),
          ('Sistema de drenaje', {'airR': 0.6}, {}, 'Un **frasco** con **doble tubuladura**: un tubo desde el paciente y otro de salida al exterior.', 1),
          ('Tubo', {'airR': 0.6}, {}, 'El **tubo de drenaje** comunica el espacio pleural con el frasco.', 2),
          ('Recipiente', {'airR': 0.6}, {'hl': {'Frasco'}}, 'El tubo del paciente desciende dentro del recipiente.', 2),
          ('Agua', {'airR': 0.6}, {'hl': {'SelloAgua'}}, 'Su **extremo queda sumergido bajo el agua**: el agua **sella** el sistema.', 2),
          ('Movimiento de aire', {'airR': 0.5}, {}, 'En la espiración (o con la tos) la presión pleural supera a la del frasco: el aire **baja por el tubo**.', 2),
          ('Salida de aire', {'airR': 0.35}, {'bubbles': 1}, 'El aire **burbujea** a través del agua y sale por el tubo de **abocamiento al exterior**.', 2),
          ('Prevención de la reentrada', {'airR': 0.3}, {'osc': 1}, 'En la inspiración el agua **sube** por el tubo: hace de **válvula unidireccional**; el aire **no vuelve**.', 2),
          ('Recuperación de la expansión', {'airR': 0.04}, {'osc': 0.3}, 'Sin aire pleural el pulmón se **reexpande**: cesa el burbujeo; el nivel sigue **oscilando**.', 2)]
    for i, (ttl, cst, wst, cap, lvl) in enumerate(st):
        s = new(D, 'Drenaje', ttl, 'azul', morph=i > 0, src=['T7.3', 'P3.13', 'T7.1'])
        A = chest(s, 3.4, 0.95, 5.7, 5.55, cst)
        F = A['F']
        step_badge(s, i + 1, len(st))
        W = None
        if lvl >= 1:
            W = water_seal(s, 0.35, 1.85, 2.75, 4.65, wst)
        if lvl >= 2:
            p0 = W['pt_tube_top']
            pts = [p0, (p0[0], 1.42), F.p(30, 300), F.p(175, 300)]
            tb = s.arrow(pts, 'C8D6E5', 9, tail=None, name='!!TuboDrenaje')
            tb2 = s.arrow(pts, '5D6D7E', 2, tail=None, name='!!TuboDrenajeBorde', dash='dash')
        lg = legend(s, cap, 9.35, 1.0, 3.65, h=2.5, size=15)
        if i == 1:
            fr = s.group_start('Rótulos frasco')
            tag(s, 0.35, 1.35, 'FRASCO · DOBLE TUBULADURA', WHITE, 12, w=2.75)
            s.group_end()
            s.step(fade(fr))
        if i == 2:
            s.step(wipe(tb, 'l', dur=800))
        if i == 3:
            s.step(pulse(W['frasco']))
        if i == 4:
            co = callout(s, [W['pt_tip'], (9.35, 4.0)], 'Extremo bajo el agua', 9.35, 3.75, 3.65, 0.55, C_FLUID, 14)
            s.step(fade(co), pulse(W['agua'], after=True))
        if i == 5:
            dots = [s.shape(F.p(175, 300)[0] - 0.1, F.p(0, 300)[1] - 0.1, 0.2, 0.2, 'ellipse', 'FFFFFF', ('1B4F72', 1.5), False, name='Aire %d' % k)
                    for k in range(3)]
            dx = W['pt_tube_top'][0] - F.p(175, 300)[0]
            s.step(*[path(d, dx, W['pt_tube_top'][1] + 1.2 - F.p(0, 300)[1], after=False, delay=k * 250, dur=1200, pts=[(-(F.p(175, 300)[0] - F.p(30, 300)[0]), 0),
                                                                                  (dx, 1.42 - F.p(0, 300)[1])]) for k, d in enumerate(dots)])
        if i == 6:
            s.step(path(W['bub'], 0, -1.2, dur=900))
            vent = s.arrow([W['pt_vent'], (W['pt_vent'][0], W['pt_vent'][1] - 0.5)], '1B4F72', 4, name='Salida exterior')
            s.step(wipe(vent, 'b'))
        if i == 7:
            s.step(path(W['col'], 0, -0.3, dur=700))
            x = s.shape(W['pt_tip'][0] - 0.25, W['pt_tip'][1] - 1.4, 0.5, 0.5, 'mathMultiply', RED, (INK, 1), False, name='Sin reentrada')
            s.step(zoom(x))
        if i == 0:
            q = box(s, 0.35, 1.85, 2.75, 4.65, '¿Cómo **evacuar** el aire sin que **vuelva a entrar**?', WHITE, 17, name='Pregunta')
            s.step(fade(q))
        extra = {0: ('Objetivo', 'Evacuar el aire (o el líquido) y permitir la **reexpansión** pulmonar.', CEL),
                 1: ('Doble tubuladura', 'Tubo largo **del paciente** (sumergido) y tubo corto de **abocamiento al exterior**.', CEL),
                 2: ('Pleurostomía', 'El tubo de tórax se coloca en el espacio pleural.', LBLUE),
                 3: ('Recipiente', 'Transparente: permite **ver** el burbujeo y la oscilación del nivel.', WHITE),
                 4: ('Sello', 'Sin el agua, el aire podría **reingresar** al tórax.', GREEN),
                 5: ('Dirección', 'El aire va de la zona de **mayor** a la de **menor** presión.', GOLD),
                 6: ('Burbujeo', 'Burbujeo **permanente** = sigue saliendo aire.', GOLD),
                 7: ('Oscilación', 'El nivel sube y baja con la respiración: **oscilación normal** = sistema permeable.', GREEN),
                 8: ('Sin oscilación', 'Tubo **tapado** o pulmón **totalmente expandido**.', ORANGE)}
        if i in extra:
            h, t, c = extra[i]
            b = box(s, 9.35, 4.45 if i == 4 else 3.7, 3.65, 2.5 if i == 4 else 3.25, t, c, 15, head=h, headfill=WHITE, bold=False)
            s.step(fade(b))
    Q.close()


def control(D):
    s = new(D, 'Drenaje', 'Control del drenaje y complicaciones', 'torax', src=['P3.13', 'P2.16', 'T7.3'])
    r1 = rx(s, 0.4, 1.0, 2.9, 2.9, {'airR': 0.4}, prefix='C1 ')
    r2 = rx(s, 3.5, 1.0, 2.9, 2.9, {'airR': 0.03}, prefix='C2 ')
    ar = s.arrow([(3.05, 2.45), (3.75, 2.45)], GOLD, 6, name='Evolución')
    tag(s, 0.4, 4.0, 'Inicio', WHITE, 13, w=2.9); tag(s, 3.5, 4.0, 'Reexpandido', WHITE, 13, w=2.9)
    cs = two_cards(s, [('Burbujeo', 'Su presencia confirma que **sigue saliendo aire**.', GOLD),
                       ('Abocamiento', 'El tubo de salida **debe estar abierto al exterior**.', CEL),
                       ('Rx de control', 'Radiografías **periódicas** para seguir la **reexpansión**.', LBLUE),
                       ('Retiro a tiempo', 'Si el tubo no se retira cuando el pulmón se reexpandió, **puede volver a punzarlo**.', RED)], 6.7, 1.0, 6.3, 5.95, 0.15, 14.5)
    n = box(s, 0.4, 4.55, 6.0, 2.4, 'Iatrogenia del procedimiento: neumotórax por punción, **hemotórax**, hidroneumotórax, **edema de reexpansión** (Unidad VIII).',
            ORANGE, 14, name='Iatrogenia drenaje', bold=False)
    s.step(wipe(ar, 'l'))
    reveal(s, cs, 1)
    s.step(fade(n))


# ------------------------------------------------------------------ UNIDAD XVIII
def div18(D):
    def art(s):
        chest(s, 7.0, 0.6, 3.1, 3.0, {'rind': 1, 'fluidR': 0.3, 'exud': 1}, names=False)
        rx(s, 10.2, 0.65, 2.9, 2.95, {'nodules': 1}, prefix='Arte Rx')
        pleura_zoom(s, 7.0, 3.85, 3.0, 3.0, {'gap': 0.25, 'tumor': 'meta', 'kind': 'blood'})
        pleura_zoom(s, 10.2, 3.85, 2.9, 3.0, {'gap': 0.4, 'tumor': 'tfs'})
    divider(D, 'XVIII', 'Tumores pleurales', 'Primarios, secundarios y benignos',
            ['Clasificación', 'Desarrollo de un tumor pleural (secuencia)', 'Mesotelioma pleural maligno', 'Metástasis y derrame maligno',
             'Imagen en «suelta de globos»', 'Tumor fibroso solitario'], art, src=['T8.1', 'T8.2', 'T8.3', 'T8.4', 'T5.2'])


def clasif_tum(D):
    s = new(D, 'Tumores', 'Clasificación de los tumores pleurales', 'mesotelio', src=['T8.1'])
    rows = [['TIPO', 'SUBTIPO', 'DESCRIPCIÓN'],
            ['Primario maligno', '**Mesotelioma**', 'El más frecuente de los **primarios** de la pleura; células **mesoteliales**'],
            ['Primario benigno', 'Varios (raros)', 'Incluye el **tumor fibroso solitario**'],
            ['Metastásico', 'Metástasis', '**Causa más frecuente** de tumor pleural; por contigüidad, vía hematógena o linfática'],
            ['Otros', 'Tumor fibroso solitario', 'Benigno; origen en **fibroblastos subpleurales**; tratamiento quirúrgico']]
    ids, h = gtable(s, 0.4, 1.0, 8.2, rows, [1.1, 1.2, 2.5], 14, head_fill=LILAC, fill_to=6.95)
    z = [pleura_zoom(s, 8.9, 1.0, 4.1, 1.9, {'gap': 0.15, 'tumor': 'meso'}),
         pleura_zoom(s, 8.9, 3.0, 4.1, 1.9, {'gap': 0.25, 'tumor': 'meta', 'kind': 'blood'}),
         pleura_zoom(s, 8.9, 5.0, 4.1, 1.95, {'gap': 0.45, 'tumor': 'tfs'})]
    for k, t in enumerate(('Mesotelioma: engrosamiento difuso nodular', 'Metástasis: nódulos múltiples', 'Tumor fibroso: masa única pediculada')):
        tag(s, 8.95, 1.05 + k * 2.0, t, WHITE, 11, w=4.0)
    table_anim(s, ids, 1)


def seq_tumor(D):
    Q = Seq(D, 'Desarrollo de un tumor pleural (mesotelioma) (Unidad XVIII)', 'Tórax: !!PulmonDerecho, !!Mesotelioma, !!LiquidoPleuralD · Corte: '
            '!!PleuraParietal, !!PleuraVisceral, !!LiquidoPleural, !!Leyenda', 'Una región de la pleura se engrosa, crece en forma nodular difusa, '
            'envuelve las superficies, se acumula líquido y el pulmón queda comprimido y restringido.')
    st = [({}, {'gap': 0.05}, 'Pleura normal', 'Hojas pleurales delgadas, revestidas por **células mesoteliales**.', None),
          ({'hl': {'PleuraParietalD'}}, {'gap': 0.05, 'hl': {'PleuraParietal'}}, 'Región afectada', 'El mesotelioma se origina en las **células mesoteliales** de la pleura.',
           ('Factor de riesgo', 'Exposición laboral al **asbesto** (amianto); latencia de **20–40 años**.', GOLD)),
          ({'rind': 0.3}, {'gap': 0.06, 'tumor': 'meso'}, 'Lesión tumoral', 'Aparecen engrosamientos **nodulares** en la hoja parietal.', None),
          ({'rind': 0.6}, {'gap': 0.1, 'tumor': 'meso'}, 'Crecimiento', 'El tumor **crece en superficie**: engrosamiento **difuso y nodular**.', None),
          ({'rind': 0.8}, {'gap': 0.12, 'tumor': 'meso'}, 'Alteración de las superficies', 'Ambas hojas pierden su superficie lisa: el **deslizamiento** se altera.', None),
          ({'rind': 1}, {'gap': 0.14, 'tumor': 'meso', 'inflam': 1}, 'Compromiso local', 'Invade la pared: **dolor torácico** (síntoma principal y precoz).',
           ('Dolor', 'La hoja **parietal** está inervada.', ORANGE)),
          ({'rind': 1, 'fluidR': 0.35, 'exud': 1}, {'gap': 0.45, 'tumor': 'meso', 'kind': 'exud', 'prot': 20}, 'Acumulación de líquido',
           'Derrame **exudado**, característicamente **viscoso**.', ('Líquido', 'Viscoso · exudado · citología positiva.', C_EXUD)),
          ({'rind': 1, 'fluidR': 0.55, 'exud': 1}, {'gap': 0.55, 'tumor': 'meso', 'kind': 'exud', 'prot': 25}, 'Consecuencias mecánicas',
           'El pulmón queda **comprimido y encarcelado**: **disnea insidiosa** progresiva.', ('Disnea', 'Progresiva, por el derrame y la restricción.', CEL)),
          ({'rind': 1, 'fluidR': 0.55, 'exud': 1}, {'gap': 0.55, 'tumor': 'meso', 'kind': 'exud', 'prot': 25}, 'Hallazgos diagnósticos',
           'TAC: engrosamiento pleural **difuso nodular** + derrame importante → **biopsia pleural** (confirmatoria).', ('Diagnóstico', 'TAC de tórax + biopsia.', LBLUE))]
    for i, (cst, zst, ttl, cap, card) in enumerate(st):
        s = new(D, 'Tumores', ttl, 'azul', morph=i > 0, src=['T8.2', 'T8.1'])
        A = chest(s, 0.25, 0.95, 4.8, 4.7, cst)
        Z = pleura_zoom(s, 5.25, 0.95, 4.2, 4.7, zst)
        step_badge(s, i + 1, len(st))
        tag(s, 0.25, 5.75, 'TÓRAX', WHITE, 13, w=1.4); tag(s, 5.25, 5.75, 'CORTE DE LAS HOJAS', WHITE, 13, w=2.6)
        lg = legend(s, cap, 0.25, 6.25, 9.2, h=0.8, size=15)
        if i == 8:
            C = ct_axial(s, 9.7, 0.95, 3.35, 3.2, {'thick': 1, 'fluidR': 0.35}, prefix='!!TAC')
            c = box(s, 9.7, 4.3, 3.35, 2.75, card[1], card[2], 15, head=card[0], headfill=WHITE, bold=False)
            s.step(fade(c))
        else:
            if card:
                c = box(s, 9.7, 0.95, 3.35, 3.0, card[1], card[2], 15, head=card[0], headfill=WHITE, bold=False)
                s.step(fade(c))
            info = ['El tumor más frecuente de la pleura es la **metástasis**; el primario maligno más frecuente, el **mesotelioma**.',
                    '', 'Las otras neoplasias pleurales **no** comparten esta morfología (ver diapositivas siguientes).', 'Crecimiento **en manto** sobre la pleura.',
                    'Engrosamiento que puede **englobar** el pulmón.', '', '', '']
            if info[i]:
                b = box(s, 9.7, 4.1 if card else 0.95, 3.35, 2.95 if card else 6.1, info[i], WHITE, 15, name='Dato tumor', bold=False)
                s.step(fade(b))
    Q.close()


def mesotelioma(D):
    s = new(D, 'Tumores', 'Mesotelioma pleural maligno: lo esencial', 'rosa', src=['T8.2'])
    A = chest(s, 0.3, 0.95, 4.4, 4.3, {'rind': 1, 'fluidR': 0.45, 'exud': 1})
    t = tube(s, 1.95, 5.35, 0.65, 1.3, 'C9B07A', None, 'viscous', name='Tubo viscoso')
    cs = [box(s, 4.9, 1.0, 4.0, 2.9, 'Más frecuente en **hombres de 40–70 años**. **Trabajadores del asbesto**: principal factor de riesgo; latencia **20–40 años**.',
              GOLD, 13.5, head='Epidemiología', headfill=WHITE, bold=False),
          box(s, 9.05, 1.0, 3.95, 2.9, '**Dolor torácico** (principal y precoz) · **disnea insidiosa** · pérdida de peso, tos seca.', ORANGE, 14,
              head='Clínica', headfill=WHITE, bold=False),
          box(s, 4.9, 4.05, 4.0, 2.9, 'Líquido **viscoso**, **exudado**, **citología positiva**. TAC: engrosamiento **difuso nodular** + derrame. **Biopsia** confirma.',
              LBLUE, 13.5, head='Diagnóstico', headfill=WHITE, bold=False),
          box(s, 9.05, 4.05, 3.95, 2.9, 'Muy agresivo; sobrevida media **< 12–18 meses**; **sin tratamiento curativo** (paliativo).', RED, 14,
              head='Pronóstico', headfill=WHITE, bold=False)]
    reveal(s, cs, 1)
    s.note('El material atribuye también al mesotelioma hipoglucemias intermitentes y osteoartropatía hipertrófica (acropaquias, uñas en vidrio '
           'de reloj). Ambas manifestaciones se describen clásicamente en el tumor fibroso solitario: el dato se registra para revisión y no '
           'se muestra como rasgo del mesotelioma.')


def metastasis(D):
    s = new(D, 'Tumores', 'Metástasis pleurales y derrame maligno', 'rosa', src=['T8.3', 'T5.2', 'T8.1'])
    Z = pleura_zoom(s, 0.3, 0.95, 4.6, 4.2, {'gap': 0.4, 'tumor': 'meta', 'kind': 'blood'})
    t = tube(s, 2.2, 5.3, 0.7, 1.4, 'B22222', None, 'blood', name='Tubo hemorrágico')
    cs = [box(s, 5.1, 1.0, 3.9, 2.9, '**Causa más frecuente** de derrame pleural maligno. Llegan por **contigüidad**, vía **hematógena** o **linfática**.', LILAC, 14,
              head='Concepto', headfill=WHITE, bold=False),
          box(s, 9.15, 1.0, 3.85, 2.9, 'Cáncer de **mama**, **pulmón**, **linfomas**, **próstata**.', GOLD, 14.5, head='Primarios citados', headfill=WHITE, bold=False),
          box(s, 5.1, 4.05, 3.9, 2.9, '**LDH elevada** · líquido **hemorrágico** (> 50 %) · **citología positiva** (~60 %), estudio principal.', C_EXUD, 14,
              head='Líquido', headfill=WHITE, bold=False),
          box(s, 9.15, 4.05, 3.85, 2.9, 'Citología negativa con alta sospecha → **biopsia pleural** (aguja guiada por TAC o toracoscopia); inmunohistoquímica para el origen.',
              CEL, 13.5, head='Si la citología es negativa', headfill=WHITE, bold=False)]
    reveal(s, cs, 1)
    s.note('El orden de frecuencia de los tumores primarios difiere entre apartados del material (mama primero en uno; distinto orden en otro) y '
           'una fuente describe «proteínas bajas» como paradoja del exudado maligno. Ambos puntos se registran en la auditoría.')
    s = new(D, 'Tumores', 'Imagen en «suelta de globos»', 'azul', src=['T8.3'])
    R = rx(s, 0.4, 0.95, 6.0, 6.0, {'nodules': 1})
    cs = two_cards(s, [('Imagen', 'Múltiples **opacidades redondeadas** de distintos tamaños en **ambos campos**, como globos sueltos.', LBLUE),
                       ('Significado', 'Característica de metástasis por vía **hematógena**.', GOLD),
                       ('Precisión', 'Es un signo de **nódulos pulmonares** (parénquima); el compromiso **pleural** se evalúa además con TAC y derrame. '
                        'Su atribución a «metástasis pleurales» está **en revisión**.', RED)], 6.7, 1.0, 6.3, 5.95, 0.15, 14.5)
    s.step(fade(R['nod']))
    reveal(s, cs, 1)


def tfs(D):
    s = new(D, 'Tumores', 'Tumor fibroso solitario de la pleura', 'rosa', src=['T8.4', 'T8.1'])
    A = chest(s, 0.3, 0.95, 4.3, 4.2, {'mass': (210, 620, 75)})
    Z = pleura_zoom(s, 0.3, 5.25, 4.3, 1.75, {'gap': 0.45, 'tumor': 'tfs'})
    cs = [box(s, 4.85, 1.0, 4.05, 2.9, 'Tumor **benigno**. Origen en **fibroblastos subpleurales**, no en células mesoteliales.', LGREEN, 14.5,
              head='Naturaleza', headfill=WHITE, bold=False),
          box(s, 9.05, 1.0, 3.95, 2.9, 'Masa **solitaria**, **bien delimitada**, redondeada, **sin derrame** asociado.', LBLUE, 14.5, head='Imagen', headfill=WHITE, bold=False),
          box(s, 4.85, 4.05, 4.05, 2.9, 'Puede asociarse a **hipoglucemia paraneoplásica** y **osteoartropatía hipertrófica**.', ORANGE, 14.5,
              head='Asociaciones', headfill=WHITE, bold=False),
          box(s, 9.05, 4.05, 3.95, 2.9, '**Quirúrgico** (resección completa): buen pronóstico si se reseca completamente.', GOLD, 14.5,
              head='Tratamiento', headfill=WHITE, bold=False)]
    reveal(s, cs, 1)


# ------------------------------------------------------------------ UNIDAD XIX
def div19(D):
    def art(s):
        for i, st in enumerate(({'fluidR': 0.5}, {'airR': 0.6}, {'fluidR': 0.45, 'pus': 1, 'septa': 1}, {'airR': 0.92, 'shift': 85, 'cava': 0.8, 'heart': 1})):
            chest(s, 7.0 + (i % 2) * 3.05, 0.7 + (i // 2) * 3.05, 2.9, 2.85, st, names=False)
    divider(D, 'XIX', 'Integración clínica', 'Cuatro comparaciones para decidir',
            ['Derrame pleural frente a neumotórax', 'Trasudado frente a exudado', 'Derrame simple, complicado y empiema',
             'Neumotórax simple frente a neumotórax a tensión', 'Cadena diagnóstica', 'Mensajes finales'], art, src=['T9.1', 'T9.2', 'P4.1'])


def comp(D, ttl, left, right, rows, src, lbl, cols=(C_FLUID, C_AIR), bg='blanco', rxs=True):
    s = new(D, 'Integración', ttl, bg, src=src)
    a = chest(s, 0.2, 1.0, 3.3, 3.25, left, names=False)
    b = chest(s, 9.8, 1.0, 3.3, 3.25, right, names=False)
    tag(s, 0.2, 4.3, lbl[0], cols[0], 14, w=3.3)
    tag(s, 9.8, 4.3, lbl[1], cols[1], 14, w=3.3)
    if rxs:
        ra = rx(s, 0.75, 4.8, 2.2, 2.15, left, prefix='Comp Rx izq ')
        rb = rx(s, 10.35, 4.8, 2.2, 2.15, right, prefix='Comp Rx der ')
    n = len(rows)
    hh = min(0.85, 5.95 / n - 0.06)
    ids = []
    for i, (k, l, r) in enumerate(rows):
        y = 1.0 + i * (hh + 0.06)
        g = s.group_start('Fila ' + k)
        box(s, 3.65, y, 2.35, hh, l, cols[0], 12.5, bold=False, grow=False)
        box(s, 6.05, y, 1.5, hh, smart_upper(k), WHITE, 11.5, grow=False)
        box(s, 7.6, y, 2.05, hh, r, cols[1] if cols[1] != C_AIR else 'EAF6FB', 12.5, bold=False, grow=False)
        ids.append(s.group_end())
    reveal(s, ids, 1)
    return s


def integracion(D):
    s = comp(D, 'Derrame pleural frente a neumotórax', {'fluidR': 0.5}, {'airR': 0.6},
             [('Contenido', '**Líquido**', '**Aire**'), ('Mecanismo', 'Starling / permeabilidad / linfa', 'Rotura de bula, trauma, iatrogenia'),
              ('Presiones', 'El líquido ocupa volumen', 'Se pierde la presión negativa'), ('Ventilación', 'Compresión del pulmón', 'Retracción / colapso'),
              ('Percusión', '**Matidez** hídrica', '**Hipersonoridad**'), ('Auscultación', '↓ MV · soplo tubario', 'Ausencia MV · soplo anfórico'),
              ('Radiografía', 'Opacidad · Damoiseau · seno borrado', 'Hiperclaridad · línea pleural · sin trama'),
              ('Emergencia', 'Derrame masivo', 'Neumotórax a tensión')], ['T9.1', 'T6.4'], ('DERRAME', 'NEUMOTÓRAX'), rxs=False)
    w = box(s, 0.2, 4.85, 3.3, 2.1, 'Tráquea en el derrame: «hacia el lado afectado o central» figura en una tabla, pero el derrame **masivo** la desplaza al '
            'lado **sano**: revisar.', RED, 11.5, name='Tráquea revisar', bold=False, grow=False)
    rb = rx(s, 10.35, 4.8, 2.2, 2.15, {'airR': 0.6}, prefix='Comp Rx der ')
    s.step(fade(w))
    comp(D, 'Trasudado frente a exudado', {'fluidR': 0.3, 'fluidL': 0.27}, {'fluidR': 0.45, 'exud': 1},
         [('Mecanismo', '↑ P_{c} / ↓ π_{c}', '↑ permeabilidad / ↓ linfa'), ('Pleura', 'Sana (sistémico)', 'Enferma (local)'),
          ('Proteínas pl/sér', '≤ 0,5', '> 0,5'), ('LDH pl/sér', '≤ 0,6', '> 0,6'), ('LDH absoluta', '< 2/3 LSN', '> 2/3 (o ≥) LSN'),
          ('Aspecto', 'Claro, seroso', 'Turbio, lechoso, hemorrágico, purulento'), ('Células', 'Pocas; macrófagos', 'PMN o linfocitos'),
          ('Causas', 'ICC, cirrosis, nefrótico', 'Neumonía, TBC, tumor, colagenopatías, pancreatitis')], ['T9.2', 'T4.2'], ('TRASUDADO', 'EXUDADO'),
         (C_FLUID, C_EXUD))
    comp(D, 'Derrame paraneumónico simple, complicado y empiema', {'fluidR': 0.3, 'exud': 1, 'consol': (250, 560, 100)},
         {'fluidR': 0.45, 'pus': 1, 'septa': 1, 'consol': (250, 560, 100)},
         [('Líquido', 'Exudado **estéril**', 'Infectado → **pus**'), ('Gram / cultivo', 'Negativos', '**Positivos**'), ('pH', '> 7,20', '< 7,2'),
          ('Glucosa', 'Normal', '< 60 (complicado) · < 40 (empiema, formulación 1)'), ('LDH', '< 1000', '> 1000 (empiema)'),
          ('Aspecto', 'Seroso / turbio', 'Turbio / **purulento**, tabicado'), ('Resolución', 'Antibióticos', '**Drenaje** + antibióticos')],
         ['T5.1', 'P2.14'], ('NO COMPLICADO', 'COMPLICADO · EMPIEMA'), (C_EXUD, C_PUS))
    comp(D, 'Neumotórax simple frente a neumotórax a tensión', {'airR': 0.5}, {'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'heart': 1},
         [('Mecanismo', 'Aire que entra y se equilibra', '**Válvula unidireccional**'), ('Presión pleural', 'Cercana a la atmosférica', '**Positiva**'),
          ('Mediastino', 'Central', 'Desplazado al **lado sano**'), ('Retorno venoso', 'Conservado', '**↓** (cavas comprimidas)'),
          ('Hemodinamia', 'Estable', '**Taquicardia, hipotensión, yugulares ingurgitadas**'), ('Diagnóstico', 'Clínica + imagen', '**Clínico** (no esperar Rx)'),
          ('Conducta', 'Según tamaño y estabilidad', '**Descompresión inmediata** → toracostomía')], ['T6.3', 'T7.2', 'P3.14'], ('SIMPLE', 'A TENSIÓN'),
         ('EAF6FB', RED))


def cierre(D):
    s = new(D, 'Integración', 'La cadena diagnóstica', 'torax', src=['P4.1', 'P1.1'])
    res = flow(s, ['SÍNTOMA / SIGNO', 'SÍNDROME', 'FISIOPATOLOGÍA', 'ETIOLOGÍA', 'TRATAMIENTO'], 0.4, 1.0, 12.6, 1.3,
               [WHITE, CEL, GREEN, GOLD, ORANGE], 15, 0.3)
    ex = [('Derrame', 'Disnea + matidez + frémito abolido → ocupación líquida → Starling/permeabilidad → ICC o neumonía → diuréticos o drenaje', C_FLUID),
          ('Neumotórax', 'Dolor + hipersonoridad + MV abolido → ocupación aérea → pérdida de presión negativa → bula/trauma/iatrogenia → observar o drenar', 'EAF6FB'),
          ('Tensión', 'Disnea + hipotensión + yugulares + desviación traqueal → shock obstructivo → válvula → descompresión inmediata', 'F5B7B1')]
    ids = [box(s, 0.4, 2.6 + i * 1.12, 12.6, 1.0, '**%s:** %s' % (h, t), c, 14, name='Ejemplo ' + h, bold=False, align='l') for i, (h, t, c) in enumerate(ex)]
    m = box(s, 0.4, 6.0, 12.6, 0.95, '**No existe el cuadro puro** · **nunca la imagen sola** · vigilar al paciente después de cada procedimiento.', RED, 16, name='Mensajes')
    flow_anim(s, res, 1)
    reveal(s, ids, 1)
    s.step(zoom(m))
    s = D.new(BG['portada']); s.src = []; s.tagname = 'Cierre'
    A = chest(s, 7.2, 0.55, 6.0, 5.9, {})
    t = s.text(0.5, 1.4, 6.6, 1.8, 'ENFERMEDADES\nPLEURALES', 48, F_TITLE, INK, True, 'c', 'm', name='Título', lnspc=0.88)
    b = box(s, 0.8, 3.45, 6.0, 1.9, 'Dos hojas, un espacio virtual y una presión negativa: cuando el espacio se llena de **líquido**, **pus** o **aire**, '
            'cambian la mecánica, la semiología y las imágenes.', CEL, 15, name='Síntesis final', bold=False)
    c = box(s, 1.9, 5.6, 3.8, 0.6, 'FIN DE LA CLASE', GOLD, 16, name='Fin')
    s.step(fade(t), fade(b, after=True))
    s.step(zoom(c))


def build(D):
    unit_start(D, 'XVII', 'Tratamiento y drenaje torácico')
    div17(D)
    conducta(D)
    seq_sello(D)
    control(D)
    unit_end(D, 'XVII')
    unit_start(D, 'XVIII', 'Tumores pleurales')
    div18(D)
    clasif_tum(D)
    seq_tumor(D)
    mesotelioma(D)
    metastasis(D)
    tfs(D)
    unit_end(D, 'XVIII')
    unit_start(D, 'XIX', 'Integración clínica')
    div19(D)
    integracion(D)
    cierre(D)
    unit_end(D, 'XIX')
