# -*- coding: utf-8 -*-
"""UNIDAD IV (parte 1): caso clínico inicial, dolor, criterios diagnósticos, fisiopatología (Morph) y ECG."""
from plantillas import *


def divisor_u4(D):
    def arte(s):
        g = s.group_start('Arte unidad IV')
        corazon_anat(s, 7.0, 0.5, 2.9, name='Corazón div')
        cardiomiocito(s, 10.0, 0.9, 3.0, 1.5, name='Cardiomiocito div')
        ecg(s, 9.9, 2.75, 3.2, 1.3, 'st', name='ECG div')
        sarcomero_troponina(s, 7.2, 4.3, 5.6, 1.6, name='Filamento div')
        s.group_end()
        return g
    divisor(D, 4, 'IV', 'Infarto agudo de miocardio y biomarcadores cardíacos', 'Del cardiomiocito lesionado a la curva de troponina',
            ['Caso clínico inicial', 'Dolor y criterios diagnósticos', 'Fisiopatología del daño miocárdico', 'Electrocardiograma', 'CK, CK-MB, troponinas, mioglobina, LDH',
             'Liberación de biomarcadores', 'Cinética y ventana diagnóstica', 'Reinfarto y seguimiento a 8 días', 'Factores de riesgo'], arte, src=['IAM 1 Caso clínico'])


def caso_inicial(D):
    s = nueva(D, 4, 'Caso clínico: un dolor que no cede', src=['IAM 1 Caso clínico'], tipo='der', c1=AZUL, c2=LAVANDA)
    p = caso_cabecera(s, 0.4, 1.2, 5.4, 'Varón de 36 años', 'Dolor intenso y opresivo en el tórax, «en la zona de la corbata».', color=AZUL)
    hu = human(s, 6.2, 1.1, 5.9, name='!!Paciente')
    dolor = s.shape(7.45, 2.25, 0.55, 0.9, 'ellipse', ('a', 'E74C3C', 55), (ROJO, 2.0), False, name='Zona del dolor')
    irr = s.arrow([(7.9, 2.6), (8.55, 2.9), (8.8, 4.0)], ROJO, 4, curve=True, name='Irradiación brazo izquierdo')
    clk = clock(s, 0.6, 3.05, 1.3, hours=7, name='Reloj 7 horas')
    t7 = caja(s, 2.1, 3.05, 3.7, 1.3, 'Evolución de **7 horas**.', CREMA, 18, anchor='m', name='Tiempo de evolución')
    ir = caja(s, 0.4, 4.6, 5.4, 1.2, 'Irradiación al **brazo izquierdo** (hasta el dedo meñique).', ROSA, 16, anchor='m', name='Irradiación texto')
    q = caja(s, 0.4, 6.0, 5.4, 1.05, '¿Qué más necesitamos saber antes de pedir el laboratorio?', AMA, 15.5, anchor='m', name='Pregunta IAM')
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Los datos se presentan **de a uno**: primero el paciente, luego antecedentes, ECG y biomarcadores.', BLANCO, 15, head='Razonamiento', name='Método caso')
    s.step(fade(p), fade(hu, after=True))
    s.step(zoom(dolor), pulse(dolor, after=True))
    s.step(wipe(irr, 't'), fade(ir, after=True))
    s.step(fade(clk), fade(t7, after=True))
    s.step(fade(c))
    s.step(fade(q))


