# -*- coding: utf-8 -*-
"""UNIDAD I — Fundamentos y estado alimentado (temas 1–3)"""
from base import *

U = 1


def div(D):
    def art(s):
        pancreas(s, 8.4, 1.0, 4.4, name='Arte páncreas')
        islet(s, 9.3, 3.0, 2.4, name='Arte islote')
        hepatocyte(s, 8.2, 4.7, 2.4, name='Arte hepatocito')
        adipocyte_white(s, 11.3, 4.9, 1.6, name='Arte adipocito')
        mol(s, 11.9, 3.2, 'ins', d=0.55); mol(s, 12.3, 3.8, 'glc', d=0.55); mol(s, 11.6, 4.1, 'glc', d=0.5)
    divider(D, U, 'I', 'FUNDAMENTOS Y\nESTADO ALIMENTADO', 'Del bocado a la señal de abundancia',
            ['1 · Alimentación, nutrición y metabolismo', '2 · Ciclo alimentación–ayuno y transición hormonal',
             '3 · Destino de glucosa, lípidos y aminoácidos en saciedad', '4 · Secreción de insulina y glucagón',
             '5 · Recuperación de la glucemia basal tras la ingesta', '6 · Metabolismo posprandial tejido por tejido'], art,
            'Unidad I. Se construye el lenguaje común de la clase: diferencia entre alimentación, nutrición y metabolismo; '
            'concepto de flujo; fases del ciclo alimentación–ayuno; y la respuesta integrada a una comida, desde el sensor '
            'pancreático hasta cada tejido.')


# ------------------------------------------------------------------ TEMA 1
def t1a(D):
    s = new(D, U, '1 · Alimentación, nutrición y metabolismo')
    cols = [
        ('ALIMENTACIÓN', 'Comportamiento **biológico, social y neuroendocrino** por el que se seleccionan, ingieren y aportan alimentos.\nEs voluntaria y está modulada por hambre, saciedad, recompensa y cultura.', LSALMON),
        ('NUTRICIÓN', 'Conjunto de procesos que siguen a la ingesta: **digestión, absorción, transporte, incorporación, utilización y eliminación** de nutrientes.\nEs involuntaria.', YEL),
        ('METABOLISMO', 'Conjunto de **transformaciones químicas intracelulares** acopladas a transferencia de **materia, energía e información**.\nOcurre en compartimentos: citosol, mitocondria, RE, peroxisoma.', LBLUE),
    ]
    ids = []
    for i, (h, t, f) in enumerate(cols):
        x = 0.45 + i * 4.3
        g = s.group_start('Columna ' + h.lower())
        card(s, x, 3.0, 3.95, 2.9, t, f, 15, head=h)
        if i == 0:
            person(s, x + 1.35, 1.05, 1.75, name='Ícono persona')
            mol(s, x + 2.6, 1.7, 'glc', d=0.5); mol(s, x + 3.1, 2.1, 'aa', d=0.45); ag_chain(s, x + 2.5, 2.55, 0.9, 0.18)
        elif i == 1:
            intestine(s, x + 0.35, 1.0, 1.95, name='Ícono intestino')
            vessel(s, x + 2.3, 1.75, 1.5, 0.45, rbcs=2, name='Ícono vaso')
        else:
            hepatocyte(s, x + 0.25, 1.05, 2.25, name='Ícono hepatocito')
            mito(s, x + 2.65, 1.55, 1.1, name='Ícono mitocondria')
        ids.append(s.group_end())
    a1 = s.arrow([(4.42, 4.45), (4.73, 4.45)], TRN, 4)
    a2 = s.arrow([(8.72, 4.45), (9.03, 4.45)], TRN, 4)
    p = note_box(s, 0.45, 6.15, 12.4, 0.95, '«Comer no es solo introducir calorías: es cambiar el modo de operación de hígado, músculo, adipocito, intestino, riñón y cerebro».', 17)
    s.step(fade(ids[0]))
    s.step(wipe(a1, 'l'), fade(ids[1], after=True))
    s.step(wipe(a2, 'l'), fade(ids[2], after=True))
    s.step(zoom(p))
    s.note('Tres conceptos que no deben confundirse. La alimentación es una conducta (qué, cuánto y cuándo se come) regulada por '
           'circuitos hipotalámicos, de recompensa y sociales. La nutrición abarca los procesos fisiológicos posteriores: digestión, '
           'absorción, transporte, incorporación tisular, utilización y eliminación. El metabolismo es el conjunto de reacciones '
           'químicas intracelulares, acopladas a transferencia de materia (carbono, nitrógeno), energía (ATP, poder reductor) e '
           'información (señales hormonales y metabólicas).\nEjemplo oral: una persona puede alimentarse en exceso y aun así estar '
           'malnutrida si la absorción o la utilización de nutrientes están alteradas.')


