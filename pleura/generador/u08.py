# -*- coding: utf-8 -*-
"""UNIDAD XV (radiografía y TAC del neumotórax) y XVI (neumotórax a tensión)."""
from base import *
from u07 import manometro


def div15(D):
    def art(s):
        rx(s, 7.1, 0.8, 3.0, 3.0, {'airR': 0.6}, prefix='Arte Rx1')
        rx(s, 10.2, 0.8, 2.9, 3.0, {'atelR': 1, 'shift': -50, 'flatR': -0.8}, prefix='Arte Rx2')
        ct_axial(s, 8.5, 4.0, 3.0, 2.9, {'airR': 0.6}, prefix='Arte TAC')
    divider(D, 'XV', 'Radiografía y TAC del neumotórax', 'Leer la imagen con orden',
            ['Orden de lectura', 'Formación de la imagen (secuencia)', 'Tamaño: grados y criterios ACCP/BTS', 'Signos específicos: muñón, seno profundo, cúpula',
             'Neumotórax frente a atelectasia', 'TAC: neumotórax pequeño, hidroneumotórax, neumopericardio'], art, src=['T6.5', 'P3.8', 'P3.9', 'P3.10', 'P3.12'])


def orden(D):
    s = new(D, 'Radiología', 'Orden de interpretación de la radiografía', 'azul', src=['P3.8', 'T6.5'])
    R = rx(s, 0.4, 1.0, 5.9, 5.95, {'airR': 0.5, 'shift': 30})
    F = R['F']
    pts = [F.p(140, 500), F.p(260, 420), F.p(560, 640), F.p(230, 790)]
    items = [('PLEURA', 'Reforzamiento, aumento de densidad, adherencia a la cara interna costal; **línea pleural**.'),
             ('PULMÓN', '¿Hay trama vascular y bronquial? Comparar lado oscuro y claro: **sin trama = aire**. Buscar el muñón.'),
             ('MASA CARDÍACA', 'Tamaño, posición, **desplazamiento del mediastino**.'),
             ('DIAFRAGMA Y ÁNGULOS', 'Profundidad de los senos (**seno profundo**); cúpula plana o invertida; comparar ambos lados.')]
    ids = []
    for i, ((h, t), p) in enumerate(zip(items, pts)):
        g = s.group_start('Lectura %d' % (i + 1))
        badge(s, p[0] - 0.22, p[1] - 0.22, i + 1, 0.46)
        box(s, 6.6, 1.0 + i * 1.3, 6.4, 1.18, '**%s** · %s' % (h, t), [WHITE, PALE][i % 2], 14, bold=False, align='l')
        ids.append(s.group_end())
    n = box(s, 6.6, 6.25, 6.4, 0.7, 'Paciente **sentado o de pie**: el aire se colecta en el **ápice**.', GOLD, 14, name='Posición')
    reveal(s, ids, 1)
    s.step(fade(n))


