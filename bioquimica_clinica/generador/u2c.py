# -*- coding: utf-8 -*-
"""UNIDAD II (parte 3): complejo piruvato deshidrogenasa (vista animada en una diapositiva + secuencia Morph)
y su regulación."""
from plantillas import *

E1B = (1.5, 3.3, 1.9, 1.7)
E2B = (3.3, 3.9, 2.3, 2.0)
E3B = (5.6, 3.3, 1.8, 1.6)
PIV = (4.45, 4.9)
ARM = {'rest': (4.45, 3.35), 'e1': (3.2, 3.95), 'coa': (3.95, 6.35), 'e3': (5.85, 4.05)}


def complejo(s, prefix='!!'):
    ids = {}
    ids['E1'] = enzima_globular(s, *E1B, 'E59866', 'E1', prefix + 'E1', size=18, seed=1)
    ids['E2'] = enzima_globular(s, *E2B, '82E0AA', 'E2', prefix + 'E2', size=18, seed=3)
    ids['E3'] = enzima_globular(s, *E3B, '85C1E9', 'E3', prefix + 'E3', size=18, seed=5)
    ids['TPP'] = ficha(s, 1.65, 4.62, 'TPP', 'F4D03F', w=0.8, h=0.38, size=12, name=prefix + 'TPP')
    return ids


def brazo_lipoilo(s, pos, red=False, prefix='!!'):
    end = ARM[pos]
    a = s.arrow([PIV, end], '1E8449', 4.5, tail=None, name=prefix + 'Brazo lipoílo')
    b = s.shape(end[0] - 0.3, end[1] - 0.3, 0.6, 0.6, 'ellipse', shade('F7DC6F' if not red else 'F5B041', 0.45, 0.2), ('7D6608', 1.5), False,
                'HS SH' if red else 'S–S', 9.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), name=prefix + 'Lipoato', fit=False)
    return a, b


PDH_TXT = {1: 'Complejo PDH: tres enzimas en la matriz mitocondrial', 2: 'Llegada del piruvato a E1', 3: 'Descarboxilación del piruvato en E1',
           4: 'Transferencia del grupo de 2 C al brazo lipoílo de E2', 5: 'Formación del acetil-CoA en E2', 6: 'Liberación del acetil-CoA',
           7: 'E3 reoxida el brazo lipoílo: FAD → FADH_{2}', 8: 'Formación de NADH: regeneración de E3', 9: 'Productos del complejo PDH', 10: 'Balance global del complejo PDH'}


def escena_pdh(D, st):
    s = nueva(D, 2, PDH_TXT[st], tipo='der', c1=VERDE_OSC, c2=BLANCO, morph=st > 1, src=['TM 10 Complejo PDH', 'TM 10.3 Ciclo de las tres enzimas'], tw=8.7)
    ids = {}
    ids['mito'] = mitocondria_grande(s, -0.45, 1.0, 9.55, 6.35, name='!!Mitocondria', crestas=True, prof=0.25)
    ids['mat'] = texto(s, 0.7, 5.95, 3.0, 0.4, 'MATRIZ MITOCONDRIAL', 13, '784212', True, name='!!Rótulo matriz')
    ids.update(complejo(s))
    arm = {1: 'rest', 2: 'rest', 3: 'rest', 4: 'e1', 5: 'coa', 6: 'coa', 7: 'e3', 8: 'e3', 9: 'rest', 10: 'rest'}[st]
    ids['arm'], ids['lip'] = brazo_lipoilo(s, arm, red=st in (5, 6))
    fadt = 'FADH_{2}' if st == 7 else 'FAD'
    ids['FAD'] = ficha(s, 6.15, 4.55, fadt, 'D4AC0D' if st == 7 else 'F4D03F', w=1.05, h=0.38, size=12, name='!!FAD')
    # sustrato que viaja
    sub = {1: ('Piruvato (3 C)', 0.35, 1.75, 2.0, 'F39C12'), 2: ('Piruvato (3 C)', 0.75, 2.75, 2.0, 'F39C12'),
           3: ('Hidroxietil-TPP (2 C)', 0.45, 2.75, 2.6, 'E59866'), 4: ('Acetilo (2 C)', 2.4, 3.1, 1.7, 'B7950B'), 5: ('Acetilo (2 C)', 3.1, 6.15, 1.7, 'B7950B')}
    if st in sub:
        t, x, y, w, c = sub[st]
        ids['sub'] = ficha(s, x, y, t, c, w=w, h=0.48, size=14, name='!!Sustrato')
    if st >= 3:
        cpos = {3: (0.75, 2.05), 4: (7.55, 2.55), 5: (7.55, 2.55), 6: (7.55, 2.55), 7: (7.55, 2.55), 8: (7.55, 2.55), 9: (6.95, 2.95), 10: (6.95, 2.95)}[st]
        ids['co2'] = ficha(s, cpos[0], cpos[1], 'CO_{2}', '95A5A6', w=0.95, h=0.45, size=14, name='!!CO2')
    if st >= 6:
        apos = {6: (6.6, 1.65), 7: (6.6, 1.65), 8: (6.6, 1.65), 9: (6.6, 1.75), 10: (6.6, 1.75)}[st]
        ids['acoa'] = ficha(s, apos[0], apos[1], 'Acetil-CoA', 'B7950B', w=1.9, h=0.5, size=15, name='!!AcetilCoA')
    if st >= 8:
        npos = {8: (7.35, 5.35), 9: (6.95, 2.35), 10: (6.95, 2.35)}[st]
        ids['nad'] = ficha(s, npos[0], npos[1], 'NADH', '1F618D', w=1.2, h=0.45, size=14, name='!!NAD')
    return s, ids


