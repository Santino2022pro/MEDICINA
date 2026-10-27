# -*- coding: utf-8 -*-
"""UNIDAD VI — Control neuroendocrino del apetito, peso y gasto energético (Secuencia E con Morph)"""
from base import *

U = 6


def div(D):
    def art(s):
        s.pic('brain-2', 10.6, 0.6, 2.5, name='Cerebro')
        s.pic('stomach', 11.0, 3.6, 1.8, name='Estómago')
        s.pic('adipocyte-1', 0.2, 4.7, 2.2, name='Adipocitos')
        model(s, 'glucosa', 0.2, 1.2, 2.0, name='Glc')
    divider(D, U, 'VI', 'APETITO, PESO Y\nGASTO ENERGÉTICO', 'Hipotálamo, tronco, recompensa y estrés',
            ['Balance y gasto energético', 'Secuencia E: del adipocito al núcleo arcuato', 'POMC/CART frente a AgRP/NPY', 'Leptina, insulina y grelina',
             'Saciedad: CCK, GLP-1, PYY, vago', 'Recompensa: VTA → accumbens', 'Serotonina, endocannabinoides, estrés', 'AMPK/mTOR, sueño y Mapa 6'], art,
            'Unidad VI. La regulación del peso no reside en un único «centro del hambre»: el hipotálamo integra señales de reservas '
            '(leptina, insulina), el tronco encefálico integra señales viscerales, el sistema mesolímbico aporta motivación y el eje '
            'del estrés modula todo el sistema. La obesidad no se reduce a falta de voluntad.')


def balance(D):
    s = new(D, U, 'Balance energético: ecuación necesaria, no suficiente', 'cyan')
    sc = s.group_start('Balanza')
    s.shape(5.9, 2.0, 1.5, 0.3, 'rect', INK, None, False)
    s.shape(6.5, 2.3, 0.3, 1.7, 'rect', INK, None, False)
    s.shape(2.0, 1.85, 9.3, 0.15, 'rect', '7F8C8D', (INK, 1), False, rot=-4)
    mbox(s, 1.6, 1.15, 3.2, 0.6, 'ENERGÍA INCORPORADA', 's', 15)
    mbox(s, 8.5, 1.15, 3.2, 0.6, 'ENERGÍA GASTADA', 'g', 15)
    s.group_end()
    f = formula(s, 0.4, 4.25, 12.55, 0.7, 'Δ reservas = energía incorporada − energía gastada (en intervalos prolongados)', 18)
    c = steps_panel(s, 0.4, 5.15, 12.55, ['Ingesta y gasto **no son independientes**: la restricción activa **hambre**, baja el **gasto espontáneo** y modifica el basal.',
                                          'Entorno alimentario, **sueño, estrés, fármacos, genética y recompensa** modulan el balance: «come menos y muévete más» ignora la compensación.'], 14.5, anim=False)[0]
    s.step(fade(f)); s.step(fade(c[0])); s.step(fade(c[1]))
    s.note('Principio termodinámico: el cambio de reservas resulta de la relación entre energía incorporada y gastada durante '
           'intervalos prolongados. Sin embargo, ingesta y gasto no son variables independientes: la restricción energética puede '
           'activar el hambre, disminuir el gasto espontáneo y modificar el gasto basal con la nueva masa corporal. El entorno '
           'alimentario, el sueño, el estrés, los medicamentos, la genética y la recompensa modulan el balance. «Come menos y muévete '
           'más» ignora los mecanismos compensatorios que dificultan sostener los cambios de peso [A].')


def get(D):
    s = new(D, U, 'Componentes del gasto energético total', 'pink')
    comps = [('Metabolismo en reposo / basal', 'Masa libre de grasa, órganos, edad, sexo', 2.2, 'F4877F'),
             ('Actividad física estructurada', 'Ejercicio planificado', 0.8, '9DC3E6'),
             ('NEAT', 'Estar de pie, caminar, posturas, actividad cotidiana', 0.9, '92D050'),
             ('Termogénesis de los alimentos', 'Efecto térmico de su procesamiento', 0.45, 'FFC000'),
             ('Termogénesis adaptativa', 'Frío · activación simpática', 0.3, 'C39BD3')]
    y = 6.6
    ids = []
    for i, (h, t, hh, c) in enumerate(comps):
        y -= hh
        g = s.group_start('Componente GET %d' % i)
        s.shape(0.9, y, 2.4, hh, 'rect', c, (INK, 1.5), False)
        s.arrow([(3.35, y + hh / 2), (4.0, y + hh / 2)], INK, 2)
        mbox(s, 4.1, y + hh / 2 - 0.27, 3.4, 0.54, h, 'w', 13, caps=False)
        s.text(7.65, y + hh / 2 - 0.27, 5.3, 0.54, t, 13.5, F_BODY, INK, False, 'l', 'm')
        ids.append(s.group_end())
    lab(s, 0.6, 1.45, 3.0, 0.4, 'GASTO ENERGÉTICO TOTAL', 13)
    p = pearl(s, 4.1, 6.15, 8.85, 0.7, 'Las alturas son **esquemáticas**: no se suman porcentajes fijos; cambian entre individuos y según el gasto total.', 14)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Componentes del gasto energético total: 1) metabolismo en reposo o basal, muy influido por la masa libre de grasa, los '
           'órganos, la edad y el sexo; 2) actividad física estructurada; 3) NEAT (non-exercise activity thermogenesis): estar de pie, '
           'caminar, posturas, actividad cotidiana; 4) termogénesis de los alimentos; 5) termogénesis adaptativa (frío, activación '
           'simpática). No se deben sumar porcentajes fijos rígidos: cambian entre individuos y según el gasto total. El artículo '
           '[A], figura 1, página 3, distingue señales de saciedad de corto plazo y adiposidad de largo plazo.')


