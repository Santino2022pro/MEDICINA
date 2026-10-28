# -*- coding: utf-8 -*-
"""UNIDAD V (parte 1): enzimología clínica abdominal, hepatocito y transaminasas (Morph), De Ritis, FAL, GGT,
bilirrubina, colestasis (Morph)."""
from plantillas import *


def divisor_u5(D):
    def arte(s):
        g = s.group_start('Arte unidad V')
        arbol_biliar(s, 6.9, 0.6, 6.2, 6.3)
        s.group_end()
        return g
    divisor(D, 5, 'V', 'Pancreatitis aguda, biomarcadores hepatopancreáticos y diagnóstico diferencial', 'Leer el perfil enzimático para ubicar el daño',
            ['Enzimología clínica abdominal', 'Transaminasas y De Ritis', 'FAL, GGT y bilirrubina', 'Colestasis', 'Amilasa y lipasa', 'Zimógenos y pancreatitis',
             'Caso de pancreatitis', 'Caso de hepatitis', 'Diagnóstico diferencial'], arte, src=['PA 1 Marco conceptual'])


def marco(D):
    s = nueva(D, 5, 'Enzimología clínica abdominal: cada tejido, un perfil', src=['PA 1 Marco conceptual'], tipo='der', c1=NARANJA, c2=BLANCO)
    org = []
    for k, (fn, t, enz_, x) in enumerate(((lambda s, x: liver(s, x, 1.6, 2.6, name='Hígado perfil'), 'Hígado', 'ALT · AST · LDH', 0.4),
                                          (lambda s, x: s.free(x + 0.5, 1.4, 1.2, 1.9, smooth([(300, 0), (800, 80), (950, 600), (600, 1000), (200, 900), (80, 400)]),
                                                               shade('8DB255', 0.4, 0.3), ('4E6B22', 1.5), name='Vesícula perfil'), 'Vías biliares', 'FAL · GGT', 3.4),
                                          (lambda s, x: pancreas(s, x, 1.9, 2.6, name='Páncreas perfil'), 'Páncreas', 'Amilasa · lipasa', 5.95))):
        g = s.group_start('Perfil ' + t)
        fn(s, x)
        rotulo(s, x + 0.2, 3.65, t, NAVY, 15, w=2.3)
        rotulo(s, x + 0.2, 4.25, enz_, AMA, 14, w=2.3)
        org.append(s.group_end())
    c = caja(s, 0.4, 5.0, 8.4, 2.05, 'Cada tejido tiene un **perfil enzimático** particular. Cuando se daña, sus enzimas pasan a la sangre en cantidades medibles: interpretarlas permite **localizar el daño**.',
             BLANCO, 15.5, name='Perfil texto')
    rg = caja(s, 9.35, 1.2, 3.7, 5.85, '**Un solo biomarcador no dice nada.** La integración de **varios biomarcadores + síntomas clínicos** es lo que permite el diagnóstico.', AMA, 17,
              head='Regla de oro', name='Regla de oro abdomen')
    for g in org:
        s.step(fade(g))
    s.step(fade(c))
    s.step(zoom(rg))


