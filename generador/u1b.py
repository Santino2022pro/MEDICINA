# -*- coding: utf-8 -*-
"""UNIDAD I — Tema 4: secreción de insulina y glucagón (secuencia animada célula β + Morph)"""
from base import *

U = 1
STEPS = ['Glucosa extracelular', 'Entrada por GLUT', 'Metabolismo de glucosa', '↑ ATP/ADP', 'Cierre de K_{ATP}',
         'Despolarización', 'Apertura de Ca_{V}', 'Entrada de Ca^{2+}', 'Exocitosis', 'Liberación de insulina']


def progress(s, active):
    """tira de progreso de los 10 pasos (los activos en amarillo)"""
    g = s.group_start('!!Progreso')
    s.text(8.75, 6.42, 4.2, 0.28, 'SECUENCIA DE SECRECIÓN', 11.5, F_HEAD, '5A2D0C', True, 'l')
    for i in range(10):
        on = (i + 1) in active
        done = (i + 1) < min(active) if active else False
        s.shape(8.75 + i * 0.42, 6.72, 0.36, 0.36, 'ellipse', TAG if on else ('F8C471' if done else 'EEEEEE'), (INK, 1.0), False,
                str(i + 1), 10.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False, name='Progreso %d' % (i + 1))
    return s.group_end()


def scene(s, katp_open=True, ca_open=False, depol=False, labels=False, gran_at_membrane=False):
    """escena común de la célula β (mismos nombres para Morph)"""
    s.text(0.5, 1.05, 4.5, 0.35, 'MEDIO EXTRACELULAR', 14, F_HEAD, '7A3B12', True, 'l', name='!!Rótulo extracelular')
    beta_cell_body(s, 0.4, 2.35, 8.0, 4.75, name='!!Célula beta')
    s.text(5.6, 6.6, 2.7, 0.35, 'CITOSOL DE LA CÉLULA β', 12.5, F_HEAD, '7A3B12', True, 'r', name='!!Rótulo citosol')
    ids = {}
    ids['glut'] = glut(s, 1.05, 2.03, 0.62, name='!!GLUT', color='5DADE2', text='GLUT1/3 (GLUT2)')
    if katp_open:
        ids['katp'] = channel(s, 3.05, 1.99, 0.7, True, name='!!KATP abierto', text='K_{ATP} (Kir6.2/SUR1)')
    else:
        ids['katp'] = channel(s, 3.05, 1.99, 0.7, False, name='!!KATP cerrado', text='K_{ATP} cerrado')
    if ca_open:
        ids['cav'] = channel(s, 5.35, 1.99, 0.7, True, name='!!CaV abierto', color='D35400', flank='F5CBA7', text='Ca_{V} abierto')
    else:
        ids['cav'] = channel(s, 5.35, 1.99, 0.7, False, name='!!CaV cerrado', color='D35400', flank='F5CBA7', text='Ca_{V} (voltaje-dep.)')
    ids['mito'] = mito(s, 2.25, 3.75, 1.55, name='!!Mitocondria beta')
    gpos = [(5.2, 3.7), (6.0, 3.45), (6.8, 3.75), (5.6, 4.45), (6.45, 4.4), (7.2, 4.6), (5.3, 5.25), (6.15, 5.2)]
    if gran_at_membrane:
        gpos = [(6.55, 2.62), (7.05, 2.62), (6.8, 3.75), (5.6, 4.45), (6.45, 4.4), (7.2, 4.6), (5.3, 5.25), (6.15, 5.2)]
    ids['gran'] = [granule(s, x, y, 0.48, name='!!Gránulo %d' % i) for i, (x, y) in enumerate(gpos)]
    # cargas de membrana
    if depol:
        ins_sign, out_sign, col_in, col_out = '+', '−', INH, TRN
    else:
        ins_sign, out_sign, col_in, col_out = '−', '+', TRN, INH
    g = s.group_start('!!Cargas de membrana')
    for i in range(6):
        xx = 0.75 + i * 1.25 if i < 2 else 0.75 + i * 1.25 + 0.35
        if 2.8 < xx < 4.0 or 5.1 < xx < 6.3:
            xx += 0.45
        s.text(xx, 1.62, 0.3, 0.3, out_sign, 18, F_HEAD, col_out, True, 'c', 'm')
        s.text(xx, 2.72, 0.3, 0.3, ins_sign, 18, F_HEAD, col_in, True, 'c', 'm')
    s.group_end()
    ids['charges'] = g
    return ids


def panel(s, n, head, text, fill=CREAM, h=4.95):
    g = s.group_start('!!Panel')
    s.shape(8.75, 1.15, 4.2, h, 'rect', fill, (INK, 1.25), SHD)
    badge(s, 8.9, 1.28, n, 0.55)
    s.text(9.55, 1.25, 3.3, 0.62, head, 17, F_HEAD, INK, True, 'l', 'm')
    s.text(8.95, 1.95, 3.85, h - 0.95, text, 15, F_BODY, INK, False, 'l', 't', spc=5)
    return s.group_end()