def adaptation(D):
    s = new(D, U, 'Adaptación tras la pérdida de peso', 'lime')
    nodes = {
        'w': (0.4, 1.3, 3.0, 0.65, 'Pérdida de peso', 'y', 17),
        'l': (4.0, 1.2, 4.2, 0.6, 'Leptina ↓ (menos adiposo y energía)', 'Y', 13.5),
        'g': (4.0, 2.0, 4.2, 0.6, 'Grelina y otras señales ↑ → hambre ↑', 'Y', 13.5),
        'e': (4.0, 2.8, 4.2, 0.6, 'Gasto absoluto ↓ (menor masa)', 'Y', 13.5),
        'a': (4.0, 3.6, 4.2, 0.6, '± adaptación metabólica adicional', 'Y', 13.5),
        'r': (8.8, 2.0, 4.15, 1.4, 'Tendencia a recuperar peso: el mantenimiento requiere apoyo prolongado', 'r', 14),
    }
    edges = [('w', 'l', {'pts': [(3.45, 1.6), (3.95, 1.5)]}), ('w', 'g', {'pts': [(3.45, 1.7), (3.95, 2.3)]}), ('w', 'e', {'pts': [(3.45, 1.8), (3.95, 3.1)]}),
             ('w', 'a', {'pts': [(3.45, 1.9), (3.95, 3.9)]}), ('g', 'r'), ('e', 'r', {'pts': [(8.25, 3.1), (8.75, 2.9)]})]
    graph(s, nodes, edges, [['w'], ['w>l', 'l', 'w>g', 'g'], ['w>e', 'e', 'w>a', 'a'], ['g>r', 'e>r', 'r']])
    t = tbox(s, 0.4, 4.6, 12.55, 2.25, 'Estos mecanismos **no niegan** la conservación de la energía: explican por qué sostener el descenso requiere **estrategias conductuales y, cuando corresponde, farmacológicas** de largo plazo, y por qué la obesidad es **crónica y recidivante**.', 15.5, head='Interpretación')
    s.step(fade(t))
    s.note('Adaptación tras la pérdida de peso: la leptina disminuye al reducirse el tejido adiposo y la energía disponible; la grelina '
           'y otras respuestas pueden aumentar el hambre; el gasto absoluto desciende por menor masa corporal y en algunos casos '
           'aparece adaptación metabólica adicional. No niegan la conservación de energía: explican por qué el mantenimiento requiere '
           'apoyo prolongado y estrategias conductuales o farmacológicas cuando corresponda [A].')


# ---------------------------------------------------------------- Secuencia E (Morph)
def e1(D):
    s = new(D, U, 'Secuencia E · 1 · organismo y reservas', 'cyan')
    s.pic('Human_male', 1.0, 1.1, h=5.8, name='!!Organismo E')
    s.pic('adipocyte-1', 2.0, 3.5, 0.6, name='!!Adiposo E')
    s.pic('brain-2', 1.75, 1.1, 0.75, name='!!Cerebro E')
    c = s.shape(1.7, 3.3, 1.2, 1.0, 'ellipse', None, ('C00000', 3), False, name='!!Lupa E')
    t = tbox(s, 4.6, 1.3, 8.35, 2.0, 'El organismo necesita **informar al cerebro** cuánta energía tiene almacenada. Esa información proviene principalmente del **tejido adiposo** (leptina) y del **páncreas** (insulina).', 16, head='La pregunta')
    t2 = tbox(s, 4.6, 3.6, 8.35, 2.3, '- **Largo plazo**: leptina e insulina (reservas).\n- **Corto plazo**: grelina, CCK, GLP-1, PYY, distensión gástrica (comida a comida).\n- **Moduladores**: recompensa, estrés, sueño, entorno.', 15.5, head='Tres niveles de señal')
    s.step(zoom(c)); s.step(fade(t2))
    s.note('Secuencia E (Morph): organismo → tejido adiposo → leptina → hipotálamo → núcleo arcuato → neuronas POMC/AgRP → control del '
           'hambre. Punto de partida: el organismo informa al cerebro sus reservas (leptina, insulina) y su estado de comida a comida '
           '(grelina y señales de saciedad).')


def e2(D):
    s = new(D, U, 'Secuencia E · 2 · el adipocito secreta leptina', 'cyan', morph=True)
    s.pic('Human_male', -20.0, -9.0, h=34.0, name='!!Organismo E', transp=85)
    s.pic('adipocyte-1', 0.5, 1.2, 4.8, name='!!Adiposo E')
    s.pic('brain-2', 11.0, 0.9, 1.6, name='!!Cerebro E')
    lp = [s.shape(3.6 + i * 0.75, 2.3 + (i % 2) * 0.6, 0.55, 0.42, 'roundRect', 'C39BD3', ('5B2C6F', 1.25), False, 'Leptina', 8.5, F_HEAD, INK, True,
                  'c', 'm', (0, 0, 0, 0), fit=False, name='!!Leptina %d' % i) for i in range(4)]
    t = tbox(s, 5.9, 2.9, 7.0, 3.0, '- La **leptina** circulante se relaciona con la **cantidad de grasa** y el estado nutricional.\n- Señala **suficiencia de reservas**; permite funciones reproductivas, tiroideas e inmunitarias.\n- En ayuno y descenso rápido de energía puede **caer desproporcionadamente**.', 15, head='Leptina')
    s.step(*[zoom(l, after=i > 0, dur=200) for i, l in enumerate(lp)])
    s.step(fade(t))
    s.note('Paso 2. El adipocito blanco produce leptina en proporción a la masa grasa y al estado nutricional. La leptina señala '
           'suficiencia de reservas y permite funciones reproductivas, tiroideas e inmunitarias; en ayuno puede caer '
           'desproporcionadamente [A][T].')


def e3(D):
    s = new(D, U, 'Secuencia E · 3 · la leptina llega al hipotálamo', 'cyan', morph=True)
    s.pic('adipocyte-1', 0.4, 4.6, 1.8, name='!!Adiposo E')
    s.pic('brain-2', 5.3, 1.0, 4.4, name='!!Cerebro E')
    lp = [s.shape(1.9 + i * 0.6, 4.6 - i * 0.2, 0.55, 0.42, 'roundRect', 'C39BD3', ('5B2C6F', 1.25), False, 'Leptina', 8.5, F_HEAD, INK, True,
                  'c', 'm', (0, 0, 0, 0), fit=False, name='!!Leptina %d' % i) for i in range(4)]
    tgt = s.shape(7.15, 3.6, 0.8, 0.6, 'ellipse', None, ('C00000', 3), False, name='!!Lupa hipotálamo')
    t = tbox(s, 9.9, 1.2, 3.05, 4.4, 'Acceso por la región de la **eminencia media** cercana al **núcleo arcuato** y por transporte; alteraciones del **transporte o la señal central** contribuyen a la resistencia a la leptina.', 14, head='Llegada')
    s.step(*[path(l, 5.7 - i * 0.3, -0.75 + i * 0.25, dur=1600, delay=i * 200) for i, l in enumerate(lp)])
    s.step(zoom(tgt)); s.step(fade(t))
    s.note('Paso 3. La leptina viaja por la sangre hasta el hipotálamo. El núcleo arcuato, cercano a la eminencia media, recibe '
           'información hormonal y nutricional. La alteración del transporte o de la señal central es uno de los mecanismos de la '
           'resistencia a la leptina [A].')


BR = (0.4, 1.05, 7.3, 5.8)


