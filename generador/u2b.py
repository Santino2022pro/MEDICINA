# -*- coding: utf-8 -*-
"""UNIDAD II — temas 10–12: astrocito–neurona, hígado por fases (Morph), reservas (Morph 6)"""
from base import *

U = 2


def an_scene(s):
    vessel(s, 0.3, 1.05, 8.4, 0.7, name='Capilar cerebral', rbcs=5)
    astrocyte(s, 0.2, 2.0, 3.6, name='Astrocito')
    s.text(0.3, 2.0, 2.0, 0.35, 'ASTROCITO', 14, F_HEAD, '1E5631', True, 'l')
    neuron(s, 4.4, 3.2, 4.4, name='Neurona')
    s.text(6.2, 3.25, 2.2, 0.35, 'NEURONA', 14, F_HEAD, '4A235A', True, 'l')
    glycogen(s, 1.5, 3.9, 0.7, 0.55, 5, name='Glucógeno astrocitario')


def t10a(D):
    s = new(D, U, '10 · Acoplamiento astrocito–neurona: carbono y energía')
    an_scene(s)
    g1 = glut(s, 1.7, 1.75, 0.45, text=None, color='85C1E9'); s.text(2.2, 1.8, 0.8, 0.3, 'GLUT1', 11, F_HEAD, TRN, True, 'l')
    gl1 = mol(s, 1.75, 1.2, 'glc', d=0.38, name='Glucosa a astrocito')
    gl2 = mol(s, 5.6, 1.2, 'glc', d=0.38, name='Glucosa a neurona')
    a_n = s.arrow([(5.8, 1.75), (5.5, 3.8)], TRN, 3, name='Glucosa directa neurona')
    g3 = chip(s, 5.75, 2.55, 'GLUT3', LBLUE, 11.5, name='GLUT3')
    gly = s.arrow([(2.0, 2.4), (2.4, 4.6)], TRN, 2.5, name='Glucólisis astroglial')
    lac = mol(s, 2.5, 4.75, 'lac', d=0.42, name='Lactato astro')
    mct = chip(s, 2.9, 5.25, 'MCT1/4 → MCT2', LILAC, 11.5, name='MCT')
    a_l = s.arrow([(3.0, 5.0), (4.9, 4.75)], '8E44AD', 3.5, name='Lanzadera lactato')
    pyr = chip(s, 4.8, 5.5, 'LDH → piruvato → mitocondria', YEL, 11.5, name='Oxidación neuronal')
    c1 = card(s, 8.95, 1.1, 3.95, 2.55, '**Hipótesis de la lanzadera de lactato**: la actividad glutamatérgica estimula la glucólisis astroglial; el lactato sale por **MCT1/MCT4** y la neurona lo capta por **MCT2** y lo oxida.', CREAM, 13.5, head='Modelo')
    c2 = card(s, 8.95, 3.85, 3.95, 1.75, 'Los astrocitos tienen **pequeños depósitos de glucógeno** que alimentan la glucólisis local.', YEL, 13.5)
    c3 = note_box(s, 8.95, 5.8, 3.95, 1.3, 'Modelo **debatido**: la neurona **también capta y oxida glucosa** directamente.', 13.5)
    s.step(fade(gl1), path(gl1, 0.0, 0.85, after=True, dur=900), fade(g1))
    s.step(wipe(gly, 't'), zoom(lac, after=True), fade(c2))
    s.step(fade(mct), wipe(a_l, 'l', after=True), fade(pyr, after=True), fade(c1))
    s.step(fade(gl2), wipe(a_n, 't', after=True), fade(g3), fade(c3))
    s.note('Acoplamiento metabólico (flechas de carbono/energía, en azul y violeta). La glucosa sale de los capilares y entra a '
           'los astrocitos por GLUT1; las neuronas expresan GLUT3. Los astrocitos poseen pequeños depósitos de glucógeno. La '
           'hipótesis de la lanzadera de lactato astrocito–neurona propone que la mayor actividad glutamatérgica estimula la '
           'glucólisis astroglial, con producción de lactato que sale por MCT1/MCT4; la neurona lo capta por MCT2, la LDH lo '
           'convierte en piruvato y éste se oxida. Es un modelo relevante pero debatido: las neuronas también captan y oxidan '
           'glucosa directamente, y el sentido y la magnitud del flujo de lactato dependen del estado, la región y la actividad.')