def islet_slide(D):
    s = new(D, U, '4 · El islote pancreático: anatomía funcional')
    pancreas(s, 0.4, 1.2, 5.0, name='Páncreas')
    c0 = s.shape(1.65, 1.95, 0.5, 0.5, 'ellipse', None, (INH, 2.5), False, name='Lupa islote')
    a0 = s.arrow([(2.1, 2.4), (4.95, 3.3)], INK, 2, dash='dash')
    isl = islet(s, 5.0, 2.2, 3.2, name='Islote ampliado')
    cells = [('β', '7FB3D5', 'Insulina (y amilina). Mayoritarias. Sensor de glucosa.'),
             ('α', 'F1948A', 'Glucagón. Responde a hipoglucemia, aminoácidos y señales autonómicas.'),
             ('δ', 'F7DC6F', 'Somatostatina: freno paracrino de α y β.'),
             ('PP', 'C39BD3', 'Polipéptido pancreático (≠ PYY).')]
    ids = []
    for i, (t, col, d) in enumerate(cells):
        y = 1.2 + i * 1.18
        g = s.group_start('Célula ' + t)
        s.shape(8.75, y, 0.75, 0.75, 'ellipse', shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), SHD, t, 18, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
        card(s, 9.65, y - 0.05, 3.25, 0.95, d, CREAM, 13.5, anchor='m')
        s.group_end(); ids.append(g)
    k = card(s, 0.4, 3.75, 4.4, 3.3, '- Islotes: **~1–2 %** del volumen pancreático, muy **vascularizados** e inervados (vago y simpático).\n- La sangre insular drena a la **vena porta**: el hígado recibe las mayores concentraciones de insulina y glucagón.\n- Comunicación **paracrina** entre α, β y δ.', YEL, 14)
    s.step(fade(c0), wipe(a0, 'l', after=True), zoom(isl, after=True))
    s.step(*[fade(g, after=(i > 0)) for i, g in enumerate(ids)])
    s.step(fade(k))
    s.note('El páncreas endocrino representa una fracción mínima del órgano (ampliación bibliográfica: Guyton y Hall, cap. 79). '
           'En el islote humano las células α, β y δ se encuentran entremezcladas (en roedores predomina un núcleo de β rodeado '
           'por α). La sangre venosa del islote drena en la vena porta, de modo que el hígado es el primer órgano blanco y recibe '
           'las concentraciones más altas de insulina y glucagón: por eso la relación insulina/glucagón portal es el gran '
           'regulador hepático. Precisión: el polipéptido pancreático (células PP) no es el mismo péptido que el PYY intestinal.')


def b_anat(D):
    s = new(D, U, '4 · La célula β: anatomía funcional del sensor', 'SECUENCIA INSULINA')
    ids = scene(s)
    lab = [(ids['glut'], 'Transportador de glucosa'), (ids['katp'], 'Canal de K^{+} sensible a ATP'), (ids['cav'], 'Canal de Ca^{2+} dependiente de voltaje'),
           (ids['mito'], 'Mitocondria: Krebs y fosforilación oxidativa')]
    p = panel(s, 'β', 'Componentes del sensor', '- **GLUT**: entrada de glucosa proporcional a su concentración.\n- **Glucocinasa**: fija el umbral (sensor).\n- **Mitocondria**: convierte flujo de glucosa en ATP.\n- **K_{ATP}** (Kir6.2/SUR1) y **Ca_{V}**: traducen metabolismo en señal eléctrica.\n- **Gránulos**: insulina almacenada lista para exocitosis.')
    pr = progress(s, [])
    s.step(pulse(ids['glut']), pulse(ids['katp'], after=True), pulse(ids['cav'], after=True), pulse(ids['mito'], after=True))
    s.step(*[pulse(gx, after=(i > 0), dur=200) for i, gx in enumerate(ids['gran'][:4])])
    s.note('Anatomía funcional de la célula β como sensor de glucosa. Componentes: transportadores GLUT (en humanos predominan '
           'GLUT1 y GLUT3 y puede participar GLUT2; en roedores se usa clásicamente GLUT2), la glucocinasa (hexocinasa IV), la '
           'mitocondria, los canales de potasio sensibles a ATP (KATP, formados por Kir6.2 y SUR1), los canales de calcio '
           'dependientes de voltaje y los gránulos de secreción con insulina.\nEsta escena se mantiene idéntica en las '
           'diapositivas siguientes (mismos nombres de objetos) para que la transición Morph muestre solo lo que cambia en cada '
           'paso de la secuencia.')


def b_step12(D):
    s = new(D, U, '4 · Pasos 1–2: glucosa extracelular y entrada por GLUT', 'SECUENCIA INSULINA', morph=True)
    ids = scene(s)
    p = panel(s, '1–2', 'Glucosa ↑ → entrada', '- Tras la comida aumenta la **glucemia** portal y sistémica.\n- La glucosa ingresa por **difusión facilitada** a través de GLUT, siguiendo su gradiente.\n- La entrada **no limita** la velocidad: el paso que «decide» es la fosforilación.')
    progress(s, [1, 2])
    gl = [mol(s, 0.6 + i * 0.55, 1.1 + (i % 2) * 0.35, 'glc', d=0.42, name='Glc ext %d' % i) for i in range(4)]
    s.step(*[fade(m, after=(i > 0), delay=0) for i, m in enumerate(gl)])
    s.step(*[path(m, 1.15 - (0.6 + i * 0.55) + 0.05, 0.0, pts=[(1.15 - (0.6 + i * 0.55) + 0.05, 0.9 - (1.1 + (i % 2) * 0.35) + 0.0)], dur=1400, delay=i * 350)
             for i, m in enumerate(gl)])
    s.anim[-1] = [path(m, 1.1 - (0.6 + i * 0.55), 2.2 - (1.1 + (i % 2) * 0.35) + i * 0.15,
                       pts=[(1.1 - (0.6 + i * 0.55), 0.8 - (1.1 + (i % 2) * 0.35))], dur=1600, delay=i * 300)
                  for i, m in enumerate(gl)]
    s.note('Pasos 1 y 2. Las fichas de glucosa aparecen en el medio extracelular y luego se desplazan (trayectorias de movimiento) '
           'hacia el transportador y lo atraviesan. La entrada por GLUT es difusión facilitada y en la célula β no es el paso '
           'limitante: la velocidad del sistema la fija la glucocinasa.')