def brain_sag(s, prefix='!!', box=None, labels=True):
    """corte sagital esquemático del encéfalo con núcleos del control del apetito"""
    x, y, w, h = box or BR
    out = smooth([(120, 520), (100, 380), (160, 240), (300, 130), (500, 90), (700, 120), (860, 230), (930, 400), (900, 560),
                  (800, 610), (660, 590), (560, 630), (450, 650), (330, 640), (200, 610)], True, 0.8)
    g = s.group_start(prefix + 'Encéfalo sagital')
    s.free(x, y, w, h, out, ('rad', [(0, 'FDEDEC'), (100, 'F1A7B5')], (45, 40)), ('A93226', 2.0))
    s.free(x, y, w, h, smooth([(300, 420), (450, 360), (620, 380), (720, 450)], False, 0.8), None, ('B03A2E', 6))
    s.free(x, y, w, h, smooth([(720, 610), (820, 600), (900, 660), (880, 760), (780, 790), (700, 720)], True, 0.8), ('rad', [(0, 'F5CBA7'), (100, 'DC7633')], (45, 40)), ('A04000', 1.5))
    s.free(x, y, w, h, smooth([(560, 600), (650, 610), (660, 760), (640, 960), (580, 960), (570, 760)], True, 0.6), ('lin', [(0, 'F5B7B1'), (100, 'E6B0AA')], 0), ('A93226', 1.5))
    s.shape(x + w * 0.395, y + h * 0.66, w * 0.07, h * 0.08, 'ellipse', 'D7BDE2', ('6C3483', 1.25), False)
    s.group_end()
    nuc = {'PFC': (0.22, 0.33, 'Corteza\nprefrontal'), 'NAc': (0.33, 0.5, 'N. accumbens'), 'VTA': (0.6, 0.66, 'ATV'),
           'HT': (0.44, 0.58, 'Hipotálamo'), 'NTS': (0.62, 0.82, 'NTS')}
    loff = {'PFC': (0.3, -0.2), 'NAc': (-2.05, -0.2), 'VTA': (0.3, -0.05), 'HT': (-0.85, 0.42), 'NTS': (0.3, -0.2)}
    ids = {}
    for k, (fx, fy, t) in nuc.items():
        cx, cy = x + w * fx, y + h * fy
        d = (0.42 if k != 'HT' else 0.6) * (w / BR[2])
        ids[k] = s.shape(cx - d / 2, cy - d / 2, d, d, 'ellipse', {'PFC': '5DADE2', 'NAc': 'F39C12', 'VTA': 'E74C3C', 'HT': BOX, 'NTS': '27AE60'}[k],
                         (INK, 1.5), SHD, name=prefix + 'Núcleo ' + k)
        if not labels:
            continue
        ids[k + 'l'] = s.shape(cx + loff[k][0], cy + loff[k][1], 1.7, 0.4, 'rect', WHITE, (INK, 1.0), False, t, 11.5, F_HEAD, INK, True, 'c', 'm', (0.03, 0, 0.03, 0),
                               name=prefix + 'Rótulo ' + k, minsize=8)
    return ids


def e4(D):
    s = new(D, U, 'Secuencia E · 4 · corte sagital: centros y circuitos', 'peach', morph=True)
    ids = brain_sag(s)
    t = tbox(s, 7.95, 1.15, 5.0, 4.6, '- **Hipotálamo**: balance energético (ARC, PVN, LHA, VMH, DMH).\n- **NTS (tronco)**: señales vagales digestivas + humorales.\n'
             '- **ATV → núcleo accumbens**: dopamina, motivación.\n- **Corteza prefrontal**: decisión y control ejecutivo.\n- No existe un único «centro del hambre».', 14.5, head='Red, no centro')
    pr = pearl(s, 7.95, 5.95, 5.0, 0.9, 'Hipotálamo = balance · tronco = vísceras · mesolímbico = motivación · corteza = decisión', 12.5)
    s.step(*[pulse(ids[k], after=i > 0) for i, k in enumerate(['HT', 'NTS', 'VTA', 'NAc', 'PFC'])])
    s.step(fade(t)); s.step(zoom(pr))
    s.note('Ilustración obligatoria: corte sagital esquemático del encéfalo con hipotálamo, núcleo del tracto solitario (tronco), área '
           'tegmental ventral, núcleo accumbens y corteza prefrontal. La regulación no reside en un único centro del hambre: el núcleo '
           'arcuato se conecta con el paraventricular, el hipotálamo lateral, las regiones ventromedial y dorsomedial, el tronco '
           'encefálico y los sistemas de recompensa. El NTS integra señales vagales gastrointestinales con señales humorales [A]. '
           'Idea fuerza: «hipotálamo = balance energético; tronco = señales viscerales; mesolímbico = motivación; corteza = '
           'decisión; adipocito = señal de reservas». La diapositiva siguiente hace un acercamiento Morph al núcleo arcuato.')


def arc_scene(s, mode):
    """mode: 0 escena · 1 POMC activa · 2 AgRP activa"""
    s.shape(0.4, 1.1, 7.6, 5.75, 'roundRect', ('rad', [(0, 'FDF2E9'), (100, 'F5CBA7')], (50, 50)), ('A04000', 2), SHD, adj={'adj': 8000},
            name='!!Núcleo Hipotálamo ampliado')
    s.shape(0.4, 5.75, 7.6, 1.1, 'rect', ('lin', [(0, 'D6EAF8'), (100, 'AED6F1')], 90), (INK, 1.0), False, 'Eminencia media · capilares fenestrados', 12, F_HEAD, INK, True, 'c', 'm',
            name='!!Eminencia media')
    s.shape(3.85, 1.1, 0.7, 4.65, 'rect', ('lin', [(0, 'D6EAF8'), (100, 'EBF5FB')], 0), None, False, '3.er\nventrículo', 10, F_HEAD, '1F618D', True, 'c', 'm', name='!!Tercer ventrículo')
    lab(s, 0.55, 4.55, 3.0, 0.35, 'NÚCLEO ARCUATO', 13, name='!!Rótulo ARC')
    pomc = s.shape(0.7, 3.25, 1.35, 1.2, 'ellipse', shade('58D68D', 0.4, 0.3), ('1D8348', 2.5 if mode == 1 else 1.25), SHD, 'POMC\nCART', 13, F_HEAD, INK, True, 'c', 'm', fit=False,
                   name='!!Neurona POMC')
    agrp = s.shape(2.3, 3.6, 1.35, 1.2, 'ellipse', shade('EC7063', 0.4, 0.3), ('922B21', 2.5 if mode == 2 else 1.25), SHD, 'AgRP\nNPY', 13, F_HEAD, INK, True, 'c', 'm', fit=False,
                   name='!!Neurona AgRP')
    pvn = s.shape(4.9, 1.45, 1.75, 1.4, 'ellipse', shade('5DADE2', 0.4, 0.3), ('1F618D', 1.5), SHD, 'PVN\nMC4R', 14, F_HEAD, INK, True, 'c', 'm', fit=False,
                  name='!!Neurona PVN')
    a1 = s.arrow([(1.6, 3.2), (4.85, 2.25)], ACT if mode == 1 else '7F8C8D', 3.5 if mode == 1 else 1.5, name='!!Axón POMC')
    a2 = s.arrow([(3.3, 3.55), (4.95, 2.75)], INH if mode == 2 else '7F8C8D', 3.5 if mode == 2 else 1.5, name='!!Axón AgRP')
    a3 = s.inhib([(2.3, 4.05), (2.05, 3.95)], INH if mode == 2 else '7F8C8D', 3.0 if mode == 2 else 1.5, name='!!GABA a POMC')
    out = s.shape(4.7, 3.4, 3.0, 1.0, 'rect', ('C00000' if mode == 2 else ('00A651' if mode == 1 else WHITE)), (INK, 1.5), False,
                  {0: 'Salida melanocortínica', 1: 'Ingesta ↓ · gasto ↑', 2: 'HAMBRE ↑'}[mode], 15, F_HEAD, WHITE if mode else INK, True, 'c', 'm',
                  name='!!Salida ARC')
    return {'pomc': pomc, 'agrp': agrp, 'pvn': pvn, 'a1': a1, 'a2': a2, 'out': out}