def pdh_vistazo(D):
    """diapositiva única con la secuencia de 10 clics"""
    s = nueva(D, 2, 'Complejo PDH: el mecanismo en diez pasos', tipo='der', c1=VERDE_OSC, c2=BLANCO, src=['TM 10 Complejo PDH', 'TM 10.3 Ciclo de las tres enzimas'], tw=8.7)
    mi = mitocondria_grande(s, -0.45, 1.0, 9.55, 6.35, name='Mitocondria vistazo', crestas=True, prof=0.25)
    cx = complejo(s, prefix='')
    grp = [cx['E1'], cx['E2'], cx['E3'], cx['TPP']]
    arm, lip = brazo_lipoilo(s, 'rest', prefix='')
    fad = ficha(s, 6.15, 4.55, 'FAD', 'F4D03F', w=1.05, h=0.38, size=12, name='FAD vistazo')
    pir = ficha(s, 0.35, 1.75, 'Piruvato (3 C)', 'F39C12', w=2.0, h=0.48, size=14, name='Piruvato vistazo')
    co2 = ficha(s, 1.0, 2.25, 'CO_{2}', '95A5A6', w=0.95, h=0.45, size=14, name='CO2 vistazo')
    dos = ficha(s, 1.75, 2.85, '2 C', 'E59866', w=0.8, h=0.45, size=14, name='Fragmento 2C vistazo')
    coa = ficha(s, 0.9, 6.3, 'CoA', '58D68D', w=0.95, h=0.45, size=14, name='CoA vistazo')
    acoa = ficha(s, 3.05, 6.25, 'Acetil-CoA', 'B7950B', w=1.9, h=0.5, size=15, name='Acetil-CoA vistazo')
    nad = ficha(s, 7.5, 5.4, 'NAD^{+}', '85C1E9', w=1.1, h=0.45, size=14, name='NAD+ vistazo')
    nadh = ficha(s, 7.5, 5.4, 'NADH', '1F618D', w=1.1, h=0.45, size=14, name='NADH vistazo')
    e1c = caja(s, 9.35, 1.2, 3.7, 2.15, '**E1** (con **TPP**, vitamina B_{1}) quita el CO_{2}: el piruvato (3 C) queda como un fragmento de **2 C** unido al TPP.', BLANCO, 14,
               head='Primera transformación', name='Caja E1 vistazo')
    e2c = caja(s, 9.35, 3.5, 3.7, 1.75, '**E2** (ácido lipoico + CoA) transfiere el grupo **acetilo** a la CoA → **acetil-CoA**.', 'EAF5EA', 14, head='Transferencia', name='Caja E2 vistazo')
    bal = caja(s, 9.35, 5.4, 3.7, 1.65, 'Piruvato + NAD^{+} + CoA → **acetil-CoA + NADH + CO_{2}**', AMA, 14.5, head='Balance', name='Balance vistazo')
    # clics
    s.step(fade(mi))                                                                   # 1 mitocondria
    s.step(*[zoom(g, after=(k > 0), dur=400) for k, g in enumerate(grp)], fade(arm, after=True), fade(lip), fade(fad), pulse(cx['E2'], after=True))   # 2 complejo
    s.step(fade(pir))                                                                  # 3 piruvato
    s.step(path(pir, 0.45, 1.05, dur=900))                                             # 4 entrada a E1
    s.step(pulse(cx['TPP']), out(pir, after=True), fade(dos), fade(co2), path(co2, -0.2, -0.9, after=True, dur=800))  # 5 descarboxilación
    s.step(fade(e1c))                                                                  # 6 cuadro explicativo
    s.step(path(dos, 1.15, 0.95, dur=900), pulse(lip, after=True))  # 7 siguiente etapa (brazo de E2)
    s.step(fade(coa), path(coa, 2.3, -0.05, after=True, dur=900), out(dos, after=True), out(coa), zoom(acoa), fade(e2c, after=True))  # 8 transferencia
    s.step(pulse(cx['E3']), colorear(fad, 'D4AC0D', after=True), fade(nad, after=True), out(nad, after=True), fade(nadh), colorear(fad, 'F4D03F', after=True))  # 9 productos
    s.step(fade(bal), pulse(acoa, after=True), pulse(nadh), pulse(co2))                 # 10 balance
    s.note('Clic 1 mitocondria · 2 complejo PDH · 3 piruvato · 4 entrada a E1 · 5 descarboxilación (CO2) · 6 cuadro E1 · 7 brazo lipoílo de E2 · '
           '8 CoA y formación de acetil-CoA · 9 E3: FAD → FADH2 → NADH · 10 balance global.')