def b_step3(D):
    s = new(D, U, '4 · Paso 3: glucocinasa y metabolismo intracelular', 'SECUENCIA INSULINA', morph=True)
    ids = scene(s)
    p = panel(s, '3', 'La glucocinasa fija el umbral', '- **Glucocinasa** (Km aparente alto, sin inhibición por G6P): su velocidad sigue la glucemia → **sensor de disponibilidad**.\n- **Glucólisis → piruvato → ciclo de Krebs → fosforilación oxidativa**.\n- Aquí el metabolismo es parte del **sistema de detección**, no solo producción de ATP.')
    progress(s, [3])
    g0 = mol(s, 1.2, 2.95, 'glc', d=0.42, name='Glc intracelular')
    gk = enz(s, 0.7, 3.5, 'Glucocinasa', name='GK beta')
    g6 = mol(s, 1.15, 4.0, 'glc', 'G6P', d=0.5, name='G6P beta')
    a1 = arrow_lbl(s, [(1.65, 4.25), (2.3, 4.25)], None, ACT, 3)
    py = chip(s, 1.0, 4.65, 'Piruvato', YEL, 12.5, name='Piruvato beta')
    a2 = s.arrow([(1.9, 4.85), (2.45, 4.45)], ACT, 3)
    kr = s.shape(2.55, 3.85, 1.0, 0.45, 'ellipse', ('a', 'FFFFFF', 70), (ACT, 1.5), False, 'Krebs', 12, F_HEAD, ACT, True, 'c', 'm', (0, 0, 0, 0), name='Krebs beta')
    ox = chip(s, 2.3, 4.6, 'Fosforilación oxidativa', ENE, 11.5, name='OXPHOS beta')
    s.step(fade(g0), fade(gk, after=True), out(g0, after=True), fade(g6))
    s.step(wipe(a1, 'l'), fade(py, after=True), wipe(a2, 'l', after=True))
    s.step(zoom(kr), fade(ox, after=True), pulse(ids['mito'], after=True))
    s.note('Paso 3. La glucocinasa fosforila la glucosa a glucosa-6-fosfato; su alta Km aparente y la ausencia de inhibición por '
           'producto hacen que la velocidad de fosforilación acompañe a la glucemia en el rango fisiológico, por eso se la '
           'considera el sensor que define el umbral secretor. El flujo glucolítico alimenta el ciclo de Krebs y la fosforilación '
           'oxidativa. En la célula β, glucólisis y metabolismo oxidativo son parte del sistema de detección de glucosa. '
           'Clínica: mutaciones inactivantes de glucocinasa elevan el umbral (hiperglucemia leve estable); activantes lo bajan '
           '(hipoglucemia por hiperinsulinismo).')


def b_step45(D):
    s = new(D, U, '4 · Pasos 4–5: ↑ ATP/ADP y cierre del canal K_{ATP}', 'SECUENCIA INSULINA', morph=True)
    ids = scene(s, katp_open=True)
    closed = channel(s, 3.05, 1.99, 0.7, False, name='!!KATP cerrado', text=None)
    p = panel(s, '4–5', 'ATP cierra K_{ATP}', '- El metabolismo oxidativo **aumenta la relación ATP/ADP**.\n- El ATP se une a **Kir6.2** y el MgADP deja de activar **SUR1** → el canal **se cierra**.\n- Cesa la salida de K^{+} que mantenía la membrana **hiperpolarizada**.')
    progress(s, [4, 5])
    atps = [mol(s, 3.0 + i * 0.5, 3.6 + (i % 2) * 0.3, 'atp', 'ATP', d=0.42, w=0.55, name='ATP %d' % i) for i in range(3)]
    adp = mol(s, 2.0, 3.25, 'atp', 'ADP', d=0.38, w=0.5, name='ADP')
    kout = [mol(s, 3.2 + i * 0.3, 2.95, 'k', d=0.32, name='K salida %d' % i) for i in range(2)]
    s.step(*[path(k, 0.15, -1.55, dur=1200, delay=i * 300) for i, k in enumerate(kout)])
    s.step(fade(adp), out(adp, after=True), *[zoom(a, after=(i == 0)) for i, a in enumerate(atps)])
    s.step(path(atps[0], 0.35, -0.75, dur=900), path(atps[1], -0.05, -0.95, dur=900), out(ids['katp'], after=True), fade(closed))
    s.step(pulse(closed))
    s.note('Pasos 4 y 5. El aumento del flujo oxidativo eleva la relación ATP/ADP. El ATP se une a la subunidad Kir6.2 e inhibe '
           'el canal, mientras disminuye el MgADP que lo activaba a través de SUR1: el canal KATP se cierra. En reposo (glucosa '
           'baja), la salida de K+ por KATP mantiene la membrana hiperpolarizada. La animación muestra primero la salida de K+ '
           'por el canal abierto, luego el aumento de ATP y finalmente el cambio visual del canal de abierto a cerrado.\n'
           'Farmacología: las sulfonilureas se unen a SUR1 y cierran KATP independientemente de la glucosa; el diazóxido lo abre. '
           'Defectos genéticos de Kir6.2/SUR1 alteran el umbral (diabetes neonatal o hiperinsulinismo congénito).')


