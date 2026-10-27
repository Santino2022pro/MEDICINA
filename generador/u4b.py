# -*- coding: utf-8 -*-
"""UNIDAD IV — temas 31 a 35"""
from base import *

U = 4


def t31a(D):
    s = new(D, U, '31 · Adenilato cinasa y AMP desaminasa en el ejercicio intenso')
    muscle_fiber(s, 0.4, 1.15, 12.5, 0.7, name='Fibra en sprint', color='B03A2E')
    r1 = s.shape(0.4, 2.15, 6.0, 0.9, 'rect', CREAM, (INK, 1.25), SHD, '**Adenilato cinasa** (mioquinasa): 2 ADP ⇌ ATP + AMP', 16, F_HEAD, INK, False, 'c', 'm', name='Reacción AK')
    r2 = s.shape(0.4, 3.25, 6.0, 0.9, 'rect', LBLUE, (INK, 1.25), SHD, '**AMP desaminasa (AMPD1)**: AMP + H_{2}O → IMP + NH_{3}', 16, F_HEAD, INK, False, 'c', 'm', name='Reacción AMPD')
    sg = card(s, 0.4, 4.35, 6.0, 1.45, 'El **AMP** acumulado señaliza déficit: activa **AMPK** y **PFK-1**.', YEL, 14.5)
    pn = card(s, 0.4, 6.0, 6.0, 1.1, 'Al **remover AMP**, AMPD empuja la adenilato cinasa hacia **más ATP**.', MINT, 14)
    # ciclo de nucleótidos de purina
    cyc = s.group_start('Ciclo de nucleótidos de purina')
    s.shape(7.0, 2.15, 5.9, 4.95, 'rect', ('a', 'FFFFFF', 45), (INK, 1.25), SHD)
    s.text(7.1, 2.2, 5.7, 0.4, 'CICLO DE NUCLEÓTIDOS DE PURINA', 15, F_HEAD, INK, True, 'c', 'm')
    s.shape(8.2, 2.8, 3.5, 3.4, 'ellipse', None, (ACT, 3.0), False)
    for t, x, y, f in (('AMP', 9.4, 2.55, ENE), ('IMP', 11.15, 4.25, YEL), ('Adenilosuccinato', 8.95, 5.95, YEL)):
        s.shape(x, y, 1.0 if t != 'Adenilosuccinato' else 2.0, 0.5, 'roundRect', f, (INK, 1.25), SHD, t, 13, F_HEAD, INK, True, 'c', 'm')
    s.text(11.3, 3.3, 1.5, 0.7, '→ NH_{3}', 14, F_HEAD, NIT, True, 'l', 'm')
    s.text(7.1, 4.3, 1.4, 0.6, '+ Asp\n+ GTP', 13, F_HEAD, '1E8449', True, 'r', 'm')
    s.text(7.1, 3.0, 1.2, 0.6, 'Fumarato\n→ Krebs', 13, F_HEAD, 'C55A11', True, 'r', 'm')
    s.group_end()
    s.step(fade(r1)); s.step(fade(r2)); s.step(fade(sg)); s.step(fade(pn)); s.step(fade(cyc))
    s.note('Adenilato cinasa (mioquinasa): 2 ADP ⇌ ATP + AMP. En ejercicio de máxima intensidad, la caída de ATP y el aumento de '
           'ADP impulsan generación adicional inmediata de ATP; el AMP acumulado señaliza el déficit energético activando AMPK y '
           'PFK-1. La AMP desaminasa (AMPD1 en músculo) cataliza AMP + H2O → IMP + NH3; al remover AMP favorece '
           'termodinámicamente la continuación de la reacción de adenilato cinasa y controla el pool de adenilatos. Participa en '
           'el ciclo de nucleótidos de purina: IMP + aspartato (+ GTP) → adenilosuccinato → AMP + fumarato, con producción de '
           'fumarato (anaplerosis) y eliminación de nitrógeno.')


