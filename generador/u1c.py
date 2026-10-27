# -*- coding: utf-8 -*-
"""UNIDAD I — Secuencia Morph 1 (señalización insulínica), GLUT, temas 5 y 6"""
from base import *

U = 1


def seqtxt(s, text, x=8.75, y=1.15, w=4.15, h=4.0, head=None):
    return card(s, x, y, w, h, text, CREAM, 15, name='!!Texto secuencia', head=head)


def m1_org(D):
    s = new(D, U, 'Señal de insulina: del organismo a la célula', 'SECUENCIA MORPH 1 · 1/6')
    human(s, 2.2, 0.95, 6.15, name='!!Organismo')
    brain(s, 3.53, 1.1, 0.55, name='!!Cerebro')
    heart(s, 3.95, 2.3, 0.35, name='!!Corazón')
    liver(s, 3.3, 2.75, 0.85, name='!!Hígado')
    pancreas(s, 3.95, 3.15, 0.55, name='!!Páncreas')
    intestine(s, 3.55, 3.4, 0.75, name='!!Intestino')
    muscle(s, 3.25, 4.5, 0.85, name='!!Músculo', fibers=2)
    adipocyte_white(s, 4.55, 3.85, 0.42, name='!!Adipocito')
    lb = [chip(s, 0.5, 2.85, 'Hígado', TAG, 12.5, name='Rótulo hígado'), chip(s, 5.6, 3.15, 'Páncreas', TAG, 12.5, name='Rótulo páncreas'),
          chip(s, 0.5, 4.55, 'Músculo', TAG, 12.5, name='Rótulo músculo'), chip(s, 5.6, 3.95, 'Adiposo', TAG, 12.5, name='Rótulo adiposo')]
    ls = [s.arrow([(1.45, 3.0), (3.35, 3.0)], INK, 1, tail=None), s.arrow([(5.6, 3.3), (4.5, 3.3)], INK, 1, tail=None),
          s.arrow([(1.45, 4.7), (3.3, 4.7)], INK, 1, tail=None), s.arrow([(5.6, 4.1), (4.95, 4.05)], INK, 1, tail=None)]
    ins = [mol(s, 4.15, 3.2, 'ins', d=0.3, name='Insulina %d' % i) for i in range(3)]
    t = seqtxt(s, '- La insulina se secreta a la **vena porta**: el **hígado** es el primer y principal blanco.\n- Luego alcanza la circulación sistémica: **músculo** y **tejido adiposo**.\n- Una misma señal produce respuestas **distintas en cada tejido**, según receptores, enzimas y transportadores.', head='Organismo')
    s.step(*[fade(x) for x in lb + ls])
    s.step(zoom(ins[0]), zoom(ins[1]), zoom(ins[2]), path(ins[0], -0.6, -0.15, after=True, dur=1000), path(ins[1], -0.65, 1.35, dur=1300),
           path(ins[2], 0.55, 0.75, dur=1200))
    s.step(fade(t))
    s.note('Secuencia Morph 1: organismo completo → hígado → hepatocito → membrana → receptor de insulina → señalización '
           'intracelular. Las seis diapositivas comparten nombres de objetos («!!») para que la transición Morph realice un '
           'acercamiento continuo. En esta escena la insulina sale del páncreas hacia la vena porta y el hígado, y luego hacia '
           'músculo y tejido adiposo. Mensaje: la misma hormona genera respuestas distintas en cada tejido.')


def m1_liver(D):
    s = new(D, U, 'Señal de insulina: el hígado como primer blanco', 'SECUENCIA MORPH 1 · 2/6', morph=True)
    human(s, -6.0, -3.0, 22.0, name='!!Organismo')
    liver(s, 0.5, 1.4, 7.6, name='!!Hígado')
    pancreas(s, 4.6, 5.65, 3.0, name='!!Páncreas')
    for i, (x, y) in enumerate(((5.2, 5.4), (5.9, 5.2), (6.5, 5.45))):
        mol(s, x, y, 'ins', d=0.4, name='!!Insulina portal %d' % i)
    t = seqtxt(s, '- La insulina portal alcanza concentraciones **mayores** que en sangre periférica.\n- Una fracción importante se **degrada en el hígado** en el primer paso.\n- Efectos hepáticos: ↓ producción de glucosa, ↑ glucógeno, ↑ lipogénesis.', head='Hígado')
    s.step(fade(t))
    s.note('Morph: la silueta se agranda hasta salir de la diapositiva y el hígado ocupa el centro. La sangre portal lleva '
           'insulina en concentraciones superiores a las periféricas, y una parte relevante se degrada en el primer paso '
           'hepático (ampliación bibliográfica). Por eso el hígado responde de manera especialmente sensible a la relación '
           'insulina/glucagón portal: reduce la producción endógena de glucosa, activa la síntesis de glucógeno y la lipogénesis.')