def b_step6(D):
    s = new(D, U, '4 · Paso 6: despolarización de la membrana', 'SECUENCIA INSULINA', morph=True)
    ids = scene(s, katp_open=False)
    p = panel(s, '6', 'La membrana se despolariza', '- Con K_{ATP} cerrado predominan **corrientes despolarizantes** de fondo.\n- El potencial de membrana se vuelve **menos negativo** y alcanza el umbral.\n- Aparecen **potenciales de acción** en ráfagas.')
    progress(s, [6])
    g = s.group_start('!!Cargas despolarizadas')
    for i in range(6):
        xx = 0.75 + i * 1.25 if i < 2 else 0.75 + i * 1.25 + 0.35
        if 2.8 < xx < 4.0 or 5.1 < xx < 6.3:
            xx += 0.45
        s.text(xx, 1.62, 0.3, 0.3, '−', 18, F_HEAD, TRN, True, 'c', 'm')
        s.text(xx, 2.72, 0.3, 0.3, '+', 18, F_HEAD, INH, True, 'c', 'm')
    s.group_end()
    # gráfico de potencial
    gg = s.group_start('Trazado de potencial')
    s.shape(0.9, 4.95, 3.9, 1.85, 'rect', ('a', 'FFFFFF', 75), (INK, 1.0), False)
    s.text(1.0, 4.97, 3.7, 0.3, 'Potencial de membrana (esquema)', 12, F_HEAD, INK, True, 'l')
    tr = 'M 0 820 L 300 820 C 350 820 380 600 420 560 L 470 560 L 490 120 L 510 560 L 560 560 L 580 120 L 600 560 L 650 560 L 670 120 L 690 560 L 740 560 L 760 120 L 780 560 L 830 560 L 850 120 L 870 560 L 1000 560'
    s.free(1.0, 5.3, 3.7, 1.4, [(tr, False, True)], None, (INH, 2.0))
    s.text(1.0, 6.45, 1.5, 0.3, 'reposo', 11, F_BODY, INK, False, 'l')
    s.text(3.0, 6.45, 1.8, 0.3, 'ráfagas', 11, F_BODY, INK, False, 'r')
    s.group_end()
    s.step(out(ids['charges']), fade(g, after=True))
    s.step(wipe(gg, 'l', dur=1500))
    s.note('Paso 6. Al cerrarse KATP desaparece la principal conductancia hiperpolarizante; las corrientes despolarizantes de '
           'fondo llevan el potencial hacia valores menos negativos hasta el umbral de los canales dependientes de voltaje y se '
           'generan potenciales de acción en ráfagas. La animación invierte las cargas a ambos lados de la membrana para indicar '
           'el cambio eléctrico (representación didáctica: la inversión real es transitoria durante cada potencial de acción). '
           'El trazado es esquemático, sin escala.')


def b_step78(D):
    s = new(D, U, '4 · Pasos 7–8: apertura de Ca_{V} y entrada de Ca^{2+}', 'SECUENCIA INSULINA', morph=True)
    ids = scene(s, katp_open=False, depol=True, ca_open=False)
    op = channel(s, 5.35, 1.99, 0.7, True, name='!!CaV abierto', color='D35400', flank='F5CBA7', text=None)
    p = panel(s, '7–8', 'Ca^{2+} entra a la célula', '- La despolarización abre **canales de Ca^{2+} dependientes de voltaje** (tipo L y otros).\n- El Ca^{2+} **entra desde el medio extracelular** a favor de su gradiente.\n- El ↑ de Ca^{2+} citosólico es el **disparador** de la exocitosis.')
    progress(s, [7, 8])
    cas = [mol(s, 5.0 + i * 0.4, 1.15 + (i % 2) * 0.3, 'ca', d=0.36, name='Ca %d' % i) for i in range(4)]
    s.step(out(ids['cav']), fade(op, after=True))
    s.step(*[fade(c, after=(i > 0), delay=0) for i, c in enumerate(cas)])
    s.step(*[path(c, 5.62 - (5.0 + i * 0.4), 3.3 - (1.15 + (i % 2) * 0.3) + i * 0.12, pts=[(5.62 - (5.0 + i * 0.4), 0.8 - (1.15 + (i % 2) * 0.3))],
                  dur=1500, delay=i * 250) for i, c in enumerate(cas)])
    s.note('Pasos 7 y 8. La despolarización abre canales de calcio dependientes de voltaje y el Ca2+ ingresa desde el medio '
           'extracelular, donde su concentración es mucho mayor que en el citosol. La animación muestra primero el cambio del canal '
           '(cerrado → abierto) y luego el desplazamiento de los iones hacia el interior. El aumento de Ca2+ citosólico, sobre todo '
           'en microdominios cercanos a los sitios de liberación, activa la maquinaria SNARE/sinaptotagmina de la exocitosis '
           '(ampliación bibliográfica).')


def b_step910(D):
    s = new(D, U, '4 · Pasos 9–10: exocitosis y liberación de insulina', 'SECUENCIA INSULINA', morph=True)
    ids = scene(s, katp_open=False, depol=True, ca_open=True)
    p = panel(s, '9–10', 'Exocitosis de gránulos', '- El Ca^{2+} desencadena la **fusión** de gránulos con la membrana.\n- **1.ª fase**: gránulos ya **preparados** (pool inmediato).\n- **2.ª fase**: **reclutamiento** de gránulos y síntesis sostenida.\n- La insulina sale a la sangre portal.')
    progress(s, [9, 10])
    cas = [mol(s, 5.55 + i * 0.35, 3.0 + (i % 2) * 0.25, 'ca', d=0.32, name='Ca int %d' % i) for i in range(3)]
    gr = ids['gran']
    s.step(*[pulse(c, after=(i > 0), dur=200) for i, c in enumerate(cas)])
    s.step(path(gr[1], 0.85, -0.9, dur=1300), path(gr[2], 0.3, -1.05, dur=1400, delay=200))
    s.step(out(gr[1]), out(gr[2]))
    ins = [mol(s, 6.7 + i * 0.45, 1.85, 'ins', d=0.4, name='Insulina %d' % i) for i in range(3)]
    s.anim[-1] += [zoom(m, after=(i == 0)) for i, m in enumerate(ins)]
    s.step(*[path(m, 0.2 * (i - 1), -0.8, dur=1300, delay=i * 200) for i, m in enumerate(ins)])
    s.step(path(gr[4], 0.6, -1.7, dur=1600), path(gr[3], 1.6, -1.75, dur=1900, delay=300))
    s.note('Pasos 9 y 10. El Ca2+ desencadena la fusión de los gránulos con la membrana plasmática y la liberación de su '
           'contenido (insulina, péptido C y amilina). La animación desplaza los gránulos hasta la membrana, muestra su fusión '
           '(desaparición del gránulo) y la salida de insulina al espacio extracelular. El último clic representa la segunda '
           'fase: reclutamiento de nuevos gránulos desde el interior.\nPrimera fase: liberación rápida de gránulos ya acoplados y '
           'preparados; segunda fase: reclutamiento y síntesis sostenida mientras persiste la hiperglucemia.')


