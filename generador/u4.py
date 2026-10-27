# -*- coding: utf-8 -*-
"""UNIDAD IV — Morph 5 (nitrógeno), temas 25 a 30"""
from base import *

U = 4


def div(D):
    def art(s):
        kidney(s, 8.6, 0.9, 1.6, name='Arte riñón')
        liver(s, 10.0, 1.3, 3.0, name='Arte hígado')
        muscle(s, 8.4, 3.6, 3.2, name='Arte músculo', fibers=2)
        mol(s, 11.8, 3.9, 'urea', d=0.65); mol(s, 12.2, 4.7, 'nh4', d=0.6); mol(s, 11.5, 5.3, 'gln', d=0.6)
        brain(s, 8.6, 5.3, 2.0, name='Arte cerebro'); adipocyte_brown(s, 10.9, 5.6, 1.4, name='Arte BAT')
    divider(D, U, 'IV', 'NITRÓGENO, RIÑÓN\nY HOMEOSTASIS', 'Carbono, nitrógeno, ácido–base y balance energético',
            ['25 · Zonación hepática y amoníaco', '26 · Ureogénesis en saciedad y ayuno', '27 · Dieta hiperproteica y agua', '28 · Ciclo de urea en la inanición',
             '29 · Glutamina: carbono y nitrógeno', '30 · Gluconeogénesis renal', '31 · AMP desaminasa en el ejercicio', '32 · Tejido adiposo blanco y marrón',
             '33 · Balance energético', '34 · Control hipotalámico', '35 · Azúcares, lipogénesis y adiposidad'], art,
            'Unidad IV. El nitrógeno no tiene depósito: se redistribuye entre órganos (alanina, glutamina) y se elimina como urea y '
            'NH4+. Se integran hígado, riñón, músculo e intestino con el equilibrio ácido–base, y luego el balance energético y su '
            'control hipotalámico.')


def m5txt(s, t, head):
    return card(s, 8.9, 1.1, 4.0, 4.4, t, CREAM, 15, name='!!Texto M5', head=head)


def m5a(D):
    s = new(D, U, 'Nitrógeno: del músculo a los aminoácidos', 'SECUENCIA MORPH 5 · 1/5')
    muscle(s, 0.4, 1.3, 8.2, name='!!Músculo M5', fibers=3)
    aas = [mol(s, 1.5 + i * 1.3, 2.4 + (i % 2) * 1.0, 'aa', d=0.5, name='!!AA M5 %d' % i) for i in range(5)]
    m5txt(s, '- **Proteólisis** muscular (recambio, ayuno, estrés).\n- Los grupos amino se concentran en **glutamato** por transaminación.\n- Se exportan como **alanina** y **glutamina**: formas seguras de transporte de N.', 'Músculo')
    s.step(*[zoom(a, after=(i > 0)) for i, a in enumerate(aas)])
    s.note('Secuencia Morph 5 (metabolismo del nitrógeno): músculo → aminoácidos → hígado → ciclo de la urea → riñón → '
           'excreción. Las fichas verdes de aminoácidos conservan su nombre en todas las diapositivas para que Morph muestre su '
           'recorrido. El músculo es el principal reservorio de proteínas; su nitrógeno sale como alanina y glutamina.')


def m5b(D):
    s = new(D, U, 'Nitrógeno: transporte en sangre', 'SECUENCIA MORPH 5 · 2/5', morph=True)
    muscle(s, 0.4, 4.8, 3.6, name='!!Músculo M5', fibers=3)
    vessel(s, 0.3, 3.4, 8.4, 0.9, name='!!Vaso M5', rbcs=4)
    liver(s, 4.6, 0.95, 4.0, name='!!Hígado M5')
    labs = ['Ala', 'Gln', 'Ala', 'Gln', 'Ala']
    aas = [mol(s, 1.0 + i * 1.3, 3.6, 'ala' if labs[i] == 'Ala' else 'gln', d=0.5, name='!!AA M5 %d' % i) for i in range(5)]
    m5txt(s, '- **Alanina** → hígado (gluconeogénesis + urea).\n- **Glutamina** → riñón e intestino (y hígado periportal).\n- Así se evita circular **NH_{3}** libre, neurotóxico.', 'Sangre')
    s.note('Morph: el músculo se reduce, aparece el vaso y el hígado. Los aminoácidos se transforman en alanina y glutamina, que '
           'circulan hacia hígado, riñón e intestino. Transportar el nitrógeno en estas moléculas evita circular amoníaco libre, '
           'que es neurotóxico.')


def m5c(D):
    s = new(D, U, 'Nitrógeno: el hígado periportal fabrica urea', 'SECUENCIA MORPH 5 · 3/5', morph=True)
    vessel(s, 0.3, 6.1, 8.4, 0.7, name='!!Vaso M5', rbcs=4)
    liver(s, 0.4, 1.0, 8.0, name='!!Hígado M5')
    aas = [mol(s, 1.4 + i * 0.6, 2.3, 'nh4', d=0.5, name='!!AA M5 %d' % i) for i in range(5)]
    uc = s.shape(2.0, 3.0, 3.0, 1.6, 'ellipse', ('a', 'FFFFFF', 60), ('1E8449', 3.0), SHD, 'CICLO\nDE LA UREA', 16, F_HEAD, '1E8449', True, 'c', 'm', name='!!Ciclo urea M5')
    ur = mol(s, 5.4, 3.5, 'urea', d=0.65, name='!!Urea M5')
    m5txt(s, '- Desaminación/transaminación → **NH_{4}^{+}** y **aspartato**.\n- **Ciclo de la urea** (mitocondria + citosol) en la zona **periportal**.\n- La **urea** es hidrosoluble y poco tóxica.', 'Hígado')
    s.step(pulse(uc), zoom(ur, after=True))
    s.note('Morph: el hígado ocupa la escena; los aminoácidos se convierten en NH4+ (fichas verde azulado) que ingresan al ciclo '
           'de la urea de los hepatocitos periportales. La urea resultante es hidrosoluble, poco tóxica y sale a la sangre.')


