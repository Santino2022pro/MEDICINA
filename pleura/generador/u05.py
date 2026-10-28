# -*- coding: utf-8 -*-
"""UNIDAD VII (imágenes del derrame) y UNIDAD VIII (toracocentesis)."""
from base import *


def div7(D):
    def art(s):
        chest(s, 6.9, 0.7, 3.1, 3.0, {'fluidR': 0.5}, names=False)
        rx(s, 10.15, 0.75, 2.85, 2.9, {'fluidR': 0.5}, prefix='Arte Rx')
        ct_axial(s, 7.2, 3.95, 2.8, 2.9, {'fluidR': 0.3, 'loc': 1}, prefix='Arte TAC')
        bmode(s, 10.2, 3.95, 2.8, 2.9, {'pattern': 'liq'}, prefix='Arte Eco')
    divider(D, 'VII', 'Diagnóstico por imágenes del derrame', 'La imagen debe coincidir con la anatomía',
            ['Radiografía: primer estudio', 'Borramiento del seno costofrénico', 'Línea (curva) de Damoiseau',
             'Derrame masivo y desplazamiento mediastínico', 'TAC: derrames pequeños y tabicados', 'Ecografía: el líquido es anecoico'], art,
            src=['T3.3', 'P3.6'])


def seq_rx(D):
    Q = Seq(D, 'Derrame progresivo: ilustración anatómica y radiografía sincronizadas (Unidad VII)',
            'Tórax: !!PulmonDerecho, !!LiquidoPleuralD, !!Mediastino, !!Corazon, !!Traquea · Rx: !!RxOpacidadD, !!RxPulmonD, !!RxMediastino, '
            '!!RxTraquea, !!RxDiafragma, !!Leyenda', 'Ambas escenas usan la misma geometría: a cada aumento del líquido en la ilustración '
            'corresponde el mismo cambio de opacidad en la radiografía.')
    st = [({}, 'Pulmón normal', 'Senos costofrénicos agudos y libres; campos pulmonares con trama vascular.', None),
          ({'fluidR': 0.06}, 'Pequeño volumen pleural', 'Un volumen pequeño puede **no verse** en la radiografía frontal.', None),
          ({'fluidR': 0.16}, 'Ocupación del seno costofrénico', '**Borramiento del seno**: se necesitan **al menos ~200 ml** en la Rx de frente.', 'cp'),
          ({'fluidR': 0.32}, 'Aumento del volumen', 'Radiopacidad homogénea con borde superior **cóncavo hacia arriba**.', 'dam'),
          ({'fluidR': 0.5}, 'Compresión pulmonar', 'El pulmón comprimido se desplaza hacia el hilio y el ápice.', None),
          ({'fluidR': 0.68}, 'Mayor opacidad', 'La opacidad asciende y ocupa la mayor parte del hemitórax.', None),
          ({'fluidR': 0.92, 'shift': 75, 'widenR': 1}, 'Desplazamiento mediastínico', 'Derrame **masivo**: opacidad de todo el hemitórax y '
           'mediastino desplazado **hacia el lado sano**.', 'med'),
          ({'fluidR': 0.92, 'shift': 75, 'widenR': 1}, 'Imagen radiológica final', 'Interpretación: siempre correlacionar con la clínica y '
           'buscar la causa.', 'fin')]
    for i, (sst, ttl, cap, mark) in enumerate(st):
        s = new(D, 'Imágenes', ttl, 'azul', morph=i > 0, src=['T3.3', 'P3.8'])
        A = chest(s, 0.25, 0.95, 5.0, 4.9, sst)
        R = rx(s, 5.5, 1.0, 4.6, 4.8, sst)
        step_badge(s, i + 1, len(st))
        tag(s, 0.25, 5.9, 'ANATOMÍA', WHITE, 13, w=1.8)
        tag(s, 5.5, 5.9, 'RADIOGRAFÍA FRONTAL', WHITE, 13, w=2.6)
        lg = legend(s, cap, 0.25, 6.4, 9.85, h=0.75, size=15)
        F = R['F']
        side = []
        if mark == 'cp':
            c = s.shape(*F.p(105, 800), F.sx(110), F.sy(110), 'ellipse', None, ('FFFF00', 3.5), False, name='!!MarcaSeno')
            side.append(box(s, 10.35, 1.0, 2.7, 2.2, 'El ángulo agudo entre diafragma y pared se **borra**.', GOLD, 14, name='Seno texto', bold=False))
            s.step(zoom(c), fade(side[0], after=True))
        if mark == 'dam':
            cav = R['cavR']
            from anat import fluid_level
            lvl = fluid_level('R', sst, cav)
            xs = [p[0] for p in cav]; xl, xm = min(xs), max(xs)
            pts = [F.p(xl + (xm - xl) * k / 20, lvl - min(110, 40 + 260 * sst['fluidR']) * ((1 - k / 20) ** 2.2)) for k in range(21)]
            d = s.arrow(pts, 'FFFF00', 4, tail=None, name='!!CurvaDamoiseau')
            side.append(box(s, 10.35, 1.0, 2.7, 3.0, '**Línea de Damoiseau** (Ellis-Damoiseau): asciende desde el ángulo costovertebral, sube '
                            'lateralmente y desciende hacia el mediastino.', GOLD, 13.5, name='Damoiseau texto', bold=False))
            s.step(wipe(d, 'r', dur=900), fade(side[0], after=True))
        if mark == 'med':
            side.append(box(s, 10.35, 1.0, 2.7, 2.6, 'Tráquea y corazón **se alejan** del lado del derrame.', ORANGE, 14, name='Mediastino texto', bold=False))
            s.step(fade(side[0]))
        if mark == 'fin':
            rows = [['SIGNO', 'SIGNIFICADO'], ['Seno borrado', '≥ ~200 ml'], ['Damoiseau', 'Derrame libre'], ['Hemitórax opaco', 'Derrame masivo'],
                    ['Mediastino → sano', 'Efecto de masa']]
            ids, h = gtable(s, 10.3, 1.0, 2.8, rows, [1, 1], 12, head_fill=LBLUE, fill_to=5.8)
            table_anim(s, ids, 2)
        if not side and mark != 'fin':
            info = ['Primer estudio a solicitar ante sospecha de derrame.', 'Rx: el derrame se evidencia cuando supera **200–300 ml**.',
                    '', '', 'La opacidad es **homogénea**: el líquido borra la trama.', 'El pulmón ya no se ve en la base.'][i] if i < 6 else ''
            if info:
                side.append(box(s, 10.35, 1.0, 2.7, 2.6, info, LBLUE, 14, name='Dato Rx', bold=False))
                s.step(fade(side[0]))
        mini = box(s, 10.35, 3.85 if mark != 'dam' else 4.2, 2.7, 1.95 if mark != 'dam' else 1.6,
                   'Blanco = **radiopaco** (líquido, hueso)\nNegro = **aire**', WHITE, 12.5, name='Clave Rx', bold=False) if mark != 'fin' else None
    Q.close()