def b_biphasic(D):
    s = new(D, U, '4 · Secreción bifásica de insulina', 'SECUENCIA INSULINA')
    g = s.group_start('Gráfico bifásico')
    s.shape(0.45, 1.15, 7.7, 5.9, 'rect', ('a', 'FFFFFF', 55), (INK, 1.25), SHD)
    s.arrow([(1.1, 6.35), (7.8, 6.35)], INK, 1.75); s.arrow([(1.1, 6.35), (1.1, 1.5)], INK, 1.75)
    s.text(5.2, 6.45, 2.6, 0.3, 'tiempo tras el estímulo', 12.5, F_BODY, INK, False, 'r')
    s.text(0.5, 1.45, 0.5, 4.7, 'Secreción de insulina', 13, F_HEAD, INK, True, 'c', 'm', txt_rot=270)
    s.shape(1.15, 1.6, 0.04, 4.7, 'rect', ('a', '3B82C4', 40), None, False)
    s.text(1.25, 1.55, 2.2, 0.3, '↑ glucosa', 12.5, F_HEAD, '1F4E79', True, 'l')
    s.group_end()
    f1 = s.free(1.15, 1.9, 6.6, 4.4, [('M 0 980 L 40 980 C 60 980 70 50 120 50 C 180 50 190 820 260 820', False, True)], None, ('C0392B', 4.5), name='Primera fase')
    f2 = s.free(1.15, 1.9, 6.6, 4.4, [('M 260 820 C 400 800 500 600 650 480 C 780 380 880 340 1000 330', False, True)], None, ('1F4E9A', 4.5), name='Segunda fase')
    l1 = card(s, 2.15, 1.85, 2.4, 1.05, '**1.ª fase**: pico rápido, gránulos preparados', LSALMON, 13, name='Rótulo 1.ª fase')
    l2 = card(s, 5.3, 3.0, 2.6, 1.05, '**2.ª fase**: sostenida, reclutamiento y síntesis', LBLUE, 13, name='Rótulo 2.ª fase')
    c = card(s, 8.45, 1.15, 4.45, 3.0, '- **Glucocinasa** define el umbral; **K_{ATP}/Ca^{2+}** convierten metabolismo en secreción.\n- Además del «disparo» por K_{ATP} existen vías **amplificadoras** dependientes de metabolitos.', CREAM, 14, head='Mecanismo')
    c2 = card(s, 8.45, 4.35, 4.45, 2.7, '- En la diabetes tipo 2 temprana se pierde característicamente la **1.ª fase**.\n- La **ACh vagal** (fase cefálica) favorece la liberación.', YEL, 14, head='Clínica')
    s.step(fade(g))
    s.step(wipe(f1, 'l', dur=900), fade(l1, after=True))
    s.step(wipe(f2, 'l', dur=1500), fade(l2, after=True))
    s.step(fade(c))
    s.step(fade(c2))
    s.note('Ante un aumento brusco y sostenido de glucosa, la secreción de insulina es bifásica: una primera fase rápida '
           '(minutos) a partir de gránulos ya preparados, seguida de una segunda fase progresiva por reclutamiento de gránulos y '
           'síntesis sostenida. El gráfico es esquemático (sin escala). La pérdida temprana de la primera fase es un rasgo '
           'característico de la disfunción β en la diabetes tipo 2 (ampliación bibliográfica). La acetilcolina vagal favorece la '
           'liberación, en especial durante la fase cefálica de la ingesta.')


def b_incretin(D):
    s = new(D, U, '4 · Amplificación por incretinas: GLP-1 y GIP', 'SECUENCIA INSULINA')
    membrane_h(s, 0.4, 2.35, 7.9, 0.4, name='Membrana célula β')
    s.shape(0.4, 2.75, 7.9, 4.35, 'rect', ('a', 'FDE2D2', 70), None, False, name='Citosol')
    intestine(s, 0.4, 0.95, 1.25, name='Intestino (células L y K)')
    glp = mol(s, 1.8, 1.05, 'ins', 'GLP-1', d=0.5, w=0.85, name='GLP-1')
    gip = mol(s, 2.75, 1.05, 'gcg', 'GIP', d=0.5, w=0.75, name='GIP')
    rc = gpcr(s, 3.0, 2.37, 0.4, 0.9, name='Receptor GLP-1R / GIPR', text='GLP-1R / GIPR')
    gp = gprotein(s, 3.2, 3.05, 0.9, name='Gs', text='Gs')
    ac = enz(s, 4.6, 3.1, 'Adenilato ciclasa', name='AC')
    camp = mol(s, 5.15, 3.75, 'atp', 'AMPc', d=0.45, w=0.75, name='AMPc')
    pka = enz(s, 4.0, 4.55, 'PKA', name='PKA')
    ep = enz(s, 5.55, 4.55, 'Epac2', name='Epac2')
    gr = [granule(s, 5.6 + i * 0.55, 5.4 + (i % 2) * 0.3, 0.45, name='Gránulo %d' % i) for i in range(4)]
    a1 = s.arrow([(4.4, 4.15), (4.25, 4.5)], ACT, 2.5); a2 = s.arrow([(5.6, 4.2), (5.85, 4.5)], ACT, 2.5)
    a3 = s.arrow([(4.4, 4.9), (5.8, 5.4)], ACT, 2.5); a4 = s.arrow([(6.0, 4.9), (6.3, 5.35)], ACT, 2.5)
    c1 = card(s, 8.6, 1.1, 4.3, 2.4, '- **GLP-1** (células L) y **GIP** (células K) se liberan al llegar nutrientes al intestino.\n- Receptores acoplados a **Gs** → **AMPc** → **PKA** y **Epac2**.', CREAM, 14, head='Señal')
    c2 = card(s, 8.6, 3.7, 4.3, 1.75, 'Potencian la secreción **solo si la glucosa está elevada**: amplifican, no disparan.', YEL, 14.5, head='Dependencia de glucosa')
    c3 = card(s, 8.6, 5.65, 4.3, 1.45, '**Efecto incretina**: más insulina tras glucosa oral que por vía venosa.', LBLUE, 14)
    s.step(fade(glp), fade(gip), path(glp, 1.55, 1.05, after=True, dur=1100), path(gip, 0.6, 1.05, dur=1100))
    s.step(pulse(rc), fade(gp, after=True), fade(ac, after=True), zoom(camp, after=True))
    s.step(wipe(a1, 't'), fade(pka, after=True), wipe(a2, 't'), fade(ep))
    s.step(wipe(a3, 'l'), wipe(a4, 't'), *[pulse(g, after=(i == 0)) for i, g in enumerate(gr)])
    s.step(fade(c1)); s.step(fade(c2)); s.step(fade(c3))
    s.note('Las incretinas GLP-1 (células L del íleon y colon) y GIP (células K del duodeno y yeyuno) se liberan ante la llegada '
           'de nutrientes. Sus receptores en la célula β están acoplados a Gs: aumentan el AMPc, que activa PKA y Epac2 y potencia '
           'la exocitosis de gránulos. Esta amplificación es dependiente de glucosa: con glucemia baja no estimulan una secreción '
           'significativa, lo que explica el bajo riesgo intrínseco de hipoglucemia de los agonistas del receptor de GLP-1. '
           'Efectos distintos sobre la célula α: GLP-1 tiende a suprimir el glucagón cuando la glucosa no está baja, mientras que '
           'GIP puede favorecerlo en determinadas glucemias.')