def caso_riesgo(D):
    s = nueva(D, 4, 'Caso clínico: factores de riesgo cardiovascular', src=['IAM 1 Caso clínico', 'IAM 8 Factores de riesgo'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    fr = [('Tabaquismo severo', 'cig'), ('Obesidad', 'obe'), ('Hipertensión arterial', 'hta'), ('Padre fallecido por IAM', 'fam')]
    ids = []
    for k, (t, kind) in enumerate(fr):
        x = 0.45 + (k % 2) * 4.3; y = 1.25 + (k // 2) * 2.7
        g = s.group_start('Riesgo ' + t)
        caja(s, x, y, 4.1, 2.45, '', BLANCO, 12, lw=2.0)
        if kind == 'cig':
            s.shape(x + 0.4, y + 0.8, 2.4, 0.35, 'rect', 'FDFEFE', (INK, 1.25), False)
            s.shape(x + 2.8, y + 0.8, 0.5, 0.35, 'rect', 'E67E22', (INK, 1.25), False)
            strokes(s, x + 2.9, y + 0.1, 0.6, 0.7, ['M 200 1000 C 0 700 600 500 300 200 C 200 50 500 0 600 0'], '95A5A6', 2.5)
        elif kind == 'obe':
            s.shape(x + 1.3, y + 0.25, 1.4, 1.4, 'ellipse', shade('F5CBA7', 0.35, 0.2), ('A0522D', 1.5), False)
        elif kind == 'hta':
            s.shape(x + 1.2, y + 0.3, 1.5, 1.3, 'ellipse', BLANCO, (INK, 2.0), False)
            s.arrow([(x + 1.95, y + 0.95), (x + 2.45, y + 0.55)], ROJO, 3)
        else:
            persona_ = s.group_start('Familia')
            for j in range(2):
                s.shape(x + 1.1 + j * 1.0, y + 0.25, 0.5, 0.5, 'ellipse', 'AEB6BF', (INK, 1.0), False)
                s.shape(x + 0.95 + j * 1.0, y + 0.8, 0.8, 0.85, 'flowChartDelay', 'AEB6BF', (INK, 1.0), False, rot=-90)
            s.group_end()
        texto(s, x + 0.15, y + 1.75, 3.8, 0.6, t, 18, AZUL, True, 'c', 'm')
        ids.append(s.group_end())
    c = caja(s, 9.1, 1.25, 3.95, 3.2, 'Reúne **todos los elementos clásicos** del IAM: la presentación es **altamente sugestiva** antes de ver el laboratorio.', AMA, 15.5, name='Sugestivo')
    c2 = caja(s, 9.1, 4.7, 3.95, 2.35, 'Los factores de riesgo **se potencian entre sí**.', BLANCO, 16, anchor='m', name='Potencian')
    for g in ids:
        s.step(fade(g))
    s.step(fade(c))
    s.step(fade(c2))


def caso_ecg_lab(D):
    s = nueva(D, 4, 'Caso clínico: ECG y laboratorio de ingreso', src=['IAM 1 Caso clínico', 'IAM 7.2 Laboratorio día 0'], tipo='der', c1=AZUL, c2=BLANCO)
    e = ecg(s, 0.4, 1.3, 8.4, 2.2, 'st', beats=3, name='!!ECG caso')
    lbl = rotulo(s, 0.6, 3.65, 'cara inferior: elevación del segmento ST', ROJO, 15, name='Rótulo ECG caso')
    rows = [['Biomarcador al ingreso', 'Resultado'], ['CPK total', '1173 UI/L (muy alta)'], ['CPK-MB', 'Elevada'], ['Troponina I', 'Muy elevada'], ['Mioglobina', 'Elevada'], ['LDH', 'Elevada']]
    ids, H = tabla_filas(s, 0.4, 4.35, [4.0, 4.4], rows, rowh=0.44, size=14.5, name='Laboratorio ingreso')
    c = caja(s, 9.35, 1.2, 3.7, 2.9, 'ECG con cambios patológicos en la **cara inferior** del corazón.', BLANCO, 16, head='ECG', name='ECG caso texto')
    c2 = caja(s, 9.35, 4.35, 3.7, 2.7, 'Laboratorio de ingreso con **todos los biomarcadores elevados**: ¿qué dice cada uno y en qué momento?', AMA, 15, name='Pregunta biomarcadores')
    s.step(fade(e['papel']), wipe(e['traza'], 'l', after=True, dur=1200))
    s.step(fade(lbl), fade(c, after=True))
    s.step(fade(ids[0]))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(c2))


def dolor_irradiado(D):
    s = nueva(D, 4, 'Dolor torácico irradiado: cómo interpretarlo', src=['IAM 1 Análisis del caso', 'REV IAM 1 Dolor'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    hu = human(s, 0.9, 1.1, 5.9, name='!!Paciente')
    cor = corazon_anat(s, 2.3, 2.35, 0.75, name='Corazón dolor', coronarias=False)
    med = s.shape(2.3, 1.95, 0.15, 3.0, 'rect', ('a', 'F4D03F', 70), ('B7950B', 1.0), False, name='Médula espinal T1-T5')
    zona = s.free(3.15, 2.2, 1.0, 2.2, smooth([(200, 0), (0, 300), (300, 1000), (700, 950), (800, 300)]), ('a', 'E74C3C', 45), (ROJO, 1.5), name='Dermatomas brazo')
    a1 = s.arrow([(2.75, 2.9), (2.45, 2.6)], ROJO, 3, name='Aferencia visceral')
    a2 = s.arrow([(2.45, 2.4), (3.3, 2.75)], ROJO, 3, name='Proyección somática')
    c1 = caja(s, 4.0, 1.2, 9.05, 1.6, 'Dolor intenso y **opresivo** en la zona de la corbata, con **irradiación al brazo izquierdo**, cuello, mandíbula o espalda; puede acompañarse de **disnea** y **náuseas** (reflejo vagal).',
              BLANCO, 15.5, name='Clínica dolor')
    c2 = caja(s, 4.0, 3.0, 9.05, 1.45, 'El material lo atribuye a que la inflamación del daño cardíaco «comprime los nervios» de la zona torácica.', CREMA, 15, name='Explicación material')
    r_ = rigor(s, 4.0, 4.65, 9.05, 2.4, 'Explicación aceptada: **dolor referido**. Las fibras aferentes viscerales del corazón ingresan a la médula en los mismos segmentos (≈ **T1–T5**) que las fibras somáticas del tórax y '
               'de la cara interna del brazo; el cerebro **atribuye** el dolor a esos territorios. No se debe a compresión nerviosa por inflamación.', 14, name='Rigor dolor')
    s.step(fade(hu), fade(cor['g'], after=True))
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(med), wipe(a1, 'r', after=True), wipe(a2, 'r', after=True), fade(zona, after=True), fade(r_, after=True))


def criterios(D):
    s = nueva(D, 4, 'Criterios diagnósticos del IAM', src=['IAM 2 Criterios diagnósticos', 'REV IAM 2'], tipo='der', c1=AZUL, c2=LAVANDA)
    tri = s.group_start('!!Trípode')
    s.shape(2.5, 1.5, 4.0, 3.5, 'triangle', ('a', 'D6EAF8', 70), (NAVY, 2.5), False)
    s.group_end()
    v1 = caja(s, 3.15, 1.15, 2.7, 1.25, '**Síntomas clínicos**', ROSA, 17, align='c', anchor='m', name='Vértice síntomas')
    v2 = caja(s, 0.5, 4.55, 3.0, 1.25, '**Cambios en el ECG**', CELESTE, 17, align='c', anchor='m', name='Vértice ECG')
    v3 = caja(s, 5.45, 4.55, 3.2, 1.25, '**Biomarcadores cardíacos**', AMA, 17, align='c', anchor='m', name='Vértice biomarcadores')
    t = caja(s, 0.5, 6.05, 8.15, 1.0, 'En el material: el diagnóstico se basa en la **conjunción de los tres criterios**; no alcanza con uno solo.', BLANCO, 15, anchor='m', name='Trípode texto')
    r_ = rigor(s, 9.35, 1.2, 3.7, 5.85, 'Definición universal vigente (4.ª, 2018): IAM = **ascenso y/o descenso de troponina** con al menos un valor **> percentil 99** **más** al menos uno de: síntomas de isquemia, '
               'cambios isquémicos nuevos en el ECG, ondas Q patológicas, imagen compatible o trombo coronario. La troponina dinámica es **obligatoria**; no se exigen los tres criterios a la vez.',
               13.5, name='Rigor criterios')
    s.step(fade(tri))
    s.step(fade(v1))
    s.step(fade(v2))
    s.step(fade(v3))
    s.step(fade(t))
    s.step(fade(r_))


# ---------------------------------------------------------------- fisiopatología (Morph)
FP_TXT = {1: 'Corazón y arterias coronarias: el aporte de oxígeno', 2: 'Placa de ateroma: estrechamiento coronario', 3: 'Oclusión coronaria: isquemia del territorio',
          4: 'Necrosis del miocardio: el infarto'}


def escena_fp(D, st):
    s = nueva(D, 4, FP_TXT[st], tipo='der', c1=AZUL, c2=BLANCO, morph=st > 1, src=['IAM 10 Glosario IAM', 'IAM 10 Glosario Ateroesclerosis', 'IAM 3.2 Evolución temporal'], tw=8.7)
    ids = corazon_anat(s, 0.35, 1.0, 3.9, name='!!Corazon')
    if st >= 3:
        col = ('a', '7F8C8D', 55) if st == 3 else ('a', '4A235A', 75)
        ids['zona'] = s.shape(1.25, 4.0, 1.9, 1.15, 'ellipse', col, ('4A235A', 1.5, 'dash'), False, name='!!Zona isquémica', rot=-20)
    # corte longitudinal de la arteria coronaria (ampliación)
    ids['art'] = s.shape(4.6, 2.0, 4.2, 1.4, 'roundRect', vshade('E57373', 0.3, 0.3), ('7B241C', 2.0), SH_I, name='!!ArteriaCoronaria corte', adj={'adj': 50000})
    ids['lumen'] = s.shape(4.75, 2.25, 3.9, 0.9, 'roundRect', ('lin', [(0, 'F5B7B1'), (50, 'FDEDEC'), (100, 'F5B7B1')], 90), ('C0392B', 0.75), False, name='!!Luz coronaria',
                           adj={'adj': 50000})
    lupa = s.shape(2.1, 2.7, 0.7, 0.7, 'ellipse', None, (AMA2, 3.0), False, name='!!Lupa coronaria')
    ids['lupa'] = lupa
    ids['lineaL'] = s.arrow([(2.8, 3.0), (4.6, 2.7)], AMA2, 2, tail=None, dash='dash', name='!!Línea ampliación')
    if st >= 2:
        h = {2: 0.45, 3: 0.82, 4: 0.82}[st]
        ids['placa'] = s.shape(6.1, 2.25 + 0.9 - h, 1.3, h, 'flowChartDelay' if False else 'roundRect', ('lin', [(0, 'F9E79F'), (100, 'F4D03F')], 90), ('9A7D0A', 1.25), False,
                               name='!!Placa', adj={'adj': 40000})
    if st >= 3:
        ids['trombo'] = s.shape(5.85, 2.27, 0.55, 0.5, 'ellipse', shade('922B21', 0.3, 0.3), ('4A0D0D', 1.0), False, name='!!Trombo')
    # flujo / eritrocitos
    n_ok = {1: 4, 2: 3, 3: 0, 4: 0}[st]
    for k in range(4):
        xx = 4.95 + k * 0.9 if k < 2 else 7.6 + (k - 2) * 0.55
        vis = k < n_ok
        ids['f%d' % k] = s.shape(xx, 2.5, 0.42, 0.42, 'ellipse', shade('C0392B', 0.35, 0.3) if vis else ('a', 'C0392B', 15), ('6E1A12', 0.75 if vis else 0.25), False,
                                 name='!!Flujo %d' % k)
    ids['o2'] = ficha(s, 7.5 if st < 3 else 4.9, 3.75, 'O_{2}', '5DADE2', w=0.8, h=0.42, size=13, name='!!O2 miocardio')
    ids['cel'] = cardiomiocito(s, 4.6, 4.5, 4.2, 1.9, name='!!Cardiomiocito')['g']
    if st == 4:
        ids['nec'] = s.shape(4.6, 4.5, 4.2, 1.9, 'roundRect', ('a', '4A235A', 45), None, False, name='!!Necrosis', adj={'adj': 20000})
    return s, ids


def fisiopatologia(D):
    ini = len(D.slides) + 1
    s, i = escena_fp(D, 1)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Las **arterias coronarias** llevan sangre oxigenada al **miocardio**; el cardiomiocito depende de ese aporte continuo de O_{2}.', BLANCO, 15, head='Aporte',
             name='Caja FP1')
    s.step(fade(i['g']), wipe(i['ci'], 't', after=True), wipe(i['cd'], 't', after=True))
    s.step(zoom(i['lupa']), wipe(i['lineaL'], 'l', after=True), fade(i['art'], after=True), fade(i['lumen']), *[fade(i['f%d' % k]) for k in range(4)])
    s.step(fade(i['o2']), fade(i['cel'], after=True), fade(c, after=True))
    s, i = escena_fp(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.7, '**Ateroesclerosis**: depósito de placas de colesterol (**LDL oxidadas**) en la pared → **estrechamiento progresivo** → isquemia.', CREMA, 15, head='Placa',
             headfill=AMA2, name='Caja FP2')
    s.step(pulse(i['placa']), fade(c, after=True))
    s, i = escena_fp(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.7, '**Oclusión de una arteria coronaria** que impide el aporte de O_{2}: el territorio irrigado (en el caso, la **cara inferior**) queda isquémico.', ROSA, 15,
             head='Oclusión', headfill=ROJO, name='Caja FP3')
    s.step(pulse(i['trombo']), fade(c, after=True))
    s, i = escena_fp(D, 4)
    c = caja(s, 9.35, 1.2, 3.7, 3.0, '**IAM**: muerte (**necrosis**) de un área del músculo cardíaco por falta de O_{2}.', ROSA, 16, head='Infarto', headfill=ROJO, name='Caja FP4')
    c2 = caja(s, 9.35, 4.45, 3.7, 2.6, 'Las células necrosadas **liberan su contenido** a la sangre: allí nacen los **biomarcadores**.', AMA, 15.5, name='Puente biomarcadores')
    s.step(fade(c))
    s.step(fade(c2))
    registrar_morph(D, ini, len(D.slides), 'Fisiopatología del IAM: coronaria normal → placa de ateroma → oclusión e isquemia → necrosis',
                    ['!!Corazon', '!!ArteriaCoronaria izquierda', '!!ArteriaCoronaria derecha', '!!ArteriaCoronaria corte', '!!Luz coronaria', '!!Placa', '!!Trombo', '!!Zona isquémica',
                     '!!Flujo 0–3', '!!O2 miocardio', '!!Cardiomiocito', '!!Necrosis'],
                    'La placa crece dentro de la misma arteria ampliada hasta ocluirla; los eritrocitos del flujo se desvanecen; la zona isquémica del corazón pasa de gris a violeta; '
                    'el cardiomiocito queda cubierto por la necrosis.')


def zonas(D):
    s = nueva(D, 4, 'Necrosis, lesión e isquemia: tres zonas', src=['IAM 3.2 Evolución temporal'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    z = s.group_start('!!Zonas concéntricas')
    s.shape(0.5, 1.4, 4.0, 4.0, 'ellipse', ('a', '85C1E9', 70), (NAVY, 2.0), False)
    s.shape(1.1, 2.0, 2.8, 2.8, 'ellipse', ('a', 'F5B041', 80), ('9C640C', 2.0), False)
    s.shape(1.75, 2.65, 1.5, 1.5, 'ellipse', ('a', '4A235A', 85), ('1B0E24', 2.0), False)
    s.group_end()
    l = []
    for k, (t, d, f, y) in enumerate((('Necrosis', '**Onda Q** patológica: necrosis transmural; persiste como **cicatriz eléctrica**.', 'E8DAEF', 1.25),
                                      ('Lesión', '**Elevación del ST** («corriente de lesión»): células dañadas pero aún no muertas.', 'FDEBD0', 3.15),
                                      ('Isquemia', '**Inversión de la onda T**: isquemia perilesional.', CELESTE, 5.05))):
        g = s.group_start('Zona ' + t)
        caja(s, 5.0, y, 8.05, 1.75, '**%s**: %s' % (t, d), f, 17, anchor='m')
        l.append(s.group_end())
    s.step(fade(z))
    for g in l:
        s.step(fade(g))


def ecg_normal(D):
    s = nueva(D, 4, 'Electrocardiograma normal: ondas, segmentos e intervalos', src=['IAM 3.1 ECG normal'], tipo='der', c1=AZUL, c2=BLANCO)
    e = ecg(s, 0.4, 1.4, 8.4, 3.2, 'normal', beats=1, name='!!ECG')
    # posiciones aproximadas en el latido (fracciones del ancho)
    X0, W = 0.4, 8.4
    def X(f):
        return X0 + W * f
    yb = 1.4 + 3.2 * 350 / 600
    marks = [('P', X(0.13), yb - 0.75, 'F5B041'), ('QRS', X(0.31), yb - 2.0, ROJO), ('ST', X(0.4), yb - 0.55, VERDE_OSC), ('T', X(0.52), yb - 1.15, '2E86C1')]
    ids = []
    for t, x, y, c in marks:
        ids.append(rotulo(s, x - 0.35, y, t, c, 16, w=0.8 if t != 'QRS' else 1.0, name='Marca ' + t))
    qt = s.arrow([(X(0.26), 4.75), (X(0.62), 4.75)], NAVY, 2.5, head='triangle', name='Intervalo QT')
    qtl = rotulo(s, X(0.4) - 0.4, 4.85, 'QT', NAVY, 15, w=0.8, name='Rótulo QT')
    rows = [['Onda / segmento', 'Significado'], ['Onda P', 'Despolarización auricular'], ['Complejo QRS', 'Despolarización ventricular'],
            ['Segmento ST', 'Fin de la despolarización → inicio de la repolarización; normalmente **isoeléctrico**'], ['Onda T', 'Repolarización ventricular'],
            ['Intervalo QT', 'Duración total de la actividad eléctrica ventricular']]
    tb, H = tabla_filas(s, 9.25, 1.2, [1.65, 2.2], rows, rowh=0.5, size=12.5, name='Tabla ECG')
    r_ = rigor(s, 9.25, 1.4 + H, 3.85, 6.95 - (1.4 + H), 'El ECG registra **actividad eléctrica**: la P y el QRS preceden a la contracción auricular y ventricular, no son la contracción.', 12.5,
               name='Rigor ECG')
    s.step(fade(e['papel']), wipe(e['traza'], 'l', after=True, dur=1000))
    s.step(zoom(ids[0]), fade(tb[0], after=True), fade(tb[1], after=True))
    for k in range(1, 4):
        s.step(zoom(ids[k]), fade(tb[k + 1], after=True))
    s.step(wipe(qt, 'l'), fade(qtl, after=True), fade(tb[5], after=True))
    s.step(fade(r_))


def ecg_evolucion(D):
    s = nueva(D, 4, 'Evolución temporal del ECG en el IAM', src=['IAM 3.2 Evolución temporal', 'REV IAM 3.2'], tipo='izq', c1=LAVANDA, c2=BLANCO)
    et = [('Minutos – horas', 'st', 'Elevación del ST (corriente de lesión)'), ('Horas después', 'q', 'Disminuye R, aparece Q profunda, T invertida'),
          ('Días – semanas', 'ntinv', 'El ST se normaliza; la T puede normalizarse'), ('Semanas – permanente', 'cicatriz', 'La Q patológica persiste: cicatriz eléctrica')]
    ids = []
    for k, (t, kind, d) in enumerate(et):
        x = 0.4 + (k % 2) * 4.4; y = 1.2 + (k // 2) * 2.95
        g = s.group_start('Etapa ECG %d' % (k + 1))
        rotulo(s, x, y, t, NAVY, 14, w=4.2)
        e = ecg(s, x, y + 0.5, 4.2, 1.85, kind if kind != 'ntinv' else 'normal', beats=2, name='ECG etapa %d' % (k + 1))
        texto(s, x, y + 2.4, 4.2, 0.5, d, 14, INK, True, 'c')
        ids.append(s.group_end())
    r_ = rigor(s, 9.25, 1.2, 3.85, 5.85, 'Es una secuencia **típica**, no obligatoria: muchos IAM **no** muestran elevación del ST (NSTEMI) ni desarrollan onda Q; la reperfusión precoz modifica la evolución. '
               'El ECG se interpreta junto con la clínica y la troponina.', 13.5, name='Rigor evolución ECG')
    for g in ids:
        s.step(fade(g))
    s.step(fade(r_))


def stemi(D):
    s = nueva(D, 4, 'STEMI y NSTEMI', src=['IAM 3.2 STEMI vs NSTEMI', 'IAM 10 Glosario STEMI', 'REV IAM 3.2 STEMI'], tipo='bandas', c1=ROSA, c2=CELESTE)
    a = s.group_start('STEMI')
    s.shape(0.5, 1.5, 2.4, 0.9, 'roundRect', vshade('E57373', 0.3, 0.3), ('7B241C', 1.5), False, adj={'adj': 50000})
    s.shape(1.4, 1.55, 0.6, 0.8, 'ellipse', shade('922B21', 0.3, 0.3), None, False)
    ecg(s, 0.35, 2.7, 2.8, 2.3, 'st', beats=1, name='ECG STEMI')
    rotulo(s, 0.6, 5.2, 'ST elevado', ROJO, 15, w=2.3)
    s.group_end()
    b = s.group_start('NSTEMI')
    s.shape(10.45, 1.5, 2.4, 0.9, 'roundRect', vshade('E57373', 0.3, 0.3), ('7B241C', 1.5), False, adj={'adj': 50000})
    s.shape(11.35, 1.55, 0.6, 0.45, 'ellipse', shade('922B21', 0.3, 0.3), None, False)
    ecg(s, 10.35, 2.7, 2.8, 2.3, 'normal', beats=1, name='ECG NSTEMI')
    rotulo(s, 10.6, 5.2, 'sin elevación del ST', AZUL, 14, w=2.3)
    s.group_end()
    ca = caja(s, 3.55, 1.2, 3.2, 3.5, '**STEMI** (con elevación del ST): oclusión **total** de la coronaria. Emergencia máxima: **angioplastia primaria o trombólisis** urgente.', ROSA, 14.5,
              head='STEMI', headfill=ROJO, name='Caja STEMI')
    cb = caja(s, 6.95, 1.2, 3.2, 3.5, '**NSTEMI** (sin elevación del ST): oclusión **parcial** o suboclusión. Los **biomarcadores sí se elevan** (confirman necrosis). También requiere tratamiento urgente.',
              CELESTE, 14.5, head='NSTEMI', headfill=AZUL, name='Caja NSTEMI')
    r_ = rigor(s, 3.55, 4.95, 6.6, 2.1, 'La correspondencia «oclusión total = STEMI / parcial = NSTEMI» es una **aproximación**: algunas oclusiones totales no elevan el ST (p. ej., territorio circunflejo) '
               'y algunas elevaciones del ST no son IAM. Lo que define el NSTEMI es la **troponina dinámica** sin elevación persistente del ST.', 13, name='Rigor STEMI')
    s.step(fade(a), fade(ca, after=True))
    s.step(fade(b), fade(cb, after=True))
    s.step(fade(r_))


def build(D):
    divisor_u4(D)
    caso_inicial(D)
    caso_riesgo(D)
    caso_ecg_lab(D)
    dolor_irradiado(D)
    criterios(D)
    fisiopatologia(D)
    zonas(D)
    ecg_normal(D)
    ecg_evolucion(D)
    stemi(D)
