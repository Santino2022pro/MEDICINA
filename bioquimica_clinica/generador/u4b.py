# -*- coding: utf-8 -*-
"""UNIDAD IV (parte 2): biomarcadores cardíacos, liberación (Morph), cinética, reinfarto, seguimiento (Morph),
factores de riesgo e integración."""
from plantillas import *


def biomarcador(D):
    s = nueva(D, 4, 'Biomarcador: sensibilidad y especificidad en el IAM', src=['IAM 4.1 Concepto de biomarcador'], tipo='der', c1=AZUL, c2=BLANCO)
    cel = cardiomiocito(s, 0.4, 1.3, 4.6, 2.0, name='Cardiomiocito concepto')['g']
    vas = vessel(s, 0.3, 3.65, 8.5, 0.8, name='Vaso concepto', rbcs=7)
    mols = [ficha(s, 2.2 + k * 0.6, 2.4, m, c, w=0.55, h=0.36, size=10, name='Marcador %d' % k) for k, (m, c) in enumerate((('Tn', 'EC7063'), ('CK', 'F39C12'), ('Mb', 'C0392B')))]
    d = caja(s, 5.3, 1.2, 3.5, 2.2, 'Molécula medible en sangre u otros fluidos que refleja el estado fisiológico o patológico de un tejido.', AMA, 14, name='Def biomarcador')
    sn = caja(s, 0.4, 4.75, 4.1, 2.3, '**Sensibilidad**: detectar el IAM cuando existe (pocos falsos negativos). Un marcador muy sensible se eleva ante **cualquier daño muscular**.', ROSA, 14.5,
              name='Sensibilidad IAM')
    sp = caja(s, 4.7, 4.75, 4.1, 2.3, '**Especificidad**: ser positivo **solo** cuando hay daño miocárdico (pocos falsos positivos).', 'EAF5EA', 14.5, name='Especificidad IAM')
    c = caja(s, 9.35, 1.2, 3.7, 5.85, 'El biomarcador ideal sería **muy sensible y muy específico**. En la práctica, algunos son más sensibles (se elevan pronto, ante cualquier daño) y otros más específicos (solo ante daño cardíaco).',
             BLANCO, 15, head='Ideal', name='Ideal biomarcador')
    s.step(fade(cel), fade(vas, after=True))
    s.step(*[fade(m, after=(k > 0)) for k, m in enumerate(mols)], *[path(m, 0.2 * k, 1.55, after=(k == 0), dur=900) for k, m in enumerate(mols)], fade(d, after=True))
    s.step(fade(sn))
    s.step(fade(sp))
    s.step(fade(c))


def ck(D):
    s = nueva(D, 4, 'Creatín fosfoquinasa (CPK / CK)', src=['IAM 4.2 CPK'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    enz_ = enzima_globular(s, 1.2, 1.5, 2.4, 2.0, 'F39C12', 'CK', '!!CK', size=22, seed=4)
    r1 = s.group_start('Reacción CK')
    ficha(s, 4.9, 1.6, 'Creatina', 'AED6F1', w=1.6, h=0.5, size=14)
    ficha(s, 6.6, 1.6, 'ATP', 'FFC000', w=0.9, h=0.5, size=14)
    s.arrow([(7.6, 1.6), (8.3, 1.6)], INK, 2.5); s.arrow([(8.3, 2.0), (7.6, 2.0)], INK, 2.5)
    ficha(s, 8.4, 1.6, 'Creatín fosfato', '5DADE2', w=2.2, h=0.5, size=14)
    ficha(s, 10.7, 1.6, 'ADP', 'F8C471', w=0.9, h=0.5, size=14)
    s.group_end()
    c1 = caja(s, 4.9, 2.4, 8.15, 1.3, 'Es una **enzima**: fosforila la creatina a **creatín fosfato**, reserva energética rápida del músculo.', AMA, 16, anchor='m', name='Función CK')
    tej = s.group_start('Tejidos CK')
    muscle(s, 0.5, 4.3, 2.5, name='Músculo CK', fibers=2)
    corazon_anat(s, 3.2, 4.0, 1.3, name='Corazón CK', coronarias=False)
    brain(s, 4.7, 4.3, 1.8, name='Cerebro CK')
    s.group_end()
    c2 = caja(s, 6.85, 4.0, 6.2, 3.05, 'Presente en **todos los tejidos musculares y en el cerebro** → **alta sensibilidad** pero **baja especificidad** para el IAM.', ROSA, 16, anchor='m',
              name='Distribución CK')
    s.step(fade(enz_))
    s.step(fade(r1), fade(c1, after=True))
    s.step(fade(tej), fade(c2, after=True))


def isoenzimas(D):
    s = nueva(D, 4, 'Las tres isoenzimas de la CK', src=['IAM 4.2 Isoenzimas CPK'], tipo='der', c1=AZUL, c2=BLANCO)
    iso = []
    for k, (n, a, b, org, f) in enumerate((('CK-BB', 'B', 'B', 'Cerebro (brain)', 'D2B4DE'), ('CK-MM', 'M', 'M', 'Músculo esquelético (muscle)', 'F5B7B1'),
                                          ('CK-MB', 'M', 'B', 'Corazón: más MB que en músculo o cerebro', 'F9E79F'))):
        x = 0.5 + k * 2.9
        g = s.group_start('!!' + n)
        for j, sub in enumerate((a, b)):
            col = 'E74C3C' if sub == 'M' else '8E44AD'
            s.shape(x + 0.15 + j * 0.95, 1.5, 1.05, 1.05, 'ellipse', shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), False, sub, 20, F_HEAD, BLANCO, True, 'c', 'm',
                    (0, 0, 0, 0), fit=False)
        rotulo(s, x + 0.05, 2.75, n, NAVY, 16, w=2.2)
        texto(s, x, 3.35, 2.3, 0.9, org, 14, INK, True, 'c')
        iso.append(s.group_end())
    pie = s.group_start('Proporción corazón')
    s.shape(0.8, 4.55, 2.2, 2.2, 'pie', 'E74C3C', (INK, 1.25), False, adj={'adj1': 16200000, 'adj2': 10800000})
    s.shape(0.8, 4.55, 2.2, 2.2, 'pie', 'F4D03F', (INK, 1.25), False, adj={'adj1': 10800000, 'adj2': 14400000})
    s.shape(0.8, 4.55, 2.2, 2.2, 'pie', '8E44AD', (INK, 1.25), False, adj={'adj1': 14400000, 'adj2': 16200000})
    texto(s, 0.6, 6.8, 2.6, 0.3, 'corazón: MM > MB > BB (esquema)', 11.5, INK, True, 'c')
    s.group_end()
    c1 = caja(s, 3.4, 4.55, 5.4, 2.5, 'Las **tres isoenzimas** están en **los tres tejidos**: cambia la **proporción**. En el corazón la **MM sigue siendo la mayoritaria**, pero la **MB** es proporcionalmente más alta que en músculo o cerebro.',
              BLANCO, 14.5, name='Proporciones CK')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.0, '**Isoenzima**: cataliza la **misma reacción** con **distinta estructura** molecular.', AMA, 16, head='Definición', name='Def isoenzima')
    mn = caja(s, 9.35, 4.45, 3.7, 2.6, 'Mnemotecnia: **B = brain**, **M = muscle**; **MB** = mezcla → corazón.', CREMA, 16, name='Mnemotecnia CK')
    s.step(fade(c2))
    for g in iso:
        s.step(fade(g))
    s.step(fade(pie), fade(c1, after=True))
    s.step(fade(mn))


