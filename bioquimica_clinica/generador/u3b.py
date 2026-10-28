# -*- coding: utf-8 -*-
"""UNIDAD III (parte 2): anemia megaloblástica, absorción de B12 (Morph), ácido fólico, biomarcadores,
casos clínicos, etiología de las hemolíticas, anemias fisiológicas e integración."""
from plantillas import *
from u3 import falciforme


def megaloblastica(D):
    s = nueva(D, 3, 'Anemia megaloblástica: falla la síntesis de ADN', src=['AN 7.1 Fisiopatología megaloblástica'], tipo='der', c1=ROJO, c2=ROSA)
    cic = s.group_start('!!Ciclo celular')
    cx, cy, R = 2.6, 3.6, 1.9
    for k, (t, a0, a1, c) in enumerate((('G1', -90, 60, 'AED6F1'), ('S', 60, 170, ROJO), ('G2', 170, 230, 'F9E79F'), ('M', 230, 270, 'A9DFBF'))):
        s.shape(cx - R, cy - R, 2 * R, 2 * R, 'blockArc', c, (INK, 1.25), False, adj={'adj1': int((a0 % 360) * 60000), 'adj2': int((a1 % 360) * 60000), 'adj3': 22000})
        am = math.radians((a0 + a1) / 2)
        texto(s, cx + (R - 0.25) * math.cos(am) - 0.4, cy + (R - 0.25) * math.sin(am) - 0.2, 0.8, 0.4, t, 18, BLANCO if c == ROJO else INK, True, 'c', 'm')
    s.group_end()
    x_ = s.shape(cx + 0.35, cy + 0.85, 0.8, 0.8, 'rect', None, None, False, 'X', 36, F_HEAD, ROJO, True, 'c', 'm', (0, 0, 0, 0), name='Bloqueo fase S', fit=False)
    vit = s.group_start('Vitaminas')
    ficha(s, 5.0, 1.6, 'Vitamina B_{12}', 'E74C3C', w=2.0, h=0.5, size=14)
    ficha(s, 7.1, 1.6, 'Ácido fólico', '27AE60', w=1.8, h=0.5, size=14)
    s.group_end()
    c1 = caja(s, 5.0, 2.35, 3.95, 2.3, 'Son **cofactores indispensables** para la **síntesis de ADN**: su déficit afecta la **fase S** del ciclo celular (duplicación del material genético).', BLANCO, 14.5,
              name='Cofactores ADN')
    c2 = caja(s, 5.0, 4.9, 3.95, 2.15, 'Sin duplicación correcta del ADN las células **no se dividen** normalmente: aparece el **megaloblasto**.', AMA, 15, name='Consecuencia ADN')
    c3 = caja(s, 9.35, 1.2, 3.7, 3.0, 'Déficit de **vitamina B_{12}** y/o **ácido fólico** → anemia **macrocítica megaloblástica**.', BLANCO, 16, head='Causa', name='Causa megaloblástica')
    mg = megaloblasto(s, 10.2, 4.5, 2.1, name='Megaloblasto deco')
    s.step(fade(cic))
    s.step(fade(vit), fade(c1, after=True))
    s.step(zoom(x_), fade(c2, after=True))
    s.step(fade(c3), fade(mg, after=True))


AS_TXT = {1: 'Maduración normal: núcleo y citoplasma sincronizados', 2: 'Asincronismo madurativo: nace el megaloblasto',
          3: 'Eritropoyesis ineficaz y hemólisis'}


def escena_asin(D, st):
    s = nueva(D, 3, AS_TXT[st], tipo='der', c1=ROJO, c2=ROSA, morph=st > 1, src=['AN 7.1 Asincronismo madurativo'], tw=8.7)
    ids = {}
    ids['mo'] = medula_osea(s, 0.3, 1.2, 8.5, 4.0, name='!!MedulaOsea', celulas=0)
    # cuatro estadios
    if st == 1:
        stages = [(1.0, 1.4, 0.75, '7D5BA6'), (2.9, 1.25, 0.55, '7D5BA6'), (4.6, 1.1, 0.35, '5B2C6F'), (6.3, 1.0, 0.0, None)]
    else:
        stages = [(1.0, 1.4, 0.75, '7D5BA6'), (2.9, 1.75, 0.72, 'B39DDB'), (4.9, 2.1, 0.7, 'B39DDB'), (6.9, 1.6, 0.0, None)]
    for k, (x, d, nf, col) in enumerate(stages):
        y = 3.2 - d / 2
        cyto = 'E8A3B6' if st == 1 else ('E8A3B6' if k < 1 else 'F1B6C6')
        ids['c%d' % k] = s.shape(x, y, d, d, 'ellipse', shade(cyto if k < 3 else 'E57373', 0.4, 0.25), ('8E3A59', 1.25), False, name='!!Célula %d' % (k + 1))
        if nf:
            nd = d * nf
            ids['n%d' % k] = s.shape(x + (d - nd) / 2, y + (d - nd) / 2, nd, nd, 'ellipse', ('rad', [(0, lighten(col, 0.3)), (100, col)], (40, 35)), ('311B92', 1.0), False,
                                     name='!!Núcleo %d' % (k + 1))
    if st == 3:
        for k, (x, y) in enumerate(((5.2, 4.3), (5.6, 4.55), (5.0, 4.6))):
            s.shape(x, y, 0.32, 0.22, 'ellipse', 'C0392B', ('6E1A12', 0.75), False, name='Fragmento %d' % k)
    return s, ids


def asincronismo(D):
    ini = len(D.slides) + 1
    s, i = escena_asin(D, 1)
    c = caja(s, 0.3, 5.45, 8.5, 1.6, 'En la eritropoyesis normal el **núcleo** se condensa mientras el **citoplasma** se llena de hemoglobina; al final el núcleo se expulsa.', BLANCO, 15.5,
             name='Normal madura')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.0, 'Maduración **sincronizada**: núcleo y citoplasma avanzan juntos.', 'EAF5EA', 16, head='Normal', headfill=VERDE_OSC, name='Caja sincronía')
    s.step(fade(i['mo']))
    s.step(*[fade(i[k], after=(n > 0)) for n, k in enumerate(['c0', 'n0', 'c1', 'n1', 'c2', 'n2', 'c3'])])
    s.step(fade(c))
    s.step(fade(c2))
    s, i = escena_asin(D, 2)
    c = caja(s, 0.3, 5.45, 8.5, 1.6, 'El **citoplasma crece normalmente** (no necesita ADN para sintetizar proteínas y Hb); el **núcleo no puede duplicarse** y queda inmaduro → **célula grande con núcleo anómalo: megaloblasto**.',
             ROSA, 15, name='Asincronía')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.0, '**Asincronismo madurativo** entre núcleo y citoplasma.', AMA, 17, head='Megaloblástica', name='Caja asincronía')
    s.step(pulse(i['c2']), pulse(i['n2']), fade(c, after=True))
    s.step(fade(c2))
    s, i = escena_asin(D, 3)
    c = caja(s, 0.3, 5.45, 8.5, 1.6, 'Estas células son **frágiles**: muchas **abortan en la médula** (eritropoyesis ineficaz) y las que salen a la circulación **se destruyen rápidamente → hemólisis**.',
             ROSA, 15, name='Ineficaz')
    c2 = caja(s, 9.35, 1.2, 3.7, 3.0, 'Por eso en la megaloblástica pueden aumentar la **LDH** y la **bilirrubina** (destrucción celular).', BLANCO, 16, head='Consecuencia', name='Caja ineficaz')
    s.step(fade(c))
    s.step(fade(c2))
    registrar_morph(D, ini, len(D.slides), 'Maduración eritroide normal → asincronismo madurativo (megaloblasto) → eritropoyesis ineficaz',
                    ['!!MedulaOsea'] + ['!!Célula %d' % k for k in range(1, 5)] + ['!!Núcleo %d' % k for k in range(1, 4)],
                    'Las mismas cuatro células: en la secuencia megaloblástica crecen de tamaño mientras sus núcleos permanecen grandes y laxos.')