def t1b(D):
    s = new(D, U, '1 · Qué entrega una comida')
    items = [('ENERGÍA QUÍMICA', 'Glucosa, lípidos y aminoácidos oxidables a CO_{2} con generación de ATP.', 'glc', YEL),
             ('MATERIAL ESTRUCTURAL', 'Aminoácidos esenciales, ácidos grasos esenciales, minerales y vitaminas.', 'aa', MINT),
             ('SEÑALES', 'Nutrientes, incretinas, cambios vagales y hormonas que reprograman los tejidos.', 'ins', LBLUE)]
    ids = []
    for i, (h, t, k, f) in enumerate(items):
        y = 1.15 + i * 1.5
        g = s.group_start('Aporte ' + h.lower())
        card(s, 0.45, y, 5.2, 1.3, t, f, 15, head=h)
        mol(s, 5.0, y + 0.55, k, d=0.5)
        ids.append(s.group_end())
    # gráfico conceptual: aporte discontinuo vs ATP continuo
    gg = s.group_start('Gráfico aporte vs ATP')
    s.shape(6.1, 1.15, 6.8, 4.15, 'rect', ('a', 'FFFFFF', 55), (INK, 1.25), SHD)
    s.text(6.25, 1.2, 6.5, 0.4, 'APORTE DISCONTINUO → PROVISIÓN CONTINUA DE ATP', 14, F_HEAD, INK, True, 'c', 'm')
    s.arrow([(6.5, 4.85), (12.6, 4.85)], INK, 1.5); s.arrow([(6.5, 4.85), (6.5, 1.7)], INK, 1.5)
    s.text(11.2, 4.88, 1.5, 0.3, 'tiempo', 12, F_BODY, INK, False, 'r')
    meals = 'M 0 900 L 80 900 C 120 900 130 150 180 150 C 230 150 260 900 330 900 L 380 900 C 420 900 430 250 480 250 C 530 250 560 900 630 900 L 700 900 C 740 900 750 100 800 100 C 860 100 900 900 960 900 L 1000 900'
    s.free(6.55, 1.75, 5.95, 3.05, [(meals, False, True)], None, ('E67E22', 3.0), name='Curva comidas')
    s.free(6.55, 1.75, 5.95, 3.05, [('M 0 520 C 300 500 600 540 1000 515', False, True)], None, (ACT, 4.0), name='Curva ATP')
    s.text(6.65, 1.65, 2.3, 0.3, 'Ingestas', 13, F_HEAD, 'C55A11', True, 'l')
    s.text(10.4, 2.75, 2.2, 0.3, 'Provisión de ATP', 13, F_HEAD, ACT, True, 'l')
    s.group_end()
    o1 = card(s, 6.1, 5.5, 3.3, 1.6, '**Abundancia**: oxidar una parte y **almacenar** otra (glucógeno, TAG, proteínas).', CREAM, 14, head='Objetivo 1', headfill=ACT)
    o2 = card(s, 9.6, 5.5, 3.3, 1.6, '**Carencia**: **movilizar** reservas y **defender** sustratos obligatorios (glucosa del SNC y eritrocitos).', CREAM, 14, head='Objetivo 2', headfill=INH)
    s.step(fade(ids[0]), fade(ids[1], after=True), fade(ids[2], after=True))
    s.step(fade(gg))
    s.step(fade(o1), fade(o2, after=True))
    s.note('Una comida entrega energía química, material estructural y señales. El organismo transforma un aporte discontinuo '
           '(comidas) en una provisión continua de ATP alternando dos objetivos: en la abundancia oxida una parte y almacena otra; '
           'en la carencia moviliza reservas y defiende sustratos obligatorios. El gráfico es conceptual (sin escala): '
           'las ingestas son picos, mientras que la disponibilidad de ATP se mantiene prácticamente constante gracias a la '
           'regulación interorgánica.')