def t31b(D):
    s = new(D, U, '31 · Costo adaptativo: del IMP al ácido úrico')
    c = chain(s, 0.5, 1.15, ['ATP → ADP → AMP', 'IMP', 'Inosina', 'Hipoxantina', 'Xantina', 'Ácido úrico'], dy=0.95, w=3.0,
              enzymes=['AMPD1', None, None, 'xantina oxidorreductasa', 'xantina oxidorreductasa'], rev=[False] * 5,
              fill=[ENE, YEL, YEL, YEL, YEL, lighten(MOL['urate'][0], 0.5)], name='Degradación purinas', h=0.55, size=14.5)
    k1 = card(s, 4.6, 1.1, 8.3, 1.9, 'Si el IMP se degrada continuamente → **pérdida de nucleótidos** de purina y riesgo de **hiperuricemia transitoria**. El esfuerzo intenso puede elevar **hipoxantina** y **lactato**.', CREAM, 14.5, head='Costo')
    k2 = card(s, 4.6, 3.2, 8.3, 1.5, 'El **lactato** puede **competir** con la excreción renal de urato en determinadas condiciones.', LSALMON, 14.5, head='Riñón')
    k3 = card(s, 4.6, 4.9, 8.3, 2.2, '**Déficit de AMPD1**: intolerancia al ejercicio, calambres **o asintomático**; relación genotipo–fenotipo heterogénea. **No** es el mismo mecanismo que los defectos de oxidación de AG o las glucogenosis musculares.', YEL, 14, head='Clínica')
    chain_anim(s, c, per_click=2)
    s.step(fade(k1)); s.step(fade(k2)); s.step(fade(k3))
    s.note('Costo adaptativo: al descender el AMP total se modifica la señal metabólica; si hay degradación continua de IMP a '
           'inosina, hipoxantina, xantina y ácido úrico, aumenta la pérdida de nucleótidos purínicos y el riesgo de hiperuricemia '
           'transitoria. Durante el esfuerzo intenso la degradación de ATP puede elevar hipoxantina y lactato; el lactato puede '
           'competir con la excreción renal de urato. El déficit de AMPD1 puede asociarse a intolerancia al ejercicio y calambres '
           'o ser asintomático.')


# ------------------------------------------------------------------ TEMA 32
def t32a(D):
    s = new(D, U, '32 · Tejido adiposo blanco frente a marrón: histología')
    adipocyte_white(s, 0.6, 1.2, 3.2, name='Adipocito blanco')
    adipocyte_brown(s, 7.1, 1.2, 3.2, name='Adipocito marrón')
    w = card(s, 0.4, 4.6, 6.1, 2.5, '- Adipocito grande **unilocular**: una gota de TAG.\n- Núcleo desplazado a la **periferia**.\n- Menor densidad mitocondrial por volumen.\n- Estroma con células inmunes y fibroblastos.', YEL, 14, head='Blanco (WAT)')
    b = card(s, 6.8, 4.6, 6.1, 2.5, '- **Multilocular**, con **numerosas mitocondrias** (citocromos: color).\n- Rica **irrigación e inervación simpática**.\n- **UCP1** (termogenina) en la membrana mitocondrial interna.', LSALMON, 14, head='Marrón (BAT)')
    l1 = chip(s, 4.0, 2.3, 'una gota', CREAM, 13, name='Rótulo una gota'); l2 = chip(s, 10.5, 2.3, 'muchas gotas + mitocondrias', CREAM, 13, name='Rótulo muchas')
    s.step(fade(l1), fade(w)); s.step(fade(l2), fade(b))
    s.note('Tejido adiposo blanco: adipocito grande unilocular, una gota predominante de TAG, núcleo desplazado a la periferia, '
           'menor densidad mitocondrial por volumen, vascularización y matriz con células inmunes y fibroblastos. Tejido adiposo '
           'marrón: adipocitos multiloculares, numerosas mitocondrias ricas en citocromos (color), rica irrigación e inervación '
           'simpática; contiene UCP1 (termogenina) en la membrana mitocondrial interna.')