def pancitopenia(D):
    s = nueva(D, 3, 'Pancitopenia: todas las líneas que se dividen', src=['AN 7.1 Pancitopenia'], tipo='izq', c1=ROSA, c2=BLANCO)
    mo = medula_osea(s, 0.35, 1.25, 4.1, 3.0, name='!!MedulaOsea', celulas=6)
    lines = []
    for k, (t, d, c, f) in enumerate((('Glóbulos rojos bajos', 'anemia', 'gr', ROSA), ('Glóbulos blancos bajos', 'leucopenia → inmunosupresión', 'lc', LAVANDA),
                                      ('Plaquetas bajas', 'trombocitopenia → riesgo hemorrágico', 'pl', CREMA))):
        y = 1.25 + k * 1.95
        g = s.group_start('Línea ' + t)
        if c == 'gr':
            eritrocito(s, 5.0, y + 0.25, 1.1, name='GR panc')
        elif c == 'lc':
            leucocito(s, 5.0, y + 0.25, 1.1, 'neutrofilo', name='Lc panc')
        else:
            plaqueta(s, 5.05, y + 0.45, 1.0, name='Pl panc')
        s.shape(6.25, y + 0.35, 0.5, 0.9, 'downArrow', ROJO, (INK, 1.0), False)
        caja(s, 6.95, y + 0.05, 6.1, 1.55, '**%s**: %s' % (t, d), f, 17, anchor='m')
        lines.append(s.group_end())
    p = perla(s, 0.35, 4.5, 4.4, 2.55, 'Como el problema está en el **ADN**, afecta a **todos los linajes** que se dividen. Tres valores bajos en el hemograma → pensar en **megaloblástica**.', 15,
              head='Pancitopenia')
    s.step(fade(mo))
    for g in lines:
        s.step(fade(g))
    s.step(fade(p))


# ---------------------------------------------------------------- absorción de B12 (Morph)
B12_TXT = {1: 'Vitamina B_{12}: ingreso con los alimentos', 2: 'Llegada al estómago', 3: 'Factores gástricos: HCl y pepsina liberan la B_{12}',
           4: 'Unión al factor intrínseco', 5: 'Tránsito intestinal del complejo B_{12}–factor intrínseco', 6: 'Íleon terminal',
           7: 'Absorción y destino de la B_{12}', 8: 'Anemia perniciosa: sin factor intrínseco no hay absorción', 9: 'Consecuencia hematológica'}


def tracto(s):
    ids = {}
    ids['est'] = stomach(s, 0.35, 1.25, 3.1, name='!!Estomago')
    path_ = 'M 300 120 C 420 220 380 420 250 470 C 120 520 140 700 300 720 C 520 740 560 520 720 560 C 880 600 860 820 700 860 C 560 900 640 980 900 960'
    ids['int'] = s.free(2.2, 3.6, 6.8, 3.5, [(path_, False, True)], None, ('8E3B32', 22), name='!!Intestino delgado')
    ids['int2'] = s.free(2.2, 3.6, 6.8, 3.5, [(path_, False, True)], None, ('F0A39B', 16), name='!!Intestino luz')
    ids['lbl_int'] = texto(s, 3.1, 4.55, 1.8, 0.4, 'duodeno', 12, '922B21', True, 'c', name='!!Rótulo duodeno')
    ids['lbl_ile'] = texto(s, 7.3, 6.95, 1.6, 0.35, 'íleon terminal', 12, '922B21', True, 'c', name='!!Rótulo íleon')
    return ids


B12P = {1: (4.1, 1.35), 2: (1.25, 2.75), 3: (0.95, 2.6), 4: (0.95, 2.6), 5: (4.6, 5.0), 6: (7.65, 6.4), 7: (7.65, 5.65), 8: (8.25, 6.7), 9: (8.25, 6.7)}


def escena_b12(D, st):
    s = nueva(D, 3, B12_TXT[st], tipo='der', c1=ROJO, c2=ROSA, morph=st > 1, src=['AN 7.2 Absorción de B12', 'AN 7.3 Anemia perniciosa'], tw=8.7)
    ids = tracto(s)
    if st == 1:
        ids['plato'] = s.shape(3.8, 1.75, 1.9, 0.55, 'ellipse', shade('ECF0F1', 0.3, 0.2), ('7F8C8D', 1.5), False, name='!!Alimento')
    # célula parietal (gris en la anemia perniciosa)
    if st >= 3:
        ids['par'] = s.shape(2.45, 1.45, 0.95, 0.75, 'roundRect', shade('BDC3C7' if st >= 8 else 'A9DFBF', 0.4, 0.25), ('1E8449' if st < 8 else '5D6D7E', 1.25), False,
                             'parietal', 10.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), name='!!CelulaParietal', fit=False, adj={'adj': 30000})
    x, y = B12P[st]
    ids['b12'] = s.shape(x, y, 0.62, 0.62, 'ellipse', shade('E74C3C', 0.45, 0.25), ('922B21', 1.5), False, 'B_{12}', 12, F_HEAD, BLANCO, True, 'c', 'm', (0, 0, 0, 0),
                         name='!!B12', fit=False)
    if st <= 2:
        ids['prot'] = s.shape(x + 0.55, y - 0.05, 0.7, 0.7, 'ellipse', shade('F5B041', 0.45, 0.25), ('9C640C', 1.25), False, 'prot', 10.5, F_HEAD, INK, True, 'c', 'm',
                              (0, 0, 0, 0), name='!!Proteina alimentaria', fit=False)
    elif st == 3:
        ids['prot'] = s.shape(1.75, 3.45, 0.7, 0.7, 'ellipse', shade('F5B041', 0.45, 0.25), ('9C640C', 1.25), False, 'prot', 10.5, F_HEAD, INK, True, 'c', 'm',
                              (0, 0, 0, 0), name='!!Proteina alimentaria', fit=False)
    if 4 <= st <= 7:
        fx, fy = (x + 0.55, y + 0.05)
        ids['fi'] = s.shape(fx, fy, 0.62, 0.55, 'roundRect', shade('58D68D', 0.45, 0.25), ('1E8449', 1.25), False, 'FI', 13, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
                            name='!!FactorIntrinseco', fit=False, adj={'adj': 40000})
    if st >= 6:
        ids['ile'] = s.shape(6.8, 5.8, 2.3, 1.2, 'ellipse', None, (AMA2, 4.0, 'dash'), False, name='!!Ileon')
    if st >= 7:
        ids['vas'] = vessel(s, 4.9, 5.85, 1.85, 0.55, name='!!Vaso portal', rbcs=2)
        ids['mo'] = medula_osea(s, 5.45, 1.25, 3.4, 1.9, name='!!MedulaOsea', celulas=7 if st == 7 else 0)
    return s, ids


