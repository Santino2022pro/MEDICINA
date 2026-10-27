# -*- coding: utf-8 -*-
"""UNIDAD II — Ayuno y ciclos interorgánicos (temas 7–9)"""
from base import *

U = 2


def div(D):
    def art(s):
        liver(s, 8.3, 1.0, 4.5, name='Arte hígado')
        clock(s, 11.6, 3.6, 1.2, 9, name='Arte reloj')
        muscle(s, 8.2, 4.3, 3.2, name='Arte músculo', fibers=2)
        rbc(s, 11.4, 5.3, 0.9, name='Arte eritrocito'); rbc(s, 12.2, 5.9, 0.7, name='Arte eritrocito 2')
        mol(s, 9.3, 3.5, 'lac', d=0.55); mol(s, 10.0, 3.4, 'ala', d=0.55); mol(s, 10.7, 3.6, 'glc', d=0.55)
    divider(D, U, 'II', 'AYUNO Y CICLOS\nINTERORGÁNICOS', 'Cuando falta el aporte intestinal',
            ['7 · Glucogenólisis hepática', '8 · Relaciones hígado–músculo–tejido adiposo', '9 · Ciclo de Cori y ciclo glucosa–alanina',
             '10 · Acoplamiento metabólico astrocito–neurona', '11 · Hígado en saciedad y ayuno corto, intermedio y prolongado',
             '12 · Reservas energéticas a 8–12 h, 24–48 h y >3 días'], art,
            'Unidad II. El problema central del ayuno es sostener la glucosa para los tejidos que la necesitan (eritrocito, '
            'médula renal, cerebro) mientras se movilizan los lípidos como combustible principal, y luego reducir la pérdida de '
            'proteína gracias a los cuerpos cetónicos.')


def fast_steps(D, part):
    s = new(D, U, 'El ayuno paso a paso: integración entre órganos (%d/2)' % part, 'MAPA · AYUNO')
    ids = organ_map(s)
    if part == 1:
        steps = [('1', 'Disminuye la entrada intestinal de glucosa', 'intestine'), ('2', 'Disminuye la señal de insulina', 'pancreas'),
                 ('3', 'Aumenta la movilización de reservas', 'liver'), ('4', 'El adiposo libera AG y glicerol', 'adipose'),
                 ('5', 'El hígado oxida AG para obtener energía', 'liver'), ('6', 'La gluconeogénesis sostiene la glucosa', 'liver')]
    else:
        steps = [('7', 'Los eritrocitos siguen generando lactato', 'vessel'), ('8', 'El lactato retorna a órganos gluconeogénicos', 'liver'),
                 ('9', 'El riñón aumenta su gluconeogénesis con el ayuno', 'kidney'), ('10', 'El cerebro adapta la selección de combustibles', 'brain'),
                 ('11', 'Los cuerpos cetónicos contribuyen al ahorro proteico', 'muscle')]
    eff = []
    if part == 1:
        x1 = s.inhib([(1.9, 4.45), (1.9, 4.12)], name='Menor absorción')
        b1 = badge(s, 2.05, 4.45, '1')
        p2 = s.inhib([(4.6, 3.35), (4.6, 3.55)], name='Insulina baja')
        i2 = mol(s, 5.0, 2.75, 'ins', d=0.32, name='Insulina escasa'); g2 = mol(s, 5.35, 2.72, 'gcg', d=0.36, name='Glucagón')
        b2 = badge(s, 5.75, 2.7, '2')
        a3 = s.arrow([(2.0, 3.1), (2.0, 3.5)], TRN, 4); b3 = badge(s, 1.45, 3.0, '3')
        a4 = s.arrow([(10.5, 2.75), (10.5, 3.5)], TRN, 4); f4 = ag_chain(s, 10.7, 3.0, 0.7, 0.16, name='AG'); gy = mol(s, 11.5, 2.95, 'gly', d=0.36)
        b4 = badge(s, 9.95, 2.95, '4')
        ag5 = ag_chain(s, 2.7, 3.1, 0.7, 0.16, name='AG al hígado'); a5 = s.arrow([(3.4, 3.5), (3.2, 3.15)], TRN, 3); b5 = badge(s, 3.05, 2.25, '5')
        g6 = mol(s, 0.85, 3.05, 'glc', d=0.38, name='Glucosa hepática'); a6 = s.arrow([(1.05, 3.1), (1.05, 3.5)], TRN, 4); b6 = badge(s, 0.4, 2.55, '6')
        grp = [(b1, x1), (b2, p2, i2, g2), (b3, a3), (b4, a4, f4, gy), (b5, ag5, a5), (b6, g6, a6)]
    else:
        l7 = mol(s, 5.0, 3.6, 'lac', d=0.36, name='Lactato eritrocitario'); b7 = badge(s, 4.45, 3.55, '7')
        a8 = s.arrow([(4.9, 3.55), (2.6, 3.1)], TRN, 4); b8 = badge(s, 3.0, 2.9, '8')
        a9 = s.arrow([(5.55, 4.45), (5.55, 4.1)], TRN, 4); g9 = mol(s, 4.7, 4.95, 'glc', d=0.38, name='Glucosa renal'); b9 = badge(s, 4.65, 5.45, '9')
        c10 = mol(s, 6.75, 2.95, 'cc', d=0.4, name='Cetonas cerebro'); a10 = s.arrow([(6.6, 3.5), (6.6, 2.75)], TRN, 4); b10 = badge(s, 7.3, 2.85, '10')
        n11 = card(s, 6.3, 4.4, 2.2, 1.05, '↓ proteólisis muscular: **ahorro proteico**', MINT, 12.5, name='Ahorro proteico'); b11 = badge(s, 8.55, 4.45, '11')
        grp = [(b7, l7), (b8, a8), (b9, a9, g9), (b10, c10, a10), (b11, n11)]
    for g in grp:
        s.step(*[fade(e, after=(i > 0)) for i, e in enumerate(g)])
    caps = []
    for (n, t, k), g in zip(steps, grp):
        caps.append(s.shape(3.0, 6.45, 5.6, 0.62, 'rect', CREAM, (INK, 1.25), SHD, '**%s.** %s' % (n, t), 15, F_BODY, INK, False, 'l', 'm',
                            name='Leyenda paso %s' % n))
    for i, c in enumerate(caps):
        s.anim[i].append(fade(c))
        if i:
            s.anim[i].insert(0, out(caps[i - 1], dur=200))
    s.note(('Integración del ayuno (pasos 1 a 6). 1) Disminuye la entrada intestinal de glucosa. 2) Disminuye la señal de '
            'insulina y aumenta relativamente el glucagón. 3) Aumenta la movilización de reservas (primero glucógeno hepático). '
            '4) El tejido adiposo libera ácidos grasos (unidos a albúmina) y glicerol. 5) El hígado utiliza ácidos grasos para '
            'obtener energía (β-oxidación). 6) La gluconeogénesis sostiene el aporte de glucosa, con energía derivada de esa '
            'oxidación lipídica. Cada número aparece por clic sobre el órgano correspondiente.') if part == 1 else
           ('Integración del ayuno (pasos 7 a 11). 7) Los eritrocitos continúan generando lactato porque dependen de la glucólisis. '
            '8) El lactato retorna a órganos gluconeogénicos (hígado y, cada vez más, riñón). 9) El riñón incrementa su '
            'participación gluconeogénica conforme progresa el ayuno. 10) El cerebro adapta gradualmente la selección de '
            'combustibles, incorporando cuerpos cetónicos. 11) La utilización de cuerpos cetónicos contribuye al ahorro proteico: '
            'disminuye la necesidad de degradar proteína muscular para fabricar glucosa.'))
    return s