def m5d(D):
    s = new(D, U, 'Nitrógeno: la urea llega al riñón', 'SECUENCIA MORPH 5 · 4/5', morph=True)
    liver(s, 0.3, 1.0, 2.6, name='!!Hígado M5')
    vessel(s, 0.3, 3.4, 8.4, 0.9, name='!!Vaso M5', rbcs=4)
    s.shape(1.0, 2.0, 1.2, 0.6, 'ellipse', ('a', 'FFFFFF', 60), ('1E8449', 2.0), False, 'urea', 11, F_HEAD, '1E8449', True, 'c', 'm', name='!!Ciclo urea M5')
    mol(s, 3.6, 3.55, 'urea', d=0.6, name='!!Urea M5')
    kidney(s, 6.0, 1.0, 1.7, name='!!Riñón M5')
    aas = [mol(s, 4.4 + i * 0.5, 3.6, 'urea', d=0.45, name='!!AA M5 %d' % i) for i in range(5)]
    gl = mol(s, 1.2, 5.0, 'gln', d=0.55, name='Glutamina a riñón')
    m5txt(s, '- La **urea** se **filtra** en el glomérulo; su reabsorción depende del flujo y de **ADH**.\n- La **glutamina** llega al túbulo proximal: **amoniogénesis**.', 'Circulación')
    s.step(fade(gl), path(gl, 5.6, -1.6, after=True, dur=1600))
    s.note('Morph: el hígado se reduce y aparece el riñón. La urea se filtra en el glomérulo y una fracción se reabsorbe según el '
           'flujo tubular y la ADH. La glutamina llega al túbulo proximal, donde se genera NH4+ (amoniogénesis).')