def absorcion_b12(D):
    ini = len(D.slides) + 1
    # 1
    s, i = escena_b12(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'La **vitamina B_{12} (cobalamina)** llega **unida a proteínas** de los alimentos: carnes, lácteos, huevos.', BLANCO, 15.5, head='Ingreso', name='Caja B1')
    s.step(fade(i['est']), fade(i['int'], after=True), fade(i['int2']), fade(i['lbl_int']), fade(i['lbl_ile']))
    s.step(fade(i['plato']), zoom(i['b12'], after=True), zoom(i['prot']))
    s.step(fade(c))
    # 2
    s, i = escena_b12(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 2.6, 'El complejo **B_{12}–proteína alimentaria** llega a la luz gástrica.', BLANCO, 16, head='Estómago', name='Caja B2')
    s.step(pulse(i['est']), fade(c, after=True))
    # 3
    s, i = escena_b12(D, 3)
    hcl = ficha(s, 0.55, 3.55, 'HCl', 'F4D03F', w=0.85, h=0.42, size=13, name='HCl')
    pep = ficha(s, 0.55, 4.05, 'pepsina', 'D7BDE2', w=1.1, h=0.42, size=12, name='Pepsina')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'El **ácido clorhídrico** y la **pepsina** rompen la unión B_{12}–proteínas alimentarias: queda **B_{12} libre**.', AMA, 15.5, head='Factores gástricos',
             name='Caja B3')
    s.step(fade(hcl), fade(pep, after=True))
    s.step(pulse(i['b12']), fade(c, after=True))
    # 4
    s, i = escena_b12(D, 4)
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'La B_{12} libre se une al **factor intrínseco (FI)**, producido por las **células parietales** gástricas.', 'EAF5EA', 15.5, head='Factor intrínseco',
             headfill=VERDE_OSC, name='Caja B4')
    s.step(pulse(i['par']), zoom(i['fi'], after=True))
    s.step(fade(c))
    # 5
    s, i = escena_b12(D, 5)
    c = caja(s, 9.35, 1.2, 3.7, 2.8, 'El complejo **B_{12}–FI** recorre el intestino delgado sin absorberse hasta el segmento final.', BLANCO, 15.5, head='Tránsito', name='Caja B5')
    s.step(fade(c))
    # 6
    s, i = escena_b12(D, 6)
    c = caja(s, 9.35, 1.2, 3.7, 2.8, 'El complejo B_{12}–factor intrínseco **se absorbe en el íleon terminal**.', 'EAF5EA', 16, head='Íleon', headfill=VERDE_OSC, name='Caja B6')
    s.step(fade(i['ile']), pulse(i['ile'], after=True))
    s.step(fade(c))
    # 7
    s, i = escena_b12(D, 7)
    adn = s.group_start('ADN')
    for k in range(5):
        s.shape(6.0 + k * 0.45, 3.35 + (k % 2) * 0.12, 0.4, 0.26, 'ellipse', '2E86C1' if k % 2 else 'E74C3C', None, False)
    texto(s, 5.7, 3.7, 3.0, 0.4, 'síntesis de ácidos nucleicos', 12.5, NAVY, True, 'c')
    s.group_end()
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Una vez absorbida, la B_{12} participa (junto con el **ácido fólico**) en la **síntesis de ácidos nucleicos**: la médula ósea la necesita para dividir sus células.',
             BLANCO, 15, head='Destino', name='Caja B7')
    s.step(fade(i['vas']), fade(i['mo'], after=True))
    s.step(fade(adn), fade(c, after=True))
    # 8
    s, i = escena_b12(D, 8)
    x_ = s.shape(2.5, 1.25, 0.9, 0.9, 'rect', None, None, False, 'X', 34, F_HEAD, ROJO, True, 'c', 'm', (0, 0, 0, 0), name='Sin FI', fit=False)
    c = caja(s, 9.35, 1.2, 3.7, 3.5, 'En la **anemia perniciosa** falta el **factor intrínseco** (generalmente por **gastritis atrófica autoinmune**): la B_{12} **no se absorbe aunque esté en la dieta**.',
             ROSA, 15, head='Perniciosa', headfill=ROJO, name='Caja B8')
    c2 = caja(s, 9.35, 4.95, 3.7, 2.1, 'Defecto de **absorción**, no nutricional: la paciente puede tener una dieta perfecta.', BLANCO, 15, name='No nutricional')
    s.step(zoom(x_), fade(c, after=True))
    s.step(pulse(i['b12']), fade(c2, after=True))
    # 9
    s, i = escena_b12(D, 9)
    meg = s.group_start('Megaloblastos médula')
    for k in range(3):
        megaloblasto(s, 5.75 + k * 1.0, 1.55, 0.95, name='Megaloblasto %d' % k)
    s.group_end()
    c = caja(s, 9.35, 1.2, 3.7, 3.6, 'Sin B_{12} la médula no sintetiza ADN correctamente: **macrocitosis, megaloblastos y pancitopenia**. El cuadro es **idéntico** al del déficit nutricional de B_{12}.',
             ROSA, 15, head='Consecuencia', headfill=ROJO, name='Caja B9')
    s.step(fade(meg))
    s.step(fade(c))
    registrar_morph(D, ini, len(D.slides), 'Absorción de vitamina B12: alimento → estómago → HCl/pepsina → factor intrínseco → intestino → íleon terminal → absorción → anemia perniciosa → consecuencia',
                    ['!!Estomago', '!!Intestino delgado', '!!Intestino luz', '!!B12', '!!Proteina alimentaria', '!!CelulaParietal', '!!FactorIntrinseco', '!!Ileon', '!!Vaso portal',
                     '!!MedulaOsea'],
                    'La ficha de B12 viaja del plato al estómago, se separa de la proteína, se une al factor intrínseco y recorre el intestino hasta el íleon; '
                    'en la anemia perniciosa la célula parietal se vuelve gris, desaparece el FI y la B12 sigue de largo.')


def dx_perniciosa(D):
    s = nueva(D, 3, '¿Perniciosa o déficit nutricional? El razonamiento diagnóstico', src=['AN 7.3 Diagnóstico perniciosa', 'REV AN 7.3'], tipo='izq', c1=ROSA, c2=BLANCO)
    pasos = [('Paso 1', 'Solicitar **B_{12} sérica y ácido fólico**: en ambas condiciones pueden estar bajos.', CELESTE),
             ('Paso 2', 'Dar suplementos: en el déficit nutricional **mejora**; en la perniciosa la B_{12} **por vía oral habitual no se absorbe**.', CREMA),
             ('Paso 3', '**Test de Schilling**: B_{12} radiactiva + factor intrínseco; si la B_{12} marcada se absorbe y aparece en orina, el problema era la falta de FI.', ROSA)]
    ids = []
    for k, (t, d, f) in enumerate(pasos):
        g = s.group_start('Diagnóstico %s' % t)
        num(s, 0.5, 1.45 + k * 1.75, k + 1, d=0.6)
        caja(s, 1.25, 1.2 + k * 1.75, 7.4, 1.55, d, f, 15.5, anchor='m')
        ids.append(s.group_end())
    tr = caja(s, 0.5, 6.4, 8.15, 0.7, 'Tratamiento: **B_{12} intramuscular** (saltea la absorción intestinal).', AMA, 15.5, anchor='m', name='Tratamiento B12')
    r_ = rigor(s, 9.0, 1.2, 4.05, 5.9, '- El **test de Schilling** prácticamente **ya no se utiliza**.\n- El tratamiento estándar es la **B_{12} parenteral** (o dosis orales altas en algunos casos); '
               'administrar **factor intrínseco** no es la terapia habitual.\n- «Suplementos que no mejoran» se refiere a la vía oral en dosis habituales.', 13.5, name='Rigor perniciosa')
    for g in ids:
        s.step(fade(g))
    s.step(fade(tr))
    s.step(fade(r_))


