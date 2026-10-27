# -*- coding: utf-8 -*-
"""UNIDAD I (b) — Secuencia A (Morph): organismo → páncreas → islote → célula β → K_ATP → exocitosis.
Secreción de insulina estimulada por glucosa paso a paso, incretinas y glucagón."""
from base import *

U = 1
SEQ = 'cyan'
STEPS = ['Glucosa ↑', 'Entrada GLUT', 'Glucocinasa', 'Oxidación', 'ATP/ADP ↑', 'Cierre K_{ATP}', 'Despolarización',
         'Ca_{V} abre', 'Entrada Ca^{2+}', 'Fusión', 'Insulina + péptido C']


# ---------------------------------------------------------------- zoom anatómico
def zoom_org(D):
    s = new(D, U, 'Secuencia A · del organismo al páncreas', SEQ, morph=False)
    s.pic('Human_male', 1.6, 1.05, h=6.1, name='!!Organismo')
    p = s.pic('pancreas', 2.55, 3.65, 0.85, name='!!Páncreas')
    c = s.shape(2.35, 3.35, 1.25, 0.85, 'ellipse', None, ('C00000', 3.0), False, name='!!Lupa')
    t = tbox(s, 7.3, 1.4, 5.6, 2.2, 'El páncreas se ubica en el **retroperitoneo**, detrás del estómago. Más del 95 % es tejido **exocrino**; '
             'los **islotes de Langerhans** forman una fracción mínima, pero muy vascularizada e inervada.', 16, head='Órgano mixto', name='!!Texto A')
    t2 = tbox(s, 7.3, 4.0, 5.6, 2.1, 'La sangre de los islotes drena a la **vena porta**: el **hígado** recibe primero las concentraciones '
              'más altas de insulina y glucagón.', 16, head='Drenaje portal')
    s.step(zoom(c), pulse(p, after=True))
    s.step(fade(t2))
    s.note('Inicio de la secuencia A (Morph): del organismo completo a la membrana de la célula β. En las diapositivas siguientes '
           'los objetos conservan su nombre (prefijo !!), de modo que la transición Morph produce un acercamiento continuo. '
           'El páncreas endocrino es una fracción mínima del órgano (ampliación bibliográfica: el tejido exocrino supera '
           'ampliamente el 95 %). Los islotes drenan a la vena porta, de modo que el hígado es el primer órgano blanco de la '
           'insulina y del glucagón.')


def zoom_panc(D):
    s = new(D, U, 'Secuencia A · páncreas', SEQ, morph=True)
    s.pic('Human_male', -3.6, -6.9, h=24.0, name='!!Organismo', transp=25)
    p = s.pic('pancreas', 0.9, 2.0, 7.6, name='!!Páncreas')
    c = s.shape(5.15, 3.05, 0.9, 0.75, 'ellipse', None, ('C00000', 3.0), False, name='!!Lupa')
    lab(s, 0.9, 5.4, 7.6, 0.45, 'CABEZA · CUELLO · CUERPO · COLA', 15)
    t = tbox(s, 8.9, 1.4, 4.1, 4.6, '- **Ácinos** (exocrino): enzimas digestivas hacia el duodeno.\n- **Islotes** dispersos (endocrino): '
             'células β (insulina, amilina), α (glucagón), δ (somatostatina) y PP.\n- Inervación **vagal** (estimula) y **simpática**.', 15.5,
             head='Dos glándulas en una', name='!!Texto A')
    s.step(pulse(c), fade(t, after=True))
    s.note('Acercamiento al páncreas. La transición Morph agranda el organismo y lo desplaza fuera de la diapositiva mientras el '
           'páncreas crece hasta ocupar el centro. Funcionalmente coexisten dos glándulas: la exocrina (ácinos que vierten enzimas '
           'digestivas al duodeno) y la endocrina (islotes de Langerhans). La lupa señala la región que se ampliará: un islote.')