def mecanismos_liberacion(D):
    s = nueva(D, 5, 'Cuatro mecanismos de liberación enzimática', src=['PA 1.1 Mecanismo general de liberación'], tipo='bandas', c1=DURAZNO_CL, c2=CREMA)
    items = [('Pérdida de permeabilidad', 'Daño **leve** (ej.: hepatitis viral inicial): salen enzimas **citoplasmáticas** (en hígado, sobre todo **ALT**).', 'perm'),
             ('Necrosis celular completa', 'Daño **grave** (ej.: cirrosis, hepatocarcinoma): sale **todo**, incluidas enzimas **mitocondriales** (ALT y **AST**).', 'nec'),
             ('Obstrucción de conductos', 'Colestasis: sin daño celular directo inicial; la bilis no fluye → daño secundario; suben **FAL y GGT**.', 'obs'),
             ('Autodigestión pancreática', 'Los zimógenos se activan dentro del páncreas → necrosis → **amilasa y lipasa** a la sangre.', 'aut')]
    ids = []
    for k, (t, d, kind) in enumerate(items):
        x = 0.4 + (k % 2) * 6.35; y = 1.2 + (k // 2) * 2.95
        g = s.group_start('Mecanismo ' + t)
        caja(s, x, y, 6.15, 2.75, '', BLANCO, 12, lw=2.0)
        if kind == 'perm':
            s.shape(x + 0.25, y + 0.5, 1.8, 1.5, 'roundRect', ('lin', [(0, 'F5CBA7'), (100, 'E59866')], 90), ('A04000', 2.0, 'dash'), False, adj={'adj': 30000})
            for j in range(3):
                ficha(s, x + 2.15, y + 0.55 + j * 0.5, 'ALT', '2E86C1', w=0.7, h=0.36, size=10)
        elif kind == 'nec':
            s.shape(x + 0.25, y + 0.5, 1.8, 1.5, 'irregularSeal2', ('lin', [(0, '8E6E8E'), (100, '5B3E5B')], 90), ('1B0E24', 1.5), False)
            for j, (m, c) in enumerate((('ALT', '2E86C1'), ('AST', 'C0392B'), ('AST', 'C0392B'))):
                ficha(s, x + 2.15, y + 0.55 + j * 0.5, m, c, w=0.7, h=0.36, size=10)
        elif kind == 'obs':
            s.shape(x + 0.25, y + 0.95, 2.4, 0.6, 'rect', ('lin', [(0, 'A9DFBF'), (100, '27AE60')], 90), ('1E8449', 1.5), False)
            s.shape(x + 1.3, y + 0.85, 0.65, 0.8, 'ellipse', shade('7F8C8D', 0.4, 0.3), (INK, 1.25), False)
        else:
            pancreas(s, x + 0.1, y + 0.75, 2.5, name='Páncreas autodigestión')
            s.shape(x + 1.0, y + 0.55, 0.9, 0.9, 'irregularSeal1', ('a', ROJO, 60), None, False)
        texto(s, x + 3.0, y + 0.15, 3.0, 0.75, t, 17, NARANJA_OSC, True, 'l', 'm')
        texto(s, x + 3.0, y + 0.95, 3.0, 1.7, d, 13.5)
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))


# ---------------------------------------------------------------- hepatocito (Morph)
HP_TXT = {1: 'Hepatocito: dónde están la ALT y la AST', 2: 'Daño de membrana: sale la ALT', 3: 'Necrosis: sale también la AST mitocondrial'}


def escena_hep(D, st):
    s = nueva(D, 5, HP_TXT[st], tipo='der', c1=NARANJA, c2=BLANCO, morph=st > 1, src=['PA 2.1 GPT/ALT', 'PA 2.2 GOT/AST', 'PA 1.1 Mecanismo general de liberación'], tw=8.7)
    ids = {}
    ids['sin'] = vessel(s, 0.3, 5.75, 8.5, 0.95, name='!!Sinusoide', rbcs=6)
    ids['sinl'] = texto(s, 0.45, 6.75, 3.0, 0.32, 'sangre (sinusoide)', 12, '922B21', True, name='!!Rótulo sangre')
    pts = [(80, 120), (500, 30), (920, 110), (990, 520), (900, 930), (500, 990), (90, 920), (15, 500)]
    col = {1: 'E8A08A', 2: 'E8A08A', 3: '9B7B8B'}[st]
    ids['hep'] = s.free(1.2, 1.15, 6.4, 4.4, smooth(pts, True, 0.55), shade(col, 0.45, 0.25), (darken(col, 0.55), 2.5 if st < 2 else 2.5, 'dash' if st >= 2 else None),
                        SH_I, name='!!Hepatocito')
    ids['nuc'] = nucleus(s, 3.9, 2.55, 1.3, name='!!Núcleo hepatocito')
    ids['can'] = s.shape(7.1, 2.0, 0.35, 2.4, 'roundRect', ('lin', [(0, 'A9DFBF'), (100, '27AE60')], 0), ('1E8449', 1.25), False, name='!!Canalículo biliar', adj={'adj': 50000})
    mits = [(1.7, 1.75), (5.4, 1.65), (1.8, 3.95), (5.5, 3.95)]
    for k, (mx, my) in enumerate(mits):
        ids['m%d' % k] = mito(s, mx, my, 1.35, name='!!Mitocondria %d' % (k + 1))
    # ALT en citoplasma
    altp = {1: [(2.9, 1.8), (2.6, 3.2), (5.0, 3.15), (3.4, 4.5), (5.2, 2.6)], 2: [(2.9, 1.8), (2.4, 5.95), (4.2, 6.0), (6.1, 5.95), (5.2, 2.6)],
            3: [(1.2, 5.95), (2.4, 5.95), (4.2, 6.0), (6.1, 5.95), (7.3, 5.95)]}[st]
    for k, (x, y) in enumerate(altp):
        ids['alt%d' % k] = ficha(s, x, y, 'ALT', '2E86C1', w=0.68, h=0.36, size=10.5, name='!!ALT %d' % (k + 1))
    astp = {1: [(2.05, 1.85), (5.75, 1.75), (2.15, 4.05)], 2: [(2.05, 1.85), (5.75, 1.75), (2.15, 4.05)], 3: [(3.2, 5.95), (5.1, 5.95), (7.9, 5.95)]}[st]
    for k, (x, y) in enumerate(astp):
        ids['ast%d' % k] = ficha(s, x, y, 'AST', 'C0392B', w=0.68, h=0.36, size=10.5, name='!!AST %d' % (k + 1))
    return s, ids