def pdh_secuencia(D):
    ini = len(D.slides) + 1
    # 1
    s, i = escena_pdh(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, '**No es una enzima: son tres** (E1, E2, E3) organizadas en un complejo multienzimático en la **matriz mitocondrial**.', BLANCO, 15, head='Complejo',
             name='Caja PDH1')
    c2 = caja(s, 9.35, 4.45, 3.7, 2.6, 'E1: **TPP** · E2: **ácido lipoico + CoA** · E3: **FAD + NAD^{+}**', AMA, 15.5, head='Cofactores', name='Cofactores PDH1')
    s.step(fade(i['mito']), fade(i['mat'], after=True))
    s.step(*[zoom(i[k], after=(n > 0)) for n, k in enumerate(('E1', 'E2', 'E3'))], fade(i['TPP'], after=True), fade(i['arm']), fade(i['lip']), fade(i['FAD']))
    s.step(fade(i['sub']))
    s.step(fade(c))
    s.step(fade(c2))
    # 2
    s, i = escena_pdh(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, '**E1** es el componente **descarboxilante** del complejo. Su cofactor es el **pirofosfato de tiamina (TPP)**, derivado de la **vitamina B_{1}**: sin él la reacción es imposible.',
             'FDEBD0', 15, head='E1', headfill='E59866', name='Caja PDH2')
    r_ = rigor(s, 9.35, 4.85, 3.7, 2.2, 'Nombre de E1: **piruvato deshidrogenasa** (componente E1). «Piruvato descarboxilasa» designa otra enzima.', 13.5, name='Rigor E1')
    s.step(pulse(i['TPP']), pulse(i['E1'], after=True))
    s.step(fade(c))
    s.step(fade(r_))
    # 3
    s, i = escena_pdh(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.3, 'E1 quita el **grupo carboxilo**: sale **CO_{2}** y queda un fragmento de **2 carbonos** unido al TPP. El carbono «perdido» (3 C → 2 C) es el CO_{2}.',
             'FDEBD0', 15, head='Descarboxilación', headfill='E59866', name='Caja PDH3')
    s.step(zoom(i['co2']), pulse(i['co2'], after=True))
    s.step(fade(c))
    # 4
    s, i = escena_pdh(D, 4)
    c = caja(s, 9.35, 1.2, 3.7, 3.6, '**E2 (transacetilasa)** usa el **ácido lipoico** como un brazo que «barre» como un ventilador: recoge el fragmento de E1 y lo lleva como **grupo acetilo**.',
             'EAF5EA', 15, head='E2: brazo lipoílo', headfill=VERDE_OSC, name='Caja PDH4')
    r_ = rigor(s, 9.35, 5.05, 3.7, 2.0, 'Al pasar al lipoato, el fragmento se **oxida** a acetilo; el lipoato queda **reducido**.', 13.5, name='Rigor PDH4')
    s.step(pulse(i['lip']), fade(c, after=True))
    s.step(fade(r_))
    # 5
    s, i = escena_pdh(D, 5)
    coa = ficha(s, 0.8, 6.15, 'CoA', '58D68D', w=0.95, h=0.48, size=14, name='CoA libre')
    acoa = ficha(s, 2.95, 6.15, 'Acetil-CoA', 'B7950B', w=1.95, h=0.5, size=15, name='!!AcetilCoA')
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'La **coenzima A** «atrapa» el acetilo: E2 forma el **acetil-CoA**. El brazo lipoílo queda **reducido** (–SH HS–).', 'EAF5EA', 15,
             head='Acetil-CoA', headfill=VERDE_OSC, name='Caja PDH5')
    s.step(fade(coa))
    s.step(out(coa), out(i['sub'], after=False), zoom(acoa, after=True), pulse(i['lip'], after=True))
    s.step(fade(c))
    # 6
    s, i = escena_pdh(D, 6)
    c = caja(s, 9.35, 1.2, 3.7, 3.3, 'El acetil-CoA abandona el complejo. Para un nuevo ciclo, **E2 debe volver a oxidarse**: ese es el trabajo de **E3**.', AMA, 15.5,
             head='Problema', name='Caja PDH6')
    s.step(pulse(i['acoa']))
    s.step(fade(c))
    # 7
    s, i = escena_pdh(D, 7)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, '**E3 (dihidrolipoil deshidrogenasa)** reoxida el lipoato: los electrones pasan al **FAD**, que se reduce a **FADH_{2}**.', CELESTE, 15,
             head='E3', headfill=AZUL, name='Caja PDH7')
    nad = ficha(s, 7.35, 5.35, 'NAD^{+}', '85C1E9', w=1.2, h=0.45, size=14, name='!!NAD')
    s.step(pulse(i['FAD']), fade(c, after=True))
    s.step(fade(nad))
    # 8
    s, i = escena_pdh(D, 8)
    c = caja(s, 9.35, 1.2, 3.7, 3.3, 'El **FADH_{2}** cede sus electrones al **NAD^{+}** → **NADH**. E3 vuelve a tener FAD y E2 queda **oxidada y lista** para un nuevo ciclo.', CELESTE, 15,
             head='NADH', headfill=AZUL, name='Caja PDH8')
    r_ = rigor(s, 9.35, 4.75, 3.7, 2.3, 'El FAD permanece **unido a E3**: actúa como intermediario interno; el aceptor final del complejo es el **NAD^{+}**.', 13.5, name='Rigor FAD')
    s.step(pulse(i['nad']), fade(c, after=True))
    s.step(fade(r_))
    # 9
    s, i = escena_pdh(D, 9)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Por cada piruvato:\n- **1 acetil-CoA**\n- **1 NADH**\n- **1 CO_{2}**', 'EAF5EA', 17, head='Productos', headfill=VERDE_OSC, name='Caja PDH9')
    s.step(pulse(i['acoa']), pulse(i['nad'], after=True), pulse(i['co2'], after=True))
    s.step(fade(c))
    # 10
    s, i = escena_pdh(D, 10)
    eq = caja(s, 0.5, 1.3, 8.4, 1.0, 'Piruvato + NAD^{+} + CoA → Acetil-CoA + NADH + CO_{2}', AMA, 22, align='c', anchor='m', bold=True, name='Ecuación global')
    c = caja(s, 9.35, 1.2, 3.7, 2.8, 'Reacción **irreversible**: una vez formado el acetil-CoA, no puede volver a piruvato. Ocurre en la **matriz mitocondrial**.', ROSA, 15,
             head='Irreversible', headfill=ROJO, name='Caja PDH10')
    c2 = caja(s, 9.35, 4.25, 3.7, 2.8, 'Es el **punto de control** más importante entre la glucólisis y el ciclo de Krebs.', BLANCO, 15.5, name='Punto de control PDH')
    s.step(zoom(eq))
    s.step(fade(c))
    s.step(fade(c2))
    registrar_morph(D, ini, len(D.slides), 'Complejo piruvato deshidrogenasa: piruvato → E1 (TPP, descarboxilación) → brazo lipoílo de E2 → acetil-CoA → E3 (FAD → FADH2) → NADH → balance',
                    ['!!Mitocondria', '!!E1', '!!E2', '!!E3', '!!TPP', '!!Brazo lipoílo', '!!Lipoato', '!!FAD', '!!Sustrato', '!!CO2', '!!AcetilCoA', '!!NAD', '!!Rótulo matriz'],
                    'El sustrato se desplaza hacia E1; el brazo lipoílo gira entre E1, el sitio de la CoA y E3; el lipoato cambia de S–S a HS SH; el FAD cambia a FADH2 y regresa; '
                    'CO2, acetil-CoA y NADH migran a la zona de productos.')