def b_fasting(D):
    s = new(D, U, '4 · Célula β en ayuno: freno de la secreción', 'SECUENCIA INSULINA')
    ids = scene(s, katp_open=True)
    progress(s, [])
    p = panel(s, 'β', 'Ayuno: K_{ATP} abiertos', '- ↓ metabolismo de glucosa → ↓ ATP/ADP.\n- K_{ATP} **relativamente abiertos** → salida de K^{+} → **hiperpolarización**.\n- Ca_{V} cerrados → ↓ Ca^{2+} → ↓ exocitosis.', h=3.35)
    k = note_box(s, 8.75, 4.65, 4.2, 1.65, 'Persiste una **secreción basal** indispensable para frenar la lipólisis y la cetogénesis extremas.', 14)
    ks = [mol(s, 3.2 + i * 0.3, 2.95, 'k', d=0.32, name='K salida %d' % i) for i in range(3)]
    d1 = card(s, 0.6, 5.55, 4.4, 1.35, '**Diabetes tipo 1**: sin insulina se pierde este freno **aun con abundante glucosa extracelular** → riesgo de cetoacidosis.', YEL, 13)
    s.step(*[path(m, 0.1, -1.6, dur=1200, delay=i * 300) for i, m in enumerate(ks)])
    s.step(zoom(k))
    s.step(fade(d1))
    s.note('En ayuno el menor metabolismo de glucosa reduce la relación ATP/ADP: los canales KATP permanecen relativamente '
           'abiertos, el K+ sale, la membrana se hiperpolariza, los canales de Ca2+ permanecen cerrados y la exocitosis disminuye. '
           'Sin embargo, existe una secreción basal de insulina indispensable para restringir la lipólisis y la cetogénesis '
           'extremas. En la diabetes tipo 1 la pérdida de insulina elimina este freno aun con abundante glucosa extracelular: '
           'el adipocito libera AG sin control y el hígado produce cuerpos cetónicos en exceso (cetoacidosis).')