def e5(D):
    s = new(D, U, 'Secuencia E · 5 · núcleo arcuato: dos poblaciones', 'peach', morph=True)
    k = 6.0
    brain_sag(s, box=(4.2 - 0.44 * BR[2] * k, 3.9 - 0.58 * BR[3] * k, BR[2] * k, BR[3] * k), labels=False)
    ids = arc_scene(s, 0)
    t = tbox(s, 8.3, 1.15, 4.65, 5.7, '- **POMC/CART** (anorexígenas) y **AgRP/NPY/GABA** (orexígenas) en el ARC.\n- Ambas proyectan a neuronas de **segundo orden** del **PVN**, que expresan **MC4R**.\n'
             '- Leptina e insulina **estimulan POMC** e **inhiben AgRP**; la grelina **activa AgRP**.\n- El equilibrio **no es aritmético**: importan tiempo de disparo, plasticidad, aprendizaje y señales del tronco.', 14.5, head='Dos poblaciones')
    s.step(pulse(ids['pomc']), pulse(ids['agrp'], after=True), pulse(ids['pvn'], after=True))
    s.step(fade(t))
    s.note('Paso 5 de la secuencia E: acercamiento Morph desde el corte sagital al núcleo arcuato (junto al tercer ventrículo y la '
           'eminencia media). Dos poblaciones principales: neuronas POMC/CART (anorexígenas) y neuronas AgRP/NPY/GABA (orexígenas). '
           'Ambas proyectan a neuronas de segundo orden del núcleo paraventricular que expresan MC4R. La figura 2 de la página 4 del '
           'artículo [A] compara ambas poblaciones y su salida melanocortínica.')


def pomc(D):
    s = new(D, U, 'Ejemplo 6 · vía POMC: señal anorexígena', 'peach', morph=True)
    ids = arc_scene(s, 1)
    nodes = {
        'l': (8.3, 1.15, 2.0, 0.55, 'Leptina', 's', 15), 'i': (10.95, 1.15, 2.0, 0.55, 'Insulina', 's', 15),
        'r': (8.3, 1.95, 4.65, 0.55, 'LEPRb → JAK2–STAT3 · IRS–PI3K/Akt', 'g', 13),
        'p': (8.3, 2.75, 4.65, 0.55, 'POMC → convertasas (PC1/3) → α-MSH', 'y', 13),
        'm': (8.3, 3.55, 4.65, 0.55, 'α-MSH activa MC4R (PVN)', 'g', 14),
        'o': (8.3, 4.35, 4.65, 0.65, 'Ingesta ↓ · respuestas autonómicas · gasto ↑', 'r', 13),
    }
    edges = [('l', 'r'), ('i', 'r'), ('r', 'p'), ('p', 'm'), ('m', 'o')]
    graph(s, nodes, edges, [['l', 'i'], ['l>r', 'i>r', 'r'], ['r>p', 'p'], ['p>m', 'm'], ['m>o', 'o']])
    ms = [s.shape(1.9 + i * 0.7, 3.05 - i * 0.25, 0.55, 0.32, 'roundRect', '58D68D', ('1D8348', 1.0), False, 'α-MSH', 8, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                  name='aMSH %d' % i) for i in range(3)]
    t = tbox(s, 8.3, 5.2, 4.65, 1.65, '**Setmelanotida** (agonista MC4R) trata subgrupos de obesidad **genética definida**, no la obesidad común.', 13.5)
    s.step(*[fade(m, after=i > 0, dur=150) for i, m in enumerate(ms)], *[path(m, 4.9 - (1.9 + i * 0.7), 2.2 - (3.05 - i * 0.25), dur=1400, delay=i * 200) for i, m in enumerate(ms)])
    s.step(fade(t))
    s.note('Ejemplo 6, rama anorexígena. La leptina favorece la actividad POMC por LEPRb–JAK2–STAT3; la insulina puede modularla por '
           'IRS–PI3K/Akt, con acciones dependientes de la población neuronal. La prohormona POMC se procesa mediante convertasas y '
           'genera, entre otros, α-MSH, que activa receptores de melanocortina, especialmente MC4R, en neuronas de segundo orden: '
           'reduce la ingesta y favorece respuestas autonómicas y gasto (animación: las fichas α-MSH viajan al PVN). Agonistas '
           'específicos de MC4R constituyen un tratamiento para subgrupos de obesidad genética definida, no para la obesidad común [A].')


