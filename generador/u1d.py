# -*- coding: utf-8 -*-
"""UNIDAD I — Tema 6: metabolismo posprandial tejido por tejido"""
from base import *

U = 1


def t6_hep(D):
    s = new(D, U, '6 · Hepatocito posprandial: rutas y enzimas')
    s.shape(0.3, 1.0, 9.0, 6.15, 'roundRect', ('a', 'F5CBA7', 60), ('A04000', 2.0), False, adj={'adj': 6000}, name='Hepatocito fondo')
    s.text(0.45, 6.75, 3, 0.3, 'HEPATOCITO (CITOSOL)', 12, F_HEAD, '7A3B12', True, 'l')
    gl = chain(s, 0.55, 1.15, ['Glucosa', 'Glucosa-6-P', 'Fructosa-6-P', 'Fructosa-1,6-bisP', 'Triosas fosfato', 'Fosfoenolpiruvato', 'Piruvato', 'Acetil-CoA'],
               dy=0.69, w=2.1, enzymes=['Glucocinasa', None, 'PFK-1', 'Aldolasa', 'varias etapas', 'Piruvato cinasa L', 'PDH (mitocondria)'],
               rev=[False, True, False, True, True, False, False], fill=[MOL['glc'][0] and LBLUE, YEL, YEL, YEL, YEL, YEL, YEL, ENE], name='Glucólisis', side='r', h=0.4)
    br1 = chain(s, 4.65, 1.84, ['Glc-1-P', 'UDP-glucosa', 'Glucógeno'], w=1.3, horizontal=True, dx=1.55, enzymes=[None, None, 'G. sintasa'], name='Glucogenogénesis', fill=[YEL, YEL, MINT])
    a_g = s.arrow([(2.67, 2.04), (4.63, 2.04)], INK, 2.0, head='triangle')
    ppp = chip(s, 4.65, 2.6, 'G6PDH → NADPH + ribosa-5-P', LILAC, 12, name='Vía pentosas')
    a_p = s.arrow([(2.67, 2.2), (4.6, 2.78)], INK, 2.0)
    li = chain(s, 4.65, 5.98, ['Citrato', 'Malonil-CoA', 'AG → TAG/VLDL'], w=1.3, horizontal=True, dx=1.55, enzymes=[None, 'ACC', 'FASN'],
               rev=[False, False], name='Lipogénesis', fill=[YEL, ENE, LSALMON])
    a_l = s.arrow([(2.67, 6.17), (4.63, 6.17)], INK, 3.0)
    regs = [('**Glucocinasa**', 'Km aparente alto; liberada de **GKRP** al subir glucosa'),
            ('**PFK-1**', 'activada por **F2,6BP** (alta con insulina)'),
            ('**PK-L**', 'activa **desfosforilada**'),
            ('**PDH**', 'activa desfosforilada; piruvato e insulina'),
            ('**G. sintasa**', 'activa por **desfosforilación**'),
            ('**G6PDH**', 'NADPH para biosíntesis')]
    rc = card(s, 9.55, 1.0, 3.35, 4.25, '\n'.join('- %s: %s' % r for r in regs), CREAM, 13, head='Interruptores', minsize=10.5)
    ob = note_box(s, 9.55, 5.45, 3.35, 1.7, '**Objetivo**: amortiguar la glucemia y canalizar carbonos hacia reserva y oxidación.', 13.5)
    chain_anim(s, gl, per_click=2)
    s.step(wipe(a_g, 'l'), *[e for (m, st) in br1 for e in ([wipe(st, 'l', after=True)] if st else []) + [fade(m, after=True)]])
    s.step(wipe(a_p, 'l'), fade(ppp, after=True))
    s.step(wipe(a_l, 'l'), *[e for (m, st) in li for e in ([wipe(st, 'l', after=True)] if st else []) + [fade(m, after=True)]])
    s.step(fade(rc))
    s.step(fade(ob))
    s.note('Hepatocito posprandial, tejido por tejido. GLUT2 bidireccional; glucocinasa de alta Km aparente regulada por GKRP '
           '(proteína reguladora que la secuestra en el núcleo en ayuno). Glucogenogénesis: G6P → G1P → UDP-glucosa → glucógeno '
           '(glucógeno sintasa activada por desfosforilación). Glucólisis: PFK-1 favorecida por fructosa-2,6-bisfosfato; '
           'piruvato cinasa L activa cuando está desfosforilada. Vía de las pentosas: la G6PDH genera NADPH para biosíntesis. '
           'PDH activa (desfosforilada) con alta disponibilidad de piruvato e insulina. El acetil-CoA mitocondrial sale como '
           'citrato y en el citosol alimenta ACC y FASN. Flechas gruesas de una punta = pasos irreversibles reguladores; '
           'flechas con dos puntas = pasos reversibles compartidos con la gluconeogénesis.')