def t32b(D):
    s = new(D, U, '32 · Termogénesis: UCP1 disipa el gradiente como calor', 'RUTA ANIMADA')
    s.shape(0.3, 1.05, 8.4, 1.3, 'rect', ('a', 'F5B7B1', 45), None, False, name='Espacio intermembrana')
    s.text(0.4, 1.08, 4, 0.3, 'ESPACIO INTERMEMBRANA', 12.5, F_HEAD, '922B21', True, 'l')
    membrane_h(s, 0.3, 2.4, 8.4, 0.6, name='Membrana interna', head='E59866', tail='FDEBD0')
    s.shape(0.3, 3.05, 8.4, 2.5, 'rect', ('a', 'F8C471', 55), None, False, name='Matriz')
    etc = s.shape(0.8, 2.05, 1.8, 1.3, 'roundRect', shade('A569BD', 0.35, 0.25), (INK, 1.5), SHD, 'Cadena\nrespiratoria', 13, F_HEAD, WHITE, True, 'c', 'm', name='Cadena')
    syn = s.shape(3.4, 2.05, 1.3, 1.3, 'roundRect', shade('58D68D', 0.35, 0.25), (INK, 1.5), SHD, 'ATP\nsintasa', 13, F_HEAD, INK, True, 'c', 'm', name='ATP sintasa')
    ucp = s.shape(5.8, 2.05, 1.3, 1.3, 'roundRect', shade('E74C3C', 0.35, 0.25), (INK, 1.5), SHD, 'UCP1', 16, F_HEAD, WHITE, True, 'c', 'm', name='UCP1')
    h1 = s.arrow([(1.7, 2.05), (1.7, 1.4)], INH, 3.5); hh = [mol(s, 2.0 + i * 0.4, 1.4, 'ca', 'H^{+}', d=0.35, name='H %d' % i) for i in range(3)]
    hl = s.arrow([(6.45, 1.45), (6.45, 3.9)], INH, 4.5, name='Fuga H+')
    fl = flame(s, 6.15, 4.0, 0.7, name='Calor')
    sm = s.arrow([(4.05, 1.45), (4.05, 3.6)], INH, 1.5, dash='dash', name='Menor ATP')
    sig = flow(s, ['Frío', 'Noradrenalina (simpático)', 'Receptor β-adrenérgico', 'AMPc → PKA', 'Lipólisis → AG activan UCP1'], 9.0, 1.1, 3.9, 6.0,
               [LBLUE, LSALMON, LSALMON, ENE, YEL], 13.5, 0.2, 'v', ACT)
    k = card(s, 0.3, 5.75, 8.4, 1.35, 'UCP1 permite el **retorno de protones sin producir ATP**: la energía del gradiente se disipa como **calor**. **T3** favorece la maquinaria termogénica; pueden surgir adipocitos **beige** en depósitos blancos.', CREAM, 13.5)
    flow_anim(s, sig)
    s.step(fade(etc), wipe(h1, 'b', after=True), *[zoom(x, after=(i == 0)) for i, x in enumerate(hh)])
    s.step(fade(syn), wipe(sm, 't', after=True))
    s.step(pulse(ucp), wipe(hl, 't', after=True), zoom(fl, after=True), pulse(fl, after=True))
    s.step(fade(k))
    s.note('Termogénesis en el tejido adiposo marrón: el frío activa el simpático; la noradrenalina actúa sobre receptores '
           'β-adrenérgicos → AMPc/PKA → lipólisis; los AG liberados activan UCP1 y además son combustible. La cadena respiratoria '
           'bombea protones; la UCP1 permite su retorno a la matriz sin pasar por la ATP sintasa, de modo que la energía del '
           'gradiente se disipa como calor (animación: fuga de protones y llama). T3 favorece la maquinaria termogénica; pueden '
           'emerger adipocitos beige en determinados depósitos blancos según estímulos.')


def t32c(D):
    s = new(D, U, '32 · El tejido adiposo blanco como órgano endocrino')
    adipose_tissue(s, 4.5, 2.2, 4.3, name='Tejido adiposo central')
    ad = [('Leptina', 'informa el **tamaño de las reservas** al hipotálamo y otros tejidos', 0.4, 1.1, MINT),
          ('Adiponectina', 'mejora sensibilidad insulínica y oxidación; **inversa** a la adiposidad visceral', 0.4, 3.1, MINT),
          ('Resistina', 'papel humano **distinto** al murino', 0.4, 5.1, LSALMON),
          ('TNF-α · IL-6', 'inflamación: alteran **IRS/PI3K/Akt**, lipólisis y endotelio', 9.0, 1.1, LSALMON),
          ('PAI-1 · angiotensinógeno', 'trombosis y presión arterial', 9.0, 3.1, LSALMON),
          ('Fuente celular', 'adipocito **o** células inmunes del estroma', 9.0, 5.1, CREAM)]
    ids = []
    for t, d, x, y, f in ad:
        ids.append(card(s, x, y, 3.9, 1.8, '**%s**: %s' % (t, d), f, 14, anchor='m', name='Adipocina ' + t))
    vc = chip(s, 4.6, 1.15, 'Visceral ≠ subcutáneo', TAG, 14, name='Visceral')
    lp = note_box(s, 4.45, 5.75, 4.3, 1.35, '**Lipodistrofia**: diabetes e hipertrigliceridemia severas con **poca grasa**.', 13)
    for g in ids:
        s.step(fade(g))
    s.step(fade(vc)); s.step(fade(lp))
    s.note('El tejido adiposo blanco almacena AG como TAG, libera AG y glicerol, amortigua el desbordamiento de lípidos hacia otros '
           'órganos, aísla y protege, y secreta hormonas y citocinas: leptina (tamaño aproximado de las reservas), adiponectina '
           '(mejora la sensibilidad insulínica y la oxidación; generalmente inversa a la adiposidad visceral), resistina (papel '
           'humano diferente al murino), TNF-α, IL-6, PAI-1, angiotensinógeno y múltiples adipocinas, cuya fuente puede ser el '
           'adipocito o las células inmunes estromales. Visceral y subcutáneo se comportan distinto. La pérdida de capacidad de '
           'expansión sana favorece el almacenamiento ectópico; la lipodistrofia produce diabetes e hipertrigliceridemia severas '
           'a pesar de la poca grasa corporal.')