def m1_hep(D):
    s = new(D, U, 'Señal de insulina: el hepatocito', 'SECUENCIA MORPH 1 · 3/6', morph=True)
    liver(s, 0.35, 5.6, 2.2, name='!!Hígado')
    hepatocyte(s, 2.3, 1.05, 6.2, name='!!Hepatocito')
    for i, (x, y) in enumerate(((2.0, 1.4), (2.2, 2.1), (1.9, 2.8))):
        mol(s, x, y, 'ins', d=0.4, name='!!Insulina portal %d' % i)
    hl = s.shape(2.15, 1.15, 0.6, 4.3, 'ellipse', None, (INH, 3.0, 'dash'), False, name='Resalte membrana')
    t = seqtxt(s, '- La señal comienza en la **membrana plasmática** sinusoidal del hepatocito.\n- Allí se encuentra el **receptor de insulina**, una tirosina cinasa.\n- La respuesta intracelular combina **fosforilación** (minutos) y **transcripción** (horas).', head='Hepatocito')
    s.step(fade(hl), pulse(hl, after=True))
    s.step(fade(t))
    s.note('Morph: el hígado se reduce a un ícono y el hepatocito pasa al primer plano. La insulina llega a la cara sinusoidal '
           'del hepatocito (espacio de Disse). El resalte rojo señala la membrana donde se ubica el receptor, que se amplía en la '
           'diapositiva siguiente.')


def m1_mem(D):
    s = new(D, U, 'Señal de insulina: la membrana plasmática', 'SECUENCIA MORPH 1 · 4/6', morph=True)
    hepatocyte(s, -1.0, 2.75, 22.0, name='!!Hepatocito')
    membrane_h(s, 0.3, 2.6, 8.2, 0.45, name='!!Membrana')
    insulin_receptor(s, 3.6, 2.65, 0.45, 0.7, name='!!Receptor de insulina')
    for i, (x, y) in enumerate(((1.2, 1.2), (2.4, 1.0), (5.8, 1.3))):
        mol(s, x, y, 'ins', d=0.4, name='!!Insulina portal %d' % i)
    s.text(0.4, 1.0, 3, 0.3, 'ESPACIO DE DISSE', 13, F_HEAD, '7A3B12', True, 'l', name='!!Rótulo exterior')
    s.text(0.4, 6.65, 3, 0.3, 'CITOSOL', 13, F_HEAD, '7A3B12', True, 'l', name='!!Rótulo citosol')
    t = seqtxt(s, '- **Bicapa lipídica**: cabezas polares hacia el agua, colas hidrofóbicas al centro.\n- El receptor la **atraviesa**: dominio extracelular (α) que une insulina y dominio intracelular (β) con actividad **tirosina cinasa**.', head='Membrana')
    s.note('Morph: el hepatocito se amplía hasta que solo se ve su borde, donde aparece la membrana plasmática con el receptor '
           'de insulina. La bicapa separa el espacio de Disse (sangre sinusoidal) del citosol. El receptor es un tetrámero α2β2: '
           'las subunidades α son extracelulares y unen la hormona; las β atraviesan la membrana y contienen el dominio tirosina '
           'cinasa.')