def t6_adi(D):
    s = new(D, U, '6 · Adipocito posprandial: glucosa para el glicerol-3-P')
    adipocyte_white(s, 0.4, 1.15, 5.8, name='Adipocito grande')
    glu = glut(s, 0.25, 3.7, 0.7, text='GLUT4', color='1B4F72', horizontal=True)
    c = chain(s, 1.3, 2.3, ['Glucosa', 'G6P', 'DHAP', 'Glicerol-3-P'], dy=0.85, w=1.6, enzymes=[None, 'glucólisis', 'G3P DH'], rev=[False, True, True],
              fill=[LBLUE, YEL, YEL, ENE], name='Ruta adipocito')
    ag = chain(s, 3.65, 2.3, ['AG (desde LPL)', 'Acil-CoA'], dy=0.85, w=1.75, enzymes=['acil-CoA sintetasa'], rev=[False], fill=[YEL, ENE], name='Activación AG')
    tg = s.shape(2.6, 5.45, 2.4, 0.6, 'roundRect', shade('F4D03F', 0.4, 0.2), ('9A7D0A', 1.5), SHD, 'TAG (gota lipídica)', 14, F_HEAD, INK, True, 'c', 'm', name='TAG')
    a1 = s.arrow([(2.1, 5.27), (3.0, 5.43)], ACT, 3); a2 = s.arrow([(4.5, 3.6), (4.0, 5.43)], ACT, 3)
    k1 = card(s, 6.55, 1.1, 6.35, 1.75, 'El adipocito blanco posee **poca glicerol cinasa**: depende especialmente de la **glucosa** para el esqueleto de glicerol (también existe **gliceroneogénesis**).', YEL, 14, head='Clave')
    k2 = card(s, 6.55, 3.05, 6.35, 1.6, '- Glucólisis aporta ATP y **DHAP → glicerol-3-P**.\n- **Vía de las pentosas** aporta NADPH.', CREAM, 14, head='Rutas')
    k3 = card(s, 6.55, 4.85, 6.35, 2.25, '- **Insulina** favorece la síntesis de TAG y suprime **ATGL/HSL** (sistema de lipólisis).\n- Aumenta la **LPL** del lecho adiposo: capta AG de QM y VLDL.', LBLUE, 14, head='Regulación')
    s.step(fade(glu))
    chain_anim(s, c, per_click=4)
    chain_anim(s, ag, per_click=2)
    s.step(wipe(a1, 'l'), wipe(a2, 't'), zoom(tg, after=True))
    s.step(fade(k1)); s.step(fade(k2)); s.step(fade(k3))
    s.note('Adipocito posprandial: GLUT4 dependiente de insulina; glucólisis y conversión de DHAP en glicerol-3-fosfato por la '
           'glicerol-3-fosfato deshidrogenasa; vía de las pentosas para NADPH; reesterificación y acumulación de TAG. Como el '
           'adipocito blanco posee poca glicerol cinasa, depende especialmente de la glucosa para su esqueleto de glicerol, aunque '
           'también existe gliceroneogénesis (desde piruvato/lactato vía PEPCK, ampliación bibliográfica). La insulina favorece la '
           'síntesis de TAG y suprime HSL/ATGL mediante el control del sistema de lipólisis.')