# ------------------------------------------------------------------ TEMA 33
def t33a(D):
    s = new(D, U, '33 · Balance energético: ingreso, gasto y regulación')
    g = s.group_start('Balanza energética')
    s.shape(5.9, 5.3, 1.5, 1.4, 'triangle', shade('A04000', 0.3, 0.2), (INK, 1.5), SHD)
    s.shape(1.4, 5.0, 10.5, 0.2, 'rect', '6E2C00', (INK, 1.0), False)
    s.group_end()
    ing = card(s, 0.4, 1.1, 5.9, 3.7, '- Disponibilidad y elección\n- Hambre y saciedad\n- Digestión, absorción y biodisponibilidad\n- Factores **hipotalámicos**, **hedónicos** y **sociales**', LSALMON, 15, head='Ingreso de energía')
    gas = card(s, 7.0, 1.1, 5.9, 3.7, '- Metabolismo **basal/reposo**\n- Actividad física **voluntaria e involuntaria**\n- **Efecto térmico** de la alimentación\n- **Termogénesis adaptativa**', LBLUE, 15, head='Gasto de energía')
    k = note_box(s, 0.4, 6.1, 12.5, 1.0, 'El peso cambia si ingreso y gasto **divergen sostenidamente**, y el cuerpo **modifica ambos** con la propia variación de peso.', 15)
    s.step(fade(g)); s.step(fade(ing)); s.step(fade(gas)); s.step(fade(k))
    s.note('Entrada de energía: disponibilidad, elección, comportamiento alimentario, hambre, saciedad, digestión, absorción y '
           'biodisponibilidad; factores hipotalámicos, hedónicos y sociales interactúan. Gasto: metabolismo basal/reposo, '
           'actividad física voluntaria e involuntaria, efecto térmico de la alimentación y termogénesis adaptativa. El peso '
           'cambia si la ingesta absorbida y el gasto divergen sostenidamente; el cuerpo modifica ambos con la propia variación de '
           'peso.')


def t33b(D):
    s = new(D, U, '33 · Órganos y señales del balance energético')
    data = [('brain', 'HIPOTÁLAMO Y TRONCO', 'Integran leptina, insulina, PYY, GLP-1, CCK, grelina, vagales y nutrientes', LILAC),
            ('intestine', 'INTESTINO', 'Absorción, incretinas, saciedad', LSALMON),
            ('pancreas', 'PÁNCREAS', 'Insulina/glucagón ajustan sustratos', LBLUE),
            ('liver', 'HÍGADO', 'Distribuye combustibles; señales metabólicas y neurales', MINT),
            ('adipose', 'ADIPOSO', 'Almacena; envía leptina, adiponectina, AG', YEL),
            ('muscle', 'MÚSCULO', 'Reservorio proteico; gran consumidor en actividad', LSALMON),
            ('adrenal', 'TIROIDES', 'Modula el gasto basal (T3)', CREAM),
            ('kidney', 'RIÑÓN', 'Agua, nitrógeno, glucosa y ácido–base', LBLUE)]
    ids = organ_tiles(s, data, th=2.0, size=13.5, icon=0.8)
    k = card(s, 0.4, 5.4, 12.5, 1.7, '**Control dinámico**: al reducirse las reservas ↓ leptina y a menudo ↓ T3 y actividad simpática, ↑ impulso alimentario y ↓ gasto relativo → **se opone** al descenso sostenido de peso. Con sobrealimentación ↑ la termogénesis en grado variable, sin compensar siempre el exceso. **El peso es resultado de redes, no de una sola hormona.**', YEL, 14)
    for g in ids:
        s.step(fade(g))
    s.step(fade(k))
    s.note('Hipotálamo y tronco encefálico integran señales de leptina, insulina, PYY, GLP-1, CCK, grelina, vagales y nutrientes. '
           'Intestino: absorción, incretinas y saciedad; páncreas: insulina/glucagón; hígado: distribuye combustibles e informa '
           'por señales metabólicas y neuronales; adiposo: almacena y envía leptina, adiponectina y AG; músculo: principal '
           'reservorio de proteínas y gran consumidor de energía durante la actividad; tiroides: modula el gasto basal; riñón: '
           'equilibra agua, nitrógeno, glucosa y ácido–base; SNC: coordina apetito, recompensa, conducta y sistema autónomo. '
           'Control dinámico: la reducción de reservas desencadena respuestas compensatorias que dificultan mantener el descenso '
           'de peso.')