def agrp(D):
    s = new(D, U, 'Ejemplo 6 · vía AgRP/NPY: señal orexígena (en paralelo)', 'peach', morph=True)
    ids = arc_scene(s, 2)
    nodes = {
        'g': (8.3, 1.15, 4.65, 0.55, 'Grelina (GHSR) · déficit energético', 's', 13.5),
        'a': (8.3, 1.95, 4.65, 0.55, 'Neuronas AgRP/NPY/GABA activas', 'y', 13.5),
        'n': (8.3, 2.75, 2.25, 0.6, 'NPY → Y1/Y5', 'g', 13), 'ag': (10.7, 2.75, 2.25, 0.6, 'AgRP ⊣ MC3R/MC4R', 'g', 12),
        'gb': (8.3, 3.55, 4.65, 0.55, 'GABA inhibe POMC y dianas', 'g', 13),
        'o': (8.3, 4.35, 4.65, 0.65, 'HAMBRE y búsqueda de alimento ↑', 'r', 14),
    }
    edges = [('g', 'a'), ('a', 'n'), ('a', 'ag'), ('n', 'gb', {'pts': [(9.4, 3.38), (9.4, 3.52)]}), ('gb', 'o')]
    graph(s, nodes, edges, [['g', 'g>a', 'a'], ['a>n', 'n', 'a>ag', 'ag'], ['n>gb', 'gb'], ['gb>o', 'o']])
    lepi = s.group_start('Leptina inhibe AgRP')
    s.inhib([(1.4, 5.65), (2.8, 4.85)], INH, 3.0)
    s.shape(0.6, 5.25, 1.3, 0.42, 'roundRect', 'C39BD3', ('5B2C6F', 1.25), False, 'Leptina', 11, F_HEAD, INK, True, 'c', 'm', fit=False)
    s.group_end()
    t = tbox(s, 8.3, 5.2, 4.65, 1.65, '**Homeostático**: compara reservas y necesidades. Los sistemas **hedónicos** pueden impulsar la ingesta sin déficit (diapositivas siguientes).', 13.5)
    s.step(fade(lepi)); s.step(fade(t))
    s.note('Ejemplo 6, rama orexígena, que opera en paralelo a la anterior (no es una secuencia obligatoria). Las neuronas NPY/AgRP '
           'promueven el hambre en el déficit energético: NPY activa receptores Y (Y1/Y5); AgRP antagoniza MC3R/MC4R y contrarresta '
           'a α-MSH; la liberación de GABA inhibe neuronas diana (incluidas POMC) y contribuye a la respuesta rápida. La grelina '
           'activa fuertemente estos circuitos mediante GHSR; la leptina los inhibe. El equilibrio no es aritmético [A].')


def leptin(D):
    s = new(D, U, 'Leptina: señal de reservas y resistencia funcional', 'lime')
    nodes = {
        'l': (0.4, 1.2, 2.6, 0.6, 'Leptina', 'y', 17),
        'r': (3.5, 1.2, 3.0, 0.6, 'LEPRb (isoforma larga)', 'g', 14),
        'j': (7.0, 1.2, 2.6, 0.6, 'JAK2 → STAT3', 'g', 15),
        'p': (10.1, 1.2, 2.85, 0.6, 'PI3K · MAPK', 'g', 15),
        'o': (7.0, 2.2, 5.95, 0.6, 'POMC ↑ · NPY/AgRP ↓ (según circuito)', 'Y', 14),
        's': (0.4, 2.2, 6.1, 0.6, 'Freno: SOCS3 · PTP1B', 'r', 14),
    }
    edges = [('l', 'r'), ('r', 'j'), ('r', 'p', {'pts': [(5.0, 1.15), (5.0, 0.98), (11.5, 0.98), (11.5, 1.15)]}), ('j', 'o'), ('s', 'j', {'inh': True, 'pts': [(6.55, 2.5), (7.6, 2.5), (7.6, 1.85)]})]
    graph(s, nodes, edges, [['l', 'l>r', 'r', 'r>j', 'j', 'r>p', 'p'], ['j>o', 'o'], ['s', 's>j']])
    res = tbox(s, 0.4, 3.15, 6.1, 3.7, '- **Transporte** o señal central alterados.\n- **SOCS3** y **PTP1B** (frenos de la vía).\n- **Inflamación hipotalámica**.\n- Cambios de **circuitos**.', 15, head='Resistencia a la leptina en obesidad común')
    pr = pearl(s, 6.85, 3.15, 6.1, 1.8, 'Leptina **alta** con respuesta **ineficaz**: no suponer **deficiencia absoluta** en toda obesidad.', 15.5)
    t = tbox(s, 6.85, 5.15, 6.1, 1.7, 'La leptina **recombinante** es útil en deficiencias **congénitas** de leptina, no como supresor general del apetito.', 14.5)
    s.step(fade(res)); s.step(zoom(pr)); s.step(fade(t))
    s.note('Leptina: producida principalmente por adipocitos; se une a la isoforma larga LEPRb, activa JAK2/STAT3 y rutas PI3K/MAPK; '
           'estimula POMC y reduce NPY/AgRP según los circuitos. En la obesidad común la leptina suele estar alta pero hay resistencia '
           'a sus acciones, atribuible a alteración del transporte o de la señal central, SOCS3, PTP1B, inflamación hipotalámica y '
           'cambios de circuitos. No es apropiado suponer deficiencia absoluta de leptina en toda obesidad; la leptina recombinante '
           'es útil en determinadas deficiencias congénitas [A][T].')


def insulin_ghrelin(D):
    s = new(D, U, 'Insulina central y grelina', 'blue')
    l = s.group_start('Insulina central')
    mbox(s, 0.4, 1.2, 6.0, 0.6, 'INSULINA COMO SEÑAL CENTRAL', 'y', 15)
    tbox(s, 0.4, 1.9, 6.0, 3.0, '- Informa al SNC la **disponibilidad energética** a largo plazo.\n- Receptores **hipotalámicos y mesolímbicos**: saciedad, ingesta, función autonómica.\n'
         '- La señal IRS–PI3K/Akt neuronal **no equivale** a la del músculo.\n- **Resistencia central** puede coexistir con **hiperinsulinemia periférica**.\n- Modula el **transportador de dopamina** y la recompensa.', 14)
    s.group_end()
    r = s.group_start('Grelina')
    mbox(s, 6.85, 1.2, 6.1, 0.6, 'GRELINA (GHRELINA)', 's', 15)
    s.pic('stomach', 6.95, 1.95, 1.7, name='Estómago grelina')
    tbox(s, 8.8, 1.9, 4.15, 3.0, '- **Fundus gástrico**; acilada por **GOAT** → **GHSR1a**.\n- **Sube antes** de comer y baja después (dinámica cambia con obesidad y cirugía).\n- Activa **NPY/AgRP**, apetito, búsqueda y **GH**.', 13.5)
    s.group_end()
    p = pearl(s, 0.4, 5.15, 12.55, 1.7, 'La **grelina desacilada** tiene biología propia y no es idéntica a la activa. Término correcto: **grelina/ghrelina** (no «GHrelina»).', 15.5)
    s.step(fade(l)); s.step(fade(r)); s.step(zoom(p))
    s.note('Insulina como señal central: informa disponibilidad energética a largo plazo; sus receptores hipotalámicos y mesolímbicos '
           'modulan saciedad, ingesta y función autonómica; la señal neuronal no equivale a la muscular; la resistencia central puede '
           'coexistir con hiperinsulinemia periférica; puede modular el transportador de dopamina. Grelina: producida sobre todo en '
           'células endocrinas del fundus; su forma acilada por GOAT activa GHSR1a; asciende antes de las comidas y desciende '
           'después; activa NPY/AgRP, favorece apetito, búsqueda alimentaria y secreción de GH. La guía escribe «GHrelina»: el '
           'término correcto es grelina/ghrelina [A].')