def t10b(D):
    s = new(D, U, '10 · Ciclo glutamato–glutamina: nitrógeno y neurotransmisión')
    an_scene(s)
    syn = s.shape(3.6, 4.0, 1.0, 1.0, 'ellipse', ('a', 'FFFFFF', 40), ('7F8C8D', 1.0, 'dash'), False, name='Hendidura')
    glu = mol(s, 4.85, 4.3, 'aa', 'Glu', d=0.42, name='Glutamato liberado')
    ea = chip(s, 2.5, 3.55, 'EAAT1/EAAT2 + Na^{+}', LBLUE, 11.5, name='EAAT')
    a1 = s.arrow([(4.8, 4.5), (3.4, 3.95)], NIT, 3, name='Recaptación')
    gs = enz(s, 0.5, 4.75, 'Glutamina sintetasa', name='GS astro')
    nh = mol(s, 0.45, 5.35, 'nh4', d=0.4, name='NH4 astro'); at = mol(s, 0.95, 5.4, 'atp', 'ATP', d=0.34, w=0.55, name='ATP GS')
    gln = mol(s, 2.3, 5.4, 'gln', d=0.45, name='Glutamina astro')
    a2 = s.arrow([(2.8, 5.65), (5.2, 5.5)], NIT, 3.5, name='Glutamina a neurona')
    gla = enz(s, 5.0, 6.05, 'Glutaminasa (activada por fosfato)', name='Glutaminasa')
    gad = chip(s, 6.2, 6.6, 'GAD (PLP): Glu → GABA', LILAC, 11.5, name='GAD')
    nk = chip(s, 0.4, 6.3, 'Na^{+}/K^{+} ATPasa: costo indirecto', ENE, 11, name='NaK')
    c1 = card(s, 8.95, 1.1, 3.95, 3.4, '- La neurona libera **glutamato**.\n- **EAAT1/EAAT2** astrogliales lo captan con **Na^{+}** (gasto indirecto de ATP).\n- **GS**: glutamato + NH_{4}^{+} + ATP → **glutamina**.\n- La neurona la reconvierte con **glutaminasa**.', CREAM, 13.5, head='Ciclo')
    c2 = card(s, 8.95, 4.7, 3.95, 2.4, 'Previene **excitotoxicidad** y **recicla** neurotransmisores (glutamato y GABA).', MINT, 14, head='Función')
    s.step(fade(syn), zoom(glu, after=True))
    s.step(wipe(a1, 'r'), fade(ea, after=True), fade(nk))
    s.step(fade(gs), fade(nh), fade(at), zoom(gln, after=True))
    s.step(wipe(a2, 'l'), fade(gla, after=True), fade(gad, after=True))
    s.step(fade(c1)); s.step(fade(c2))
    s.note('Flechas de nitrógeno/neurotransmisor (verde azulado), distintas de las de carbono para no confundirlas. La neurona '
           'libera glutamato; los transportadores astrogliales EAAT1/EAAT2 lo captan junto con Na+, con un gasto indirecto de ATP '
           'por la Na+/K+ ATPasa. La glutamina sintetasa astroglial cataliza glutamato + NH4+ + ATP → glutamina, que se exporta a '
           'la neurona, donde la glutaminasa activada por fosfato la reconvierte en glutamato. En terminales GABAérgicas, el '
           'glutamato se descarboxila a GABA por la glutamato descarboxilasa (dependiente de PLP). La vía previene la '
           'excitotoxicidad y recicla neurotransmisores.')