def seq_rx_ptx(D):
    Q = Seq(D, 'Radiografía del neumotórax (Unidad XV)', '!!RxPulmonD, !!RxAireD, !!RxLineaPleuralD, !!RxMediastino, !!RxDiafragma, tórax de '
            'referencia (!!PulmonDerecho, !!AirePleuralD), !!Leyenda', 'La hiperclaridad sin trama crece desde el ápice, la línea pleural visceral '
            'se aleja de la pared y el pulmón termina como muñón hiliar.')
    st = [({}, 'Imagen torácica normal', 'Trama vascular hasta la periferia en ambos campos.'),
          ({'hl': set()}, 'Identificación pulmonar', 'Los campos pulmonares: **oscuros con trama** (vasos y bronquios).'),
          ({'airR': 0.15}, 'Aparición de aire pleural', 'Aparece una zona **hiperclara** (negra) en el **ápice**.'),
          ({'airR': 0.25}, 'Línea pleural', '**Línea pleural visceral** visible: el borde del pulmón separado de la pared.'),
          ({'airR': 0.38}, 'Disminución de marcas periféricas', 'Entre la línea pleural y la pared **no hay trama vascular**.'),
          ({'airR': 0.6}, 'Retracción del pulmón', 'El pulmón se retrae hacia el **hilio**.'),
          ({'airR': 0.88}, 'Imagen final', '**Signo del muñón**: pulmón colapsado como masa densa hiliar rodeada de aire.'),
          ({'airR': 0.88}, 'Interpretación', 'Integrar con la **estabilidad hemodinámica**: nunca la imagen sola.')]
    for i, (sst, ttl, cap) in enumerate(st):
        s = new(D, 'Radiología', ttl, 'azul', morph=i > 0, src=['T6.5', 'P3.9'])
        R = rx(s, 0.3, 0.95, 6.2, 6.0, sst)
        A = chest(s, 6.85, 0.95, 2.9, 2.85, sst)
        step_badge(s, i + 1, len(st))
        tag(s, 6.85, 3.85, 'ANATOMÍA', WHITE, 12, w=1.6)
        lg = legend(s, cap, 6.85, 4.35, 6.15, h=1.15, size=15)
        F = R['F']
        if i == 1:
            c = s.shape(*F.p(140, 300), F.sx(280), F.sy(420), 'ellipse', None, ('FFFF00', 3), False, name='!!MarcaCampo')
            s.step(zoom(c))
        if i == 3:
            co = callout(s, [R['F'].p(*([p for p in R['cavR']][3])), (10.0, 1.3)], 'Línea pleural', 10.0, 1.0, 2.9, 0.6, WHITE, 14)
            s.step(fade(co), pulse(R['lineR'], after=True))
        if i == 4:
            b = box(s, 10.0, 1.0, 3.0, 2.8, 'Aire = **radiolúcido**: espacio negro, **sin trama**.', LBLUE, 15, name='Sin trama', bold=False)
            s.step(fade(b))
        if i == 6:
            co = callout(s, [R['F'].p(390, 470), (10.0, 1.3)], 'Muñón pulmonar', 10.0, 1.0, 2.9, 0.6, ORANGE, 14)
            s.step(fade(co))
        if i == 7:
            b = box(s, 10.0, 1.0, 3.0, 2.8, 'Tamaño + **FR, FC, TA, SpO_{2}** → decidir observar o evacuar.', GOLD, 14, name='Integrar', bold=False)
            s.step(fade(b))
        extra = ['', '', 'En el paciente erguido el aire asciende: buscarlo primero en el ápice.', '', '', 'Distancia ápice-borde torácico mayor del lado afectado.', '', '']
        if extra[i]:
            b = box(s, 6.85, 5.65, 6.15, 1.3, extra[i], WHITE, 14, name='Dato extra', bold=False)
            s.step(fade(b))
    Q.close()


def tamano(D):
    s = new(D, 'Radiología', 'Ponderar el tamaño: criterios ACCP y BTS', 'azul', src=['P3.11'])
    R = rx(s, 0.3, 0.95, 5.6, 6.0, {'airR': 0.5})
    F = R['F']
    lr = s.arrow([F.p(300, 135), F.p(300, 320)], 'FFFF00', 4, head='triangle', name='Distancia ápice-cúpula')
    lb = s.arrow([F.p(120, 470), F.p(250, 470)], '00FFFF', 4, head='triangle', name='Distancia interpleural hiliar')
    rows = [['CRITERIO', 'PEQUEÑO → OBSERVAR', 'GRANDE → DRENAR'],
            ['**ACCP** (ápice–cúpula)', '< 3 cm', '> 3 cm'],
            ['**BTS** (interpleural a nivel del hilio)', '< 2 cm', '> 2 cm']]
    ids, h = gtable(s, 6.2, 1.0, 6.8, rows, [1.6, 1.1, 1.1], 15, head_fill=[WHITE, LGREEN, ORANGE], fill_to=3.6)
    a = box(s, 6.2, 3.8, 6.8, 1.4, 'Los criterios pueden **discordar**: si **uno** indica «grande» → **drenar**.', GOLD, 15, name='Discordancia', bold=False)
    b = box(s, 6.2, 5.4, 6.8, 1.55, '**Nunca la imagen sola**: integrar siempre con FC, FR, TA y SpO_{2}.', RED, 16, name='Nunca imagen sola')
    s.step(wipe(lr, 't'), fade(ids[0], after=True), fade(ids[1], after=True))
    s.step(wipe(lb, 'l'), fade(ids[2], after=True))
    s.step(fade(a))
    s.step(zoom(b))
    s = new(D, 'Radiología', 'Grados radiológicos descritos y su conducta', 'mesotelio', src=['T6.5', 'T7.1'])
    sts = [({'airR': 0.25}, 'GRADO I (< 20 %)', 'Separación **apical** sin despegamiento completo.\nO_{2} + kinesioterapia; se reabsorbe; control.', LGREEN),
           ({'airR': 0.5}, 'GRADO II (20–50 %)', 'Borde pulmonar **distal a la línea media clavicular**.\nPleurostomía con **trampa de agua**.', GOLD),
           ({'airR': 0.88}, 'GRADO III (> 50 %)', 'Borde en la línea media clavicular o medial: **signo del muñón**.\nPleurostomía + trampa de agua (± aspiración).', ORANGE)]
    ids = []
    for i, (st, h, t, c) in enumerate(sts):
        x = 0.4 + i * 4.25
        g = s.group_start('Grado %d' % (i + 1))
        rx(s, x + 0.5, 1.0, 3.05, 3.0, st, prefix='G%d ' % i)
        box(s, x, 4.15, 4.05, 2.1, t, c, 13.5, head=h, headfill=WHITE, bold=False)
        ids.append(s.group_end())
    w = box(s, 0.4, 6.35, 12.6, 0.62, 'Esta graduación y la de ACCP/BTS provienen de fuentes distintas: **no son equivalentes** (ver auditoría).', RED, 13.5, name='Escalas distintas')
    reveal(s, ids, 1)
    s.step(fade(w))