def t1c(D):
    s = new(D, U, '1 · Destino del carbono y del nitrógeno: pensar en flujos')
    g1 = s.group_start('Destino del carbono')
    s.shape(0.45, 1.1, 5.9, 3.55, 'rect', CREAM, (INK, 1.25), SHD)
    s.text(0.6, 1.15, 5.6, 0.42, 'EL CARBONO ALIMENTARIO PUEDE TERMINAR COMO…', 14, F_HEAD, INK, True, 'c', 'm')
    chip(s, 2.55, 1.7, 'C alimentario', TAG, 15, h=0.45)
    dest = [('CO_{2}', 'co2'), ('Glucógeno', 'glc'), ('TAG', 'tag'), ('Colesterol', 'chol'), ('Proteínas', 'aa'), ('Intermediarios', 'acoa')]
    for i, (t, k) in enumerate(dest):
        x = 0.65 + (i % 3) * 1.9; y = 2.75 + (i // 3) * 0.95
        s.arrow([(3.4, 2.18), (x + 0.75, y - 0.05)], TRN, 1.75)
        chip(s, x, y, t, lighten(MOL[k][0], 0.55), 13, w=1.55, h=0.42, font=F_HEAD)
    s.group_end()
    g2 = s.group_start('Destino del nitrógeno')
    s.shape(0.45, 4.85, 5.9, 2.25, 'rect', LBLUE, (INK, 1.25), SHD)
    s.text(0.6, 4.9, 5.6, 0.4, 'EL NITRÓGENO AMINOACÍDICO…', 14, F_HEAD, INK, True, 'c', 'm')
    s.text(0.7, 5.35, 3.4, 1.6, '- se **redistribuye** entre tejidos (alanina, glutamina)\n- se **elimina** principalmente como **urea** y **NH_{4}^{+}**', 14, F_BODY)
    mol(s, 4.4, 5.55, 'urea', d=0.6); mol(s, 5.25, 5.55, 'nh4', d=0.6); mol(s, 4.85, 6.3, 'gln', d=0.55)
    s.group_end()
    # flujo vs concentración
    g3 = s.group_start('Flujo frente a concentración')
    s.shape(6.6, 1.1, 6.3, 4.4, 'rect', ('a', 'FFFFFF', 50), (INK, 1.25), SHD)
    s.text(6.75, 1.15, 6.0, 0.42, 'CONCENTRACIÓN ≠ FLUJO', 16, F_HEAD, INK, True, 'c', 'm')
    tank(s, 8.6, 2.2, 2.0, 2.4, 0.5, name='Pool plasmático')
    s.text(8.6, 4.62, 2.0, 0.3, 'glucemia «normal»', 12.5, F_HEAD, '1F4E79', True, 'c')
    s.arrow([(7.2, 1.75), (8.4, 1.75), (8.95, 2.35)], TRN, 9, name='Entrada alta')
    s.arrow([(10.3, 4.45), (10.95, 4.95), (12.3, 4.95)], TRN, 9, name='Salida alta')
    s.text(6.8, 1.85, 1.8, 0.75, '**Entrada**\n(producción hepática + absorción)', 12, F_BODY, INK, False, 'l')
    s.text(10.75, 3.7, 2.0, 0.75, '**Salida**\n(utilización periférica)', 12, F_BODY, INK, False, 'r')
    s.group_end()
    ex = card(s, 6.6, 5.7, 6.3, 1.4, '- Glucemia normal puede coexistir con **alta producción hepática** y **alta utilización** periférica.\n- Trigliceridemia alta: **exceso de producción**, **menor depuración** o ambas.', YEL, 14)
    s.step(fade(g1))
    s.step(fade(g2))
    s.step(fade(g3))
    s.step(fade(ex))
    s.note('La energía no se crea: el carbono de la dieta termina como CO2, glucógeno, TAG, colesterol, proteínas u otros '
           'intermediarios; el nitrógeno aminoacídico se redistribuye o se elimina, principalmente como urea y NH4+.\n'
           'Idea central de toda la clase: la regulación actúa sobre FLUJOS (moléculas por unidad de tiempo) y no solo sobre '
           'concentraciones. Un tanque con nivel constante puede tener entrada y salida muy grandes o muy pequeñas. Así, una '
           'glucemia normal no informa por sí sola si el hígado produce mucha o poca glucosa; una trigliceridemia elevada puede '
           'reflejar aumento de secreción de VLDL, menor depuración por LPL o ambas cosas.')


def t1d(D):
    s = new(D, U, '1 · Seis niveles de integración metabólica')
    lv = [('1', 'DISPONIBILIDAD DE SUSTRATOS', 'glucosa, AG, aminoácidos, O_{2}', 'continuo', 'FDEBD0'),
          ('2', 'SENSORES CELULARES', 'ATP/AMP, malonil-CoA, acetil-CoA, NADH/NAD^{+}', 'instantáneo', 'FAD7A0'),
          ('3', 'MODIFICACIÓN ALOSTÉRICA / COVALENTE', 'efectores alostéricos; fosforilación–desfosforilación', 'segundos–minutos', 'F8C471'),
          ('4', 'TRANSCRIPCIÓN', 'CREB, FOXO1, ChREBP, SREBP, PPARα', 'horas–días', 'F5B041'),
          ('5', 'INTERCAMBIO ENTRE ÓRGANOS', 'lactato, alanina, glutamina, glicerol, cuerpos cetónicos', 'minutos–días', 'EB984E'),
          ('6', 'CONTROL HIPOTALÁMICO Y CONDUCTUAL', 'hambre, saciedad, gasto, sistema autónomo', 'horas–años', 'DC7633')]
    ids = []
    for i, (n, t, d, tm, col) in enumerate(lv):
        y = 6.25 - i * 0.92
        x = 0.45 + i * 0.35
        g = s.group_start('Nivel ' + n)
        s.shape(x, y, 8.6 - i * 0.35, 0.8, 'rect', col, (INK, 1.25), SHD)
        badge(s, x + 0.12, y + 0.17, n, 0.46)
        s.text(x + 0.7, y + 0.02, 7.6 - i * 0.35, 0.4, t, 15, F_HEAD, INK, True, 'l', 'm')
        s.text(x + 0.7, y + 0.4, 5.6 - i * 0.35, 0.36, d, 12.5, F_BODY, '3A2A20', False, 'l', 'm')
        chip(s, x + 8.6 - i * 0.35 - 1.75, y + 0.42, tm, 'FFFFFF', 11.5, w=1.6, h=0.3, line=(INK, 0.75))
        s.group_end(); ids.append(g)
    c = card(s, 9.55, 1.15, 3.35, 3.0, '**Insulina** expresa predominantemente **abundancia**.\n\nEl **descenso de su acción**, junto con glucagón y señales contrarreguladoras, mantiene el aporte energético en ayuno.', YEL, 14.5, head='Señal maestra')
    mol(s, 12.1, 4.3, 'ins', d=0.6); mol(s, 11.35, 4.45, 'gcg', d=0.5)
    c2 = card(s, 9.55, 5.15, 3.35, 1.9, 'El balance **insulina/glucagón** importa más que una hormona aislada.', CREAM, 14.5)
    s.step(*[fade(g, after=(k > 0)) for k, g in enumerate(ids)])
    s.step(fade(c))
    s.step(fade(c2))
    s.note('Los seis niveles de integración funcionan con escalas temporales distintas: la disponibilidad de sustratos y los '
           'sensores (relación ATP/AMP, malonil-CoA, acetil-CoA) actúan de inmediato; la regulación alostérica y covalente '
           '(fosforilación por PKA, AMPK, Akt) en segundos a minutos; la transcripción en horas a días; el intercambio entre órganos '
           'acopla tejidos; y el hipotálamo coordina conducta alimentaria y gasto energético.\nEsta jerarquía se usará para '
           'responder siempre: ¿qué señal?, ¿dónde?, ¿qué enzima decide?, ¿a dónde va el carbono o el nitrógeno?, ¿qué pasa si falla?')


# ------------------------------------------------------------------ TEMA 2
def t2a(D):
    s = new(D, U, '2 · Ciclo alimentación–ayuno: fases orientativas')
    x0, x1 = 0.8, 12.6
    g = s.group_start('Eje temporal')
    s.arrow([(x0, 5.6), (x1 + 0.3, 5.6)], INK, 2.5)
    ticks = [(0, '0 h'), (0.13, '4 h'), (0.2, '6 h'), (0.36, '12 h'), (0.62, '48 h'), (0.75, '72 h'), (0.95, 'días')]
    for f, t in ticks:
        xx = x0 + f * (x1 - x0)
        s.arrow([(xx, 5.5), (xx, 5.7)], INK, 1.5, tail=None)
        s.text(xx - 0.4, 5.75, 0.8, 0.3, t, 13, F_HEAD, INK, True, 'c')
    s.group_end()
    phases = [(0, 0.13, 'Ingesta y absorción activa', '0–4 h', 'F5B041', 1.2),
              (0, 0.2, 'Posprandial', '0–6 h', 'F8C471', 1.9),
              (0.13, 0.36, 'Posabsortivo / ayuno temprano', '4–12 h', '85C1E9', 2.6),
              (0.36, 0.62, 'Ayuno intermedio', '12–48 h', '5DADE2', 3.3),
              (0.62, 1.0, 'Ayuno prolongado', '>48–72 h', '2E86C1', 4.0)]
    ids = []
    for a, b, t, tm, col, y in phases:
        xa = x0 + a * (x1 - x0); xb = x0 + b * (x1 - x0)
        ids.append(s.shape(xa, y, xb - xa, 0.55, 'rect', ('lin', [(0, lighten(col, 0.5)), (50, col), (100, lighten(col, 0.5))], 0),
                           (INK, 1.0), SHD, '**%s** · %s' % (t, tm), 13, F_HEAD, INK, False, 'l', 'm', (0.08, 0, 0.05, 0), name='Fase ' + tm))
    p = card(s, 0.8, 6.25, 7.6, 0.9, 'Los cortes son **orientativos**: el cambio es progresivo y depende del tamaño y la composición de la comida y de las reservas hepáticas.', CREAM, 14)
    r = note_box(s, 8.6, 6.25, 4.3, 0.9, 'Regla: lo que define la fase es la **dirección de los flujos** y la relación insulina/glucagón, no una hora exacta.', 13.5)
    w = s.shape(8.8, 1.15, 4.1, 0.95, 'rect', LBLUE, (INK, 1.0), False, 'Un desayuno graso y abundante prolonga la presencia de quilomicrones respecto de una carga líquida de glucosa.', 13, name='Ejemplo QM')
    s.step(fade(g))
    s.step(*[wipe(i, 'l', after=(k > 0)) for k, i in enumerate(ids)])
    s.step(fade(w))
    s.step(fade(p), fade(r, after=True))
    s.note('No existe una frontera horaria universal. Una clasificación didáctica razonable: ingesta y absorción activa 0–4 h '
           '(con superposición), posprandial 0–6 h, posabsortivo o ayuno temprano 4–12 h, ayuno intermedio 12–48 h y ayuno '
           'prolongado >48–72 h; la inanición sostenida se refiere a períodos más extensos de déficit energético. Las barras se '
           'superponen a propósito. En guías locales los cortes pueden variar: interpretarlos como orientadores. '
           'Lo que caracteriza el cambio de fase es la dirección de los flujos (captar frente a liberar glucosa, almacenar frente a '
           'movilizar lípidos) y la relación insulina/glucagón.')


def t2b(D):
    s = new(D, U, '2 · Qué cambia en cada fase')
    ph = [('0–4 h', 'F5B041', '- ↑ glucosa, aminoácidos e incretinas\n- ↑ insulina; ↓ glucagón/insulina\n- Hígado: glucogenogénesis y glucólisis\n- Músculo: capta glucosa, sintetiza glucógeno\n- Adipocito: esterifica AG\n- QM aparecen tras absorber grasa', 1),
          ('4–12 h', '85C1E9', '- Cae el flujo intestinal; ↓ insulina\n- Hígado pasa de captar a **liberar** glucosa\n- Predomina glucogenólisis al inicio\n- Crece la gluconeogénesis (lactato, glicerol, alanina)\n- Adiposo libera AG no esterificados y glicerol', 8),
          ('12–48 h', '5DADE2', '- ↓↓ glucógeno hepático\n- ↑ % de glucosa nueva de hígado y **corteza renal**\n- β-oxidación aporta energía para la gluconeogénesis\n- ↑ cetogénesis y lipólisis\n- Proteólisis aporta N y carbonos gluconeogénicos', 24),
          ('>3 días', '2E86C1', '- Cuerpos cetónicos: papel creciente en el SNC\n- ↓ necesidad de glucosa a expensas de proteína\n- Riñón: ↑ gluconeogénesis y amoniogénesis\n- Músculo: predominan AG\n- Eritrocito y otras células siguen requiriendo glucólisis', 72)]
    ids = []
    for i, (t, col, txt, hr) in enumerate(ph):
        x = 0.35 + i * 3.18
        g = s.group_start('Fase ' + t)
        s.shape(x, 1.15, 3.0, 5.95, 'rect', CREAM, (INK, 1.25), SHD)
        s.shape(x, 1.15, 3.0, 0.75, 'rect', col, (INK, 1.25), False, t, 22, F_HEAD, INK if i < 2 else WHITE, True, 'c', 'm')
        clock(s, x + 2.35, 1.22, 0.6, min(hr, 12) if hr < 24 else 12, name='Reloj ' + t)
        s.text(x + 0.12, 2.05, 2.8, 4.95, txt, 13.5, F_BODY, INK, False, 'l', 't', spc=5)
        s.group_end(); ids.append(g)
    for k, g in enumerate(ids):
        s.step(fade(g))
    s.note('0–4 h: suben glucosa, aminoácidos e incretinas; aumenta la insulina y baja la relación glucagón/insulina; el hígado '
           'realiza glucogenogénesis y glucólisis, el músculo capta glucosa y sintetiza glucógeno, el adipocito esterifica ácidos '
           'grasos. Los quilomicrones aparecen después de la absorción intestinal de grasa.\n4–12 h: cae el flujo intestinal, baja '
           'la insulina y el hígado pasa gradualmente de captar glucosa a liberarla; predomina al principio la glucogenólisis y '
           'crece la contribución gluconeogénica desde lactato, glicerol y alanina.\n12–48 h: el glucógeno hepático disminuye '
           'significativamente; aumenta el porcentaje de glucosa nueva producida por hígado y corteza renal; la β-oxidación aporta '
           'la energía hepática para la gluconeogénesis; aumentan cetogénesis y lipólisis; la proteólisis aporta nitrógeno y '
           'carbonos gluconeogénicos.\n>3 días: los cuerpos cetónicos adquieren un papel creciente en el SNC y disminuye la '
           'necesidad de producir glucosa a expensas de proteína muscular; el riñón incrementa gluconeogénesis y amoniogénesis. '
           'La necesidad de glucosa no desaparece: eritrocitos y otras células dependen de la glucólisis.')


def t2c(D):
    s = new(D, U, '2 · Evolución hormonal y de sustratos (esquema conceptual)')
    cats = ['Comida', '2 h', '6 h', '12 h', '24 h', '48 h', '3 d', '5 d']
    ser = [('Insulina', [10, 8, 4.5, 3.2, 2.6, 2.2, 2.0, 1.9]),
           ('Glucagón', [3, 3.2, 4.5, 5.5, 6.3, 6.8, 6.9, 6.9]),
           ('AG no esterificados', [2, 1.6, 3.2, 4.8, 6.4, 7.6, 8.2, 8.4]),
           ('Cuerpos cetónicos', [0.3, 0.3, 0.6, 1.2, 2.8, 5.0, 7.6, 8.8])]
    ch = chart_line(s, 0.45, 1.1, 8.3, 5.95, cats, ser, ['1F4E9A', 'D35400', 'D4AC0D', 'C2185B'],
                    ytitle='Nivel relativo (sin escala)', name='Gráfico evolución hormonal', size=13)
    c1 = card(s, 9.0, 1.1, 3.9, 1.85, 'La **insulina cae** pero no desaparece: la insulina residual limita lipólisis y cetogénesis extremas.', LBLUE, 14, head='Insulina')
    c2 = card(s, 9.0, 3.1, 3.9, 1.85, 'Aumenta la **relación glucagón/insulina**; catecolaminas, cortisol y GH participan según el contexto.', LSALMON, 14, head='Contrarregulación')
    c3 = card(s, 9.0, 5.1, 3.9, 1.95, 'Los **AG** suben primero; los **cuerpos cetónicos** crecen más tarde y sostienen al SNC en el ayuno prolongado.', YEL, 14, head='Sustratos')
    s.step(fade(ch))
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(c3))
    s.note('Gráfico conceptual de tendencias (no son valores medidos ni promedios obligatorios; el eje vertical no tiene escala). '
           'Tras una comida predomina la insulina; con el ayuno disminuye y aumenta la relación glucagón/insulina. Los ácidos grasos '
           'no esterificados ascienden al liberarse el freno antilipolítico, y los cuerpos cetónicos aumentan más tardíamente, '
           'alcanzando valores relevantes a partir de las 24–48 h y sosteniéndose en el ayuno prolongado. '
           'Insistir: el ayuno no es sinónimo de cetosis patológica; la insulina residual frena la lipólisis y la cetogénesis '
           'excesivas (diferencia con la cetoacidosis diabética).')