def folico(D):
    s = nueva(D, 3, 'Ácido fólico y depósitos: dos relojes distintos', src=['AN 7.4 Ácido fólico'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    X, Y = 0.6, 2.0
    eje = s.group_start('Línea de tiempo')
    s.arrow([(X, 3.8), (8.7, 3.8)], INK, 2.5)
    for k, t in enumerate(('0', '3 meses', '1 año', '2 años', '3 años', '4 años')):
        xx = X + 0.2 + k * 1.55
        s.arrow([(xx, 3.7), (xx, 3.9)], INK, 1.5, tail=None)
        texto(s, xx - 0.6, 3.95, 1.2, 0.35, t, 12.5, INK, True, 'c')
    s.group_end()
    fo = s.shape(X + 0.2, 2.6, 1.55, 0.6, 'rect', ('lin', [(0, 'A9DFBF'), (100, '27AE60')], 0), (INK, 1.25), False, 'ácido fólico', 13, F_HEAD, INK, True, 'c', 'm',
                 name='Barra fólico')
    b1 = s.shape(X + 0.2, 1.75, 1.55 * 4.5, 0.6, 'rect', ('lin', [(0, 'F5B7B1'), (100, 'C0392B')], 0), (INK, 1.25), False, 'vitamina B_{12} (depósitos hepáticos)', 13, F_HEAD,
                 BLANCO, True, 'c', 'm', name='Barra B12')
    c1 = caja(s, 0.5, 4.6, 4.0, 2.45, 'Déficit de **ácido fólico**: carencia nutricional de **3 meses** como mínimo.', 'EAF5EA', 16, name='Fólico 3 meses')
    c2 = caja(s, 4.75, 4.6, 4.0, 2.45, 'Déficit de **B_{12}**: carencia de **3–4 años** (grandes depósitos hepáticos).', ROSA, 16, name='B12 años')
    fu = caja(s, 9.35, 1.2, 3.7, 2.7, '**Tetrahidrofolato (THF)**. Fuentes: frutas, verduras y cereales (origen animal y vegetal). Trabaja **junto con la B_{12}** en la síntesis de nucleótidos.',
              BLANCO, 14.5, head='Ácido fólico', name='Fuentes fólico')
    ri = caja(s, 9.35, 4.15, 3.7, 2.9, 'Condiciones de riesgo: **embarazo, alcoholismo, malabsorción intestinal, dietas extremas**.', AMA, 15.5, head='Riesgo', name='Riesgo fólico')
    s.step(fade(eje))
    s.step(wipe(fo, 'l'), fade(c1, after=True))
    s.step(wipe(b1, 'l', dur=1200), fade(c2, after=True))
    s.step(fade(fu))
    s.step(fade(ri))


# ---------------------------------------------------------------- biomarcadores
def ldh(D):
    s = nueva(D, 3, 'LDH: marcador de destrucción celular', src=['AN 8.1 LDH'], tipo='bandas', c1=ROSA, c2=CREMA)
    org = s.group_start('Tejidos con LDH')
    corazon_anat(s, 0.45, 1.25, 1.35, name='Corazón LDH', coronarias=False)
    liver(s, 1.9, 1.5, 1.35, name='Hígado LDH')
    muscle(s, 0.4, 3.0, 1.5, name='Músculo LDH', fibers=2)
    kidney(s, 2.3, 2.75, 0.65, name='Riñón LDH')
    eritrocito(s, 0.5, 4.35, 0.9, name='GR LDH')
    s.group_end()
    gr = eritrocito(s, 4.1, 2.1, 1.7, name='!!Eritrocito hemólisis')
    frag = s.group_start('Lisis')
    for k in range(6):
        a = 2 * math.pi * k / 6
        s.shape(4.9 + 1.2 * math.cos(a), 2.85 + 1.0 * math.sin(a), 0.36, 0.36, 'ellipse', shade('E59866', 0.4, 0.2), ('784212', 1.0), False, 'LDH', 7, F_HEAD, INK, True,
                'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    c1 = caja(s, 3.55, 4.4, 6.5, 2.65, '- Presente en prácticamente **todos los tejidos**: corazón, hígado, músculo, riñón, pulmón, **eritrocitos**, tejido linfoide.\n- Normal: **100–190 U/L** (según el laboratorio).\n'
              '- Elevada: **destrucción celular** (necrosis o lisis). En anemia orienta a **hemólisis**.', BLANCO, 14.5, name='Datos LDH')
    lim = caja(s, 10.3, 1.2, 2.75, 2.8, '**No es órgano-específica**: dice que algo se destruye, no dónde.', ROSA, 15, head='Limitación', headfill=ROJO, name='Limitación LDH')
    iso = caja(s, 10.3, 4.25, 2.75, 2.8, '**Isoenzimas** LDH1–LDH5: misma reacción, distinto origen. **LDH1 cardíaca**, **LDH5 hepática/muscular**.', CELESTE, 14, name='Isoenzimas LDH')
    s.step(fade(org))
    s.step(fade(gr), out(gr, after=True, delay=300), fade(frag, after=True))
    s.step(fade(c1))
    s.step(fade(lim))
    s.step(fade(iso))


def bilirrubina(D):
    s = nueva(D, 3, 'Bilirrubina: del grupo hemo a la ictericia', src=['AN 8.2 Bilirrubina', 'PA 2.6 Bilirrubina'], tipo='der', c1=ROJO, c2=BLANCO)
    gr = eritrocito(s, 0.4, 1.45, 1.3, name='GR origen')
    hemo = molecula3d(s, 2.05, 1.3, 1.5, 'hemo', name='Hemo')
    bi = ficha(s, 3.85, 1.75, 'Bilirrubina indirecta', 'F4D03F', w=2.3, h=0.5, size=13, name='!!BI')
    alb = proteina_bola(s, 6.25, 1.65, 0.7, 'F9E79F', 'Alb', name='Albúmina BI')
    hig = liver(s, 3.9, 3.0, 3.0, name='Hígado bilirrubina')
    bd = ficha(s, 7.1, 3.6, 'Bilirrubina directa', '27AE60', w=1.9, h=0.5, size=13, name='!!BD')
    flech = s.group_start('Flechas bilirrubina')
    s.arrow([(1.75, 2.1), (2.05, 2.05)], INK, 2.5); s.arrow([(3.5, 2.0), (3.8, 2.0)], INK, 2.5)
    s.arrow([(5.0, 2.3), (5.2, 3.0)], INK, 2.5); s.arrow([(6.6, 3.85), (7.05, 3.85)], INK, 2.5)
    texto(s, 4.6, 4.95, 2.6, 0.4, 'conjugación hepática', 13, '641E16', True, 'c')
    s.group_end()
    rows = [['Fracción', 'Normal', 'Si está elevada'], ['Total', '< 1 mg/dL', 'Hemólisis y/o disfunción hepática'],
            ['Directa (conjugada)', '< 0,2 mg/dL', 'Problema hepático o posthepático'], ['Indirecta (no conjugada)', '< 0,8 mg/dL', 'Problema **prehepático → hemólisis**']]
    ids, H = tabla_filas(s, 0.4, 5.35 - 0.0, [2.6, 1.6, 4.5], rows, rowh=0.42, size=13.5, name='Tabla bilirrubina')
    c = caja(s, 9.35, 1.2, 3.7, 2.9, 'En la anemia **hemolítica** sube la **indirecta**: llega mucho hemo al hígado antes de conjugarse; la directa es normal si el hígado funciona.', BLANCO, 14.5,
             head='Hemólisis', name='Hemólisis bilirrubina')
    ic = caja(s, 9.35, 4.35, 3.7, 2.7, 'Bilirrubina total > **2–3 mg/dL** → tiñe piel y mucosas: **ictericia**.', AMA, 16, head='Ictericia', name='Ictericia')
    s.step(fade(gr), fade(hemo, after=True))
    s.step(fade(bi), fade(alb, after=True))
    s.step(fade(hig), fade(flech, after=True), fade(bd, after=True))
    s.step(*[fade(r, after=(k > 0)) for k, r in enumerate(ids)])
    s.step(fade(c))
    s.step(fade(ic))


def neonatal(D):
    s = nueva(D, 3, 'Anemia fisiológica e ictericia del recién nacido', src=['AN 11.1 Anemia fisiológica del RN', 'AN 8.2 Ictericia neonatal', 'REV AN 8.2'], tipo='izq', c1=CREMA, c2=BLANCO)
    bebe = s.group_start('!!Recién nacido')
    s.shape(1.2, 1.6, 2.2, 1.6, 'ellipse', shade('F8C471', 0.4, 0.2), ('9C640C', 1.5), False)
    s.shape(2.9, 1.4, 1.2, 1.2, 'ellipse', shade('F8C471', 0.4, 0.2), ('9C640C', 1.5), False)
    s.group_end()
    luz = s.group_start('Fototerapia')
    s.shape(0.6, 0.95, 4.0, 0.3, 'rect', '5DADE2', (INK, 1.0), False)
    for k in range(6):
        s.arrow([(0.9 + k * 0.6, 1.3), (0.9 + k * 0.6, 1.6)], '2E86C1', 2.5)
    s.group_end()
    o2 = caja(s, 0.4, 3.5, 4.0, 1.7, 'Al nacer pasa de baja concentración de O_{2} a respirar aire con **21 % de O_{2}**: el **estrés oxidativo** destruye eritrocitos fetales.', ROSA, 14,
              name='Estrés oxidativo')
    c1 = caja(s, 4.95, 1.2, 8.1, 1.4, 'Hemólisis fisiológica en las primeras semanas → mucho hemo → **bilirrubina elevada → ictericia fisiológica neonatal**.', AMA, 16, name='Ictericia RN')
    c2 = caja(s, 4.95, 2.8, 8.1, 1.3, 'La bilirrubina en exceso puede ser **neurotóxica (kernicterus)**: se trata con **fototerapia**.', ROSA, 16, name='Kernicterus')
    c3 = caja(s, 4.95, 4.3, 8.1, 1.3, '**Nadir** de Hb ≈ **3 meses** de vida (~9,5 g/dL); los valores del adulto se alcanzan hacia los **11–12 años**.', CELESTE, 16, name='Nadir')
    r_ = rigor(s, 0.4, 5.45, 12.65, 1.6, 'La fototerapia neonatal usa **luz azul (≈ 460 nm)**, no ultravioleta: la bilirrubina absorbe esa luz y se **fotoisomeriza** a formas más hidrosolubles que se eliminan. '
               'El mecanismo de la hemólisis neonatal es multifactorial (vida media más corta del eritrocito fetal).', 13.5, name='Rigor fototerapia')
    s.step(fade(bebe), fade(o2, after=True))
    s.step(fade(c1))
    s.step(fade(c2), fade(luz, after=True))
    s.step(fade(c3))
    s.step(fade(r_))


def coombs(D):
    s = nueva(D, 3, 'Prueba de Coombs: anticuerpos sobre el eritrocito', src=['AN 8.3 Prueba de Coombs', 'REV AN 8.3'], tipo='der', c1=ROJO, c2=ROSA)
    grs = []
    for k in range(3):
        g = s.group_start('!!Eritrocito Coombs %d' % k)
        eritrocito(s, 0.8 + k * 2.1, 2.2, 1.6, name='GR c%d' % k)
        s.group_end(); grs.append(g)
    abs_ = s.group_start('Autoanticuerpos')
    for k in range(3):
        for j in range(3):
            a = math.radians(-60 + j * 60)
            cx = 1.6 + k * 2.1 + 0.9 * math.cos(a); cy = 3.0 + 0.9 * math.sin(a)
            s.arrow([(cx, cy), (cx + 0.3 * math.cos(a), cy + 0.3 * math.sin(a))], '2E86C1', 3, tail=None)
    s.group_end()
    anti = s.group_start('Antiglobulina')
    for k in range(2):
        x = 2.85 + k * 2.1
        s.arrow([(x - 0.3, 2.35), (x, 2.0), (x + 0.3, 2.35)], '8E44AD', 3.5, tail=None)
    texto(s, 2.2, 1.2, 4.0, 0.4, 'reactivo de Coombs (antiglobulina)', 13, '6C3483', True, 'c')
    s.group_end()
    agl = rotulo(s, 2.6, 4.25, 'aglutinación = POSITIVA', ROJO, 15, name='Aglutinación')
    c1 = caja(s, 0.5, 5.0, 8.3, 2.05, 'Detecta **autoanticuerpos** (inmunoglobulinas) adheridos a la superficie del eritrocito.\n**Positiva** → anemia hemolítica **autoinmune** · **Negativa** → no es de origen autoinmune.',
              BLANCO, 15, name='Def Coombs')
    c2 = caja(s, 9.35, 1.2, 3.7, 2.7, 'Si es autoinmune hay hemólisis periférica: esperamos una anemia **regenerativa**. Arregenerativa con Coombs + → **revisar el diagnóstico**.', AMA, 14,
              head='Coherencia', name='Coherencia Coombs')
    r_ = rigor(s, 9.35, 4.15, 3.7, 2.9, 'La regla «siempre regenerativa» admite excepciones: algunos pacientes con hemólisis autoinmune presentan **reticulocitopenia** transitoria (p. ej., por afectación medular asociada).',
               13, name='Rigor Coombs')
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(grs)])
    s.step(fade(abs_))
    s.step(fade(anti), fade(agl, after=True))
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(r_))