def tac(D):
    s = new(D, 'Imágenes', 'TAC: mayor sensibilidad que la radiografía', 'azul', src=['T3.3'])
    a = ct_axial(s, 0.3, 1.0, 4.1, 4.1, {'fluidR': 0.18})
    b = ct_axial(s, 4.6, 1.0, 4.1, 4.1, {'fluidR': 0.4, 'loc': 1})
    tag(s, 0.3, 5.2, 'DERRAME PEQUEÑO (declive)', WHITE, 13, w=4.1)
    tag(s, 4.6, 5.2, 'DERRAME TABICADO (loculado)', WHITE, 13, w=4.1)
    cs = two_cards(s, [('Sensibilidad', 'Detecta derrames **pequeños** y **tabicados**; los diferencia del **engrosamiento pleural**.', LBLUE),
                       ('Hallazgo', 'Densidad aumentada («blanca») entre la pleura parietal y el pulmón, en zona **declive**.', CEL),
                       ('Causa', 'Permite ver **adenopatías, tumores** y patología pulmonar subyacente.', GOLD),
                       ('Indicación', 'Derrames **loculados** o sospecha de causa **maligna**.', ORANGE)], 8.95, 1.0, 4.1, 5.95, 0.15, 14)
    n = box(s, 0.3, 5.75, 8.4, 1.2, 'Corte axial en decúbito supino: el líquido libre se dispone **posterior** (declive); los tabiques lo '
            'fragmentan en compartimentos.', WHITE, 14, name='Lectura TAC', bold=False)
    s.step(fade(a['fluid']))
    s.step(fade(b['fluid']), fade(b['septa'], after=True))
    reveal(s, cs, 1)
    s.step(fade(n))
    s = new(D, 'Imágenes', 'Ecografía: el líquido es anecoico', 'azul', src=['P3.6'])
    p = probe(s, 1.0, 1.2, 0.75)
    e = bmode(s, 2.1, 1.0, 5.0, 4.4, {'pattern': 'liq'})
    w = waves(s, 1.37, 2.55, 0.25, 3, 0.25, 'F1C40F', 4, (40, 140), name='!!OndaUltrasonido')
    co = callout(s, [e['F'].p(500, 560), (4.6, 5.85)], 'Líquido = NEGRO (anecoico)', 3.1, 5.6, 3.0, 0.55, C_FLUID, 14)
    sc = [('Líquido', 'Imagen **negra** (anecoica)', '111111', WHITE), ('Tejidos intermedios', 'Escala de **grises**', '888888', WHITE),
          ('Muy denso (hueso)', 'Muy **blanco** + **cono de sombra** posterior', 'F2F2F2', INK)]
    ids = []
    for i, (h, t, c, tc) in enumerate(sc):
        g = s.group_start('Escala ' + h)
        s.shape(7.5, 1.0 + i * 1.3, 1.0, 1.1, 'rect', c, BORDER, False)
        box(s, 8.6, 1.0 + i * 1.3, 4.4, 1.1, '**%s**: %s' % (h, t), WHITE, 14, bold=False, align='l')
        ids.append(s.group_end())
    n = box(s, 7.5, 5.0, 5.5, 1.95, 'La ecogenicidad depende de la **densidad** del tejido que genera el eco. Solo el **líquido** es anecoico; '
            'los tejidos blandos tienen **ecogenicidad intermedia** (ver auditoría).', GOLD, 13, name='Ecogenicidad', bold=False)
    s.step(fade(p), wipe(w, 't', after=True))
    s.step(fade(co))
    reveal(s, ids, 1)
    s.step(fade(n))