# ------------------------------------------------------------------ TEMA 3 — secuencia Morph 2
def portal_scene(s, stage):
    """stage 1: organismo; 2: hígado + hepatocito; 3: hepatocito con G6P"""
    if stage == 1:
        intestine(s, 0.8, 3.4, 3.0, name='!!Intestino')
        liver(s, 6.4, 1.3, 4.4, name='!!Hígado')
        pv = s.free(2.6, 2.4, 5.4, 2.2, [('M 0 900 C 250 900 400 650 600 450 C 750 300 850 150 1000 80', False, True)], None, ('6C3483', 22), name='!!Vena porta')
        return pv
    if stage == 2:
        intestine(s, -2.2, 5.2, 2.0, name='!!Intestino')
        liver(s, 0.4, 1.5, 4.6, name='!!Hígado')
        pv = s.free(-0.5, 3.4, 2.4, 2.4, [('M 0 900 C 250 900 400 650 600 450 C 750 300 850 150 1000 80', False, True)], None, ('6C3483', 22), name='!!Vena porta')
        return pv


def t3_portal1(D):
    s = new(D, U, '3 · Destino de la glucosa: intestino → porta → hígado', 'SECUENCIA MORPH 2 · 1/3')
    pv = portal_scene(s, 1)
    chip(s, 0.9, 6.6, 'INTESTINO DELGADO', TAG, 13, name='!!Rótulo intestino')
    chip(s, 3.6, 2.2, 'VENA PORTA', 'D7BDE2', 13, name='!!Rótulo porta')
    chip(s, 9.2, 1.1, 'HÍGADO', TAG, 13, name='!!Rótulo hígado')
    g1 = mol(s, 2.3, 4.6, 'glc', d=0.5, name='Glc 1'); g2 = mol(s, 2.0, 5.1, 'glc', d=0.5, name='Glc 2'); g3 = mol(s, 2.7, 5.0, 'glc', d=0.5, name='Glc 3')
    c = card(s, 8.0, 4.55, 4.9, 2.55, '- Absorción por **SGLT1** (apical) y **GLUT2** (basolateral) en el enterocito.\n- La glucosa llega por la **vena porta**: el hígado recibe la primera y mayor concentración.\n- Capta una **fracción variable**; el resto pasa a la circulación sistémica.', CREAM, 14)
    s.step(fade(g1), fade(g2), fade(g3))
    pts = [(1.0, -1.0), (2.6, -2.0), (4.4, -2.6)]
    s.step(path(g1, 5.0, -2.9, pts=[(1.2, -0.3), (2.8, -1.5)], dur=2200), path(g2, 5.4, -3.0, pts=[(1.5, -0.6), (3.2, -1.9)], dur=2400, delay=200),
           path(g3, 4.7, -2.6, pts=[(1.0, -0.3), (2.5, -1.2)], dur=2300, delay=100))
    s.step(fade(c))
    s.note('Secuencia Morph 2 (destino de la glucosa). Primera escena: la glucosa absorbida en el intestino (SGLT1 apical, GLUT2 '
           'basolateral) entra en la vena porta y alcanza el hígado antes que cualquier otro órgano. El hígado capta una fracción '
           'variable según la carga y el estado hormonal; el resto llega a la circulación sistémica.\nLas fichas azules (glucosa) '
           'se desplazan mediante trayectorias de movimiento reales. La transición siguiente es Morph: el hígado se agranda y '
           'aparece el hepatocito.')