def vsg(D):
    s = nueva(D, 3, 'Eritrosedimentación (VSG)', src=['AN 8.4 Eritrosedimentación', 'REV AN 8.4'], tipo='izq', c1=ROSA, c2=BLANCO)
    t1 = tubo(s, 1.0, 1.4, 0.75, 4.6, [(0.72, 'B3261E', 'GR normal'), (0.1, 'F7DC6F', 'P normal')], tapa='34495E', name='Pipeta normal', etiqueta='VSG normal', grupo='Pipeta VSG normal')
    t2 = tubo(s, 2.7, 1.4, 0.75, 4.6, [(0.45, '922B21', 'GR rapida'), (0.37, 'F7DC6F', 'P rapida')], tapa='34495E', name='Pipeta elevada', etiqueta='VSG elevada', grupo='Pipeta VSG elevada')
    car = s.group_start('Carga negativa')
    for k in range(3):
        eritrocito(s, 4.0 + k * 0.7, 1.4, 0.6, name='GR z%d' % k)
        texto(s, 4.1 + k * 0.7, 2.0, 0.4, 0.3, '−', 18, NAVY, True, 'c')
    s.group_end()
    c1 = caja(s, 4.0, 2.5, 4.8, 2.0, 'Velocidad a la que los eritrocitos sedimentan en una pipeta en **1 hora**. Su carga negativa (**potencial Z**) hace que se repelan y sedimenten lentamente.',
              BLANCO, 14, name='Principio VSG')
    c2 = caja(s, 4.0, 4.7, 4.8, 2.35, 'Si cambian las proteínas plasmáticas (**fibrinógeno**, proteínas de fase aguda), los eritrocitos pierden carga, **se agregan y sedimentan más rápido** → proceso inflamatorio o infección.',
              ROSA, 14, name='VSG elevada')
    v = caja(s, 9.15, 1.2, 3.9, 2.0, 'Normal: **5–10 mm/h**. **No es específica**: solo orienta que «algo está pasando».', AMA, 15, name='Valor VSG')
    r_ = rigor(s, 9.15, 3.45, 3.9, 3.6, 'El intervalo de la VSG **varía con la edad y el sexo** (en general más alto en mujeres y en adultos mayores); 5–10 mm/h no aplica a todos los pacientes.',
               13.5, name='Rigor VSG')
    s.step(fade(t1), fade(t2, after=True))
    s.step(fade(car), fade(c1, after=True))
    s.step(fade(c2))
    s.step(fade(v))
    s.step(fade(r_))


