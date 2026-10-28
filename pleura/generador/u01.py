# -*- coding: utf-8 -*-
"""Portada, índice, código visual, razonamiento sindromático y UNIDAD I
(anatomía y fisiología de la pleura)."""
from base import *

UNIDADES = [
    ('I', 'Anatomía y fisiología de la pleura'), ('II', 'Formación y reabsorción del líquido: Starling'),
    ('III', 'Mecanismos del derrame pleural'), ('IV', 'Trasudado y exudado'), ('V', 'Etiologías del derrame'),
    ('VI', 'Semiología del derrame'), ('VII', 'Imágenes del derrame'), ('VIII', 'Toracocentesis'),
    ('IX', 'Criterios de Light'), ('X', 'Análisis del líquido pleural'), ('XI', 'Derrame paraneumónico y empiema'),
    ('XII', 'Neumotórax'), ('XIII', 'Semiología del neumotórax'), ('XIV', 'Ecografía pleural'),
    ('XV', 'Radiografía y TAC del neumotórax'), ('XVI', 'Neumotórax a tensión'), ('XVII', 'Tratamiento y drenaje torácico'),
    ('XVIII', 'Tumores pleurales'), ('XIX', 'Integración clínica'),
]


def portada(D):
    s = D.new(BG['portada']); s.src = []; s.tagname = 'Portada'
    A = chest(s, 7.2, 0.55, 6.0, 5.9, {'hl': set()})
    t = s.text(0.5, 1.2, 6.6, 2.4, 'ENFERMEDADES\nPLEURALES', 54, F_TITLE, INK, True, 'c', 'm', name='Título', lnspc=0.88,
               reff='<a:effectLst><a:glow rad="101600"><a:srgbClr val="FFFFFF"><a:alpha val="90000"/></a:srgbClr></a:glow></a:effectLst>')
    b1 = box(s, 0.8, 3.75, 6.0, 0.62, 'FISIOPATOLOGÍA · SEMIOLOGÍA · DIAGNÓSTICO · MANEJO CLÍNICO', CEL, 15, name='Subtítulo')
    b2 = box(s, 0.8, 4.55, 6.0, 1.05, 'Derrame pleural · Trasudados y exudados · Criterios de Light · Toracocentesis · '
             'Empiema · Neumotórax · Neumotórax a tensión · Tumores pleurales', WHITE, 14, name='Temario')
    b3 = box(s, 1.9, 5.85, 3.8, 0.6, 'MEDICINA INTERNA · FISIOPATOLOGÍA RESPIRATORIA', GOLD, 12.5, name='Materia')
    s.step(fade(t), fade(b1, after=True))
    s.step(wipe(b2, 'l'), fade(b3, after=True))
    s.note('Clase de Medicina Interna sobre enfermedades de la pleura. Hilo conductor: cada hallazgo clínico se explica por un '
           'cambio anatómico o de presiones en el espacio pleural.')


def indice(D):
    for part, rng in ((1, UNIDADES[:10]), (2, UNIDADES[10:])):
        s = new(D, 'Índice', 'Recorrido de la clase (%d/2)' % part, 'mesotelio')
        ids = []
        for i, (r, t) in enumerate(rng):
            col = i % 2; row = i // 2
            x = 0.6 + col * 6.2; y = 1.15 + row * 1.12
            g = s.group_start('Unidad ' + r)
            s.shape(x, y, 1.2, 0.8, 'rect', GOLD, BORDER, False, r, 22, F_HEAD, INK, True, 'c', 'm', fit=False)
            s.shape(x + 1.25, y, 4.75, 0.8, 'rect', WHITE if row % 2 == 0 else PALE, BORDER, False, t, 17, F_HEAD, INK, True,
                    'l', 'm', (0.15, 0, 0.1, 0), minsize=11)
            ids.append(s.group_end())
        reveal(s, ids, 2)
        s.note('Organización: anatomía y fisiología → derrame (mecanismos, clasificación, causas, semiología, imágenes, '
               'toracocentesis, laboratorio, empiema) → neumotórax (formación, semiología, ecografía, radiología, tensión, '
               'drenaje) → tumores → integración.')