def m1_rec(D):
    s = new(D, U, 'Receptor de insulina: activación', 'SECUENCIA MORPH 1 · 5/6', morph=True)
    membrane_h(s, 0.3, 3.2, 8.2, 0.45, name='!!Membrana')
    insulin_receptor(s, 3.05, 3.25, 0.45, 1.5, name='!!Receptor de insulina')
    ins = mol(s, 3.55, 1.0, 'ins', d=0.55, name='!!Insulina portal 0')
    for i, (x, y) in enumerate(((1.0, 1.1), (6.6, 1.3))):
        mol(s, x, y, 'ins', d=0.4, name='!!Insulina portal %d' % (i + 1))
    s.text(0.4, 1.0, 3, 0.3, 'ESPACIO DE DISSE', 13, F_HEAD, '7A3B12', True, 'l', name='!!Rótulo exterior')
    s.text(0.4, 6.65, 3, 0.3, 'CITOSOL', 13, F_HEAD, '7A3B12', True, 'l', name='!!Rótulo citosol')
    ps = [mol(s, x, y, 'atp', 'P', d=0.34, name='Fosfato %d' % i) for i, (x, y) in enumerate(((2.85, 4.55), (4.35, 4.6), (2.85, 5.25), (4.35, 5.3)))]
    irs = s.shape(4.9, 5.55, 1.3, 0.55, 'roundRect', shade('F5B041', 0.4, 0.2), ('9C640C', 1.25), SHD, 'IRS-1/2', 13, F_HEAD, INK, True, 'c', 'm', name='IRS')
    p2 = mol(s, 5.95, 5.4, 'atp', 'P', d=0.32, name='Fosfato IRS')
    t = seqtxt(s, '- La insulina se une a las subunidades **α**.\n- Cambio conformacional → **autofosforilación** en tirosinas de las subunidades **β**.\n- Las fosfotirosinas reclutan **IRS**, que también se fosforila y sirve de plataforma.', head='Receptor')
    s.step(path(ins, 0.05, 1.05, dur=1100), pulse(ins, after=True))
    s.step(*[zoom(p, after=(i == 0), delay=0) for i, p in enumerate(ps)])
    s.step(fade(irs), path(irs, -0.4, -0.25, after=True, dur=800), zoom(p2, after=True))
    s.note('La unión de la insulina a las subunidades α provoca un cambio conformacional que activa la tirosina cinasa de las '
           'subunidades β, que se transfosforilan (autofosforilación). Las fosfotirosinas sirven de sitio de anclaje para los '
           'sustratos del receptor de insulina (IRS-1/2), que también se fosforilan en tirosinas y actúan como plataforma de '
           'reclutamiento de proteínas con dominios SH2 (PI3K, Grb2). La animación muestra la llegada de la hormona, la aparición '
           'de los fosfatos y el acoplamiento de IRS.')


def m1_sig(D):
    s = new(D, U, 'Señalización intracelular de la insulina', 'SECUENCIA MORPH 1 · 6/6', morph=True)
    membrane_h(s, 0.3, 1.75, 12.7, 0.4, name='!!Membrana')
    insulin_receptor(s, 0.75, 1.78, 0.4, 0.75, name='!!Receptor de insulina')
    mol(s, 0.95, 0.75, 'ins', d=0.42, name='!!Insulina portal 0')
    irs = s.shape(1.95, 2.45, 1.2, 0.5, 'roundRect', shade('F5B041', 0.4, 0.2), ('9C640C', 1.25), SHD, 'IRS', 14, F_HEAD, INK, True, 'c', 'm', name='IRS')
    pi3 = s.shape(3.55, 2.45, 1.2, 0.5, 'roundRect', shade('85C1E9', 0.4, 0.2), ('1F618D', 1.25), SHD, 'PI3K', 14, F_HEAD, INK, True, 'c', 'm', name='PI3K')
    pip = chip(s, 3.45, 1.4, 'PIP_{2} → PIP_{3}', LILAC, 12.5, name='PIP3')
    pdk = s.shape(5.2, 2.45, 1.2, 0.5, 'roundRect', shade('BB8FCE', 0.4, 0.2), ('6C3483', 1.25), SHD, 'PDK1', 14, F_HEAD, INK, True, 'c', 'm', name='PDK1')
    akt = s.shape(6.85, 2.35, 1.5, 0.7, 'roundRect', shade('58D68D', 0.4, 0.25), ('1E8449', 1.5), SHD, 'Akt (PKB)', 16, F_HEAD, INK, True, 'c', 'm', name='Akt')
    a1 = s.arrow([(3.15, 2.7), (3.53, 2.7)], ACT, 2.5); a2 = s.arrow([(4.15, 2.45), (4.0, 1.85)], ACT, 2.5)
    a3 = s.arrow([(4.77, 2.7), (5.18, 2.7)], ACT, 2.5); a4 = s.arrow([(6.42, 2.7), (6.83, 2.7)], ACT, 2.5)
    targets = [('AS160 → **GLUT4** a membrana', 'Músculo y adiposo: ↑ captación', MINT, '+'),
               ('**GSK3** inhibida → glucógeno sintasa activa', '↑ glucogenogénesis', MINT, '+'),
               ('**FOXO1** fosforilado → sale del núcleo', '↓ PCK1 y G6PC', LSALMON, '−'),
               ('**PDE3B** → ↓ AMPc', '↓ PKA: ↓ lipólisis y glucogenólisis', LBLUE, '+'),
               ('**mTORC1** → síntesis proteica', '+ SREBP-1c: lipogénesis', YEL, '+')]
    tids = []
    for i, (t, e, f, sg) in enumerate(targets):
        x = 8.75; y = 2.3 + i * 0.98
        g = s.group_start('Blanco Akt %d' % i)
        s.arrow([(8.37, 2.7), (8.72, y + 0.42)], ACT, 2.0)
        card(s, x, y, 4.2, 0.88, '%s\n~~%s~~' % (t, e), f, 13, grow=False, minsize=10)
        s.group_end(); tids.append(g)
    mapk = card(s, 0.4, 3.55, 4.6, 1.6, '**Rama MAPK**: IRS/Shc → Grb2–SOS → Ras → Raf → MEK → **ERK** → expresión génica, crecimiento y proliferación.', LILAC, 13.5, head='Crecimiento')
    a5 = s.arrow([(2.5, 2.98), (2.5, 3.5)], '6C3483', 2.5)
    end = card(s, 0.4, 5.45, 7.95, 1.65, '**Escalas**: fosforilación de enzimas en **minutos** (GLUT4, GSK3, PDE3B); cambio de **transcripción** en **horas** (FOXO1, SREBP-1c). La señal se apaga por fosfatasas (PTEN, PTP1B) y degradación del complejo.', CREAM, 13.5)
    s.step(fade(irs), wipe(a1, 'l', after=True), fade(pi3, after=True))
    s.step(wipe(a2, 'b'), fade(pip, after=True), wipe(a3, 'l', after=True), fade(pdk, after=True), wipe(a4, 'l', after=True), zoom(akt, after=True))
    s.step(*[fade(g, after=(i > 0)) for i, g in enumerate(tids)])
    s.step(wipe(a5, 't'), fade(mapk, after=True))
    s.step(fade(end))
    s.note('Señalización intracelular: IRS fosforilado recluta la PI3K (clase IA), que convierte PIP2 en PIP3 en la cara interna '
           'de la membrana; PIP3 recluta PDK1 y Akt, y PDK1 (junto con mTORC2) activa Akt. Blancos de Akt: (1) AS160/TBC1D4 → '
           'translocación de GLUT4 en músculo y adiposo; (2) inhibición de GSK3 → glucógeno sintasa desfosforilada y activa; '
           '(3) fosforilación de FOXO1 → exclusión nuclear y menor transcripción de PCK1 (PEPCK) y G6PC; (4) activación de PDE3B → '
           'menor AMPc y menor actividad de PKA (antilipolítico en adipocito, antiglucogenolítico en hígado); (5) activación de '
           'mTORC1 → síntesis proteica y procesamiento de SREBP-1c. La rama Grb2–SOS–Ras–MAPK media efectos sobre crecimiento.\n'
           'La terminación de la señal (PTEN, PTP1B, fosforilación en serinas de IRS) es ampliación bibliográfica (Lehninger, '
           'Harper) y se relaciona con la resistencia a la insulina inducida por intermediarios lipídicos (tema 13).')


