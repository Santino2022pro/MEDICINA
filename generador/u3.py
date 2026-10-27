# -*- coding: utf-8 -*-
"""UNIDAD III — temas 13 y 14 (malonil-CoA con escenarios Morph; combustibles musculares)"""
from base import *

U = 3


def div(D):
    def art(s):
        adipocyte_white(s, 8.6, 0.9, 2.6, name='Arte adipocito')
        mito(s, 10.6, 3.3, 2.4, name='Arte mitocondria')
        lipoprotein(s, 8.3, 3.7, 1.6, 'F7DC6F', 'VLDL', [('2E4A9E', 200, 140, 6, None)], name='Arte VLDL')
        lipoprotein(s, 9.7, 5.4, 1.2, 'F39C12', 'LDL', [('2E4A9E', 180, 160, 6, None)], name='Arte LDL')
        ag_chain(s, 11.2, 5.8, 1.5, 0.3, name='Arte AG')
    divider(D, U, 'III', 'LÍPIDOS, COLESTEROL\nY CONTROL METABÓLICO', 'Síntesis, oxidación, transporte y regulación génica',
            ['13 · Malonil-CoA: punto de decisión', '14 · Combustibles musculares', '15 · ATP desde ácidos grasos', '16 · Origen de los TAG hepáticos',
             '17 · AG de cadena corta y media', '18 · Ácidos grasos esenciales', '19 · Quilomicrones y VLDL', '20 · AMPK: sensor energético',
             '21 · Colesterol: síntesis, transporte, destino', '22 · Cetogénesis y cetólisis', '23 · Control génico', '24 · Estrés fisiológico'], art,
            'Unidad III. Se integran las decisiones lipídicas: sintetizar u oxidar (malonil-CoA/CPT1), cómo se obtiene ATP de los '
            'AG, cómo viajan los lípidos (QM, VLDL, LDL, HDL), el sensor AMPK, el colesterol, los cuerpos cetónicos y los factores '
            'de transcripción que adaptan la maquinaria enzimática.')


def t13a(D):
    s = new(D, U, '13 · Malonil-CoA: una molécula, dos funciones')
    c = chain(s, 0.6, 1.3, ['Acetil-CoA', 'Malonil-CoA', 'Palmitato (C16)'], dy=1.45, w=2.6, enzymes=['ACC (biotina · ATP · HCO_{3}^{−})', 'FASN (+7 malonil · NADPH)'],
              rev=[False, False], fill=[ENE, lighten(MOL['mal'][0], 0.55), YEL], name='Síntesis AG', h=0.55, size=15)
    s.shape(0.4, 1.05, 5.9, 4.2, 'rect', ('a', 'FFFFFF', 0), (ACT, 2.0, 'dash'), False, name='Marco citosol')
    s.text(0.5, 4.85, 3.5, 0.35, 'CITOSOL · síntesis', 13, F_HEAD, ACT, True, 'l')
    mt = s.shape(7.4, 1.4, 5.4, 3.6, 'ellipse', ('a', 'F8C471', 70), ('B9770E', 3.0), SHD, name='Mitocondria')
    s.text(8.4, 4.3, 3.4, 0.35, 'MITOCONDRIA · β-oxidación', 13, F_HEAD, '7E5109', True, 'c')
    cp = s.shape(6.95, 2.6, 0.9, 1.0, 'roundRect', shade('F5B041', 0.4, 0.3), ('9C640C', 1.5), SHD, 'CPT1', 14, F_HEAD, INK, True, 'c', 'm', name='CPT1')
    ag = ag_chain(s, 5.1, 3.75, 1.6, 0.25, name='AG de cadena larga')
    ih = s.inhib([(3.3, 3.25), (6.85, 3.15)], name='Malonil inhibe CPT1', w=3.0)
    lb = s.text(3.7, 2.7, 2.8, 0.35, 'inhibición alostérica', 13, F_HEAD, INH, True, 'c')
    bx = s.shape(8.3, 2.3, 3.6, 1.6, 'ellipse', ('a', 'FFFFFF', 50), ('7E5109', 1.25, 'dash'), False, 'β-oxidación de AG largos', 15, F_HEAD, '7E5109', True, 'c', 'm', name='Beta ox')
    k = card(s, 0.4, 5.45, 12.5, 1.65, 'El malonil-CoA es **(a)** el donador de unidades de 2 C para la **FASN** y **(b)** el **inhibidor alostérico de CPT1**, puerta de entrada de los AG largos a la mitocondria. Así se impide —**aunque no de forma absoluta**— sintetizar y degradar AG a la vez.', YEL, 14.5)
    chain_anim(s, c, per_click=1)
    s.step(fade(mt), fade(bx), fade(cp, after=True), fade(ag))
    s.step(wipe(ih, 'l'), fade(lb, after=True), pulse(cp, after=True))
    s.step(fade(k))
    s.note('El malonil-CoA se forma por carboxilación del acetil-CoA catalizada por la acetil-CoA carboxilasa (ACC), con biotina '
           'como cofactor, bicarbonato y consumo de ATP. Es a la vez (a) donador de unidades de dos carbonos para la síntesis '
           'citosólica de AG por la FASN (7 malonil-CoA + 1 acetil-CoA + 14 NADPH → palmitato), y (b) inhibidor alostérico de la '
           'carnitina palmitoiltransferasa 1 (CPT1), puerta de entrada de los AG de cadena larga a la oxidación mitocondrial. De '
           'este modo impide, aunque no absolutamente, sintetizar y degradar AG simultáneamente.')