def satiety(D):
    s = new(D, U, 'Saciedad de corto plazo: eje intestino–vago–tronco', 'cyan')
    s.pic('stomach', 0.4, 3.6, 1.8, name='Estómago sac')
    s.pic('small-intestine', 2.3, 4.6, 1.9, name='Intestino sac')
    s.pic('pancreas', 0.6, 6.0, 1.9, name='Páncreas sac')
    hs = [('CCK', 'Células I duodeno/yeyuno (grasas, proteínas) → CCK1 en aferencias vagales: tamaño de comida ↓, vaciamiento ↓, secreción pancreática y vesicular'),
          ('GLP-1', 'Células L → GLP-1R (Gs–AMPc–PKA/Epac): insulina glucosa-dependiente, glucagón ↓, vaciamiento ↓, saciedad'),
          ('GIP', 'Células K → GIPR: insulina glucosa-dependiente; base de los agonistas duales'),
          ('PYY₃₋₃₆', 'Células L posprandiales → receptores Y2: inhibe actividad orexígena'),
          ('Oxintomodulina', 'Derivada de proglucagón; receptores relacionados con saciedad'),
          ('Amilina', 'Cosecretada con insulina (β): saciedad, glucagón ↓, vaciamiento ↓ (área postrema/NTS)')]
    ids = []
    for i, (h, t) in enumerate(hs):
        y = 1.15 + i * 0.78
        g = s.group_start('Señal ' + h)
        mbox(s, 4.4, y, 1.7, 0.66, h, 's', 14, caps=False)
        tbox(s, 6.2, y, 6.75, 0.66, t, 12, anchor='m', minsize=9)
        ids.append(s.group_end())
    br = s.group_start('Vago NTS')
    s.pic('brain-2', 1.05, 1.1, 1.85, name='Cerebro sac')
    s.arrow([(1.3, 3.65), (1.6, 2.95)], '7030A0', 4)
    lab(s, 0.4, 2.95, 1.0, 0.6, 'vago\n→ NTS', 12, '7030A0')
    s.group_end()
    s.step(fade(br))
    for g in ids:
        s.step(fade(g))
    s.note('Señales de saciedad de corto plazo. CCK: liberada por células I duodenales/yeyunales tras grasas y proteínas; activa CCK1 '
           'en aferencias vagales y circuitos troncoencefálicos, disminuye el tamaño de la comida y enlentece el vaciamiento gástrico, '
           'además de estimular secreción pancreática y contracción vesicular; no mide reservas. GLP-1: células L, GLP-1R '
           '(Gs–AMPc–PKA/Epac): insulina dependiente de glucosa, menos glucagón en hiperglucemia, vaciamiento más lento y saciedad por '
           'circuitos vagales y centrales. GIP: células K, GIPR. PYY3-36: receptores Y2, inhibe la actividad orexígena. '
           'Oxintomodulina: comparte origen con proglucagón. Amilina: cosecretada con insulina; área postrema/NTS [A]. La distensión '
           'gástrica y las aferencias vagales llevan la información al NTS.')


def reward(D):
    s = new(D, U, 'Recompensa: homeostático frente a hedónico', 'pink')
    br = brain_sag(s, prefix='')
    da = s.arrow([(0.4 + 7.3 * 0.57, 1.05 + 5.8 * 0.62), (0.4 + 7.3 * 0.36, 1.05 + 5.8 * 0.5)], 'C00000', 5, name='Vía dopaminérgica', curve=False)
    da2 = s.arrow([(0.4 + 7.3 * 0.57, 1.05 + 5.8 * 0.60), (0.4 + 7.3 * 0.25, 1.05 + 5.8 * 0.35)], 'C00000', 3, dash='dash', name='Vía a corteza')
    lab(s, 2.4, 4.15, 1.6, 0.32, 'DOPAMINA', 12, INH)
    t1 = tbox(s, 7.95, 1.15, 5.0, 2.6, '- Dopamina = **saliencia motivacional**, aprendizaje por recompensa, selección de acciones.\n- **No** es idéntica al placer subjetivo ni equivale a «adicción» ante cualquier comida apetecible.', 14, head='ATV → accumbens')
    t2 = tbox(s, 7.95, 3.95, 5.0, 1.85, 'Alimentos **palatables**, señales **condicionadas**, estrés y expectativa pueden activar la búsqueda **sin déficit** homeostático.', 14, head='Hedónico')
    p = pearl(s, 7.95, 6.0, 5.0, 0.85, 'La obesidad **no es falta de voluntad**: biología + entorno + aprendizaje.', 13.5)
    s.step(wipe(da, 'r'), wipe(da2, 'r', after=True)); s.step(fade(t1)); s.step(fade(t2)); s.step(zoom(p))
    s.note('Dopamina y recompensa: las neuronas del área tegmental ventral proyectan al núcleo accumbens, la corteza prefrontal y otras '
           'estructuras. La dopamina atribuye saliencia motivacional, aprendizaje por recompensa y selección de acciones; no es idéntica '
           'al placer subjetivo ni equivale a adicción ante cualquier comida apetecible. Alimentos palatables, señales condicionadas, '
           'estrés y expectativa pueden activar circuitos de búsqueda aun cuando las señales homeostáticas no indican déficit. El '
           'hipotálamo modula estos circuitos y viceversa [A]. Por eso la obesidad no se reduce a falta de voluntad.')