def ck_mb_sola(D):
    s = nueva(D, 4, 'Nunca CK-MB sola: el cociente con la CK total', src=['IAM 4.2 Regla CPK-MB', 'REV IAM 4.2'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    tr = s.group_start('Traumatismo muscular')
    muscle(s, 0.5, 1.4, 3.6, name='Músculo trauma', fibers=3)
    s.shape(1.6, 1.3, 1.0, 0.9, 'irregularSeal1', ROJO, (INK, 1.0), False)
    s.group_end()
    c1 = caja(s, 4.6, 1.2, 8.45, 1.5, 'La **CK-MB** también está en músculo esquelético y cerebro: una MB elevada aislada **no distingue** corazón de traumatismo muscular.', ROSA, 15.5, name='Problema MB')
    c2 = caja(s, 4.6, 2.9, 8.45, 1.25, 'Siempre se piden **juntas: CK total + CK-MB**.', AMA, 19, anchor='m', align='c', name='Juntas')
    bar = s.group_start('Barras cociente')
    for k, (t, tot, mb, col) in enumerate((('Músculo esquelético', 4.0, 0.12, 'F5B7B1'), ('Corazón', 2.6, 0.35, 'F9E79F'))):
        y = 4.6 + k * 1.15
        texto(s, 0.4, y + 0.1, 2.4, 0.5, t, 14.5, INK, True)
        s.shape(2.9, y, tot * 2.0, 0.65, 'rect', col, (INK, 1.25), False, 'CK total', 13, F_HEAD, INK, True, 'l', 'm', (0.1, 0, 0, 0))
        s.shape(2.9 + tot * 2.0 - tot * 2.0 * mb, y, tot * 2.0 * mb, 0.65, 'rect', ('lin', [(0, 'F4D03F'), (100, 'B7950B')], 0), (INK, 1.25), False, 'MB', 12, F_HEAD, INK, True,
                'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    r_ = rigor(s, 11.1, 4.35, 1.95, 2.7, 'El cociente depende del método (masa o actividad); hoy la **troponina** es el marcador de elección.', 12, name='Rigor cociente')
    c3 = rotulo(s, 7.3, 6.2, 'MB / CK total > 5–6 % → origen miocárdico', NAVY, 14, name='Cociente')
    s.step(fade(tr), fade(c1, after=True))
    s.step(fade(c2))
    s.step(wipe(bar, 'l'), fade(c3, after=True))
    s.step(fade(r_))


def troponinas(D):
    s = nueva(D, 4, 'Troponinas: proteínas del aparato contráctil', src=['IAM 4.3 Troponinas I y T'], tipo='der', c1=AZUL, c2=LAVANDA)
    t = sarcomero_troponina(s, 0.4, 1.4, 8.4, 2.6, name='!!Filamento delgado')
    act = rotulo(s, 0.5, 4.15, 'actina', '85C1E9', 14, name='Rótulo actina')
    tpm = rotulo(s, 2.0, 4.15, 'tropomiosina', 'D2B4DE', 14, name='Rótulo tropomiosina')
    ca = s.shape(4.6, 1.15, 0.5, 0.5, 'ellipse', shade('F4D03F', 0.4, 0.2), ('7D6608', 1.0), False, 'Ca^{2+}', 10, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), name='Calcio',
                 fit=False)
    rows = [['Subunidad', 'Función'], ['Troponina C (TnC)', 'Fija el **calcio**: la señal que desencadena la contracción.'],
            ['Troponina T (TnT)', 'Fija el complejo troponina a la **tropomiosina**.'], ['Troponina I (TnI)', 'Subunidad **inhibidora**: regula la interacción actina–miosina dependiente de Ca^{2+}.']]
    ids, H = tabla_filas(s, 0.4, 4.7, [2.3, 6.1], rows, rowh=0.55, size=14, name='Tabla troponinas')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Son **proteínas estructurales (no enzimas)**: los biomarcadores **más importantes y específicos** del IAM en la práctica actual.', AMA, 15,
             head='Concepto', name='Concepto Tn')
    s.step(fade(t['g']), fade(act, after=True), fade(tpm, after=True))
    s.step(zoom(t['TnT']), fade(ids[0], after=True), fade(ids[2], after=True))
    s.step(zoom(t['TnC']), fade(ca, after=True), path(ca, 0.45, 0.25, after=True), fade(ids[1], after=True))
    s.step(zoom(t['TnI']), fade(ids[3], after=True))
    s.step(fade(c))


def especificidad_tn(D):
    s = nueva(D, 4, '¿Por qué la troponina es tan específica del corazón?', src=['IAM 4.3 Especificidad troponinas'], tipo='bandas', c1=LAVANDA, c2=CELESTE)
    c1 = s.group_start('Isoforma cardíaca')
    s.shape(0.6, 1.6, 2.2, 1.6, 'ellipse', shade('EC7063', 0.4, 0.25), ('922B21', 1.5), False, 'cTnI\ncardíaca', 16, F_HEAD, INK, True, 'c', 'm')
    s.group_end()
    c2 = s.group_start('Isoforma esquelética')
    s.shape(10.5, 1.6, 2.2, 1.6, 'hexagon', shade('ABB2B9', 0.4, 0.25), ('5D6D7E', 1.5), False, 'TnI\nesquelética', 15, F_HEAD, INK, True, 'c', 'm', adj={'adj': 25000, 'vf': 115470})
    s.group_end()
    ab = s.group_start('Anticuerpo del laboratorio')
    s.arrow([(1.7, 4.6), (1.7, 3.9)], '2E86C1', 8, tail=None)
    s.arrow([(1.7, 3.9), (1.2, 3.35)], '2E86C1', 8, tail=None)
    s.arrow([(1.7, 3.9), (2.2, 3.35)], '2E86C1', 8, tail=None)
    texto(s, 0.4, 4.7, 2.7, 0.4, 'reconoce', 14, VERDE_OSC, True, 'c')
    s.group_end()
    no = s.group_start('No reconoce')
    s.arrow([(11.6, 4.6), (11.6, 3.9)], '7F8C8D', 8, tail=None)
    s.arrow([(11.6, 3.9), (11.1, 3.35)], '7F8C8D', 8, tail=None)
    s.arrow([(11.6, 3.9), (12.1, 3.35)], '7F8C8D', 8, tail=None)
    texto(s, 10.3, 4.7, 2.7, 0.4, 'no reconoce', 14, ROJO, True, 'c')
    s.group_end()
    t = caja(s, 3.55, 1.2, 6.5, 2.4, 'La **troponina I cardíaca (cTnI)** y la **troponina T cardíaca (cTnT)** son **estructuralmente distintas** de las isoformas del músculo esquelético.', AMA, 17,
             anchor='m', name='Isoformas')
    t2 = caja(s, 3.55, 3.85, 6.5, 2.0, 'El **anticuerpo** que usa el laboratorio reconoce **solo la isoforma cardíaca**: por eso son altamente específicas de miocardio.', BLANCO, 16.5, anchor='m',
              name='Anticuerpo')
    s.step(fade(c1), fade(c2, after=True), fade(t, after=True))
    s.step(fade(ab), fade(no, after=True), fade(t2, after=True))


def permeabilidad(D):
    s = nueva(D, 4, 'Pérdida de permeabilidad frente a necrosis', src=['IAM 4.3 Por qué la troponina aparece tarde', 'IAM 5.1 Regla de oro', 'REV IAM 4.3'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    a = s.group_start('Célula permeable')
    s.shape(0.4, 1.4, 4.0, 2.3, 'roundRect', ('lin', [(0, 'F5B7B1'), (100, 'EC9A90')], 90), ('7B241C', 2.5, 'dash'), False, adj={'adj': 30000})
    for k in range(4):
        ficha(s, 0.7 + k * 0.9, 1.9, 'CK', 'F39C12', w=0.6, h=0.36, size=10)
        ficha(s, 0.9 + k * 0.85, 2.6, 'Mb', 'C0392B', w=0.55, h=0.36, size=10)
    s.group_end()
    sale = [ficha(s, 4.5, 1.8 + k * 0.6, m, c, w=0.6, h=0.36, size=10, name='Sale %d' % k) for k, (m, c) in enumerate((('CK', 'F39C12'), ('Mb', 'C0392B'), ('CK', 'F39C12')))]
    b = s.group_start('Célula necrótica')
    s.shape(0.4, 4.4, 4.0, 2.3, 'roundRect', ('lin', [(0, '8E6E8E'), (100, '5B3E5B')], 90), ('1B0E24', 2.5, 'sysDash'), False, adj={'adj': 30000})
    sarcomero_troponina(s, 0.6, 4.9, 3.4, 1.2, name='Filamento roto')
    s.group_end()
    tnl = [ficha(s, 4.5, 4.8 + k * 0.6, t, 'EC7063', w=0.7, h=0.36, size=10, name='Tn libre %d' % k) for k, t in enumerate(('TnI', 'TnT', 'TnI'))]
    c1 = caja(s, 5.5, 1.2, 7.55, 2.6, 'Con **solo pérdida transitoria de permeabilidad** de la membrana salen las moléculas **citoplasmáticas pequeñas y solubles**: mioglobina y enzimas como la **CK**.',
              'FDEBD0', 15.5, name='Permeabilidad')
    c2 = caja(s, 5.5, 4.0, 7.55, 1.65, 'Las troponinas forman parte del aparato contráctil: para que aparezcan en sangre se necesita **necrosis** (ruptura de toda la estructura).', ROSA, 15,
              name='Necrosis Tn')
    r_ = rigor(s, 5.5, 5.85, 7.55, 1.2, 'Existe además una pequeña **fracción citosólica** de troponina que puede liberarse precozmente; la persistencia de 7–10 días se debe sobre todo a la **degradación lenta** del aparato contráctil.',
               12.5, name='Rigor pool Tn')
    s.step(fade(a))
    s.step(*[fade(x_, after=(k > 0)) for k, x_ in enumerate(sale)], fade(c1, after=True))
    s.step(fade(b))
    s.step(*[fade(x_, after=(k > 0)) for k, x_ in enumerate(tnl)], fade(c2, after=True))
    s.step(fade(r_))


def mioglobina(D):
    s = nueva(D, 4, 'Mioglobina: la más rápida, la menos específica', src=['IAM 4.4 Mioglobina', 'REV IAM 4.4'], tipo='der', c1=AZUL, c2=BLANCO)
    mb = s.group_start('!!Mioglobina')
    s.shape(0.8, 1.5, 2.2, 2.2, 'ellipse', shade('E57373', 0.4, 0.25), ('922B21', 1.5), False)
    s.shape(1.65, 2.35, 0.5, 0.5, 'diamond', 'C0392B', ('641E16', 1.0), False)
    texto(s, 0.6, 3.8, 2.6, 0.4, 'mioglobina (1 cadena, 1 hemo)', 13, '922B21', True, 'c')
    s.group_end()
    hb = hemoglobina(s, 3.5, 1.4, 2.3, name='Hb comparación')
    hl = texto(s, 3.3, 3.8, 2.7, 0.4, 'hemoglobina (4 cadenas)', 13, '922B21', True, 'c', name='Rótulo Hb comp')
    rows = [['Propiedad', 'Descripción'], ['Función', 'Almacena y transporta O_{2} intramuscular'], ['Localización', 'Músculo esquelético + miocardio (no específica)'],
            ['Tamaño', 'Muy pequeña: aparece rápido y filtra rápido por el riñón'], ['Sensibilidad / especificidad', 'Altísima / muy baja']]
    ids, H = tabla_filas(s, 0.4, 4.35, [2.7, 5.7], rows, rowh=0.5, size=13.5, name='Tabla mioglobina')
    c = caja(s, 9.35, 1.2, 3.7, 2.5, 'Útil en guardia, **sin traumatismo**, con síntomas de IAM: apoyo diagnóstico **temprano**. Con traumatismo muscular su utilidad es **nula**.', BLANCO, 14.5,
             head='Utilidad', name='Utilidad Mb')
    cu = caja(s, 9.35, 3.9, 3.7, 1.55, 'Rabdomiólisis: **mioglobinuria** (orina rojo-marrón) y riesgo de **insuficiencia renal aguda**.', ROSA, 13.5, name='Mioglobinuria')
    r_ = rigor(s, 9.35, 5.65, 3.7, 1.4, 'La mioglobina es **monomérica**: una sola cadena de globina con un hemo (no dos cadenas).', 12.5, name='Rigor mioglobina')
    s.step(fade(mb), fade(hb, after=True), fade(hl, after=True))
    for r in ids:
        s.step(fade(r)) if r == ids[0] else s.anim[-1].append(fade(r, after=True))
    s.step(fade(c))
    s.step(fade(cu))
    s.step(fade(r_))


def ldh_iam(D):
    s = nueva(D, 4, 'LDH en el IAM: tardía e inespecífica', src=['IAM 4.5 LDH'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    rx = s.group_start('Reacción LDH')
    ficha(s, 0.6, 1.5, 'Lactato', '8E44AD', w=1.6, h=0.5, size=14)
    s.arrow([(2.3, 1.6), (3.1, 1.6)], INK, 2.5); s.arrow([(3.1, 1.9), (2.3, 1.9)], INK, 2.5)
    ficha(s, 3.2, 1.5, 'Piruvato', 'F39C12', w=1.6, h=0.5, size=14)
    enzima_globular(s, 1.9, 2.25, 1.6, 1.3, 'E59866', 'LDH', 'LDH forma', size=16)
    s.group_end()
    org = s.group_start('Órganos LDH')
    corazon_anat(s, 0.4, 3.9, 1.3, name='c'); liver(s, 1.8, 4.3, 1.5, name='h'); eritrocito(s, 3.4, 4.3, 0.9, name='e'); kidney(s, 0.8, 5.6, 0.6, name='r')
    brain(s, 1.8, 5.7, 1.4, name='b'); muscle(s, 3.3, 5.6, 1.2, name='m', fibers=2)
    s.group_end()
    pts = ['Alta **sensibilidad** (se eleva ante cualquier daño celular), **bajísima especificidad**.', 'Se eleva **muy tarde (8–18 h)** y tarda **10–14 días** en normalizarse.',
           'El recambio celular normal mantiene un **nivel basal**: necesita un daño grande para elevarse significativamente.',
           'Conclusión: casi nunca sirve como marcador diagnóstico de IAM; valor relativo como **apoyo contextual tardío**.']
    ids = [caja(s, 5.0, 1.2 + k * 1.47, 8.05, 1.32, p, [CREMA, ROSA, BLANCO, AMA][k], 15, anchor='m', name='LDH punto %d' % (k + 1)) for k, p in enumerate(pts)]
    s.step(fade(rx))
    s.step(fade(org))
    for g in ids:
        s.step(fade(g))


# ---------------------------------------------------------------- liberación de biomarcadores (Morph)
LB_TXT = {1: 'Liberación de biomarcadores: el cardiomiocito', 2: 'Estructuras intracelulares: dónde está cada marcador', 3: 'Lesión del cardiomiocito',
          4: 'Liberación de los marcadores citoplasmáticos', 5: 'Aparición en la circulación', 6: 'Obtención de la muestra', 7: 'Medición en el laboratorio',
          8: 'Interpretación temporal'}
MOLP = {  # posiciones de Mb, CK y Tn por etapa
    'mb': {1: [(1.3, 1.9), (2.6, 3.4), (5.9, 1.8)], 4: [(4.55, 4.35), (5.25, 4.55), (6.0, 4.35)], 5: [(1.5, 5.45), (3.6, 5.5), (6.3, 5.45)]},
    'ck': {1: [(2.1, 1.8), (4.4, 3.45), (7.0, 2.0)], 4: [(3.75, 4.6), (4.95, 4.85), (6.6, 4.65)], 5: [(2.3, 5.45), (4.6, 5.5), (7.2, 5.45)]},
    'tn': {1: [(3.0, 2.55), (5.2, 2.55)], 5: [(0.8, 5.45), (5.4, 5.45)]},
}


def mpos(kind, st):
    keys = sorted(MOLP[kind])
    k = max(x for x in keys if x <= st)
    return MOLP[kind][k]


def escena_lb(D, st):
    s = nueva(D, 4, LB_TXT[st], tipo='der', c1=AZUL, c2=BLANCO, morph=st > 1, src=['IAM 4 Biomarcadores', 'IAM 5.1 Cinética por estructura'], tw=8.7)
    ids = {}
    small = st >= 6
    cx, cy, cw, ch = (0.35, 1.2, 4.6, 2.4) if small else (0.35, 1.2, 8.4, 3.3)
    ids['cel'] = cardiomiocito(s, cx, cy, cw, ch, name='!!Cardiomiocito', detalle=False)['g']
    if st >= 3:
        ids['les'] = s.shape(cx + cw * 0.45, cy + ch * 0.82, cw * 0.14, ch * 0.3, 'irregularSeal1', ('a', '4A235A', 70), None, False, name='!!Lesión')
    if st >= 2:
        ids['fil'] = s.group_start('!!Filamento')
        s.shape(cx + cw * 0.08, cy + ch * 0.42, cw * 0.84, ch * 0.16, 'rect', ('lin', [(0, '85C1E9'), (100, '5DADE2')], 90), ('2471A3', 1.0), False)
        s.group_end()
    ids['cap'] = vessel(s, 0.3, 5.2, 8.5, 0.85, name='!!Capilar', rbcs=0)
    if st >= 2:
        ms = []
        if st <= 5:
            for kind, lab, col in (('mb', 'Mb', 'C0392B'), ('ck', 'CK', 'F39C12')):
                for k, (x, y) in enumerate(mpos(kind, st)):
                    if small:
                        continue
                    ms.append(ficha(s, x, y, lab, col, w=0.6, h=0.38, size=11, name='!!%s %d' % (lab, k + 1)))
            for k, (x, y) in enumerate(mpos('tn', st)):
                ms.append(ficha(s, x, y, 'Tn', 'EC7063', w=0.62, h=0.38, size=11, name='!!Troponina %d' % (k + 1)))
        ids['mols'] = ms
    if st >= 6:
        ids['tubo'] = tubo(s, 5.3, 1.25, 0.65, 2.6, [(0.5, 'B3261E', '!!Coágulo muestra'), (0.32, 'FCF3CF', '!!Suero muestra')], tapa='C0392B', name='!!TuboMuestra')
        for k, (lab, col) in enumerate((('Mb', 'C0392B'), ('CK', 'F39C12'), ('Tn', 'EC7063'))):
            ficha(s, 5.32 + (k % 2) * 0.28, 1.9 + k * 0.32, lab, col, w=0.45, h=0.28, size=8, name='!!Marcador en tubo %d' % k)
    if st >= 7:
        g = s.group_start('!!Analizador')
        s.shape(6.3, 1.25, 2.5, 2.6, 'roundRect', shade('D5DBDB', 0.3, 0.2), (INK, 1.75), SH_I, adj={'adj': 10000})
        s.shape(6.5, 1.45, 2.1, 1.4, 'rect', '1C2833', (INK, 1.0), False, 'CPK 1173 UI/L\nTnI: muy elevada', 11, F_HEAD, '58D68D', True, 'c', 'm', (0.04, 0, 0.04, 0))
        s.shape(6.6, 3.1, 0.6, 0.5, 'roundRect', '2E86C1', None, False, adj={'adj': 30000})
        s.group_end()
        ids['ana'] = g
    return s, ids


def liberacion(D):
    ini = len(D.slides) + 1
    s, i = escena_lb(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Un cardiomiocito sano **retiene** su contenido: los biomarcadores están dentro de la célula.', BLANCO, 16, head='Punto de partida', name='Caja LB1')
    s.step(fade(i['cel']), fade(i['cap'], after=True))
    s.step(fade(c))
    s, i = escena_lb(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 4.0, '- **Mioglobina (Mb)** y **CK**: en el **citoplasma**, pequeñas y solubles.\n- **Troponinas (Tn)**: unidas al **aparato contráctil** (filamento).', BLANCO, 15,
             head='Ubicación', name='Caja LB2')
    s.step(fade(i['fil']), *[fade(m, after=(k == 0)) for k, m in enumerate(i['mols'])])
    s.step(fade(c))
    s, i = escena_lb(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'La isquemia **lesiona** la membrana (sarcolema): aumenta su permeabilidad.', ROSA, 16, head='Lesión', headfill=ROJO, name='Caja LB3')
    s.step(zoom(i['les']), pulse(i['les'], after=True))
    s.step(fade(c))
    s, i = escena_lb(D, 4)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Salen primero las moléculas **pequeñas y solubles** del citoplasma: **mioglobina** y **CK**. Las troponinas siguen unidas a la estructura.', 'FDEBD0', 15,
             head='Liberación', name='Caja LB4')
    s.step(fade(c))
    s, i = escena_lb(D, 5)
    c = caja(s, 9.35, 1.2, 3.7, 3.6, 'Los marcadores **aparecen en la sangre**. Con la **necrosis** se rompe la estructura y también se liberan las **troponinas**.', ROSA, 15, head='Circulación',
             headfill=ROJO, name='Caja LB5')
    s.step(*[pulse(m, after=(k > 0)) for k, m in enumerate(i['mols'][-2:])])
    s.step(fade(c))
    s, i = escena_lb(D, 6)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Se extrae sangre: los marcadores quedan en la fase líquida que se analiza.', BLANCO, 16, head='Muestra', name='Caja LB6')
    s.step(fade(c))
    s, i = escena_lb(D, 7)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'El laboratorio informa la concentración o la actividad de cada marcador (en el caso: **CPK 1173 UI/L** al ingreso).', AMA, 15.5, head='Medición',
             name='Caja LB7')
    s.step(fade(i['ana']))
    s.step(fade(c))
    s, i = escena_lb(D, 8)
    tl = s.group_start('Línea temporal LB')
    s.arrow([(0.5, 4.3), (8.7, 4.3)], INK, 2.5)
    for k, (t, x) in enumerate((('1–4 h\nmioglobina', 0.9), ('3–6 h\ntroponinas', 2.8), ('4–6 h\nCK-MB', 4.6), ('8–18 h\nLDH', 6.6))):
        s.arrow([(x + 0.5, 4.15), (x + 0.5, 4.45)], INK, 1.5, tail=None)
        texto(s, x - 0.2, 4.5, 1.6, 0.65, t, 12.5, NAVY, True, 'c')
    s.group_end()
    c = caja(s, 9.35, 1.2, 3.7, 3.6, 'El valor de un marcador **depende del momento** de la toma de muestra respecto del inicio del dolor: cada uno tiene su propia **cinética**.', AMA, 15.5,
             head='Interpretación', name='Caja LB8')
    s.step(wipe(tl, 'l'))
    s.step(fade(c))
    registrar_morph(D, ini, len(D.slides), 'Liberación de biomarcadores: cardiomiocito → contenido → lesión → liberación → circulación → muestra → medición → interpretación temporal',
                    ['!!Cardiomiocito', '!!Filamento', '!!Lesión', '!!Capilar', '!!Mb 1–3', '!!CK 1–3', '!!Troponina 1–2', '!!TuboMuestra', '!!Analizador'],
                    'Las fichas de Mb y CK salen por la lesión y descienden al capilar; las troponinas se desprenden después; el cardiomiocito se reduce para dejar lugar al tubo y al analizador.')


# ---------------------------------------------------------------- cinética
TX = [(0, 0.0), (6, 0.12), (12, 0.22), (24, 0.36), (48, 0.5), (72, 0.6), (168, 0.78), (240, 0.88), (336, 1.0)]


def tx(t):
    for (t0, x0), (t1, x1) in zip(TX, TX[1:]):
        if t <= t1:
            return x0 + (x1 - x0) * (t - t0) / (t1 - t0)
    return 1.0


def curva_bm(start, peak, end, h):
    xs = [0, start, (start + peak) / 2, peak, (peak + end) / 2, end, 336]
    ys = [0, 0, h * 0.55, h, h * 0.4, 0.0, 0.0]
    return [(int(tx(t) * 1000), int(1000 - 60 - y * 880)) for t, y in zip(xs, ys)]


def cinetica(D):
    s = nueva(D, 4, 'Cinética de los biomarcadores: las curvas se construyen', src=['IAM 5 Perfil cinético', 'IAM 5.3 Ventana diagnóstica'], tipo='der', c1=AZUL, c2=BLANCO)
    X, Y, W, H = 0.8, 1.45, 7.9, 4.3
    ej = s.group_start('!!Ejes cinética')
    s.arrow([(X, Y + H), (X, Y - 0.05)], INK, 2.25)
    s.arrow([(X, Y + H), (X + W + 0.1, Y + H)], INK, 2.25)
    for t, lab in ((0, '0'), (6, '6 h'), (12, '12 h'), (24, '24 h'), (48, '48 h'), (72, '72 h'), (168, '7 d'), (240, '10 d'), (336, '14 d')):
        xx = X + W * tx(t)
        s.arrow([(xx, Y + H), (xx, Y + H + 0.1)], INK, 1.25, tail=None)
        texto(s, xx - 0.4, Y + H + 0.12, 0.8, 0.3, lab, 11.5, INK, True, 'c')
    texto(s, X + 0.1, Y - 0.45, 4.5, 0.35, 'concentración relativa (esquema)', 12.5, INK, True)
    texto(s, X + W - 3.6, Y + H + 0.42, 3.7, 0.3, 'tiempo desde el inicio del dolor (escala no lineal)', 11, '5D6D7E', True, 'r')
    s.group_end()
    dolor = s.arrow([(X, Y), (X, Y + H)], ROJO, 3, tail=None, dash='dash', name='Inicio del evento')
    dl = rotulo(s, X + 0.1, Y - 0.05, 'inicio del dolor', ROJO, 11.5, name='Rótulo inicio')
    cs = {}
    for k, (n, st_, pk, en, h, col) in enumerate((('Mioglobina', 2.5, 6.5, 24, 0.72, 'C0392B'), ('CK-MB', 5, 18, 60, 0.55, 'F39C12'), ('Troponina I', 4.5, 18, 204, 0.95, '7D3C98'),
                                                 ('LDH', 13, 36, 288, 0.42, '1E8449'))):
        cs[n] = curva(s, X, Y, W, H, curva_bm(st_, pk, en, h), col, 4.5, name='!!Curva ' + n)
    lab = {}
    for n, (x, y, col) in {'Mioglobina': (X + W * 0.07, Y + H * 0.12, 'C0392B'), 'CK-MB': (X + W * 0.38, Y + H * 0.38, 'F39C12'), 'Troponina I': (X + W * 0.42, Y - 0.05, '7D3C98'),
                           'LDH': (X + W * 0.62, Y + H * 0.52, '1E8449')}.items():
        lab[n] = rotulo(s, x, y, n, col, 12.5, name='Rótulo ' + n)
    muestra = s.arrow([(X + W * tx(192), Y + 0.2), (X + W * tx(192), Y + H)], NAVY, 3, tail=None, dash='sysDash', name='Toma de muestra día 8')
    ml = rotulo(s, X + W * tx(192) - 0.7, Y + H * 0.62, 'día 8', NAVY, 12.5, w=1.0, name='Rótulo día 8')
    c1 = caja(s, 9.35, 1.2, 3.7, 1.75, 'Esquema **cualitativo**: los tiempos son los del material; la altura de cada curva es ilustrativa.', CREMA, 13, name='Aclaración esquema')
    c2 = caja(s, 9.35, 3.15, 3.7, 1.95, 'La **mioglobina** sube y baja primero; **CK-MB** normaliza en 48–72 h; la **troponina** persiste 7–10 días; la **LDH** es la más tardía.', BLANCO, 13.5,
              head='Comparación', name='Comparación curvas')
    c3 = caja(s, 9.35, 5.3, 3.7, 1.75, 'A los **8 días** solo siguen altas **troponina** y **LDH**: lo esperable por su cinética.', AMA, 13.5, head='Momento de la muestra', name='Interpretación día 8')
    s.step(fade(ej))                                                             # 1 ejes
    s.step(fade(dolor), fade(dl, after=True))                                    # 2 inicio del evento
    s.step(wipe(cs['Mioglobina'], 'l', dur=900), fade(lab['Mioglobina'], after=True))  # 3 primera curva
    s.step(pulse(lab['Mioglobina']))                                             # 4 evolución
    s.step(wipe(cs['CK-MB'], 'l', dur=900), fade(lab['CK-MB'], after=True))      # 5 siguiente curva
    s.step(wipe(cs['Troponina I'], 'l', dur=1100), fade(lab['Troponina I'], after=True))
    s.step(wipe(cs['LDH'], 'l', dur=1100), fade(lab['LDH'], after=True))
    s.step(fade(c1), fade(c2, after=True))                                       # 6 comparación
    s.step(wipe(muestra, 't'), fade(ml, after=True), fade(c3, after=True))        # 7 interpretación de la toma


def tabla_maestra(D):
    s = nueva(D, 4, 'Perfil cinético: tabla maestra', src=['IAM 5 Perfil cinético', 'IAM 9 Tabla comparativa'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    rows = [['Biomarcador', 'Inicio', 'Pico', 'Normalización', 'Sensibilidad', 'Especificidad cardíaca', 'Uso principal'],
            ['Mioglobina', '1–4 h', '6–7 h', '24 h', 'Muy alta', 'Muy baja', 'Ayuda temprana; no confirma IAM sola'],
            ['Troponina I', '3–6 h', '12–24 h', '7–10 días', 'Alta', 'Muy alta', 'Referencia diagnóstica: necrosis miocárdica'],
            ['Troponina T', '3–6 h', '12–24 h', '7–10 días', 'Alta', 'Alta', 'Similar a TnI'],
            ['CPK total', '4–8 h', '12–24 h (hasta 48 h)', '48–72 h', 'Alta', 'Baja', 'Siempre con CK-MB; reinfarto'],
            ['CPK-MB', '4–6 h', '12–24 h', '48–72 h', 'Alta', 'Moderada', 'Junto a CK total; nuevos eventos'],
            ['LDH', '8–18 h', '24–48 h', '10–14 días', 'Alta (tardía)', 'Muy baja', 'Contextual tardío']]
    ids, H = tabla_filas(s, 0.35, 1.2, [1.65, 1.0, 1.45, 1.4, 1.35, 1.6, 4.2], rows, rowh=0.62, size=13, name='Tabla cinética')
    c = caja(s, 0.35, 1.4 + H, 12.65, 6.95 - (1.4 + H), 'La cinética depende del **tamaño y solubilidad**, de si la molécula es **citoplasmática o estructural**, de la **depuración renal** y de la **magnitud del daño**.',
             AMA, 15, anchor='m', name='Determinantes cinética')
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))


def por_que_cinetica(D):
    s = nueva(D, 4, '¿Por qué cada biomarcador tiene su propia cinética?', src=['IAM 5.1 Regla de oro'], tipo='der', c1=AZUL, c2=LAVANDA)
    grupos = [('Pequeñas y solubles', 'Mioglobina: se liberan rápido al dañarse la membrana y filtran fácil por el riñón → aparición, pico y normalización **rápidos**.', 'C0392B', 0.35),
              ('Enzimas citoplasmáticas', 'CK, CK-MB: salen con la pérdida de permeabilidad o la necrosis inicial → latencia **intermedia**, depuración en 48–72 h.', 'F39C12', 0.55),
              ('Proteínas estructurales', 'Troponinas: solo con **necrosis** completa; moléculas grandes → latencia moderada y depuración **muy lenta** (7–10 días).', '7D3C98', 0.75),
              ('Ubicuas y grandes', 'LDH: el recambio normal ya mantiene niveles basales; necesita daño masivo y tarda mucho en normalizarse.', '1E8449', 0.95)]
    ids = []
    for k, (t, d, col, sz) in enumerate(grupos):
        y = 1.2 + k * 1.47
        g = s.group_start('Grupo cinética %d' % (k + 1))
        s.shape(0.45 + (1 - sz) * 0.5, y + (1.2 - sz * 1.2) / 2, sz * 1.2, sz * 1.2, 'ellipse', shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), False)
        caja(s, 1.85, y, 6.95, 1.3, '**%s**: %s' % (t, d), BLANCO, 14, anchor='m')
        ids.append(s.group_end())
    c = caja(s, 9.35, 1.2, 3.7, 5.85, '**Regla de oro**: la cinética depende de la **estructura molecular** (tamaño, solubilidad, ubicación en la célula) y de cómo se **depura**.', AMA, 16,
             head='Regla', name='Regla cinética')
    for g in ids:
        s.step(fade(g))
    s.step(fade(c))


def magnitud(D):
    s = nueva(D, 4, 'La magnitud del daño se refleja en el pico', src=['IAM 5.2 Magnitud del daño'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    X, Y, W, H = 0.7, 1.5, 6.6, 4.0
    ej = ejes(s, X, Y, W, H, 'tiempo', 'troponina', name='Ejes magnitud')
    peq = curva(s, X, Y, W, H, [(0, 950), (150, 940), (350, 700), (550, 800), (1000, 940)], '85C1E9', 4.5, name='Infarto pequeño')
    gra = curva(s, X, Y, W, H, [(0, 950), (150, 940), (350, 120), (600, 500), (1000, 900)], '7D3C98', 4.5, name='Infarto extenso')
    l1 = rotulo(s, 3.4, 4.05, 'infarto pequeño: pico bajo', '85C1E9', 13, name='Rótulo pequeño')
    l2 = rotulo(s, 3.6, 1.55, 'infarto extenso: pico muy alto', '7D3C98', 13, name='Rótulo extenso')
    c1 = caja(s, 7.7, 1.2, 5.35, 2.4, 'Los valores pico son **proporcionales a la extensión** del daño: los biomarcadores también sirven para **estimar el tamaño del infarto**.', AMA, 15.5,
              name='Proporcional')
    c2 = caja(s, 7.7, 3.85, 5.35, 3.2, 'Comparación clínica: no es lo mismo un **golpe leve** (CPK moderadamente elevada) que una **caída de altura o un accidente vial** (CPK y mioglobina masivamente elevadas por rabdomiólisis).',
              BLANCO, 15, name='Comparación trauma')
    s.step(fade(ej))
    s.step(wipe(peq, 'l'), fade(l1, after=True))
    s.step(wipe(gra, 'l'), fade(l2, after=True), fade(c1, after=True))
    s.step(fade(c2))


def ventana(D):
    s = nueva(D, 4, 'Ventana diagnóstica: qué pedir según el tiempo', src=['IAM 5.3 Ventana diagnóstica'], tipo='bandas', c1=LAVANDA, c2=CELESTE)
    tl = s.group_start('!!Línea de tiempo')
    s.arrow([(0.5, 2.0), (12.9, 2.0)], NAVY, 4)
    s.group_end()
    et = [('0–4 h', 'Mioglobina (primer marcador). ECG y síntomas son lo más relevante.', 'C0392B'), ('3–6 h', 'Troponinas, CPK y CK-MB empiezan: solicitar **todo junto** al ingreso.', '7D3C98'),
          ('12–24 h', 'Pico de troponinas, CPK y CK-MB: momento ideal para **confirmar** si los primeros fueron dudosos.', 'F39C12'),
          ('48–72 h', 'CPK y CK-MB deberían normalizarse; si no → sospechar **reinfarto o extensión**.', '1E8449'),
          ('7–10 días', 'Troponinas aún elevadas (esperable): no interpretar como nuevo evento salvo **escalada súbita**.', '2E86C1')]
    ids = []
    for k, (t, d, col) in enumerate(et):
        x = 0.45 + k * 2.5
        g = s.group_start('Ventana %s' % t)
        s.shape(x + 0.95, 1.8, 0.4, 0.4, 'ellipse', col, (INK, 1.25), False)
        rotulo(s, x + 0.25, 1.05, t, col, 15, w=1.8)
        caja(s, x, 2.5, 2.35, 3.0, d, BLANCO, 14)
        ids.append(s.group_end())
    c = caja(s, 0.45, 5.75, 12.4, 1.3, 'Cada marcador responde a una pregunta distinta según **cuánto tiempo pasó** desde el inicio del dolor.', AMA, 16, anchor='m', name='Síntesis ventana')
    s.step(wipe(tl, 'l'))
    for g in ids:
        s.step(fade(g))
    s.step(fade(c))


def reinfarto(D):
    s = nueva(D, 4, 'Reinfarto: ¿cómo detectar un nuevo evento?', src=['IAM 6 Evaluación del reinfarto', 'REV IAM 6'], tipo='der', c1=AZUL, c2=BLANCO)
    X, Y, W, H = 0.7, 1.5, 7.9, 3.0
    ej = ejes(s, X, Y, W, H, 'días', 'concentración (esquema)', name='Ejes reinfarto')
    tn = curva(s, X, Y, W, H, [(0, 950), (80, 900), (180, 150), (500, 450), (800, 750), (1000, 900)], '7D3C98', 4.5, name='Troponina residual')
    ckmb = curva(s, X, Y, W, H, [(0, 950), (80, 920), (150, 350), (300, 940), (550, 945), (620, 450), (750, 940), (1000, 950)], 'F39C12', 4.5, name='CK-MB con nuevo pico')
    l1 = rotulo(s, 4.0, 2.0, 'troponina: aún elevada', '7D3C98', 12.5, name='Rótulo Tn residual')
    l2 = rotulo(s, 5.3, 3.2, 'CK-MB: nuevo ascenso', 'F39C12', 12.5, name='Rótulo nuevo pico')
    rows = [['Biomarcador', '¿Sirve para reinfarto? (material)'], ['Troponina I/T', 'No: sigue elevada 7–10 días'], ['CPK total', 'Sí: normaliza en 48–72 h'],
            ['CPK-MB', 'Sí: preferida, más específica'], ['Mioglobina', 'Solo en las primeras 24 h'], ['LDH', 'No: tardía e inespecífica']]
    ids, Hh = tabla_filas(s, 0.4, 4.85, [2.6, 5.9], rows, rowh=0.36, size=12.5, name='Tabla reinfarto')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'Con troponinas de alta sensibilidad, la definición universal vigente diagnostica el reinfarto por un **nuevo ascenso de troponina > 20 %** respecto del valor previo (con clínica compatible). '
               'La CK-MB es una alternativa histórica o cuando no hay troponina disponible.', 13.5, name='Rigor reinfarto')
    s.step(fade(ej))
    s.step(wipe(tn, 'l'), fade(l1, after=True))
    s.step(wipe(ckmb, 'l', dur=1200), fade(l2, after=True))
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids)])
    s.step(fade(r_))


def tratamiento(D):
    s = nueva(D, 4, 'Evolución del caso: tratamiento durante la internación', src=['IAM 7.1 Tratamiento administrado'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    rows = [['Fármaco', 'Indicación y acción (según el material)'], ['Nitratos endovenosos', 'Vasodilatación coronaria → alivio del dolor anginoso. Contraindicados con **sildenafil** (inhibidor de PDE5): hipotensión severa.'],
            ['Aspirina 100 mg/día', 'Antiagregante: inhibe la **COX-1** → bloquea la síntesis de **tromboxano A_{2}**.'],
            ['Clopidogrel 75 mg/día', 'Antiagregante: inhibe el receptor **P2Y12** del ADP; con aspirina = **doble antiagregación**.']]
    ids, H = tabla_filas(s, 0.4, 1.25, [2.8, 9.85], rows, rowh=0.9, size=15, name='Tabla tratamiento')
    pl = s.group_start('Plaquetas tratamiento')
    for k in range(5):
        plaqueta(s, 0.6 + k * 0.9, 5.45, 0.7, name='pl%d' % k, activa=k % 2 == 0)
    s.group_end()
    n = caja(s, 5.3, 1.45 + H, 7.75, 6.95 - (1.45 + H), 'Se presenta el tratamiento **tal como figura en el caso**, para contextualizar el seguimiento; las indicaciones terapéuticas se individualizan.', CREMA, 14.5,
             name='Nota tratamiento')
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(pl), fade(n, after=True))


SEG = {
    # marcador: (valor ingreso, altura ingreso, valor día 8, altura día 8, color)
    'CPK total': ('1173 UI/L', 0.95, '100 UI/L (normal)', 0.18, 'F39C12'),
    'CPK-MB': ('elevada', 0.8, '4 ng/mL (normal)', 0.15, 'F5B041'),
    'Troponina I': ('muy elevada', 0.98, '36 pg/mL (VN < 34)', 0.3, '7D3C98'),
    'LDH': ('elevada', 0.55, 'sigue elevada', 0.5, '1E8449'),
    'Mioglobina': ('elevada', 0.7, 'no se dosó', 0.0, 'C0392B'),
}


def escena_seg(D, st):
    tt = {1: 'Seguimiento del caso: laboratorio de ingreso', 2: 'Seguimiento del caso: laboratorio a los 8 días'}[st]
    s = nueva(D, 4, tt, tipo='der', c1=AZUL, c2=BLANCO, morph=st > 1, src=['IAM 7.2 Laboratorio día 8 vs ingreso'], tw=8.7)
    ids = {}
    base = 5.6; Hmax = 3.8
    ids['base'] = s.arrow([(0.4, base), (8.8, base)], INK, 2.25, tail=None, name='!!Línea base')
    ids['lim'] = s.arrow([(0.4, base - 0.65), (8.8, base - 0.65)], VERDE_OSC, 2, tail=None, dash='dash', name='!!Límite superior de referencia')
    ids['liml'] = texto(s, 3.2, base + 0.62, 2.6, 0.32, 'línea punteada: límite de referencia', 11.5, VERDE_OSC, True, 'c', name='!!Rótulo límite')
    for k, (n, (v0, h0, v8, h8, col)) in enumerate(SEG.items()):
        x = 0.6 + k * 1.65
        h = h0 if st == 1 else h8
        if h > 0:
            ids['b%d' % k] = s.shape(x, base - Hmax * h, 1.2, Hmax * h, 'rect', ('lin', [(0, lighten(col, 0.35)), (100, col)], 90), (INK, 1.25), False, name='!!Barra ' + n)
        else:
            ids['b%d' % k] = s.shape(x, base - 0.05, 1.2, 0.05, 'rect', 'D5DBDB', (INK, 0.5), False, name='!!Barra ' + n)
        ids['n%d' % k] = texto(s, x - 0.15, base + 0.08, 1.5, 0.55, n, 13, INK, True, 'c', name='!!Nombre ' + n)
        ids['v%d' % k] = texto(s, x - 0.2, base - Hmax * max(h, 0.02) - 0.62, 1.6, 0.55, v0 if st == 1 else v8, 12, darken(col, 0.3), True, 'c', name='!!Valor ' + n)
    ids['dia'] = rotulo(s, 0.5, 6.4, 'DÍA 0 (ingreso)' if st == 1 else 'DÍA 8', NAVY, 16, w=2.6, name='!!Rótulo día')
    return s, ids


def seguimiento(D):
    ini = len(D.slides) + 1
    s, i = escena_seg(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Al ingreso, **todos** los marcadores estaban elevados (alturas esquemáticas; los números son los del caso).', BLANCO, 15, head='Ingreso', name='Caja ingreso')
    s.step(fade(i['base']), fade(i['lim'], after=True), fade(i['liml'], after=True), fade(i['dia'], after=True))
    s.step(*[e for k in range(5) for e in (wipe(i['b%d' % k], 'b', after=(k > 0)), fade(i['n%d' % k], after=True), fade(i['v%d' % k], after=True))])
    s.step(fade(c))
    s, i = escena_seg(D, 2)
    lec = [('CPK y CK-MB **normalizadas**: el daño agudo se resolvió; no hay reinfarto.', 'EAF5EA'), ('Troponina I **levemente** elevada: esperable por su cinética (7–10 días).', LAVANDA),
           ('LDH **sigue elevada**: normaliza a los 10–14 días.', 'EAF5EA'), ('Mioglobina **no se dosó**: normaliza en 24 h; a los 8 días no aporta.', CREMA)]
    ids = [caja(s, 9.35, 1.2 + k * 1.47, 3.7, 1.35, t, f, 13, anchor='m', name='Lectura día 8 %d' % (k + 1)) for k, (t, f) in enumerate(lec)]
    for g in ids:
        s.step(fade(g))
    registrar_morph(D, ini, len(D.slides), 'Seguimiento del caso de IAM: laboratorio de ingreso → laboratorio a los 8 días',
                    ['!!Barra CPK total', '!!Barra CPK-MB', '!!Barra Troponina I', '!!Barra LDH', '!!Barra Mioglobina', '!!Valor …', '!!Nombre …', '!!Rótulo día', '!!Línea base'],
                    'Cada barra cambia de altura (CPK y CK-MB descienden bajo el límite; la troponina queda apenas por encima; la LDH se mantiene; la mioglobina desaparece) y los valores numéricos se reemplazan.')


def reinternar(D):
    s = nueva(D, 4, '¿Hay que reinternarlo por la troponina elevada?', src=['IAM 7.3 Reinternación', 'REV IAM 7.3'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    q = caja(s, 0.4, 1.2, 12.65, 1.0, 'Troponina I = **36 pg/mL** al día 8 (referencia < 34 pg/mL).', AMA, 19, anchor='m', align='c', name='Dato troponina')
    no = caja(s, 0.4, 2.45, 6.2, 2.4, '**No**: la troponina levemente elevada a los 8 días es **esperable por su cinética**; puede permanecer elevada hasta 10 días.', 'EAF5EA', 16, head='Respuesta',
              headfill=VERDE_OSC, name='No reinternar')
    si = caja(s, 6.85, 2.45, 6.2, 2.4, 'Sí se sospecha un nuevo evento ante una **escalada súbita** (nuevo pico) **con síntomas** y **cambios nuevos en el ECG**.', ROSA, 16, head='¿Cuándo sí?',
              headfill=ROJO, name='Cuándo sí')
    ck_ = caja(s, 0.4, 5.1, 6.2, 1.95, 'Marcador de elección para reinfarto en el material: **CK-MB**, ya normalizada en este paciente.', BLANCO, 15, name='CK-MB normal')
    r_ = rigor(s, 6.85, 5.1, 6.2, 1.95, 'Con troponinas de alta sensibilidad, se compara con el valor previo: un **ascenso > 20 %** con clínica compatible orienta a reinfarto.', 13.5,
               name='Rigor reinternar')
    s.step(fade(q))
    s.step(fade(no))
    s.step(fade(si))
    s.step(fade(ck_))
    s.step(fade(r_))


def factores_riesgo(D):
    s = nueva(D, 4, 'Factores de riesgo: mecanismos fisiopatológicos', src=['IAM 8 Factores de riesgo', 'REV IAM 8'], tipo='der', c1=AZUL, c2=BLANCO)
    aw = artery_wall(s, 0.4, 1.25, 8.4, 2.3, name='!!Pared arterial')
    ldl = [lipoprotein(s, 1.2 + k * 1.4, 1.35, 0.5, text='LDL', name='LDL %d' % k) for k in range(4)]
    rows = [['Factor', 'Mecanismo'], ['Tabaquismo severo', 'Más LDL; las LDL oxidadas se depositan en la pared → placa → obstrucción progresiva.'],
            ['Obesidad', 'Dislipemia, exceso de ácidos grasos libres, resistencia a la insulina.'],
            ['Hipertensión arterial', 'Microtraumatismos endoteliales → entrada de LDL oxidadas → inflamación vascular; vasos rígidos.'],
            ['Antecedentes familiares', 'Predisposición genética (hipercolesterolemia familiar, disfunción endotelial, trombofilia).']]
    ids, H = tabla_filas(s, 0.4, 3.75, [2.5, 5.9], rows, rowh=0.55, size=13, name='Tabla factores riesgo')
    c = caja(s, 9.35, 1.2, 3.7, 2.4, 'Los factores **se potencian**: HTA + tabaquismo + obesidad → riesgo **exponencialmente mayor**.', AMA, 15, name='Potenciación')
    r_ = rigor(s, 9.35, 3.85, 3.7, 3.2, 'El tabaquismo daña sobre todo por **disfunción endotelial, estrés oxidativo** (oxidación de LDL), descenso del HDL y un estado **protrombótico**.', 13,
               name='Rigor tabaco')
    s.step(fade(aw))
    s.step(*[fade(l, after=(k > 0)) for k, l in enumerate(ldl)], *[path(l, 0.2, 0.9, after=(k == 0), dur=900) for k, l in enumerate(ldl)])
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))
    s.step(fade(r_))


def tabla_completa(D):
    s = nueva(D, 4, 'Tabla comparativa de los biomarcadores cardíacos', src=['IAM 9 Tabla comparativa'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    rows = [['', 'Mioglobina', 'Troponina I/T', 'CPK-MB', 'CPK total', 'LDH'],
            ['Tipo', 'Proteína transportadora de O_{2}', 'Proteína estructural cardíaca', 'Isoenzima citoplasmática', 'Enzima (suma de isoenzimas)', 'Enzima metabólica'],
            ['Localización', 'Músculo esquelético + corazón', 'Solo corazón (isoforma cardíaca)', 'Corazón > esquelético > cerebro', 'Músculo, corazón, cerebro', 'Casi todos los tejidos'],
            ['Inicio / pico', '1–4 h / 6–7 h', '3–6 h / 12–24 h', '4–6 h / 12–24 h', '4–8 h / 12–48 h', '8–18 h / 24–48 h'],
            ['Normalización', '24 h', '7–10 días', '48–72 h', '48–72 h', '10–14 días'],
            ['Especificidad', 'Muy baja', 'Muy alta', 'Moderada', 'Baja', 'Muy baja'],
            ['Uso práctico', 'Marcador temprano de apoyo', 'Diagnóstico de IAM y necrosis', 'Evolución y reinfarto (con CK total)', 'Siempre junto a MB', 'Contextual tardío']]
    ids, H = tabla_filas(s, 0.35, 1.2, [1.75, 2.15, 2.25, 2.25, 2.15, 2.1], rows, rowh=0.6, size=12.5, name='Tabla completa')
    c = caja(s, 0.35, 1.35 + H, 12.65, 6.95 - (1.35 + H), 'La **troponina** confirma necrosis miocárdica; **CK + CK-MB** van juntas; una troponina elevada **no siempre** es un nuevo infarto: hay que leer la cinética.',
             AMA, 15, anchor='m', name='Mensaje tabla')
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c))


def integracion_d(D):
    s = nueva(D, 4, 'Integración D: del cardiomiocito a la curva', src=['IAM 4 Biomarcadores', 'IAM 5 Perfil cinético', 'IAM 10 Glosario IAM'], tipo='bandas', c1=LAVANDA, c2=AZUL_M)
    pasos = [('Cardiomiocito', 'Depende del aporte coronario de O_{2}.', 'cel'), ('Lesión', 'Oclusión coronaria → isquemia → necrosis.', 'les'),
             ('Liberación', 'Mb y CK primero; troponinas con la necrosis.', 'lib'), ('Evolución temporal', 'Curvas: Mb → CK-MB → Tn → LDH.', 'cur')]
    ids = []
    for k, (t, d, kind) in enumerate(pasos):
        x = 0.45 + k * 3.2
        g = s.group_start('Integración D %d' % (k + 1))
        if kind == 'cel':
            cardiomiocito(s, x + 0.1, 1.5, 2.8, 1.3, name='Cel D')
        elif kind == 'les':
            corazon_anat(s, x + 0.8, 1.2, 1.5, name='Corazón D')
        elif kind == 'lib':
            for j, (m, c) in enumerate((('Mb', 'C0392B'), ('CK', 'F39C12'), ('Tn', 'EC7063'))):
                ficha(s, x + 0.3 + j * 0.85, 1.9, m, c, w=0.7, h=0.42, size=12)
        else:
            curva(s, x + 0.1, 1.3, 2.8, 1.6, [(0, 900), (150, 880), (300, 150), (600, 600), (1000, 880)], '7D3C98', 3.5, name='Curva D')
        caja(s, x, 3.35, 3.0, 2.2, '**%s**\n%s' % (t, d), BLANCO, 15)
        if k < 3:
            s.arrow([(x + 3.02, 4.45), (x + 3.18, 4.45)], INK, 3)
        ids.append(s.group_end())
    c = caja(s, 0.45, 5.8, 12.45, 1.25, 'El diagnóstico integra **clínica, ECG y troponina dinámica**; la cinética de cada marcador indica **cuándo** ocurrió el daño y si hay un evento nuevo.', NAVY, 15.5,
             anchor='m', name='Síntesis D')
    for g in ids:
        s.step(fade(g))
    s.step(zoom(c))


def build(D):
    biomarcador(D)
    ck(D)
    isoenzimas(D)
    ck_mb_sola(D)
    troponinas(D)
    especificidad_tn(D)
    permeabilidad(D)
    mioglobina(D)
    ldh_iam(D)
    liberacion(D)
    cinetica(D)
    tabla_maestra(D)
    por_que_cinetica(D)
    magnitud(D)
    ventana(D)
    reinfarto(D)
    tratamiento(D)
    seguimiento(D)
    reinternar(D)
    factores_riesgo(D)
    tabla_completa(D)
    integracion_d(D)