# ------------------------------------------------------------------ UNIDAD VIII
def div8(D):
    def art(s):
        patient_back(s, 7.3, 0.7, 4.0, name='Arte paciente')
        for i, (c, l) in enumerate((('F7DC6F', 'Bacteriología'), ('D98880', 'Citología'), ('F9E79F', 'Fisicoquímico'))):
            tube(s, 10.9 + i * 0.7, 4.1, 0.5, 1.9, c, None, 'clear', name='Arte tubo %d' % i)
    divider(D, 'VIII', 'Toracocentesis', 'Punción y aspiración del espacio pleural',
            ['Objetivos diagnósticos y terapéuticos', 'Anatomía de la pared: el paquete vasculonervioso', 'Obtención de la muestra (concepto)',
             'Los tres frascos', 'Indicaciones y algoritmo en sospecha de ICC', 'Complicaciones e iatrogenia'], art, src=['T4.1', 'P2.15', 'P2.16'])


def seq_toraco(D):
    Q = Seq(D, 'Toracocentesis: del paciente al análisis (Unidad VIII)', '!!Paciente, !!ZonaLiquido, !!PielPared, !!Costillas, !!PaqueteVN, '
            '!!PleuraParietal, !!LiquidoPleural, !!Aguja, tubos, !!Leyenda', 'Del paciente sentado a la zona de matidez, luego acercamiento al '
            'corte de la pared con la aguja conceptual y finalmente los frascos y su análisis.')
    TOT = 9
    # 1 paciente
    s = new(D, 'Toracocentesis', 'El paciente', 'torax', src=['T4.1'])
    g, F = patient_back(s, 0.8, 1.0, 5.9)
    step_badge(s, 1, TOT)
    cs = two_cards(s, [('Definición', '**Punción y aspiración** del espacio pleural.', CEL),
                       ('Doble finalidad', '**Diagnóstica** (analizar el líquido) y **terapéutica** (evacuarlo para aliviar la disnea).', GREEN),
                       ('Cuándo', 'Estudio fundamental ante **todo derrame de causa no clara**.', GOLD)], 6.8, 1.0, 6.2, 5.9, 0.18, 15)
    reveal(s, cs, 1)
    # 2 tórax
    s = new(D, 'Toracocentesis', 'El tórax desde atrás', 'torax', morph=True, src=['T4.1'])
    g, F = patient_back(s, 0.8, 1.0, 5.9)
    step_badge(s, 2, TOT)
    ribs = []
    for k in range(7):
        y = 330 + k * 85
        for sg in (-1, 1):
            ribs.append(catmull([(500 + sg * 30, y), (500 + sg * 150, y - 20), (500 + sg * 260, y + 20), (500 + sg * 290, y + 70)], False, 5))
    r = draw_lines(s, F, ribs, darken(C_BONE, 0.4), 4, '!!CostillasPosteriores')
    b = box(s, 6.8, 1.0, 6.2, 2.3, 'Proyección posterior de las costillas: los **espacios intercostales** son la vía de acceso al espacio pleural.',
            WHITE, 15, name='Espacios', bold=False)
    b2 = box(s, 6.8, 3.55, 6.2, 3.4, 'El nivel superior del líquido se delimita por la **matidez** a la percusión y por las imágenes '
             '(Unidades VI y VII). Ese dato, no una regla fija, guía el sitio de acceso.', CEL, 15, name='Nivel del líquido', bold=False)
    s.step(fade(r))
    s.step(fade(b))
    s.step(fade(b2))
    # 3 localización del líquido
    s = new(D, 'Toracocentesis', 'Localización del líquido', 'torax', morph=True, src=['T4.1', 'T3.2'])
    g, F = patient_back(s, 0.8, 1.0, 5.9)
    step_badge(s, 3, TOT)
    r = draw_lines(s, F, ribs, darken(C_BONE, 0.4), 4, '!!CostillasPosteriores')
    # derecha del paciente = derecha de la imagen en vista posterior
    z = draw_poly(s, F, Polygon(catmull([(530, 640), (780, 600), (800, 900), (540, 930)], True, 5)), ('a', C_FLUID, 55), ('2E86C1', 2, 'dash'), '!!ZonaLiquido')
    lb = tag(s, F.p(800, 0)[0] - 0.2, F.p(0, 960)[1], 'Zona de matidez (lado derecho)', C_FLUID, 13)
    cs = two_cards(s, [('Clínica e imágenes', 'La **matidez**, la radiografía y las imágenes delimitan dónde está el líquido.', TURQ),
                       ('Vista posterior', 'Aquí el lado **derecho** del paciente queda a la **derecha** de la imagen.', GOLD)], 6.8, 1.0, 6.2, 4.0, 0.18, 15)
    s.step(fade(z), fade(lb, after=True))
    reveal(s, cs, 1)
    # 4 acercamiento
    s = new(D, 'Toracocentesis', 'Acercamiento: corte de la pared', 'azul', morph=True, src=['T4.1'])
    A = pleura_zoom(s, 0.3, 0.95, 8.3, 6.3, {'gap': 0.35, 'axis': 1})
    step_badge(s, 4, TOT)
    b = box(s, 8.9, 1.0, 4.1, 2.6, 'Corte sagital del espacio intercostal (izquierda = craneal; derecha = caudal) con derrame entre las hojas.',
            WHITE, 15, name='Corte', bold=False)
    b2 = box(s, 8.9, 3.8, 4.1, 3.15, 'Capas de afuera hacia adentro: **piel → tejido subcutáneo → músculos intercostales → pleura parietal → '
             'espacio pleural** (líquido) → pleura visceral → pulmón.', GREEN, 14, name='Capas', bold=False)
    s.step(fade(b))
    s.step(fade(b2))
    # 5 estructuras relevantes
    s = new(D, 'Toracocentesis', 'Estructuras relevantes: el paquete vasculonervioso', 'azul', morph=True, src=['T4.1'])
    A = pleura_zoom(s, 0.3, 0.95, 8.3, 6.3, {'gap': 0.35, 'axis': 1, 'hl': set()})
    step_badge(s, 5, TOT)
    c1 = callout(s, [A['nvb_pt'], (8.9, 1.3)], 'Paquete vasculonervioso', 8.9, 1.0, 3.2, 0.6, GOLD, 14)
    c2 = callout(s, [A['upper_border'], (8.9, 2.0)], 'Borde superior costilla inferior', 8.9, 1.7, 3.6, 0.6, LGREEN, 14)
    cs = two_cards(s, [('Surco subcostal', 'El paquete corre por el **borde INFERIOR** de cada costilla.', ORANGE),
                       ('Principio', 'Se ingresa **por encima del borde superior** de la costilla **inferior** para alejarse del paquete.', GREEN),
                       ('En revisión', 'El orden de vena, arteria y nervio dentro del paquete debe verificarse (Auditoría).', RED)], 8.9, 2.5, 4.1, 4.45, 0.15, 13.5)
    s.step(fade(c1), pulse(A['nvb'], after=True))
    s.step(fade(c2))
    reveal(s, cs, 1)
    # 6 obtención conceptual
    s = new(D, 'Toracocentesis', 'Obtención de la muestra: representación conceptual', 'azul', morph=True, src=['T4.1'])
    A = pleura_zoom(s, 0.3, 0.95, 8.3, 6.3, {'gap': 0.35, 'axis': 1})
    step_badge(s, 6, TOT)
    ux, uy = A['upper_border']
    nd = s.shape(ux - 0.04, 0.95 - 1.6, 0.08, 1.6 + 0.2, 'rect', vshade('BFC9CA', 0.4, 0.3, 0), (INK, 1.25), False, name='!!Aguja')
    sy0, sy1 = A['space_y']
    target = A['F'].p(0, (sy0 + sy1) / 2)[1]
    b = box(s, 8.9, 1.0, 4.1, 3.0, 'La aguja atraviesa piel, músculo intercostal y **pleura parietal** hasta el líquido, **sin alcanzar** la pleura visceral.',
            WHITE, 15, name='Trayecto', bold=False)
    w = box(s, 8.9, 4.2, 4.1, 2.75, 'Esquema **didáctico**: el sitio de punción se **individualiza** en cada paciente; no es un protocolo universal.',
            RED, 14, name='Seguridad', bold=False)
    s.step(fade(nd), path(nd, 0, target - 1.15, after=True, dur=1200))
    s.step(fade(b))
    s.step(fade(w))
    # 7 tubos
    s = new(D, 'Toracocentesis', 'Tres frascos', 'mesotelio', morph=True, src=['T4.1'])
    step_badge(s, 7, TOT)
    fr = [('Bacteriología', 'Agente causal: **cultivo, Gram, BAAR** (TBC).', 'F7DC6F', CEL), ('Anatomía patológica', '**Citología**: búsqueda de células malignas.', 'E6B0AA', LILAC),
          ('Fisicoquímico', 'El **más importante**: permite aplicar los **criterios de Light**.', 'F9E79F', GOLD)]
    ids = []
    for i, (h, t, c, f) in enumerate(fr):
        x = 0.6 + i * 4.2
        g = s.group_start('Frasco ' + h)
        tube(s, x + 1.35, 1.1, 1.1, 3.4, c, None, 'clear', name='!!Frasco%d' % (i + 1))
        box(s, x, 4.75, 3.8, 2.2, t, f, 15, head='%d · %s' % (i + 1, h), headfill=WHITE, bold=False)
        ids.append(s.group_end())
    reveal(s, ids, 1)
    # 8 análisis
    s = new(D, 'Toracocentesis', 'Análisis: qué aporta cada estudio', 'mesotelio', morph=True, src=['T4.1', 'P2.12'])
    step_badge(s, 8, TOT)
    for i, c in enumerate(('F7DC6F', 'E6B0AA', 'F9E79F')):
        tube(s, 0.6 + i * 1.0, 1.1, 0.7, 2.4, c, None, 'clear', name='!!Frasco%d' % (i + 1))
    rows = [['FRASCO', 'DETERMINACIONES (ver Unidades IX y X)'], ['Bacteriología', 'Gram · cultivo · BAAR'],
            ['Anatomía patológica', 'Citología (células malignas)'], ['Fisicoquímico', 'Proteínas y LDH (con valores séricos) · glucosa · pH · ADA · '
            'amilasa · triglicéridos · colesterol · recuento celular']]
    ids, h = gtable(s, 3.8, 1.0, 9.2, rows, [1, 2.3], 15, head_fill=LBLUE, fill_to=5.0)
    n = box(s, 0.6, 5.3, 12.4, 1.65, 'Las proteínas y la LDH se miden **en el líquido y en la sangre** al mismo tiempo: los criterios se basan en '
            '**relaciones**.', GOLD, 16, name='Muestra simultánea', bold=False)
    table_anim(s, ids, 1)
    s.step(fade(n))
    # 9 interpretación
    s = new(D, 'Toracocentesis', 'Interpretación: del frasco al diagnóstico', 'mesotelio', morph=True, src=['T4.1', 'T4.2'])
    step_badge(s, 9, TOT)
    res = flow(s, ['Fisicoquímico', 'Criterios de Light', '¿≥ 1 criterio positivo?'], 0.6, 1.0, 12.4, 1.3, [GOLD, CEL, WHITE], 16, 0.4)
    a = box(s, 0.6, 2.8, 6.0, 2.0, '**SÍ → EXUDADO**: buscar causa local con bacteriología, citología y parámetros (Unidad X).', C_EXUD, 16, name='Exudado ruta', bold=False)
    b = box(s, 7.0, 2.8, 6.0, 2.0, '**NO → TRASUDADO**: tratar la enfermedad sistémica de base.', C_FLUID, 16, name='Trasudado ruta', bold=False)
    n = box(s, 0.6, 5.1, 12.4, 1.85, 'La toracocentesis transforma un **síndrome** (derrame) en una **orientación etiológica**.', GREEN, 17, name='Síndrome a etiología')
    flow_anim(s, res, 1)
    s.step(fade(a))
    s.step(fade(b))
    s.step(zoom(n))
    Q.close()