def codigo(D):
    s = new(D, 'Código visual', 'Cómo leer las ilustraciones', 'mesotelio')
    sw = [(C_PARIETAL, 'Pleura parietal'), (C_VISCERAL, 'Pleura visceral'), (C_FLUID, 'Líquido seroso / trasudado'),
          (C_EXUD, 'Exudado (turbio, proteico)'), (C_PUS, 'Pus (empiema)'), (C_BLOOD, 'Líquido hemorrágico'),
          (C_AIR, 'Aire en el espacio pleural'), (C_LYMPH, 'Vaso linfático'), (C_ART, 'Capilar / arterial'), (C_VEN, 'Venoso / venas cavas')]
    ids = []
    for i, (c, t) in enumerate(sw):
        x = 0.5 + (i % 2) * 3.35; y = 1.1 + (i // 2) * 0.95
        g = s.group_start('Código ' + t)
        s.shape(x, y, 0.75, 0.7, 'rect', c, BORDER, False)
        s.shape(x + 0.85, y, 2.35, 0.7, 'rect', WHITE, THIN, False, t, 13.5, F_HEAD, INK, True, 'l', 'm', (0.08, 0, 0.05, 0), minsize=9)
        ids.append(s.group_end())
    bx = [('DEFINICIÓN / CONCEPTO', CEL), ('MECANISMO FISIOPATOLÓGICO', GREEN), ('CONSECUENCIA CLÍNICA', ORANGE),
          ('DATO CLAVE / CIFRA', GOLD), ('HALLAZGO SEMIOLÓGICO', TURQ), ('IMÁGENES', LBLUE),
          ('ALERTA · EMERGENCIA · REVISAR', RED)]
    bids = []
    for i, (t, c) in enumerate(bx):
        bids.append(box(s, 7.4, 1.1 + i * 0.78, 5.5, 0.62, t, c, 15, name='Tipo ' + t[:12]))
    n = box(s, 0.5, 6.0, 6.6, 0.95, 'Lado DERECHO del paciente = lado IZQUIERDO de la imagen (convención radiológica).', WHITE, 14,
            name='Convención')
    reveal(s, ids, 5)
    reveal(s, bids, 7)
    s.step(zoom(n))
    s.note('Los colores se mantienen idénticos en toda la presentación: la pleura parietal siempre verde azulada, la visceral '
           'morada, el líquido seroso celeste, el exudado ámbar, el pus amarillo, la sangre roja y el aire casi blanco con '
           'borde punteado. El tipo de recuadro anticipa la función del texto.')


def sindrome(D):
    s = new(D, 'Razonamiento clínico', 'Síndrome: hallazgos unidos por un mismo mecanismo', 'torax', src=['P1.1', 'P4.1'])
    d = box(s, 0.4, 1.0, 6.2, 1.55, '**SÍNDROME**: conjunto de síntomas y signos con el **mismo nexo fisiopatogénico**. '
            'Si los hallazgos no están concatenados por un mecanismo común, no constituyen un síndrome.', CEL, 16,
            name='Definición síndrome', bold=False, align='l')
    items = ['SÍNTOMA / SIGNO', 'SÍNDROME', 'FISIOPATOLOGÍA', 'ETIOLOGÍA', 'TRATAMIENTO']
    res = flow(s, items, 0.4, 2.85, 6.2, 3.7, [WHITE, CEL, GREEN, GOLD, ORANGE], 16, 0.22, 'v')
    ex = box(s, 7.0, 1.0, 5.95, 2.6, 'Ejemplo integrado: **disnea + matidez + abolición del frémito + disminución del murmullo** '
             'en una base comparten un mismo mecanismo: **líquido interpuesto** entre el pulmón y la pared. '
             'Ese nexo los convierte en el **síndrome de derrame pleural**.', WHITE, 15, name='Ejemplo', bold=False, align='l',
             head='Síndrome de ocupación pleural líquida', headfill=TURQ)
    r = box(s, 7.0, 3.85, 5.95, 1.35, 'Nivel descriptivo: enumerar causas y criterios.\nNivel interpretativo: **conectar** los datos '
            'con la fisiopatología, anticipar complicaciones y decidir la conducta.', GOLD, 14.5, name='Niveles', bold=False, align='l')
    w = box(s, 7.0, 5.45, 5.95, 1.0, 'Nunca saltear pasos: la etiología se busca DESPUÉS de reconocer el síndrome y su mecanismo.',
            RED, 14.5, name='Alerta pasos')
    s.step(fade(d))
    flow_anim(s, res, 1, 'v')
    s.step(fade(ex))
    s.step(fade(r))
    s.step(zoom(w))
    s.note('El síntoma y el signo «buscan» el síndrome; el síndrome se explica por la fisiopatología; la fisiopatología orienta '
           'la etiología y esta, el tratamiento. Esta cadena estructura toda la clase.')


# ------------------------------------------------------------------ UNIDAD I
def div1(D):
    def art(s):
        chest(s, 7.0, 0.5, 6.2, 6.0, {})
    divider(D, 'I', 'Anatomía y fisiología de la pleura', 'Dos hojas, un espacio virtual, una mecánica acoplada',
            ['Pleura visceral y pleura parietal', 'Cavidad y espacio pleural', 'Inervación y relaciones',
             'Líquido pleural normal: composición', 'Presión intrapleural negativa', 'Deslizamiento en inspiración y espiración'],
            art, src=['T1.1', 'T1.2', 'P2.1'])


ZOOM = [  # (X, Y, W, H) del tórax en cada etapa del acercamiento
    (0.35, 0.95, 6.5, 6.3), (-0.6, -0.15, 10.4, 10.1), (-0.6, -0.15, 10.4, 10.1), (-0.6, -0.15, 10.4, 10.1),
    (-1.5, -6.0, 24, 23.2)]


def seq_anat(D):
    Q = Seq(D, 'De tórax completo a espacio pleural y mecánica respiratoria (Unidad I)',
            '!!ParedToracica, !!Costillas, !!PulmonDerecho, !!PulmonIzquierdo, !!PleuraVisceralD/I, !!PleuraParietalD/I, '
            '!!Mediastino, !!Corazon, !!Diafragma, !!Leyenda → luego !!PleuraParietal, !!PleuraVisceral, !!LiquidoPleural, !!Alveolos',
            'Acercamiento progresivo (escala y posición del mismo tórax) hasta el corte de las dos hojas; el espacio pleural se '
            'amplía; la hoja visceral se desliza en inspiración y vuelve en espiración.')
    TOT = 10
    # 1 · tórax completo
    s = new(D, 'Anatomía', 'El tórax: continente y contenido', 'azul', src=['T1.1'])
    A = chest(s, *ZOOM[0], {})
    step_badge(s, 1, TOT)
    ids = A['ids']
    lab = []
    for txt, pt, (x, y) in (('Costillas y pared', A['latR'], (7.2, 1.0)), ('Pulmón derecho', A['lungR'], (7.2, 1.75)),
                            ('Mediastino y corazón', A['heart'], (7.2, 2.5)), ('Diafragma', A['diaphR'], (7.2, 3.25))):
        lab.append(callout(s, [pt, (x, y + 0.27)], txt, x, y, 2.6, 0.55, WHITE, 14))
    c = box(s, 10.0, 1.0, 3.0, 2.8, 'Cada pulmón está envuelto por una **serosa de doble hoja**: la **pleura**.', CEL, 15,
            name='Concepto pleura', bold=False)
    lg = legend(s, 'Ambos pulmones, costillas, diafragma, mediastino y las dos hojas pleurales forman una unidad mecánica.', 7.2, 4.2, 5.8, h=1.2)
    s.step(fade(ids['wall']), fade(ids['ribs'], after=True), fade(ids['clav']))
    s.step(fade(ids['lungR']), fade(ids['lungL']), fade(ids['visc' + 'R']), fade(ids['visc' + 'L']))
    s.step(fade(ids['med']), fade(ids['heart'], after=True), fade(ids['aorta']), fade(ids['svc']), fade(ids['ivc']), fade(ids['trachea']))
    s.step(wipe(ids['diaph'], 'l'), fade(ids['parR']), fade(ids['parL']))
    reveal(s, lab, 2)
    s.step(fade(c))
    s.note('Vista frontal esquemática: pared torácica con costillas, ambos pulmones (el derecho con tres lóbulos y dos cisuras; '
           'el izquierdo con dos lóbulos), mediastino con corazón, venas cavas, aorta y tráquea, y el diafragma con la cúpula '
           'derecha más alta. Sobre cada pulmón, la pleura visceral (morada); sobre la pared, el diafragma y el mediastino, la '
           'pleura parietal (verde azulada).')
    # 2 · acercamiento al pulmón
    s = new(D, 'Anatomía', 'Acercamiento al pulmón derecho', 'azul', morph=True, src=['T1.1'])
    A = chest(s, *ZOOM[1], {})
    step_badge(s, 2, TOT)
    b = box(s, 8.2, 1.0, 4.8, 2.0, 'El pulmón ocupa casi por completo su hemitórax: entre su superficie y la pared queda solo '
            'un **espacio virtual**.', CEL, 15, name='Pulmón ocupa', bold=False)
    lg = legend(s, 'Mismo tórax, mayor escala: el pulmón derecho con sus lóbulos, cisuras, vasos y bronquios.', 8.2, 5.2, 4.8, h=1.3)
    s.step(fade(b))
    # 3 · pleura visceral
    s = new(D, 'Anatomía', 'Pleura visceral: la hoja interna', 'azul', morph=True, src=['T1.1'])
    A = chest(s, *ZOOM[2], {'hl': {'PleuraVisceralD'}})
    step_badge(s, 3, TOT)
    co = callout(s, [A['viscR'], (8.2, 1.35)], 'PLEURA VISCERAL', 8.2, 1.0, 2.6, 0.6, C_VISCERAL, 15)
    b = box(s, 8.2, 1.85, 4.8, 2.4, '- Reviste **directamente la superficie del pulmón**.\n- Se introduce en las **cisuras interlobares**.\n'
            '- **No tiene inervación sensitiva**.', WHITE, 15, name='Visceral texto', bold=False, align='l', anchor='t')
    lg = legend(s, 'La hoja visceral acompaña al pulmón en todos sus movimientos.', 8.2, 5.2, 4.8, h=1.3)
    s.step(fade(co), pulse(A['ids']['viscR'], after=True))
    s.step(wipe(b, 't'))
    # 4 · pleura parietal
    s = new(D, 'Anatomía', 'Pleura parietal: la hoja externa', 'azul', morph=True, src=['T1.1'])
    A = chest(s, *ZOOM[3], {'hl': {'PleuraParietalD'}})
    step_badge(s, 4, TOT)
    co = callout(s, [A['latR'], (8.2, 1.35)], 'PLEURA PARIETAL', 8.2, 1.0, 2.6, 0.6, C_PARIETAL, 15)
    b = box(s, 8.2, 1.85, 4.8, 2.0, 'Tapiza la cara interna de:\n- la **pared torácica** (costal)\n- el **diafragma**\n- el **mediastino**',
            WHITE, 15, name='Parietal texto', bold=False, align='l')
    inn = box(s, 8.2, 4.05, 4.8, 1.0, 'Recibe **inervación sensitiva** → origen del **dolor pleurítico**.', ORANGE, 15, name='Inervación')
    lg = legend(s, 'Dos hojas que se continúan en el hilio y delimitan la cavidad pleural.', 8.2, 5.3, 4.8, h=1.2)
    s.step(fade(co), pulse(A['ids']['parR'], after=True))
    s.step(wipe(b, 't'))
    s.step(zoom(inn))
    # 5 · ampliación de ambas hojas (zoom extremo sobre la pared lateral)
    s = new(D, 'Anatomía', 'Ampliación de ambas hojas en la pared lateral', 'azul', morph=True, src=['T1.1'])
    A = chest(s, *ZOOM[4], {'hl': {'PleuraParietalD', 'PleuraVisceralD'}})
    step_badge(s, 5, TOT)
    b = box(s, 8.3, 1.0, 4.7, 2.2, 'A esta escala ya se distinguen **dos hojas paralelas** separadas por una **lámina mínima**: '
            'el espacio pleural.', CEL, 15, name='Dos hojas', bold=False)
    lg = legend(s, 'Pared costal → pleura parietal → espacio pleural → pleura visceral → pulmón.', 8.3, 5.3, 4.7, h=1.2)
    s.step(fade(b))
    # 6 · espacio pleural (corte microscópico)
    s = new(D, 'Anatomía', 'El espacio pleural: virtual en condiciones normales', 'azul', morph=True, src=['T1.1'])
    A = pleura_zoom(s, 0.3, 0.95, 8.4, 6.35, {'gap': 0.08})
    step_badge(s, 6, TOT)
    labs = [callout(s, [A['rib_pt'], (8.95, 1.27)], 'Costilla', 8.95, 1.0, 1.9, 0.5, C_BONE, 13),
            callout(s, [A['nvb_pt'], (8.95, 1.92)], 'Paquete vasculonervioso', 8.95, 1.65, 3.0, 0.5, WHITE, 13),
            callout(s, [A['par_pt'], (8.95, 2.57)], 'Pleura parietal (mesotelio)', 8.95, 2.3, 3.0, 0.5, C_PARIETAL, 13),
            callout(s, [A['space'], (8.95, 3.22)], 'Espacio pleural', 8.95, 2.95, 2.3, 0.5, C_FLUID, 13),
            callout(s, [A['visc_pt'], (8.95, 3.87)], 'Pleura visceral (mesotelio)', 8.95, 3.6, 3.0, 0.5, C_VISCERAL, 13),
            callout(s, [A['alv_pt'], (8.95, 4.52)], 'Alvéolos', 8.95, 4.25, 1.8, 0.5, C_LUNG, 13)]
    b = box(s, 8.95, 5.0, 4.05, 1.35, '**Cavidad pleural**: espacio potencial que en patología puede acumular **líquido, aire o pus**.',
            WHITE, 14, name='Cavidad potencial', bold=False)
    reveal(s, labs, 2)
    s.step(fade(b))
    # 7 · líquido lubricante
    s = new(D, 'Fisiología', 'Una lámina de líquido lubricante', 'azul', morph=True, src=['T1.1', 'T1.2'])
    A = pleura_zoom(s, 0.3, 0.95, 8.4, 6.35, {'gap': 0.08, 'hl': {'LiquidoPleural'}})
    step_badge(s, 7, TOT)
    b = box(s, 8.95, 1.0, 4.05, 2.1, 'El espacio contiene una **pequeña cantidad de líquido** que **lubrica** y permite el '
            '**deslizamiento** de las hojas.', CEL, 15, name='Lubricante', bold=False)
    v = box(s, 8.95, 3.3, 4.05, 1.05, 'Volumen normal: **0,13 ± 0,06 ml/kg**', GOLD, 15, name='Volumen normal')
    w = box(s, 8.95, 4.55, 4.05, 1.6, 'Alterar su **producción**, su **reabsorción** o su **composición** puede conducir a un '
            '**derrame pleural**.', ORANGE, 14, name='Alteración', bold=False)
    s.step(fade(b), pulse(A['fluid'], after=True))
    s.step(zoom(v))
    s.step(fade(w))
    # 8 · inspiración
    s = new(D, 'Mecánica', 'Inspiración: la hoja visceral se desliza', 'azul', morph=True, src=['T1.1', 'P2.1'])
    A = pleura_zoom(s, 0.3, 0.95, 8.4, 6.35, {'gap': 0.08})
    step_badge(s, 8, TOT)
    ar = arrow_lbl(s, [(2.2, 4.75), (5.6, 4.75)], 'deslizamiento', C_VISCERAL, 5, 14, lx=2.6, ly=4.25, lw=2.6, name='Flecha deslizamiento')
    b = box(s, 8.95, 1.0, 4.05, 2.2, 'Al contraerse el diafragma y los intercostales, la pared se expande y **arrastra al pulmón**: '
            'la hoja visceral **se desliza** sobre la parietal **sin fricción**.', GREEN, 14, name='Inspiración texto', bold=False)
    k = box(s, 8.95, 3.4, 4.05, 1.3, 'Las hojas se separan **lateralmente**, no se despegan: el líquido las mantiene **acopladas**.',
            WHITE, 14, name='Acople', bold=False)
    s.step(fade(b))
    s.step(wipe(ar, 'l'), path(A['visc'], 0.55, 0, after=False, dur=1100), path(A['alv'], 0.55, 0, dur=1100))
    s.step(fade(k))
    # 9 · espiración
    s = new(D, 'Mecánica', 'Espiración: retorno por la retracción elástica', 'azul', morph=True, src=['T1.1', 'P2.1'])
    A = pleura_zoom(s, 0.3, 0.95, 8.4, 6.35, {'gap': 0.08, 'dx': 65})
    step_badge(s, 9, TOT)
    ar = arrow_lbl(s, [(5.6, 4.75), (2.2, 4.75)], 'retorno', C_PARIETAL, 5, 14, lx=2.6, ly=4.25, lw=2.6, name='Flecha retorno')
    b = box(s, 8.95, 1.0, 4.05, 2.2, 'Al relajarse los músculos, la **retracción elástica** del pulmón lo devuelve a su volumen; '
            'la hoja visceral **vuelve a deslizarse** en sentido opuesto.', GREEN, 14, name='Espiración texto', bold=False)
    s.step(fade(b))
    s.step(wipe(ar, 'r'), path(A['visc'], -0.55, 0, dur=1100), path(A['alv'], -0.55, 0, dur=1100))
    # 10 · integración
    s = new(D, 'Mecánica', 'Integración: el acoplamiento pared–pulmón', 'azul', morph=True, src=['T1.1', 'P2.1'])
    A = chest(s, *ZOOM[0], {})
    step_badge(s, 10, TOT)
    F = A['F']
    arr = []
    for (x, y, dx, dy) in ((150, 450, -70, 0), (850, 450, 70, 0), (300, 780, 0, 70), (700, 800, 0, 70)):
        arr.append(s.arrow([F.p(x, y), F.p(x + dx, y + dy)], '1F4E79', 5, name='Expansión %d' % len(arr)))
    items = [('Presión negativa', 'El espacio pleural tiene **presión negativa** respecto a la atmósfera: mantiene el pulmón **expandido**.', CEL),
             ('Lubricación', 'El líquido reduce la **fricción** entre las superficies.', GREEN),
             ('Acoplamiento', 'La pared y el pulmón se mueven **juntos** durante la ventilación.', GOLD)]
    cs = two_cards(s, items, 7.2, 1.0, 5.8, 5.4, 0.2, 14.5)
    s.step(*[fade(a, after=bool(i)) for i, a in enumerate(arr)])
    reveal(s, cs, 1)
    Q.close()
    s.note('Síntesis: la pleura no es un órgano «inútil». Protege el parénquima, permite el deslizamiento, hace posible el '
           'movimiento pulmonar en inspiración y espiración y participa en la mecánica ventilatoria. La presión negativa del '
           'espacio pleural es la que mantiene el pulmón expandido: si entra aire, el pulmón se retrae (Unidad XII).')


def anat_tablas(D):
    # pleura visceral vs parietal
    s = new(D, 'Anatomía', 'Pleura visceral y pleura parietal', 'mesotelio', src=['T1.1'])
    rows = [['', 'PLEURA PARIETAL', 'PLEURA VISCERAL'],
            ['Posición', 'Hoja **externa**', 'Hoja **interna**'],
            ['Reviste', 'Cara interna de la **pared torácica**, el **diafragma** y el **mediastino**', 'Superficie del **pulmón**, incluidas las **cisuras interlobares**'],
            ['Inervación sensitiva', '**Sí** → dolor pleurítico', '**No**'],
            ['Color en las ilustraciones', 'Verde azulado', 'Morado']]
    ids, h = gtable(s, 0.5, 1.15, 8.1, rows, [1.2, 2, 2], 16, head_fill=[WHITE, C_PARIETAL, C_VISCERAL], fill_to=5.0)
    A = pleura_zoom(s, 8.9, 1.15, 4.1, 5.8, {'gap': 0.05})
    n = box(s, 0.5, 5.2, 4.0, 1.75, 'Ambas hojas se continúan entre sí en el **hilio pulmonar**: delimitan un espacio cerrado.', CEL, 15,
            name='Continuidad', bold=False)
    p = box(s, 4.65, 5.2, 3.95, 1.75, '**Dolor pleurítico**: puntada de costado que aumenta con la inspiración y la tos; nace en la '
            'hoja **parietal**.', ORANGE, 15, name='Dolor pleurítico', bold=False)
    table_anim(s, ids, 1)
    s.step(fade(n))
    s.step(fade(p))
    # funciones de la pleura
    s = new(D, 'Fisiología', 'Funciones de la pleura', 'torax', src=['P2.1', 'T1.2'])
    A = pleura_zoom(s, 0.35, 1.0, 5.6, 5.9, {'gap': 0.08})
    fs = [('Protección', 'Protección **mecánica** del parénquima pulmonar.', CEL),
          ('Deslizamiento', 'Permite el movimiento del pulmón dentro del tórax **sin fricción**.', GREEN),
          ('Permisibilidad', 'Hace posible el movimiento pulmonar en **inspiración y espiración**.', TURQ),
          ('Mecánica ventilatoria', 'Acopla mecánicamente **pared torácica y pulmón**.', GOLD)]
    cs = two_cards(s, fs, 6.3, 1.0, 6.7, 5.3, 0.15, 14.5)
    w = box(s, 6.3, 6.45, 6.7, 0.55, 'Que su función se estudie poco no significa que sea prescindible.', RED, 13.5, name='No inútil')
    reveal(s, cs, 1)
    s.step(fade(w))
    # contenido posible de la cavidad
    s = new(D, 'Anatomía', 'La cavidad pleural: un espacio potencial', 'azul', src=['T1.1'])
    sts = [({}, 'NORMAL', 'Lámina mínima de líquido'), ({'fluidR': 0.45}, 'LÍQUIDO', 'Derrame pleural'),
           ({'airR': 0.55}, 'AIRE', 'Neumotórax'), ({'fluidR': 0.45, 'pus': 1}, 'PUS', 'Empiema')]
    gs = []
    for i, (st, h1, h2) in enumerate(sts):
        x = 0.3 + i * 3.25
        g = s.group_start('Estado ' + h1)
        chest(s, x, 1.05, 3.05, 3.0, st, names=False)
        box(s, x, 4.15, 3.05, 0.55, h1, [WHITE, C_FLUID, C_AIR, C_PUS][i], 16)
        box(s, x, 4.75, 3.05, 0.55, h2, WHITE, 13.5, bold=False)
        gs.append(s.group_end())
    n = box(s, 0.3, 5.6, 12.75, 1.3, 'En condiciones patológicas el espacio virtual se hace **real**: lo ocupa **líquido** (derrame), '
            '**aire** (neumotórax) o **pus** (empiema). Cada contenido modifica de manera distinta la mecánica y los hallazgos.',
            CEL, 15, name='Conclusión cavidad', bold=False)
    reveal(s, gs, 1)
    s.step(fade(n))
    # líquido normal: composición
    s = new(D, 'Fisiología', 'Líquido pleural normal: composición', 'mesotelio', src=['T1.2'])
    rows = [['PARÁMETRO', 'VALOR DE REFERENCIA'],
            ['Volumen', '0,13 ± 0,06 ml/kg'],
            ['pH', '7,50 – 7,60 (alcalino respecto del plasma)'],
            ['HCO_{3}^{−}', 'Mayor que el plasmático (pH alcalino)'],
            ['Proteínas', '< 1–2 g/dl (< 0,5 del valor sérico)'],
            ['Glucosa', 'Similar a la plasmática'],
            ['LDH', 'Inferior a la sérica'],
            ['Albúmina', '50–70 % de la albúmina plasmática']]
    ids, h = gtable(s, 0.4, 1.0, 7.4, rows, [1.2, 2.6], 16, fill_to=6.95)
    tb = tube(s, 8.4, 1.4, 1.2, 4.6, 'FFF6D5', 'Seroso, claro', 'clear', name='Tubo normal', fill=0.55)
    r = box(s, 10.1, 1.2, 2.9, 5.3, 'Varios valores de esta tabla (volumen, HCO_{3}^{−}, glucosa, LDH) están **en revisión** por inconsistencias de '
            'unidad o de redacción: ver **Auditoría científica**.', RED, 13, name='Revisión valores', bold=False)
    table_anim(s, ids, 2)
    s.step(fade(tb))
    s.step(fade(r))
    s.note('Valores tomados del material académico. El pH del líquido normal es alcalino respecto del plasma, lo que implica '
           'mayor concentración de bicarbonato: la redacción original «HCO3 disminuido» es incompatible con ese pH y se registra '
           'en la auditoría junto con las unidades del volumen (cm frente a ml) y las proporciones de glucosa y LDH.')
    # celularidad
    s = new(D, 'Fisiología', 'Celularidad normal del líquido pleural', 'rosa', src=['T1.2'])
    bars = [('Macrófagos', 64, 80, '8E7CC3'), ('Linfocitos', 18, 36, '5DADE2'), ('Células mesoteliales', 0, 2, C_PARIETAL), ('PMN', 0, 3, 'F5B041')]
    gs = []
    base_x = 3.6; scale = 0.075
    s.shape(0.4, 1.0, 8.0, 5.1, 'rect', ('a', 'FFFFFF', 85), BORDER, False, name='Panel gráfico')
    label(s, 0.6, 1.1, 7.6, 0.45, 'Proporción del recuento (%)', 15)
    for i, (n_, a, b, c) in enumerate(bars):
        y = 1.8 + i * 1.05
        g = s.group_start('Barra ' + n_)
        label(s, 0.6, y, 2.9, 0.6, n_, 14, align='r')
        s.shape(base_x, y + 0.08, max(0.05, b * scale), 0.45, 'rect', ('a', c, 45), THIN, False)
        s.shape(base_x, y + 0.08, max(0.05, a * scale), 0.45, 'rect', c, THIN, False)
        label(s, base_x + b * scale + 0.1, y, 1.5, 0.6, ('%d–%d %%' % (a, b)) if n_ != 'PMN' else 'pocos', 13, align='l')
        gs.append(s.group_end())
    t = box(s, 8.7, 1.0, 4.3, 1.5, 'Leucocitos: **1.000 – 5.000/mm^{3}**', GOLD, 16, name='Recuento total')
    m = box(s, 8.7, 2.7, 4.3, 2.0, 'Predominio de **macrófagos**; los **PMN son escasos**. Un predominio distinto orienta a patología '
            '(Unidad X).', WHITE, 14.5, name='Interpretación celular', bold=False)
    reveal(s, gs, 1)
    s.step(zoom(t))
    s.step(fade(m))
    # presión negativa y fuerzas opuestas
    s = new(D, 'Mecánica', 'Presión intrapleural negativa: dos fuerzas opuestas', 'azul', src=['T1.1', 'T6.1'])
    A = chest(s, 0.35, 0.95, 6.4, 6.2, {})
    F = A['F']
    a1 = arrow_lbl(s, [F.p(250, 470), F.p(350, 470)], 'retracción pulmonar', C_VISCERAL, 6, 12, lx=F.p(170, 0)[0], ly=F.p(0, 380)[1], lw=1.7,
                   name='Retracción pulmón')
    a2 = arrow_lbl(s, [F.p(150, 600), F.p(70, 600)], 'expansión de pared', C_PARIETAL, 6, 12, lx=F.p(0, 0)[0] + 0.05, ly=F.p(0, 640)[1], lw=1.6,
                   name='Expansión pared')
    cs = two_cards(s, [('Pulmón', 'Por su **elasticidad intrínseca** tiende a **retraerse** hacia el hilio.', LILAC),
                       ('Pared torácica', 'Tiende a **expandirse** hacia afuera.', TURQ),
                       ('Resultado', 'Entre ambas fuerzas el espacio pleural queda a **presión negativa** (subatmosférica): el pulmón '
                        'permanece **expandido** y acoplado a la pared.', CEL)], 7.1, 1.0, 5.9, 4.4, 0.18, 14.5)
    w = box(s, 7.1, 5.6, 5.9, 1.3, 'Si entra aire, la presión negativa se pierde y el pulmón **colapsa por su propia elasticidad** '
            '→ neumotórax (Unidad XII).', RED, 14, name='Puente neumotórax', bold=False)
    s.step(wipe(a1, 'r'))
    s.step(wipe(a2, 'l'))
    reveal(s, cs, 1)
    s.step(fade(w))


def build(D):
    portada(D)
    indice(D)
    codigo(D)
    sindrome(D)
    unit_start(D, 'I', UNIDADES[0][1])
    div1(D)
    seq_anat(D)
    anat_tablas(D)
    unit_end(D, 'I')