def glut_table(D):
    s = new(D, U, 'Esquema de transportadores de glucosa')
    rows = [['Transportador', 'Tejidos principales', 'Características', '¿Depende de insulina?'],
            ['**GLUT1**', 'Eritrocito, barrera hematoencefálica, astrocito, glándula mamaria', 'Captación basal de alta afinidad', 'No'],
            ['**GLUT2**', 'Hepatocito, enterocito (basolateral), túbulo renal; islote (roedor)', 'Baja afinidad, alta capacidad, **bidireccional**', 'No'],
            ['**GLUT3**', 'Neurona; célula β humana', 'Muy alta afinidad: entrada estable aun con glucemia baja', 'No'],
            ['**GLUT4**', 'Músculo esquelético y cardíaco, adipocito', 'Vesículas intracelulares que **translocan** a membrana', '**Sí** (y contracción)'],
            ['**GLUT5**', 'Enterocito (apical), otros', 'Transporta **fructosa**', 'No'],
            ['**SGLT1**', 'Enterocito (apical)', 'Cotransporte Na^{+}–glucosa (activo secundario)', 'No']]
    t, H = table(s, 0.4, 1.15, 9.1, rows, [1.5, 3.2, 3.0, 1.4], size=13.5, rowh=0.55, name='Tabla GLUT')
    membrane_v(s, 10.6, 1.15, 5.9, 0.42, name='Membrana esquema')
    gls = []
    for i, (lab, col, y) in enumerate((('GLUT1', '85C1E9', 1.4), ('GLUT2', '5DADE2', 2.6), ('GLUT3', '2E86C1', 3.8), ('GLUT4', '1B4F72', 5.0))):
        g = s.group_start('Ícono ' + lab)
        glut(s, 10.45, y, 0.72, text=None, color=col, horizontal=True)
        s.text(11.25, y + 0.05, 1.7, 0.4, lab, 14, F_HEAD, INK, True, 'l', 'm')
        mol(s, 9.75, y + 0.06, 'glc', d=0.4)
        s.group_end(); gls.append(g)
    k = note_box(s, 0.4, 1.3 + H + 0.1, 9.1, 0.95, 'Solo **GLUT4** convierte la señal de insulina en mayor captación. El hígado capta por **GLUT2** según la glucemia portal.', 14)
    s.step(fade(t))
    s.step(*[fade(g, after=(i > 0)) for i, g in enumerate(gls)])
    s.step(fade(k))
    s.note('Transportadores de glucosa por difusión facilitada (familia GLUT, SLC2A) y cotransportador SGLT1 (SLC5A1). '
           'En la célula β humana predominan GLUT1 y GLUT3, con participación posible de GLUT2 (en roedores, GLUT2 es el clásico). '
           'GLUT5 (fructosa) y la descripción de afinidades son ampliación bibliográfica (Lehninger, Harper). Clave fisiológica: '
           'la captación hepática, neuronal y eritrocitaria no depende de insulina; la muscular y adiposa sí (GLUT4), y la '
           'contracción muscular la estimula por vías independientes.')


