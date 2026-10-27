# -*- coding: utf-8 -*-
"""Portada, recorrido, código visual y red interorgánica"""
from base import *

U = 0


def cover(D):
    s = D.new(WHITE)
    s.unit = 0; s.morph = False
    background(s, 'cover')
    # moléculas 3D alrededor del título (como la referencia)
    model(s, 'glucosa', 2.45, 0.35, 3.0, name='!!Glucosa 3D portada', tilt=(0.5, 0.3, 0.2))
    model(s, 'palmitato', 5.6, 5.85, 4.8, hs=False, name='!!Ácido graso 3D portada', tilt=(0.2, 0.9, 0.1))
    model(s, 'bhb', 8.3, 0.45, 2.1, name='!!β-OHB 3D portada', tilt=(0.4, 0.6, 0.3))
    model(s, 'glicerol', 2.7, 5.55, 1.9, name='!!Glicerol 3D portada', tilt=(0.6, 0.2, 0.5))
    s.pic('adipocyte-1', 0.15, 4.95, 2.3, name='!!Adipocitos portada')
    s.pic('pancreas', 10.75, 1.2, 2.5, name='!!Páncreas portada')
    s.pic('healthy_liver', 10.8, 4.6, 2.4, name='!!Hígado portada')
    t = btitle(s, 'DIABETES, OBESIDAD\nY TEJIDO ADIPOSO', 54, y=1.95, x=2.6, w=8.1, name='Título portada')
    sub = s.text(2.8, 4.05, 7.7, 0.85, 'Integración metabólica: regulación hormonal, señalización celular,\nmetabolismo interorgánico y fisiopatología',
                 17, F_HEAD, INK, True, 'c', 'm', name='Subtítulo portada', reff=GLOWW)
    tg = mbox(s, 4.35, 5.05, 4.6, 0.5, 'BIOQUÍMICA INTEGRADA · MEDICINA', 'y', 15, name='Etiqueta portada')
    s.step(fade(sub), zoom(tg, after=True))
    s.note('Presentación de bioquímica integrada sobre diabetes, obesidad y tejido adiposo. El hilo conductor es la red '
           'PÁNCREAS ↔ HÍGADO ↔ TEJIDO ADIPOSO ↔ MÚSCULO ↔ RIÑÓN ↔ HIPOTÁLAMO ↔ SISTEMA CARDIOVASCULAR. '
           'Los modelos moleculares de la portada son geometrías tridimensionales reales (β-D-glucopiranosa, palmitato, '
           'D-β-hidroxibutirato y glicerol) calculadas con campo de fuerza y representadas con código de colores CPK: '
           'carbono gris oscuro, oxígeno rojo, hidrógeno blanco.\n'
           'Las ilustraciones de órganos y células provienen de Servier Medical Art (licencia CC BY 3.0/4.0).')


def route(D):
    s = new(D, U, 'Recorrido de la clase', 'cyan')
    parts = [('I', 'Bases bioquímicas de la diabetes', 'y'), ('II', 'Caso 11: cetoacidosis y neumonía', 's'),
             ('III', 'Caso 12: estado hiperglucémico hiperosmolar', 'g'), ('IV', 'Integración CAD frente a EHH', 'b'),
             ('V', 'Tejido adiposo: histología, señalización y metabolismo', 'y'), ('VI', 'Apetito, peso y gasto energético', 's'),
             ('VII', 'Caso 20: obesidad clase III', 'g'), ('VIII', 'Tratamiento, farmacología y normativa', 'b'),
             ('IX', 'Síndrome metabólico', 'y'), ('X', 'Práctica aplicada: cálculos y preguntas', 's'),
             ('XI', 'Fuentes, límites e integración final', 'g')]
    ids = []
    for i, (r, t, k) in enumerate(parts):
        c = i // 6; rr = i % 6
        x = 0.5 + c * 6.35; y = 1.2 + rr * 0.95
        g = s.group_start('Parte ' + r)
        s.shape(x, y, 0.95, 0.72, 'rect', INK, (INK, 2), SHD, r, 24, F_POP, BOX, False, 'c', 'm', (0, 0, 0, 0), fit=False)
        mbox(s, x + 1.05, y, 5.0, 0.72, t, k, 16, caps=False)
        ids.append(s.group_end())
    s.pic('Human_male', 7.0, 6.0 - 0.0, h=1.2, name='Organismo pequeño') if False else None
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids[:6])])
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids[6:])])
    s.note('Recorrido en once partes. Las unidades I a IV construyen la base molecular de la diabetes y la aplican a dos '
           'emergencias hiperglucémicas (casos 11 y 12). Las unidades V a VII trasladan el foco al tejido adiposo, el control '
           'neuroendocrino del apetito y la obesidad clase III (caso 20). La VIII desarrolla el tratamiento y la normativa '
           'argentina; la IX, el síndrome metabólico y la aterogénesis; la X reúne doce ejercicios y preguntas de opción '
           'múltiple; la XI cierra con límites de interpretación, datos faltantes y bibliografía.')