def signos_rx(D):
    s = new(D, 'Radiología', 'Signos radiológicos del neumotórax grande', 'azul', src=['P3.9', 'T6.5'])
    st = {'airR': 0.9, 'shift': 85, 'flatR': 1, 'widenR': 1}
    R = rx(s, 0.3, 0.95, 6.0, 6.0, st)
    F = R['F']
    items = [('Muñón pulmonar', F.p(420, 470), ORANGE), ('Desviación traqueal', F.p(520, 200), GOLD),
             ('Mediastino al lado contralateral', F.p(640, 640), CEL), ('Seno profundo', F.p(130, 930), LGREEN),
             ('Cúpula aplanada / invertida', F.p(300, 900), LBLUE)]
    ids = []
    for i, (t, p, c) in enumerate(items):
        ids.append(callout(s, [p, (6.7, 1.28 + i * 0.75)], t, 6.7, 1.0 + i * 0.75, 3.6, 0.58, c, 14))
    n = box(s, 10.5, 1.0, 2.5, 3.6, 'El aire acumulado **empuja hacia abajo** y puede **invertir** la cúpula.', WHITE, 14, name='Empuje aire', bold=False)
    w = box(s, 6.7, 4.85, 6.3, 2.1, 'El **signo del seno profundo** se describe clásicamente en placas en **decúbito**; la posición de la placa no está precisada → '
            '**en revisión**.', RED, 13.5, name='Seno profundo revisar', bold=False)
    reveal(s, ids, 1)
    s.step(fade(n))
    s.step(fade(w))


def atelectasia(D):
    s = new(D, 'Radiología', 'Neumotórax frente a atelectasia: dos pérdidas de volumen opuestas', 'blanco', src=['P3.10'])
    sp = {'airR': 0.75, 'shift': 60, 'flatR': 0.6}
    sa = {'atelR': 1, 'shift': -60, 'flatR': -0.9, 'lungcolR': '8E3B4F'}
    a = chest(s, 0.3, 1.0, 3.2, 3.1, sp, names=False)
    b = rx(s, 3.6, 1.0, 3.0, 3.1, sp, prefix='PTX ')
    c = chest(s, 6.75, 1.0, 3.2, 3.1, sa, names=False)
    d = rx(s, 10.05, 1.0, 3.0, 3.1, sa, prefix='ATL ')
    tag(s, 0.3, 4.2, 'NEUMOTÓRAX', C_AIR, 15, w=6.3)
    tag(s, 6.75, 4.2, 'ATELECTASIA', 'D7BDE2', 15, w=6.3)
    rows = [('Mediastino', 'Se **desplaza** al lado contralateral («huye» del aire)', 'Es **atraído** hacia el lado afectado'),
            ('Densidad', '**Hiperlucencia** (negro)', '**Aumento de densidad** (blanco)'),
            ('Diafragma', '**Seno profundo**; cúpula descendida', '**Elevación** del hemidiafragma homolateral'),
            ('Pulmón', 'Muñón denso hacia el hilio', 'Sin imagen pulmonar expandida')]
    ids = []
    for i, (k, l, r) in enumerate(rows):
        y = 4.75 + i * 0.56
        g = s.group_start('Diferencia ' + k)
        box(s, 0.3, y, 5.2, 0.5, l, C_AIR, 12.5, bold=False, grow=False)
        box(s, 5.55, y, 2.25, 0.5, k.upper(), WHITE, 12.5, grow=False)
        box(s, 7.85, y, 5.2, 0.5, r, 'E8DAEF', 12.5, bold=False, grow=False)
        ids.append(s.group_end())
    reveal(s, ids, 1)
    s.note('La atelectasia no desplaza: atrae. El lado de la atelectasia es el lado del colapso sin aire, por eso el mediastino y el '
           'diafragma se acercan a él. En el neumotórax, el aire ocupa volumen y empuja las estructuras hacia el lado opuesto.')