# ------------------------------------------------------------------ TEMA 5
def t5a(D):
    s = new(D, U, '5 · Por qué la glucemia vuelve a la basal después de comer')
    g = s.group_start('Curva glucémica')
    s.shape(0.4, 1.15, 6.4, 4.0, 'rect', ('a', 'FFFFFF', 55), (INK, 1.25), SHD)
    s.arrow([(0.9, 4.65), (6.5, 4.65)], INK, 1.5); s.arrow([(0.9, 4.65), (0.9, 1.45)], INK, 1.5)
    s.text(0.45, 1.5, 0.4, 3.1, 'Glucemia', 12.5, F_HEAD, INK, True, 'c', 'm', txt_rot=270)
    s.text(4.5, 4.7, 2.1, 0.3, 'minutos tras comer', 12, F_BODY, INK, False, 'r')
    s.arrow([(0.95, 3.85), (6.4, 3.85)], '7F8C8D', 1.25, tail=None, dash='dash')
    s.text(5.2, 3.55, 1.3, 0.3, 'basal', 12, F_HEAD, '5D6D7E', True, 'r')
    s.group_end()
    cv = s.free(0.95, 1.7, 5.5, 2.15, [('M 0 1000 C 80 1000 120 100 220 60 C 330 20 420 450 560 800 C 680 1000 800 1000 1000 1000', False, True)], None, ('2E86C1', 4.0), name='Curva glucemia')
    lb = card(s, 2.2, 1.35, 3.1, 0.75, 'Ejemplo: pico ~30 min, basal ~2 h', LBLUE, 13, name='Ejemplo curva')
    eq = s.shape(0.4, 5.35, 6.4, 0.85, 'rect', TAG, (INK, 1.5), SHD, 'Δ glucemia = **Ra** (entrada) − **Rd** (desaparición)', 20, F_HEAD, INK, False, 'c', 'm', name='Ecuación balance')
    w = card(s, 0.4, 6.35, 6.4, 0.75, 'El patrón es un **ejemplo, no una ley**.', CREAM, 14)
    dep = card(s, 7.1, 1.15, 5.8, 2.6, '- Carga glucémica\n- Líquidos frente a sólidos\n- Incretinas y **vaciamiento gástrico**\n- **Sensibilidad** a la insulina', YEL, 15, head='La forma de la curva depende de')
    ra = card(s, 7.1, 3.95, 2.8, 3.15, '**Ra**:\n- absorción intestinal\n- producción **endógena** (hígado ± riñón)', LSALMON, 14.5, head='Entrada')
    rd = card(s, 10.1, 3.95, 2.8, 3.15, '**Rd**:\n- captación **muscular** y adiposa (insulina)\n- cerebro, eritrocitos (independiente)', LBLUE, 14.5, head='Desaparición')
    s.step(fade(g), wipe(cv, 'l', after=True, dur=1600), fade(lb, after=True))
    s.step(zoom(eq), fade(w, after=True))
    s.step(fade(ra), fade(rd, after=True))
    s.step(fade(dep))
    s.note('El patrón "pico a los 30 minutos y basal a las 2 horas" es un ejemplo, no una ley universal: depende de la carga '
           'glucémica, del estado físico (líquidos o sólidos), de las incretinas, de la sensibilidad a la insulina y del '
           'vaciamiento gástrico. El balance que determina la glucemia es la tasa de aparición (Ra: absorción intestinal + '
           'producción endógena) menos la tasa de desaparición (Rd: captación tisular). La curva dibujada es esquemática.')