def t10c(D):
    s = new(D, U, '10 · Amonio y astrocito: de la protección a la encefalopatía')
    astrocyte(s, 0.3, 1.3, 3.4, name='Astrocito normal')
    astrocyte(s, 4.4, 1.0, 4.0, name='Astrocito tumefacto', color='C5E1A5')
    s.text(0.4, 4.1, 3.2, 0.35, 'Normal: atrapa NH_{4}^{+} en glutamina', 13, F_HEAD, '1E5631', True, 'c')
    s.text(4.6, 4.3, 3.8, 0.35, 'Hiperamonemia: glutamina ↑↑', 13, F_HEAD, INH, True, 'c')
    nhs = [mol(s, 4.9 + (i % 4) * 0.7, 4.75 + (i // 4) * 0.5, 'nh4', d=0.4, name='NH4 exceso %d' % i) for i in range(8)]
    ar = s.arrow([(3.7, 2.6), (4.4, 2.6)], INH, 4)
    seq = flow(s, ['NH_{4}^{+} ↑ (falla hepática, derivación portosistémica)', 'Glutamina astroglial ↑', 'Estrés osmótico y mitocondrial', 'Disfunción de neurotransmisión → encefalopatía'],
               8.85, 1.1, 4.05, 6.0, [LSALMON, YEL, PINK, RED], 13.5, 0.3, 'v', INH)
    p = card(s, 0.3, 5.9, 8.2, 1.2, 'El SNC requiere **aporte continuo de glucosa o cetonas** y un control fino del equilibrio excitación–inhibición.', CREAM, 14)
    s.step(wipe(ar, 'l'), *[zoom(n, after=(i == 0)) for i, n in enumerate(nhs)])
    flow_anim(s, seq)
    s.step(fade(p))
    s.note('Los astrocitos atrapan NH4+ en glutamina, algo protector en condiciones normales. Con hiperamonemia severa '
           '(insuficiencia hepática, derivación portosistémica, defectos del ciclo de la urea) la acumulación de glutamina '
           'astroglial puede favorecer estrés osmótico (tumefacción) y mitocondrial y contribuir a la encefalopatía. No todos los '
           'síntomas se explican solo por la concentración plasmática de amonio: intervienen inflamación y otros factores '
           '(Unidad V). El SNC requiere aporte continuo de glucosa o cetonas.')


# ------------------------------------------------------------------ TEMA 11 — tablero hepático (Morph)
NODES = [('ggn', 'Glucogenogénesis', 0.75, 1.55), ('ggl', 'Glucogenólisis', 3.15, 1.55), ('glc', 'Glucólisis', 0.75, 2.6),
         ('gng', 'Gluconeogénesis', 3.15, 2.6), ('ppp', 'Vía de las pentosas', 5.55, 1.55), ('lip', 'Lipogénesis (ACC/FASN)', 0.75, 3.65),
         ('box', 'β-oxidación', 3.15, 3.65), ('cet', 'Cetogénesis', 5.55, 3.65), ('vldl', 'Síntesis TAG / VLDL', 0.75, 4.7),
         ('urea', 'Ureogénesis', 3.15, 4.7), ('prot', 'Síntesis proteica', 5.55, 2.6)]
LV = {0: ('E5E7E9', '95A5A6', INK, False), 1: ('D5F5E3', '7DCEA0', INK, False), 2: ('82E0AA', '1E8449', INK, True), 3: ('1E8449', '0B5345', WHITE, True)}


def board(D, n, ttl, states, text, glc_out, cc_out, gin, genes):
    s = new(D, U, '11 · Hígado: %s' % ttl, 'TABLERO HEPÁTICO · %d/4' % n, morph=(n > 1))
    s.shape(0.3, 1.05, 7.95, 5.0, 'roundRect', ('a', 'F5CBA7', 70), ('A04000', 2.5), SHD, name='!!Tablero hepatocito', adj={'adj': 8000})
    s.text(0.45, 1.1, 4, 0.35, 'HEPATOCITO', 13, F_HEAD, '7A3B12', True, 'l', name='!!Rótulo hepatocito')
    for k, t, x, y in NODES:
        lv = states.get(k, 0)
        f, l, c, b = LV[lv]
        s.shape(x, y, 2.25, 0.8, 'roundRect', f, (l, 2.5 if lv >= 2 else 1.25), SHD if lv >= 2 else False, t, 14, F_HEAD, c, b, 'c', 'm',
                name='!!Nodo ' + k, adj={'adj': 20000}, fit=True, minsize=11)
    # exportaciones
    s.arrow([(8.3, 2.0), (9.6, 2.0)], TRN, max(glc_out, 0.5) * 3 + 0.5, name='!!Flecha glucosa')
    mol(s, 9.7, 1.75, 'glc', d=0.5, name='!!Ficha glucosa')
    s.arrow([(9.6, 2.9), (8.3, 2.9)], TRN, max(gin, 0.5) * 3 + 0.5, name='!!Flecha entrada glucosa')
    s.text(9.65, 2.7, 1.8, 0.4, 'captación', 12, F_HEAD, TRN, True, 'l', name='!!Rótulo captación')
    s.arrow([(8.3, 3.95), (9.6, 3.95)], 'C2185B', max(cc_out, 0.5) * 3 + 0.5, name='!!Flecha cetonas')
    mol(s, 9.7, 3.7, 'cc', d=0.5, name='!!Ficha cetonas')
    s.text(10.3, 1.8, 1.2, 0.4, 'glucosa', 12, F_HEAD, TRN, True, 'l', name='!!Rótulo glucosa')
    s.text(10.3, 3.75, 1.2, 0.4, 'cetonas', 12, F_HEAD, 'C2185B', True, 'l', name='!!Rótulo cetonas')
    lg = s.group_start('!!Leyenda niveles')
    for i, t in enumerate(['inactiva', 'baja', 'activa', 'máxima']):
        f, l, c, b = LV[i]
        s.shape(0.45 + i * 1.95, 6.2, 0.35, 0.3, 'roundRect', f, (l, 1.25), False, name='Nivel %d' % i)
        s.text(0.85 + i * 1.95, 6.15, 1.5, 0.4, t, 12, F_BODY, INK, False, 'l', 'm')
    s.group_end()
    card(s, 8.6, 4.55, 4.3, 2.55, text, CREAM, 13.5, name='!!Texto fase hígado')
    card(s, 0.3, 6.6, 7.95, 0.5, genes, YEL, 12.5, name='!!Eje génico', grow=False)
    clock(s, 11.9, 1.2, 0.95, {1: 1, 2: 8, 3: 12, 4: 12}[n], name='!!Reloj hígado')
    s.note(text.replace('**', '').replace('\n', ' '))
    return s


def t11(D):
    s1 = board(D, 1, 'saciedad', {'ggn': 3, 'glc': 3, 'ppp': 2, 'lip': 2, 'vldl': 2, 'prot': 2, 'urea': 2, 'box': 1, 'gng': 0, 'ggl': 0, 'cet': 0},
               '**Saciedad**: glucólisis (PFK-1, PK-L), glucogenogénesis, PPP, ACC/FASN, TAG/VLDL, síntesis proteica y **ureogénesis tras comidas proteicas**. Citrato → ATP-citrato liasa → acetil-CoA citosólico.',
               0, 0, 3, 'Eje: insulina → Akt → FOXO1 fuera del núcleo · ChREBP y SREBP-1c ↑')
    s1.note('Tablero hepático: los mismos nodos se recolorean en cada fase y la transición Morph anima el cambio. Saciedad: '
            'aumentan glucólisis (PFK-1, piruvato cinasa L), glucogenogénesis, vía de las pentosas, síntesis de AG (ACC/FASN), '
            'síntesis de TAG/VLDL según disponibilidad, síntesis proteica y ureogénesis tras comidas proteicas. El acetil-CoA '
            'procede de la glucosa y otros sustratos; el citrato sale al citosol y la ATP-citrato liasa produce acetil-CoA. El NADPH '
            'procede de la vía de las pentosas, la enzima málica y otras fuentes.')
    s2 = board(D, 2, 'ayuno temprano (≈4–12 h)', {'ggl': 3, 'gng': 2, 'glc': 1, 'box': 2, 'cet': 1, 'vldl': 1, 'urea': 1, 'prot': 1, 'ppp': 1, 'lip': 0, 'ggn': 0},
               '**Ayuno temprano**: la glucogenólisis domina; PKA fosforila **PFK-2/FBPasa-2** → ↓ F2,6BP → ↓ glucólisis, ↑ gluconeogénesis. ↓ ACC/malonil-CoA → **CPT1 liberada**.',
               2, 1, 0.5, 'Eje: glucagón → PKA (efectos covalentes rápidos) · insulina en descenso')
    s3 = board(D, 3, 'ayuno de 12–48 h', {'gng': 3, 'box': 3, 'cet': 2, 'urea': 3, 'ggl': 1, 'vldl': 1, 'ppp': 1, 'prot': 1, 'glc': 0, 'lip': 0, 'ggn': 0},
               '**12–48 h**: se intensifican gluconeogénesis, β-oxidación y cetogénesis; el glucógeno cae. AA y glicerol aportan carbonos; la **urea suele aumentar**.',
               3, 2, 0.5, 'Eje: CREB/CRTC2 + FOXO1 nuclear → PCK1, G6PC · PPARα → oxidación y cetogénesis')
    s4 = board(D, 4, 'ayuno prolongado (>3 días)', {'gng': 2, 'box': 3, 'cet': 3, 'urea': 1, 'ggl': 0, 'vldl': 1, 'ppp': 1, 'prot': 1, 'glc': 0, 'lip': 0, 'ggn': 0},
               '**>3 días**: cetogénesis sostenida; el SNC requiere menos glucosa; cambia el sustrato gluconeogénico y el **riñón colabora más**. La ureogénesis **puede disminuir** respecto del pico temprano.',
               2, 3, 0.5, 'Los cambios son graduales: no hay un «interruptor» temporal')
    s3.note('12–48 h: se intensifican gluconeogénesis, β-oxidación y cetogénesis mientras el glucógeno hepático disminuye. '
            'Aminoácidos y glicerol aportan carbonos; la urea suele aumentar al crecer el flujo aminoacídico. La transcripción '
            'inducida por CREB/CRTC2 y FOXO1 facilita el programa gluconeogénico, aunque no explica sola las tasas de producción. '
            'PPARα se asocia a la expresión de genes de oxidación de AG y cetogénesis.')
    s4.note('>3 días: cetogénesis sostenida e importante utilización periférica de cetonas; se requiere menos glucosa para el '
            'SNC, parte de la gluconeogénesis cambia de sustrato y el riñón colabora más. La ureogénesis puede disminuir respecto '
            'del pico temprano por ahorro de proteínas: no afirmar que sube indefinidamente. Los cambios de concentraciones y '
            'flujos son graduales, no un interruptor temporal.')


# ------------------------------------------------------------------ TEMA 12 — reservas (Morph 6)
def reserves(D, n, ttl, gly, tag, prot, ket, text, glyc_txt):
    s = new(D, U, '12 · Reservas y combustibles: %s' % ttl, 'SECUENCIA MORPH 6 · %d/4' % n, morph=(n > 1))
    rows = [('liver', 'Glucógeno hepático', gly, '8E44AD'), ('adipose', 'TAG del tejido adiposo', tag, 'D4AC0D'), ('muscle', 'Proteína muscular', prot, 'C0392B')]
    for i, (k, t, v, col) in enumerate(rows):
        y = 1.2 + i * 1.45
        organ_icon(s, k, 0.4, y - 0.05, 1.1)
        s.text(1.7, y - 0.05, 4.5, 0.4, t, 15, F_HEAD, INK, True, 'l', 'm', name='!!Rótulo reserva %d' % i)
        s.shape(1.7, y + 0.42, 5.2, 0.5, 'rect', ('a', 'FFFFFF', 60), (INK, 1.25), False, name='!!Fondo barra %d' % i)
        s.shape(1.72, y + 0.44, max(5.16 * v, 0.05), 0.46, 'rect', ('lin', [(0, lighten(col, 0.3)), (100, col)], 0), None, False, name='!!Barra reserva %d' % i)
    # cerebro
    brain(s, 7.3, 1.05, 1.7, name='!!Cerebro fase')
    s.text(9.15, 1.1, 3.8, 0.4, 'Combustible cerebral', 15, F_HEAD, INK, True, 'l', name='!!Rótulo cerebro')
    s.shape(9.15, 1.6, 3.75 * (1 - ket), 0.55, 'rect', shade(MOL['glc'][0], 0.3, 0.1), (INK, 1.0), False, 'Glucosa' if ket < 0.8 else '', 12, F_HEAD, WHITE, True, 'c', 'm', name='!!Cerebro glucosa', fit=False)
    s.shape(9.15 + 3.75 * (1 - ket), 1.6, max(3.75 * ket, 0.02), 0.55, 'rect', shade(MOL['cc'][0], 0.3, 0.1), (INK, 1.0), False, 'Cetonas' if ket > 0.25 else '', 12, F_HEAD, WHITE, True, 'c', 'm', name='!!Cerebro cetonas', fit=False)
    s.text(9.15, 2.2, 3.8, 0.35, 'proporciones esquemáticas', 11, F_BODY, '5D6D7E', False, 'l', name='!!Nota esquema')
    card(s, 7.3, 2.95, 5.6, 3.15, text, CREAM, 14, name='!!Texto reservas')
    s.shape(0.4, 5.6, 6.5, 0.5, 'rect', LBLUE, (INK, 1.0), False, glyc_txt, 13.5, F_HEAD, INK, True, 'c', 'm', name='!!Glucemia fase')
    s.shape(0.4, 6.3, 12.5, 0.8, 'rect', TAG, (INK, 1.5), SHD, ttl.upper(), 22, F_HEAD, INK, True, 'c', 'm', name='!!Fase actual')
    return s


def t12(D):
    s1 = reserves(D, 1, 'estado alimentado', 1.0, 1.0, 1.0, 0.0,
                  '- Glucógeno hepático **repleto**.\n- Lípidos dietarios hacia el **adiposo**.\n- Balance proteico **anabólico**.\n- El cerebro usa **glucosa**.', 'Glucemia: posprandial, regulada por insulina')
    s1.note('Secuencia Morph 6 (adaptación al ayuno): estado alimentado → 8–12 h → 24–48 h → ayuno prolongado. Las barras de '
            'reserva y el combustible cerebral cambian de longitud y la transición Morph anima la evolución. Las longitudes son '
            'esquemáticas y relativas: no representan mediciones.')
    s2 = reserves(D, 2, '8–12 h', 0.6, 0.99, 1.0, 0.03,
                  '- Glucógeno **todavía relevante pero menor**; gluconeogénesis **ya activa**.\n- Lipólisis **moderada**.\n- Músculo y corazón: mezcla de AG, glucosa y lactato.\n- Cerebro: mayormente glucosa; eritrocito: solo glucosa.', 'Glucemia generalmente estable')
    s2.note('8–12 h: glucógeno hepático todavía relevante pero menor, gluconeogénesis ya activa, lipólisis moderada; glucemia '
            'generalmente estable. Músculo y corazón usan una mezcla variable de AG, glucosa y lactato. El cerebro usa mayormente '
            'glucosa; los eritrocitos, solo glucosa.')
    s3 = reserves(D, 3, '24–48 h', 0.15, 0.95, 0.96, 0.22,
                  '- **Marcada caída** del glucógeno hepático: gluconeogénesis **indispensable**.\n- ↑ AG plasmáticos y **cuerpos cetónicos**.\n- Balance nitrogenado puede tornarse **muy negativo**.\n- El hígado exporta glucosa y cetonas, **no usa sus cetonas**.\n- El **glicerol** aporta carbonos sin pérdida muscular.', 'Glucemia sostenida por gluconeogénesis')
    s3.note('24–48 h: marcada caída de la reserva hepática; la gluconeogénesis es indispensable; aumentan los AG plasmáticos y '
            'los cuerpos cetónicos; el balance nitrogenado puede tornarse muy negativo si no hay ingesta. El hígado exporta glucosa '
            'y cetonas pero no puede consumir sus propias cetonas. El glicerol aporta carbonos glucogénicos sin requerir pérdida '
            'muscular.')
    s4 = reserves(D, 4, 'ayuno prolongado (>3 días)', 0.05, 0.85, 0.93, 0.6,
                  '- **Ascenso progresivo** del consumo cerebral de cetonas.\n- **Menor dependencia de aminoácidos**: ↓ excreción de N tras la fase inicial.\n- Corazón y músculo usan AG abundantemente.\n- Se **reduce el gasto energético** (adaptación hormonal).', 'Glucemia algo menor pero estable')
    s4.note('>3 días: ascenso progresivo del consumo cerebral de cetonas, menor dependencia de aminoácidos y descenso relativo de '
            'la excreción de nitrógeno tras la fase inicial. Corazón y músculo pueden utilizar AG abundantemente; la utilización '
            'muscular de cetonas no permanece necesariamente máxima (se reserva para el cerebro). Se reduce el gasto energético '
            'por adaptación hormonal (↓ T3, ↓ actividad simpática) y cambios de masa libre de grasa.')


def fuel_chart(D):
    s = new(D, U, '12 · Selección de combustibles cerebrales (esquema conceptual)')
    cats = ['Alimentado', '12 h', '24 h', '48 h', '3 d', '5 d', '2–3 sem']
    ch = chart_line(s, 0.4, 1.1, 7.6, 6.0, cats, [('Glucosa', [100, 99, 95, 85, 72, 55, 35]), ('Cuerpos cetónicos', [0, 1, 5, 15, 28, 45, 65])],
                    [MOL['glc'][0], MOL['cc'][0]], ytitle='Proporción relativa del combustible cerebral', stacked_area=True, name='Gráfico combustible cerebral', size=13, ymax=100)
    k1 = card(s, 8.3, 1.1, 4.6, 2.2, 'Los cuerpos cetónicos **reemplazan progresivamente** a la glucosa en el cerebro; la necesidad de glucosa **no desaparece**.', CREAM, 14, head='Lectura')
    k2 = card(s, 8.3, 3.5, 4.6, 1.75, 'Menos glucosa requerida → menos **proteína** degradada para gluconeogénesis.', MINT, 14, head='Ahorro proteico')
    k3 = card(s, 8.3, 5.45, 4.6, 1.65, 'Eritrocitos y médula renal **siguen** dependiendo de la glucólisis.', LSALMON, 14, head='Glucosa obligatoria')
    s.step(fade(ch)); s.step(fade(k1)); s.step(fade(k2)); s.step(fade(k3))
    s.note('Gráfico conceptual (áreas apiladas, proporciones relativas sin valores medidos): a medida que se prolonga el ayuno, '
           'los cuerpos cetónicos aportan una fracción creciente de la energía cerebral. Clásicamente, tras semanas de ayuno '
           'pueden cubrir alrededor de dos tercios (ampliación bibliográfica: estudios de Cahill; Lehninger cap. 23). La '
           'necesidad de glucosa no desaparece: eritrocitos, médula renal y parte del metabolismo cerebral la requieren. El '
           'beneficio es el ahorro proteico.')


def ketosis_vs_dka(D):
    s = new(D, U, '12 · Alerta conceptual: cetosis fisiológica frente a cetoacidosis')
    l = card(s, 0.4, 1.1, 6.1, 4.6, '- Insulina **baja pero presente** (insulina residual).\n- La insulina **limita** la lipólisis y la cetogénesis.\n- Producción ≈ **utilización** de cetonas.\n- pH generalmente **conservado**.\n- Glucemia normal o algo baja.', MINT, 15, head='Cetosis fisiológica del ayuno', headfill=ACT)
    r = card(s, 6.8, 1.1, 6.1, 4.6, '- **Insulinopenia funcional marcada** + hormonas contrarreguladoras.\n- Lipólisis y cetogénesis **sin freno**.\n- Producción **excede** utilización, depuración y tampones.\n- **Acidosis** de anion gap elevado, deshidratación, alteraciones electrolíticas.\n- Hiperglucemia frecuente (existe forma **euglucémica**).', LSALMON, 15, head='Cetoacidosis diabética', headfill=INH)
    m = note_box(s, 0.4, 5.9, 12.5, 1.2, 'Ayuno **no es sinónimo** de cetosis patológica. La medición de **β-hidroxibutirato** en sangre interpreta mejor la cetoacidosis que las tiras urinarias de acetoacetato.', 14.5)
    s.step(fade(l)); s.step(fade(r)); s.step(fade(m))
    s.note('Alerta conceptual: el ayuno no es sinónimo de cetosis patológica. En ayuno existe insulina residual que limita la '
           'lipólisis y la cetogénesis. La cetoacidosis diabética aparece por insulinopenia funcional marcada y hormonas '
           'contrarreguladoras, con hiperglucemia frecuente y acidosis de anion gap elevado; existe cetoacidosis euglucémica en '
           'situaciones específicas (por ejemplo, con inhibidores de SGLT2, embarazo o ayuno con alcohol; ampliación clínica). '
           'El β-hidroxibutirato sanguíneo es mejor marcador que las tiras urinarias de acetoacetato.')


def central_table(D):
    s = new(D, U, 'Cuadro central: cómo cambian las vías según el estado')
    rows = [['Vía / tejido', 'Alimentación', 'Ayuno 8–12 h', 'Ayuno 24–48 h', 'Ayuno >3 días'],
            ['**Glucosa hepática**', 'Captación + glucógeno + glucólisis', 'Glucogenólisis + GNG', 'GNG dominante; poco glucógeno', 'GNG sostenida + aporte renal'],
            ['**Lipólisis adiposa**', 'Inhibida por insulina', 'Aumenta', 'Alta', 'Alta mientras haya reservas'],
            ['**β-oxidación hepática**', 'Menor si malonil-CoA alto', 'Aumenta', 'Alta', 'Alta'],
            ['**Cetogénesis**', 'Baja', 'Leve aumento', 'Aumento marcado', 'Alta y sostenida'],
            ['**Proteólisis muscular**', 'Balance más anabólico', 'Intermedia', 'Puede aumentar para GNG', 'Ahorro relativo tras adaptación cetónica'],
            ['**Uso cerebral de cetonas**', 'Mínimo', 'Muy bajo', 'Crece', 'Sustancial'],
            ['**Urea por proteólisis**', 'Depende de proteínas comidas', 'Componente endógeno', 'Puede aumentar', 'Disminuye respecto del pico']]
    t, H = table(s, 0.4, 1.1, 12.5, rows, [2.5, 2.6, 2.3, 2.5, 2.6], size=15, rowh=0.7, name='Cuadro central')
    n = s.text(0.4, 1.2 + H, 12.5, 0.4, 'GNG = gluconeogénesis. La tabla sintetiza **tendencias**, no promedios obligatorios.', 12.5, F_BODY, '5D4037', False, 'l')
    s.step(fade(t))
    s.note('Cuadro central de cambios por estado. Lectura por filas: cada vía cambia gradualmente. Puntos finos: la cetogénesis '
           'es baja en alimentación y aumenta de forma marcada recién a las 24–48 h; la proteólisis muscular puede aumentar para la '
           'gluconeogénesis al inicio y luego se ahorra; la urea por proteólisis disminuye respecto del pico de adaptación. Son '
           'tendencias, no valores obligatorios.')


def fast_tiles(D):
    s = new(D, U, 'Comparación órgano por órgano: ayuno', 'AYUNO')
    data = [('intestine', 'INTESTINO', '- Sin aporte de glucosa\n- Usa **glutamina** como combustible', LSALMON),
            ('pancreas', 'PÁNCREAS', '- Insulina **baja** (no nula)\n- **Glucagón** relativo ↑', LBLUE),
            ('liver', 'HÍGADO', '- Glucogenólisis → **GNG**\n- β-oxidación → **cetogénesis**\n- Ureogénesis', MINT),
            ('muscle', 'MÚSCULO', '- Usa **AG** (y cetonas)\n- Exporta **alanina, glutamina, lactato**\n- Sin G6Pasa', MINT),
            ('adipose', 'TEJIDO ADIPOSO', '- **Lipólisis**: AG + glicerol\n- Glicerol → hígado/riñón', YEL),
            ('brain', 'CEREBRO', '- Glucosa → **cetonas** crecientes\n- Ahorro proteico', LILAC),
            ('rbc', 'ERITROCITO', '- **Siempre glucosa**\n- Lactato → Cori', PINK),
            ('kidney', 'RIÑÓN', '- **GNG cortical** creciente\n- **Amoniogénesis** (glutamina)', LBLUE)]
    ids = organ_tiles(s, data)
    for g in ids:
        s.step(fade(g))
    s.note('Comparación órgano por órgano en el ayuno, con la misma grilla que el estado alimentado para facilitar el contraste. '
           'Intestino: sin aporte de glucosa, usa glutamina. Páncreas: insulina baja pero presente, glucagón relativo alto. '
           'Hígado: glucogenólisis y luego gluconeogénesis, β-oxidación, cetogénesis y ureogénesis. Músculo: usa AG y exporta '
           'alanina, glutamina y lactato. Adiposo: lipólisis. Cerebro: glucosa y cada vez más cetonas. Eritrocito: siempre glucosa. '
           'Riñón: gluconeogénesis cortical y amoniogénesis crecientes.')


def build(D):
    t10a(D); t10b(D); t10c(D)
    t11(D)
    t12(D); fuel_chart(D); ketosis_vs_dka(D)
    central_table(D); fast_tiles(D)