def code(D):
    s = new(D, U, 'Código visual de los mapas', 'peach')
    items = [
        (mbox, (0.6, 1.3, 2.6, 0.62, 'Glucosa', 'y', 16), 'Metabolito / molécula clave (recuadro amarillo, borde negro, texto rojo)'),
        (mbox, (0.6, 2.2, 2.6, 0.62, 'Hormona / señal', 's', 16), 'Hormona, citocina o mediador'),
        (mbox, (0.6, 3.1, 2.6, 0.62, 'Receptor / transportador', 'g', 15), 'Receptor, canal o transportador'),
        (elabel, (0.85, 4.12, 'ENZIMA · proceso', 13), 'Enzima o proceso escrito sobre la flecha'),
        (mbox, (0.6, 4.85, 2.6, 0.62, 'Consecuencia clínica', 'r', 15), 'Consecuencia clínica o alerta'),
    ]
    ids = []
    for i, (fn, args, d) in enumerate(items):
        g = s.group_start('Código %d' % i)
        fn(s, *args)
        s.text(3.45, args[1] - 0.02 if fn is mbox else args[1] - 0.12, 3.2, 0.66, d, 14, F_BODY, INK, False, 'l', 'm')
        ids.append(s.group_end())
    g = s.group_start('Código flechas')
    s.arrow([(7.2, 1.6), (8.8, 1.6)], INK, 2.5); s.text(9.0, 1.4, 4.0, 0.4, 'Conversión, flujo o estímulo', 14, F_BODY, INK, False, 'l', 'm')
    s.arrow([(7.2, 2.3), (8.8, 2.3)], ACT, 3.0); s.text(9.0, 2.1, 4.0, 0.4, '[g]Activación[/]', 14, F_BODY, INK, False, 'l', 'm')
    s.inhib([(7.2, 3.0), (8.8, 3.0)]); s.text(9.0, 2.8, 4.0, 0.4, '[r]Inhibición (⊣)[/]', 14, F_BODY, INK, False, 'l', 'm')
    s.arrow([(7.2, 3.7), (8.8, 3.7)], TRN, 3.0, dash='dash'); s.text(9.0, 3.5, 4.0, 0.4, '[b]Transporte entre compartimentos[/]', 14, F_BODY, INK, False, 'l', 'm')
    ids.append(s.group_end())
    g = s.group_start('Código moléculas')
    model(s, 'glucosa', 7.1, 4.35, 1.55, label='Glucosa')
    model(s, 'acetoacetato', 8.95, 4.5, 1.3, label='Acetoacetato')
    model(s, 'glicerol', 10.55, 4.45, 1.15, label='Glicerol')
    s.text(7.1, 6.3, 5.9, 0.6, 'Modelos 3D: [k]C[/] gris · [r]O[/] rojo · H blanco · [b]N[/] azul · [o]P[/] naranja', 14, F_BODY, INK, False, 'c', 'm')
    ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Código visual constante. Los recuadros amarillos con borde negro y texto rojo representan metabolitos y moléculas '
           'clave; los salmón, hormonas y mediadores; los verdes, receptores, canales y transportadores; los pequeños rótulos '
           'sobre las flechas nombran enzimas o procesos; los rojos, consecuencias clínicas. Flechas negras: conversión o flujo; '
           'verdes: activación; rojas terminadas en barra: inhibición; azules discontinuas: transporte. Los modelos '
           'moleculares 3D usan el código CPK. Cuando un mecanismo ocurre en paralelo (por ejemplo, las dos ramas de la '
           'cetoacidosis) se anima en ramas simultáneas y no como cadena obligatoriamente consecutiva.')