def zoom_islet(D):
    s = new(D, U, 'Secuencia A · islote de Langerhans', SEQ, morph=True)
    s.pic('pancreas', -12.0, -6.0, 31.0, name='!!Páncreas', transp=55)
    isl = s.pic('langerhans-islet-pancreas', 0.7, 1.15, h=5.9, name='!!Islote')
    c = s.shape(2.6, 3.0, 1.1, 1.0, 'ellipse', None, ('C00000', 3.0), False, name='!!Lupa')
    cells = [('β', '7FB3D5', 'Insulina y amilina · mayoritarias · **sensor de glucosa**'),
             ('α', 'F1948A', 'Glucagón · responde a hipoglucemia, aminoácidos y SNA'),
             ('δ', 'F7DC6F', 'Somatostatina · freno **paracrino** de α y β'),
             ('PP', 'C39BD3', 'Polipéptido pancreático')]
    ids = []
    for i, (t, col, d) in enumerate(cells):
        y = 1.3 + i * 1.3
        g = s.group_start('Célula ' + t)
        sphere(s, 7.3, y, 0.85, col, text=t, size=18, tcolor=INK)
        tbox(s, 8.35, y - 0.05, 4.6, 0.95, d, 14.5, anchor='m')
        ids.append(s.group_end())
    s.step(*[fade(g, after=i > 0) for i, g in enumerate(ids)])
    s.step(pulse(c))
    s.note('Islote de Langerhans (ilustración: ácinos exocrinos alrededor de un islote central muy vascularizado). Células β: '
           'insulina y amilina, la población mayoritaria y el sensor de glucosa; α: glucagón; δ: somatostatina, freno paracrino de '
           'α y β; PP: polipéptido pancreático. La comunicación paracrina entre estas células modula la respuesta. La lupa marca '
           'una célula β, que se ampliará en la diapositiva siguiente.')


# ---------------------------------------------------------------- escena de la célula β
def progress(s, active):
    g = s.group_start('!!Progreso')
    for i in range(11):
        on = (i + 1) in active
        done = (i + 1) < min(active) if active else False
        s.shape(8.78 + i * 0.38, 6.62, 0.34, 0.34, 'ellipse', BOX if on else ('FFE699' if done else WHITE), (INK, 1.0), False,
                str(i + 1), 10.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False, name='Progreso %d' % (i + 1))
    if active:
        t = ' → '.join(STEPS[a - 1] for a in active)
        s.shape(8.75, 6.12, 4.2, 0.42, 'rect', BOX, (INK, 1.25), False, t, 12.5, F_HEAD, BOXT, True, 'c', 'm', (0.04, 0, 0.04, 0), minsize=9)
    return s.group_end()