# ------------------------------------------------------------------ TEMA 34
def t34a(D):
    s = new(D, U, '34 · Núcleo arcuato: dos poblaciones neuronales opuestas', 'MAPA HIPOTALÁMICO')
    arc = s.shape(0.4, 1.1, 7.6, 6.0, 'roundRect', ('a', 'E8DAEF', 80), ('6C3483', 2.0), False, name='Hipotálamo', adj={'adj': 10000})
    s.text(0.5, 1.15, 4, 0.35, 'HIPOTÁLAMO', 13, F_HEAD, '4A235A', True, 'l')
    agrp = s.shape(1.0, 4.4, 2.2, 1.1, 'ellipse', shade('E74C3C', 0.35, 0.25), (INK, 1.5), SHD, 'NPY / AgRP\n(orexigénica)', 12.5, F_HEAD, WHITE, True, 'c', 'm', name='AgRP')
    pomc = s.shape(4.9, 4.4, 2.2, 1.1, 'ellipse', shade('27AE60', 0.35, 0.25), (INK, 1.5), SHD, 'POMC / CART\n(anorexigénica)', 12.5, F_HEAD, WHITE, True, 'c', 'm', name='POMC')
    s.text(1.0, 5.6, 6.1, 0.35, 'NÚCLEO ARCUATO (ARC)', 13, F_HEAD, '4A235A', True, 'c')
    pvn = s.shape(2.9, 1.7, 2.4, 1.1, 'ellipse', shade('85C1E9', 0.35, 0.25), (INK, 1.5), SHD, 'PVN\n(MC4R)', 13, F_HEAD, INK, True, 'c', 'm', name='PVN')
    am = s.arrow([(6.0, 4.38), (4.9, 2.85)], ACT, 3.5); s.text(5.6, 3.4, 1.6, 0.35, 'α-MSH', 13, F_HEAD, ACT, True, 'l', name='aMSH')
    ai = s.inhib([(2.1, 4.38), (3.3, 2.85)], w=3.5); s.text(0.9, 3.4, 1.8, 0.35, 'AgRP (antagoniza)', 12.5, F_HEAD, INH, True, 'r', name='AgRPtxt')
    ip = s.inhib([(3.25, 4.95), (4.85, 4.95)], w=3.0, name='AgRP inhibe POMC')
    lep = mol(s, 4.0, 6.25, 'gly', 'Leptina', d=0.5, w=1.15, name='Leptina', size=11.5); ins = mol(s, 5.4, 6.25, 'ins', 'Insulina', d=0.5, w=1.15, name='Insulina', size=11.5)
    gh = mol(s, 0.8, 6.25, 'gcg', 'Grelina', d=0.5, w=1.15, name='Grelina', size=11.5); py = mol(s, 2.15, 6.25, 'aa', 'PYY_{3-36}', d=0.5, w=1.2, name='PYY', size=11.5)
    l1 = s.arrow([(5.0, 6.25), (5.8, 5.52)], ACT, 2.5); l2 = s.inhib([(4.3, 6.25), (2.7, 5.52)], w=2.5)
    g1 = s.arrow([(1.4, 6.25), (1.7, 5.52)], ACT, 2.5); p1 = s.inhib([(2.6, 6.25), (2.3, 5.52)], w=2.5)
    k1 = card(s, 8.3, 1.1, 4.6, 2.5, '**NPY/AgRP** favorecen la ingesta: AgRP antagoniza/invierte el tono de **MC3R/MC4R**; NPY actúa en receptores **Y**.', LSALMON, 13.5, head='Orexigénicas')
    k2 = card(s, 8.3, 3.75, 4.6, 1.95, '**POMC/CART**: el POMC se procesa a **α-MSH**, que activa **MC4R** (saciedad y gasto).', MINT, 13.5, head='Anorexigénicas')
    k3 = card(s, 8.3, 5.85, 4.6, 1.25, '**Leptina e insulina**: activan POMC y frenan AgRP (JAK2–STAT3, PI3K).', YEL, 13)
    s.step(fade(agrp), fade(pomc), fade(pvn))
    s.step(wipe(am, 'b'), fade(k2))
    s.step(wipe(ai, 'b'), wipe(ip, 'l'), fade(k1))
    s.step(fade(lep), fade(ins), wipe(l1, 'b', after=True), wipe(l2, 'b'), fade(k3))
    s.step(fade(gh), wipe(g1, 'b', after=True), fade(py), wipe(p1, 'b'))
    s.note('Núcleo arcuato: neuronas NPY/AgRP orexigénicas favorecen la ingesta (AgRP antagoniza o invierte el tono constitutivo '
           'de MC3R/MC4R; NPY actúa en receptores Y); neuronas POMC/CART anorexigénicas procesan POMC a α-MSH, que activa MC4R '
           'en circuitos de saciedad y gasto (la expresión de CART no es marcador exclusivo de todas las acciones de POMC). '
           'Leptina e insulina tienden a activar POMC y frenar AgRP vía JAK2–STAT3 y PI3K según receptor y célula; la señal puede '
           'desarrollar resistencia con la obesidad. La grelina gástrica en ayuno actúa en GHS-R estimulando NPY/AgRP y el hambre; '
           'el PYY3-36 activa Y2 e inhibe las neuronas NPY/AgRP.')