def t3_portal2(D):
    s = new(D, U, '3 · En el hepatocito: GLUT2 y glucocinasa', 'SECUENCIA MORPH 2 · 2/3', morph=True)
    portal_scene(s, 2)
    chip(s, 0.6, 6.55, 'HÍGADO', TAG, 13, name='!!Rótulo hígado')
    hepatocyte(s, 5.7, 1.2, 4.2, name='!!Hepatocito', detail=False)
    nucleus(s, 7.15, 2.05, 0.9, name='!!Núcleo hepatocito')
    gl = glut(s, 5.55, 2.6, 0.62, name='!!GLUT2', color='5DADE2', text='GLUT2', horizontal=True)
    gk = enz(s, 6.6, 3.55, 'Glucocinasa (HK IV)', name='!!Glucocinasa')
    m = mol(s, 4.5, 2.65, 'glc', d=0.5, name='!!Glc hepática')
    g6 = mol(s, 7.6, 4.15, 'glc', 'G6P', d=0.62, name='!!G6P')
    gkrp = card(s, 10.15, 1.15, 2.75, 2.35, '**GLUT2**: bidireccional, alta capacidad.\n**Glucocinasa**: Km aparente alto, no inhibida por G6P; regulada por **GKRP**.', LBLUE, 13.5, name='Recuadro GLUT2 GK')
    trap = card(s, 10.15, 3.7, 2.75, 1.9, 'La fosforilación **atrapa** la glucosa como G6P y mantiene el gradiente de entrada.', YEL, 13.5, name='Recuadro atrapamiento')
    k = card(s, 5.7, 5.85, 7.2, 1.25, 'Glucosa → **glucosa-6-fosfato** (consume ATP). La G6P es la encrucijada que decide el destino del carbono.', CREAM, 14.5, name='Recuadro G6P')
    s.step(path(m, 1.65, 0.0, dur=1200))
    s.step(fade(gk), out(m, after=True), zoom(g6, after=True))
    s.step(fade(gkrp), fade(trap, after=True))
    s.step(fade(k))
    s.note('Morph: el hígado de la escena anterior se transforma (posición y tamaño) y aparece el hepatocito. GLUT2 es un '
           'transportador bidireccional de alta capacidad y baja afinidad: la entrada es proporcional a la glucemia portal. La '
           'glucocinasa (hexocinasa IV) tiene Km aparente alto y no es inhibida por la G6P; en ayuno se secuestra en el núcleo '
           'unida a GKRP y se libera al citosol cuando sube la glucosa (y la fructosa-1-P). La fosforilación atrapa la glucosa '
           'como G6P, que es la encrucijada metabólica de la diapositiva siguiente.')