def mal_scene(s, fed):
    """escenario común (nombres «!!» para Morph entre alimentado y ayuno/ejercicio)"""
    s.shape(0.3, 1.05, 6.6, 4.85, 'rect', ('a', 'FFFFFF', 35), (INK, 1.0), False, name='!!Citosol')
    s.text(0.4, 1.08, 3, 0.32, 'CITOSOL', 12.5, F_HEAD, INK, True, 'l', name='!!Rótulo citosol')
    s.shape(7.3, 1.25, 5.6, 4.5, 'ellipse', ('a', 'F8C471', 75), ('B9770E', 3.0), SHD, name='!!Mitocondria')
    s.text(8.3, 1.45, 3.6, 0.32, 'MITOCONDRIA', 12.5, F_HEAD, '7E5109', True, 'c', name='!!Rótulo mitocondria')
    ids = {}
    ids['cpt'] = channel(s, 6.85, 2.7, 1.05, open_=not fed, name='!!CPT1', color='F5B041', flank='FAD7A0', horizontal=True)
    s.text(6.5, 2.3, 1.6, 0.3, 'CPT1', 14, F_HEAD, '7E5109', True, 'c', name='!!Rótulo CPT1')
    ids['acc'] = s.shape(2.0, 2.5, 1.7, 0.75, 'roundRect', shade('58D68D' if fed else 'BDC3C7', 0.35, 0.2), (INK, 1.5), SHD,
                         'ACC activa' if fed else 'ACC–P inactiva', 14, F_HEAD, INK, True, 'c', 'm', name='!!ACC')
    s.shape(8.4, 3.75, 3.4, 0.4, 'rect', ('a', 'FFFFFF', 70), (INK, 1.0), False, name='!!Fondo indicador')
    ids['bar'] = s.shape(8.42, 3.77, 0.55 if fed else 3.36, 0.36, 'rect', ('lin', [(0, 'F9E79F'), (100, 'E67E22')], 0), None, False, name='!!Barra beta-ox')
    s.text(8.4, 3.3, 3.4, 0.4, 'flujo de β-oxidación', 13, F_HEAD, '7E5109', True, 'c', name='!!Rótulo flujo')
    return ids