def m5e(D):
    s = new(D, U, 'Nitrógeno: excreción renal de urea y NH_{4}^{+}', 'SECUENCIA MORPH 5 · 5/5', morph=True)
    kidney(s, 0.6, 1.0, 3.6, name='!!Riñón M5')
    aas = [mol(s, 5.5 + (i % 3) * 0.7, 4.6 + (i // 3) * 0.7, 'urea' if i < 3 else 'nh4', d=0.55, name='!!AA M5 %d' % i) for i in range(5)]
    s.shape(5.2, 4.3, 2.9, 2.0, 'roundRect', ('a', 'F9E79F', 60), ('B7950B', 2.0), False, 'ORINA', 14, F_HEAD, '7E5109', True, 'c', 'b', name='Orina')
    m5txt(s, '- **Urea**: principal forma de excreción de N.\n- **NH_{4}^{+}** urinario: excreción de **ácido neto** (crece en acidosis y ayuno).\n- **Ureogénesis ≠ amoniogénesis**: distinta enzimología, órgano y función.', 'Excreción')
    s.note('Morph final: la urea y el NH4+ llegan a la orina. La urea es la principal forma de excreción de nitrógeno; el NH4+ '
           'urinario es un mecanismo crucial de excreción de ácido neto (aumenta en acidosis y ayuno prolongado). Distinción '
           'clave: ureogénesis (hígado, ciclo de la urea) frente a amoniogénesis (riñón, glutaminasa y GDH).')


# ------------------------------------------------------------------ TEMA 25
def t25_zone(D):
    s = new(D, U, '25 · Zonación hepática: periportal frente a perivenosa', 'ÁCINO HEPÁTICO')
    pt = s.group_start('Tríada portal')
    s.shape(0.4, 2.3, 1.4, 2.4, 'roundRect', ('a', 'FFFFFF', 60), (INK, 1.0), False, adj={'adj': 30000})
    s.shape(0.55, 2.5, 0.6, 0.6, 'ellipse', shade('5D6D7E', 0.3, 0.2), (INK, 1.0), False, 'VP', 10, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.shape(1.15, 3.2, 0.45, 0.45, 'ellipse', shade('C0392B', 0.3, 0.2), (INK, 1.0), False, 'A', 10, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.shape(0.6, 3.8, 0.4, 0.4, 'ellipse', shade('27AE60', 0.3, 0.2), (INK, 1.0), False, 'B', 10, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.text(0.4, 4.75, 1.4, 0.3, 'Tríada portal', 12, F_HEAD, INK, True, 'c')
    s.group_end()
    cv = s.shape(11.0, 2.6, 1.6, 1.6, 'ellipse', shade('5B2C6F', 0.3, 0.2), (INK, 1.25), SHD, 'Vena\ncentral', 12, F_HEAD, WHITE, True, 'c', 'm', name='Vena central')
    s.shape(1.8, 3.15, 9.2, 0.6, 'rect', ('lin', [(0, 'F5B7B1'), (100, 'C39BD3')], 0), (INK, 0.75), False, 'sinusoide: gradiente de O_{2}, hormonas y sustratos →', 12, F_HEAD, INK, True, 'c', 'm', name='Sinusoide')
    for row, y in ((0, 2.15), (1, 3.85)):
        for i in range(9):
            f = i / 8
            col = '%02X%02X%02X' % (int(0xF5 + (0xBB - 0xF5) * f), int(0xB0 + (0x8F - 0xB0) * f), int(0x9A + (0xCE - 0x9A) * f))
            s.shape(1.85 + i * 1.02, y, 0.98, 0.95, 'hexagon', shade(col, 0.3, 0.15), ('7B241C', 0.75), False, name='Hepatocito %d-%d' % (row, i), adj={'adj': 25000, 'vf': 115470})
    z1 = s.shape(1.85, 1.2, 3.0, 0.8, 'rect', TAG, (INK, 1.25), SHD, 'ZONA 1 · PERIPORTAL', 14, F_HEAD, INK, True, 'c', 'm', name='Zona 1')
    z3 = s.shape(8.0, 1.2, 2.9, 0.8, 'rect', LILAC, (INK, 1.25), SHD, 'ZONA 3 · PERIVENOSA', 14, F_HEAD, INK, True, 'c', 'm', name='Zona 3')
    nh = [mol(s, 2.0 + i * 0.35, 3.25, 'nh4', d=0.38, name='NH4 sinusoide %d' % i) for i in range(4)]
    ur = mol(s, 4.45, 3.95, 'urea', d=0.55, name='Urea zona 1')
    gq = mol(s, 9.45, 3.95, 'gln', d=0.55, name='Glutamina zona 3')
    k1 = card(s, 0.4, 5.15, 5.8, 1.95, '**Zona 1**: más O_{2}; transaminaciones, **glutaminasa**, **GDH** y ciclo de la urea (**CPS1, OTC, ASS1, ASL, ARG1**). **Gran capacidad**, afinidad global menor.', MINT, 13.5)
    k2 = card(s, 6.6, 5.15, 6.3, 1.95, '**Zona 3**: banda pequeña con **glutamina sintetasa** (GS): glutamato + NH_{4}^{+} + ATP → glutamina. **Último filtro de alta afinidad** para el NH_{4}^{+} residual.', LILAC, 13.5)
    s.step(fade(z1), fade(z3))
    s.step(*[path(n, 1.6 - i * 0.3, 0.0, dur=1200, delay=i * 150) for i, n in enumerate(nh[:3])], path(nh[3], 7.3, 0.0, dur=2200))
    s.step(*[out(n) for n in nh[:3]], zoom(ur, after=True), fade(k1))
    s.step(out(nh[3]), zoom(gq, after=True), fade(k2))
    s.note('El lobulillo/ácino hepático tiene un gradiente desde la zona periportal (zona 1, sangre recién llegada, más O2) hasta '
           'la pericentral/perivenosa (zona 3, menos O2). La organización funcional evita que la sangre salga del hígado cargada de '
           'NH3/NH4+. Zona periportal: captación y oxidación de aminoácidos, transaminaciones, glutaminasa, glutamato '
           'deshidrogenasa y ciclo de la urea enzimáticamente enriquecido; gran capacidad pero afinidad global menor. Zona '
           'perivenosa: una banda menor de hepatocitos expresa glutamina sintetasa, último filtro de alta afinidad para el NH4+ '
           'residual que escapó a la ureogénesis. La animación muestra la mayoría del amonio convertido en urea en la zona 1 y el '
           'residual capturado como glutamina en la zona 3.')


def t25_urea(D):
    s = new(D, U, '25 · Ciclo de la urea paso a paso', 'CICLO ANIMADO')
    s.shape(0.3, 1.05, 4.2, 6.05, 'roundRect', ('a', 'F8C471', 65), ('B9770E', 2.5), False, name='Mitocondria', adj={'adj': 15000})
    s.text(0.4, 1.1, 4.0, 0.35, 'MITOCONDRIA', 13, F_HEAD, '7E5109', True, 'c')
    s.text(4.7, 1.1, 4.4, 0.35, 'CITOSOL', 13, F_HEAD, INK, True, 'c')
    nh = mol(s, 0.5, 1.6, 'nh4', d=0.48, name='NH4'); hc = chip(s, 1.1, 1.65, 'HCO_{3}^{−}', LBLUE, 12.5, name='HCO3')
    at = mol(s, 2.3, 1.62, 'atp', '2 ATP', d=0.42, w=0.75, name='2ATP')
    cps = enz(s, 0.55, 2.3, 'CPS1', name='CPS1')
    nag = s.shape(1.55, 2.25, 1.6, 0.42, 'roundRect', MINT, (ACT, 1.5), False, 'NAG (obligatorio)', 11.5, F_HEAD, INK, True, 'c', 'm', name='NAG')
    cp = chip(s, 0.55, 2.95, 'Carbamoil-P', YEL, 13, w=1.7, name='Carbamoil-P')
    orm = chip(s, 2.55, 3.95, 'Ornitina', YEL, 13, w=1.5, name='Ornitina mito')
    otc = enz(s, 0.6, 3.95, 'OTC', name='OTC')
    cim = chip(s, 0.55, 4.7, 'Citrulina', YEL, 13, w=1.7, name='Citrulina mito')
    a = [s.arrow([(1.0, 2.1), (1.0, 2.93)], ACT, 3), s.arrow([(1.4, 3.37), (1.4, 4.68)], ACT, 3), s.arrow([(2.55, 4.15), (2.27, 4.85)], ACT, 2.5)]
    cit = chip(s, 4.9, 2.0, 'Citrulina', YEL, 13, w=1.7, name='Citrulina cito')
    asc = chip(s, 7.4, 2.0, 'Argininosuccinato', YEL, 13, w=2.0, name='Argininosuccinato')
    arg = chip(s, 7.4, 4.7, 'Arginina', YEL, 13, w=2.0, name='Arginina')
    orn = chip(s, 4.9, 4.7, 'Ornitina', YEL, 13, w=1.7, name='Ornitina cito')
    t1 = s.arrow([(2.27, 4.75), (4.88, 2.2)], TRN, 2.5, name='Salida citrulina')
    e1 = s.group_start('Paso ASS1'); s.arrow([(6.62, 2.2), (7.38, 2.2)], ACT, 3); enz(s, 6.3, 2.55, 'ASS1', size=11.5)
    mol(s, 6.65, 1.35, 'aa', 'Asp', d=0.42, name='Aspartato'); s.text(7.1, 1.35, 1.9, 0.4, '+ ATP → AMP + PP_{i}', 11.5, F_HEAD, '7E5109', True, 'l', 'm'); s.group_end()
    e2 = s.group_start('Paso ASL'); s.arrow([(8.4, 2.43), (8.4, 4.68)], ACT, 3); enz(s, 8.55, 3.2, 'ASL', size=11.5); s.group_end()
    fum = chip(s, 8.55, 3.65, 'Fumarato → Krebs', LSALMON, 12, name='Fumarato')
    e3 = s.group_start('Paso ARG1'); s.arrow([(7.38, 4.9), (6.62, 4.9)], ACT, 3); enz(s, 6.3, 5.25, 'Arginasa 1', size=11.5); s.group_end()
    ur = mol(s, 6.6, 5.75, 'urea', d=0.6, name='Urea producto')
    rt = s.arrow([(4.88, 4.95), (4.05, 4.2)], TRN, 2.5, name='Ornitina regresa')
    k = card(s, 9.3, 1.1, 3.6, 6.0, '**Costo**: 3 ATP, pero **4 enlaces** de alta energía por urea.\n\n**Nitrógenos**: NH_{4}^{+} libre y **aspartato**.\n\n**Carbono**: bicarbonato/CO_{2}.\n\n**CPS1** exige **N-acetilglutamato** (NAG).', CREAM, 14, head='Balance')
    s.step(fade(nh), fade(hc), zoom(at, after=True), fade(cps), fade(nag), fade(a[0], after=True), fade(cp, after=True))
    s.step(fade(orm), fade(otc), wipe(a[1], 't'), wipe(a[2], 'l'), fade(cim, after=True))
    s.step(wipe(t1, 'l'), fade(cit, after=True))
    s.step(fade(e1), fade(asc, after=True))
    s.step(fade(e2), fade(arg, after=True), fade(fum))
    s.step(fade(e3), fade(orn, after=True), zoom(ur, after=True))
    s.step(wipe(rt, 'r'), pulse(orm, after=True))
    s.step(fade(k))
    s.note('Ciclo de la urea paso a paso (por clic). (1) Mitocondria: NH4+ + HCO3− + 2 ATP → carbamoil-fosfato por la CPS1, '
           'activada obligatoriamente por N-acetilglutamato (NAG). (2) Carbamoil-P + ornitina → citrulina (OTC). La citrulina sale '
           'al citosol. (3) Citrulina + aspartato + ATP → argininosuccinato (ASS1), liberando AMP + PPi. (4) ASL → arginina + '
           'fumarato. (5) Arginasa 1 → urea + ornitina, que regresa a la mitocondria. Costo: 3 ATP pero 4 enlaces fosfato de alta '
           'energía por urea. Orígenes del nitrógeno: NH4+ libre y aspartato; carbono de la urea: bicarbonato/CO2.')


def t25_krebs(D):
    s = new(D, U, '25 · Ciclo de Krebs conectado con la ureogénesis')
    u = s.shape(0.6, 1.5, 5.0, 4.6, 'ellipse', None, ('1E8449', 4.0), False, name='Ciclo urea')
    k = s.shape(7.7, 1.5, 5.0, 4.6, 'ellipse', None, ('B9770E', 4.0), False, name='Ciclo Krebs')
    s.text(1.7, 3.5, 2.8, 0.6, 'CICLO DE\nLA UREA', 18, F_HEAD, '1E8449', True, 'c', 'm')
    s.text(8.8, 3.5, 2.8, 0.6, 'CICLO DE\nKREBS', 18, F_HEAD, '7E5109', True, 'c', 'm')
    un = [('Ornitina', 1.0, 4.9), ('Citrulina', 1.0, 1.6), ('Argininosuccinato', 3.2, 1.25), ('Arginina', 3.9, 5.3)]
    kn = [('Citrato', 10.6, 1.35), ('α-cetoglutarato', 11.2, 3.5), ('Succinil-CoA', 10.6, 5.6), ('Oxaloacetato', 7.6, 2.0)]
    for t, x, y in un:
        chip(s, x, y, t, MINT, 12.5, name='U ' + t)
    for t, x, y in kn:
        chip(s, x, y, t, YEL, 12.5, name='K ' + t)
    fum = s.shape(5.6, 4.6, 1.6, 0.5, 'roundRect', LSALMON, (INK, 1.5), SHD, 'Fumarato', 13.5, F_HEAD, INK, True, 'c', 'm', name='Fumarato puente')
    mal = s.shape(7.1, 4.0, 1.4, 0.5, 'roundRect', YEL, (INK, 1.5), SHD, 'Malato', 13.5, F_HEAD, INK, True, 'c', 'm', name='Malato puente')
    asp = s.shape(5.6, 1.3, 1.6, 0.5, 'roundRect', MINT, (INK, 1.5), SHD, 'Aspartato', 13.5, F_HEAD, INK, True, 'c', 'm', name='Aspartato puente')
    a1 = s.arrow([(5.1, 4.4), (5.6, 4.75)], ACT, 3)
    a2 = s.arrow([(7.2, 4.85), (7.5, 4.52)], ACT, 3)
    a3 = s.arrow([(7.8, 3.98), (8.2, 2.5)], ACT, 3)
    a4 = arrow_lbl(s, [(7.6, 2.0), (7.22, 1.6)], 'transaminación (AST)', ACT, 3, lw=2.1, lx=6.0, ly=1.85, size=11.5)
    a5 = s.arrow([(5.6, 1.55), (4.95, 1.5)], ACT, 3)
    k1 = note_box(s, 0.4, 6.35, 12.5, 0.75, 'Derivación **aspartato–argininosuccinato**: fumarato → malato → oxaloacetato → aspartato, que aporta el **segundo N** de la urea.', 14)
    s.step(fade(u), fade(k))
    s.step(wipe(a1, 'l'), fade(fum, after=True))
    s.step(wipe(a2, 'l'), fade(mal, after=True), wipe(a3, 'b', after=True))
    s.step(wipe(a4, 'r'), fade(asp, after=True), wipe(a5, 'r', after=True))
    s.step(fade(k1))
    s.note('Conexión Krebs–urea ("bicicleta de Krebs"): el fumarato liberado por la argininosuccinato liasa se hidrata a malato, '
           'que se oxida a oxaloacetato (con NADH); la aspartato aminotransferasa (AST) transamina el oxaloacetato a aspartato, que '
           'reingresa al ciclo de la urea aportando el segundo nitrógeno. Así se acoplan el destino del carbono y el del '
           'nitrógeno.')


def t25_ctrl(D):
    s = new(D, U, '25 · Control de la ureogénesis y clínica')
    nag = flow(s, ['Arginina ↑', 'NAGS', 'N-acetilglutamato', 'CPS1 activa'], 0.4, 1.15, 6.0, 3.3, [YEL, 'FFFFFF', MINT, ACT], 14.5, 0.22, 'v', ACT, bold=True)
    k1 = card(s, 6.7, 1.1, 6.2, 1.8, 'La arginina favorece la síntesis de **NAG** vía **NAGS**: acopla la necesidad de eliminar N con la activación de CPS1. En estados proteicos/catabólicos ↑ la **expresión** de varias enzimas.', CREAM, 13.5, head='Regulación')
    k2 = card(s, 6.7, 3.05, 6.2, 1.4, '**GDH**: desamina glutamato a α-KG + NH_{4}^{+} **o lo amina** según las condiciones: no es una flecha irreversible.', LBLUE, 13.5, head='GDH')
    k3 = note_box(s, 0.4, 4.65, 6.0, 1.15, '**Glutaminasa**: glutamina → glutamato + NH_{4}^{+}. **GS**: dirección contraria y **gasta ATP**.', 13.5)
    cl = card(s, 6.7, 4.65, 6.2, 2.45, '- Si falla la urea, **asciende el amonio** (neurotóxico, altera el metabolismo astroglial).\n- Déficit de **OTC**: el carbamoil-P se desvía a **pirimidinas** → ↑ **ácido orótico**.\n- **Alcalosis respiratoria** temprana y encefalopatía orientan a hiperamonemia grave.', LSALMON, 13.5, head='Clínica')
    ui = card(s, 0.4, 6.0, 6.0, 1.1, 'A diferencia del amonio, la **urea no es neurotóxica**.', MINT, 14)
    flow_anim(s, nag)
    s.step(fade(k1)); s.step(fade(k2)); s.step(fade(k3)); s.step(fade(cl)); s.step(fade(ui))
    s.note('Control: la arginina favorece la síntesis de N-acetilglutamato vía NAGS, coordinando la necesidad de eliminación '
           'nitrogenada con la activación de CPS1; en estado proteico o catabólico aumenta la expresión de varias enzimas. La GDH '
           'puede desaminar glutamato a α-cetoglutarato + NH4+ o aminarlo según las condiciones. Clínica: si falla la urea '
           'asciende el amonio; en el déficit de OTC puede elevarse el ácido orótico porque el carbamoil-P mitocondrial se desvía '
           'a la síntesis pirimidínica; la alcalosis respiratoria temprana (hiperventilación por estimulación central) y la '
           'encefalopatía orientan a hiperamonemia grave.')


def t26(D):
    s = new(D, U, '26 · ¿Por qué hay ureogénesis en saciedad y en ayuno?')
    l = card(s, 0.4, 1.1, 6.1, 2.9, '- La ingesta proteica entrega **N que excede** los requerimientos anabólicos.\n- ↑ transaminación/desaminación → **↑ urea**.', MINT, 15, head='Saciedad', headfill=ACT)
    r = card(s, 6.8, 1.1, 6.1, 2.9, '- Sin aporte dietario, la **proteólisis endógena** y el reciclado de AA generan N (sobre todo en la adaptación inicial).\n- Luego la **cetosis reduce** el catabolismo proteico relativo.', LBLUE, 15, head='Ayuno', headfill=TRN)
    b = card(s, 0.4, 4.2, 6.1, 2.9, 'Siempre se degradan proteínas: **recambio**, mantenimiento intestinal y tisular, neurotransmisores. **No existe depósito** de AA. La urea es una vía **segura de excreción**, no de ATP.', YEL, 14.5, head='Base común')
    p = note_box(s, 6.8, 4.2, 6.1, 2.9, '**Urea plasmática ≠ velocidad de producción**: cambia con función renal, hidratación (ADH) y **hemorragia digestiva**. No equiparar urea alta con dieta proteica.', 14.5)
    s.step(fade(l)); s.step(fade(r)); s.step(fade(b)); s.step(fade(p))
    s.note('Siempre se degradan proteínas y aminoácidos por recambio proteico, mantenimiento intestinal, hígado, tejidos y '
           'metabolismo de neurotransmisores; no existe depósito exclusivo para el exceso de aminoácidos. En saciedad la ingesta '
           'proteica entrega nitrógeno que excede los requerimientos anabólicos. En ayuno, aunque no haya aporte dietario, la '
           'proteólisis endógena y el reciclado generan nitrógeno; luego la cetosis reduce el catabolismo proteico relativo. El '
           'riñón excreta urea filtrada y reabsorbida en proporciones que dependen del flujo y de la ADH; la concentración de urea '
           'no es idéntica a su velocidad de producción.')


def t27(D):
    s = new(D, U, '27 · Dieta hiperproteica y necesidad de agua')
    kidney(s, 0.5, 1.15, 1.4, name='Riñón agua')
    f = s.shape(2.4, 1.2, 10.5, 1.3, 'rect', TAG, (INK, 1.5), SHD, 'Volumen urinario mínimo ≈ **osmoles a excretar** / **osmolalidad urinaria máxima**', 19, F_HEAD, INK, False, 'c', 'm', name='Fórmula volumen')
    ex = s.shape(2.4, 2.75, 10.5, 1.1, 'rect', CREAM, (INK, 1.25), SHD, 'Ejemplo teórico: 900 mOsm/d ÷ 1200 mOsm/kg ≈ **0,75 L/d** como mínimo. Con menor capacidad de concentración el volumen necesario **aumenta**.', 15, F_BODY, INK, False, 'c', 'm', name='Ejemplo')
    k1 = card(s, 0.4, 4.1, 6.1, 3.0, '- Más proteína que excede la síntesis → ↑ **urea** y otros solutos: mayor **carga osmótica**.\n- Hidratación suficiente ayuda a excretarla (ejercicio, calor).\n- **No** implica beber litros excesivos ni que el agua «neutralice» una insuficiencia renal.', LBLUE, 14, head='Fundamento renal')
    k2 = card(s, 6.8, 4.1, 6.1, 1.6, 'Proteínas animales ricas en AA **azufrados** ↑ ácidos fijos y la **carga ácida** renal.', LSALMON, 14, head='Ácido–base')
    k3 = card(s, 6.8, 5.85, 6.1, 1.25, 'No intercambiar: urea sérica · excreción de urea · volumen urinario · osmoles · **TFG**.', YEL, 13.5)
    s.step(fade(f)); s.step(fade(ex)); s.step(fade(k1)); s.step(fade(k2)); s.step(fade(k3))
    s.note('Cuando el aporte proteico excede la síntesis y renovación, aumentan la desaminación y la producción de urea; los '
           'riñones deben eliminar una mayor carga osmótica. El volumen mínimo de orina depende de los osmoles a excretar dividido '
           'la osmolalidad urinaria máxima: por ejemplo, 900 mOsm/d requerirían al menos 0,75 L si se alcanzan 1200 mOsm/kg; con '
           'menor capacidad de concentración el volumen necesario será mayor. Es un ejemplo teórico: esas cifras dependen de edad, '
           'función renal, ADH y contexto. En enfermedad renal se individualizan las necesidades proteicas, hídricas y '
           'electrolíticas.')


def t28(D):
    s = new(D, U, '28 · Inanición y ciclo de la urea: una afirmación con matiz temporal')
    cats = ['Día 1', 'Día 2', 'Día 3', 'Día 5', 'Semana 2', 'Semana 4', 'Agotamiento de grasa']
    ch = chart_line(s, 0.4, 1.1, 7.6, 6.0, cats, [('Excreción de N / urea (relativa)', [6, 9, 8, 6, 4, 3.2, 8])], ['0F7C7C'],
                    ytitle='Nivel relativo (esquema)', name='Curva tres fases', legend=False, size=13, ymax=10)
    p1 = card(s, 8.3, 1.1, 4.6, 1.85, '**Fase 1**: proteólisis para GNG → **↑ urea** e inducción de enzimas ureogénicas.', LSALMON, 14, head='Inicio')
    p2 = card(s, 8.3, 3.1, 4.6, 1.85, '**Fase 2**: adaptación cetónica → **ahorro nitrogenado**, ↓ excreción de urea.', MINT, 14, head='Adaptación')
    p3 = card(s, 8.3, 5.1, 4.6, 2.0, '**Fase 3**: si se **agota la grasa**, fracasa el ahorro proteico y vuelve a intensificarse la proteólisis.', RED, 14, color=WHITE, head='Terminal')
    s.step(fade(ch)); s.step(fade(p1)); s.step(fade(p2)); s.step(fade(p3))
    s.note('Al iniciarse un ayuno prolongado, parte de la glucosa necesaria surge de esqueletos carbonados de aminoácidos '
           'musculares (alanina, glutamina); su desaminación aumenta la carga de nitrógeno al hígado, eleva el flujo de urea y puede '
           'inducir enzimas ureogénicas; también se regula NAG/CPS1. Pero no sube indefinidamente: con varios días de ayuno el SNC '
           'utiliza cantidades crecientes de cetonas, se conserva proteína y disminuye la excreción urinaria de nitrógeno respecto '
           'del pico inicial. La afirmación "la inanición aumenta las enzimas de la urea" solo es adecuada si se aclara la fase y '
           'si se habla de actividad o de expresión. En etapas terminales por agotamiento de grasa vuelve a intensificarse la '
           'proteólisis. La curva es conceptual (sin valores medidos).')


def t29a(D):
    s = new(D, U, '29 · Glutamina: moneda de carbono, nitrógeno y ácido–base')
    data = [('liver', 'HEPATOCITO', '- **Glutaminasa** periportal → NH_{4}^{+} para urea\n- **GS** perivenosa captura NH_{4}^{+}\n- Balance neto según pH y nutrición', MINT),
            ('gut', 'ENTEROCITO', '- Combustible y precursor de nucleótidos\n- Glutaminasa → glutamato → α-KG\n- Produce NH_{3}, citrulina', LSALMON),
            ('muscle', 'MÚSCULO', '- **GS** incorpora N en glutamina\n- La exporta a riñón e intestino\n- Transporte seguro de NH_{3}', LSALMON),
            ('astro', 'ASTROCITO–NEURONA', '- GS astroglial recicla glutamato/GABA\n- En hiperamonemia: **edema** y disfunción', LILAC),
            ('kidney', 'RIÑÓN (TÚBULO PROXIMAL)', '- Glutaminasa + GDH → **2 NH_{4}^{+}**\n- **HCO_{3}^{−} nuevo** y gluconeogénesis\n- Clave en **acidosis** y ayuno', LBLUE),
            ('tumor', 'RECAMBIO RÁPIDO', '- Linfocitos, intestino, algunos tumores\n- N para purinas/pirimidinas; anaplerosis\n- No deducir «alimenta al tumor»', YEL)]
    ids = organ_tiles(s, data, cols=3, tw=4.1, th=2.9, size=14.5)
    for g in ids:
        s.step(fade(g))
    s.note('Glutamina en distintos órganos. Hepatocito: la glutaminasa periportal libera NH4+ para la ureogénesis y la GS '
           'perivenosa captura el amonio residual; el hígado decide netamente producir o consumir glutamina según el balance '
           'ácido–base y el estado nutricional. Enterocito: combustible y precursor de nucleótidos; glutaminasa → glutamato → '
           'α-cetoglutarato; produce NH3 y citrulina (la suplementación clínica rutinaria requiere evidencia específica). Músculo: '
           'captura nitrógeno en glutamina mediante GS, sobre todo en estados catabólicos. Astrocito–neurona: recicla '
           'glutamato/GABA; en hiperamonemia la glutamina se acumula. Riñón: glutaminasa y GDH generan NH4+ y bicarbonato nuevo. '
           'Tejidos de recambio rápido: N para purinas/pirimidinas y anaplerosis; no deducir que la glutamina alimente '
           'selectivamente al tumor ni que siempre convenga restringirla.')


def t29b(D):
    s = new(D, U, '29 · Amoniogénesis renal: excretar ácido y crear bicarbonato', 'RUTA ANIMADA')
    s.shape(0.3, 1.05, 8.6, 0.85, 'rect', ('a', 'F9E79F', 70), ('B7950B', 1.0), False, 'LUZ TUBULAR (orina)', 13, F_HEAD, '7E5109', True, 'c', 'm', name='Luz')
    tubule_cell(s, 0.3, 1.85, 8.6, 4.2, name='Célula túbulo proximal')
    vessel(s, 0.3, 6.15, 8.6, 0.85, name='Capilar peritubular', rbcs=3)
    mt = s.shape(1.9, 3.0, 4.6, 2.3, 'ellipse', ('a', 'F8C471', 70), ('B9770E', 2.0), False, name='Mitocondria')
    gq = mol(s, 2.2, 6.25, 'gln', d=0.5, name='Glutamina sangre')
    c = chain(s, 2.6, 3.2, ['Glutamina', 'Glutamato', 'α-cetoglutarato'], dy=0.7, w=1.9, enzymes=['glutaminasa', 'GDH'], rev=[False, True], fill=[MINT, MINT, YEL], name='Amoniogénesis', h=0.42, size=13)
    n1 = mol(s, 5.0, 3.55, 'nh4', d=0.42, name='NH4 1'); n2 = mol(s, 5.0, 4.25, 'nh4', d=0.42, name='NH4 2')
    nhe = chip(s, 6.6, 2.0, 'NHE3 / secreción', LBLUE, 12, name='NHE3')
    gl = mol(s, 6.8, 5.5, 'glc', d=0.45, name='Glucosa renal'); bi = chip(s, 7.35, 5.55, '2 HCO_{3}^{−}', LBLUE, 12.5, name='Bicarbonato')
    a1 = s.arrow([(4.5, 4.9), (6.8, 5.6)], ACT, 2.5)
    k = card(s, 9.2, 1.1, 3.7, 6.0, '- **Glutaminasa** → glutamato + NH_{4}^{+}; **GDH** → α-KG + NH_{4}^{+}.\n- El **NH_{4}^{+}** se excreta en la orina (**ácido neto**).\n- El esqueleto carbonado genera **HCO_{3}^{−} nuevo** y **glucosa**.\n- La **acidosis** aumenta la amoniogénesis.', CREAM, 14)
    s.step(fade(gq), path(gq, 0.5, -2.95, after=True, dur=1400))
    chain_anim(s, c, per_click=3)
    s.step(zoom(n1), zoom(n2, after=True), fade(nhe), path(n1, 1.8, -2.6, after=True, dur=1300), path(n2, 2.3, -3.25, dur=1400))
    s.step(wipe(a1, 'l'), zoom(gl, after=True), fade(bi), path(bi, 0.0, 0.85, after=True, dur=900))
    s.step(fade(k))
    s.note('Riñón (túbulo proximal): la glutamina de la sangre entra a la célula y a la mitocondria; la glutaminasa produce '
           'glutamato + NH4+ y la GDH α-cetoglutarato + NH4+. El NH4+ se secreta a la luz (por NHE3 y otros mecanismos) y se '
           'excreta: es un mecanismo crucial de excreción de ácido neto. El metabolismo del esqueleto carbonado (α-KG → '
           'gluconeogénesis) genera bicarbonato nuevo que vuelve a la sangre. Es especialmente relevante en acidosis y ayuno. '
           'La animación sigue la glutamina desde el capilar hasta la orina (NH4+) y la sangre (glucosa y HCO3−).')


def t30(D):
    s = new(D, U, '30 · Gluconeogénesis renal en el ayuno prolongado')
    kidney(s, 0.4, 1.1, 2.6, name='Riñón GNG')
    co = card(s, 3.4, 1.1, 4.6, 2.2, '- **Corteza** (túbulo proximal): lactato → piruvato; **glutamina** → α-KG → OAA; **glicerol** → DHAP.\n- **PC, PEPCK (PCK1/PCK2), FBPasa, G6Pasa**.', MINT, 13.5, head='Corteza: produce glucosa')
    me = card(s, 3.4, 3.5, 4.6, 1.6, '**Médula**: metabolismo más **glucolítico** → **lactato**. Evitar decir «todo el riñón hace glucosa».', LSALMON, 13.5, head='Médula: consume glucosa')
    ab = card(s, 8.3, 1.1, 4.6, 4.0, '- La glutaminólisis forma **NH_{4}^{+}** (orina) y **HCO_{3}^{−}** nuevo (sangre).\n- La **acidosis** aumenta amoniogénesis y uso de glutamina.\n- El riñón **prefiere excretar N como NH_{4}^{+}** para eliminar ácido; el hígado, como urea.', CREAM, 13.5, head='Acoplamiento ácido–base')
    pr = card(s, 0.4, 5.3, 12.5, 1.8, 'La **contribución renal** a la producción sistémica de glucosa **aumenta relativamente con el ayuno** y puede ser considerable; las proporciones exactas dependen del método. **Clínica**: la insuficiencia renal altera la homeostasis glucémica (menor GNG, menor eliminación de **insulina**), con efectos netos no predecibles por una sola variable.', YEL, 13.5)
    s.step(fade(co)); s.step(fade(me)); s.step(fade(ab)); s.step(fade(pr))
    s.note('La corteza renal, especialmente el túbulo proximal, realiza gluconeogénesis: lactato → piruvato; glutamina → '
           'glutamato → α-cetoglutarato → intermediarios de Krebs → oxaloacetato; glicerol → DHAP. Piruvato carboxilasa, PEPCK '
           '(PCK1/PCK2), FBPasa y G6Pasa permiten liberar glucosa. La contribución renal aumenta relativamente con el ayuno. '
           'Acoplamiento ácido–base: la glutaminólisis forma NH4+ (orina) y HCO3− nuevo (sangre); la acidosis aumenta la '
           'amoniogénesis. La médula renal es más glucolítica y produce lactato. La insuficiencia renal puede alterar la '
           'homeostasis glucémica por menor gluconeogénesis y menor eliminación de insulina, entre otros mecanismos.')


def n_compare(D):
    s = new(D, U, 'Distinciones clave del metabolismo del nitrógeno')
    rows = [['', 'Ureogénesis', 'Amoniogénesis'],
            ['Órgano', '**Hígado** (zona periportal)', '**Riñón** (túbulo proximal)'],
            ['Producto excretado', '**Urea** (neutra)', '**NH_{4}^{+}** urinario'],
            ['Sustrato principal', 'NH_{4}^{+} + aspartato + HCO_{3}^{−}', '**Glutamina**'],
            ['Efecto ácido–base', 'Consume HCO_{3}^{−}', 'Excreta ácido y genera **HCO_{3}^{−} nuevo**'],
            ['Estímulo', 'Carga proteica, catabolismo', '**Acidosis**, ayuno prolongado']]
    t1, H1 = table(s, 0.4, 1.1, 7.0, rows, [1.9, 2.55, 2.55], size=13.5, rowh=0.55, name='Tabla urea amonio')
    rows2 = [['', 'Glutaminasa', 'Glutamina sintetasa'],
             ['Reacción', 'Gln → Glu + NH_{4}^{+}', 'Glu + NH_{4}^{+} + **ATP** → Gln'],
             ['Dónde', 'Hígado periportal, riñón, intestino, neurona', 'Hígado perivenoso, músculo, astrocito'],
             ['Función', '**Libera** NH_{4}^{+}', '**Captura** NH_{4}^{+} (alta afinidad)']]
    t2, H2 = table(s, 7.7, 1.1, 5.2, rows2, [1.2, 2.0, 2.0], size=13, rowh=0.55, name='Tabla GS glutaminasa')
    p = note_box(s, 7.7, 1.3 + H2, 5.2, 1.3, 'Dos enzimas **opuestas** sobre el mismo par glutamato/glutamina: no confundirlas.', 15)
    s.step(fade(t1)); s.step(fade(t2)); s.step(fade(p))
    s.note('Distinciones obligatorias: ureogénesis (hígado, urea, consume bicarbonato) frente a amoniogénesis (riñón, NH4+, '
           'genera bicarbonato nuevo); glutaminasa (libera NH4+) frente a glutamina sintetasa (captura NH4+ gastando ATP).')


def build(D):
    div(D)
    m5a(D); m5b(D); m5c(D); m5d(D); m5e(D)
    t25_zone(D); t25_urea(D); t25_krebs(D); t25_ctrl(D)
    t26(D); t27(D); t28(D); t29a(D); t29b(D); t30(D); n_compare(D)