def t3_portal3(D):
    s = new(D, U, '3 · La G6P como encrucijada en saciedad', 'SECUENCIA MORPH 2 · 3/3', morph=True)
    hepatocyte(s, 0.3, 1.0, 7.4, name='!!Hepatocito', detail=False)
    nucleus(s, 0.9, 1.6, 1.0, name='!!Núcleo hepatocito')
    gl = glut(s, 0.15, 3.3, 0.62, name='!!GLUT2', color='5DADE2', text='GLUT2', horizontal=True)
    g6 = mol(s, 3.55, 3.45, 'glc', 'G6P', d=0.8, name='!!G6P')
    br = [((3.95, 3.45), (3.95, 1.85), 'Glucógeno', 'Glucógeno sintasa (desfosforilada)', MINT, (2.6, 1.15)),
          ((4.35, 3.85), (4.95, 3.85), 'Glucólisis → piruvato', 'PFK-1 (F2,6BP) · PK-L', LSALMON, (5.0, 3.4)),
          ((3.55, 3.85), (2.0, 5.2), 'Vía de las pentosas', 'G6PDH → NADPH', LILAC, (0.8, 5.25)),
          ((4.2, 4.25), (5.2, 5.6), 'Acetil-CoA → citrato → lipogénesis', 'si persiste excedente', YEL, (4.3, 5.65))]
    ids = []
    for (p1, p2, t, e, f, (bx, by)) in br:
        g = s.group_start('Rama ' + t[:20])
        s.arrow([p1, p2], ACT, 3.5)
        card(s, bx, by, 2.65, 0.95, '**%s**\n%s' % (t, e), f, 13, align='c', anchor='m')
        s.group_end(); ids.append(g)
    gp = enz(s, 2.05, 2.75, 'G6Pasa (inactiva en saciedad)', fill='EEEEEE', color='7F8C8D', name='G6Pasa')
    side = card(s, 8.0, 1.0, 4.9, 3.0, '**Objetivo hepático posprandial**: amortiguar la glucemia y canalizar carbonos hacia **reserva** (glucógeno), **oxidación** y **biosíntesis** (NADPH, AG).', CREAM, 14.5, head='Integración')
    side2 = card(s, 8.0, 4.25, 4.9, 2.85, '- **Insulina** activa glucógeno sintasa e inhibe fosforilasa.\n- **ChREBP** (carbohidratos) y **SREBP-1c** (insulina) inducen genes lipogénicos.\n- El exceso persistente aumenta la secreción de **VLDL**.', YEL, 14, head='Regulación')
    for g in ids:
        s.step(fade(g))
    s.step(fade(gp))
    s.step(fade(side), fade(side2, after=True))
    s.note('Morph: el hepatocito ocupa ahora gran parte de la diapositiva y la G6P se ubica en el centro. Destinos en saciedad: '
           '(1) glucógeno, por glucógeno sintasa activada por desfosforilación; (2) glucólisis, favorecida por la '
           'fructosa-2,6-bisfosfato (activador de PFK-1) y la piruvato cinasa L desfosforilada; (3) vía de las pentosas fosfato '
           '(G6PDH) que genera NADPH para biosíntesis; (4) si persiste el excedente energético, piruvato → acetil-CoA → citrato, '
           'que sale al citosol y alimenta la lipogénesis (ATP-citrato liasa, ACC, FASN). La glucosa-6-fosfatasa no aporta glucosa '
           'a la sangre en este estado. Este es el "punto de bifurcación" que se regulará de modo opuesto en ayuno.')


def t3_muscle(D):
    s = new(D, U, '3 · Glucosa en músculo y adipocito: GLUT4 dependiente de insulina')
    membrane_h(s, 0.4, 2.3, 7.6, 0.4, name='Membrana plasmática')
    ir = insulin_receptor(s, 1.0, 2.32, 0.4, 0.75, name='Receptor de insulina')
    ins = mol(s, 1.25, 1.0, 'ins', d=0.45, name='Insulina')
    cas = flow(s, ['IRS', 'PI3K', 'PIP_{3}', 'Akt'], 0.6, 3.75, 4.6, 0.62, [LBLUE, LBLUE, LBLUE, MINT], 15, 0.35, bold=True)
    ves = []
    for i, (vx, vy) in enumerate(((5.6, 5.2), (6.4, 5.7), (7.1, 5.0))):
        g = s.group_start('Vesícula GLUT4 %d' % (i + 1))
        s.shape(vx, vy, 0.7, 0.7, 'ellipse', ('a', 'FDEBD0', 80), ('C0392B', 1.5), False)
        glut(s, vx + 0.18, vy + 0.08, 0.5, text=None, color='2E86C1')
        s.group_end(); ves.append(g)
    s.text(5.5, 6.45, 2.6, 0.5, 'Vesículas con GLUT4', 12.5, F_HEAD, '922B21', True, 'c')
    glcs = [mol(s, 5.7 + i * 0.7, 1.25, 'glc', d=0.42, name='Glc %d' % i) for i in range(3)]
    tx = card(s, 8.4, 1.1, 4.5, 3.0, '- Insulina → receptor **tirosina cinasa** → **IRS** → **PI3K** → PIP_{3} → **Akt**.\n- Akt (vía AS160/TBC1D4) promueve la **translocación de GLUT4** a la membrana.\n- La glucosa se **oxida**, se **almacena** (glucógeno) o aporta **glicerol-3-P** (adipocito).', CREAM, 14)
    tx2 = card(s, 8.4, 4.3, 4.5, 2.8, '- La **contracción** también transloca GLUT4 por vías **independientes de insulina** (AMPK, Ca^{2+}).\n- Hígado (GLUT2), eritrocito (GLUT1) y neurona (GLUT3) **no** dependen de insulina para captar glucosa.', LBLUE, 14)
    s.step(path(ins, 0.0, 0.85, dur=900), pulse(ir, after=True))
    for b, a in cas:
        if a:
            s.anim[-1].append(wipe(a, 'l', after=True)); s.anim[-1].append(fade(b))
        else:
            s.anim[-1].append(fade(b, after=True))
    s.step(path(ves[0], 0.0, -2.85, dur=1400), path(ves[1], -0.1, -3.35, dur=1600, delay=150), path(ves[2], 0.2, -2.65, dur=1500, delay=300))
    s.step(*[path(g, 0, 1.6, dur=1000, after=(i > 0), delay=0) for i, g in enumerate(glcs)])
    s.step(fade(tx))
    s.step(fade(tx2))
    s.note('En músculo y tejido adiposo la captación de glucosa depende de la insulina: la unión al receptor (tirosina cinasa) '
           'produce autofosforilación, reclutamiento de IRS, activación de PI3K, formación de PIP3 y activación de Akt. Akt '
           'fosforila AS160 (TBC1D4), lo que permite que las vesículas intracelulares con GLUT4 se fusionen con la membrana '
           'plasmática (ampliación bibliográfica: Lehninger, cap. 12 y 23). La animación muestra primero la cascada, luego el '
           'desplazamiento de las vesículas y por último la entrada de glucosa por los GLUT4 recién insertados.\nEn el músculo, la '
           'contracción moviliza GLUT4 por vías independientes de insulina (AMPK y Ca2+), por eso el ejercicio mejora la captación '
           'aun en resistencia insulínica.')