def hepatocito_seq(D):
    ini = len(D.slides) + 1
    s, i = escena_hep(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 2.4, '**ALT (GPT)**: abundante en el **citoplasma** del hepatocito.', CELESTE, 16, head='Citoplasma', headfill=AZUL, name='Caja ALT ubic')
    c2 = caja(s, 9.35, 3.85, 3.7, 3.2, '**AST (GOT)**: principalmente **mitocondrial** (también citoplasmática, en menor proporción).', ROSA, 16, head='Mitocondria', headfill=ROJO,
              name='Caja AST ubic')
    s.step(fade(i['hep']), fade(i['nuc'], after=True), *[fade(i['m%d' % k], after=True) for k in range(4)], fade(i['can'], after=True), fade(i['sin'], after=True),
           fade(i['sinl'], after=True))
    s.step(*[fade(i['alt%d' % k], after=(k > 0)) for k in range(5)], fade(c, after=True))
    s.step(*[fade(i['ast%d' % k], after=(k > 0)) for k in range(3)], fade(c2, after=True))
    s, i = escena_hep(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Una **lesión de la membrana** plasmática basta para que salga la **ALT** (no requiere necrosis completa): por eso se eleva **precozmente** en la hepatitis.',
             CELESTE, 15, head='Permeabilidad', headfill=AZUL, name='Caja HP2')
    s.step(*[pulse(i['alt%d' % k], after=(k > 0)) for k in (1, 2, 3)])
    s.step(fade(c))
    s, i = escena_hep(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Con **necrosis** se destruyen las organelas: sale también la **AST mitocondrial**. Ejemplos: cirrosis, hepatocarcinoma, hepatitis alcohólica.', ROSA, 15,
             head='Necrosis', headfill=ROJO, name='Caja HP3')
    s.step(*[pulse(i['ast%d' % k], after=(k > 0)) for k in range(3)])
    s.step(fade(c))
    registrar_morph(D, ini, len(D.slides), 'Hepatocito: ubicación de ALT y AST → daño de membrana (sale ALT) → necrosis (sale AST)',
                    ['!!Hepatocito', '!!Núcleo hepatocito', '!!Mitocondria 1–4', '!!Canalículo biliar', '!!Sinusoide', '!!ALT 1–5', '!!AST 1–3'],
                    'Las fichas de ALT descienden desde el citoplasma al sinusoide; luego las de AST salen de las mitocondrias; la membrana pasa a trazo discontinuo y el hepatocito se oscurece.')


def alt(D):
    s = nueva(D, 5, 'ALT / GPT: la transaminasa más específica del hígado', src=['PA 2.1 GPT/ALT'], tipo='izq', c1=CELESTE, c2=BLANCO)
    rx = s.group_start('Reacción ALT')
    ficha(s, 0.5, 1.5, 'Alanina', '27AE60', w=1.6, h=0.5, size=14)
    texto(s, 2.15, 1.5, 0.4, 0.5, '+', 22, INK, True, 'c', 'm')
    ficha(s, 2.55, 1.5, 'α-cetoglutarato', 'F5B041', w=2.0, h=0.5, size=13)
    s.arrow([(1.6, 2.1), (1.6, 2.85)], INK, 3)
    enzima_globular(s, 2.0, 2.15, 1.3, 0.9, '2E86C1', 'ALT', 'ALT forma', size=14)
    ficha(s, 0.5, 3.1, 'Piruvato', 'F39C12', w=1.6, h=0.5, size=14)
    texto(s, 2.15, 3.1, 0.4, 0.5, '+', 22, INK, True, 'c', 'm')
    ficha(s, 2.55, 3.1, 'Glutamato', '16A085', w=2.0, h=0.5, size=14)
    s.group_end()
    lv = liver(s, 0.6, 4.2, 3.6, name='Hígado ALT')
    pts = [('Nombre', '**GPT** (glutámico-pirúvica transaminasa) = **ALT** (alanina aminotransferasa).'),
           ('Localización', 'Principalmente **citoplasma** del hepatocito.'),
           ('Especificidad', 'La **más específica del hígado** entre las transaminasas; preferida para el diagnóstico de **hepatitis**.'),
           ('Valores', 'Hombres < 40 UI/L; mujeres < 31–37 UI/L. En hepatitis viral aguda: **400–500 UI/L** (≈ 10 veces el VN).')]
    ids = [caja(s, 4.95, 1.2 + k * 1.47, 8.1, 1.32, '**%s**: %s' % (t, d), [CELESTE, BLANCO, 'EAF5EA', AMA][k], 15, anchor='m', name='ALT %s' % t) for k, (t, d) in enumerate(pts)]
    s.step(fade(rx))
    s.step(fade(lv))
    for g in ids:
        s.step(fade(g))