def t6_rbc(D):
    s = new(D, U, '6 · Eritrocito: glucólisis anaerobia permanente')
    rbc(s, 0.3, 1.2, 5.6, name='Eritrocito grande')
    s.text(0.5, 6.6, 5, 0.4, 'Sin núcleo · sin mitocondrias', 15, F_HEAD, '7B1F17', True, 'c')
    g1 = glut(s, 0.1, 3.7, 0.7, text='GLUT1', color='5DADE2', horizontal=True)
    c = chain(s, 2.1, 1.75, ['Glucosa', 'G6P', '1,3-BPG', '3-fosfoglicerato', 'Piruvato', 'Lactato'], dy=0.78, w=1.9,
              enzymes=['hexocinasa', 'glucólisis', None, 'glucólisis', 'LDH'], rev=[False, True, True, False, True],
              fill=[LBLUE, YEL, YEL, YEL, YEL, lighten(MOL['lac'][0], 0.6)], name='Glucólisis eritrocito')
    rl = chip(s, 4.25, 3.42, '2,3-BPG', ENE, 13, name='23BPG')
    r1 = s.arrow([(4.03, 3.37), (4.4, 3.42)], '8E44AD', 2.0); r2 = s.arrow([(4.6, 3.84), (4.05, 4.12)], '8E44AD', 2.0)
    ppp = chip(s, 4.1, 2.15, 'G6PDH → NADPH', LILAC, 12.5, name='G6PDH eritrocito')
    rp = s.arrow([(4.03, 2.55), (4.25, 2.53)], INK, 2.0)
    k1 = card(s, 6.3, 1.1, 6.6, 1.55, '**LDH** reduce piruvato a lactato y **regenera NAD^{+}** para que la glucólisis continúe. Siempre libera **lactato**.', CREAM, 14, head='Lactato')
    k2 = card(s, 6.3, 2.85, 6.6, 1.5, '**PPP/G6PDH** provee **NADPH** para mantener el **glutatión reducido** (defensa antioxidante).', LILAC, 14, head='NADPH')
    k3 = card(s, 6.3, 4.55, 6.6, 1.35, 'Derivación de **Rapoport–Luebering**: 2,3-BPG a costa de ATP (modula la afinidad de la Hb por O_{2}).', YEL, 14, head='2,3-BPG')
    k4 = note_box(s, 6.3, 6.05, 6.6, 1.05, 'Poco dependiente de insulina: su demanda de glucosa **persiste en ayuno**. No oxida AG ni usa cuerpos cetónicos.', 13.5)
    s.step(fade(g1))
    chain_anim(s, c, per_click=3)
    s.step(fade(k1))
    s.step(wipe(rp, 'l'), fade(ppp, after=True), fade(k2))
    s.step(wipe(r1, 'l'), fade(rl, after=True), wipe(r2, 'l', after=True), fade(k3))
    s.step(fade(k4))
    s.note('Eritrocito: GLUT1, glucólisis anaerobia siempre, porque carece de mitocondrias; el piruvato se reduce a lactato por '
           'LDH para regenerar NAD+. La vía de las pentosas (G6PDH) provee NADPH para mantener el glutatión reducido. La '
           'derivación de Rapoport–Luebering produce 2,3-bisfosfoglicerato a costa de ATP (se saltea la fosfoglicerato cinasa). '
           'La glucólisis eritrocitaria es poco dependiente de insulina: su demanda persiste en ayuno y es la base del ciclo de '
           'Cori. El eritrocito no puede oxidar ácidos grasos ni utilizar cuerpos cetónicos.')