def t3_lip1(D):
    s = new(D, U, '3 · Lípidos de la dieta: del enterocito al quilomicrón')
    s.shape(0.4, 1.05, 12.5, 0.9, 'rect', ('a', 'FFF3D6', 70), None, False, name='Luz intestinal')
    s.text(0.5, 1.07, 3, 0.3, 'LUZ INTESTINAL', 12, F_HEAD, '7E5109', True)
    tag = mol(s, 0.7, 1.4, 'tag', 'TAG', d=0.5, name='TAG dietario')
    mic = []
    for i in range(3):
        g = s.group_start('Micela %d' % i)
        cx = 2.4 + i * 0.75
        s.shape(cx, 1.35, 0.55, 0.55, 'ellipse', ('a', 'FCF3CF', 90), ('B7950B', 1.25, 'sysDot'), False)
        ag_chain(s, cx + 0.1, 1.55, 0.36, 0.1)
        s.group_end(); mic.append(g)
    enterocyte_row(s, 0.4, 2.0, 7.6, 3.1, 4, name='Enterocitos')
    er = rer(s, 2.1, 3.0, 1.6, 0.8, name='RE liso')
    tag2 = mol(s, 4.0, 3.15, 'tag', 'TAG', d=0.5, name='TAG reesterificado')
    qm = lipoprotein(s, 5.6, 3.2, 1.15, 'F7DC6F', 'QM', [('2E4A9E', 200, 120, 5, 'ApoB-48')], name='Quilomicrón naciente')
    s.shape(0.4, 5.25, 7.6, 0.75, 'rect', ('lin', [(0, 'FDFEFE'), (100, 'EAF2F8')], 90), ('85929E', 1.0), False, 'VASO LINFÁTICO (QUILÍFERO) → conducto torácico → sangre', 13, F_HEAD, '34495E', True, 'c', 'm', name='Quilífero')
    st = [('1', 'Emulsificación (sales biliares) e hidrólisis por **lipasa pancreática** → 2-monoacilglicerol + AG.'),
          ('2', 'Micelas entregan AG y MAG al enterocito.'),
          ('3', '**Reesterificación** a TAG en el RE.'),
          ('4', 'Ensamblaje con **ApoB-48** (MTP), fosfolípidos y colesterol → **quilomicrón**.'),
          ('5', 'Exocitosis basolateral hacia la **linfa**; luego a la sangre.')]
    ids = []
    for i, (n, t) in enumerate(st):
        g = s.group_start('Paso lípidos %s' % n)
        badge(s, 8.3, 1.1 + i * 1.18, n)
        s.text(8.85, 1.03 + i * 1.18, 4.05, 1.1, t, 14, F_BODY, INK, False, 'l', 'm')
        s.group_end(); ids.append(g)
    s.step(fade(ids[0]), fade(tag, after=True))
    s.step(fade(ids[1]), *[fade(m, after=True) for m in mic])
    s.step(fade(ids[2]), path(mic[1], -0.2, 1.75, dur=1000, after=True), fade(er), fade(tag2, after=True))
    s.step(fade(ids[3]), zoom(qm, after=True))
    s.step(fade(ids[4]), path(qm, 0.4, 1.95, dur=1500, after=True))
    s.note('Los TAG dietarios se emulsifican con sales biliares y se hidrolizan por la lipasa pancreática (con colipasa) a '
           '2-monoacilglicerol y ácidos grasos, que llegan al enterocito en micelas. En el retículo endoplasmático se reesterifican '
           'a TAG y se ensamblan con ApoB-48 por acción de la MTP, junto con fosfolípidos, colesterol y vitaminas liposolubles, '
           'formando quilomicrones (QM). Los QM salen por exocitosis basolateral a los quilíferos (linfa) y llegan a la sangre por '
           'el conducto torácico, evitando el primer paso hepático. Los ácidos grasos de cadena media siguen otra ruta (portal) '
           'que se analiza en el tema 17.')


def t3_lip2(D):
    s = new(D, U, '3 · Quilomicrones en circulación: LPL y remanentes')
    vessel(s, 0.3, 1.3, 12.7, 1.3, name='Capilar', rbcs=5)
    qm = lipoprotein(s, 0.6, 1.4, 1.1, 'F7DC6F', 'QM', [('2E4A9E', 200, 120, 5, None)], name='!!QM circulante')
    hdl = lipoprotein(s, 3.2, 3.0, 0.75, 'F5CBA7', 'HDL', [('5DADE2', 180, 160, 4, None)], name='HDL donante')
    apc = chip(s, 2.5, 3.85, 'ApoC-II + ApoE', MINT, 13, name='Apos transferidas')
    lpl = enz(s, 5.2, 2.65, 'LPL (endotelio)', name='LPL')
    ag1 = ag_chain(s, 5.6, 3.3, 0.7, 0.16, name='AG liberados 1'); ag2 = ag_chain(s, 6.2, 3.55, 0.7, 0.16, name='AG liberados 2')
    gly = mol(s, 7.3, 2.0, 'gly', d=0.4, name='Glicerol')
    musc = muscle_fiber(s, 4.6, 4.65, 3.1, 0.55, name='Fibra muscular')
    adi = adipocyte_white(s, 7.9, 4.35, 1.4, name='Adipocito')
    s.text(4.6, 5.25, 3.1, 0.3, 'MÚSCULO: oxidación', 12.5, F_HEAD, '922B21', True, 'c')
    s.text(7.6, 5.8, 2.0, 0.3, 'ADIPOCITO: reserva', 12.5, F_HEAD, '7E5109', True, 'c')
    rem = lipoprotein(s, 10.4, 1.55, 0.75, 'F39C12', 'REM', [('8E44AD', 300, 60, 4, None)], name='Remanente')
    liv = liver(s, 10.0, 3.35, 2.9, name='Hígado')
    s.text(9.9, 5.4, 3.1, 0.4, 'Remanentes captados vía **ApoE**', 13, F_HEAD, '6E2C00', True, 'c')
    k = card(s, 0.4, 5.85, 9.3, 1.25, 'Los AG **no son producidos** por el quilomicrón: se **liberan de los TAG** que transporta. La insulina favorece el direccionamiento posprandial de la grasa hacia el adiposo (según lecho vascular y estado metabólico).', YEL, 13.5)
    s.step(fade(hdl), fade(apc, after=True), path(apc, -1.5, -1.95, dur=1300, after=True))
    s.step(path(qm, 4.0, 0.0, dur=1800), fade(lpl, after=True))
    s.step(fade(ag1), fade(ag2), wipe(musc, 'l', after=True), fade(adi))
    s.step(path(ag1, -0.5, 1.4, dur=1200), path(ag2, 2.0, 1.4, dur=1300), fade(gly), path(gly, 3.4, 1.5, after=True, dur=1500))
    s.step(path(qm, 4.9, 0.0, dur=1600), fade(rem, after=True), path(rem, 0.6, 1.6, after=True, dur=1200), fade(liv))
    s.step(fade(k))
    s.note('En la circulación los QM adquieren ApoC-II y ApoE desde las HDL. La ApoC-II activa la lipoproteína lipasa (LPL), '
           'anclada al endotelio capilar (vía GPIHBP1), que hidroliza los TAG del QM: los ácidos grasos se captan en músculo '
           '(oxidación) y adipocito (reesterificación y reserva), y el glicerol viaja sobre todo al hígado, que posee glicerol '
           'cinasa. El QM se transforma en remanente rico en colesterol, captado por el hígado mediante receptores que reconocen '
           'ApoE. La insulina aumenta la LPL del tejido adiposo en el estado alimentado. Precisión conceptual: los ácidos grasos '
           'no son "producidos" por el quilomicrón, se liberan de los TAG que transporta.')