def network(D, final=False):
    s = new(D, U, 'La red interorgánica' if not final else 'La red interorgánica: síntesis', 'green')
    P = {}
    P['brain'] = s.pic('brain-2', 5.75, 1.0, 1.75, name='!!Cerebro red')
    P['liver'] = s.pic('healthy_liver', 0.55, 1.45, 2.9, name='!!Hígado red')
    P['panc'] = s.pic('pancreas', 4.9, 3.35, 2.6, name='!!Páncreas red')
    P['adip'] = s.pic('adipocyte-1', 10.4, 1.15, 2.2, name='!!Tejido adiposo red')
    P['musc'] = s.pic('muscle-fiber', 9.85, 4.65, 2.8, name='!!Músculo red')
    P['kid'] = s.pic('kidney-1', 3.35, 4.9, 0.95, name='!!Riñón red')
    P['heart'] = s.pic('heart-front', 0.75, 4.55, 1.55, name='!!Corazón red')
    labs = {'brain': (7.55, 1.7, 'HIPOTÁLAMO'), 'liver': (0.75, 3.15, 'HÍGADO'), 'panc': (5.15, 4.35, 'PÁNCREAS'),
            'adip': (10.45, 3.3, 'TEJIDO ADIPOSO'), 'musc': (10.2, 6.1, 'MÚSCULO'), 'kid': (4.4, 5.3, 'RIÑÓN'),
            'heart': (0.6, 6.45, 'SISTEMA CARDIOVASCULAR')}
    L = {}
    for k, (x, y, t) in labs.items():
        w = text_w(t, F_HEAD, True, 13) + 0.35
        L[k] = mbox(s, x, y, w, 0.4, t, 'y', 13, name='!!Rótulo ' + t.lower())
    E = []
    E.append(arrow_lbl(s, [(5.4, 3.7), (3.35, 2.7)], 'insulina / glucagón', ACT, 3, 11.5, lx=3.4, ly=3.25, lw=1.9, name='Insulina a hígado', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(7.45, 3.85), (10.0, 5.1)], 'insulina', ACT, 3, 11.5, lx=8.2, ly=4.6, lw=1.0, name='Insulina a músculo', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(7.35, 3.55), (10.35, 2.45)], 'insulina', ACT, 3, 11.5, lx=8.35, ly=2.75, lw=1.0, name='Insulina a adiposo', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(10.4, 1.6), (7.55, 1.45)], 'leptina', '7030A0', 3, 11.5, lx=8.5, ly=1.12, lw=0.9, name='Leptina a cerebro', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(10.4, 2.05), (3.45, 2.1)], 'AGNE · glicerol', TRN, 2.5, 11.5, lx=6.95, ly=2.15, lw=1.5, dash='dash', name='AGNE a hígado', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(2.2, 3.6), (3.4, 5.1)], 'glucosa', INK, 2.5, 11.5, lx=1.6, ly=4.2, lw=0.9, name='Glucosa a riñón', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(6.55, 2.75), (6.3, 3.45)], 'SNA', '7030A0', 2.5, 11, lx=5.75, ly=2.95, lw=0.55, name='SNA a páncreas', lbg='FFFFFF'))
    E.append(arrow_lbl(s, [(4.35, 5.4), (2.35, 5.4)], 'Na⁺ · volumen', INH, 2.5, 11.5, lx=2.6, ly=5.48, lw=1.3, name='Riñón a corazón', lbg='FFFFFF'))
    for k in ('liver', 'panc', 'adip', 'musc', 'kid', 'heart', 'brain'):
        pass
    if not final:
        s.step(pulse(P['panc']), fade(L['panc'], after=True))
        s.step(fade(E[0]), fade(E[1], after=True), fade(E[2], after=True))
        s.step(fade(E[4]), fade(E[3], after=True))
        s.step(fade(E[6]), fade(E[5], after=True), fade(E[7], after=True))
        box = pearl(s, 4.6, 6.2, 5.0, 0.85, 'La energía no circula por órganos aislados: el organismo funciona como una red metabólica, hormonal, neuronal y vascular.', 14)
        s.step(zoom(box))
    s.note('Mapa general de la red. El páncreas endocrino envía insulina y glucagón; el hígado recibe primero esas señales por '
           'la vena porta. La insulina actúa sobre hígado, músculo y tejido adiposo. El tejido adiposo devuelve información '
           '(leptina hacia el hipotálamo) y sustratos (ácidos grasos no esterificados y glicerol hacia el hígado). El sistema '
           'nervioso autónomo modula la secreción pancreática. El riñón filtra glucosa y, cuando la carga filtrada supera la '
           'reabsorción, aparece glucosuria; además regula sodio y volumen y conecta adiposidad, resistencia insulínica e '
           'hipertensión con el sistema cardiovascular. Animación: primero el páncreas, luego la acción insulínica en tres '
           'tejidos, luego las señales de vuelta del adipocito y finalmente el eje renal-cardiovascular.')