# ---------------------------------------------------------------- casos clínicos
def caso1(D):
    # presentación
    s = nueva(D, 3, 'Caso clínico 1: presentación', src=['AN 9 Caso 1'], tipo='der', c1=ROJO, c2=ROSA)
    p = caso_cabecera(s, 0.4, 1.2, 8.4, 'Mujer de 55 años', 'Disnea de esfuerzo que se intensificó en las últimas horas.')
    a1 = caja(s, 0.4, 3.0, 4.1, 1.7, '**Antecedente**: hipotiroidismo diagnosticado hace 8 años, bien controlado con levotiroxina.', BLANCO, 15, name='Antecedente C1')
    a2 = caja(s, 4.7, 3.0, 4.1, 1.7, '**Dieta**: variada, con carnes y verduras.', BLANCO, 16, name='Dieta C1')
    q = caja(s, 0.4, 4.95, 8.4, 2.1, '¿Qué datos necesitamos para decidir **si hay anemia**, **de qué tipo** y **por qué mecanismo**?', AMA, 17, anchor='m', name='Pregunta C1')
    h = human(s, 10.1, 1.1, 5.9, name='Silueta C1')
    s.step(fade(p), fade(h, after=True))
    s.step(fade(a1))
    s.step(fade(a2))
    s.step(fade(q))
    # signos
    s = nueva(D, 3, 'Caso clínico 1: signos vitales y examen físico', src=['AN 9 Caso 1'], tipo='izq', c1=ROSA, c2=BLANCO)
    sv = signos_vitales(s, 0.4, 1.3, [('TA', '110/70', True), ('FC', '110 lpm', True), ('Temp.', '35,9 °C', False), ('FR', '22 rpm', True), ('SatO_{2}', '95 %', False)],
                        w=2.35, h=1.1, gap=0.17)
    ex = caja(s, 0.4, 2.75, 6.1, 1.4, '**Examen físico**: palidez de piel y mucosas.', ROSA, 18, anchor='m', name='Examen C1')
    i1 = caja(s, 6.7, 2.75, 6.35, 1.4, 'FC 110: **taquicardia compensatoria** · FR 22: taquipnea leve · TA levemente baja.', BLANCO, 15, anchor='m', name='Lectura signos C1')
    hu = human(s, 0.6, 4.35, 2.8, name='Paciente palidez', fill='F2E6DF')
    c = caja(s, 2.4, 4.4, 10.65, 2.65, 'Los signos son compatibles con un organismo que **compensa** una menor capacidad de transporte de O_{2}. Falta el laboratorio para confirmar y clasificar.',
             AMA, 16, anchor='m', name='Síntesis signos C1')
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(sv)])
    s.step(fade(ex), fade(hu, after=True))
    s.step(fade(i1))
    s.step(fade(c))
    # laboratorio 1
    s = nueva(D, 3, 'Caso clínico 1: hemograma', src=['AN 9 Caso 1 Laboratorio'], tipo='der', c1=ROJO, c2=BLANCO)
    rows = [['Parámetro', 'Paciente', 'Referencia', 'Lectura'], ['Hemoglobina', '8 g/dL', '12–16 g/dL', '**Baja → anemia**'], ['Hematocrito', '25 %', '36–47 %', 'Bajo (8 × 3 = 24)'],
            ['Eritrocitos', '2,6 × 10^{12}/L', '4,2–5,4 × 10^{12}/L', 'Disminuidos'], ['VCM', '100 fL', '80–100 fL', 'Límite superior: tendencia macrocítica'],
            ['HCM', 'Normal', '27–32 pg', 'Normocrómico'], ['CHCM', 'Normal', '32–36 g/dL', 'Normal: descarta esferocitosis']]
    ids, H = tabla_filas(s, 0.35, 1.2, [1.75, 1.65, 2.15, 3.1], rows, rowh=0.62, size=14.5, name='Laboratorio C1a')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Primera lectura: hay **anemia** y el tamaño eritrocitario está en el **límite superior**.', AMA, 16, name='Lectura C1a')
    g = eritrocito(s, 10.2, 4.6, 2.0, name='GR caso 1')
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c), fade(g, after=True))
    # laboratorio 2
    s = nueva(D, 3, 'Caso clínico 1: otras líneas y marcadores', src=['AN 9 Caso 1 Laboratorio', 'REV AN 9 Caso 1'], tipo='der', c1=ROJO, c2=BLANCO)
    rows = [['Parámetro', 'Paciente', 'Referencia', 'Lectura'], ['Leucocitos', '3.000/mm^{3}', '4.500–11.000/mm^{3}', '**Leucopenia**'],
            ['Plaquetas', '80.000/mm^{3}', '150.000–400.000/mm^{3}', '**Trombocitopenia**'], ['Reticulocitos', '8 %', '0,5–2 %', 'Ver nota de rigor'],
            ['LDH', 'Elevada', '100–190 U/L', 'Destrucción celular'], ['Bilirrubina total', 'Elevada', '< 1 mg/dL', 'Más catabolismo del hemo'],
            ['Bilirrubina directa', 'Normal', '< 0,2 mg/dL', 'Problema prehepático'], ['Coombs', 'Negativa', 'Negativa', 'No autoinmune']]
    ids, H = tabla_filas(s, 0.35, 1.2, [1.85, 1.6, 2.35, 2.85], rows, rowh=0.62, size=14, name='Laboratorio C1b')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'En el material el valor de reticulocitos figura como **8 %** y se lo interpreta como «normal (arregenerativa)». Con el intervalo 0,5–2 %, **8 % está elevado**: '
               'el dato es **inconsistente** con el resto del cuadro. La conclusión arregenerativa se apoya en el mecanismo (síntesis de ADN, pancitopenia) y requiere **verificar el recuento**.',
               13.5, name='Rigor reticulocitos caso 1')
    s.step(fade(ids[0]))
    s.step(fade(ids[1]), fade(ids[2], after=True))
    s.step(fade(ids[3]))
    s.step(fade(ids[4]), fade(ids[5], after=True), fade(ids[6], after=True))
    s.step(fade(ids[7]))
    s.step(fade(r_))
    # interpretación
    s = nueva(D, 3, 'Caso clínico 1: integración del razonamiento', src=['AN 9 Caso 1 Análisis'], tipo='izq', c1=ROSA, c2=BLANCO)
    pasos = [('Morfología', 'Macrocítica (VCM en el límite superior) normocrómica.', CELESTE), ('Etiopatogenia', 'Arregenerativa según el material: la médula no responde.', CREMA),
             ('Pancitopenia', 'Tres linajes afectados → problema de **síntesis de ADN → megaloblástica**.', ROSA),
             ('LDH y bilirrubina ↑', 'Destrucción celular: eritropoyesis ineficaz + hemólisis de células defectuosas.', LAVANDA),
             ('Bilirrubina directa normal', 'El hígado funciona: la hemólisis es **prehepática**.', 'EAF5EA'), ('Coombs negativa', 'Descarta origen autoinmune.', CELESTE),
             ('Dieta normal', 'Descarta déficit **nutricional** de B_{12} o ácido fólico.', AMA)]
    ids = []
    for k, (t, d, f) in enumerate(pasos):
        x = 0.4 + (k % 2) * 6.35; y = 1.2 + (k // 2) * 1.47
        ids.append(caja(s, x, y, 6.15, 1.32, '**%s**: %s' % (t, d), f, 15, anchor='m', name='Integración C1 %d' % (k + 1)))
    for g in ids:
        s.step(fade(g))
    # conclusión
    s = nueva(D, 3, 'Caso clínico 1: conclusión', src=['AN 9 Caso 1 Diagnóstico final'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    est = stomach(s, 0.6, 1.3, 2.6, name='Estómago C1')
    par = s.shape(2.3, 1.5, 0.9, 0.7, 'roundRect', shade('BDC3C7', 0.4, 0.25), ('5D6D7E', 1.25), False, 'parietal', 10.5, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0),
                  name='Parietal C1', fit=False, adj={'adj': 30000})
    x_ = s.shape(2.4, 1.3, 0.8, 0.8, 'rect', None, None, False, 'X', 30, F_HEAD, ROJO, True, 'c', 'm', (0, 0, 0, 0), name='Sin FI C1', fit=False)
    con = conclusion(s, 3.7, 1.2, 5.3, 3.2, '**ANEMIA PERNICIOSA**: déficit de **factor intrínseco** (no de B_{12} en la dieta). La paciente come bien, pero la B_{12} no se absorbe → mismo cuadro que el déficit de B_{12}.',
                     title='Diagnóstico final', size=16)
    cf = caja(s, 0.5, 4.65, 8.5, 2.4, '**Confirmación** propuesta en el material: test de Schilling (B_{12} radiactiva + FI).\n**Tratamiento**: B_{12} intramuscular, que saltea la absorción intestinal.',
              BLANCO, 15.5, name='Confirmación C1')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'El antecedente de **hipotiroidismo** (enfermedad autoinmune frecuente) es coherente con una **gastritis atrófica autoinmune**. '
               'El Schilling está en desuso; la conducta habitual es la **B_{12} parenteral**.', 13.5, name='Rigor C1')
    s.step(fade(est), fade(par, after=True), zoom(x_, after=True))
    s.step(fade(con))
    s.step(fade(cf))
    s.step(fade(r_))


def caso2(D):
    s = nueva(D, 3, 'Caso clínico 2: presentación', src=['AN 9 Caso 2'], tipo='der', c1=ROJO, c2=ROSA)
    p = caso_cabecera(s, 0.4, 1.2, 8.4, 'Mujer de 45 años', 'Adinamia severa en las últimas 24 h, palidez, palpitaciones y disnea.')
    a1 = caja(s, 0.4, 3.0, 8.4, 1.5, '**Antecedente**: 4 abortos espontáneos (dato relevante: posible patología autoinmune subyacente).', BLANCO, 16, anchor='m', name='Antecedente C2')
    q = caja(s, 0.4, 4.75, 8.4, 2.3, 'Instalación **aguda** y síntomas intensos: ¿pérdida, destrucción o falla de producción?', AMA, 17, anchor='m', name='Pregunta C2')
    h = human(s, 10.1, 1.1, 5.9, name='Silueta C2', fill='FCE4A8')
    s.step(fade(p), fade(h, after=True))
    s.step(fade(a1))
    s.step(fade(q))
    s = nueva(D, 3, 'Caso clínico 2: signos vitales y examen físico', src=['AN 9 Caso 2'], tipo='izq', c1=ROSA, c2=BLANCO)
    sv = signos_vitales(s, 0.4, 1.3, [('TA', '95/60', True), ('FC', '125 lpm', True), ('Temp.', 'normal', False), ('FR', '28 rpm', True), ('SatO_{2}', '90 %', True)],
                        w=2.35, h=1.1, gap=0.17)
    ex = caja(s, 0.4, 2.75, 6.1, 1.6, '**Examen físico**: **ictericia** (piel y mucosas amarillas) + **esplenomegalia**.', AMA, 17, anchor='m', name='Examen C2')
    i1 = caja(s, 6.7, 2.75, 6.35, 1.6, 'Hipotensión, taquicardia importante, taquipnea y desaturación significativa: **descompensación**.', ROSA, 15.5, anchor='m', name='Lectura signos C2')
    hu = human(s, 0.6, 4.6, 2.5, name='Paciente ictericia', fill='F7DC6F')
    bazo = s.free(3.4, 4.9, 1.6, 1.1, smooth([(100, 300), (500, 50), (950, 250), (900, 750), (400, 950), (50, 700)]), shade('8E44AD', 0.4, 0.3), ('4A235A', 1.5),
                  name='Bazo aumentado')
    c = caja(s, 5.3, 4.6, 7.75, 2.45, 'Ictericia + esplenomegalia orientan a **destrucción de eritrocitos**: hay que confirmarlo con el laboratorio.', BLANCO, 16, anchor='m', name='Síntesis signos C2')
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(sv)])
    s.step(fade(ex), fade(hu, after=True), fade(bazo, after=True))
    s.step(fade(i1))
    s.step(fade(c))
    s = nueva(D, 3, 'Caso clínico 2: laboratorio', src=['AN 9 Caso 2 Laboratorio'], tipo='der', c1=ROJO, c2=BLANCO)
    rows = [['Parámetro', 'Paciente', 'Referencia', 'Lectura'], ['Hemoglobina', '5,5 g/dL', '12–16 g/dL', '**Gravemente baja**'], ['Hematocrito', '18 %', '36–47 %', 'Muy bajo (5,5 × 3 ≈ 16,5)'],
            ['Eritrocitos', '2.100.000/mm^{3}', '4,2–5,4 × 10^{6}', 'Marcadamente disminuidos'], ['VCM', '88 fL', '80–100 fL', '**Normocítica**'],
            ['HCM / CHCM', 'Límite inf. / normal', '27–32 pg / 32–36 g/dL', 'Normocrómica; descarta esferocitosis'], ['Leucocitos / plaquetas', 'Normales / 275.000', '—', 'Conservados'],
            ['Reticulocitos', '8 %', '0,5–2 %', '**Elevados → regenerativa**'], ['LDH', 'Muy elevada', '100–190 U/L', '**Hemólisis activa**'],
            ['Eritrosedimentación', '37 mm/h', '5–10 mm/h', 'Muy elevada'], ['Coombs', 'Pendiente', 'Negativa', 'Debe solicitarse']]
    ids, H = tabla_filas(s, 0.35, 1.15, [2.05, 1.85, 2.15, 2.6], rows, rowh=0.52, size=13, name='Laboratorio C2')
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Anemia **grave**, normocítica, con **reticulocitos altos** y **LDH muy elevada**.', AMA, 16, name='Lectura C2')
    rr = reticulocito(s, 10.3, 4.6, 1.8, name='Reti C2')
    s.step(fade(ids[0]))
    for k in range(1, len(ids), 2):
        s.step(fade(ids[k]), *([fade(ids[k + 1], after=True)] if k + 1 < len(ids) else []))
    s.step(fade(c), fade(rr, after=True))
    s = nueva(D, 3, 'Caso clínico 2: integración y conclusión', src=['AN 9 Caso 2 Análisis', 'AN 9 Caso 2 Diagnóstico final', 'REV AN 9 Caso 2'], tipo='izq', c1=ROSA, c2=BLANCO)
    pasos = [('Morfología', 'Normocítica normocrómica (VCM 88 fL).', CELESTE), ('Regenerativa', 'Reticulocitos 8 %: la médula responde.', 'EAF5EA'),
             ('Hemorragia o hemólisis', 'Ictericia + LDH alta: **hemólisis** (en la hemorragia no hay ictericia).', ROSA),
             ('Esplenomegalia', 'El bazo aumentado destruye eritrocitos en exceso: **hiperesplenismo**.', LAVANDA), ('VSG elevada', 'Proceso inflamatorio activo.', CREMA),
             ('Abortos a repetición', 'Orientan a síndrome antifosfolipídico u otra autoinmunidad.', CELESTE)]
    ids = []
    for k, (t, d, f) in enumerate(pasos):
        x = 0.4 + (k % 2) * 4.3; y = 1.2 + (k // 2) * 1.32
        ids.append(caja(s, x, y, 4.15, 1.2, '**%s**: %s' % (t, d), f, 13.5, anchor='m', name='Integración C2 %d' % (k + 1)))
    con = conclusion(s, 0.4, 5.25, 8.45, 1.8, '**Anemia hemolítica por hiperesplenismo** (más probable): normocítica normocrómica, heterogénea, regenerativa. Solicitar **Coombs**. Hb 5,5 g/dL → transfusión.',
                     title='Diagnóstico', size=14.5)
    r_ = rigor(s, 9.1, 1.2, 3.95, 5.85, '- Con abortos a repetición, VSG alta y Coombs pendiente, una **anemia hemolítica autoinmune** sigue siendo una alternativa importante hasta conocer el Coombs.\n'
               '- La transfusión se decide por la **gravedad clínica** (hipotensión, desaturación, taquicardia), no solo por la cifra.', 13, name='Rigor C2')
    for g in ids:
        s.step(fade(g))
    s.step(fade(con))
    s.step(fade(r_))


def hemoliticas(D):
    s = nueva(D, 3, 'Hemólisis corpuscular: el defecto está en el eritrocito', src=['AN 10.1 Hemólisis corpuscular', 'REV AN 10.1'], tipo='der', c1=ROJO, c2=ROSA)
    g1 = s.group_start('Membranopatías')
    eritrocito(s, 0.5, 1.4, 1.2, 'esfero', name='Esferocito h')
    s.shape(1.9, 1.55, 1.5, 0.9, 'ellipse', ('rad', [(0, 'F29A8E'), (60, 'E06A5F'), (100, '7B1F17')], (50, 50)), ('6E1A12', 1.0), False, name='Eliptocito')
    caja(s, 3.6, 1.2, 5.3, 1.55, '**Membranopatías**: esferocitosis hereditaria (CHCM ↑, fragilidad osmótica), eliptocitosis, estomatocitosis.', BLANCO, 14, anchor='m')
    s.group_end()
    g2 = s.group_start('Enzimopatías')
    enzima_globular(s, 0.7, 3.05, 1.3, 1.1, 'BB8FCE', 'G6PD', 'G6PD', size=13, seed=2)
    enzima_globular(s, 2.1, 3.05, 1.3, 1.1, 'F5B041', 'PK', 'PK', size=13, seed=3)
    caja(s, 3.6, 2.95, 5.3, 1.6, '**Enzimopatías**: déficit de **G6PD** (no neutraliza el estrés oxidativo: hemólisis episódica por fármacos, infecciones, habas) y de **piruvato quinasa** (falla energética).',
         BLANCO, 13.5, anchor='m')
    s.group_end()
    g3 = s.group_start('Hemoglobinopatías')
    falciforme(s, 0.6, 5.05, 1.4, name='Drepanocito h')
    falciforme(s, 1.9, 5.3, 1.2, name='Drepanocito h2')
    caja(s, 3.6, 4.75, 5.3, 2.3, '**Hemoglobinopatías**: anemia de células falciformes (la Hb S precipita al desoxigenarse → eritrocitos en hoz → obstrucción vascular + hemólisis), Hb inestables, persistencia de Hb fetal, **talasemias**.',
         BLANCO, 13.5, anchor='m')
    s.group_end()
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'El material incluye las **porfirias** entre las enzimopatías hemolíticas: son trastornos de la síntesis del hemo y, salvo formas raras (porfiria eritropoyética congénita), '
               '**no se presentan habitualmente como anemia hemolítica**.', 13.5, name='Rigor porfirias')
    s.step(fade(g1))
    s.step(fade(g2))
    s.step(fade(g3))
    s.step(fade(r_))