def tac_ptx(D):
    s = new(D, 'Radiología', 'TAC en el neumotórax', 'azul', src=['P3.12', 'P3.15'])
    a = ct_axial(s, 0.3, 1.0, 4.1, 4.0, {'airR': 0.25}, prefix='TAC1 ')
    b = ct_axial(s, 4.6, 1.0, 4.1, 4.0, {'airR': 0.5, 'fluidR': 0.3, 'hydroR': 1}, prefix='TAC2 ')
    c = ct_axial(s, 8.9, 1.0, 4.1, 4.0, {'pneumoperi': 1, 'airR': 0.3}, prefix='TAC3 ')
    cs = [box(s, 0.3, 5.1, 4.1, 1.85, '**Gold standard** para el neumotórax **pequeño**; muestra **bulas, enfisema** o neoplasias causales.', LBLUE, 13.5,
              head='Neumotórax pequeño', headfill=WHITE, bold=False),
          box(s, 4.6, 5.1, 4.1, 1.85, '**Nivel hidroaéreo** horizontal: derrame **y** neumotórax a la vez.', C_FLUID, 13.5, head='Hidroneumotórax', headfill=WHITE, bold=False),
          box(s, 8.9, 5.1, 4.1, 1.85, 'Franja **negra** nítida por fuera del corazón y dentro del pericardio.', GOLD, 13.5, head='Neumopericardio', headfill=WHITE, bold=False)]
    s.step(fade(cs[0]))
    s.step(fade(cs[1]))
    s.step(pulse(c['peri']), fade(cs[2], after=True))


# ------------------------------------------------------------------ UNIDAD XVI
def div16(D):
    def art(s):
        chest(s, 7.0, 0.6, 6.0, 5.9, {'airR': 0.9, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.8, 'heart': 1})
    divider(D, 'XVI', 'Neumotórax a tensión', 'Del aire atrapado al shock obstructivo',
            ['Mecanismo de válvula unidireccional', 'Presión pleural positiva y colapso', 'Desplazamiento mediastínico',
             'Retorno venoso, llenado y gasto cardíaco', 'Shock obstructivo: diagnóstico clínico', 'Diferencial con taponamiento cardíaco'], art,
            src=['T6.3', 'T7.2', 'P3.14'])


CHAIN = ['Entrada de aire', 'Válvula unidireccional', 'Acumulación progresiva', '↑ presión intrapleural', 'Colapso pulmonar',
         'Desplazamiento mediastínico', 'Compresión vascular', '↓ retorno venoso', '↓ llenado cardíaco', '↓ gasto cardíaco',
         'Hipoperfusión sistémica', 'SHOCK OBSTRUCTIVO']