def counter(D):
    s = new(D, U, 'Descenso de insulina e incremento contrarregulador')
    g = s.group_start('Balanza hormonal')
    s.shape(2.4, 5.6, 1.4, 1.2, 'triangle', shade('A04000', 0.3, 0.2), (INK, 1.5), SHD)
    s.shape(0.5, 5.2, 5.2, 0.18, 'rect', '6E2C00', (INK, 1.0), False, rot=-12)
    s.group_end()
    ins = s.shape(0.65, 4.2, 1.6, 0.85, 'roundRect', shade(MOL['ins'][0], 0.35, 0.2), (INK, 1.25), SHD, 'INSULINA ↓', 15, F_HEAD, WHITE, True, 'c', 'm', name='Insulina baja')
    ctr = s.group_start('Contrarreguladoras')
    for i, (t, k) in enumerate((('Glucagón', 'gcg'), ('Adrenalina', 'gcg'), ('Cortisol', 'chol'), ('GH', 'gly'))):
        s.shape(3.6 + (i % 2) * 1.05, 3.6 + (i // 2) * 0.55, 1.0, 0.5, 'roundRect', shade(MOL[k][0], 0.35, 0.2), (INK, 1.0), False, t, 12, F_HEAD, WHITE if k != 'gly' else INK, True, 'c', 'm')
    s.group_end()
    cs = [card(s, 6.3, 1.1, 6.6, 1.35, '**Adiposo**: se libera el freno antilipolítico → **ATGL/HSL** activas → AG + glicerol.', YEL, 14, head='Lipólisis'),
          card(s, 6.3, 2.6, 6.6, 1.35, '**Hígado**: PKA → fosforilasa activa; glucógeno sintasa inactiva.', LSALMON, 14, head='Glucogenólisis'),
          card(s, 6.3, 4.1, 6.6, 1.35, '**Hígado** (y riñón): ↓ F2,6BP, ↑ PEPCK/G6Pasa (CREB, FOXO1, GR).', MINT, 14, head='Gluconeogénesis'),
          card(s, 6.3, 5.6, 6.6, 1.5, '**Músculo**: ↓ captación de glucosa; ↑ uso de AG; exporta **alanina y glutamina** (proteólisis según la fase).', LBLUE, 14, head='Proteólisis y ahorro de glucosa')]
    k = card(s, 0.5, 1.15, 5.4, 2.1, 'No es «encender» una hormona: es el **cambio de la relación insulina/contrarreguladoras**. La insulina residual sigue frenando la lipólisis y la cetogénesis extremas.', CREAM, 14.5)
    s.step(fade(k))
    s.step(fade(g), fade(ins, after=True), fade(ctr, after=True))
    for c in cs:
        s.step(fade(c))
    s.note('Al avanzar el ayuno disminuye la insulina y aumenta relativamente la influencia de las hormonas contrarreguladoras '
           '(glucagón, catecolaminas, cortisol y hormona de crecimiento). La balanza simboliza que lo determinante es la relación '
           'entre ellas. Efectos: lipólisis adiposa (descenso de insulina y catecolaminas), glucogenólisis hepática '
           '(glucagón–PKA), gluconeogénesis (descenso de F2,6BP, inducción de PEPCK y G6Pasa por CREB/CRTC2, FOXO1 y GR) y '
           'cambios musculares (menor captación de glucosa, uso de AG, exportación de alanina y glutamina).')


# ------------------------------------------------------------------ TEMA 7
def t7a(D):
    s = new(D, U, '7 · Glucogenólisis hepática: cascada de amplificación')
    res = flow(s, ['Glucagón → GCGR', 'Gs → adenilato ciclasa', 'AMPc ↑', 'PKA activa', 'Fosforilasa cinasa', 'Glucógeno fosforilasa **a**'],
               0.4, 1.2, 4.2, 5.9, [LSALMON, LSALMON, ENE, MINT, MINT, ACT], 15, 0.22, 'v', ACT, bold=False)
    gs = card(s, 4.95, 4.3, 3.6, 1.35, 'PKA también **fosforila e inhibe la glucógeno sintasa**.', LSALMON, 14, name='GS inhibida')
    ih = s.inhib([(4.65, 3.95), (5.4, 4.3)], name='PKA inhibe GS')
    amp = card(s, 4.95, 1.2, 3.6, 2.8, 'Cada nivel **multiplica** la señal: pocas moléculas de glucagón activan muchísimas moléculas de fosforilasa.', YEL, 14.5, head='Amplificación')
    gl = glycogen(s, 9.0, 1.3, 3.8, 2.5, 22, name='Gránulos de glucógeno')
    gs_ = [mol(s, 9.4 + i * 0.75, 4.0, 'glc', 'G1P', d=0.45, name='G1P %d' % i) for i in range(4)]
    k = card(s, 8.8, 4.75, 4.1, 2.35, 'Objetivo: **defender la glucemia entre comidas**, sobre todo en las **primeras horas** de ayuno.', CREAM, 14.5, head='Para qué')
    flow_anim(s, res)
    s.step(fade(amp))
    s.step(wipe(ih, 'l'), fade(gs, after=True))
    s.step(pulse(gl), *[zoom(g, after=(i == 0)) for i, g in enumerate(gs_)])
    s.step(fade(k))
    s.note('La glucogenólisis hepática defiende la glucemia entre comidas, especialmente en las horas iniciales del ayuno. '
           'Cascada: glucagón → receptor GCGR → Gs → adenilato ciclasa → AMPc → PKA → fosforilasa cinasa → glucógeno fosforilasa b '
           'convertida en a (fosforilada, activa). Simultáneamente PKA fosforila e inhibe la glucógeno sintasa, evitando un '
           'ciclo fútil. Cada etapa enzimática amplifica la señal. Las catecolaminas pueden contribuir por receptores β (AMPc) y '
           'α1 (Ca2+) según el contexto.')


def t7b(D):
    s = new(D, U, '7 · De glucógeno a glucosa sanguínea: el papel del RE')
    s.shape(0.3, 1.05, 8.4, 6.05, 'roundRect', ('a', 'F5CBA7', 60), ('A04000', 2.0), False, adj={'adj': 6000}, name='Hepatocito')
    gl = glycogen(s, 0.55, 1.2, 2.4, 1.3, 14, name='Glucógeno')
    c = chain(s, 0.6, 2.75, ['Glucosa-1-P', 'Glucosa-6-P'], dy=1.0, w=2.2, enzymes=['Fosfoglucomutasa'], fill=[YEL, YEL], name='Ruta glucogenólisis')
    gp = enz(s, 3.1, 1.85, 'Glucógeno fosforilasa (α-1,4)', name='Fosforilasa')
    de = enz(s, 3.1, 2.3, 'Enzima desramificante (α-1,6)', name='Desramificante')
    a0 = s.arrow([(1.7, 2.52), (1.7, 2.73)], ACT, 3)
    fg = chip(s, 2.95, 1.3, '+ glucosa libre (α-1,6)', LBLUE, 11.5, name='Glucosa libre ramas')
    er = s.shape(3.6, 3.5, 3.9, 2.2, 'roundRect', ('a', 'D7BDE2', 85), ('6C3483', 2.0), False, name='Retículo endoplasmático', adj={'adj': 30000})
    s.text(3.7, 3.55, 3.7, 0.35, 'RETÍCULO ENDOPLASMÁTICO', 12.5, F_HEAD, '4A235A', True, 'c')
    g6t = glut(s, 3.3, 4.0, 0.7, text=None, color='8E44AD', horizontal=True, name='G6PT')
    s.text(3.05, 4.85, 1.0, 0.3, 'G6PT', 11.5, F_HEAD, '4A235A', True, 'c')
    g6p = enz(s, 4.4, 4.4, 'Glucosa-6-fosfatasa', name='G6Pasa')
    gluc = mol(s, 6.6, 4.35, 'glc', d=0.5, name='Glucosa RE')
    pi = mol(s, 5.5, 5.0, 'atp', 'P_{i}', d=0.38, name='Pi')
    g2 = glut(s, 8.35, 4.15, 0.7, text='GLUT2', color='5DADE2', horizontal=True, name='GLUT2 salida')
    out_ = mol(s, 9.4, 4.25, 'glc', d=0.5, name='Glucosa a sangre')
    vessel(s, 9.2, 5.2, 3.7, 0.7, name='Sinusoide', rbcs=3)
    k1 = card(s, 9.0, 1.1, 3.9, 2.7, '- La fosforilasa libera **glucosa-1-P** (fosforólisis).\n- Las ramas exigen la **desramificante**.\n- **G6Pasa** del RE: **solo hígado y riñón** liberan glucosa.', CREAM, 13.5, head='Claves')
    s.step(pulse(gl), fade(gp, after=True), fade(de), wipe(a0, 't', after=True), fade(fg))
    chain_anim(s, c, per_click=2)
    s.step(fade(er), fade(g6t, after=True))
    s.step(fade(g6p), zoom(gluc, after=True), zoom(pi))
    s.step(fade(g2), path(gluc, 2.85, 0.0, after=True, dur=1300), zoom(out_, after=True), path(out_, 0.8, 1.0, after=True, dur=900))
    s.step(fade(k1))
    s.note('La glucógeno fosforilasa rompe enlaces α-1,4 por fosforólisis y libera predominantemente glucosa-1-fosfato; la '
           'enzima desramificante resuelve los enlaces α-1,6 (liberando una pequeña fracción como glucosa libre). La '
           'fosfoglucomutasa convierte la G1P en G6P. La G6P entra al retículo endoplasmático por el transportador G6PT y la '
           'glucosa-6-fosfatasa la hidroliza a glucosa + Pi; la glucosa sale del hepatocito por GLUT2 hacia el sinusoide. '
           'La animación sigue la ruta desde el gránulo hasta la sangre.')


def t7c(D):
    s = new(D, U, '7 · Glucógeno hepático frente a muscular')
    l = s.group_start('Hígado col')
    liver(s, 0.6, 1.15, 2.6)
    card(s, 0.4, 2.9, 6.0, 2.55, '- Produce **G6P → glucosa** (G6Pasa) para **toda la sangre**.\n- Control dominante: **glucagón/insulina** (y catecolaminas).\n- Su reserva **cae al avanzar el ayuno**: la gluconeogénesis asume la responsabilidad.', MINT, 14, head='Hígado: exportador')
    s.group_end()
    m = s.group_start('Músculo col')
    muscle(s, 7.1, 1.25, 3.4, fibers=2)
    card(s, 6.9, 2.9, 6.0, 2.55, '- Genera **G6P** usada **localmente** para ATP.\n- Sin G6Pasa relevante: **no aporta glucosa a la sangre**.\n- Control dominante: **Ca^{2+}**, **AMP** y adrenalina (contracción, alarma).', LSALMON, 14, head='Músculo: consumidor')
    s.group_end()
    c = note_box(s, 0.4, 5.65, 12.5, 1.45, 'Ninguna vía es «sin costo»: la **glucogenólisis** moviliza energía **previamente almacenada**; la **gluconeogénesis gasta ATP/GTP**.', 15.5)
    s.step(fade(l)); s.step(fade(m)); s.step(fade(c))
    s.note('A diferencia del hígado, la glucogenólisis muscular genera G6P que se usa localmente para obtener ATP: el músculo '
           'carece de glucosa-6-fosfatasa relevante y no aporta glucosa a la sangre. La importancia del glucógeno hepático cae '
           'cuando se agota su reserva, y la gluconeogénesis hepática y renal asume cada vez más responsabilidad. Ninguna de las '
           'dos vías es "gratuita": la glucogenólisis moviliza energía almacenada previamente (costo de la síntesis) y la '
           'gluconeogénesis consume ATP y GTP.')


def t7d(D):
    s = new(D, U, '7 · Clínica: enfermedad de von Gierke (glucogenosis tipo I)')
    liver(s, 0.4, 1.2, 3.2, name='Hígado aumentado')
    s.text(0.4, 3.25, 3.2, 0.35, 'Hepatomegalia', 14, F_HEAD, '7B241C', True, 'c')
    blk = card(s, 0.4, 3.7, 3.2, 1.45, 'Defecto de **G6Pasa** (Ia) o del transportador **G6PT** (Ib)', RED, 14, color=WHITE, name='Defecto')
    g6 = s.shape(5.3, 1.25, 2.2, 0.8, 'roundRect', shade('F4D03F', 0.4, 0.2), (INK, 1.5), SHD, 'G6P atrapada', 16, F_HEAD, INK, True, 'c', 'm', name='G6P atrapada')
    xg = s.inhib([(6.4, 2.08), (6.4, 2.55)], name='Sin salida')
    s.text(6.6, 2.1, 2.8, 0.45, '✗ glucosa a sangre → **hipoglucemia de ayuno**', 13, F_BODY, INH, False, 'l', 'm')
    br = [((5.5, 2.05), (4.6, 5.45), 'Glucólisis → **lactato** ↑', LSALMON, (3.85, 5.5)),
          ((6.2, 2.05), (6.3, 5.45), 'PPP → ribosa → **purinas** → **ácido úrico** ↑', LILAC, (5.75, 5.5)),
          ((7.0, 2.05), (8.4, 5.45), 'Acetil-CoA → **lípidos** → **TAG** ↑', YEL, (7.65, 5.5))]
    ids = []
    for (p1, p2, t, f, (bx, by)) in br:
        g = s.group_start('Desvío ' + plain(t)[:12])
        s.arrow([p1, p2], ACT, 3)
        card(s, bx, by, 1.8, 1.6, t, f, 13, anchor='m', align='c')
        s.group_end(); ids.append(g)
    sx = card(s, 9.9, 1.15, 3.0, 5.9, '- Hipoglucemia de ayuno\n- Hepatomegalia\n- Hiperlactatemia\n- Hiperuricemia\n- Hipertrigliceridemia', CREAM, 15, head='Manifestaciones')
    s.step(fade(blk))
    s.step(zoom(g6), wipe(xg, 't', after=True))
    for g in ids:
        s.step(fade(g))
    s.step(fade(sx))
    s.note('Enfermedad de von Gierke (glucogenosis tipo I): deficiencia de glucosa-6-fosfatasa (Ia) o de su transportador G6PT '
           '(Ib). El hígado no puede liberar glucosa ni desde glucógeno ni desde gluconeogénesis: hipoglucemia de ayuno '
           'característica, hepatomegalia por acumulación de glucógeno y lípidos. La G6P atrapada se desvía a glucólisis '
           '(hiperlactatemia), a la vía de las pentosas con mayor síntesis y degradación de purinas (hiperuricemia, también por '
           'competencia del lactato en la excreción renal de urato) y a la síntesis lipídica (hipertrigliceridemia).')


# ------------------------------------------------------------------ TEMA 8
def t8_lipo(D):
    s = new(D, U, '8 · Adipocito en ayuno: lipólisis por etapas')
    adipocyte_white(s, 0.35, 1.15, 5.9, name='Adipocito en ayuno')
    plin = chip(s, 2.1, 1.75, 'Perilipina / CGI-58', LILAC, 12.5, name='Perilipina')
    c = chain(s, 1.8, 2.45, ['TAG', 'DAG', 'MAG', 'Glicerol + AG'], dy=0.95, w=2.1, enzymes=['ATGL', 'HSL', 'MGL'], rev=[False, False, False],
              fill=[ENE, YEL, YEL, LSALMON], name='Lipólisis')
    agf = [ag_chain(s, 3.9 + i * 0.25, 5.95 + i * 0.2, 0.7, 0.15, name='AG libre %d' % i) for i in range(2)]
    alb = chip(s, 6.5, 5.15, 'AG–albúmina → músculo, hígado, corazón', YEL, 12.5, name='AG albúmina')
    gly = mol(s, 2.6, 6.3, 'gly', d=0.42, name='Glicerol libre')
    gl2 = chip(s, 6.5, 6.4, 'Glicerol → hígado (y riñón): glicerol cinasa', LSALMON, 12.5, name='Destino glicerol')
    sg = card(s, 6.6, 1.15, 6.3, 3.75, '- **Descenso de insulina** (menos PDE3B, más AMPc).\n- **Catecolaminas** → β-adrenérgico → AMPc → **PKA** → fosforila **perilipina** y **HSL**.\n- **CGI-58** liberado coactiva **ATGL**.\n- No asumir que el glucagón sea el activador **dominante** de la lipólisis adiposa humana.', CREAM, 14, head='Señales')
    s.step(fade(sg))
    s.step(fade(plin), pulse(plin, after=True))
    chain_anim(s, c, per_click=1)
    s.step(*[path(a, 3.3 - i * 0.3, -0.7, dur=1300, delay=i * 200) for i, a in enumerate(agf)], fade(alb, after=True))
    s.step(path(gly, 3.4, 0.25, dur=1200), fade(gl2, after=True))
    s.note('Lipólisis en ayuno: el descenso de la insulina y las señales catecolaminérgicas permiten la acción secuencial de '
           'ATGL (TAG → DAG), HSL (DAG → MAG) y MGL (MAG → glicerol + AG). La perilipina y CGI-58 regulan el acceso de las lipasas '
           'a la gota: la PKA fosforila la perilipina, que libera CGI-58, coactivador de ATGL, y fosforila HSL. Los AG libres '
           'salen unidos a albúmina; el glicerol viaja al hígado (y riñón), que poseen glicerol cinasa. No asumir que el glucagón '
           'sea el activador directo dominante de la lipólisis adiposa humana: importan el descenso de la insulina y las '
           'catecolaminas.')


def t8_liver(D):
    s = new(D, U, '8 · Hígado en ayuno: los AG pagan la gluconeogénesis')
    s.shape(0.3, 1.05, 8.4, 6.05, 'roundRect', ('a', 'F5CBA7', 60), ('A04000', 2.0), False, adj={'adj': 6000}, name='Hepatocito')
    mt = s.shape(0.6, 2.5, 5.0, 3.6, 'ellipse', ('a', 'F8C471', 75), ('B9770E', 2.5), False, name='Mitocondria hepática')
    s.text(1.4, 2.6, 3.4, 0.3, 'MITOCONDRIA', 12.5, F_HEAD, '7E5109', True, 'c')
    ag = ag_chain(s, 0.6, 1.4, 1.0, 0.2, name='AG entrante')
    box = s.shape(1.2, 3.0, 1.6, 0.5, 'roundRect', YEL, (INK, 1.0), False, 'β-oxidación', 13, F_HEAD, INK, True, 'c', 'm', name='Beta ox')
    nadh = mol(s, 1.0, 3.75, 'atp', 'NADH/FADH_{2}', d=0.42, w=1.4, name='NADH FADH2')
    atp = mol(s, 1.25, 4.5, 'atp', 'ATP', d=0.42, w=0.8, name='ATP hígado')
    aco = s.shape(3.2, 3.0, 1.6, 0.5, 'roundRect', ENE, (INK, 1.25), False, 'Acetil-CoA ↑', 13, F_HEAD, INK, True, 'c', 'm', name='AcCoA')
    pc = enz(s, 3.3, 3.75, 'Piruvato carboxilasa', name='PC activada')
    pdh = enz(s, 3.3, 4.25, 'PDH', name='PDH inhibida')
    s1 = sign(s, 5.0, 3.75, '+', 0.3); s2 = sign(s, 4.0, 4.25, '−', 0.3)
    oaa = chip(s, 2.0, 5.3, 'Oxaloacetato → GNG', MINT, 12.5, name='OAA a GNG')
    cc = chip(s, 3.85, 5.3, 'Exceso → **cetogénesis**', PINK, 12.5, name='Cetogénesis')
    a1 = s.arrow([(1.6, 1.65), (1.95, 2.98)], TRN, 2.5); a2 = s.arrow([(2.82, 3.25), (3.18, 3.25)], ACT, 2.5)
    a3 = s.arrow([(2.0, 3.52), (1.7, 3.73)], ACT, 2.0); a4 = s.arrow([(1.7, 4.2), (1.65, 4.48)], ACT, 2.0)
    a5 = s.arrow([(4.4, 3.52), (4.6, 5.28)], ACT, 2.0)
    gng = s.shape(6.0, 2.6, 2.4, 1.0, 'roundRect', shade('58D68D', 0.4, 0.2), (INK, 1.25), SHD, 'GLUCONEOGÉNESIS\n(citosol)', 13, F_HEAD, INK, True, 'c', 'm', name='GNG')
    a6 = s.arrow([(2.05, 4.7), (6.0, 3.3)], ENE, 3.5, dash='dash')
    sub = [mol(s, 6.2, 4.3, 'lac', d=0.45), mol(s, 6.75, 4.3, 'ala', d=0.45), mol(s, 7.3, 4.3, 'gly', d=0.45)]
    sl = s.text(6.0, 4.8, 2.5, 0.6, 'Sustratos: lactato, alanina y otros AA, glicerol', 12, F_BODY, INK, False, 'c')
    gout = mol(s, 7.9, 1.6, 'glc', d=0.5, name='Glucosa exportada')
    k = card(s, 9.0, 1.1, 3.9, 6.0, '- **β-oxidación** → NADH/FADH_{2} → cadena respiratoria → **ATP** que alimenta la gluconeogénesis.\n- **Acetil-CoA** activa la **piruvato carboxilasa** e inhibe la **PDH** (no se «pierde» piruvato como CO_{2}).\n- El **oxaloacetato** se destina en parte a gluconeogénesis → el exceso de acetil-CoA va a **cetogénesis**.', CREAM, 14)
    s.step(fade(ag), path(ag, 0.5, 1.4, after=True, dur=1000), wipe(a1, 't'), fade(box, after=True))
    s.step(wipe(a3, 't'), fade(nadh, after=True), wipe(a4, 't', after=True), fade(atp, after=True))
    s.step(wipe(a2, 'l'), fade(aco, after=True), fade(pc, after=True), fade(s1), fade(pdh, after=True), fade(s2))
    s.step(fade(gng), *[fade(m, after=(i == 0)) for i, m in enumerate(sub)], fade(sl), wipe(a6, 'l', after=True), fade(oaa))
    s.step(wipe(a5, 't'), fade(cc, after=True), zoom(gout))
    s.step(fade(k))
    s.note('Hígado en ayuno: los ácidos grasos entran a la mitocondria y se β-oxidan; el NADH y el FADH2 alimentan la cadena '
           'respiratoria y el ATP producido paga la gluconeogénesis (línea punteada amarilla). El acetil-CoA es una señal: activa '
           'alostéricamente la piruvato carboxilasa (el piruvato se convierte en oxaloacetato para gluconeogénesis) e inhibe la '
           'PDH, evitando oxidar a CO2 el piruvato gluconeogénico. Como parte del oxaloacetato se desvía a gluconeogénesis, el '
           'exceso de acetil-CoA no ingresa completamente al ciclo de Krebs y se dirige a la cetogénesis. Sustratos de glucosa: '
           'lactato de eritrocitos y músculo, alanina y otros aminoácidos gluconeogénicos, glicerol del adiposo.')


def t8_gng(D):
    s = new(D, U, '8 · Gluconeogénesis: ruta, compartimentos y costo')
    mitob = s.shape(0.3, 1.05, 3.6, 3.0, 'roundRect', ('a', 'F8C471', 70), ('B9770E', 2.0), False, name='Mitocondria', adj={'adj': 25000})
    s.text(0.4, 1.1, 3.4, 0.3, 'MITOCONDRIA', 12.5, F_HEAD, '7E5109', True, 'c')
    erb = s.shape(9.2, 5.35, 3.7, 1.75, 'roundRect', ('a', 'D7BDE2', 80), ('6C3483', 2.0), False, name='RE', adj={'adj': 25000})
    s.text(9.3, 5.4, 3.5, 0.3, 'RETÍCULO ENDOPLASMÁTICO', 12.5, F_HEAD, '4A235A', True, 'c')
    pyr = chip(s, 0.6, 1.55, 'Piruvato', YEL, 13, w=1.4, h=0.42, name='Piruvato m')
    oaa = chip(s, 0.6, 2.65, 'Oxaloacetato', YEL, 13, w=1.4, h=0.42, name='OAA m')
    pc = enz(s, 2.1, 2.08, 'Piruvato carboxilasa', name='PC')
    a1 = s.arrow([(1.3, 1.99), (1.3, 2.63)], ACT, 3.5)
    c1 = mol(s, 2.35, 2.55, 'atp', 'ATP', d=0.36, w=0.6, name='ATP PC')
    mal = chip(s, 0.6, 3.45, 'Malato (lanzadera)', LSALMON, 12, w=1.9, h=0.4, name='Malato')
    a2 = s.arrow([(1.3, 3.09), (1.3, 3.43)], INK, 2.0, head='triangle')
    cyto = chain(s, 4.3, 1.4, ['Oxaloacetato', 'Fosfoenolpiruvato', '2-fosfoglicerato', 'Gliceraldehído-3-P / DHAP', 'Fructosa-1,6-bisP', 'Fructosa-6-P', 'Glucosa-6-P'],
                 dy=0.72, w=2.4, enzymes=['PEPCK (PCK1)', 'reversibles', 'reversibles', 'Aldolasa', 'FBPasa-1', None], rev=[False, True, True, True, False, True],
                 fill=[YEL, YEL, YEL, YEL, YEL, YEL, YEL], name='GNG citosol', ecol=ACT)
    a3 = s.arrow([(2.52, 3.65), (4.28, 1.6)], TRN, 2.5)
    gtp = mol(s, 7.65, 1.75, 'atp', 'GTP', d=0.36, w=0.6, name='GTP PEPCK')
    atp2 = mol(s, 7.65, 2.82, 'atp', 'ATP', d=0.36, w=0.6, name='ATP PGK')
    nadh = mol(s, 7.65, 3.55, 'atp', 'NADH', d=0.36, w=0.75, name='NADH GAPDH')
    a4 = s.arrow([(6.72, 5.94), (9.5, 6.05)], TRN, 2.5)
    g6 = enz(s, 9.6, 5.8, 'Glucosa-6-fosfatasa', name='G6Pasa')
    glc = mol(s, 11.9, 5.75, 'glc', d=0.5, name='Glucosa')
    ent = card(s, 0.3, 4.3, 3.6, 2.8, '**Entradas**:\n- **Lactato** → piruvato (LDH)\n- **Alanina** → piruvato (ALT)\n- Otros AA → intermediarios de Krebs\n- **Glicerol** → DHAP (glicerol cinasa)', CREAM, 13.5, name='Entradas')
    cost = card(s, 9.2, 1.05, 3.7, 4.1, '**Costo por glucosa** (desde 2 piruvatos): **4 ATP + 2 GTP** (6 enlaces de alta energía) + 2 NADH.\n\nLas **4 enzimas propias** (PC, PEPCK, FBPasa-1, G6Pasa) **evitan los pasos irreversibles** de la glucólisis.', YEL, 14, head='Balance')
    s.step(fade(ent))
    s.step(fade(pyr), wipe(a1, 't', after=True), fade(pc), zoom(c1), fade(oaa, after=True))
    s.step(wipe(a2, 't'), fade(mal, after=True), wipe(a3, 'l', after=True))
    chain_anim(s, cyto, per_click=2)
    s.anim[-4] += [zoom(gtp)]
    s.anim[-3] += [zoom(atp2), zoom(nadh)]
    s.step(wipe(a4, 'l'), fade(g6, after=True), zoom(glc, after=True))
    s.step(fade(cost))
    s.note('Gluconeogénesis: síntesis de glucosa desde precursores no glucídicos (lactato, alanina y otros aminoácidos '
           'glucogénicos, glicerol). Compartimentos: en la mitocondria, la piruvato carboxilasa (biotina, ATP, activada por '
           'acetil-CoA) forma oxaloacetato, que sale como malato (o aspartato); en el citosol la PEPCK (PCK1, GTP) forma '
           'fosfoenolpiruvato; los pasos reversibles de la glucólisis se recorren en sentido inverso; la FBPasa-1 (inhibida por '
           'F2,6BP y AMP) evita la PFK-1; en el retículo endoplasmático la glucosa-6-fosfatasa libera glucosa. Las flechas '
           'gruesas verdes indican los pasos propios e irreversibles. Costo: 4 ATP + 2 GTP por glucosa a partir de dos piruvatos '
           '(más 2 NADH). En humanos existe también PEPCK mitocondrial (PCK2), relevante con lactato como sustrato.')


def t8_recip(D):
    s = new(D, U, '8 · Glucólisis y gluconeogénesis: regulación recíproca')
    rows = [['Punto de control', 'Glucólisis (alimentado)', 'Gluconeogénesis (ayuno)', 'Señal'],
            ['Glucosa ↔ G6P', '**Glucocinasa** (GKRP)', '**Glucosa-6-fosfatasa**', 'Insulina ↓ G6PC; FOXO1/CREB ↑ G6PC'],
            ['F6P ↔ F1,6BP', '**PFK-1** (+AMP, +F2,6BP; −ATP, −citrato)', '**FBPasa-1** (−F2,6BP, −AMP)', 'PFK-2/FBPasa-2: PKA ↓ F2,6BP'],
            ['PEP ↔ piruvato', '**Piruvato cinasa L** (desfosforilada)', '**PC** (+acetil-CoA) + **PEPCK** (inducible)', 'PKA inactiva PK-L; CREB ↑ PCK1'],
            ['Piruvato → acetil-CoA', '**PDH** activa (desfosforilada)', 'PDH inhibida (PDK; acetil-CoA, NADH)', 'Ayuno: ↑ PDK']]
    t, H = table(s, 0.4, 1.15, 12.5, rows, [2.2, 3.4, 3.4, 3.5], size=14.5, rowh=0.75, name='Tabla recíproca')
    sw = s.group_start('Interruptor F2,6BP')
    s.shape(0.4, 1.4 + H, 12.5, 1.6, 'rect', CREAM, (INK, 1.25), SHD)
    chip(s, 0.6, 1.6 + H, 'F2,6BP alta', ENE, 15, h=0.5)
    s.text(2.35, 1.55 + H, 4.0, 0.6, '→ PFK-1 ↑ · FBPasa-1 ↓ → **glucólisis**', 14, F_BODY, INK, False, 'l', 'm')
    chip(s, 6.6, 1.6 + H, 'F2,6BP baja', 'D5D8DC', 15, h=0.5)
    s.text(8.35, 1.55 + H, 4.5, 0.6, '→ PFK-1 ↓ · FBPasa-1 ↑ → **gluconeogénesis**', 14, F_BODY, INK, False, 'l', 'm')
    s.text(0.6, 2.25 + H, 12.1, 0.6, 'La enzima bifuncional **PFK-2/FBPasa-2 hepática** decide: insulina → desfosforilada (PFK-2 activa); glucagón–PKA → fosforilada (FBPasa-2 activa).', 13.5, F_BODY, INK, False, 'l', 'm')
    s.group_end()
    s.step(fade(t)); s.step(fade(sw))
    s.note('Regulación recíproca: las dos vías comparten los pasos reversibles y difieren en tres puntos de control, regulados '
           'en sentido opuesto para evitar ciclos fútiles. El interruptor clave hepático es la fructosa-2,6-bisfosfato, producida '
           'y degradada por la enzima bifuncional PFK-2/FBPasa-2: con insulina predomina la actividad quinasa (F2,6BP alta → '
           'glucólisis); con glucagón la PKA la fosforila y predomina la actividad fosfatasa (F2,6BP baja → gluconeogénesis). '
           'Además intervienen el acetil-CoA (activa PC, inhibe PDH), la inducción génica de PCK1/G6PC y la inactivación de la '
           'piruvato cinasa L por PKA.')


def t8_mus_kid(D):
    s = new(D, U, '8 · Músculo y riñón en el ayuno')
    muscle(s, 0.4, 1.15, 4.6, name='Músculo ayuno', fibers=2)
    m = card(s, 0.4, 2.75, 6.0, 4.35, '- **↓ captación de glucosa** (menos insulina) y **↑ uso de AG**.\n- Exporta **lactato** según el flujo glucolítico.\n- Exporta **alanina y glutamina** desde el manejo de nitrógeno y la proteólisis.\n- **Nunca** libera glucosa de su glucógeno (sin G6Pasa).\n- El aporte de AA a la gluconeogénesis es **mayor al inicio** del ayuno prolongado y **se modera** cuando el cerebro usa cetonas.', CREAM, 14, head='Músculo')
    kidney(s, 7.6, 1.0, 1.25, name='Riñón ayuno')
    co = chip(s, 9.1, 1.25, 'Corteza: gluconeogénesis', MINT, 13, name='Corteza')
    me = chip(s, 9.1, 1.85, 'Médula: consume glucosa → lactato', LSALMON, 13, name='Médula')
    k = card(s, 6.9, 2.75, 6.0, 2.6, '- **Cuarto actor frecuentemente omitido**.\n- La **corteza renal** hace gluconeogénesis desde **lactato, glutamina y glicerol**.\n- Su peso crece con la **prolongación del ayuno**.', YEL, 14, head='Riñón')
    p = note_box(s, 6.9, 5.55, 6.0, 1.55, 'Integración: **el tejido que usa un combustible determina qué le queda disponible al resto**.', 14.5)
    s.step(fade(m)); s.step(fade(co), fade(me, after=True), fade(k)); s.step(fade(p))
    s.note('Músculo en ayuno: reduce la captación de glucosa por menor insulina y utiliza más ácidos grasos; exporta lactato '
           'según su flujo glucolítico y alanina/glutamina a partir del manejo de nitrógeno y de la proteólisis. Nunca libera '
           'glucosa de su glucógeno al plasma por falta de glucosa-6-fosfatasa. La contribución de aminoácidos a la '
           'gluconeogénesis depende de la fase: es más relevante al inicio del ayuno prolongado y se modera cuando el cerebro usa '
           'cetonas.\nRiñón: la corteza renal realiza gluconeogénesis a partir de lactato, glutamina y glicerol, más relevante '
           'al prolongarse el ayuno; la médula consume glucosa y produce lactato. Integración significa que el tejido que usa un '
           'combustible también determina qué le queda disponible al resto.')


# ------------------------------------------------------------------ TEMA 9
def cori(D):
    s = new(D, U, '9 · Ciclo de Cori: intercambio de lactato y glucosa', 'CICLO ANIMADO')
    muscle(s, 0.4, 1.1, 3.6, name='Músculo en ejercicio', fibers=2)
    rbc(s, 3.0, 2.55, 0.75, name='Eritrocito Cori'); rbc(s, 3.55, 2.95, 0.6, name='Eritrocito Cori 2')
    s.text(0.4, 2.45, 2.6, 0.35, 'MÚSCULO / ERITROCITO', 13, F_HEAD, '7B241C', True, 'l')
    liver(s, 9.0, 1.1, 3.9, name='Hígado Cori')
    s.text(9.4, 3.55, 3.1, 0.35, 'HÍGADO', 14, F_HEAD, '7B241C', True, 'c')
    pm = chain(s, 0.5, 3.15, ['Glucosa', 'Piruvato', 'Lactato'], dy=0.85, w=1.7, enzymes=['glucólisis', 'LDH'], rev=[False, True],
               fill=[LBLUE, YEL, lighten(MOL['lac'][0], 0.6)], name='Periferia')
    pa = mol(s, 2.5, 3.65, 'atp', '+2 ATP', d=0.38, w=0.85, name='ATP periferia')
    pn = chip(s, 2.35, 4.45, 'NADH → NAD^{+}', ENE, 11.5, name='NAD regen')
    pl = chain(s, 10.6, 4.0, ['Lactato', 'Piruvato', 'Glucosa'], dy=0.85, w=1.7, enzymes=['LDH', 'PC · PEPCK · …'], rev=[True, False],
               fill=[lighten(MOL['lac'][0], 0.6), YEL, LBLUE], name='Hígado ruta', side='l')
    lc = mol(s, 9.0, 4.85, 'atp', '−4 ATP −2 GTP', d=0.4, w=1.45, name='Costo hepático')
    top = s.arrow([(10.2, 3.0), (6.7, 1.0), (3.2, 2.25)], TRN, 5, curve=True, name='Circulación glucosa')
    bot = s.arrow([(2.3, 5.4), (6.3, 6.8), (10.5, 4.2)], '8E44AD', 5, curve=True, name='Circulación lactato')
    s.text(5.6, 1.15, 2.3, 0.35, 'GLUCOSA', 15, F_HEAD, TRN, True, 'c', name='Rótulo glucosa')
    s.text(5.4, 6.3, 2.3, 0.35, 'LACTATO', 15, F_HEAD, '8E44AD', True, 'c', name='Rótulo lactato')
    lacs = [mol(s, 2.25, 5.25, 'lac', d=0.42, name='Lactato viajero %d' % i) for i in range(2)]
    glcs = [mol(s, 10.0, 2.9, 'glc', d=0.42, name='Glucosa viajera %d' % i) for i in range(2)]
    vs = s.shape(4.6, 3.3, 3.8, 1.6, 'rect', CREAM, (INK, 1.25), SHD, '**Sangre**: el lactato no es solo desecho: es **combustible** y **precursor** de glucosa.', 14, name='Sangre Cori')
    chain_anim(s, pm, per_click=3)
    s.anim[-1] += [zoom(pa, after=True), fade(pn)]
    s.step(wipe(bot, 'l', dur=900), *[path(m, 8.1 - i * 0.1, -1.15, pts=[(2.0, 1.25), (4.1, 1.4), (6.2, 0.6)], dur=2600, delay=i * 500) for i, m in enumerate(lacs)])
    chain_anim(s, pl, per_click=3)
    s.anim[-1] += [zoom(lc, after=True)]
    s.step(wipe(top, 'r', dur=900), *[path(m, -6.8 + i * 0.1, -0.6, pts=[(-1.8, -1.6), (-3.6, -1.85), (-5.4, -1.3)], dur=2600, delay=i * 500) for i, m in enumerate(glcs)])
    s.step(fade(vs))
    s.note('Ciclo de Cori animado. En el músculo en ejercicio y en el eritrocito, la glucosa se convierte por glucólisis en '
           'piruvato y la LDH lo reduce a lactato reoxidando NADH a NAD+ (gana 2 ATP por glucosa). El lactato viaja por la sangre '
           '(las fichas violetas se desplazan por trayectoria) hasta el hígado, donde la LDH lo reconvierte en piruvato y la '
           'gluconeogénesis (piruvato carboxilasa, PEPCK y etapas siguientes) produce glucosa, que vuelve a la circulación y a los '
           'tejidos (fichas azules). El costo hepático es de 4 ATP + 2 GTP por glucosa. El ciclo no transporta nitrógeno.')


def cori_bal(D):
    s = new(D, U, '9 · Balance energético del ciclo de Cori')
    l = s.group_start('Columna periferia')
    s.shape(0.4, 1.15, 4.0, 3.2, 'rect', LSALMON, (INK, 1.25), SHD)
    s.text(0.5, 1.2, 3.8, 0.45, 'PERIFERIA', 17, F_HEAD, INK, True, 'c', 'm')
    s.text(0.6, 1.75, 3.6, 0.7, 'Glucosa → 2 lactato', 16, F_HEAD, INK, False, 'c', 'm')
    s.shape(1.2, 2.6, 2.4, 1.2, 'roundRect', ENE, (INK, 1.5), SHD, '+2 ATP', 30, F_HEAD, INK, True, 'c', 'm', fit=False)
    s.group_end()
    r = s.group_start('Columna hígado')
    s.shape(8.9, 1.15, 4.0, 3.2, 'rect', MINT, (INK, 1.25), SHD)
    s.text(9.0, 1.2, 3.8, 0.45, 'HÍGADO', 17, F_HEAD, INK, True, 'c', 'm')
    s.text(9.1, 1.75, 3.6, 0.7, '2 lactato → glucosa', 16, F_HEAD, INK, False, 'c', 'm')
    s.shape(9.5, 2.6, 2.8, 1.2, 'roundRect', 'F5B7B1', (INK, 1.5), SHD, '−4 ATP −2 GTP', 24, F_HEAD, INK, True, 'c', 'm', fit=False)
    s.group_end()
    eq = s.shape(4.7, 2.2, 3.9, 1.2, 'rect', TAG, (INK, 1.5), SHD, 'Balance neto:\n**−4 enlaces** ~P por vuelta', 17, F_HEAD, INK, False, 'c', 'm', name='Balance neto')
    k1 = card(s, 0.4, 4.6, 6.1, 2.5, '- El gasto hepático se soporta sobre todo con **β-oxidación**.\n- **Traslada carga energética** de la periferia al hígado.\n- Evita la **acumulación neta de lactato**.', CREAM, 14.5, head='Propósito')
    k2 = note_box(s, 6.8, 4.6, 6.1, 2.5, 'No es un sistema de «energía gratis»: cada vuelta **consume** más enlaces de alta energía de los que la glucólisis periférica produce.', 15)
    s.step(fade(l)); s.step(fade(r)); s.step(zoom(eq)); s.step(fade(k1)); s.step(fade(k2))
    s.note('La glucólisis periférica produce 2 ATP por glucosa; reconvertir 2 lactatos en glucosa exige 4 ATP + 2 GTP en el '
           'hígado (6 equivalentes de enlaces de alta energía). El balance neto del ciclo es negativo (−4 enlaces por vuelta). '
           'Ese gasto se soporta sobre todo con la β-oxidación hepática. Propósito: trasladar la carga energética al hígado, '
           'mantener la glucólisis en tejidos sin mitocondrias o con alta demanda y evitar la acumulación neta de lactato. No es '
           'un sistema de "energía gratis".')


def alanine(D):
    s = new(D, U, '9 · Ciclo glucosa–alanina: carbono y nitrógeno juntos', 'CICLO ANIMADO')
    muscle(s, 0.4, 1.1, 3.6, name='Músculo alanina', fibers=2)
    liver(s, 9.0, 1.1, 3.9, name='Hígado alanina')
    s.text(0.4, 2.45, 2.6, 0.35, 'MÚSCULO', 13, F_HEAD, '7B241C', True, 'l')
    s.text(9.4, 3.55, 3.1, 0.35, 'HÍGADO', 14, F_HEAD, '7B241C', True, 'c')
    m1 = card(s, 0.4, 2.9, 3.9, 2.25, '- AA (proteólisis) transfieren su **–NH_{2}** al **glutamato**.\n- **ALT**: glutamato + **piruvato** → α-cetoglutarato + **alanina**.', CREAM, 13, name='Músculo pasos')
    nm = mol(s, 3.7, 1.55, 'nh4', 'N', d=0.42, name='N muscular')
    l1 = card(s, 8.9, 3.95, 4.0, 3.15, '- **ALT**: alanina → **piruvato** (a gluconeogénesis).\n- El grupo amino → **glutamato** → **GDH** → NH_{4}^{+} + **aspartato** → **ciclo de la urea**.\n- La glucosa vuelve al músculo.', CREAM, 13, name='Hígado pasos')
    ur = mol(s, 12.3, 2.9, 'urea', d=0.5, name='Urea')
    top = s.arrow([(10.2, 3.0), (6.7, 1.0), (3.2, 2.25)], TRN, 5, curve=True, name='Circulación glucosa')
    bot = s.arrow([(2.3, 5.3), (5.8, 7.0), (8.85, 6.0)], '2E9E5B', 5, curve=True, name='Circulación alanina')
    s.text(5.6, 1.15, 2.3, 0.35, 'GLUCOSA', 15, F_HEAD, TRN, True, 'c')
    s.text(5.4, 6.3, 2.3, 0.35, 'ALANINA', 15, F_HEAD, '1E8449', True, 'c')
    alas = [mol(s, 2.3, 5.2, 'ala', d=0.42, name='Alanina viajera %d' % i) for i in range(2)]
    glcs = [mol(s, 10.0, 2.9, 'glc', d=0.42, name='Glucosa viajera %d' % i) for i in range(2)]
    cmp_ = card(s, 4.6, 3.1, 3.9, 2.0, '**Ventaja**: transporta carbono gluconeogénico **y** nitrógeno de forma relativamente **segura** (no como NH_{3} libre).', YEL, 13.5, name='Ventaja')
    s.step(fade(m1), zoom(nm, after=True))
    s.step(wipe(bot, 'l', dur=900), *[path(m, 6.3 - i * 0.2, 0.6, pts=[(1.5, 1.2), (3.3, 1.5), (5.0, 1.15)], dur=2600, delay=i * 500) for i, m in enumerate(alas)])
    s.step(fade(l1), zoom(ur, after=True))
    s.step(wipe(top, 'r', dur=900), *[path(m, -6.8 + i * 0.1, -0.6, pts=[(-1.8, -1.6), (-3.6, -1.85), (-5.4, -1.3)], dur=2600, delay=i * 500) for i, m in enumerate(glcs)])
    s.step(fade(cmp_))
    s.note('Ciclo glucosa–alanina. En el músculo, los grupos amino de los aminoácidos (de la proteólisis) se concentran en el '
           'glutamato por transaminación; la alanina aminotransferasa (ALT) transfiere el nitrógeno al piruvato formando alanina. '
           'La alanina llega al hígado; la ALT regenera piruvato para la gluconeogénesis, y el grupo amino alcanza la urea a '
           'través de glutamato, glutamato deshidrogenasa (NH4+) y aspartato. La glucosa vuelve al músculo. Beneficios: '
           'transportar carbono gluconeogénico y nitrógeno de manera relativamente segura. Costo: la gluconeogénesis más la '
           'detoxificación del nitrógeno (ciclo de la urea).')


def cori_vs_ala(D):
    s = new(D, U, '9 · Cori frente a glucosa–alanina')
    rows = [['', 'Ciclo de Cori', 'Ciclo glucosa–alanina'],
            ['Metabolito que viaja al hígado', '**Lactato**', '**Alanina**'],
            ['¿Transporta nitrógeno?', '**No**', '**Sí** (grupo amino → urea)'],
            ['Origen periférico', 'Eritrocito, músculo glucolítico', 'Músculo (transaminación; proteólisis)'],
            ['Enzima periférica clave', 'LDH (regenera NAD^{+})', 'ALT (aminotransferasa)'],
            ['Costo hepático', 'Gluconeogénesis (4 ATP + 2 GTP)', 'Gluconeogénesis + **ciclo de la urea**'],
            ['Mensaje', 'Lactato = combustible y precursor', 'Exporta N de forma segura']]
    t, H = table(s, 0.4, 1.15, 8.6, rows, [2.6, 3.0, 3.0], size=14.5, rowh=0.62, name='Tabla Cori alanina')
    for i, (k, x) in enumerate((('lac', 9.6), ('ala', 11.4))):
        mol(s, x, 1.4, k, d=1.2, name='Ficha grande %s' % k)
    p = note_box(s, 9.3, 3.0, 3.6, 2.4, 'Diferencia que suele evaluarse: **Cori no transporta nitrógeno; el ciclo de la alanina sí**.', 15)
    l = card(s, 9.3, 5.6, 3.6, 1.5, 'El lactato **no es solo desecho**: combustible oxidativo y precursor biosintético.', YEL, 13.5)
    s.step(fade(t)); s.step(zoom(p)); s.step(fade(l))
    s.note('Comparación de ambos ciclos. Los dos facilitan la coordinación entre tejidos y devuelven glucosa a la periferia. La '
           'diferencia clave: el ciclo de Cori no transporta nitrógeno; el ciclo glucosa–alanina sí, y por eso agrega el costo '
           'del ciclo de la urea. El lactato no es solo un "desecho": también es combustible oxidativo (corazón, músculo oxidativo) '
           'y precursor biosintético.')


def build(D):
    div(D)
    fast_steps(D, 1); fast_steps(D, 2); counter(D)
    t7a(D); t7b(D); t7c(D); t7d(D)
    t8_lipo(D); t8_liver(D); t8_gng(D); t8_recip(D); t8_mus_kid(D)
    cori(D); cori_bal(D); alanine(D); cori_vs_ala(D)