def sero_cb(D):
    s = new(D, U, 'Serotonina y sistema endocannabinoide', 'lime')
    l = s.group_start('Serotonina')
    mbox(s, 0.4, 1.2, 6.0, 0.6, 'SEROTONINA (5-HT)', 'g', 15)
    formula(s, 0.4, 1.95, 6.0, 0.6, 'Triptófano → (TPH) 5-HTP → (descarboxilasa) 5-HT', 13.5)
    tbox(s, 0.4, 2.7, 6.0, 2.6, '- **5-HT2C** en ciertas neuronas **activa POMC** → ingesta ↓.\n- Otros subtipos tienen acciones **diferentes u opuestas**.\n- La 5-HT corporal es mayormente **periférica** y no cruza libremente la BHE.\n- No es simplemente «hormona de saciedad».', 13.5)
    s.group_end()
    r = s.group_start('Endocannabinoides')
    mbox(s, 6.85, 1.2, 6.1, 0.6, 'ANANDAMIDA (AEA) · 2-AG', 's', 15)
    formula(s, 6.85, 1.95, 6.1, 0.6, 'Fosfolípidos → a demanda → AEA / 2-AG → CB1', 13.5)
    tbox(s, 6.85, 2.7, 6.1, 2.6, '- **CB1**: SNC y tejidos periféricos; modula liberación presináptica, apetito, recompensa, metabolismo.\n- **CB2**: inmunidad.\n'
         '- Degradación: **FAAH** (AEA) y **MAGL** (2-AG).\n- CB1 suele **promover ingesta** y lipogénesis en ciertos tejidos.', 13.5)
    s.group_end()
    p = pearl(s, 0.4, 5.55, 12.55, 1.3, '**Rimonabant** (antagonista/inverso CB1) reducía peso, pero fue **retirado por efectos psiquiátricos graves** (ANMAT, Disp. 6238/2008): **no es tratamiento vigente**.', 15)
    s.step(fade(l)); s.step(fade(r)); s.step(zoom(p))
    s.note('Serotonina: participa en múltiples funciones; en ciertas neuronas el receptor 5-HT2C favorece la activación de POMC y la '
           'reducción de la ingesta; otros subtipos tienen acciones distintas u opuestas. Síntesis cerebral: triptófano hidroxilasa → '
           '5-HTP → descarboxilasa → 5-HT; la mayor parte es periférica. Anandamida y 2-AG son lípidos señalizadores producidos a '
           'demanda que actúan sobre CB1 (SNC y periferia) y CB2 (inmunidad); FAAH y MAGL los degradan. La activación de CB1 suele '
           'promover la ingesta. Rimonabant fue retirado por efectos psiquiátricos graves; no debe plantearse como tratamiento vigente '
           '[A][ANMAT].')


def stress(D):
    s = new(D, U, 'Estrés, cortisol y otras señales centrales', 'blue')
    nodes = {
        'st': (0.4, 1.2, 2.3, 0.6, 'Estrés', 's', 16), 'crh': (3.1, 1.2, 2.3, 0.6, 'CRH (hipotálamo)', 'w', 13.5),
        'acth': (5.8, 1.2, 2.6, 0.6, 'ACTH (de POMC hipofisario)', 'w', 12.5), 'cor': (8.8, 1.2, 2.2, 0.6, 'Cortisol', 'y', 16),
        'gr': (11.3, 1.2, 1.65, 0.6, 'GR nuclear', 'g', 13),
        'ef': (5.8, 2.15, 7.15, 0.75, 'Sustratos ↑ · gluconeogénesis · respuesta vascular a catecolaminas; crónico: adiposidad central, apetito ↑, músculo ↓, HTA, hiperglucemia', 'Y', 12),
    }
    edges = [('st', 'crh'), ('crh', 'acth'), ('acth', 'cor'), ('cor', 'gr'), ('cor', 'ef')]
    graph(s, nodes, edges, [['st', 'st>crh', 'crh', 'crh>acth', 'acth', 'acth>cor', 'cor', 'cor>gr', 'gr'], ['cor>ef', 'ef']])
    c = tbox(s, 0.4, 2.15, 5.1, 2.0, 'ACTH no es por sí misma una hormona orexígena principal. CRH **aguda** puede **reducir** el apetito; estrés **crónico** y recompensa pueden **aumentarlo**.', 13, head='Sin un único sentido')
    oth = [('Oxitocina', 'PVN/supraóptico: saciedad en circuitos hipotalámicos/tronco; no es terapia adelgazante'),
           ('Orexina A/B', 'Hipotálamo lateral: vigilia, motivación, alimentación'), ('MCH', 'Hipotálamo lateral: favorece ingesta'),
           ('Histamina H1', 'Suprime apetito; el bloqueo H1 de fármacos puede aumentar peso'), ('Opioides endógenos', 'Aspectos hedónicos y palatabilidad')]
    ids = []
    for i, (h, t) in enumerate(oth):
        y = 4.35 + i * 0.5
        g = s.group_start('Otra ' + h)
        mbox(s, 0.4, y, 2.4, 0.44, h, 'b', 12, caps=False)
        s.text(2.95, y, 10.0, 0.44, t, 12.5, F_BODY, INK, False, 'l', 'm')
        ids.append(s.group_end())
    s.step(fade(c))
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids)])
    s.note('Vía del estrés: estímulos de estrés → CRH hipotalámica → ACTH adenohipofisaria derivada de POMC → cortisol de la zona '
           'fasciculada → receptor glucocorticoide nuclear. El cortisol aumenta la disponibilidad de sustratos y la gluconeogénesis; la '
           'exposición crónica excesiva promueve adiposidad central, apetito, pérdida muscular, HTA e hiperglucemia. Ante signos '
           'típicos de hipercortisolismo se valora Cushing de forma específica, sin asumirlo por obesidad común. Oxitocina, orexinas, '
           'MCH, histamina H1, norepinefrina (efecto dependiente de receptor y sitio) y opioides endógenos completan la red [A].')


def ampk_sleep(D):
    s = new(D, U, 'Sensores de nutrientes y sueño', 'peach')
    l = s.group_start('AMPK mTOR')
    mbox(s, 0.4, 1.2, 2.9, 0.6, 'AMPK', 'y', 17)
    tbox(s, 0.4, 1.9, 2.9, 2.2, 'AMP/ADP ↑ (déficit). En ciertos circuitos **hipotalámicos** favorece el **apetito**; en **músculo**, oxidación y captación de glucosa.', 13)
    mbox(s, 3.5, 1.2, 2.9, 0.6, 'mTORC1', 'g', 17)
    tbox(s, 3.5, 1.9, 2.9, 2.2, 'Responde a aminoácidos, energía e insulina; anabólico; en redes hipotalámicas puede relacionarse con **saciedad**.', 13)
    pearl(s, 0.4, 4.3, 6.0, 1.25, 'No trasladar sin matices los efectos de AMPK del **músculo** al **hipotálamo**: depende del tipo neuronal.', 13.5)
    s.group_end()
    r = s.group_start('Sueño')
    mbox(s, 6.85, 1.2, 6.1, 0.6, 'SUEÑO, RITMO CIRCADIANO Y APNEA', 's', 15)
    tbox(s, 6.85, 1.9, 6.1, 2.2, '**Deprivación de sueño**: apetito, control ejecutivo, sensibilidad insulínica, eje HPA y cronobiología alterados; los cambios de grelina/leptina **no son uniformes** entre estudios.', 13.5)
    tbox(s, 6.85, 4.3, 6.1, 1.25, '**AOS**: despertares, hipoxemia intermitente y activación simpática → **HTA y resistencia insulínica**.', 13.5)
    s.group_end()
    c = tbox(s, 0.4, 5.75, 12.55, 1.1, 'Caso 20: ronquido intenso y **somnolencia diurna** con 170 kg exigen evaluación clínica y, típicamente, **estudio de sueño**.', 14.5, anchor='m')
    s.step(fade(l)); s.step(fade(r)); s.step(fade(c))
    s.note('Sensores de nutrientes: AMPK reconoce bajo estado energético celular y ajusta catabolismo/anabolismo; en ciertos circuitos '
           'hipotalámicos favorece el apetito, en músculo activa oxidación y captación de glucosa. mTORC1 responde a aminoácidos, '
           'energía e insulina; en redes hipotalámicas puede relacionarse con saciedad. El esquema de la figura 3, página 7, de [A] '
           'representa el modelo simplificado AMPK (déficit → orexigénesis) y mTOR (abundancia → anorexigénesis). Sueño: la '
           'deprivación altera apetito, regulación ejecutiva, sensibilidad a insulina, eje HPA y cronobiología. La apnea obstructiva '
           'del sueño produce despertares, hipoxemia intermitente y activación simpática, agravando HTA y resistencia insulínica.')