def t5b(D):
    s = new(D, U, '5 · Intestino e islote: la respuesta inicial')
    intestine(s, 0.4, 1.2, 2.6, name='Intestino')
    pancreas(s, 3.4, 1.35, 3.0, name='Páncreas')
    islet(s, 4.4, 2.75, 1.6, name='Islote')
    a = arrow_lbl(s, [(2.9, 2.4), (4.4, 3.4)], 'GLP-1 · GIP', ACT, 3, lw=1.6, lx=2.8, ly=3.05)
    v = arrow_lbl(s, [(3.6, 1.0), (4.6, 2.75)], 'Vago (ACh)', ACT, 2.5, lw=1.5, lx=3.85, ly=1.0, dash='dash')
    items = [('Intestino', '**SGLT1** apical y **GLUT2** basolateral absorben glucosa; células L/K secretan **GLP-1/GIP**; activación **vagal**.', LSALMON),
             ('Célula β', 'Aumento **bifásico** de insulina.', LBLUE),
             ('Célula α', 'Ajusta (reduce) el **glucagón**.', PINK),
             ('Célula δ', 'Libera **somatostatina** (freno paracrino).', YEL),
             ('Resultado', 'La insulina **reduce la producción endógena** de glucosa y **facilita la captación** muscular y adiposa.', MINT)]
    ids = []
    for i, (h, t, f) in enumerate(items):
        g = card(s, 6.75, 1.1 + i * 1.2, 6.15, 1.08, '**%s**: %s' % (h, t), f, 14, name='Paso ' + h, anchor='m')
        ids.append(g)
    sm = card(s, 0.4, 4.75, 5.9, 2.35, 'El islote integra **nutrientes** (glucosa, aminoácidos), **hormonas intestinales** y **señales nerviosas**: la respuesta empieza antes de que la glucemia alcance su pico.', CREAM, 14.5)
    s.step(fade(ids[0]), wipe(a, 'l', after=True), wipe(v, 't'))
    for g in ids[1:]:
        s.step(fade(g))
    s.step(fade(sm))
    s.note('Intestino e islote: la glucosa se absorbe por SGLT1 (apical, cotransporte con Na+) y sale por GLUT2 basolateral. '
           'Las células enteroendocrinas L y K secretan GLP-1 y GIP, y hay activación vagal (fase cefálica e intestinal). La célula '
           'β responde con un aumento bifásico de insulina; las células α ajustan el glucagón y las δ liberan somatostatina. '
           'La insulina reduce la producción endógena de glucosa y facilita la captación muscular y adiposa.')