def caption_steps(s, steps, x=0.3, y=6.05, w=12.6, h=1.05):
    caps = []
    for i, t in enumerate(steps):
        caps.append(s.shape(x, y, w, h, 'rect', CREAM, (INK, 1.25), SHD, '**%d.** %s' % (i + 1, t), 16, F_BODY, INK, False, 'l', 'm', name='Paso texto %d' % (i + 1)))
    return caps


def t13_fed(D):
    s = new(D, U, '13 · Escenario 1: estado alimentado', 'MALONIL-CoA · ALIMENTADO')
    ids = mal_scene(s, True)
    ins = mol(s, 0.6, 1.55, 'ins', d=0.5, name='!!Insulina')
    cit = chip(s, 0.55, 3.55, 'Citrato ↑', YEL, 14, name='!!Citrato')
    ph = enz(s, 0.5, 2.35, 'Fosfatasas', name='Fosfatasas')
    mals = [mol(s, 4.2 + (i % 3) * 0.6, 2.3 + (i // 3) * 0.6, 'mal', 'Mal', d=0.48, name='!!Malonil %d' % i) for i in range(5)]
    fas = s.shape(2.0, 4.25, 1.7, 0.6, 'roundRect', shade('F7DC6F', 0.4, 0.2), (INK, 1.25), False, 'FASN → AG', 14, F_HEAD, INK, True, 'c', 'm', name='!!FASN')
    ags = [ag_chain(s, 5.0, 4.4 + i * 0.4, 1.4, 0.2, name='!!AG largo %d' % i) for i in range(2)]
    blk = s.text(5.0, 5.25, 1.9, 0.5, 'AG largos **no entran**', 13, F_HEAD, INH, False, 'c', 'm', name='Bloqueo')
    a1 = s.arrow([(2.85, 3.27), (2.85, 4.23)], ACT, 3)
    ih = s.inhib([(5.9, 2.9), (6.8, 3.2)], w=3.0, name='Freno CPT1')
    caps = caption_steps(s, ['**Estado alimentado**: insulina alta y abundante citrato citosólico.',
                             '**Síntesis de AG activada**: la insulina activa fosfatasas; el citrato favorece la polimerización de ACC.',
                             '**ACC activa** carboxila acetil-CoA.', '**Malonil-CoA ↑** (sustrato de la FASN).',
                             '**Malonil-CoA inhibe CPT1** (alostérico).', '**↓ entrada mitocondrial** de AG de cadena larga.',
                             '**β-oxidación relativamente ↓**: se evita oxidar lo que se está sintetizando.'])
    seq = [[fade(caps[0]), fade(ins, after=True), fade(cit)],
           [fade(ph), pulse(ids['acc'], after=True)], [pulse(ids['acc'])],
           [*[zoom(m, after=(i == 0)) for i, m in enumerate(mals)], wipe(a1, 't', after=True), fade(fas, after=True)],
           [wipe(ih, 'l'), pulse(ids['cpt'], after=True)], [*[fade(a) for a in ags], fade(blk, after=True)], [pulse(ids['bar'])]]
    for i, st in enumerate(seq):
        if i:
            st = [out(caps[i - 1], dur=200), fade(caps[i])] + st
        s.step(*st)
    s.note('Escenario 1 (estado alimentado), siete pasos por clic: insulina alta y citrato abundante; la insulina activa '
           'fosfatasas que desfosforilan (activan) la ACC y el citrato promueve su polimerización; la ACC activa produce '
           'malonil-CoA; el malonil-CoA alimenta la FASN y a la vez inhibe la CPT1; disminuye la entrada mitocondrial de AG de '
           'cadena larga y la β-oxidación queda relativamente reducida (barra corta). A escala de horas, SREBP-1c y ChREBP '
           'incrementan la cantidad de ACC y FASN. La diapositiva siguiente usa Morph para transformar este escenario en el de '
           'ayuno o ejercicio.')


def t13_fast(D):
    s = new(D, U, '13 · Escenario 2: ayuno o ejercicio', 'MALONIL-CoA · AYUNO / EJERCICIO', morph=True)
    ids = mal_scene(s, False)
    am = s.shape(0.5, 1.55, 1.6, 0.65, 'roundRect', shade('E74C3C', 0.35, 0.2), (INK, 1.5), SHD, 'AMPK', 16, F_HEAD, WHITE, True, 'c', 'm', name='!!AMPK')
    amp = mol(s, 2.3, 1.55, 'atp', 'AMP/ADP ↑', d=0.45, w=1.35, name='AMP alto')
    p = mol(s, 3.55, 2.35, 'atp', 'P', d=0.4, name='Fosfato ACC')
    a1 = s.arrow([(1.3, 2.22), (2.1, 2.55)], INH, 3)
    mal = mol(s, 4.2, 2.3, 'mal', 'Mal', d=0.25, name='!!Malonil 0')
    mcd = enz(s, 4.6, 1.6, 'MCD (descarboxilasa)', name='MCD')
    ags = [ag_chain(s, 9.0, 2.2 + i * 0.45, 1.4, 0.2, name='!!AG largo %d' % i) for i in range(2)]
    eg = [mol(s, 10.6, 2.15, 'atp', 'NADH', d=0.38, w=0.75, name='NADH b'), mol(s, 11.45, 2.15, 'atp', 'FADH_{2}', d=0.38, w=0.85, name='FADH2 b')]
    caps = caption_steps(s, ['**Ayuno o ejercicio**: ↑ relación AMP/ATP y ADP/ATP (o ↓ insulina, ↑ glucagón).',
                             '**AMPK activada** (Thr172).', '**Fosforila e inhibe ACC** (ACC1 y ACC2).',
                             '**Malonil-CoA ↓** (además lo degrada la malonil-CoA descarboxilasa).',
                             '**Se libera el freno sobre CPT1**.', '**↑ entrada mitocondrial** de AG de cadena larga.',
                             '**β-oxidación ↑**: NADH y FADH_{2} para ATP (y, en el hígado, para gluconeogénesis y cetogénesis).'])
    seq = [[fade(caps[0]), fade(amp, after=True)], [zoom(am), pulse(am, after=True)], [wipe(a1, 'l'), zoom(p, after=True)],
           [fade(mcd), pulse(mal, after=True), out(mal, after=True)], [pulse(ids['cpt'])],
           [*[pulse(a, after=(i == 0)) for i, a in enumerate(ags)]],
           [pulse(ids['bar']), *[zoom(e, after=True) for e in eg]]]
    for i, st in enumerate(seq):
        if i:
            st = [out(caps[i - 1], dur=200), fade(caps[i])] + st
        s.step(*st)
    s.note('Transición Morph desde el escenario alimentado: la ACC cambia de color (activa → fosforilada inactiva), los '
           'malonil-CoA desaparecen o se reducen, la CPT1 pasa de cerrada a abierta, los AG largos pasan del citosol a la '
           'mitocondria y la barra de flujo de β-oxidación se alarga. Luego, por clic: ayuno o ejercicio; activación de AMPK; '
           'fosforilación e inhibición de ACC; caída del malonil-CoA (también por la malonil-CoA descarboxilasa, MCD); liberación '
           'del freno de CPT1; mayor entrada de AG; aumento de la β-oxidación. En el hígado del ayuno el glucagón (PKA) y la baja '
           'insulina contribuyen igual que la AMPK. La AMPK también modula expresión génica y otros blancos: no atribuir todo el '
           'cambio a una sola enzima.')


def t13_muscle(D):
    s = new(D, U, '13 · ¿Por qué el músculo fabrica malonil-CoA?')
    muscle_fiber(s, 0.4, 1.15, 12.5, 0.75, name='Fibra muscular')
    mt = s.shape(0.5, 2.3, 5.6, 3.0, 'ellipse', ('a', 'F8C471', 75), ('B9770E', 2.5), False, 'MITOCONDRIA\nβ-oxidación de AG largos', 15, F_HEAD, '7E5109', True, 'c', 'm', name='Mitocondria muscular')
    acc2 = s.shape(4.9, 2.35, 1.9, 0.6, 'roundRect', shade('58D68D', 0.35, 0.2), (INK, 1.25), SHD, 'ACC2 (ACACB)', 13, F_HEAD, INK, True, 'c', 'm', name='ACC2')
    cpt = s.shape(5.5, 3.3, 1.2, 0.6, 'roundRect', shade('F5B041', 0.4, 0.3), (INK, 1.25), SHD, 'CPT1B', 13, F_HEAD, INK, True, 'c', 'm', name='CPT1B')
    mal = mol(s, 6.0, 2.95, 'mal', 'Mal', d=0.38, name='Malonil local')
    mcd = enz(s, 6.9, 2.55, 'MCD', name='MCD músculo')
    k1 = card(s, 7.6, 2.2, 5.3, 2.0, 'Predomina la **función señalizadora**: la ACC2, próxima a la membrana mitocondrial, genera malonil-CoA que modula **CPT1B**.', CREAM, 14, head='Señal, no síntesis')
    k2 = card(s, 0.4, 5.5, 6.1, 1.6, '**Reposo alimentado**: el malonil-CoA puede **limitar** la oxidación de grasas.', LBLUE, 14.5)
    k3 = card(s, 6.8, 4.4, 6.1, 2.7, '**Contracción**: **AMPK inhibe ACC2** → ↓ malonil-CoA (y la MCD contribuye) → ↑ oxidación de AG.\nLa actividad de **FASN muscular es baja** frente a los tejidos lipogénicos.', MINT, 14)
    s.step(fade(acc2), zoom(mal, after=True), fade(cpt, after=True))
    s.step(fade(k1)); s.step(fade(k2)); s.step(fade(mcd), fade(k3))
    s.note('¿Por qué el músculo fabrica malonil-CoA si no hace lipogénesis neta relevante? Porque predomina su función '
           'señalizadora: la ACC2 (ACACB), localizada cerca de la membrana mitocondrial externa, genera malonil-CoA que modula la '
           'CPT1B. En reposo alimentado puede limitar la oxidación de grasas; con la contracción la AMPK inhibe la ACC2, '
           'favoreciendo la oxidación. La malonil-CoA descarboxilasa (MCD/MLYCD) contribuye a su descenso. La actividad de FASN '
           'muscular es baja comparada con tejidos lipogénicos.')


def t13_ir(D):
    s = new(D, U, '13 · Lípidos y resistencia a la insulina: localización y especie')
    membrane_h(s, 0.3, 1.3, 7.6, 0.4, name='Membrana')
    insulin_receptor(s, 1.0, 1.32, 0.4, 0.65, name='Receptor')
    irs = s.shape(2.3, 2.15, 1.2, 0.5, 'roundRect', shade('F5B041', 0.4, 0.2), ('9C640C', 1.25), False, 'IRS', 14, F_HEAD, INK, True, 'c', 'm', name='IRS')
    akt = s.shape(4.4, 2.15, 1.3, 0.5, 'roundRect', shade('58D68D', 0.4, 0.2), ('1E8449', 1.25), False, 'Akt', 14, F_HEAD, INK, True, 'c', 'm', name='Akt')
    a = s.arrow([(3.55, 2.4), (4.35, 2.4)], ACT, 3, dash='dash')
    dag = mol(s, 2.3, 3.4, 'tag', 'DAG', d=0.6, name='DAG'); cer = mol(s, 3.1, 3.5, 'chol', 'Cer', d=0.6, name='Ceramidas')
    pkc = enz(s, 2.2, 4.3, 'PKCε / otras cinasas', name='PKC')
    i1 = s.inhib([(2.8, 4.25), (2.85, 2.7)], w=2.5)
    i2 = s.inhib([(3.65, 3.6), (4.8, 2.7)], w=2.5)
    drop = lipid_drops(s, 5.6, 3.2, 2.2, 2.2, [(500, 500, 420)], name='Gota TAG')
    s.text(5.4, 5.45, 2.6, 0.5, 'TAG en gota: relativamente inerte', 12.5, F_HEAD, '7E5109', True, 'c')
    k1 = card(s, 8.2, 1.1, 4.7, 2.9, 'La acumulación de **DAG** y **ceramidas** en localizaciones críticas puede **perturbar la señalización** de insulina (IRS/Akt).', CREAM, 14, head='Intermediarios lipotóxicos')
    k2 = note_box(s, 8.2, 4.2, 4.7, 2.9, 'No basta medir **TAG intracelulares totales** para inferir «lipotoxicidad»: importan la **localización** y las **especies moleculares**.', 14.5)
    s.step(fade(irs), wipe(a, 'l', after=True), fade(akt, after=True))
    s.step(zoom(dag), zoom(cer), fade(pkc, after=True), wipe(i1, 't', after=True), wipe(i2, 'l'))
    s.step(fade(k1)); s.step(fade(drop)); s.step(fade(k2))
    s.note('Relación con la resistencia a la insulina: la acumulación de intermediarios lipídicos como DAG (que activa PKCε u '
           'otras isoformas, con fosforilación inhibitoria del receptor/IRS) y ceramidas (que interfieren con Akt) en '
           'localizaciones críticas puede perturbar la señalización de insulina (mecanismos detallados: ampliación '
           'bibliográfica). Distinción clave: acumulación de TAG (gotas relativamente inertes) frente a intermediarios '
           'lipotóxicos; no basta medir TAG totales, importan localización y especie molecular (por ejemplo, los atletas '
           'entrenados pueden tener TAG intramuscular alto con buena sensibilidad insulínica).')


# ------------------------------------------------------------------ TEMA 14
def t14a(D):
    s = new(D, U, '14 · Combustibles musculares: reposo, aeróbico y anaeróbico')
    cols = [('REPOSO', 'B03A2E', '- Mezcla de **AG y glucosa**.\n- Con alta disponibilidad lipídica e insulina baja ↑ AG.\n- ATP/citrato altos **frenan PFK-1**.\n- NADH y acetil-CoA ↑ → **PDK** inactiva PDH.\n- **CPT1** permite AG si el malonil-CoA no la inhibe.', LBLUE),
            ('AERÓBICO MODERADO', 'C0392B', '- ↑ ATP oxidativo: capilares, mitocondrias, **fibras tipo I**.\n- Contracción: ↑ AMP/ADP, **Ca^{2+}**, **AMPK**.\n- PFK-1 ↑ si AMP/ADP alto; **PDP** (Ca^{2+}) activa PDH.\n- ACC2 inhibida → **CPT1 liberada**.\n- Nunca es «solo grasas».', MINT),
            ('MUY INTENSO', 'E74C3C', '- La demanda supera la velocidad oxidativa local.\n- **Fosfocreatina** (creatina cinasa): ATP inmediato.\n- Glucogenólisis y glucólisis aceleradas.\n- Piruvato → **lactato** regenera NAD^{+}.\n- Lactato ↑ **no prueba** falta absoluta de O_{2}.', LSALMON)]
    ids = []
    for i, (t, c, txt, f) in enumerate(cols):
        x = 0.4 + i * 4.2
        g = s.group_start('Columna ' + t)
        muscle_fiber(s, x, 1.15, 4.0, 0.62, name='Fibra ' + t, color=c)
        card(s, x, 1.95, 4.0, 4.4, txt, f, 14, head=t)
        s.group_end(); ids.append(g)
    p = card(s, 0.4, 6.5, 12.5, 0.65, 'La proporción grasa/carbohidrato depende de **intensidad, duración, entrenamiento y alimentación previa**.', YEL, 14.5, grow=False)
    for g in ids:
        s.step(fade(g))
    s.step(fade(p))
    s.note('Reposo: el músculo esquelético utiliza una mezcla de AG y glucosa; con alta disponibilidad lipídica e insulina baja '
           'aumenta la contribución de AG. ATP y citrato altos frenan PFK-1; NADH y acetil-CoA altos estimulan la PDH cinasa (PDK), '
           'que fosforila e inhibe la PDH, ahorrando piruvato. CPT1 permite importar AG si el malonil-CoA no la inhibe.\n'
           'Aeróbico moderado prolongado: crece la necesidad de ATP oxidativo; capilares, mitocondrias y fibras tipo I facilitan '
           'la β-oxidación; la contracción aumenta AMP/ADP, Ca2+ y AMPK; PFK-1 aumenta su flujo; la PDH fosfatasa estimulada por '
           'Ca2+ activa la PDH; ACC2 inhibida reduce malonil-CoA y libera CPT1.\nMuy intenso: la demanda supera la velocidad de '
           'las vías oxidativas locales; la fosfocreatina entrega ATP inmediato; la glucogenólisis y la glucólisis se aceleran; '
           'el lactato regenera NAD+. El lactato también se forma con O2 cuando el flujo glucolítico es alto.')


def t14b(D):
    s = new(D, U, '14 · Regulación fina: PFK-1, PDH y CPT1')
    blocks = [('PFK-1', 'Glucólisis', ['AMP', 'ADP', 'F2,6BP'], ['ATP alto', 'Citrato', 'Acidez (H^{+})']),
              ('PDH', 'Piruvato → acetil-CoA', ['Piruvato (inhibe PDK)', 'Ca^{2+} (activa PDP)', 'Insulina (hígado/adiposo)'], ['NADH/NAD^{+} ↑', 'Acetil-CoA/CoA ↑', 'ATP/ADP ↑ (vía PDK)']),
              ('CPT1', 'Entrada de AG largos', ['↓ malonil-CoA (AMPK, MCD)', 'Glucagón (hígado)'], ['**Malonil-CoA**'])]
    ids = []
    for i, (e, v, act, inh) in enumerate(blocks):
        y = 1.15 + i * 1.95
        g = s.group_start('Regulación ' + e)
        s.shape(4.6, y + 0.35, 2.4, 1.0, 'roundRect', 'FFFFFF', ('1F3864', 2.5), SHD, e, 22, F_HEAD, '1F3864', True, 'c', 'm', adj={'adj': 40000})
        s.text(4.4, y + 1.35, 2.8, 0.35, v, 12.5, F_HEAD, '5D4037', True, 'c')
        card(s, 0.4, y + 0.15, 3.6, 1.45, '\n'.join('+ ' + a for a in act), MINT, 16, grow=False)
        s.arrow([(4.03, y + 0.85), (4.55, y + 0.85)], ACT, 4)
        card(s, 7.55, y + 0.15, 3.6, 1.45, '\n'.join('x ' + a for a in inh), LSALMON, 16, grow=False)
        s.inhib([(7.52, y + 0.85), (7.05, y + 0.85)], w=4)
        s.group_end(); ids.append(g)
    nb = note_box(s, 11.35, 1.15, 1.55, 5.9, 'No confundir **CPT1** con **CACT** (translocasa carnitina–acilcarnitina), otra proteína del transporte.', 13)
    for g in ids:
        s.step(fade(g))
    s.step(fade(nb))
    s.note('Regulación fina. PFK-1: activadores AMP, ADP y fructosa-2,6-bisfosfato; inhibidores ATP elevado, citrato y acidez '
           '(según isoforma y contexto). PDH: la PDH cinasa la fosforila e inactiva cuando aumentan NADH/NAD+, acetil-CoA/CoA y '
           'ATP/ADP; el piruvato inhibe la PDK y el Ca2+ activa la PDH fosfatasa en el músculo. CPT1 (también llamada "CAT-1" en '
           'algunas guías): el malonil-CoA la inhibe. No confundir con la carnitina–acilcarnitina translocasa (CACT), otra '
           'proteína del transporte.')


def t14c(D):
    s = new(D, U, '14 · Sistemas de producción de ATP según la intensidad')
    g = s.group_start('Gráfico sistemas ATP')
    s.shape(0.4, 1.1, 7.4, 5.0, 'rect', ('a', 'FFFFFF', 55), (INK, 1.25), SHD)
    s.arrow([(1.0, 5.6), (7.5, 5.6)], INK, 1.5); s.arrow([(1.0, 5.6), (1.0, 1.4)], INK, 1.5)
    s.text(0.45, 1.5, 0.45, 4.0, 'Potencia (velocidad de ATP)', 12.5, F_HEAD, INK, True, 'c', 'm', txt_rot=270)
    s.text(4.3, 5.65, 3.2, 0.35, 'duración del esfuerzo →', 12.5, F_BODY, INK, False, 'r')
    s.group_end()
    c1 = s.free(1.05, 1.5, 6.4, 4.05, [('M 0 30 C 60 30 100 900 220 980 L 1000 990', False, True)], None, ('E74C3C', 4.0), name='Curva PCr')
    c2 = s.free(1.05, 1.5, 6.4, 4.05, [('M 0 600 C 100 250 180 200 300 300 C 450 450 600 900 1000 960', False, True)], None, ('F39C12', 4.0), name='Curva glucólisis')
    c3 = s.free(1.05, 1.5, 6.4, 4.05, [('M 0 950 C 200 750 350 600 500 560 C 700 520 850 540 1000 560', False, True)], None, ('1E8449', 4.0), name='Curva oxidativa')
    l1 = chip(s, 1.3, 1.3, 'ATP–PCr: segundos', 'F5B7B1', 12.5, name='Rótulo PCr')
    l2 = chip(s, 3.0, 2.35, 'Glucólisis rápida', 'FAD7A0', 12.5, name='Rótulo glucólisis')
    l3 = chip(s, 5.4, 3.4, 'Fosforilación oxidativa', MINT, 12.5, name='Rótulo oxidativa')
    k1 = card(s, 8.1, 1.1, 4.8, 2.3, '«Aeróbico» y «anaeróbico» describen **contribuciones relativas**, no compartimentos mutuamente excluyentes.', YEL, 14, head='Concepto')
    k2 = card(s, 8.1, 3.6, 4.8, 3.5, '- **Sprint**: ↑ lactato, AMP y productos de nucleótidos.\n- **Carrera prolongada**: ↑ extracción de AG y recambio de glucógeno.\n- **Entrenamiento**: ↑ densidad mitocondrial y enzimas oxidativas (**AMPK–PGC-1α**).', CREAM, 14, head='Aplicación')
    s.step(fade(g)); s.step(wipe(c1, 'l'), fade(l1, after=True)); s.step(wipe(c2, 'l'), fade(l2, after=True)); s.step(wipe(c3, 'l'), fade(l3, after=True))
    s.step(fade(k1)); s.step(fade(k2))
    s.note('ATP por vías: el sistema ATP–fosfocreatina permite segundos de gran potencia; la glucólisis rápida sostiene '
           'esfuerzos intensos cortos; la fosforilación oxidativa es menos rápida pero de alta capacidad. El gráfico es '
           'cualitativo (sin escala). "Aeróbico/anaeróbico" describen contribuciones relativas. Aplicación: un sprint aumenta '
           'lactato, AMP y productos de degradación de nucleótidos; una carrera prolongada incrementa la extracción de AG y el '
           'recambio de glucógeno; el entrenamiento aumenta la densidad mitocondrial y las enzimas oxidativas por señales como '
           'AMPK–PGC-1α.')


def build(D):
    div(D)
    t13a(D); t13_fed(D); t13_fast(D); t13_muscle(D); t13_ir(D)
    t14a(D); t14b(D); t14c(D)