def t34b(D):
    s = new(D, U, '34 · Otros núcleos y señales periféricas', 'MAPA HIPOTALÁMICO')
    brain(s, 0.4, 1.2, 4.6, name='Cerebro sagital')
    nu = [('PVN', 'salida autónoma y endocrina: **CRH**, **TRH**, simpático; MC4R', LBLUE),
          ('VMH', 'detección de energía/glucosa; gasto y simpático (no solo «centro de saciedad»)', MINT),
          ('Hipotálamo lateral', '**orexina/hipocretina** y **MCH**: alerta, búsqueda de alimento', LSALMON),
          ('Tronco / NTS', 'integra señales **vagales** intestinales', LILAC)]
    ids = []
    for i, (t, d, f) in enumerate(nu):
        ids.append(card(s, 5.3, 1.1 + i * 1.0, 7.6, 0.9, '**%s**: %s' % (t, d), f, 13.5, anchor='m', name='Núcleo ' + t, grow=False))
    gut = [('CCK', 'células **I** duodenoyeyunales (grasas/proteínas): vago, enlentece vaciamiento, saciedad corta; vesícula y páncreas'),
           ('PYY_{3-36}', 'células **L** ileocólicas: **Y2** → inhibe NPY/AgRP'),
           ('PP', 'células **PP** pancreáticas: **otra** hormona (≠ PYY)'),
           ('GLP-1', 'incretina y señal de saciedad/retardo del vaciamiento'),
           ('Insulina', 'señal **aguda** de nutrientes y **crónica** de adiposidad')]
    rows = [['Señal', 'Origen y acción']] + [[a, b] for a, b in gut]
    t, H = table(s, 0.4, 5.1, 12.5, rows, [1.6, 10.9], size=12.5, rowh=0.35, name='Tabla señales')
    for g in ids:
        s.step(fade(g))
    s.step(fade(t))
    s.note('Núcleo paraventricular (PVN): salida autonómica y endocrina (CRH → ACTH → cortisol; TRH → TSH → T4/T3), proyecciones '
           'melanocortínicas y control simpático. Núcleo ventromedial (VMH): detección de energía/glucosa y control de gasto, '
           'simpático y conducta; no es exclusivamente "centro de saciedad". Área hipotalámica lateral: orexina/hipocretina y MCH '
           'conectan alerta, búsqueda de alimento y gasto; tronco encefálico/NTS integra señales vagales. CCK (células I), '
           'PYY3-36 (células L, receptor Y2), polipéptido pancreático (células PP, distinto del PYY), GLP-1 e insulina.')