def extracorpusculares(D):
    s = nueva(D, 3, 'Hemólisis extracorpuscular: el agresor está afuera', src=['AN 10.2 Hemólisis extracorpuscular', 'REV AN 10.2 HPN'], tipo='izq', c1=ROSA, c2=BLANCO)
    items = [('Autoinmune', 'Autoanticuerpos contra la membrana → **Coombs positiva**.', LAVANDA), ('Isoinmune', 'Transfusiones incompatibles; enfermedad hemolítica del recién nacido.', CELESTE),
             ('Medicamentos', 'Hemólisis inducida por fármacos.', CREMA), ('Hiperesplenismo', 'El bazo destruye eritrocitos en exceso (caso 2).', ROSA),
             ('Microangiopáticas', 'Destrucción mecánica en vasos dañados (válvulas, SHU, PTT).', 'FDEBD0'), ('Infecciosas y tóxicas', 'Paludismo, sepsis, venenos de serpiente, toxinas bacterianas.', 'EAF5EA')]
    ids = []
    for k, (t, d, f) in enumerate(items):
        x = 0.4 + (k % 2) * 4.3; y = 1.2 + (k // 2) * 1.5
        ids.append(caja(s, x, y, 4.15, 1.35, '**%s**: %s' % (t, d), f, 14.5, anchor='m', name='Extra %s' % t))
    hpn = caja(s, 0.4, 5.75, 8.45, 1.3, '**HPN (hemoglobinuria paroxística nocturna)**: hemólisis predominantemente nocturna → orina roja al levantarse.', AMA, 15, anchor='m', name='HPN')
    r_ = rigor(s, 9.1, 1.2, 3.95, 5.85, 'El material explica la HPN por la acidosis leve nocturna. La explicación actual es la **deficiencia de proteínas ancladas por GPI** (CD55, CD59) por mutación de **PIG-A**: '
               'los eritrocitos quedan **sin protección frente al complemento**. La acidificación es una idea histórica (base de la prueba de Ham).', 13, name='Rigor HPN')
    for g in ids:
        s.step(fade(g))
    s.step(fade(hpn))
    s.step(fade(r_))


def tres_ejes(D):
    s = nueva(D, 3, 'Cómo describir cualquier anemia: cuatro ejes', src=['AN 12 Cuadro resumen'], tipo='bandas', c1=ROSA, c2=CREMA)
    ejes_ = [('Morfológico', 'VCM', 'Microcítica / normocítica / macrocítica', CELESTE), ('Cromático', 'HCM', 'Hipocrómica / normocrómica / (hipercrómica, rara)', ROSA),
             ('Etiopatogénico', 'Reticulocitos', 'Regenerativa / arregenerativa', 'EAF5EA'), ('Homogeneidad', 'RDW', 'Homogénea / heterogénea (anisocitosis)', LAVANDA)]
    ids = []
    for k, (t, p, c, f) in enumerate(ejes_):
        y = 1.2 + k * 1.22
        g = s.group_start('Eje ' + t)
        rotulo(s, 3.55, y + 0.2, t, NAVY, 16, w=2.4, h=0.7)
        rotulo(s, 6.1, y + 0.2, p, AMA, 16, w=1.6, h=0.7)
        caja(s, 7.85, y, 2.2, 1.1, c, f, 13, anchor='m')
        ids.append(s.group_end())
    ej = caja(s, 3.55, 6.15, 6.5, 0.9, 'Ejemplo (caso 2): **normocítica normocrómica heterogénea regenerativa hemolítica**.', AMA, 14.5, anchor='m', name='Ejemplo ejes')
    gl = s.group_start('Eritrocitos ejes')
    eritrocito(s, 0.5, 1.4, 1.2, 'hipo', name='e1'); eritrocito(s, 1.8, 2.4, 1.3, name='e2'); reticulocito(s, 0.6, 3.9, 1.2, name='e3'); eritrocito(s, 1.9, 4.9, 1.05, 'esfero', name='e4')
    s.group_end()
    deco = molecula3d(s, 10.6, 1.5, 2.3, 'hemo', name='Hemo ejes')
    s.step(fade(gl))
    for g in ids:
        s.step(fade(g))
    s.step(fade(ej), fade(deco, after=True))


def claves(D):
    s = nueva(D, 3, 'Diez ideas clave de la unidad', src=['AN 12 Resumen'], tipo='der', c1=ROJO, c2=BLANCO)
    ideas = ['La anemia se define por **hemoglobina**, no por hematocrito ni recuento.', 'Los valores varían por **sexo, edad** y condición fisiológica.',
             '**VCM, HCM, CHCM y RDW** clasifican morfológicamente.', 'Los **reticulocitos** separan regenerativa de arregenerativa.',
             'CHCM elevada: hallazgo clásico de **esferocitosis** (no exclusivo).', 'Coombs positiva → **hemolítica autoinmune**.',
             'Pancitopenia + macrocitosis → **megaloblástica o perniciosa**.', 'Ictericia + reticulocitos altos + LDH alta → **hemólisis**.',
             'Esplenomegalia + hemólisis → **hiperesplenismo**.', 'Transfusión: umbral de **7 g/dL** en pacientes estables, siempre individualizado.']
    ids = []
    for k, t in enumerate(ideas):
        x = 0.35 + (k % 2) * 4.4; y = 1.2 + (k // 2) * 1.18
        g = s.group_start('Idea %d' % (k + 1))
        num(s, x, y + 0.3, k + 1, d=0.5)
        caja(s, x + 0.6, y, 3.7, 1.05, t, BLANCO if k % 2 else CREMA, 13.5, anchor='m')
        ids.append(s.group_end())
    gr = s.group_start('Deco claves')
    eritrocito(s, 9.6, 1.4, 1.5, name='GR clave'); hemoglobina(s, 11.2, 1.6, 1.6, name='Hb clave'); megaloblasto(s, 9.7, 3.4, 1.5, name='Mega clave')
    reticulocito(s, 11.3, 3.6, 1.4, name='Reti clave')
    s.group_end()
    c = caja(s, 9.35, 5.3, 3.7, 1.75, 'Cada idea se apoya en un **mecanismo**: tamaño, contenido, producción o destrucción.', AMA, 14.5, name='Mecanismo claves')
    s.step(fade(gr))
    for k in range(0, 10, 2):
        s.step(fade(ids[k]), fade(ids[k + 1], after=True))
    s.step(fade(c))


def integracion_c(D):
    s = nueva(D, 3, 'Integración C: anemia y transporte de oxígeno', src=['AN 1 Definición', 'AN 4 Índices hematimétricos', 'AN 6 Clasificación etiopatogénica', 'VB 2.2 A Glóbulos rojos'],
              tipo='bandas', c1=ROSA, c2=SALM)
    pasos = [('Hemoglobina', '4 globinas + 4 hemo con Fe: transporta O_{2}.', 'hb'), ('Eritrocitos', 'Disco bicóncavo, membrana flexible; 4,5–6 millones/mm^{3}.', 'gr'),
             ('Cambios de concentración', 'Hb depende de la masa eritrocitaria y del volumen plasmático.', 'vp'),
             ('Interpretación hematológica', 'VCM, HCM, CHCM, RDW, reticulocitos, LDH, bilirrubina, Coombs.', 'int')]
    ids = []
    for k, (t, d, kind) in enumerate(pasos):
        x = 0.45 + k * 3.2
        g = s.group_start('Integración C %d' % (k + 1))
        if kind == 'hb':
            hemoglobina(s, x + 0.6, 1.3, 1.8, name='Hb C')
        elif kind == 'gr':
            eritrocito(s, x + 0.6, 1.3, 1.8, name='GR C')
        elif kind == 'vp':
            tubo(s, x + 1.15, 1.25, 0.6, 1.95, [(0.45, 'B3261E', 'rc'), (0.37, 'F7DC6F', 'pc')], tapa='8E44AD', name='Tubo C')
        else:
            medula_osea(s, x + 0.15, 1.35, 2.7, 1.75, name='Médula C', celulas=9)
        caja(s, x, 3.35, 3.0, 2.2, '**%s**\n%s' % (t, d), BLANCO, 14.5)
        if k < 3:
            s.arrow([(x + 3.02, 4.45), (x + 3.18, 4.45)], INK, 3)
        ids.append(s.group_end())
    c = caja(s, 0.45, 5.8, 12.45, 1.25, 'La anemia es un problema de **transporte de O_{2}**: el laboratorio mide su causa en tamaño, contenido, producción y destrucción de eritrocitos.', NAVY, 16,
             anchor='m', name='Síntesis integración C')
    for g in ids:
        s.step(fade(g))
    s.step(zoom(c))


def build(D):
    megaloblastica(D)
    asincronismo(D)
    pancitopenia(D)
    absorcion_b12(D)
    dx_perniciosa(D)
    folico(D)
    ldh(D)
    bilirrubina(D)
    neonatal(D)
    coombs(D)
    vsg(D)
    caso1(D)
    caso2(D)
    hemoliticas(D)
    extracorpusculares(D)
    tres_ejes(D)
    claves(D)
    integracion_c(D)