def t5c(D):
    s = new(D, U, '5 · Hígado: «cerrar la canilla» de glucosa')
    hepatocyte(s, 0.35, 1.1, 5.6, name='Hepatocito', detail=False)
    nu = s.shape(1.0, 1.75, 1.7, 1.3, 'ellipse', shade('7D5BA6', 0.45, 0.3), ('4A235A', 1.25), False, 'NÚCLEO', 13, F_HEAD, WHITE, True, 'c', 'm', name='Núcleo')
    ins = mol(s, 0.2, 4.6, 'ins', d=0.5, name='Insulina')
    akt = enz(s, 1.0, 4.65, 'Akt', name='Akt hígado')
    fox = s.shape(1.45, 2.2, 0.9, 0.42, 'roundRect', LSALMON, (INH, 1.5), False, 'FOXO1', 12, F_HEAD, INK, True, 'c', 'm', name='FOXO1 núcleo')
    gen = chip(s, 2.85, 1.9, '↓ PCK1 · ↓ G6PC', LSALMON, 12.5, name='Genes gluconeogénicos')
    pp = enz(s, 3.2, 3.4, 'PP1 (fosfatasa)', name='PP1')
    gs = chip(s, 3.2, 3.95, 'Glucógeno sintasa ↑', MINT, 12.5, name='GS activa')
    gp = chip(s, 3.2, 4.45, 'Fosforilasa ↓', LSALMON, 12.5, name='GP inactiva')
    f26 = chip(s, 1.4, 5.15, 'F2,6BP ↑', ENE, 13, name='F26BP')
    pf = chip(s, 2.75, 5.0, 'PFK-1 ↑ (glucólisis)', MINT, 12.5, name='PFK1')
    fb = chip(s, 2.75, 5.48, 'FBPasa-1 ↓ (GNG)', LSALMON, 12.5, name='FBPasa1')
    a1 = s.arrow([(0.7, 4.85), (1.0, 4.82)], ACT, 2.5)
    a2 = s.arrow([(1.35, 4.62), (1.85, 2.66)], ACT, 2.0)
    a3 = s.arrow([(1.75, 4.98), (1.75, 5.12)], ACT, 2.0)
    c = card(s, 6.3, 1.1, 6.6, 2.0, '**Transcripción**: Akt fosforila **FOXO1** → exclusión nuclear → ↓ **PCK1/PEPCK** y **G6PC** (horas).', CREAM, 14.5, head='1 · Genes')
    c2 = card(s, 6.3, 3.25, 6.6, 1.85, '**Glucógeno**: desfosforilación de glucógeno sintasa (activa) y fosforilasa (inactiva) → **glucogenogénesis** (minutos).', MINT, 14.5, head='2 · Glucógeno')
    c3 = card(s, 6.3, 5.25, 6.6, 1.85, '**F2,6BP** alta activa **PFK-1** e inhibe **FBPasa-1** → glucólisis. Se frenan gluconeogénesis y glucogenólisis.', YEL, 14.5, head='3 · Glucólisis')
    s.step(path(ins, 0.25, 0.0, dur=700), wipe(a1, 'l', after=True), fade(akt, after=True))
    s.step(wipe(a2, 't'), fade(fox, after=True), path(fox, 0.0, 1.0, after=True, dur=1000), out(fox, after=True), fade(gen), fade(c))
    s.step(fade(pp), fade(gs, after=True), fade(gp), fade(c2))
    s.step(wipe(a3, 't'), fade(f26, after=True), fade(pf, after=True), fade(fb), fade(c3))
    s.note('En el hígado la insulina "cierra la canilla" de glucosa endógena para no sumar glucosa propia a la absorbida. '
           '(1) Transcripción: Akt fosforila FOXO1, que sale del núcleo (la animación lo desplaza fuera), disminuyendo la '
           'transcripción de PCK1 (PEPCK) y G6PC (glucosa-6-fosfatasa). (2) Glucógeno: la activación de fosfatasas (PP1) '
           'desfosforila la glucógeno sintasa (activa) y la fosforilasa (inactiva). (3) Glucólisis: la caída de AMPc y la '
           'desfosforilación de la PFK-2/FBPasa-2 aumentan la fructosa-2,6-bisfosfato, que activa PFK-1 e inhibe FBPasa-1. '
           'Un defecto en la supresión hepática prolonga la hiperglucemia posprandial (resistencia hepática a la insulina).')


def t5d(D):
    s = new(D, U, '5 · Músculo y adiposo: «abrir el sumidero»')
    muscle(s, 0.4, 1.2, 5.6, name='Músculo', fibers=2)
    m = card(s, 0.4, 2.85, 5.9, 2.55, '- Capta gran parte de la carga periférica estimulada por insulina.\n- **GLUT4** transloca; **hexocinasa II** retiene glucosa como G6P.\n- **Glucógeno sintasa** almacena; **PDH** deriva piruvato a acetil-CoA.\n- La **contracción** facilita GLUT4 (AMPK, Ca^{2+}).', CREAM, 14, head='Músculo esquelético')
    adipocyte_white(s, 7.0, 1.05, 1.75, name='Adipocito')
    adipocyte_white(s, 8.6, 1.35, 1.4, name='Adipocito 2')
    a = card(s, 6.7, 3.25, 6.2, 2.15, '- **GLUT4** aporta glucosa para ATP y **glicerol-3-P** (desde DHAP) → reesterificación.\n- Insulina → **PDE3B** → ↓ AMPc/PKA → ↓ fosforilación de **perilipina/HSL** → ↓ lipólisis.\n- Favorece el depósito de TAG captados tras **LPL**.', CREAM, 14, head='Adiposo blanco')
    fl = flow(s, ['Insulina', 'PDE3B ↑', 'AMPc ↓', 'PKA ↓', 'HSL/perilipina ↓'], 10.15, 1.15, 2.75, 1.95, None, 11.5, 0.12, 'v', ACT, bold=True, shadow=False)
    p = note_box(s, 0.4, 5.65, 12.5, 1.45, 'Al **disminuir los AG plasmáticos** (antilipólisis) también **mejora la acción de la insulina** en músculo e hígado: el adipocito regula la sensibilidad de los demás tejidos.', 15)
    s.step(fade(m))
    s.step(fade(a))
    flow_anim(s, fl)
    s.step(fade(p))
    s.note('Tejidos periféricos ("abrir el sumidero"). Músculo: capta gran parte de la carga periférica de glucosa estimulada '
           'por insulina; GLUT4 transloca, la hexocinasa II retiene la glucosa como G6P, la glucógeno sintasa la almacena y la PDH '
           '(desfosforilada) deriva piruvato a acetil-CoA para oxidación. La contracción facilita GLUT4 por vías independientes de '
           'insulina (AMPK, Ca2+). Adiposo blanco: GLUT4 aporta glucosa para ATP y para glicerol-3-fosfato (desde DHAP), '
           'esqueleto necesario para reesterificar AG; la insulina reduce la lipólisis vía PDE3B (↓ AMPc, ↓ PKA, menor '
           'fosforilación de perilipina y HSL) y favorece el depósito de TAG tras la acción de LPL. Disminuir los AG plasmáticos '
           'facilita la acción de la insulina en otros tejidos.')