def t3_aa(D):
    s = new(D, U, '3 · Aminoácidos en saciedad: no existe un depósito específico')
    intestine(s, 0.4, 1.2, 2.0, name='Intestino')
    liver(s, 3.0, 1.05, 3.0, name='Hígado')
    muscle(s, 0.4, 4.6, 3.2, name='Músculo', fibers=2)
    a1 = arrow_lbl(s, [(2.3, 2.3), (3.2, 2.0)], 'Porta', TRN, 3.5, lw=0.9)
    a2 = arrow_lbl(s, [(4.0, 3.0), (2.6, 4.5)], 'AA restantes', TRN, 3.5, lw=1.5)
    c1 = card(s, 6.2, 1.1, 3.2, 1.75, 'Síntesis de **proteínas hepáticas y plasmáticas** (albúmina, factores de coagulación).', LSALMON, 13.5, head='Hígado')
    c2 = card(s, 3.9, 4.05, 3.0, 1.85, '**Ramificados** (leucina, isoleucina, valina): metabolismo **extrahepático** importante (músculo).', MINT, 13.5, head='BCAA')
    # esqueletos carbonados
    g = s.group_start('Esqueletos carbonados')
    s.shape(7.2, 3.05, 5.7, 2.85, 'rect', CREAM, (INK, 1.25), SHD)
    s.text(7.35, 3.1, 5.4, 0.38, 'ENTRADA DE ESQUELETOS CARBONADOS', 14, F_HEAD, INK, True, 'c', 'm')
    for i, t in enumerate(['Piruvato', 'Acetil-CoA', 'α-cetoglutarato', 'Succinil-CoA', 'Fumarato', 'Oxaloacetato']):
        chip(s, 7.45 + (i % 3) * 1.8, 3.65 + (i // 3) * 0.6, t, YEL if t != 'Acetil-CoA' else ENE, 12.5, w=1.68, h=0.44)
    s.text(7.4, 4.95, 5.3, 0.9, 'El **nitrógeno** se reutiliza o se elimina vía transaminación, desaminación y **ciclo de la urea**.', 13.5, F_BODY)
    s.group_end()
    p = note_box(s, 0.4, 6.15, 12.5, 0.95, 'No hay «glucógeno de aminoácidos»: el balance proteico depende de **síntesis frente a degradación**. El exceso de N se elimina como urea.', 14.5)
    s.step(wipe(a1, 'l'), fade(c1, after=True))
    s.step(wipe(a2, 'r'), fade(c2, after=True))
    s.step(fade(g))
    s.step(fade(p))
    s.note('Los aminoácidos llegan mayormente por la vena porta. Una parte se usa para proteínas hepáticas y plasmáticas; otra '
           'parte pasa al músculo y a otros tejidos. Los aminoácidos de cadena ramificada (leucina, isoleucina, valina) escapan en '
           'buena medida del hígado (baja actividad de su aminotransferasa hepática) y se metabolizan en el músculo.\n'
           'Los esqueletos carbonados ingresan como piruvato, acetil-CoA, α-cetoglutarato, succinil-CoA, fumarato u oxaloacetato '
           '(los que dan acetil-CoA no son gluconeogénicos netos). El nitrógeno se reutiliza o se elimina por el ciclo de la urea. '
           'No existe un depósito de aminoácidos análogo al glucógeno: el balance proteico es la diferencia entre síntesis y '
           'degradación.')


def t3_reg(D):
    s = new(D, U, '3 · Conexión reguladora del estado alimentado')
    hepatocyte(s, 0.4, 1.3, 4.6, name='Hepatocito', detail=False)
    nuc = s.shape(1.7, 2.3, 2.0, 1.6, 'ellipse', shade('7D5BA6', 0.45, 0.3), ('4A235A', 1.5), False, 'NÚCLEO', 14, F_HEAD, WHITE, True, 'c', 'm', name='Núcleo')
    sigs = [('Insulina', 'ins', 'Promueve almacenamiento y síntesis proteica; favorece **SREBP-1c**.', LBLUE),
            ('Leucina', 'aa', 'Activa **mTORC1** cuando hay contexto energético y otros aminoácidos → síntesis proteica.', MINT),
            ('Glucosa', 'glc', 'Sus metabolitos activan **ChREBP** → genes de glucólisis y lipogénesis.', LSALMON),
            ('Exceso energético persistente', 'tag', 'Puede incrementar la **secreción hepática de VLDL**.', YEL)]
    ids = []
    for i, (h, k, t, f) in enumerate(sigs):
        y = 1.1 + i * 1.5
        g = s.group_start('Señal ' + h)
        mol(s, 5.4, y + 0.42, k, d=0.55)
        s.arrow([(5.35, y + 0.7), (3.8, 3.1)], ACT, 2.0, dash='dash')
        card(s, 6.15, y, 6.75, 1.3, t, f, 15, head=h)
        s.group_end(); ids.append(g)
    for g in ids:
        s.step(fade(g))
    s.note('Conexión reguladora en saciedad: la insulina promueve almacenamiento (glucógeno, TAG) y síntesis proteica; la leucina '
           'activa mTORC1 cuando existe contexto energético y disponibilidad de otros aminoácidos; los metabolitos de la glucosa '
           'activan ChREBP y la señal insulínica favorece el procesamiento de SREBP-1c, ambos inductores de enzimas lipogénicas '
           '(ACC, FASN). Un exceso energético persistente puede aumentar la secreción hepática de VLDL. Estos factores se '
           'desarrollan en detalle en el tema 23.')


def build(D):
    div(D)
    t1a(D); t1b(D); t1c(D); t1d(D)
    t2a(D); t2b(D); t2c(D)
    t3_portal1(D); t3_portal2(D); t3_portal3(D)
    t3_muscle(D); t3_lip1(D); t3_lip2(D); t3_aa(D); t3_reg(D)