ORG6 = [('stomach', 0.4, 1.1, 1.6, 'ESTÓMAGO', 0.45, 2.75),
        ('small-intestine', 0.45, 3.4, 1.6, 'INTESTINO', 0.45, 5.05),
        ('adipocyte-1', 11.0, 1.1, 1.8, 'TEJIDO ADIPOSO', 10.85, 2.95),
        ('pancreas', 10.75, 4.0, 2.2, 'PÁNCREAS', 11.1, 4.95),
        ('brain-2', 5.4, 1.05, 2.4, 'CEREBRO', 5.95, 3.5)]


def map6(D):
    stages = [
        [('a', [(2.05, 1.8), (5.35, 2.0)], 'grelina ↑ (antes)', '7030A0'),
         ('a', [(2.1, 4.1), (5.6, 3.0)], 'CCK · GLP-1 · PYY · vago', ACT, (2.6, 3.95)),
         ('a', [(10.95, 1.9), (7.85, 2.0)], 'leptina', ACT),
         ('a', [(10.7, 4.4), (7.7, 2.9)], 'insulina · amilina', ACT, (8.1, 3.85))],
        [('b', 3.2, 4.65, 3.0, 0.55, 'ARC: POMC ⇄ AgRP → PVN', 'y', 12.5),
         ('b', 6.45, 4.65, 3.1, 0.55, 'NTS · ATV → accumbens', 'g', 12.5),
         ('t', 3.2, 5.35, 6.35, 0.95, 'Salidas: **apetito/saciedad**, **gasto energético** (simpático, NEAT), **conducta alimentaria**', 12.5)],
    ]
    map_series(D, U, 'Mapa 6 · control del peso', 'lime', ORG6, stages,
               ['Mapa 6, etapa 1. Señales de entrada: el estómago envía grelina antes de comer; durante y después de la comida, el '
                'intestino informa por CCK, GLP-1, PYY y el vago; el tejido adiposo informa reservas con leptina y el páncreas con '
                'insulina y amilina.',
                'Mapa 6, etapa 2. El cerebro integra: el núcleo arcuato (POMC frente a AgRP) proyecta al paraventricular; el NTS integra '
                'señales viscerales y el circuito ATV → accumbens aporta motivación. Resultan apetito o saciedad, gasto energético y '
                'conducta alimentaria.'],
               'Mapa 6 completo: tracto gastrointestinal + tejido adiposo + páncreas → cerebro → apetito, saciedad, gasto energético y '
               'conducta alimentaria.',
               (0.4, 6.45, 12.55, 0.45, 'Tubo digestivo + adiposo + páncreas → **cerebro** → apetito, saciedad, gasto y conducta.', 14),
               ['señales de entrada', 'integración y salida'])


def timeline(D):
    s = new(D, U, 'Corto y largo plazo: integración del control', 'cyan')
    seg = [('ANTES DE COMER', 'Grelina y circuitos **anticipatorios** amplifican la búsqueda; señales de baja disponibilidad facilitan AgRP.', 's'),
           ('DURANTE LA COMIDA', '**Distensión gástrica**, vago, **CCK, GLP-1, PYY** modulan NTS e hipotálamo para **terminar** el episodio.', 'g'),
           ('SEMANAS / MESES', '**Leptina, insulina**, cambio de masa grasa y gasto modifican la **«ganancia»** del sistema.', 'y'),
           ('SOBRE TODO EL SISTEMA', 'Condicionamiento, **recompensa**, **estrés**, descanso, ambiente social, fármacos y acceso a alimentos.', 'b')]
    ids = []
    for i, (h, t, k) in enumerate(seg):
        x = 0.4 + i * 3.17
        g = s.group_start('Plazo ' + h)
        mbox(s, x, 1.25, 3.0, 0.75, h, k, 14)
        tbox(s, x, 2.1, 3.0, 2.6, t, 14, anchor='m')
        if i < 3:
            s.arrow([(x + 3.02, 1.62), (x + 3.15, 1.62)], INK, 3)
        ids.append(s.group_end())
    p = pearl(s, 0.4, 4.95, 12.55, 1.9, 'La obesidad aparece cuando la **ingesta acumulada excede el gasto de manera sostenida** dentro de un sistema que **responde y se adapta**. No reducir la obesidad a la voluntad: omite regulación hormonal, recompensa y entorno.', 16)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Integración del control de corto y largo plazo [A]. Antes de comer: grelina y circuitos anticipatorios amplifican la '
           'búsqueda. Durante la comida: distensión gástrica, aferencias vagales, CCK, GLP-1 y PYY modulan NTS e hipotálamo para '
           'terminar el episodio. En semanas/meses: leptina, insulina, cambio de masa grasa y gasto modifican la ganancia del sistema. '
           'Sobre ese sistema: condicionamiento, recompensa dopaminérgica, estrés, descanso, ambiente social, fármacos y acceso a '
           'alimentos. La obesidad aparece cuando la ingesta acumulada excede el gasto de manera sostenida dentro de un sistema que '
           'responde y se adapta.')


def build(D):
    div(D)
    balance(D)
    get(D)
    adaptation(D)
    e1(D)
    e2(D)
    e3(D)
    e4(D)
    e5(D)
    pomc(D)
    agrp(D)
    leptin(D)
    insulin_ghrelin(D)
    satiety(D)
    reward(D)
    sero_cb(D)
    stress(D)
    ampk_sleep(D)
    map6(D)
    timeline(D)