def t5e(D):
    s = new(D, U, '5 · Mecanismo integrador: canilla y sumidero')
    tk = tank(s, 5.2, 2.5, 2.6, 3.0, 0.5, name='Pool de glucosa plasmática')
    s.text(5.2, 5.55, 2.6, 0.35, 'GLUCOSA PLASMÁTICA', 13.5, F_HEAD, '1F4E79', True, 'c')
    lvl = s.shape(5.23, 3.0, 2.54, 1.0, 'rect', ('a', '2E86C1', 60), None, False, name='Nivel elevado')
    intestine(s, 0.4, 1.1, 1.8, name='Intestino')
    liver(s, 0.4, 3.6, 2.6, name='Hígado')
    muscle(s, 9.0, 1.3, 3.8, name='Músculo', fibers=2)
    adipocyte_white(s, 10.6, 3.9, 1.3, name='Adipocito')
    pc = pancreas(s, 5.0, 1.0, 2.9, name='Páncreas')
    f1 = s.arrow([(2.2, 1.9), (5.0, 2.7)], TRN, 9, name='Entrada intestinal')
    f2 = s.arrow([(3.05, 4.3), (5.0, 4.0)], TRN, 9, name='Producción hepática')
    f2b = s.arrow([(3.05, 4.3), (5.0, 4.0)], TRN, 2.5, name='Producción hepática reducida')
    o1 = s.arrow([(7.95, 3.6), (9.0, 2.4)], TRN, 9, name='Captación muscular')
    o2 = s.arrow([(7.95, 4.6), (10.5, 4.6)], TRN, 9, name='Captación adiposa')
    st = [('1', 'Absorción → glucemia ↑'), ('2', 'Islote responde: insulina ↑, glucagón ↓'), ('3', 'Hígado **cierra la canilla**'),
          ('4', 'Periferia **abre el sumidero**'), ('5', 'Retorno al rango basal')]
    ids = []
    for i, (n, t) in enumerate(st):
        g = s.group_start('Paso integrador ' + n)
        badge(s, 0.45 + i * 2.55, 6.25, n, 0.45)
        s.text(1.0 + i * 2.55, 6.15, 2.0, 0.7, t, 13, F_BODY, INK, False, 'l', 'm')
        s.group_end(); ids.append(g)
    fail = note_box(s, 9.0, 5.25, 3.9, 0.85, 'Falla hepática **o** periférica → hiperglucemia prolongada.', 13, name='Falla')
    s.step(fade(ids[0]), wipe(f1, 'l', after=True), fade(lvl, after=True))
    s.step(fade(ids[1]), pulse(pc, after=True))
    s.step(fade(ids[2]), out(f2, after=True), fade(f2b))
    s.step(fade(ids[3]), wipe(o1, 'l', after=True), wipe(o2, 'l'))
    s.step(fade(ids[4]), out(lvl, after=True, dur=1200))
    s.step(zoom(fail))
    s.note('Idea de mecanismo para exponer: la absorción eleva la glucemia → el islote responde (insulina ↑, glucagón ↓) → el '
           'hígado "cierra la canilla" (reduce la producción endógena) y los tejidos periféricos "abren el sumidero" (captación '
           'muscular y adiposa) → la glucemia vuelve al rango basal. La animación muestra el nivel del tanque subiendo con la '
           'entrada intestinal, la reducción del grosor de la flecha hepática (menor producción) y la apertura de las salidas. '
           'Un defecto en la supresión hepática o en la eliminación periférica prolonga la hiperglucemia (base de la '
           'intolerancia a la glucosa).')


def build(D):
    m1_org(D); m1_liver(D); m1_hep(D); m1_mem(D); m1_rec(D); m1_sig(D)
    glut_table(D)
    t5a(D); t5b(D); t5c(D); t5d(D); t5e(D)