def indicaciones(D):
    s = new(D, 'Toracocentesis', 'Indicaciones', 'torax', src=['T4.1', 'P2.15', 'P2.14'])
    a = box(s, 0.4, 1.0, 6.1, 2.75, '- **Diagnóstico etiológico** (causa desconocida)\n- **Evacuación terapéutica** (alivio de la disnea)\n'
            '- Derrame **paraneumónico**: drenar cuando es complicado', CEL, 15, head='Indicaciones generales', headfill=WHITE, bold=False, align='l')
    b = box(s, 0.4, 3.95, 6.1, 3.0, 'Se propone puncionar «todo derrame **> 2 cm** en proyección en **decúbito**»: umbral y '
            'proyección deben **verificarse** antes de enseñarse como regla (Auditoría).', RED, 14.5, head='Umbral a revisar', headfill=WHITE, bold=False)
    res = flow(s, ['Sospecha de ICC', 'Diuréticos y observación', '¿Remite?', 'NO → toracocentesis'], 6.8, 1.0, 6.2, 3.6,
               [C_FLUID, WHITE, GOLD, ORANGE], 15, 0.22, 'v')
    c = box(s, 6.8, 4.8, 6.2, 2.15, 'Aun con ICC, puncionar si hay **asimetría** persistente de la expansión, **fiebre** persistente, **dolor** que no '
            'cede o **falta de remisión** con el tratamiento.', GOLD, 14, name='Indicaciones absolutas', bold=False)
    s.step(fade(a))
    flow_anim(s, res, 2, 'v')
    s.step(fade(c))
    s.step(fade(b))
    s = new(D, 'Toracocentesis', 'Complicaciones: la iatrogenia', 'azul', src=['P2.16', 'P2.15'])
    sts = [({'airR': 0.35}, 'Neumotórax iatrogénico', 'Punción inadvertida del pulmón / pleura visceral.'),
           ({'fluidR': 0.45, 'blood': 1}, 'Hemotórax', 'Hemorragia que se suma al derrame.'),
           ({'fluidR': 0.3, 'airR': 0.35, 'hydroR': 1}, 'Hidroneumotórax', 'Aire que ingresa con evacuación incompleta.'),
           ({'lungcolR': 'C0606F'}, 'Edema de reexpansión', 'Edema del pulmón reexpandido.')]
    gs = []
    for i, (st, h1, h2) in enumerate(sts):
        x = 0.3 + i * 3.2
        g = s.group_start('Complicación ' + h1)
        chest(s, x, 1.0, 3.0, 2.95, st, names=False)
        box(s, x, 4.05, 3.0, 0.55, h1, [C_AIR, C_BLOOD, C_FLUID, PINKB][i], 14)
        box(s, x, 4.65, 3.0, 0.85, h2, WHITE, 12.5, bold=False)
        gs.append(s.group_end())
    w = box(s, 0.3, 5.65, 12.8, 1.3, 'Evaluar el **contexto cardiovascular** antes del procedimiento y **vigilar** después: una complicación súbita '
            '(aire que se suma al derrame) puede llevar a **neumotórax a tensión y shock obstructivo**.', RED, 14.5, name='Vigilar', bold=False)
    reveal(s, gs, 1)
    s.step(fade(w))
    s.note('El material vincula el edema de reexpansión con no haber evaluado la cardiopatía de base; el mecanismo clásicamente '
           'descrito es la reexpansión rápida de un pulmón colapsado. Se registra para revisión.')


def build(D):
    unit_start(D, 'VII', 'Imágenes del derrame')
    div7(D)
    seq_rx(D)
    tac(D)
    unit_end(D, 'VII')
    unit_start(D, 'VIII', 'Toracocentesis')
    div8(D)
    seq_toraco(D)
    indicaciones(D)
    unit_end(D, 'VIII')