def t6_neu(D):
    s = new(D, U, '6 · Neurona: glucosa para gradientes iónicos y sinapsis')
    vessel(s, 0.3, 1.25, 6.2, 0.75, name='Capilar cerebral', rbcs=4)
    g1 = glut(s, 1.6, 2.0, 0.55, text='GLUT1 (barrera)', color='85C1E9')
    ne = neuron(s, 0.4, 2.9, 6.2, name='Neurona')
    g3 = glut(s, 3.25, 3.25, 0.5, text='GLUT3', color='2E86C1')
    gl = [mol(s, 1.7 + i * 0.5, 1.4, 'glc', d=0.36, name='Glc cerebro %d' % i) for i in range(2)]
    ck = [card(s, 6.8, 1.1, 6.1, 1.5, '**GLUT3** de gran afinidad: entrada **poco dependiente de insulina** (GLUT1 en la barrera hematoencefálica).', LBLUE, 14, head='Captación'),
          card(s, 6.8, 2.8, 6.1, 1.45, '**Glucólisis + oxidación mitocondrial** para sostener **gradientes iónicos**, sinapsis y reciclaje vesicular.', CREAM, 14, head='Uso'),
          card(s, 6.8, 4.45, 6.1, 1.25, '**HK1** inhibida por G6P coordina captación y uso. **PPP** aporta NADPH antioxidante.', YEL, 14, head='Control'),
          card(s, 6.8, 5.9, 6.1, 1.2, 'Sin β-oxidación significativa como combustible basal; los **cuerpos cetónicos** ganan peso en ayuno prolongado.', LSALMON, 14, head='Combustibles')]
    s.step(*[path(m, 0.05, 2.1, dur=1400, delay=i * 300) for i, m in enumerate(gl)])
    for c in ck:
        s.step(fade(c))
    s.note('Neurona: GLUT3 de gran afinidad y entrada poco dependiente de insulina; en la barrera hematoencefálica la glucosa '
           'atraviesa el endotelio por GLUT1. La glucólisis y la oxidación mitocondrial sostienen los gradientes iónicos (Na+/K+ '
           'ATPasa), la transmisión sináptica y el reciclaje vesicular. La vía de las pentosas aporta NADPH antioxidante. Las '
           'neuronas no realizan β-oxidación significativa como combustible basal; la utilización de cuerpos cetónicos aumenta en '
           'el ayuno prolongado. La hexocinasa 1, inhibida por G6P, coordina captación y uso.')


def t6_mus(D):
    s = new(D, U, '6 · Músculo: reposo alimentado frente a actividad')
    muscle_fiber(s, 0.4, 1.15, 6.0, 0.9, name='Fibra en reposo')
    muscle_fiber(s, 6.9, 1.15, 6.0, 0.9, name='Fibra en contracción', color='B03A2E')
    r = card(s, 0.4, 2.3, 6.0, 3.6, '- Captación por **GLUT4** (insulina).\n- **Hexocinasa II** → G6P.\n- **Glucogenogénesis** y oxidación de glucosa.\n- **PFK-1** modulada por AMP/ATP/citrato.\n- **PDH** activada por desfosforilación.\n- Puede seguir oxidando **lípidos** según disponibilidad.', CREAM, 14.5, head='Reposo alimentado')
    a = card(s, 6.9, 2.3, 6.0, 3.6, '- **Ca^{2+}**, **AMP** y señales de contracción facilitan **GLUT4**.\n- **Glucogenólisis** por fosforilasa cinasa (Ca^{2+}) y AMP.\n- El consumo de ATP exige mayor flujo **glucolítico y oxidativo**.\n- La elección de sustrato depende de **intensidad y duración**.', LSALMON, 14.5, head='En actividad')
    ic = [sign(s, 5.7, 1.4, '+'), sign(s, 12.2, 1.4, '+')]
    p = note_box(s, 0.4, 6.1, 12.5, 1.0, 'El músculo **no libera glucosa** a la sangre: usa su glucógeno localmente (sin glucosa-6-fosfatasa).', 15)
    s.step(fade(r)); s.step(fade(a)); s.step(fade(p))
    s.note('Músculo en reposo alimentado: GLUT4, glucogenogénesis y oxidación de glucosa; hexocinasa II, PFK-1 modulada por '
           'AMP/ATP/citrato, PDH activada por desfosforilación; también puede seguir oxidando lípidos según disponibilidad. En '
           'actividad: Ca2+, AMP y las señales de contracción facilitan la translocación de GLUT4 y la glucogenólisis (fosforilasa '
           'cinasa activada por Ca2+; fosforilasa b activada alostéricamente por AMP), mientras la alta demanda de ATP exige mayor '
           'flujo glucolítico y oxidativo. La elección de sustrato depende de la intensidad y la duración (tema 14).')