def scene(s, k, bgislet=False):
    """k: 0 basal · 1 glucosa dentro · 2 ATP ↑ · 3 K_ATP cerrado · 4 Ca_V abierto · 5 exocitosis"""
    if bgislet:
        s.pic('langerhans-islet-pancreas', -18.0, -14.0, h=33.0, name='!!Islote', transp=88)
    lab(s, 6.0, 1.0, 2.4, 0.38, 'EXTRACELULAR', 13, align='r', name='!!Rótulo extracelular')
    beta_cell_body(s, 0.4, 2.35, 8.0, 4.7, name='!!Célula beta')
    ids = {}
    ids['glut'] = glut(s, 1.05, 2.03, 0.62, name='!!GLUT', color='5DADE2', text='GLUT1/3 (GLUT2)')
    if k < 3:
        ids['katp'] = channel(s, 3.05, 1.99, 0.7, True, name='!!KATP', text='K_{ATP} abierto')
    else:
        ids['katp'] = channel(s, 3.05, 1.99, 0.7, False, name='!!KATP', text='K_{ATP} cerrado')
    if k < 4:
        ids['cav'] = channel(s, 5.35, 1.99, 0.7, False, name='!!CaV', color='D35400', flank='F5CBA7', text='Ca_{V} cerrado')
    else:
        ids['cav'] = channel(s, 5.35, 1.99, 0.7, True, name='!!CaV', color='D35400', flank='F5CBA7', text='Ca_{V} abierto')
    ids['mito'] = mito(s, 2.0, 4.0, 1.7, name='!!Mitocondria beta')
    gpos = [(5.2, 3.7), (6.0, 3.45), (6.8, 3.75), (5.6, 4.45), (6.45, 4.4), (7.2, 4.6), (5.3, 5.25), (6.15, 5.2)]
    if k >= 5:
        gpos = [(6.45, 2.62), (7.1, 2.62), (6.8, 3.4), (5.6, 4.45), (6.45, 4.2), (7.2, 4.6), (5.3, 5.25), (6.15, 5.2)]
    ids['gran'] = [granule(s, x, y, 0.5, name='!!Gránulo %d' % i) for i, (x, y) in enumerate(gpos)]
    depol = k >= 3
    g = s.group_start('!!Cargas de membrana')
    for i, xx in enumerate([0.75, 2.2, 4.45, 6.6, 7.6]):
        s.text(xx, 1.62, 0.3, 0.3, '−' if depol else '+', 20, F_HEAD, TRN if depol else INH, True, 'c', 'm')
        s.text(xx, 2.75, 0.3, 0.3, '+' if depol else '−', 20, F_HEAD, INH if depol else TRN, True, 'c', 'm')
    ids['charges'] = s.group_end()
    vm = '≈ −70 mV' if not depol else 'despolarizada'
    ids['vm'] = s.shape(0.55, 6.45, 2.4, 0.42, 'rect', WHITE if not depol else 'FDE2E2', (INK, 1.0), False, 'Potencial: ' + vm, 12.5, F_HEAD,
                        INK, True, 'c', 'm', name='!!Potencial')
    if k >= 1:
        ids['g6p'] = mbox(s, 1.0, 3.2, 1.25, 0.45, 'G6P', 'y', 13, name='!!G6P')
        ids['gck'] = elabel(s, 1.05, 2.85, 'Glucocinasa', 11, name='!!Glucocinasa')
    if k >= 2:
        ids['atp'] = [mol(s, 3.85 + (i % 3) * 0.48, 4.0 + (i // 3) * 0.45, 'atp', d=0.42, name='!!ATP %d' % i) for i in range(6)]
    if k >= 4:
        ids['ca'] = [mol(s, 5.15 + (i % 3) * 0.42, 2.85 + (i // 3) * 0.4, 'ca', d=0.36, name='!!Ca %d' % i) for i in range(5)]
    return ids


def panel(s, n, head, text, h=4.7):
    g = s.group_start('!!Panel')
    s.shape(8.75, 1.15, 4.2, h, 'rect', WHITE, (INK, 1.5), SHD)
    s.shape(8.9, 1.27, 0.75, 0.55, 'rect', BOX, (INK, 1.5), False, n, 15, F_HEAD, BOXT, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.text(9.75, 1.22, 3.1, 0.65, head, 16.5, F_HEAD, INK, True, 'l', 'm')
    s.text(8.95, 1.98, 3.85, h - 0.95, text, 14.5, F_BODY, INK, False, 'l', 't', spc=5)
    return s.group_end()


def beta_full(D):
    s = new(D, U, 'Célula β: el sensor completo', SEQ, morph=True)
    ids = scene(s, 0, True)
    progress(s, [])
    p = panel(s, 'β', 'Componentes del sensor', '- **GLUT**: entrada de glucosa por difusión facilitada.\n- **Glucocinasa (GCK)**: fija el umbral; es el verdadero sensor.\n'
              '- **Mitocondria**: convierte flujo de glucosa en ATP.\n- **K_{ATP}** (Kir6.2/SUR1) y **Ca_{V}**: traducen metabolismo en señal eléctrica.\n'
              '- **Gránulos**: insulina + péptido C listos para exocitosis.')
    s.step(pulse(ids['glut']), pulse(ids['katp'], after=True), pulse(ids['cav'], after=True), pulse(ids['mito'], after=True))
    s.step(*[pulse(gx, after=(i > 0), dur=200) for i, gx in enumerate(ids['gran'][:4])])
    s.note('La célula β completa (llegada del acercamiento Morph desde el islote). En la célula β la glucosa ingresa mediante '
           'transportadores GLUT (según especie y condiciones predominan GLUT1/GLUT3 y/o GLUT2). La glucocinasa (GCK) actúa como '
           'sensor al fosforilar la glucosa a glucosa-6-fosfato. La glucólisis, la oxidación del piruvato, el ciclo de Krebs y la '
           'cadena respiratoria elevan la relación ATP/ADP. El canal K_ATP (Kir6.2/SUR1) y los canales de Ca²⁺ dependientes de '
           'voltaje traducen ese cambio metabólico en una señal eléctrica. Esta escena se repite con los mismos nombres de objeto '
           'en las seis diapositivas siguientes: el Morph muestra sólo lo que cambia en cada paso.')


def b_123(D):
    s = new(D, U, 'Pasos 1–3 · glucosa ↑, entrada y glucocinasa', SEQ, morph=True)
    ids = scene(s, 1)
    progress(s, [1, 2, 3])
    panel(s, '1–3', 'Glucosa → G6P', '- **1.** Tras la comida aumenta la glucemia portal y sistémica.\n- **2.** La glucosa ingresa por GLUT siguiendo su gradiente.\n'
          '- **3.** La **glucocinasa** (K_{m} alta, sin inhibición por producto) fosforila la glucosa a **glucosa-6-fosfato** en proporción a la glucemia.\n'
          '- La entrada no limita la velocidad: el paso que «decide» es la fosforilación.')
    gl = [mol(s, 0.55 + i * 0.55, 1.05 + (i % 2) * 0.32, 'glc', d=0.42, name='Glc ext %d' % i) for i in range(4)]
    s.anim = []
    s.step(*[fade(m, after=(i > 0), dur=250) for i, m in enumerate(gl)])
    s.step(*[path(m, 1.15 - (0.55 + i * 0.55), 2.45 - (1.05 + (i % 2) * 0.32) + i * 0.12, pts=[(1.15 - (0.55 + i * 0.55), 0.85 - (1.05 + (i % 2) * 0.32))],
                  dur=1500, delay=i * 300) for i, m in enumerate(gl)])
    s.step(*[out(m, after=(i > 0), dur=200) for i, m in enumerate(gl)], pulse(ids['gck'], after=True), pulse(ids['g6p'], after=True))
    s.note('Pasos 1 a 3. Las fichas de glucosa aparecen en el medio extracelular (aumento de la glucemia), atraviesan el GLUT '
           '(trayectorias de movimiento) y desaparecen al ser fosforiladas por la glucocinasa: la ficha G6P señala el producto. '
           'La glucocinasa (hexocinasa IV) tiene afinidad baja y no es inhibida por su producto, por lo que su velocidad acompaña '
           'proporcionalmente a la glucemia en el rango fisiológico: es el sensor que fija el umbral de secreción.')


def b_45(D):
    s = new(D, U, 'Pasos 4–5 · metabolismo oxidativo y ATP/ADP ↑', SEQ, morph=True)
    ids = scene(s, 2)
    progress(s, [4, 5])
    panel(s, '4–5', 'Metabolismo → ATP', '- **4.** Glucólisis → **piruvato** → piruvato deshidrogenasa → **acetil-CoA** → ciclo de Krebs.\n'
          '- NADH y FADH₂ alimentan la **cadena respiratoria**; la ATP sintasa fosforila ADP.\n- **5.** Sube la relación **ATP/ADP** citosólica: la señal metabólica que leerá el canal K_{ATP}.')
    pyr = mbox(s, 1.1, 4.1, 0.85, 0.42, 'Pir', 'y', 12, name='Piruvato')
    a1 = s.arrow([(1.6, 3.68), (1.55, 4.08)], INK, 2.0)
    a2 = s.arrow([(1.97, 4.3), (2.2, 4.4)], INK, 2.0)
    s.anim = []
    s.step(wipe(a1, 't'), fade(pyr, after=True), wipe(a2, 'l', after=True), pulse(ids['mito'], after=True))
    s.step(*[zoom(a, after=(i > 0), dur=250) for i, a in enumerate(ids['atp'])])
    bar = s.group_start('Relación ATP/ADP')
    s.shape(4.35, 5.25, 2.1, 0.35, 'rect', WHITE, (INK, 1.0), False)
    s.shape(4.35, 5.25, 1.75, 0.35, 'rect', BOX, (INK, 1.0), False, 'ATP/ADP ↑', 12, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    s.step(wipe(bar, 'l', dur=900))
    s.note('Pasos 4 y 5. La glucosa-6-fosfato sigue la glucólisis hasta piruvato, que entra a la mitocondria y se oxida a '
           'acetil-CoA; el ciclo de Krebs y la cadena respiratoria generan ATP. Animación: el piruvato entra a la mitocondria, '
           'aparecen las fichas de ATP y la barra muestra el aumento de la relación ATP/ADP. Lo que importa para la señal no es '
           'la cantidad absoluta de ATP, sino la relación ATP/ADP (y Mg-ADP) que perciben las subunidades del canal.')


def b_67(D):
    s = new(D, U, 'Pasos 6–7 · cierre de K_{ATP} y despolarización', SEQ, morph=True)
    ids = scene(s, 3)
    progress(s, [6, 7])
    panel(s, '6–7', 'Señal eléctrica', '- **6.** El ATP se une a **Kir6.2** y **cierra** el canal K_{ATP}: disminuye la salida de K^{+}.\n'
          '- **7.** Al reducirse la corriente de K^{+} hacia afuera, la membrana se **despolariza** (las cargas se invierten).\n'
          '- **Sulfonilureas** (glibenclamida) cierran el canal al unirse a **SUR1**, independientemente de la glucosa.')
    kk = [mol(s, 3.25 + i * 0.3, 1.5 - i * 0.12, 'k', d=0.32, name='K %d' % i) for i in range(3)]
    x = s.group_start('Salida de K bloqueada')
    s.arrow([(3.1, 1.2), (4.0, 1.9)], INH, 4, tail=None); s.arrow([(3.1, 1.9), (4.0, 1.2)], INH, 4, tail=None)
    s.group_end()
    s.anim = []
    s.step(*[fade(k_, after=(i > 0), dur=200) for i, k_ in enumerate(kk)], zoom(x, after=True))
    s.step(pulse(ids['charges']), pulse(ids['vm'], after=True))
    s.note('Pasos 6 y 7. Mediante Morph desde la diapositiva anterior, el canal K_ATP pasa de abierto a cerrado y las cargas de '
           'membrana se invierten. En reposo, la salida de K⁺ por los canales K_ATP mantiene la membrana polarizada (alrededor de '
           '−70 mV, valor aproximado). Cuando el ATP se une a Kir6.2 el canal se cierra, la corriente de K⁺ hacia afuera disminuye '
           'y la membrana se despolariza. Las sulfonilureas como la glibenclamida actúan aquí, sobre SUR1, cerrando el canal aun '
           'con glucosa baja: por eso pueden producir hipoglucemia (caso 12 y ejercicio 12).')


def b_89(D):
    s = new(D, U, 'Pasos 8–9 · apertura de Ca_{V} y entrada de Ca^{2+}', SEQ, morph=True)
    ids = scene(s, 4)
    progress(s, [8, 9])
    panel(s, '8–9', 'Calcio como disparador', '- **8.** La despolarización abre canales de **Ca^{2+} dependientes de voltaje**.\n'
          '- **9.** El Ca^{2+} ingresa a favor de un gradiente de ~10 000 veces y aumenta su concentración submembrana.\n'
          '- El Ca^{2+} es la señal que activa la maquinaria de fusión de los gránulos.')
    ce = [mol(s, 5.2 + (i % 3) * 0.42, 0.95 + (i // 3) * 0.38, 'ca', d=0.36, name='Ca ext %d' % i) for i in range(5)]
    s.anim = []
    s.step(pulse(ids['cav']))
    s.step(*[fade(c, after=(i > 0), dur=150) for i, c in enumerate(ce)])
    s.step(*[path(c, 5.55 - (5.2 + (i % 3) * 0.42), 2.95 - (0.95 + (i // 3) * 0.38) + 0.3, pts=[(5.55 - (5.2 + (i % 3) * 0.42), 1.35 - (0.95 + (i // 3) * 0.38))],
                  dur=1300, delay=i * 250) for i, c in enumerate(ce)])
    s.note('Pasos 8 y 9. La despolarización abre los canales de Ca²⁺ dependientes de voltaje (Morph: el canal cambia de cerrado '
           'a abierto). Las fichas de Ca²⁺ del medio extracelular atraviesan el canal mediante trayectorias de movimiento. El '
           'gradiente de calcio entre el exterior (milimolar) y el citosol (submicromolar) es de varios órdenes de magnitud '
           '(ampliación bibliográfica). El aumento local de Ca²⁺ es el disparador de la exocitosis.')


def b_1011(D):
    s = new(D, U, 'Pasos 10–11 · fusión de gránulos y secreción', SEQ, morph=True)
    ids = scene(s, 5)
    progress(s, [10, 11])
    panel(s, '10–11', 'Exocitosis', '- **10.** El Ca^{2+} activa la maquinaria de fusión: los gránulos anclados se fusionan con la membrana.\n'
          '- **11.** Se liberan **insulina y péptido C en cantidad equimolar** hacia los capilares del islote → vena porta → hígado.\n'
          '- Las **incretinas** potencian este paso solo si hay glucosa elevada.')
    outs = []
    for i, (x, y) in enumerate([(6.6, 2.5), (7.25, 2.5)]):
        a = mol(s, x + 0.05, y + 0.05, 'ins', d=0.4, name='Insulina sale %d' % i)
        b = s.shape(x + 0.12, y + 0.12, 0.3, 0.3, 'ellipse', BOX, (INK, 1.0), False, 'C', 10, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                    name='Péptido C sale %d' % i)
        outs.append((a, b))
    s.anim = []
    s.step(*[pulse(g, after=(i > 0), dur=250) for i, g in enumerate(ids['gran'][:2])])
    effs = []
    for i, (a, b) in enumerate(outs):
        effs += [fade(a, after=(i > 0)), path(a, -0.6 - i * 0.6, -1.35, dur=1300), fade(b), path(b, -0.2 - i * 0.6, -1.1, dur=1300)]
    s.step(*effs)
    s.note('Pasos 10 y 11. Mediante Morph los gránulos se desplazan hacia la membrana; el pulso representa la fusión y luego '
           'salen hacia el medio extracelular la insulina (fichas azules) y el péptido C (fichas amarillas) en cantidades '
           'equimolares. La insulina llega a los capilares del islote, drena a la vena porta y alcanza primero el hígado. Esta '
           'secuencia completa —glucosa → GLUT → glucocinasa → ATP/ADP → cierre de K_ATP → despolarización → Ca²⁺ → exocitosis— '
           'fundamenta la acción de las sulfonilureas.')


def katp_zoom(D):
    s = new(D, U, 'El canal K_{ATP} de cerca: Kir6.2 + SUR1', 'peach')
    membrane_h(s, 0.5, 3.0, 7.6, 0.6, name='Membrana')
    g = s.group_start('Canal octamérico')
    for i, x in enumerate([1.3, 5.75]):
        s.shape(x, 2.35, 1.3, 1.9, 'roundRect', shade('58D68D', 0.4, 0.3), ('1D8348', 1.5), SHD, 'SUR1', 15, F_HEAD, INK, True, 'c', 'm', adj={'adj': 30000})
    for i, x in enumerate([2.8, 4.45]):
        s.shape(x, 2.6, 1.35, 1.45, 'roundRect', shade('A569BD', 0.4, 0.3), ('5B2C6F', 1.5), SHD, 'Kir6.2', 15, F_HEAD, WHITE, True, 'c', 'm', adj={'adj': 30000})
    pore = s.shape(4.12, 2.45, 0.36, 1.75, 'rect', ('lin', [(0, 'D6EAF8'), (100, 'AED6F1')], 0), None, False, name='Poro')
    s.group_end()
    lab(s, 0.5, 1.85, 7.6, 0.4, 'EXTERIOR', 13); lab(s, 0.6, 4.5, 2.0, 0.4, 'CITOSOL', 13, align='l')
    k1 = mol(s, 4.1, 4.6, 'k', d=0.4, name='K sale')
    atp = mol(s, 3.0, 5.25, 'atp', d=0.6, name='ATP se une')
    su = mbox(s, 0.6, 5.3, 2.1, 0.6, 'Glibenclamida', 's', 14, caps=False, name='Sulfonilurea')
    xx = s.group_start('Poro cerrado')
    s.shape(3.95, 3.0, 0.7, 0.6, 'rect', INH, (INK, 1.0), False, '×', 26, F_HEAD, WHITE, True, 'c', 'm', fit=False)
    s.group_end()
    st = steps_panel(s, 8.5, 1.2, 4.5, ['Estructura **octamérica**: 4 Kir6.2 forman el poro; 4 SUR1 (receptor de sulfonilureas) lo regulan.',
                                       'Con ATP/ADP bajo el canal está **abierto**: sale K^{+} y la célula queda polarizada.',
                                       'El **ATP** se une a Kir6.2 → **cierre** → despolarización.',
                                       'La **glibenclamida** se une a SUR1 → cierre **independiente de glucosa** → riesgo de hipoglucemia.'], 14, anim=False)[0]
    s.step(fade(st[0]))
    s.step(fade(st[1]), fade(k1, after=True), path(k1, 0.0, -3.0, dur=1400))
    s.step(fade(st[2]), fade(atp, after=True), path(atp, 1.0, -1.1, dur=1100), zoom(xx, after=True))
    s.step(fade(st[3]), fade(su, after=True), path(su, 0.8, -1.5, dur=1100))
    s.note('El canal K_ATP es un octámero: cuatro subunidades Kir6.2 forman el poro de potasio y cuatro subunidades SUR1 '
           '(receptor de sulfonilureas) lo regulan. Con relación ATP/ADP baja el canal permanece abierto y la salida de K⁺ '
           'mantiene la célula polarizada. El aumento de ATP (unión a Kir6.2) cierra el poro. Las sulfonilureas como la '
           'glibenclamida se unen a SUR1 y cierran el canal independientemente de la glucemia; si existe reserva β estimulan la '
           'secreción de insulina endógena, pero pueden producir hipoglucemia (a veces prolongada) y aumento de peso. En la DM1 '
           'con déficit absoluto no hay secreción β que estimular. Animación: salida de K⁺, unión del ATP con cierre y unión del '
           'fármaco.')


def exo_zoom(D):
    s = new(D, U, 'Exocitosis de cerca y secreción bifásica', 'green')
    membrane_h(s, 0.5, 1.6, 6.4, 0.5, name='Membrana exo')
    lab(s, 0.5, 1.15, 6.4, 0.38, 'CAPILAR DEL ISLOTE → VENA PORTA', 13)
    gr = [granule(s, 1.0 + i * 1.5, 3.0 + (i % 2) * 0.6, 0.9, name='Gránulo exo %d' % i) for i in range(4)]
    ca = [mol(s, 1.4 + i * 1.5, 2.25, 'ca', d=0.38, name='Ca exo %d' % i) for i in range(3)]
    ins = [mol(s, 1.2 + i * 1.5, 1.7, 'ins', d=0.4, name='Ins libre %d' % i) for i in range(3)]
    cid = chart_line(s, 7.2, 1.15, 5.8, 3.4, ['0', '2', '5', '10', '20', '30', '45', '60'],
                     [('Secreción de insulina', [0.3, 3.2, 1.4, 1.0, 1.4, 1.9, 2.3, 2.5])], ['1F4E9A'],
                     title_txt='Respuesta a glucosa sostenida (min · esquema)', legend=False, size=11, name='Bifásica')
    t = tbox(s, 0.5, 4.75, 12.5, 2.05, '- **Primera fase** (minutos): fusión de gránulos ya **anclados** y preparados junto a la membrana.\n'
             '- **Segunda fase** (sostenida): reclutamiento de nuevos gránulos, amplificada por señales metabólicas e **incretinas**.\n'
             '- La pérdida precoz de la primera fase es característica de la disfunción β que precede a la DM2.', 15, head='Dos fases')
    s.step(*[fade(c, after=(i > 0), dur=200) for i, c in enumerate(ca)])
    s.step(*[path(g, 0.0, -1.0 if i % 2 == 0 else -1.6, dur=1000) for i, g in enumerate(gr[:3])])
    s.step(*[fade(m, after=(i > 0), dur=250) for i, m in enumerate(ins)], path(ins[0], 0.0, -0.6, dur=900))
    s.step(fade(t))
    s.note('Exocitosis: el aumento de Ca²⁺ submembrana activa la maquinaria de fusión (proteínas SNARE y sensores de calcio, '
           'ampliación bibliográfica) y los gránulos vierten insulina y péptido C. Con un estímulo de glucosa sostenido la '
           'secreción es bifásica: una primera fase rápida, que libera gránulos ya anclados, y una segunda fase sostenida, que '
           'requiere reclutar gránulos y es amplificada por señales metabólicas e incretinas. El gráfico es un esquema '
           'conceptual (no datos de un paciente). La pérdida precoz de la primera fase acompaña a la disfunción β de la DM2 '
           '(ampliación bibliográfica).')


def incretins(D):
    s = new(D, U, 'Incretinas GLP-1 y GIP: potenciación dependiente de glucosa', 'blue')
    s.pic('small-intestine', 0.4, 1.2, 2.2, name='Intestino')
    nodes = {
        'gut': (2.75, 1.4, 2.4, 0.6, 'Células L (GLP-1)\ncélulas K (GIP)', 's', 13.5),
        'r': (2.75, 2.55, 2.4, 0.6, 'GLP-1R / GIPR', 'g', 15),
        'gs': (2.75, 3.65, 2.4, 0.55, 'Gs → adenilil ciclasa', 'w', 14),
        'camp': (2.75, 4.7, 2.4, 0.6, 'AMPc ↑', 'y', 17),
        'pka': (5.9, 4.7, 2.6, 0.6, 'PKA · Epac2', 'g', 15),
        'gl': (5.9, 2.55, 2.6, 0.6, 'Glucosa alta → ATP/ADP ↑\nCa^{2+} ↑', 'Y', 13),
        'out': (9.4, 3.6, 3.5, 0.8, 'Más exocitosis de insulina\nSOLO si hay hiperglucemia', 'r', 15),
    }
    edges = [('gut', 'r'), ('r', 'gs'), ('gs', 'camp'), ('camp', 'pka'), ('pka', 'out', {'col': ACT, 'w': 3}), ('gl', 'out', {'col': ACT, 'w': 3})]
    graph(s, nodes, edges, [['gut'], ['gut>r', 'r'], ['r>gs', 'gs', 'gs>camp', 'camp'], ['camp>pka', 'pka'], ['gl'], ['pka>out', 'gl>out', 'out']])
    p = pearl(s, 0.45, 5.75, 12.45, 1.05, 'Las incretinas **amplifican** la señal del calcio pero no cierran el K_{ATP} por sí mismas: con glucosa baja el efecto es mínimo → '
              'bajo riesgo intrínseco de hipoglucemia (a diferencia de las sulfonilureas).', 15)
    s.step(zoom(p))
    s.note('Incretinas. Tras la ingesta, las células L intestinales secretan GLP-1 y las células K, GIP. A través de receptores '
           'acoplados a Gs aumentan el AMPc, que activa PKA y Epac2 y favorece la secreción de insulina dependiente de glucosa. '
           'La potenciación sólo es eficaz cuando la vía metabólica ya generó la señal de calcio (glucosa elevada): esa es la base '
           'del bajo riesgo intrínseco de hipoglucemia de las terapias basadas en GLP-1, en contraste con las sulfonilureas que '
           'cierran el K_ATP con cualquier glucemia. El GLP-1 además reduce el glucagón en hiperglucemia, enlentece el vaciamiento '
           'gástrico y favorece la saciedad (Unidades VI y VIII).')


def glucagon(D):
    s = new(D, U, 'Célula α y glucagón: la señal opuesta', 'peach')
    sphere(s, 0.6, 1.35, 1.3, 'F1948A', text='α', size=30, tcolor=INK, name='Célula alfa')
    s.pic('healthy_liver', 8.9, 1.2, 4.0, name='Hígado glucagón')
    nodes = {
        'st': (2.2, 1.35, 3.3, 0.85, 'Hipoglucemia · aminoácidos\nsimpático · insulina baja', 's', 14),
        'g': (2.2, 2.75, 3.3, 0.6, 'GLUCAGÓN', 'y', 18),
        'r': (6.0, 2.75, 2.6, 0.6, 'Receptor Gs (hepatocito)', 'g', 13.5),
        'c': (6.0, 3.75, 2.6, 0.55, 'AC → AMPc → PKA', 'w', 15),
        'gl': (9.2, 4.3, 3.7, 0.55, 'Glucogenólisis ↑', 'Y', 15),
        'gn': (9.2, 5.0, 3.7, 0.55, 'Gluconeogénesis ↑', 'Y', 15),
        'gs': (9.2, 5.7, 3.7, 0.55, 'Síntesis de glucógeno ↓', 'Y', 15),
        'o': (2.2, 5.0, 5.8, 1.1, 'Producción hepática de glucosa ↑\n(y modulación de la oxidación de lípidos)', 'r', 15),
    }
    edges = [('st', 'g'), ('g', 'r'), ('r', 'c'), ('c', 'gl', {'pts': [(8.6, 4.05), (9.15, 4.55)]}), ('c', 'gn', {'pts': [(8.6, 4.1), (9.15, 5.25)]}),
             ('c', 'gs', {'pts': [(8.6, 4.15), (9.15, 5.95)], 'col': INH}), ('c', 'o', {'pts': [(7.3, 4.35), (6.5, 4.95)]})]
    graph(s, nodes, edges, [['st'], ['st>g', 'g'], ['g>r', 'r', 'r>c', 'c'], ['c>gl', 'gl', 'c>gn', 'gn', 'c>gs', 'gs'], ['c>o', 'o']])
    s.note('El glucagón es secretado por las células α ante hipoglucemia, aminoácidos y estimulación simpática, y cuando la '
           'insulina es baja. En el hepatocito activa un receptor acoplado a Gs → adenilil ciclasa → AMPc → PKA. La PKA favorece '
           'la glucogenólisis y la gluconeogénesis, reduce la síntesis de glucógeno y modula la oxidación de lípidos. El balance '
           'que decide el metabolismo hepático no es la concentración aislada de una hormona, sino la relación '
           'glucagón/insulina en la sangre portal.')


def build(D):
    zoom_org(D)
    zoom_panc(D)
    zoom_islet(D)
    beta_full(D)
    b_123(D)
    b_45(D)
    b_67(D)
    b_89(D)
    b_1011(D)
    katp_zoom(D)
    exo_zoom(D)
    incretins(D)
    glucagon(D)