def alpha_cell(D):
    s = new(D, U, '4 · Célula α: secreción de glucagón')
    g0 = s.group_start('Célula alfa')
    s.shape(0.45, 1.25, 4.6, 4.2, 'roundRect', ('rad', [(0, 'FDEDEC'), (100, 'F5B7B1')], (50, 50)), ('C0392B', 7), SHD, adj={'adj': 22000})
    nucleus(s, 0.95, 3.4, 1.2)
    for i in range(7):
        granule(s, 2.4 + (i % 4) * 0.55, 2.0 + (i // 4) * 0.6, 0.42, core='D35400')
    s.text(0.6, 1.35, 4.3, 0.4, 'CÉLULA α', 16, F_HEAD, '922B21', True, 'c')
    s.group_end()
    gc = [mol(s, 2.6 + i * 0.55, 5.6, 'gcg', d=0.42, name='Glucagón %d' % i) for i in range(3)]
    st = card(s, 5.3, 1.15, 3.7, 2.55, '- **Hipoglucemia**\n- **Señales autonómicas** (simpático, adrenalina)\n- **Aminoácidos** (comida proteica)', MINT, 14.5, head='Estimulan', headfill=ACT)
    fr = card(s, 5.3, 3.9, 3.7, 2.15, '- **Glucosa** elevada\n- **Insulina** (paracrina)\n- **Somatostatina** (células δ)', LSALMON, 14.5, head='Frenan', headfill=INH)
    el = card(s, 9.2, 1.15, 3.7, 2.7, 'El mecanismo electrofisiológico es **más complejo** que «ATP bajo abre K_{ATP}»: intervienen distintas conductancias iónicas, excitabilidad y regulación **paracrina**.', YEL, 14, head='Precisión')
    pr = card(s, 9.2, 4.05, 3.7, 3.0, 'Una **comida proteica** puede elevar **insulina y glucagón a la vez**: se favorece el destino de los aminoácidos **sin hipoglucemia**.', LBLUE, 14, head='Comida proteica')
    inc = card(s, 0.45, 6.2, 8.55, 0.9, '**GLP-1** tiende a **suprimir** el glucagón cuando la glucosa no está baja; **GIP** puede favorecerlo en determinadas glucemias.', CREAM, 14)
    s.step(fade(st))
    s.step(*[zoom(m, after=(i > 0)) for i, m in enumerate(gc)])
    s.step(fade(fr))
    s.step(fade(el))
    s.step(fade(pr))
    s.step(fade(inc))
    s.note('La célula α secreta glucagón en ayuno, estimulada por hipoglucemia, señales autonómicas (simpáticas y adrenalina) y '
           'aminoácidos. El mecanismo electrofisiológico es más complejo que una simple imagen especular de la célula β: '
           'intervienen distintas conductancias iónicas, cambios de excitabilidad y regulación paracrina por insulina, zinc, '
           'GABA y somatostatina.\nEn saciedad la glucosa, la insulina y la somatostatina de las células δ frenan la secreción, '
           'pero una comida rica en proteínas puede elevar simultáneamente insulina y glucagón: la insulina favorece la captación '
           'de aminoácidos y el glucagón evita la hipoglucemia. Error frecuente: afirmar que el glucagón siempre baja después de '
           'comer.')


def gcg_receptor(D):
    s = new(D, U, '4 · Receptor de glucagón: Gs → AMPc → PKA', 'HEPATOCITO EN AYUNO')
    membrane_h(s, 0.4, 2.25, 8.0, 0.4, name='Membrana hepatocito')
    s.shape(0.4, 2.65, 8.0, 4.45, 'rect', ('a', 'F5CBA7', 55), None, False, name='Citosol hepatocito')
    s.text(0.5, 6.7, 4, 0.35, 'CITOSOL DEL HEPATOCITO', 12.5, F_HEAD, '7A3B12', True, 'l')
    gcg = mol(s, 1.2, 1.0, 'gcg', d=0.55, name='Glucagón')
    rc = gpcr(s, 1.0, 2.27, 0.4, 0.95, name='GCGR', text='GCGR')
    gp = gprotein(s, 1.4, 2.95, 0.95, name='Gαs', text='Gs')
    ac = s.shape(3.2, 2.15, 1.3, 0.6, 'roundRect', vshade('A569BD', 0.35, 0.3), ('5B2C6F', 1.25), False, 'Adenilato\nciclasa', 11, F_HEAD, WHITE, True, 'c', 'm', name='Adenilato ciclasa')
    atp = mol(s, 3.25, 3.15, 'atp', 'ATP', d=0.42, w=0.6, name='ATP')
    camp = mol(s, 4.25, 3.2, 'atp', 'AMPc', d=0.45, w=0.75, name='AMPc')
    pka = s.shape(4.2, 4.0, 1.2, 0.6, 'roundRect', shade('48C9B0', 0.35, 0.25), ('117A65', 1.25), SHD, 'PKA', 15, F_HEAD, INK, True, 'c', 'm', name='PKA')
    a0 = s.arrow([(4.62, 3.65), (4.75, 3.98)], ACT, 2.5)
    tg = [('Fosforilasa cinasa → **glucógeno fosforilasa a**', ACT, '+', 0.5), ('**Glucógeno sintasa** (fosforilada)', INH, '−', 2.05),
          ('**PFK-2/FBPasa-2** → ↓ F2,6BP', INH, '−', 3.6), ('**Piruvato cinasa L**', INH, '−', 5.15), ('**CREB** → ↑ PCK1, G6PC', ACT, '+', 6.7)]
    ids = []
    for t, col, sg, x in tg:
        g = s.group_start('Blanco PKA ' + plain(t)[:16])
        s.arrow([(4.8, 4.62), (x + 0.7, 5.35)], col, 2.25)
        sign(s, x + 0.55, 5.3, sg, 0.28)
        s.shape(x - 0.05, 5.65, 1.5, 0.95, 'rect', MINT if col == ACT else LSALMON, (INK, 1.0), False, t, 12, F_BODY, INK, False, 'c', 'm', minsize=10)
        s.group_end(); ids.append(g)
    res = card(s, 8.7, 1.1, 4.2, 3.3, '- **↑ glucogenólisis**\n- **↑ gluconeogénesis**\n- **↓ glucólisis** y **↓ lipogénesis**\n- ↓ ACC (también vía AMPK) → ↓ malonil-CoA', CREAM, 15, head='Resultado hepático')
    nb = note_box(s, 8.7, 4.65, 4.2, 2.4, 'No asumir que el glucagón sea el activador directo **dominante** de la lipólisis adiposa humana: allí importan el **descenso de insulina** y las **catecolaminas**.', 13.5)
    s.step(path(gcg, 0.15, 0.9, dur=900), pulse(rc, after=True))
    s.step(fade(gp), path(gp, 1.55, -0.2, after=True, dur=900), pulse(ac, after=True))
    s.step(fade(atp), out(atp, after=True), zoom(camp))
    s.step(wipe(a0, 't'), fade(pka, after=True))
    s.step(*[fade(g, after=(i > 0)) for i, g in enumerate(ids)])
    s.step(fade(res))
    s.step(fade(nb))
    s.note('El glucagón se une en el hepatocito a su receptor GCGR, acoplado a Gs. La subunidad αs·GTP activa la adenilato '
           'ciclasa, que convierte ATP en AMPc; el AMPc activa la proteína cinasa A (PKA). Blancos de PKA: (1) fosforilasa '
           'cinasa → glucógeno fosforilasa a (glucogenólisis); (2) glucógeno sintasa fosforilada e inactiva; (3) la enzima '
           'bifuncional PFK-2/FBPasa-2 hepática: la fosforilación reduce la fructosa-2,6-bisfosfato, lo que disminuye la '
           'glucólisis (PFK-1) y libera la FBPasa-1 (gluconeogénesis); (4) la piruvato cinasa L se inactiva; (5) CREB '
           'fosforilado (Ser133) con CRTC2 induce PCK1 y G6PC. Resultado: el hígado pasa a producir glucosa.\nPrecisión: en el '
           'tejido adiposo humano la lipólisis depende sobre todo del descenso de la insulina y de las catecolaminas.')


def hormone_table(D):
    s = new(D, U, '4 · Cuadro de hormonas, receptores y vías')
    rows = [['Hormona', 'Receptor', 'Transducción', 'Efecto metabólico principal'],
            ['**Insulina**', 'IR (tirosina cinasa)', 'IRS → PI3K → Akt; rama MAPK', 'Almacenamiento: GLUT4, glucógeno, lipogénesis; ↓ lipólisis y ↓ producción hepática de glucosa'],
            ['**Glucagón**', 'GCGR (GPCR)', 'Gs → AC → AMPc → PKA', 'Hígado: ↑ glucogenólisis y gluconeogénesis; ↓ glucólisis y lipogénesis'],
            ['**Somatostatina**', 'SSTR (GPCR)', 'Gi → ↓ AMPc', 'Freno paracrino de α y β'],
            ['**Adrenalina**', 'Receptores α y β', 'β: Gs–AMPc; α_{2}: Gi; α_{1}: Gq', 'Efectos dependientes de tejido: glucogenólisis, lipólisis, ↓ insulina (α_{2})'],
            ['**GLP-1 / GIP**', 'GLP-1R / GIPR (GPCR)', 'Gs → AMPc → PKA/Epac2', 'Potencian la secreción de insulina dependiente de glucosa'],
            ['**Cortisol**', 'GR (intracelular)', 'Factor de transcripción (GRE)', 'Coopera con CREB/FOXO1: ↑ PCK1, G6PC; proteólisis']]
    t, H = table(s, 0.4, 1.15, 12.5, rows, [1.6, 2.1, 2.8, 5.0], size=15, rowh=0.62, name='Tabla hormonas')
    p = note_box(s, 0.4, 1.25 + H + 0.15, 12.5, 0.75, 'El **balance insulina/glucagón** importa más que observar una hormona aislada.', 16)
    s.step(fade(t))
    s.step(zoom(p))
    s.note('Relación hormona–receptor–vía. Insulina: receptor tirosina cinasa, IRS, PI3K–Akt (efectos metabólicos) y rama '
           'MAPK (crecimiento). Glucagón: GPCR acoplado a Gs, AMPc y PKA. Somatostatina: SSTR acoplado a Gi. Adrenalina: '
           'receptores α y β con efectos dependientes del tejido (β: Gs; α2: Gi, inhibe la secreción de insulina; α1: Gq). '
           'GLP-1 y GIP: GPCR acoplados a Gs. Cortisol: receptor intracelular que actúa como factor de transcripción. Mensaje: el '
           'cociente insulina/glucagón (sobre todo en sangre portal) determina la dirección del metabolismo hepático.')


def clinic_beta(D):
    s = new(D, U, '4 · Correlato clínico: el umbral secretor')
    items = [('Mutaciones de glucocinasa', '**Inactivantes**: umbral más alto → hiperglucemia leve estable.\n**Activantes**: umbral más bajo → hipoglucemia por hiperinsulinismo.', LBLUE, 'GK'),
             ('Defectos de K_{ATP}', '**Kir6.2/SUR1** con pérdida de función → canal cerrado → hiperinsulinismo congénito.\nCon ganancia de función → canal abierto → diabetes neonatal.', LILAC, 'K_{ATP}'),
             ('Sulfonilureas', 'Se unen a **SUR1** y **cierran K_{ATP}** independientemente de la glucosa → riesgo de **hipoglucemia**.', LSALMON, 'SU'),
             ('Agonistas de GLP-1', 'Potencian la insulina **según la glucosa**; enlentecen el vaciamiento gástrico y aumentan la saciedad.', MINT, 'GLP-1')]
    ids = []
    for i, (h, t, f, ic) in enumerate(items):
        x = 0.4 + (i % 2) * 6.3; y = 1.15 + (i // 2) * 2.55
        g = s.group_start('Clínica ' + plain(h))
        card(s, x, y, 6.1, 2.35, t, f, 14.5, head=h)
        badge(s, x + 5.3, y + 1.5, ic, 0.7)
        s.group_end(); ids.append(g)
    p = note_box(s, 0.4, 6.3, 12.5, 0.8, 'Ningún fármaco reemplaza la integración de órganos: el efecto final depende de hígado, músculo y adiposo.', 15)
    for g in ids:
        s.step(fade(g))
    s.step(fade(p))
    s.note('Correlato clínico. Las mutaciones activadoras de glucocinasa o los defectos de KATP cambian el umbral secretor. Las '
           'mutaciones inactivantes heterocigotas de glucocinasa causan hiperglucemia leve y estable (MODY-GCK); las activantes, '
           'hipoglucemia por hiperinsulinismo. Las mutaciones de pérdida de función de Kir6.2/SUR1 producen hiperinsulinismo '
           'congénito; las de ganancia de función, diabetes neonatal tratable con sulfonilureas (ampliación bibliográfica). Las '
           'sulfonilureas cierran KATP independientemente de la glucosa y pueden causar hipoglucemia; los agonistas de GLP-1 '
           'potencian la insulina de forma dependiente de glucosa y modifican vaciamiento gástrico y saciedad.')


def build(D):
    islet_slide(D)
    b_anat(D); b_step12(D); b_step3(D); b_step45(D); b_step6(D); b_step78(D); b_step910(D)
    b_biphasic(D); b_incretin(D); b_fasting(D)
    alpha_cell(D); gcg_receptor(D); hormone_table(D); clinic_beta(D)