def t6_pearl(D):
    s = new(D, U, '6 · Perla comparativa: ¿quién puede devolver glucosa a la sangre?')
    items = [('Hígado', 'liver', True, 'Posee **glucosa-6-fosfatasa** (RE): libera glucosa por glucogenólisis y gluconeogénesis.'),
             ('Corteza renal', 'kidney', True, 'Gluconeogénesis con **G6Pasa**; relevante en ayuno prolongado.'),
             ('Músculo', 'muscle', False, 'Sin G6Pasa relevante: su G6P se usa **localmente**; exporta lactato y alanina.'),
             ('Adiposo', 'adipose', False, 'No libera glucosa: exporta **AG y glicerol**.'),
             ('Eritrocito', 'rbc', False, 'Siempre libera **lactato**; no produce cetonas ni oxida AG.')]
    ids = []
    for i, (t, k, ok, d) in enumerate(items):
        y = 1.1 + i * 1.2
        g = s.group_start('Perla ' + t)
        s.shape(0.4, y, 12.5, 1.05, 'rect', MINT if ok else LSALMON, (INK, 1.25), SHD)
        if k == 'liver':
            liver(s, 0.55, y + 0.12, 1.35)
        elif k == 'kidney':
            kidney(s, 0.85, y + 0.05, 0.65)
        elif k == 'muscle':
            muscle_fiber(s, 0.5, y + 0.3, 1.5, 0.42)
        elif k == 'adipose':
            adipocyte_white(s, 0.85, y + 0.08, 0.88)
        else:
            rbc(s, 0.85, y + 0.1, 0.85)
        s.text(2.25, y + 0.05, 2.2, 0.95, t, 18, F_HEAD, INK, True, 'l', 'm')
        s.shape(4.4, y + 0.22, 0.6, 0.6, 'ellipse', ACT if ok else INH, (WHITE, 1.5), False, '✓' if ok else '✗', 18, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
        s.text(5.25, y + 0.05, 7.5, 0.95, d, 15, F_BODY, INK, False, 'l', 'm')
        s.group_end(); ids.append(g)
    for g in ids:
        s.step(fade(g))
    s.note('Perla comparativa: el hígado puede devolver glucosa a la sangre gracias a la glucosa-6-fosfatasa del retículo '
           'endoplasmático (con el transportador G6PT); la corteza renal también la posee y su contribución aumenta en el ayuno '
           'prolongado. El músculo y el tejido adiposo no: el músculo usa su glucógeno localmente y el adiposo exporta AG y '
           'glicerol. El eritrocito siempre libera lactato y no puede producir cuerpos cetónicos ni oxidar ácidos grasos.')


def t6_table(D):
    s = new(D, U, '6 · Comparación tejido por tejido en el estado alimentado')
    rows = [['Tejido', 'Entrada de glucosa', 'Destino principal posprandial', 'Particularidad'],
            ['**Hígado**', 'GLUT2 + glucocinasa', 'Glucógeno, glucólisis, PPP, lipogénesis → VLDL', 'Amortigua la glucemia; G6Pasa (silenciada)'],
            ['**Músculo**', 'GLUT4 (insulina) + HK II', 'Glucógeno y oxidación', 'Gran sumidero periférico'],
            ['**Adiposo blanco**', 'GLUT4 (insulina)', 'Glicerol-3-P y TAG', 'Insulina suprime la lipólisis'],
            ['**Eritrocito**', 'GLUT1', 'Glucólisis → lactato; PPP; 2,3-BPG', 'Sin mitocondrias'],
            ['**Neurona**', 'GLUT3 (GLUT1 en BHE)', 'Glucólisis y oxidación', 'Sin β-oxidación significativa'],
            ['**Célula β**', 'GLUT1/3 (GLUT2) + glucocinasa', 'Metabolismo como **sensor**', 'K_{ATP}/Ca^{2+} → secreción']]
    t, H = table(s, 0.4, 1.15, 12.5, rows, [1.7, 2.7, 4.3, 3.8], size=15, rowh=0.68, name='Tabla tejidos alimentado')
    s.step(fade(t))
    s.note('Síntesis del estado alimentado tejido por tejido. Cada órgano capta la glucosa con un transportador diferente y la '
           'destina según su función: el hígado amortigua y almacena, el músculo es el gran sumidero periférico, el adiposo la usa '
           'para el esqueleto de glicerol, el eritrocito la convierte en lactato, la neurona la oxida y la célula β la usa como '
           'señal. Esta tabla sirve como repaso rápido antes de pasar al ayuno.')


def fed_map(D):
    s = new(D, U, 'Comparación órgano por órgano: estado alimentado', 'ALIMENTADO')
    data = [('intestine', 'INTESTINO', '- Absorbe glucosa y AA → **porta**\n- TAG → **QM** → linfa\n- Secreta GLP-1/GIP', LSALMON),
            ('pancreas', 'PÁNCREAS', '- β: **insulina ↑** (bifásica)\n- α: glucagón ↓ (salvo comida proteica)', LBLUE),
            ('liver', 'HÍGADO', '- Capta glucosa (GLUT2/GK)\n- **Glucógeno**, glucólisis, PPP\n- DNL → **VLDL** si sobra energía\n- ↓ producción de glucosa', MINT),
            ('muscle', 'MÚSCULO', '- **GLUT4** (insulina)\n- Glucógeno y oxidación\n- Síntesis proteica (mTORC1)', MINT),
            ('adipose', 'TEJIDO ADIPOSO', '- GLUT4 → glicerol-3-P\n- LPL capta AG de QM/VLDL\n- **↓ lipólisis** (PDE3B)', YEL),
            ('brain', 'CEREBRO', '- Glucosa (GLUT1/GLUT3)\n- Captación independiente de insulina', LILAC),
            ('rbc', 'ERITROCITO', '- GLUT1 → glucólisis\n- Exporta **lactato**', PINK),
            ('kidney', 'RIÑÓN', '- Excreta urea (dieta proteica)\n- Reabsorbe glucosa filtrada', LBLUE)]
    ids = organ_tiles(s, data)
    for g in ids:
        s.step(fade(g))
    s.note('Comparación órgano por órgano en el estado alimentado. Intestino: absorbe glucosa y aminoácidos hacia la porta y '
           'lípidos como quilomicrones hacia la linfa; secreta incretinas. Páncreas: insulina alta y glucagón bajo (una comida '
           'proteica puede elevar ambos). Hígado: capta glucosa por GLUT2/glucocinasa, sintetiza glucógeno, realiza glucólisis y '
           'vía de las pentosas, lipogénesis con exportación de VLDL si sobra energía, y suprime su producción de glucosa. Músculo: '
           'GLUT4, glucógeno, oxidación y síntesis proteica. Adiposo: glicerol-3-P, captación de AG vía LPL y supresión de la '
           'lipólisis. Cerebro y eritrocito: captación independiente de insulina. Riñón: excreta la urea del exceso proteico. '
           'Esta misma grilla se repetirá para el ayuno.')


def build(D):
    t6_hep(D); t6_adi(D); t6_rbc(D); t6_neu(D); t6_mus(D); t6_pearl(D); t6_table(D); fed_map(D)