def ast(D):
    s = nueva(D, 5, 'AST / GOT: mitocondrial y no exclusivamente hepática', src=['PA 2.2 GOT/AST'], tipo='der', c1=NARANJA, c2=BLANCO)
    rx = s.group_start('Reacción AST')
    ficha(s, 0.5, 1.5, 'Aspartato', '58D68D', w=1.7, h=0.5, size=14)
    texto(s, 2.25, 1.5, 0.4, 0.5, '+', 22, INK, True, 'c', 'm')
    ficha(s, 2.65, 1.5, 'α-cetoglutarato', 'F5B041', w=2.0, h=0.5, size=13)
    s.arrow([(1.6, 2.1), (1.6, 2.85)], INK, 3)
    enzima_globular(s, 2.0, 2.15, 1.3, 0.9, 'C0392B', 'AST', 'AST forma', size=14)
    ficha(s, 0.5, 3.1, 'Oxalacetato', 'F39C12', w=1.7, h=0.5, size=14)
    texto(s, 2.25, 3.1, 0.4, 0.5, '+', 22, INK, True, 'c', 'm')
    ficha(s, 2.65, 3.1, 'Glutamato', '16A085', w=2.0, h=0.5, size=14)
    s.group_end()
    tej = s.group_start('Tejidos AST')
    liver(s, 4.9, 1.4, 1.9, name='h'); corazon_anat(s, 7.0, 1.2, 1.3, name='c', coronarias=False)
    muscle(s, 5.0, 2.8, 1.9, name='m', fibers=2); eritrocito(s, 7.3, 2.85, 0.9, name='e')
    s.group_end()
    c1 = caja(s, 0.4, 4.0, 8.4, 1.45, '**GOT** (glutámico-oxalacética transaminasa) = **AST**. Principalmente **mitocondrial**: se eleva cuando hay **necrosis**.', ROSA, 15.5, anchor='m',
              name='AST def')
    c2 = caja(s, 0.4, 5.65, 8.4, 1.4, 'También está en **músculo cardíaco, músculo esquelético y eritrocitos**: no es exclusivamente hepática.', BLANCO, 15.5, anchor='m', name='AST tejidos')
    c3 = caja(s, 9.35, 1.2, 3.7, 5.85, 'Por eso **GOT y GPT se piden juntas**: la combinación orienta al tejido de origen.', AMA, 17, anchor='m', name='Juntas GOT GPT')
    s.step(fade(rx))
    s.step(fade(c1))
    s.step(fade(tej), fade(c2, after=True))
    s.step(fade(c3))