def tres_enzimas(D):
    s = nueva(D, 2, 'Las tres enzimas del complejo y sus cofactores', src=['TM 10.2 Las tres enzimas', 'REV TM 10.2'], tipo='izq', c1=VERDE_CL, c2=BLANCO)
    rows = [['Enzima', 'Nombre', 'Cofactor esencial', 'Reacción que cataliza'],
            ['**E1**', 'Piruvato deshidrogenasa (componente descarboxilante)', 'TPP (tiamina pirofosfato, vitamina B_{1})', 'Descarboxilación oxidativa: sale CO_{2}; queda un fragmento de 2 C.'],
            ['**E2**', 'Dihidrolipoil transacetilasa', 'Ácido lipoico + CoA', 'Transfiere el acetilo a la CoA → acetil-CoA.'],
            ['**E3**', 'Dihidrolipoil deshidrogenasa', 'FAD y NAD^{+}', 'Reoxida el lipoato de E2: FAD → FADH_{2} → NAD^{+} → NADH.']]
    ids, H = tabla_filas(s, 0.4, 1.2, [1.0, 3.6, 3.2, 4.85], rows, rowh=0.95, size=15, name='Tabla enzimas PDH', col_fills=[None, None, None, None])
    ill = s.group_start('Mini complejo')
    enzima_globular(s, 0.6, 1.4 + H + 0.25, 1.4, 1.2, 'E59866', 'E1', 'E1 tabla', size=15)
    enzima_globular(s, 1.85, 1.6 + H + 0.35, 1.6, 1.4, '82E0AA', 'E2', 'E2 tabla', size=15, seed=3)
    enzima_globular(s, 3.3, 1.4 + H + 0.25, 1.4, 1.2, '85C1E9', 'E3', 'E3 tabla', size=15, seed=5)
    s.group_end()
    regla = caja(s, 5.0, 1.45 + H, 4.1, 6.95 - (1.45 + H), 'Enzimas «-deshidrogenasa»: se produce una **coenzima reducida** (NADH o FADH_{2}). En el complejo PDH, además, sale **CO_{2}** (3 C → 2 C).',
                 AMA, 14.5, head='Regla de las deshidrogenasas', name='Regla deshidrogenasas')
    r_ = rigor(s, 9.3, 1.45 + H, 3.75, 6.95 - (1.45 + H), 'La liberación de CO_{2} **no es universal** en las deshidrogenasas: ocurre en las **descarboxilaciones oxidativas** (como la PDH), no en todas (p. ej., malato deshidrogenasa).',
               13, name='Rigor deshidrogenasas')
    s.step(fade(ids[0]), fade(ill, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(regla))
    s.step(fade(r_))


def deficit_b1(D):
    s = nueva(D, 2, 'Déficit de vitamina B_{1}: el complejo se detiene', src=['TM 10.2 Deficiencia de B1', 'REV TM 10.2 B1'], tipo='der', c1=ROJO, c2=ROSA)
    cx = complejo(s, prefix='')
    tpp_x = s.shape(1.55, 4.5, 1.0, 0.62, 'rect', None, None, False, 'X', 30, F_HEAD, ROJO, True, 'c', 'm', (0, 0, 0, 0), name='Sin TPP', fit=False)
    pir = s.group_start('Acumulación')
    for k in range(5):
        ficha(s, 0.3 + (k % 3) * 1.0, 1.3 + (k // 3) * 0.6, 'Piruvato', 'F39C12', w=0.95, h=0.42, size=10.5, name='Pir acum %d' % k)
    for k in range(3):
        ficha(s, 3.6 + k * 1.05, 1.5, 'Lactato', '8E44AD', w=1.0, h=0.42, size=10.5, name='Lac acum %d' % k)
    s.group_end()
    no = s.group_start('Sin acetil-CoA')
    ficha(s, 5.2, 6.25, 'Acetil-CoA', 'D5DBDB', w=1.9, h=0.5, size=15)
    s.shape(5.05, 6.15, 2.2, 0.7, 'rect', None, None, False, 'X', 28, F_HEAD, ROJO, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    c1 = caja(s, 9.35, 1.2, 3.7, 3.0, 'Sin **tiamina (B_{1})** el complejo PDH no funciona: no se convierte piruvato en acetil-CoA → se **acumulan piruvato y lactato**.', BLANCO, 15,
              head='Mecanismo', name='Mecanismo B1')
    c2 = caja(s, 9.35, 4.45, 3.7, 2.6, 'Cuadro clínico vinculado: **Wernicke-Korsakoff**, muy relacionado con el **alcoholismo crónico**.', AMA, 15.5, head='Clínica', name='Clínica B1')
    for k in ('E1', 'E2', 'E3', 'TPP'):
        pass
    s.step(*[fade(cx[k], after=(n > 0)) for n, k in enumerate(('E1', 'E2', 'E3', 'TPP'))])
    s.step(zoom(tpp_x), colorear(cx['E1'], 'BFC9CA', after=True))
    s.step(fade(pir), fade(no, after=True), fade(c1, after=True))
    s.step(fade(c2))


# ---------------------------------------------------------------- regulación
def reg_escena(D, st):
    tt = {1: 'Regulación covalente: complejo activo (desfosforilado)', 2: 'Regulación covalente: complejo inactivo (fosforilado)'}[st]
    s = nueva(D, 2, tt, tipo='der', c1=VERDE_OSC, c2=BLANCO, morph=st > 1, src=['TM 11.1 Regulación covalente'], tw=8.7)
    ids = {}
    act = st == 1
    ids['E1'] = enzima_globular(s, 2.6, 2.6, 2.1, 1.85, 'E59866' if act else 'BFC9CA', 'E1', '!!E1', size=20, seed=1)
    ids['E2'] = enzima_globular(s, 4.4, 3.3, 2.4, 2.1, '82E0AA' if act else 'D5DBDB', 'E2', '!!E2', size=20, seed=3)
    ids['E3'] = enzima_globular(s, 6.4, 2.6, 1.95, 1.75, '85C1E9' if act else 'CCD1D1', 'E3', '!!E3', size=20, seed=5)
    ids['halo'] = s.shape(2.3, 2.2, 6.4, 3.5, 'ellipse', None, (VERDE_V if act else '7F8C8D', 4.0, 'dash'), False, name='!!Estado complejo')
    ids['est'] = rotulo(s, 3.55, 5.85, 'ACTIVO' if act else 'INACTIVO', VERDE_OSC if act else '7F8C8D', 22, w=2.9, h=0.7, name='!!Rótulo estado')
    ids['kin'] = enzima_globular(s, 0.3, 1.2, 1.9, 1.4, 'F5B041', 'PDH\nquinasa', '!!PDH quinasa', size=14, seed=7)
    ids['fos'] = enzima_globular(s, 0.3, 4.7, 1.9, 1.4, 'AED6F1', 'PDH\nfosfatasa', '!!PDH fosfatasa', size=14, seed=8)
    ppos = (1.85, 1.35) if act else (2.75, 2.45)
    ids['P'] = s.shape(ppos[0], ppos[1], 0.5, 0.5, 'ellipse', shade('F39C12', 0.4, 0.2), (INK, 1.25), False, 'P', 16, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
                       name='!!Fosfato', fit=False)
    return s, ids


def regulacion_cov(D):
    ini = len(D.slides) + 1
    s, i = reg_escena(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 2.6, '**PDH-quinasa**: **fosforila** el complejo (E1) → lo **inactiva**.', AMA, 16, head='Quinasa', name='Caja quinasa')
    c2 = caja(s, 9.35, 4.05, 3.7, 3.0, '**PDH-fosfatasa**: **desfosforila** el complejo → lo **activa**. Regla: **fosforilado = inactivo; desfosforilado = activo**.', CELESTE, 16,
              head='Fosfatasa', headfill=AZUL, name='Caja fosfatasa')
    s.step(*[fade(i[k], after=(n > 0)) for n, k in enumerate(('E1', 'E2', 'E3', 'halo', 'est'))])
    s.step(fade(i['kin']), fade(i['P'], after=True), fade(c, after=True))
    s.step(fade(i['fos']), fade(c2, after=True))
    s, i = reg_escena(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.3, 'Con el **fosfato** unido a E1, el complejo deja de convertir piruvato en acetil-CoA: la glucosa no avanza hacia el ciclo de Krebs.', ROSA, 15.5,
              head='Inactivo', headfill=ROJO, name='Caja inactivo')
    c2 = caja(s, 9.35, 4.75, 3.7, 2.3, 'La **fosfatasa** puede retirar el fosfato y **reactivarlo**.', CELESTE, 16, name='Reactivación')
    s.step(pulse(i['P']), fade(c, after=True))
    s.step(pulse(i['fos']), fade(c2, after=True))
    registrar_morph(D, ini, len(D.slides), 'Regulación covalente del complejo PDH: forma activa (desfosforilada) → forma inactiva (fosforilada)',
                    ['!!E1', '!!E2', '!!E3', '!!PDH quinasa', '!!PDH fosfatasa', '!!Fosfato', '!!Estado complejo', '!!Rótulo estado'],
                    'El fosfato pasa de la quinasa a E1; las enzimas del complejo cambian de color (activo → gris); el rótulo cambia de ACTIVO a INACTIVO.')


def moduladores(D):
    s = nueva(D, 2, 'Moduladores de la PDH-quinasa', src=['TM 11.2 Moduladores de la PDH-kinasa'], tipo='bandas', c1=ROSA, c2='EAF5EA')
    rows = [['Modulador (abundancia)', 'Efecto sobre la quinasa', 'Resultado', 'Lógica'],
            ['ATP', 'Activa', 'Complejo **inactivo**', 'Ya hay energía: no se necesita más acetil-CoA.'],
            ['NADH', 'Activa', 'Complejo **inactivo**', 'Es producto del complejo: retroalimentación negativa.'],
            ['Acetil-CoA', 'Activa (y además inhibe el complejo directamente)', 'Complejo **inactivo**', 'Doble freno por exceso de producto.'],
            ['ADP', 'Inhibe', 'Complejo **activo**', 'Poco ATP: se necesita energía.'],
            ['NAD^{+}', 'Inhibe', 'Complejo **activo**', 'Hay aceptor de electrones disponible.'],
            ['CoA libre', 'Inhibe', 'Complejo **activo**', 'Hay sustrato disponible.'],
            ['Piruvato', 'Inhibe', 'Complejo **activo**', 'Hay sustrato para procesar.']]
    ids, H = tabla_filas(s, 0.4, 1.2, [2.2, 3.4, 2.1, 4.85], rows, rowh=0.62, size=14, name='Tabla moduladores')
    for k, r in enumerate(ids):
        if k == 0:
            s.step(fade(r))
        elif k == 1 or k == 4:
            s.step(fade(r))
        else:
            s.anim[-1].append(fade(r, after=True))
    lg = caja(s, 0.4, 1.4 + H, 12.55, 6.95 - (1.4 + H), '**Mucho producto** (ATP, NADH, acetil-CoA) → frena · **mucho sustrato o necesidad de energía** (ADP, NAD^{+}, CoA, piruvato) → activa.', AMA, 16,
              anchor='m', name='Lógica moduladores')
    s.step(fade(lg))


def senales(D):
    s = nueva(D, 2, 'Señales fisiológicas que regulan el complejo PDH', src=['TM 11.2 Moduladores de la PDH-kinasa', 'REV TM 11.2'], tipo='izq', c1=VERDE_CL, c2=BLANCO)
    items = [('Hipoxia (bajo O_{2})', 'Activa la quinasa (vía **HIF-1α**) → complejo inactivo: sin O_{2} no funcionan el ciclo de Krebs ni la cadena respiratoria.', ROSA, 'kin'),
             ('Ayuno prolongado', 'Activa la quinasa → frena el metabolismo oxidativo de la glucosa.', ROSA, 'kin'),
             ('Corticoides (uso farmacológico)', 'Activan la quinasa → inhiben el metabolismo glucídico oxidativo.', ROSA, 'kin'),
             ('Insulina (post-ingesta)', 'Inhibe la quinasa → **activa** el complejo: después de comer se metaboliza la glucosa.', 'EAF5EA', 'fos'),
             ('Calcio (Ca^{2+})', 'Activa la **fosfatasa** → activa el complejo. Muy importante en el **músculo cardíaco** durante la contracción.', 'EAF5EA', 'fos')]
    ids = []
    for k, (t, d, f, tipo) in enumerate(items):
        y = 1.2 + k * 1.18
        g = s.group_start('Señal %d' % (k + 1))
        rotulo(s, 0.4, y + 0.25, t, ROJO if tipo == 'kin' else VERDE_OSC, 14, w=3.9, h=0.6)
        caja(s, 4.55, y, 6.0, 1.05, d, f, 14, anchor='m')
        ids.append(s.group_end())
    cor = corazon_anat(s, 10.75, 4.6, 2.2, name='Corazón PDH')
    r_ = rigor(s, 10.75, 1.2, 2.3, 3.2, 'HIF-1α actúa **induciendo la expresión** de la quinasa; la insulina actúa sobre todo **activando la fosfatasa**.', 12.5, name='Rigor señales')
    for g in ids:
        s.step(fade(g))
    s.step(fade(cor['g']), fade(cor['ci'], after=True), fade(cor['cd'], after=True))
    s.step(fade(r_))


def principio(D):
    s = nueva(D, 2, 'Principio general: sustrato frente a producto', src=['TM 11.2 Principio general'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    bal = s.group_start('!!Balanza')
    s.shape(4.1, 5.2, 0.9, 1.4, 'triangle', NAVY, (INK, 1.5), False)
    s.shape(1.0, 4.95, 7.1, 0.2, 'rect', NAVY, None, False)
    s.shape(0.6, 3.6, 2.6, 1.35, 'roundRect', ('a', 'D5F5E3', 80), (INK, 1.5), False, adj={'adj': 30000})
    s.shape(5.9, 3.6, 2.6, 1.35, 'roundRect', ('a', 'FADBD8', 80), (INK, 1.5), False, adj={'adj': 30000})
    s.group_end()
    sus = s.group_start('Sustratos')
    for k, (t, c) in enumerate((('Piruvato', 'F39C12'), ('CoA', '58D68D'), ('NAD^{+}', '85C1E9'), ('ADP', 'F8C471'))):
        ficha(s, 0.7 + (k % 2) * 1.25, 3.7 + (k // 2) * 0.6, t, c, w=1.15, h=0.45, size=12)
    s.group_end()
    pro = s.group_start('Productos')
    for k, (t, c) in enumerate((('Acetil-CoA', 'B7950B'), ('NADH', '1F618D'), ('ATP', 'FFC000'))):
        ficha(s, 6.0 + (k % 2) * 1.25, 3.7 + (k // 2) * 0.6, t, c, w=1.2, h=0.45, size=11.5)
    s.group_end()
    a = caja(s, 0.4, 1.2, 4.0, 2.1, '**Mucho sustrato** → **activa** la vía (activa el complejo / inhibe la quinasa).', 'EAF5EA', 16, name='Mucho sustrato')
    b = caja(s, 4.75, 1.2, 4.0, 2.1, '**Mucho producto** → **frena** la vía (frena el complejo / activa la quinasa).', ROSA, 16, name='Mucho producto')
    c = caja(s, 9.35, 1.2, 3.7, 5.85, 'Es la **retroalimentación negativa** que asegura el equilibrio metabólico: la vía responde a la **relación entre lo que entra y lo que sale**.', AMA, 16,
             head='Principio', name='Principio retro')
    s.step(fade(bal))
    s.step(fade(sus), fade(a, after=True))
    s.step(fade(pro), fade(b, after=True))
    s.step(fade(c))


def resumen_reg(D):
    s = nueva(D, 2, 'Resumen: PDH-quinasa frente a PDH-fosfatasa', src=['TM 11.3 Tabla resumen'], tipo='bandas', c1=AMA, c2=CELESTE)
    rows = [['', 'PDH-QUINASA', 'PDH-FOSFATASA'], ['Mecanismo', 'Fosforila el complejo (E1)', 'Desfosforila el complejo (E1)'], ['Efecto', 'Complejo **inactivo**', 'Complejo **activo**'],
            ['La activan', 'ATP, NADH, acetil-CoA, hipoxia (HIF-1α), ayuno, corticoides', 'Ca^{2+}, insulina'],
            ['La inhiben', 'ADP, NAD^{+}, CoA libre, piruvato, insulina', '—']]
    ids, H = tabla_filas(s, 3.55, 1.25, [1.8, 2.75, 2.25], rows, rowh=0.9, size=15, name='Tabla resumen PDH', col_fills=[None, 'FDEBD0', 'EAF2F8'])
    nota = caja(s, 3.55, 1.45 + H, 6.8, 6.95 - (1.45 + H), 'La **insulina** figura en ambas columnas: inhibe a la quinasa y favorece a la fosfatasa; en los dos casos el resultado es un complejo **activo**.',
                AMA, 15, name='Nota insulina')
    k = enzima_globular(s, 0.5, 1.5, 2.4, 1.9, 'F5B041', 'PDH\nquinasa', 'Quinasa resumen', size=16, seed=7)
    f = enzima_globular(s, 0.5, 4.3, 2.4, 1.9, 'AED6F1', 'PDH\nfosfatasa', 'Fosfatasa resumen', size=16, seed=8)
    pr = caja(s, 10.55, 1.25, 2.5, 5.8, '**Fosforilado = inactivo**\n\n**Desfosforilado = activo**', NAVY, 18, align='c', anchor='m', name='Regla de oro PDH')
    s.step(fade(ids[0]), fade(k, after=True), fade(f, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(nota))
    s.step(zoom(pr))


def build(D):
    tres_enzimas(D)
    pdh_vistazo(D)
    pdh_secuencia(D)
    deficit_b1(D)
    regulacion_cov(D)
    moduladores(D)
    senales(D)
    principio(D)
    resumen_reg(D)