def ideas(D):
    s = new(D, U, 'Cinco ideas que organizan toda la clase', 'blue' if False else 'peach')
    items = [
        ('adipocyte-1', 'El **adipocito almacena y señaliza**: integra glucosa, ácidos grasos, insulina, catecolaminas y citocinas. La expansión **disfuncional** de grasa visceral favorece lipotoxicidad e inflamación.'),
        ('pancreas', 'La **insulina conecta órganos**: su **ausencia** activa cetogénesis (cetoacidosis); su **eficacia insuficiente** genera hiperglucemia, dislipidemia y DM2.'),
        ('brain-2', 'El **cerebro decide ingesta y gasto**: hipotálamo, tronco, circuitos mesolímbicos y sistema de estrés traducen hormonas y nutrientes en conducta alimentaria.'),
        ('kidney-1', 'El **riñón convierte hiperglucemia en deshidratación**: carga filtrada > reabsorción → glucosuria, diuresis osmótica y pérdida de agua y electrolitos.'),
        ('heart-front', 'La **enfermedad es sistémica**: resistencia insulínica, HTA, dislipidemia, esteatosis, apnea y aterosclerosis comparten vías, pero exigen evaluación **individual**.'),
    ]
    ids = []
    for i, (img, t) in enumerate(items):
        y = 1.15 + i * 1.18
        g = s.group_start('Idea %d' % (i + 1))
        s.shape(0.5, y, 0.75, 0.75, 'ellipse', BOX, (INK, 2), SHD, str(i + 1), 26, F_POP, BOXT, False, 'c', 'm', (0, 0, 0, 0), fit=False)
        fitpic(s, img, 1.4, y - 0.05, 1.25, 1.0)
        tbox(s, 2.75, y - 0.05, 10.15, 1.0, t, 15, anchor='m')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Mapa conceptual de toda la unidad en cinco ideas. 1) El adipocito no es un depósito pasivo: almacena triglicéridos y '
           'secreta señales. 2) La insulina es el conector: su ausencia explica la cetoacidosis y su eficacia insuficiente '
           'explica la hiperglucemia crónica y la DM2. 3) El cerebro integra señales periféricas en conducta alimentaria y gasto. '
           '4) El riñón traduce la hiperglucemia en pérdidas osmóticas de agua y electrolitos. 5) Las complicaciones comparten '
           'vías fisiopatológicas, pero el riesgo se evalúa en cada persona.')


def build(D):
    cover(D)
    route(D)
    code(D)
    network(D)
    ideas(D)