def de_ritis(D):
    s = nueva(D, 5, 'Índice de De Ritis (AST/ALT)', src=['PA 2.2 Índice De Ritis', 'REV PA 2.2'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    f = s.group_start('!!Fórmula De Ritis')
    s.shape(0.5, 1.3, 4.2, 2.0, 'roundRect', AMA, (INK, 2.5), SH_I, adj={'adj': 12000})
    texto(s, 0.5, 1.4, 4.2, 0.7, 'AST (GOT)', 24, ROJO, True, 'c', 'm')
    s.arrow([(1.0, 2.3), (4.2, 2.3)], INK, 3, tail=None)
    texto(s, 0.5, 2.45, 4.2, 0.7, 'ALT (GPT)', 24, AZUL, True, 'c', 'm')
    s.group_end()
    bal = s.group_start('Balanza De Ritis')
    s.shape(2.2, 5.6, 0.8, 1.2, 'triangle', NAVY, (INK, 1.5), False)
    s.shape(0.6, 5.4, 4.0, 0.18, 'rect', NAVY, None, False, rot=-8)
    ficha(s, 0.5, 4.6, 'ALT', '2E86C1', w=1.1, h=0.55, size=15)
    ficha(s, 3.6, 4.3, 'AST', 'C0392B', w=0.9, h=0.45, size=13)
    s.group_end()
    rows = [['GOT/GPT', 'Interpretación (material)'], ['< 1 (GPT > GOT)', '**Hepatitis viral aguda**: daño de membrana → sale más ALT citoplasmática.'],
            ['> 1 (GOT ≥ GPT)', 'Necrosis hepática, cirrosis, hepatocarcinoma, hepatitis alcohólica: se rompen organelas → sale AST mitocondrial.'],
            ['> 2 con GOT > 300 UI/L', 'Altamente sugestivo de **hepatitis alcohólica** (la GOT raramente supera 300–400 UI/L).']]
    ids, H = tabla_filas(s, 5.1, 1.2, [2.4, 5.55], rows, rowh=0.95, size=14.5, name='Tabla De Ritis')
    r_ = rigor(s, 5.1, 1.4 + H, 7.95, 6.95 - (1.4 + H), 'El cociente **orienta**, no diagnostica: depende de valores absolutos, del tiempo de evolución y de fuentes extrahepáticas de AST (músculo, corazón, hemólisis). '
               'Siempre se interpreta con la clínica y el resto del perfil.', 13.5, name='Rigor De Ritis')
    s.step(zoom(f))
    s.step(fade(ids[0]), fade(ids[1], after=True), fade(bal, after=True))
    s.step(fade(ids[2]))
    s.step(fade(ids[3]))
    s.step(fade(r_))


def got_sin_higado(D):
    s = nueva(D, 5, 'AST elevada sin enfermedad hepática', src=['PA 2.2 GOT sin enfermedad hepática'], tipo='bandas', c1=LAVANDA, c2=ROSA)
    items = [('Infarto agudo de miocardio', 'AST del músculo cardíaco (Unidad IV).', 'cor'), ('Rabdomiólisis', 'AST del músculo esquelético.', 'mus'),
             ('Hemólisis', 'AST de los eritrocitos (Unidad III).', 'gr')]
    ids = []
    for k, (t, d, kind) in enumerate(items):
        x = 0.45 + k * 4.25
        g = s.group_start('AST fuente %d' % (k + 1))
        caja(s, x, 1.2, 4.0, 4.3, '', BLANCO, 12, lw=2.0)
        if kind == 'cor':
            corazon_anat(s, x + 1.1, 1.4, 1.8, name='c')
        elif kind == 'mus':
            muscle(s, x + 0.5, 1.7, 3.0, name='m', fibers=3)
        else:
            for j in range(3):
                eritrocito(s, x + 0.5 + j * 1.0, 1.9 + (j % 2) * 0.5, 0.95, name='e%d' % j)
        ficha(s, x + 1.55, 3.6, 'AST', 'C0392B', w=0.9, h=0.45, size=14)
        texto(s, x + 0.2, 4.2, 3.6, 0.5, t, 17, NARANJA_OSC, True, 'c')
        texto(s, x + 0.2, 4.7, 3.6, 0.7, d, 14, INK, False, 'c')
        ids.append(s.group_end())
    c = caja(s, 0.45, 5.75, 12.5, 1.3, 'Por eso **GOT y GPT se piden juntas**: una AST alta con ALT normal obliga a buscar el origen **fuera del hígado**.', AMA, 16, anchor='m', name='Conclusión AST')
    for g in ids:
        s.step(fade(g))
    s.step(fade(c))


def fal(D):
    s = nueva(D, 5, 'Fosfatasa alcalina (FAL): vía biliar y hueso', src=['PA 2.3 FAL'], tipo='der', c1=NARANJA, c2=BLANCO)
    rows = [['Tejido / situación', 'Causa de elevación'], ['Vías biliares / vesícula (colestasis)', 'Colecistitis, colangitis, obstrucción biliar: marcador **principal** de obstrucción.'],
            ['Hígado (canalículos biliares)', 'Hepatitis colestásica, cirrosis biliar primaria.'],
            ['Hueso (osteoblastos)', 'Crecimiento óseo (**niños: muy elevada = normal**), Paget, metástasis óseas, fracturas en consolidación, hiperparatiroidismo.'],
            ['Placenta', 'Embarazo, tercer trimestre: **elevada = normal**.']]
    ids, H = tabla_filas(s, 0.4, 1.2, [2.9, 5.5], rows, rowh=0.85, size=14, name='Tabla FAL')
    d = caja(s, 0.4, 1.4 + H, 8.4, 6.95 - (1.4 + H), 'Hidroliza ésteres de fosfato en medio **alcalino**. Rango adulto: **40–130 UI/L**. En niños se usan **rangos pediátricos** (actividad osteoblástica).', AMA, 15,
             anchor='m', name='Def FAL')
    il = s.group_start('Íconos FAL')
    s.free(9.6, 1.3, 1.1, 1.8, smooth([(300, 0), (800, 80), (950, 600), (600, 1000), (200, 900), (80, 400)]), shade('8DB255', 0.4, 0.3), ('4E6B22', 1.5))
    s.shape(11.0, 1.3, 0.5, 2.1, 'roundRect', shade('F8F9F9', 0.3, 0.2), ('7F8C8D', 1.5), False, adj={'adj': 50000})
    s.shape(10.8, 1.1, 0.9, 0.5, 'ellipse', shade('F8F9F9', 0.3, 0.2), ('7F8C8D', 1.5), False)
    s.shape(10.8, 3.2, 0.9, 0.5, 'ellipse', shade('F8F9F9', 0.3, 0.2), ('7F8C8D', 1.5), False)
    s.group_end()
    c = caja(s, 9.35, 4.0, 3.7, 3.05, 'Adultos: FAL elevada indica problema **biliar** (primero) u **óseo** (segundo).', BLANCO, 16, name='FAL adultos')
    s.step(fade(ids[0]), fade(il, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(d))
    s.step(fade(c))


def ggt(D):
    s = nueva(D, 5, 'GGT: el aliado para saber de dónde viene la FAL', src=['PA 2.4 GGT', 'REV PA 2.4'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    c1 = caja(s, 0.4, 1.2, 5.2, 2.4, '- Marcador de **colestasis** (junto con la FAL)\n- Muy sensible al **alcohol** (se eleva desproporcionadamente)\n- Presente en hígado, riñón, páncreas, intestino, próstata\n- **No está en el hueso**',
              BLANCO, 14.5, head='GGT', name='Def GGT')
    arb = s.group_start('Decisión FAL')
    caja(s, 6.0, 1.2, 3.0, 1.0, '**FAL elevada**', AMA, 18, align='c', anchor='m')
    s.arrow([(6.9, 2.25), (6.4, 2.9)], INK, 3); s.arrow([(8.1, 2.25), (8.6, 2.9)], INK, 3)
    caja(s, 5.6, 2.95, 2.0, 0.9, 'GGT **alta**', ROSA, 16, align='c', anchor='m')
    caja(s, 8.0, 2.95, 2.0, 0.9, 'GGT **normal**', 'EAF5EA', 16, align='c', anchor='m')
    s.arrow([(6.6, 3.9), (6.6, 4.45)], INK, 3); s.arrow([(9.0, 3.9), (9.0, 4.45)], INK, 3)
    caja(s, 5.6, 4.5, 2.0, 1.2, 'Origen **biliar / hepático**', ROSA, 15, align='c', anchor='m')
    caja(s, 8.0, 4.5, 2.0, 1.2, 'Origen **óseo**', 'EAF5EA', 15, align='c', anchor='m')
    s.group_end()
    ldh = caja(s, 0.4, 3.85, 5.2, 1.85, '**LDH** en el contexto abdominal: omnipresente y poco específica; en la hepatitis puede estar levemente elevada; marcador inespecífico de necrosis.', CREMA, 13.5,
               name='LDH abdominal')
    r_ = rigor(s, 0.4, 5.95, 12.65, 1.1, 'La GGT no es un marcador «vesicular» específico: refleja colestasis **hepatobiliar** en general (está en el epitelio biliar y en la membrana canalicular) y se induce por alcohol y fármacos.',
               13, name='Rigor GGT')
    bone = s.group_start('Hueso')
    s.shape(10.6, 1.4, 0.5, 2.6, 'roundRect', shade('F8F9F9', 0.3, 0.2), ('7F8C8D', 1.5), False, adj={'adj': 50000})
    s.shape(10.4, 1.2, 0.9, 0.5, 'ellipse', shade('F8F9F9', 0.3, 0.2), ('7F8C8D', 1.5), False)
    s.shape(10.4, 3.8, 0.9, 0.5, 'ellipse', shade('F8F9F9', 0.3, 0.2), ('7F8C8D', 1.5), False)
    texto(s, 10.1, 4.45, 2.9, 0.4, 'sin GGT', 15, ROJO, True, 'c')
    s.group_end()
    s.step(fade(c1))
    s.step(fade(bone))
    s.step(wipe(arb, 't', dur=900))
    s.step(fade(ldh))
    s.step(fade(r_))


def bilirrubina_pa(D):
    s = nueva(D, 5, 'Bilirrubina: fracciones y tipos de ictericia', src=['PA 2.6 Bilirrubina', 'PA 2.6 Ictericia por tipo', 'REV PA 2.6'], tipo='der', c1=NARANJA, c2=BLANCO)
    rows = [['Fracción', 'Equivalente', 'Cómo se mide', 'Significado'], ['Directa', 'Conjugada / soluble', 'Directamente (hidrosoluble)', 'Colestasis, hepatitis, obstrucción biliar'],
            ['Indirecta', 'No conjugada / insoluble', 'Se **calcula**: BT − BD (va unida a albúmina)', 'Hemólisis (problema prehepático)'],
            ['Total', 'Suma de ambas', 'Se mide en el laboratorio', 'Normal 0,2–1,2 mg/dL; ictericia > 2–3 mg/dL']]
    ids, H = tabla_filas(s, 0.4, 1.2, [1.3, 2.1, 2.5, 2.5], rows, rowh=0.75, size=13.5, name='Tabla bilirrubina PA')
    tipos = s.group_start('Tipos de ictericia')
    for k, (t, d, f) in enumerate((('Prehepática', 'BI ↑: hemólisis, incompatibilidad, neonatal', CREMA), ('Hepática', 'BD ↑: hepatitis, cirrosis', ROSA),
                                   ('Posthepática', 'BD ↑: obstrucción biliar; ictericia + coluria + acolia', 'EAF5EA'))):
        x = 0.4 + k * 2.85
        caja(s, x, 1.45 + H, 2.65, 6.95 - (1.45 + H), '**%s**\n%s' % (t, d), f, 14)
        if k < 2:
            s.arrow([(x + 2.67, 1.45 + H + 0.8), (x + 2.83, 1.45 + H + 0.8)], INK, 2.5)
    s.group_end()
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'La bilirrubina directa se determina con el **reactivo diazo** (reacción de van den Bergh). El **reactivo de Ehrlich** (p-dimetilaminobenzaldehído) se usa para el **urobilinógeno**, no para la bilirrubina.',
               13.5, name='Rigor reactivo')
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(tipos))
    s.step(fade(r_))


# ---------------------------------------------------------------- colestasis (Morph)
CO_TXT = {1: 'Circulación biliar normal', 2: 'Obstrucción del conducto: la bilis no fluye', 3: 'Consecuencias bioquímicas y clínicas de la colestasis'}


def escena_col(D, st):
    s = nueva(D, 5, CO_TXT[st], tipo='der', c1=NARANJA, c2=BLANCO, morph=st > 1, src=['PA 2.7 Tríada de la colestasis', 'PA 8 Anatomía de la obstrucción'], tw=8.7)
    ids = arbol_biliar(s, 0.3, 1.1, 8.6, 5.9)
    W, H = 8.6, 5.9
    if st == 1:
        ids['flujo'] = [s.shape(0.3 + W * fx - 0.11, 1.1 + H * fy - 0.11, 0.22, 0.22, 'ellipse', '27AE60', ('145A32', 0.75), False, name='!!Bilis %d' % k)
                        for k, (fx, fy) in enumerate(((0.39, 0.38), (0.42, 0.45), (0.445, 0.56), (0.455, 0.67), (0.465, 0.76)))]
    else:
        ids['flujo'] = [s.shape(0.3 + W * fx - 0.11, 1.1 + H * fy - 0.11, 0.22, 0.22, 'ellipse', '27AE60', ('145A32', 0.75), False, name='!!Bilis %d' % k)
                        for k, (fx, fy) in enumerate(((0.385, 0.37), (0.4, 0.4), (0.415, 0.43), (0.43, 0.47), (0.442, 0.52)))]
        ids['calc'] = s.shape(0.3 + W * 0.452 - 0.22, 1.1 + H * 0.62 - 0.2, 0.44, 0.4, 'ellipse', shade('7F8C8D', 0.4, 0.3), (INK, 1.25), False, name='!!Cálculo')
    if st == 3:
        ids['bd'] = [ficha(s, 2.2 + k * 0.85, 1.25, t, c, w=0.8, h=0.38, size=11, name='!!Marcador colestasis %d' % k)
                     for k, (t, c) in enumerate((('BD', '27AE60'), ('FAL', 'F39C12'), ('GGT', 'AF7AC5')))]
    return s, ids


def colestasis(D):
    ini = len(D.slides) + 1
    s, i = escena_col(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'La bilis se forma en el hígado, baja por los **conductos hepáticos**, se almacena en la **vesícula** (conducto cístico) y llega al **duodeno** por el **colédoco** y la **ampolla de Vater**, junto al conducto pancreático.',
             BLANCO, 14, head='Recorrido', name='Caja CO1')
    s.step(fade(i['higado']), fade(i['vesicula'], after=True), fade(i['duodeno'], after=True), fade(i['duo2']), fade(i['pancreas'], after=True))
    s.step(wipe(i['hepaticos'], 't'), wipe(i['cistico'], 'r', after=True), wipe(i['coledoco'], 't', after=True), wipe(i['wirsung'], 'r', after=True), zoom(i['ampolla'], after=True))
    s.step(*[fade(b, after=(k > 0)) for k, b in enumerate(i['flujo'])], fade(c, after=True))
    s, i = escena_col(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, '**Colestasis**: obstrucción o deterioro del flujo biliar (intra o extrahepática). La bilis **se acumula** por encima del obstáculo.', ROSA, 15, head='Obstrucción',
             headfill=ROJO, name='Caja CO2')
    s.step(zoom(i['calc']), pulse(i['calc'], after=True))
    s.step(fade(c))
    s, i = escena_col(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 2.3, 'Suben la **bilirrubina directa**, la **FAL** y la **GGT**; las transaminasas solo si hay daño hepático secundario.', AMA, 14.5, head='Laboratorio', name='Caja CO3')
    tri = caja(s, 9.35, 3.75, 3.7, 3.3, '**Ictericia** (BD a la sangre y los tejidos) · **coluria** (BD hidrosoluble filtra por el riñón: orina «color té») · **acolia** (sin bilis en el intestino: heces claras).',
               ROSA, 14, head='Tríada', headfill=ROJO, name='Tríada colestasis')
    s.step(*[zoom(b, after=(k > 0)) for k, b in enumerate(i['bd'])], fade(c, after=True))
    s.step(fade(tri))
    registrar_morph(D, ini, len(D.slides), 'Colestasis: circulación biliar normal → obstrucción por cálculo → acumulación de bilis y marcadores',
                    ['!!Higado', '!!Vesicula', '!!Conductos hepaticos', '!!Conducto cistico', '!!Coledoco', '!!Conducto pancreatico', '!!Ampolla de Vater', '!!Duodeno', '!!Pancreas',
                     '!!Bilis 0–4', '!!Cálculo', '!!Marcador colestasis 0–2'],
                    'Las gotas de bilis, que en el esquema normal descienden hasta la ampolla, se agolpan por encima del cálculo; aparecen las fichas BD, FAL y GGT.')


def triada(D):
    s = nueva(D, 5, 'Tríada de la colestasis: ictericia, coluria y acolia', src=['PA 2.7 Tríada de la colestasis', 'REV PA 2.7'], tipo='bandas', c1=CREMA, c2=DURAZNO_CL)
    items = [('ICTERICIA', 'La **bilirrubina directa** se vuelca a la sangre y se deposita en los tejidos: piel y mucosas **amarillas**.', 'ojo'),
             ('COLURIA', 'La BD es **hidrosoluble**: filtra por el riñón y colorea la orina de **marrón oscuro** («color té»).', 'orina'),
             ('ACOLIA', 'La bilis no llega al intestino: sin **estercobilina**, las heces son **blancas / color arcilla**.', 'heces')]
    ids = []
    for k, (t, d, kind) in enumerate(items):
        x = 0.45 + k * 4.25
        g = s.group_start('Tríada ' + t)
        caja(s, x, 1.2, 4.0, 4.6, '', BLANCO, 12, lw=2.0)
        if kind == 'ojo':
            s.shape(x + 0.8, 1.6, 2.4, 1.3, 'ellipse', shade('F7DC6F', 0.3, 0.2), (INK, 1.5), False)
            s.shape(x + 1.55, 1.8, 0.9, 0.9, 'ellipse', shade('5D4037', 0.3, 0.3), (INK, 1.0), False)
        elif kind == 'orina':
            s.shape(x + 1.35, 1.5, 1.3, 1.6, 'can', ('lin', [(0, 'A0522D'), (100, '6E2C00')], 0), (INK, 1.5), False)
        else:
            s.shape(x + 1.0, 1.7, 2.0, 1.1, 'ellipse', shade('F2F3F4', 0.2, 0.2), ('7F8C8D', 1.5), False)
        texto(s, x + 0.2, 3.2, 3.6, 0.55, t, 22, NARANJA_OSC, True, 'c')
        texto(s, x + 0.25, 3.8, 3.5, 1.9, d, 15, INK, False, 'c')
        ids.append(s.group_end())
    r_ = rigor(s, 0.45, 6.0, 12.5, 1.05, 'La acolia sugiere **obstrucción biliar completa** pero no es estrictamente patognomónica: también puede verse en colestasis intrahepática grave.', 13.5,
               name='Rigor acolia')
    for g in ids:
        s.step(fade(g))
    s.step(fade(r_))


def build(D):
    divisor_u5(D)
    marco(D)
    mecanismos_liberacion(D)
    hepatocito_seq(D)
    alt(D)
    ast(D)
    de_ritis(D)
    got_sin_higado(D)
    fal(D)
    ggt(D)
    bilirrubina_pa(D)
    colestasis(D)
    triada(D)