def t34c(D):
    s = new(D, U, '34 · Ejes neuroendocrinos e integración ayuno–saciedad')
    ax = flow(s, ['TRH', 'TSH', 'T4 → T3 nuclear: ↑ metabolismo basal, Na^{+}/K^{+} ATPasa, termogénesis'], 0.4, 1.1, 12.5, 0.95, [LBLUE, LBLUE, MINT], 14, 0.3)
    ax2 = flow(s, ['CRH', 'ACTH', 'Cortisol: moviliza energía; exceso crónico → hiperfagia, adiposidad central, catabolismo'], 0.4, 2.3, 12.5, 0.95, [LSALMON, LSALMON, YEL], 14, 0.3)
    sy = card(s, 0.4, 3.5, 12.5, 0.85, '**Simpático**: noradrenalina estimula BAT y lipólisis; «termogénesis» **no siempre** equivale a un cambio de peso clínicamente importante.', CREAM, 13.5, grow=False)
    fa = card(s, 0.4, 4.55, 6.1, 1.4, '**Ayuno**: leptina/insulina ↓, grelina puede ↑, NPY/AgRP activas → **hambre y conservación** energética.', LSALMON, 13.5)
    fe = card(s, 6.8, 4.55, 6.1, 1.4, '**Saciedad**: nutrientes, CCK, PYY, GLP-1, insulina y leptina → **POMC/α-MSH** limitan la ingesta.', MINT, 13.5)
    q = card(s, 0.4, 6.1, 12.5, 1.0, '¿Leptina alta y hambre? **Resistencia central** y redundancia · ¿Hipertiroidismo y pérdida de peso pese al hambre? **Gasto > aporte** · ¿Por qué cuesta mantener el descenso? **Señales compensatorias**.', YEL, 13, grow=False)
    flow_anim(s, ax); flow_anim(s, ax2)
    s.step(fade(sy)); s.step(fade(fa)); s.step(fade(fe)); s.step(fade(q))
    s.note('TRH hipotalámica → TSH adenohipofisaria → producción tiroidea; la T3 nuclear regula el metabolismo basal, la bomba '
           'Na+/K+, el gasto y la termogénesis. CRH–ACTH–cortisol moviliza energía bajo estrés; su exceso crónico favorece '
           'hiperfagia en algunos contextos, adiposidad central, hiperglucemia y catabolismo muscular. Integración en ayuno y '
           'saciedad. Preguntas para la exposición: ¿cómo puede una persona con leptina alta tener hambre? (resistencia a la '
           'señalización central y circuitos redundantes); ¿por qué el hipertiroidismo suele causar pérdida de peso pese al '
           'hambre? (el gasto aumentado puede exceder el aporte); ¿por qué cuesta mantener el peso perdido? (señales '
           'compensatorias de hambre y ahorro energético).')


# ------------------------------------------------------------------ TEMA 35
def t35a(D):
    s = new(D, U, '35 · «Los azúcares engordan»: análisis crítico')
    st = s.shape(0.4, 1.1, 12.5, 1.0, 'rect', RED, (INK, 1.5), SHD, '«Los azúcares engordan» → la frase es **demasiado absoluta**', 20, F_HEAD, WHITE, False, 'c', 'm', name='Frase')
    dest = [('Oxidación', 'una gran fracción se **oxida**', LBLUE), ('Glucógeno', 'repone **glucógeno**', MINT), ('DNL', 'bajo ciertas condiciones → **lipogénesis de novo**', YEL)]
    ids = [card(s, 0.4 + i * 4.2, 2.35, 4.0, 1.6, '**%s**: %s' % (t, d), f, 15, anchor='m', name='Destino ' + t) for i, (t, d, f) in enumerate(dest)]
    k = card(s, 0.4, 4.2, 6.1, 2.9, 'El **exceso energético sostenido** favorece la acumulación de grasa **independientemente** de que las calorías provengan de azúcares, grasas o mezclas. Depende del patrón alimentario, densidad energética, saciedad, actividad y sensibilidad a insulina.', CREAM, 14, head='Balance')
    i = card(s, 6.8, 4.2, 6.1, 2.9, 'La insulina facilita el almacenamiento lipídico e inhibe la lipólisis, pero **no viola el balance energético**. «Comer azúcar se convierte automáticamente en grasa» es **falso**.', YEL, 14, head='Insulina')
    s.step(fade(st))
    for g in ids:
        s.step(fade(g))
    s.step(fade(k)); s.step(fade(i))
    s.note('La frase es demasiado absoluta. Los carbohidratos aportan energía; al consumirlos se oxidan, reponen glucógeno y, bajo '
           'determinadas condiciones, alimentan la lipogénesis de novo. El exceso energético sostenido favorece la acumulación de '
           'grasa corporal independientemente de que las calorías excedentes provengan de azúcares, grasas o mezclas. La insulina '
           'facilita el almacenamiento lipídico e inhibe la lipólisis, pero no viola el balance energético.')