def seq_tension(D):
    Q = Seq(D, 'NEUMOTÓRAX A TENSIÓN — secuencia principal (Unidad XVI)', '!!PulmonDerecho, !!PulmonIzquierdo, !!AirePleuralD, !!Mediastino, '
            '!!Corazon, !!VenaCavaSup, !!VenaCavaInf, !!Traquea, !!Diafragma, !!AgujaPresion, !!Cadena1…12, !!Leyenda',
            'El aire crece en cada paso, la aguja del manómetro pasa a presión positiva, el mediastino y la tráquea se desplazan al lado sano, '
            'las cavas se estrechan, el corazón se llena menos y la cadena hemodinámica se ilumina eslabón por eslabón.')
    st = [({}, -0.8, 'Tórax normal', 'Ventilación normal: inspiración y espiración con presión pleural negativa.'),
          ({'airR': 0.12}, -0.4, 'Entrada de aire al espacio pleural', 'Una lesión permite que el aire **entre** al espacio pleural.'),
          ({'airR': 0.2}, -0.2, 'Mecanismo de válvula unidireccional', 'En **inspiración entra** aire; en **espiración** el orificio se **cierra** y el aire **no sale**.'),
          ({'airR': 0.4}, 0.05, 'Acumulación progresiva de aire', 'Con **cada respiración** se suma más aire atrapado.'),
          ({'airR': 0.55, 'hl': {'AirePleuralD'}}, 0.55, 'Aumento de la presión intrapleural', 'La presión pleural se vuelve **POSITIVA**.'),
          ({'airR': 0.85}, 0.7, 'Colapso pulmonar', 'La presión positiva **colapsa** el pulmón ipsilateral: muñón contra el mediastino.'),
          ({'airR': 0.92, 'shift': 85, 'flatR': 1, 'widenR': 1, 'hl': {'Mediastino', 'Traquea'}}, 0.85, 'Desplazamiento mediastínico',
           'En cuadros **avanzados** el mediastino y la tráquea se desplazan al **lado sano** y comprimen el pulmón contralateral.'),
          ({'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'hl': {'VenaCavaSup', 'VenaCavaInf'}}, 0.9, 'Compresión de estructuras vasculares',
           'Las **venas cavas** superior e inferior quedan **comprimidas / acodadas**.'),
          ({'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85}, 0.9, 'Disminución del retorno venoso',
           'Llega **menos sangre** a la aurícula derecha. Las venas del cuello se **ingurgitan** (la sangre no puede entrar al corazón).'),
          ({'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'heart': 1, 'hl': {'Corazon'}}, 0.9, 'Reducción del llenado cardíaco',
           'Las cavidades cardíacas **se llenan menos** (↓ precarga).'),
          ({'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'heart': 1}, 0.9, 'Disminución del gasto cardíaco',
           'Menos llenado → **menor volumen eyectado** → ↓ gasto cardíaco → **hipotensión**.'),
          ({'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'heart': 1}, 0.9, 'Hipoperfusión sistémica',
           'Taquicardia, palidez, sudoración: los tejidos reciben **menos flujo**.'),
          ({'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'heart': 1}, 0.9, 'Shock obstructivo',
           '**SHOCK OBSTRUCTIVO** → paro cardíaco si no se descomprime de inmediato.')]
    for i, (cst, pv, ttl, cap) in enumerate(st):
        s = new(D, 'Neumotórax a tensión', ttl, 'azul', morph=i > 0, src=['T6.3', 'P3.14'])
        A = chest(s, 0.3, 0.95, 6.2, 6.05, cst)
        F = A['F']
        step_badge(s, i + 1, len(st), name='!!Paso')
        ag = manometro(s, 6.85, 1.55, 3.0, pv)
        # cadena hemodinámica (los eslabones ya recorridos se colorean)
        chips = []
        for k, t in enumerate(CHAIN):
            done = k < i
            cur = k == i - 1
            fill = (RED if k >= 9 else ORANGE) if cur else ((GOLD if k < 6 else 'F5B7B1') if done else WHITE)
            chips.append(s.shape(9.05, 0.95 + k * 0.42, 3.95, 0.38, 'rect', fill, (INK, 1.25 if not cur else 2.5), False,
                                 '%d · %s' % (k + 1, t), 12.5, F_HEAD, WHITE if (cur and k >= 9) else INK, True, 'l', 'm', (0.1, 0, 0.05, 0),
                                 name='!!Cadena%d' % (k + 1), minsize=9))
        lg = legend(s, cap, 6.7, 6.05, 6.3, h=0.92, size=14)
        if i == 0:
            s.step(pulse(A['ids']['lungR']), pulse(A['ids']['lungL']))
            s.step(pulse(A['ids']['lungR']), pulse(A['ids']['lungL']))
        if i == 1:
            hx, hy = A['latR']
            ar = s.arrow([(hx + 0.6, hy - 0.9), (hx + 0.1, hy - 1.2)], RED, 5, name='Aire entra')
            s.step(wipe(ar, 'r'), pulse(chips[0], after=True))
        if i == 2:
            g = s.group_start('Válvula')
            box(s, 6.75, 4.75, 2.1, 1.15, 'INSPIRACIÓN: entra', LGREEN, 12)
            s.group_end()
            v2 = box(s, 6.75, 4.75, 2.1, 1.15, 'ESPIRACIÓN: no sale', RED, 12, name='Válvula cerrada')
            hx, hy = A['apexR']
            a1 = s.arrow([(hx + 0.3, hy + 0.6), (hx - 0.2, hy + 0.55)], '1E8449', 5, name='Entra')
            x1 = s.shape(hx - 0.05, hy + 0.35, 0.4, 0.4, 'mathMultiply', RED, (INK, 1), False, name='No sale')
            s.step(wipe(a1, 'r'), pulse(chips[1], after=True))
            s.step(fade(v2), zoom(x1, after=True))
        if i == 3:
            for k in range(3):
                pass
            s.step(pulse(A['ids']['airR']), pulse(A['ids']['airR'], after=True))
        if i == 4:
            p = box(s, 6.75, 4.75, 2.1, 1.15, 'P > 0', RED, 22, name='Presión positiva')
            s.step(zoom(p), pulse(ag, after=True))
        if i == 6:
            ar = s.arrow([F.p(500, 450), F.p(620, 450)], RED, 7, name='Empuje mediastino')
            s.step(wipe(ar, 'l'), pulse(A['ids']['trachea'], after=True))
        if i == 7:
            s.step(pulse(A['ids']['svc']), pulse(A['ids']['ivc']))
        if i == 8:
            a1 = s.arrow([A['svc'], (A['svc'][0], A['svc'][1] + 0.9)], C_VEN, 2.5, dash='dash', name='Retorno VCS')
            a2 = s.arrow([A['ivc'], (A['ivc'][0], A['ivc'][1] - 0.7)], C_VEN, 2.5, dash='dash', name='Retorno VCI')
            j = box(s, 6.75, 4.75, 2.1, 1.15, 'Ingurgitación yugular', GOLD, 13, name='Yugulares')
            s.step(wipe(a1, 't'), wipe(a2, 'b'))
            s.step(fade(j))
        if i == 9:
            s.step(pulse(A['ids']['heart']), pulse(A['ids']['heart'], after=True))
        if i == 10:
            g = s.group_start('!!GastoCardiaco')
            label(s, 6.75, 4.7, 2.1, 0.35, 'Gasto cardíaco', 12)
            s.shape(6.85, 5.05, 1.9, 0.35, 'rect', 'D5D8DC', THIN, False)
            s.shape(6.85, 5.05, 0.55, 0.35, 'rect', RED, THIN, False)
            label(s, 6.75, 5.45, 2.1, 0.35, 'TA ↓ · FC ↑', 12, RED)
            gc = s.group_end()
            s.step(wipe(gc, 'l'))
        if i == 11:
            h = box(s, 6.75, 4.75, 2.1, 1.15, 'Palidez · sudoración', ORANGE, 12.5, name='Hipoperfusión')
            s.step(fade(h))
        if i == 12:
            sh = box(s, 6.75, 4.75, 2.1, 1.15, 'EMERGENCIA', RED, 13.5, name='Emergencia', grow=False)
            s.step(zoom(sh), pulse(chips[11], after=True))
    Q.close()


def tension_clinica(D):
    s = new(D, 'Neumotórax a tensión', 'Presentación clínica', 'azul', src=['T6.3', 'P3.14'])
    A = chest(s, 0.3, 0.95, 5.0, 4.9, {'airR': 0.92, 'shift': 90, 'flatR': 1, 'widenR': 1, 'cava': 0.85, 'heart': 1})
    rows = [['', 'HALLAZGOS'],
            ['Respiratorios', 'Dolor pleurítico · disnea severa · taquipnea · cianosis · dificultad progresiva'],
            ['Cardiovasculares (los que lo distinguen)', '**Taquicardia · hipotensión · ingurgitación yugular** · palidez · sudoración'],
            ['Examen específico', '↓/ausencia de ruidos respiratorios del lado afectado · **desviación traqueal** al lado sano · **hipersonoridad** · '
             '↑ espacios intercostales']]
    ids, h = gtable(s, 5.6, 0.95, 7.4, rows, [1.2, 2.6], 14, head_fill=RED, fill_to=5.4)
    w = box(s, 0.3, 5.95, 6.2, 1.0, 'Los signos anatómicos aparecen en cuadros **avanzados**: su **ausencia no descarta** el diagnóstico.', GOLD, 13.5,
            name='No obligatorios', bold=False)
    m = box(s, 6.7, 5.6, 6.3, 1.35, 'El término «matidez desplazada» está **en revisión** (la percusión del lado afectado es hipersonora).',
            RED, 13, name='Matidez desplazada', bold=False)
    table_anim(s, ids, 1)
    s.step(fade(w))
    s.step(fade(m))
    s = new(D, 'Neumotórax a tensión', 'Diferencial clínico en el shock: neumotórax a tensión o taponamiento', 'mesotelio', src=['P3.14', 'P3.15'])
    a = chest(s, 0.3, 1.0, 2.6, 2.55, {'airR': 0.9, 'shift': 80, 'cava': 0.8, 'heart': 1}, names=False)
    b = chest(s, 10.4, 1.0, 2.6, 2.55, {'peric': 1, 'heart': -0.6, 'cava': 0.3}, names=False)
    rows = [['NEUMOTÓRAX A TENSIÓN', 'SIGNO', 'TAPONAMIENTO CARDÍACO'],
            ['**Disminuidos o abolidos**', 'Ruidos respiratorios', 'Normales (pulmón libre)'],
            ['**Timpánica** (hiperresonancia)', 'Percusión', 'Sin cambio específico'],
            ['Normales o levemente disminuidos', 'Ruidos cardíacos', '**Hipofonéticos** (disminuidos, no abolidos)'],
            ['**Desviada** al lado contralateral', 'Tráquea', 'Centrada'],
            ['**Asimetría** de la expansión', 'Tórax', 'Simetría conservada'],
            ['Distendidas', 'Venas yugulares', 'Distendidas']]
    ids, h = gtable(s, 3.1, 1.0, 7.1, rows, [1.5, 1.0, 1.5], 13.5, head_fill=[C_AIR, WHITE, LILAC], first_fill=None, first_bold=False, fill_to=6.1,
                    col_fills=[None, PALE, None])
    w = box(s, 0.3, 6.25, 12.7, 0.72, 'Pueden **coexistir**: el **neumopericardio** lo evidencia. Percusión + auscultación cardíaca y pulmonar deciden la conducta.',
            RED, 14, name='Coexisten')
    table_anim(s, ids, 2)
    s.step(fade(w))
    s = new(D, 'Neumotórax a tensión', 'Emergencia: el diagnóstico es clínico', 'blanco', src=['T7.2', 'T6.3', 'P3.14'])
    a = box(s, 0.4, 1.0, 12.6, 1.35, 'Sospecha de neumotórax a tensión con **inestabilidad hemodinámica** = **EMERGENCIA**. **No** esperar radiografía ni TAC '
            'para actuar: el paciente puede morir en la espera.', RED, 17, name='No esperar imagen', bold=False)
    res = flow(s, ['Disnea + hipotensión + ausencia unilateral de MV + desviación traqueal', 'Descompresión inmediata con aguja gruesa',
                   'Convierte el neumotórax a tensión en un neumotórax **abierto** simple', 'Tratamiento definitivo: **toracostomía** con tubo + trampa de agua'],
               0.4, 2.6, 12.6, 2.0, [GOLD, ORANGE, CEL, GREEN], 14, 0.3)
    b = box(s, 0.4, 4.85, 6.15, 2.1, 'Sitios descritos: aguja en **2.º espacio intercostal, línea medioclavicular**, por encima del borde '
            'superior de la 3.ª costilla; tubo en **5.º espacio, línea axilar media**.', WHITE, 13.5, name='Sitios material', bold=False)
    c = box(s, 6.85, 4.85, 6.15, 2.1, 'Los sitios de descompresión recomendados han cambiado en guías recientes: **verificar** con la normativa vigente antes '
            'de enseñarlos como protocolo (ver auditoría).', GOLD, 13.5, name='Verificar sitios', bold=False)
    s.step(zoom(a))
    flow_anim(s, res, 1)
    s.step(fade(b))
    s.step(fade(c))


def build(D):
    unit_start(D, 'XV', 'Radiografía y TAC del neumotórax')
    div15(D)
    orden(D)
    seq_rx_ptx(D)
    tamano(D)
    signos_rx(D)
    atelectasia(D)
    tac_ptx(D)
    unit_end(D, 'XV')
    unit_start(D, 'XVI', 'Neumotórax a tensión')
    div16(D)
    seq_tension(D)
    tension_clinica(D)
    unit_end(D, 'XVI')