def t35b(D):
    s = new(D, U, '35 · Ruta mecanística: sacarosa, glucosa y fructosa', 'RUTA ANIMADA')
    sac = chip(s, 4.6, 1.1, 'Sacarosa', TAG, 15, name='Sacarosa')
    g = chain(s, 1.0, 1.9, ['Glucosa', 'Glucólisis → piruvato', 'Acetil-CoA → citrato citosólico', 'ACC/FASN → AG → TAG'], dy=1.15, w=3.3,
              enzymes=['PFK-1 (regulada)', 'PDH', None], rev=[False, False, False], fill=[LBLUE, YEL, ENE, LSALMON], name='Ruta glucosa', h=0.55, size=13.5)
    f = chain(s, 7.6, 1.9, ['Fructosa', 'Fructosa-1-P', 'Triosas (DHAP + gliceraldehído)', 'Glucosa · glucógeno · lactato · DNL'], dy=1.15, w=3.6,
              enzymes=['KHK (fructocinasa, ATP)', 'aldolasa B', None], rev=[False, False, False], fill=[lighten(MOL['fru'][0], 0.5), YEL, YEL, MINT], name='Ruta fructosa', h=0.55, size=13.5, side='r')
    a1 = s.arrow([(4.9, 1.6), (2.65, 1.88)], INK, 2.5); a2 = s.arrow([(5.6, 1.6), (9.4, 1.88)], INK, 2.5)
    by = note_box(s, 4.6, 3.1, 2.7, 1.75, 'La fructosa **evita** el paso limitante de **PFK-1**.', 13.5, name='Bypass')
    k = card(s, 0.4, 6.35, 12.5, 0.75, 'En ingestas **elevadas y sostenidas** (sobre todo **bebidas azucaradas**) pueden aumentar la DNL y los TAG hepáticos/VLDL.', CREAM, 14, grow=False)
    s.step(fade(sac), wipe(a1, 'r', after=True), wipe(a2, 'l'))
    chain_anim(s, g, per_click=4)
    chain_anim(s, f, per_click=4)
    s.step(zoom(by)); s.step(fade(k))
    s.note('Ruta mecanística posible: sacarosa → glucosa + fructosa. Glucosa → glucólisis → piruvato → acetil-CoA → citrato '
           'citosólico → ACC/FASN → AG → TAG. Fructosa hepática vía fructocinasa/KHK → fructosa-1-fosfato → triosas por la '
           'aldolasa B, que entran en gluconeogénesis, glucólisis, glucógeno, lactato y DNL. La fructosa evita el paso regulado '
           'por PFK-1. En ingestas elevadas y sostenidas, especialmente bebidas azucaradas, pueden aumentar la DNL y los TAG '
           'hepáticos/VLDL (Unidad V, patología 2).')


def t35c(D):
    s = new(D, U, '35 · Consecuencias nutricionales')
    l = card(s, 0.4, 1.1, 6.1, 3.2, '**Azúcar añadido líquido**: baja capacidad **saciante** por caloría en muchas circunstancias → facilita la **ingesta excesiva**.', LSALMON, 15.5, head='Bebidas azucaradas', headfill=INH)
    r = card(s, 6.8, 1.1, 6.1, 3.2, '**Frutas enteras**: azúcares junto con **fibra, agua y matriz alimentaria**; no son metabólicamente intercambiables con grandes dosis de bebidas azucaradas.', MINT, 15.5, head='Fruta entera', headfill=ACT)
    gl = s.group_start('Ícono bebida')
    s.free(1.2, 4.6, 1.0, 1.6, 'M 0 0 L 1000 0 L 850 1000 L 150 1000 Z', ('lin', [(0, 'F5B041'), (100, 'D35400')], 90), (INK, 1.5))
    s.arrow([(1.95, 4.1), (1.75, 4.9)], 'E74C3C', 4, tail=None)
    s.group_end()
    ap = s.group_start('Ícono fruta')
    s.shape(10.8, 4.75, 1.4, 1.35, 'ellipse', shade('E74C3C', 0.4, 0.3), ('922B21', 1.5), False)
    s.free(11.45, 4.35, 0.5, 0.45, smooth([(0, 1000), (300, 200), (1000, 0), (700, 700)]), shade('58D68D', 0.3, 0.2), ('1E8449', 1.0))
    s.group_end()
    p = note_box(s, 2.6, 4.55, 7.9, 2.55, '«Toda la fructosa se convierte en grasa» → **falso**: tiene muchos destinos; la DNL puede aumentar con **altas cargas**.\n«Comer azúcar se convierte automáticamente en grasa» → **falso**: la ganancia de adiposidad depende del **balance sostenido**.', 15.5)
    s.step(fade(gl), fade(l)); s.step(fade(ap), fade(r)); s.step(fade(p))
    s.note('Consecuencia nutricional: el azúcar añadido líquido tiene baja capacidad saciante por caloría en muchas circunstancias y '
           'facilita la ingesta excesiva. Las frutas enteras contienen azúcares junto con fibra, agua y matriz alimentaria y no son '
           'metabólicamente intercambiables con grandes dosis de bebidas azucaradas. Errores frecuentes: "toda la fructosa se '
           'convierte en grasa" y "comer azúcar se convierte automáticamente en grasa".')


def build(D):
    t31a(D); t31b(D)
    t32a(D); t32b(D); t32c(D)
    t33a(D); t33b(D)
    t34a(D); t34b(D); t34c(D)
    t35a(D); t35b(D); t35c(D)
