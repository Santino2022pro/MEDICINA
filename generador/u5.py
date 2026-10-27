# -*- coding: utf-8 -*-
"""UNIDAD V — Integración metabólica en patología (8 situaciones)"""
from base import *

U = 5


def div(D):
    def art(s):
        liver(s, 8.4, 0.9, 4.4, name='Arte hígado')
        heart(s, 8.6, 3.9, 1.6, name='Arte corazón')
        artery_wall(s, 10.4, 3.9, 2.6, 1.8, name='Arte arteria')
        brain(s, 10.6, 5.6, 1.8, name='Arte cerebro')
        lipoprotein(s, 8.5, 5.8, 1.1, 'E67E22', 'LDL', [('2E4A9E', 180, 180, 5, None)], name='Arte LDL')
    divider(D, U, 'V', 'INTEGRACIÓN\nEN PATOLOGÍA', 'Cuando un engranaje falla, todo el sistema cambia',
            ['P1 · Insuficiencia funcional hepática', 'P2 · Fructosa, hipertrigliceridemia e hígado graso', 'P3 · Deficiencia de CPT1 o de carnitina',
             'P4 · TAG de cadena media en hiperquilomicronemia', 'P5 · LDL, HDL, íntima arterial y aterogénesis', 'P6 · Hipertrigliceridemia y riesgo aterogénico',
             'P7 · Proteínas, neomicina y lactulosa', 'P8 · Hiperuricemia y metabolismo de purinas'], art,
            'Unidad V. Cada situación se analiza con la misma secuencia: funcionamiento normal, alteración primaria, mecanismo '
            'molecular, consecuencias metabólicas, compensaciones, manifestaciones clínicas, integración interorgánica y un esquema '
            'final que contrasta lo normal con lo patológico.')


STEPS8 = ['Normal', 'Alteración', 'Mecanismo', 'Consecuencias', 'Compensación', 'Clínica', 'Integración', 'Esquema']


def ptrack(s, active):
    """tira con las 8 etapas del análisis fisiopatológico"""
    g = s.group_start('!!Etapas análisis')
    for i, t in enumerate(STEPS8):
        on = i + 1 in active
        s.shape(0.4 + i * 1.57, 6.78, 1.5, 0.34, 'roundRect', TAG if on else ('FFFFFF' if True else 'EEEEEE'), (INK, 1.0 if on else 0.5), False,
                '%d · %s' % (i + 1, t), 10.5, F_HEAD, INK if on else '7F8C8D', True, 'c', 'm', (0.02, 0, 0.02, 0), fit=False, adj={'adj': 40000})
    return s.group_end()


def pnew(D, n, ttl, sub, active):
    s = new(D, U, 'P%d · %s' % (n, ttl), 'PATOLOGÍA %d · %s' % (n, sub))
    ptrack(s, active)
    return s


def scheme(s, left, right, block_at, x0=0.4, w=6.1, y0=1.15, h=5.45, ltitle='FUNCIONAMIENTO NORMAL', rtitle='ALTERACIÓN PATOLÓGICA',
           swap=False):
    """esquema final: dos columnas de flujo; en la columna patológica el paso block_at aparece interrumpido"""
    ids = []
    cfg = ((0, left, ltitle, MINT, ACT), (1, right, rtitle, LSALMON, INH))
    if swap:
        cfg = ((0, left, ltitle, LSALMON, INH), (1, right, rtitle, MINT, ACT))
    bcol = 0 if swap else 1
    for col, items, ttl, f, bc in cfg:
        x = x0 + col * (w + 0.3)
        g = s.group_start('Esquema ' + ttl.lower())
        s.shape(x, y0, w, h, 'rect', ('a', 'FFFFFF', 45), (bc, 2.5), SHD)
        s.shape(x, y0, w, 0.5, 'rect', bc, None, False, ttl, 15, F_HEAD, WHITE, True, 'c', 'm')
        n = len(items)
        bh = (h - 0.7 - 0.25 * (n - 1)) / n
        for i, t in enumerate(items):
            yy = y0 + 0.6 + i * (bh + 0.25)
            ff = (RED if (col == bcol and i == block_at) else f)
            s.shape(x + 0.25, yy, w - 0.5, bh, 'roundRect', ff, (INK, 1.0), False, t, 13.5, F_BODY, WHITE if ff == RED else INK, False, 'c', 'm', (0.06, 0, 0.06, 0), adj={'adj': 15000}, minsize=10)
            if i:
                if col == bcol and i == block_at + 1:
                    s.arrow([(x + w / 2, yy - 0.24), (x + w / 2, yy - 0.02)], INH, 2.5, dash='sysDash', tail='triangle')
                    s.text(x + w / 2 + 0.1, yy - 0.26, 0.6, 0.25, '✗', 13, F_HEAD, INH, True, 'l', 'm')
                else:
                    s.arrow([(x + w / 2, yy - 0.24), (x + w / 2, yy - 0.02)], bc, 2.5)
        ids.append(s.group_end())
    return ids


# ------------------------------------------------------------------ P1 insuficiencia hepática
def p1a(D):
    s = pnew(D, 1, 'Insuficiencia funcional hepática', 'HÍGADO', [1, 2])
    liver(s, 0.4, 1.15, 3.6, name='Hígado sano')
    fn = card(s, 4.3, 1.1, 8.6, 2.3, 'Produce y almacena glucosa · detoxifica nitrógeno (urea) · sintetiza **albúmina y coagulación** · conjuga **bilirrubina** y secreta bilis · maneja **lipoproteínas** · depura **hormonas, fármacos y lactato**.', MINT, 14.5, head='Funcionamiento normal', headfill=ACT)
    al = card(s, 4.3, 3.6, 8.6, 1.5, 'La insuficiencia altera **simultáneamente** producción, depuración, almacenamiento, síntesis proteica y biotransformación; **cada cambio repercute en otros órganos**.', LSALMON, 14.5, head='Alteración primaria', headfill=INH)
    lab = note_box(s, 0.4, 5.3, 12.5, 1.35, '**Lesión ≠ insuficiencia**: ALT/AST indican **lesión**; INR/tiempo de protrombina, factor V, bilirrubina, albúmina y evolución clínica orientan (con limitaciones) a **funciones** específicas.', 14)
    s.step(fade(fn)); s.step(fade(al)); s.step(fade(lab))
    s.note('Patología 1. La insuficiencia hepática altera simultáneamente producción, depuración, almacenamiento, síntesis proteica '
           'y biotransformación; cada cambio tiene repercusiones interorgánicas. No todo paciente con enzimas de lesión elevadas '
           'tiene insuficiencia de síntesis: ALT/AST indican lesión, mientras INR/tiempo de protrombina, factor V, bilirrubina, '
           'albúmina y la evolución clínica orientan, con limitaciones, a funciones específicas. La tira inferior indica la etapa '
           'del análisis fisiopatológico en curso.')


def p1b(D):
    s = pnew(D, 1, 'Glucosa y nitrógeno en la falla hepática', 'HÍGADO', [3, 4])
    g = card(s, 0.4, 1.1, 6.1, 2.6, '- ↓ glucógeno útil y ↓ salida de glucosa (glucogenólisis/GNG) → **hipoglucemia** en insuficiencia severa, sobre todo en **ayuno** o desnutrición.\n- En cirrosis pueden **coexistir** resistencia insulínica e **hiperglucemia** (captación/depuración de insulina alteradas).', LBLUE, 13.5, head='1 · Homeostasis de glucosa')
    seq = flow(s, ['↓ ciclo de la urea + derivación portosistémica', 'NH_{4}^{+} ↑', 'Glutamina astroglial ↑', 'Neurotransmisión alterada → encefalopatía'],
               6.8, 1.1, 6.1, 4.2, [LSALMON, YEL, PINK, RED], 13.5, 0.22, 'v', INH)
    nb = note_box(s, 0.4, 3.95, 6.1, 1.35, 'No atribuir **todos** los síntomas neurológicos solo al amonio plasmático: **inflamación**, otros tóxicos y precipitantes interactúan.', 13)
    lv = liver(s, 0.6, 5.4, 1.6, name='Hígado cirrótico', color='9C640C')
    br = brain(s, 2.8, 5.4, 1.6, name='Cerebro')
    a = s.arrow([(2.2, 5.85), (2.8, 5.85)], INH, 3)
    s.step(fade(g))
    flow_anim(s, seq)
    s.step(fade(nb)); s.step(fade(lv), wipe(a, 'l', after=True), fade(br, after=True))
    s.note('1) Homeostasis de glucosa: disminución del glucógeno útil y de la salida de glucosa por glucogenólisis y '
           'gluconeogénesis → hipoglucemia en la insuficiencia severa, sobre todo en ayuno o desnutrición; pueden coexistir '
           'resistencia insulínica e hiperglucemia en la cirrosis por alteraciones complejas de captación y depuración de '
           'insulina. 2) Detoxificación nitrogenada: disminución de la capacidad del ciclo de la urea y derivación portosistémica → '
           'hiperamonemia, glutamina astroglial aumentada, disfunción de la neurotransmisión y encefalopatía; no todos los síntomas '
           'se deben solo al amonio plasmático.')


def p1c(D):
    s = pnew(D, 1, 'Síntesis proteica, bilirrubina y bilis', 'HÍGADO', [4, 6])
    a = card(s, 0.4, 1.1, 6.1, 2.65, '- ↓ **albúmina** → menor presión oncótica: participa, con **hipertensión portal** y **retención renal de Na^{+}**, en **ascitis/edemas**.\n- ↓ **factores de coagulación** → **INR prolongado**.', LBLUE, 14, head='3 · Síntesis proteica plasmática')
    i = note_box(s, 0.4, 3.95, 6.1, 1.45, 'En la hepatopatía crónica caen **procoagulantes y anticoagulantes**: el INR **no refleja por sí solo** el riesgo hemorrágico real.', 13.5)
    b = card(s, 6.8, 1.1, 6.1, 2.65, '- Captación, conjugación o excreción alteradas → **ictericia**, **coluria** (según fracción) y colestasis.\n- ↓ bilis al intestino → **malabsorción** de lípidos y vitaminas **A, D, E, K**; **esteatorrea**.', YEL, 14, head='4 · Bilirrubina y sales biliares')
    k = card(s, 6.8, 3.95, 6.1, 1.45, 'La vitamina **K** malabsorbida agrava el defecto de coagulación (según tipo y grado de lesión).', LSALMON, 13.5)
    ic = [mol(s, 0.6 + i * 0.75, 5.75, k, d=0.6) for i, k in enumerate(('aa', 'chol', 'gly'))]
    s.text(3.0, 5.7, 9.8, 0.7, 'Proteínas plasmáticas · colesterol/ácidos biliares · bilirrubina: tres productos hepáticos que **faltan** en la falla.', 13.5, F_BODY, INK, False, 'l', 'm')
    s.step(fade(a)); s.step(fade(i)); s.step(fade(b)); s.step(fade(k))
    s.note('3) Síntesis proteica plasmática: menos albúmina → menor presión oncótica, que participa con la hipertensión portal y la '
           'retención renal de sodio en la ascitis y los edemas; menos factores de coagulación → INR prolongado. En la hepatopatía '
           'crónica disminuyen simultáneamente proteínas procoagulantes y anticoagulantes, por lo que el INR no refleja por sí solo '
           'el riesgo hemorrágico. 4) Bilirrubina y sales biliares: captación, conjugación o excreción alteradas → ictericia, '
           'coluria según la fracción y colestasis; menor secreción de bilis → malabsorción de lípidos y vitaminas A, D, E, K y '
           'esteatorrea, según el tipo y grado de lesión.')


def p1d(D):
    s = pnew(D, 1, 'Lípidos, hormonas, fármacos y lactato', 'HÍGADO', [4, 5, 6])
    it = [('5 · Lípidos y lipoproteínas', 'Alteración de síntesis de VLDL, esterificación/oxidación de AG y producción/eliminación de colesterol → perfiles **heterogéneos**; la esteatosis puede coexistir con desnutrición. Difiere entre hepatopatía colestásica, metabólica y falla extrema.', YEL),
          ('6 · Metabolismo hormonal', '↓ depuración de hormonas; cambios en esteroides y hormonas tiroideas: **hiperestrogenismo relativo**, hipogonadismo, cambios de masa muscular y del eje glucémico.', LILAC),
          ('7 · Xenobióticos y fármacos', '↓ CYP/UGT, ↓ primer paso, cambios de albúmina y flujo → dosis efectivas y **toxicidad variables**.', LBLUE),
          ('8 · Lactato', '↓ depuración hepática → **hiperlactatemia**, sobre todo con hipoperfusión; el lactato alto **no prueba** hipoxia aislada.', LSALMON)]
    ids = [card(s, 0.4 + (i % 2) * 6.4, 1.1 + (i // 2) * 2.75, 6.1, 2.55, d, f, 14, head=t) for i, (t, d, f) in enumerate(it)]
    for g in ids:
        s.step(fade(g))
    s.note('5) Lípidos: alteración de la síntesis de VLDL, de la esterificación/oxidación de AG y de la producción/eliminación de '
           'colesterol → perfiles heterogéneos de TAG y colesterol; la esteatosis puede coexistir con desnutrición. 6) Hormonas: '
           'disminuye la depuración hormonal y cambia el metabolismo de esteroides y tiroideas → hiperestrogenismo relativo, '
           'cambios de masa muscular, hipogonadismo y alteraciones glucémicas. 7) Fármacos: menor actividad CYP/UGT, menor primer '
           'paso y cambios de albúmina/flujo → dosis efectivas y toxicidad variables. 8) Lactato: depuración reducida → '
           'hiperlactatemia, sobre todo con hipoperfusión; el lactato elevado no prueba necesariamente hipoxia aislada.')


def p1e(D):
    s = pnew(D, 1, 'Integración y esquema: hígado sano frente a falla', 'HÍGADO', [7, 8])
    ids = scheme(s, ['Glucógeno + GNG → glucosa estable', 'NH_{4}^{+} → urea (periportal) + GS (perivenosa)', 'Albúmina y factores de coagulación', 'Bilirrubina conjugada → bilis', 'Depuración de hormonas, fármacos y lactato'],
                 ['Hipoglucemia (o hiperglucemia en cirrosis)', '↑ NH_{4}^{+} → glutamina astroglial → encefalopatía', '↓ albúmina (ascitis) · INR prolongado', 'Ictericia · malabsorción de vitaminas liposolubles', 'Toxicidad de fármacos · hiperestrogenismo · ↑ lactato'], 1)
    s.step(fade(ids[0])); s.step(fade(ids[1]))
    s.note('Esquema final de la patología 1 y eje clínico: en la falla hepática conviene estudiar glucosa, INR, bilirrubina, '
           'función renal, sodio, estado nutricional, precipitantes de encefalopatía y signos hemodinámicos, más que memorizar '
           '"el hígado hace 500 funciones". Integración interorgánica: cerebro (encefalopatía), riñón (retención de sodio, '
           'síndrome hepatorrenal), músculo (sarcopenia, menor captación muscular de amonio), intestino (fuente de amonio) y '
           'sistema endocrino.')


# ------------------------------------------------------------------ P2 fructosa
def p2a(D):
    s = pnew(D, 2, 'Fructosa, hipertrigliceridemia e hígado graso', 'FRUCTOSA', [1, 2])
    intestine(s, 0.4, 1.2, 2.2, name='Intestino'); liver(s, 2.9, 1.3, 3.0, name='Hígado')
    n = card(s, 6.2, 1.1, 6.7, 2.35, 'La fructosa se metaboliza principalmente en **intestino e hígado**; con cargas moderadas el intestino capta y transforma una parte importante.', MINT, 14.5, head='Funcionamiento normal', headfill=ACT)
    a = card(s, 6.2, 3.65, 6.7, 2.95, 'Cuando la carga **supera la capacidad intestinal**, una **mayor fracción** alcanza el hígado, donde su entrada **evita PFK-1** y puede generar un **flujo rápido de triosas**; con exceso **sostenido** → DNL, TAG, VLDL.', LSALMON, 14.5, head='Alteración primaria', headfill=INH)
    f1 = [mol(s, 1.0 + i * 0.4, 3.6, 'fru', d=0.42, name='Fru %d' % i) for i in range(4)]
    s.step(fade(n), *[fade(m, after=(i == 0)) for i, m in enumerate(f1[:2])], *[path(m, 2.6, -1.2, dur=1200, after=(i == 0)) for i, m in enumerate(f1[:1])])
    s.step(fade(a), *[fade(m) for m in f1[2:]], path(f1[2], 2.4, -1.1, dur=1200, after=True), path(f1[3], 2.2, -1.0, dur=1200), path(f1[1], 2.7, -1.15, dur=1200))
    s.note('Patología 2. La fructosa se metaboliza principalmente en el intestino y el hígado; cuando la carga supera la '
           'capacidad intestinal, una mayor fracción alcanza el hígado. Allí su entrada por fructocinasa evita el paso limitante de '
           'PFK-1, lo que puede favorecer un flujo rápido de triosas en determinadas cargas. Las fichas naranjas muestran el paso '
           'de fructosa del intestino al hígado; con mayor carga, más fructosa llega al hígado.')


def p2b(D):
    s = pnew(D, 2, 'Mecanismo molecular hepático de la fructosa', 'FRUCTOSA', [3, 4])
    c = chain(s, 0.5, 1.15, ['Fructosa', 'Fructosa-1-P', 'Gliceraldehído + DHAP', 'Triosas fosfato'], dy=1.15, w=2.9,
              enzymes=['KHK/fructocinasa (ATP → ADP)', 'aldolasa B', 'triosa cinasa (ATP)'], rev=[False, False, False],
              fill=[lighten(MOL['fru'][0], 0.5), YEL, YEL, YEL], name='Fructolisis', h=0.55, size=14)
    br = [('Piruvato/acetil-CoA → **DNL** (ChREBP/SREBP-1c) → TAG → **VLDL**', LSALMON, 4.1, 1.15),
          ('Glicerol-3-P → esterificación', YEL, 4.1, 2.45),
          ('Glucosa · **glucógeno** · **lactato**', MINT, 4.1, 3.75)]
    ids = []
    for t, f, x, y in br:
        g = s.group_start('Destino ' + plain(t)[:14])
        s.arrow([(3.42, 4.8), (x - 0.02, y + 0.45)], ACT, 2.5)
        card(s, x, y, 4.6, 1.05, t, f, 13.5, anchor='m', grow=False)
        s.group_end(); ids.append(g)
    ur = flow(s, ['Consumo rápido de ATP', 'AMP → IMP', 'Ácido úrico'], 9.0, 1.15, 3.9, 3.65, ['FDEBD0', YEL, lighten(MOL['urate'][0], 0.5)], 13.5, 0.2, 'v', INH)
    k = card(s, 4.1, 5.05, 8.8, 1.55, 'Ruta **posible** en todas las cargas; **aumentada** en carga alta crónica. No todo el carbono de la fructosa se transforma en grasa.', CREAM, 14)
    chain_anim(s, c, per_click=2)
    for g in ids:
        s.step(fade(g))
    flow_anim(s, ur)
    s.step(fade(k))
    s.note('En el hígado la KHK/fructocinasa forma fructosa-1-fosfato consumiendo ATP; la aldolasa B produce gliceraldehído y '
           'DHAP; la triosa cinasa forma gliceraldehído-3-P. Secuencia de exceso sostenido: triosas → piruvato/acetil-CoA, '
           'glicerol-3-P y señales de carbohidratos → ↑ DNL vía ChREBP/SREBP-1c → TAG hepáticos y VLDL. El consumo rápido de ATP y '
           'la degradación de AMP → IMP → ácido úrico pueden acompañar a las altas cargas. La fructosa también contribuye a '
           'glucógeno y lactato.')


def p2c(D):
    s = pnew(D, 2, 'Consecuencias, evidencia y clínica', 'FRUCTOSA', [4, 5, 6])
    c = card(s, 0.4, 1.1, 6.1, 2.6, '- ↑ **TAG hepáticos** (esteatosis) y ↑ **VLDL** → hipertrigliceridemia.\n- Baja saciedad de bebidas → **exceso calórico**, adiposidad, **resistencia insulínica**.\n- Posible ↑ **urato**.', LSALMON, 14, head='Consecuencias')
    e = card(s, 6.8, 1.1, 6.1, 2.6, '- Estudios **isocalóricos** y de **sobrealimentación** no dan la misma respuesta: **el exceso energético importa**.\n- No confundir **fruta entera** con jarabes o bebidas de alta carga.', YEL, 14, head='Interpretación de la evidencia')
    k = card(s, 0.4, 3.9, 12.5, 1.5, 'Las asociaciones epidemiológicas con hígado graso/DM2 pueden incluir factores **dietarios y de adiposidad**; los mecanismos moleculares **no implican causalidad única universal**. La hipertrigliceridemia deriva de **mayor secreción de VLDL y/o menor depuración**, acentuada por la resistencia insulínica.', CREAM, 14)
    s.step(fade(c)); s.step(fade(e)); s.step(fade(k))
    s.note('Consecuencias: TAG hepáticos y VLDL, posible aumento de urato; el exceso calórico y la baja saciedad de las bebidas '
           'facilitan la acumulación adiposa, la resistencia insulínica y la esteatosis. Interpretación de la evidencia: los '
           'experimentos isocalóricos y con sobrealimentación no dan exactamente la misma respuesta; el exceso energético '
           'importa. Las asociaciones epidemiológicas pueden incluir factores dietarios y de adiposidad; los mecanismos moleculares '
           'no implican causalidad única universal.')


def p2d(D):
    s = pnew(D, 2, 'Esquema: carga habitual frente a carga alta crónica', 'FRUCTOSA', [7, 8])
    ids = scheme(s, ['Fructosa moderada (fruta entera)', 'Mayor parte captada por el intestino', 'Hígado: triosas → glucosa, glucógeno, lactato', 'DNL baja · TAG estables'],
                 ['Fructosa alta y sostenida (bebidas)', 'Desborda el intestino → hígado', 'Triosas sin freno de PFK-1 → ↑ DNL', '↑ TAG hepático (esteatosis) · ↑ VLDL · ↑ urato'], 2,
                 ltitle='CARGA HABITUAL', rtitle='CARGA ALTA CRÓNICA')
    s.step(fade(ids[0])); s.step(fade(ids[1]))
    s.note('Esquema final: con cargas moderadas (por ejemplo, fruta entera) la mayor parte de la fructosa se maneja en el '
           'intestino y el hígado la deriva a glucosa, glucógeno y lactato; con cargas altas y sostenidas, más fructosa llega al '
           'hígado y, sin el freno de PFK-1, aumenta la lipogénesis de novo, los TAG hepáticos, la VLDL y el urato. Integración: '
           'intestino → hígado → adiposo/músculo (resistencia insulínica) → riñón (urato).')


# ------------------------------------------------------------------ P3 CPT1/carnitina
def p3a(D):
    s = pnew(D, 3, 'Deficiencia de CPT1 o de carnitina y aporte al SNC', 'CPT1 / CARNITINA', [1, 2])
    liver(s, 0.4, 1.3, 2.8, name='Hígado'); brain(s, 0.6, 3.55, 2.4, name='Cerebro')
    n = card(s, 3.5, 1.1, 9.4, 2.4, 'En **ayuno** el hígado importa AG largos (**CPT1 → acilcarnitina → CACT → CPT2**), los β-oxida y obtiene **ATP/NADH** para la gluconeogénesis y **acetil-CoA** para **cetogénesis** y activar la piruvato carboxilasa: el cerebro recibe **glucosa y cetonas**.', MINT, 14.5, head='Funcionamiento normal', headfill=ACT)
    a = card(s, 3.5, 3.7, 9.4, 2.85, 'Deficiencia hepática de **CPT1A** o de **carnitina** utilizable → los AG largos **no atraviesan** eficazmente la membrana mitocondrial interna como acil-CoA → ↓ β-oxidación hepática en ayuno.', LSALMON, 14.5, head='Alteración primaria', headfill=INH)
    s.step(fade(n)); s.step(fade(a))
    s.note('Patología 3. Los AG largos no atraviesan eficazmente la membrana mitocondrial interna como acil-CoA: requieren CPT1 → '
           'acilcarnitina → CACT → CPT2. Una deficiencia hepática de CPT1A o de carnitina utilizable reduce la β-oxidación '
           'hepática durante el ayuno.')


def p3b(D):
    s = pnew(D, 3, 'La cadena causal correcta', 'CPT1 / CARNITINA', [3, 4])
    seq = flow(s, ['Defecto de importación mitocondrial **hepática** (CPT1A / carnitina)', '↓ β-oxidación: ↓ ATP/NADH y ↓ acetil-CoA', '↓ activación de piruvato carboxilasa → ↓ soporte gluconeogénico', '↓ cetogénesis', 'Cerebro: **menos glucosa y menos cetonas**', 'Hipoglucemia **hipocetósica**, letargo, convulsiones, encefalopatía'],
               0.4, 1.1, 7.6, 5.5, [LSALMON, YEL, YEL, PINK, LBLUE, RED], 14, 0.18, 'v', INH)
    w = note_box(s, 8.3, 1.1, 4.6, 3.0, 'Incorrecto: «las neuronas dependen de CPT1 para oxidar AG largos». El cerebro falla **indirectamente**, porque el hígado no le provee glucosa ni cetonas.', 14)
    iso = card(s, 8.3, 4.3, 4.6, 2.3, '**CPT1A** (hígado) · **CPT1B** (músculo) · **CPT1C** (predominantemente neuronal, función diferente).', CREAM, 14, head='Isoformas')
    flow_anim(s, seq)
    s.step(zoom(w)); s.step(fade(iso))
    s.note('Cadena causal correcta: defecto de importación mitocondrial hepática → β-oxidación inadecuada → menos ATP/NADH y '
           'menos acetil-CoA activador de la piruvato carboxilasa → menor capacidad de sostener la gluconeogénesis y menor '
           'cetogénesis → el SNC, que no utiliza grandes cantidades de AG de cadena larga como combustible directo, recibe menos '
           'glucosa y menos cuerpos cetónicos → hipoglucemia hipocetósica, letargo, convulsiones o encefalopatía. No debe '
           'explicarse diciendo que las neuronas dependen de CPT1 para oxidar AG largos a gran escala.')


def p3c(D):
    s = pnew(D, 3, 'Clínica, diagnóstico y esquema', 'CPT1 / CARNITINA', [5, 6, 7, 8])
    cl = card(s, 0.4, 1.1, 4.6, 5.5, '- Crisis tras **enfermedad o ayuno**\n- **Hipoglucemia**\n- **Cetonas inadecuadamente bajas**\n- Hepatomegalia\n- Posible **hiperamonemia**\n- **Perfil de acilcarnitinas** y genética orientan\n- Principio general: **evitar el ayuno prolongado**', LSALMON, 14, head='Clínica y diagnóstico')
    ids = scheme(s, ['Ayuno → AG al hígado', 'CPT1 → β-oxidación', 'GNG + cetogénesis', 'Cerebro: glucosa + cetonas'],
                 ['Ayuno → AG al hígado', 'CPT1/carnitina deficiente', '↓ GNG · ↓ cetogénesis', 'Hipoglucemia hipocetósica'], 1, x0=5.25, w=3.7, h=4.95)
    k = s.text(5.25, 6.25, 7.6, 0.4, 'Deficiencia **sistémica** de carnitina: puede afectar también **miocardio y músculo** (≠ defecto aislado de CPT1A).', 12.5, F_BODY, INK, False, 'l', 'm')
    s.step(fade(cl)); s.step(fade(ids[0])); s.step(fade(ids[1])); s.step(fade(k))
    s.note('Clínica y diagnóstico: crisis tras enfermedad o ayuno, hipoglucemia, cetonas inadecuadamente bajas, hepatomegalia y '
           'posible hiperamonemia; el perfil de acilcarnitinas y la genética orientan. La deficiencia sistémica de carnitina puede '
           'afectar también miocardio y músculo, y no es idéntica al defecto aislado de CPT1A. El abordaje específico exige un '
           'equipo de enfermedades metabólicas; evitar el ayuno prolongado es un principio general.')


# ------------------------------------------------------------------ P4 MCT
def p4a(D):
    s = pnew(D, 4, 'TAG de cadena media en la hiperquilomicronemia', 'MCT', [1, 2, 3])
    n = card(s, 0.4, 1.1, 6.1, 2.3, 'Los AG **largos** viajan en **QM**; la **LPL** (con ApoC-II, GPIHBP1, APOA5) hidroliza sus TAG en los capilares.', MINT, 14.5, head='Funcionamiento normal', headfill=ACT)
    a = card(s, 6.8, 1.1, 6.1, 2.3, 'Alteración grave de **LPL** o proteínas relacionadas → los QM se depuran mal → **TAG muy elevados** y riesgo de **pancreatitis**.', LSALMON, 14.5, head='Alteración primaria', headfill=INH)
    vessel(s, 0.4, 3.7, 12.5, 1.1, name='Capilar con QM', rbcs=2)
    qms = [lipoprotein(s, 1.0 + i * 1.3, 3.75, 1.0, 'F7DC6F', 'QM', [('2E4A9E', 200, 110, 4, None)], name='QM acumulado %d' % i) for i in range(8)]
    x = s.shape(5.2, 4.95, 2.9, 0.5, 'roundRect', RED, (INK, 1.0), False, 'LPL deficiente', 13, F_HEAD, WHITE, True, 'c', 'm', name='LPL deficiente')
    m = card(s, 0.4, 5.65, 12.5, 1.0, 'Los AG **C8/C10** de los MCT se absorben en mayor proporción por **vía portal** y usan menos el ensamblaje de QM.', YEL, 14, grow=False)
    s.step(fade(n)); s.step(fade(a), *[zoom(q, after=(i == 0)) for i, q in enumerate(qms)], fade(x)); s.step(fade(m))
    s.note('Patología 4. En la hiperquilomicronemia por alteración grave de LPL o proteínas relacionadas (ApoC-II, GPIHBP1, APOA5), '
           'los QM se depuran deficientemente y los TAG circulantes pueden alcanzar valores elevados con riesgo de pancreatitis. '
           'Los TAG C8/C10, una vez digeridos, generan AG que se absorben en mayor proporción por vía portal y usan menos el '
           'ensamblaje de QM, frente a los AG largos.')


def p4b(D):
    s = pnew(D, 4, 'Mecanismo del beneficio y sus límites', 'MCT', [3, 5, 6, 7, 8])
    ids = scheme(s, ['Grasa de cadena larga', 'Enterocito → QM → linfa', 'LPL deficiente → QM persisten', 'TAG ↑↑ → riesgo de pancreatitis'],
                 ['MCT (C8/C10)', 'Enterocito → vena porta (albúmina)', 'Hígado: oxidación sin depender de CPT1', 'Energía con menor carga de QM'], 2,
                 ltitle='GRASA LARGA EN DÉFICIT DE LPL', rtitle='MCT: RUTA ALTERNATIVA', w=3.9, h=5.45, swap=True)
    k = card(s, 8.85, 1.15, 4.05, 5.45, '- Restricción **intensa** de AG largos con **supervisión** nutricional.\n- Garantizar **AG esenciales** y **vitaminas liposolubles**.\n- No sustituir por mezclas con **laurato** (no todos los MCT son iguales).\n- En la forma **multifactorial**: limitar **azúcares refinados y alcohol** (↑ VLDL).\n- Los MCT **no curan** la deficiencia de LPL.', CREAM, 13.5, head='Límites y manejo')
    s.step(fade(ids[0])); s.step(fade(ids[1])); s.step(fade(k))
    s.note('Mecanismo: los MCT aportan energía con menor carga sobre la vía intestinal QM → LPL y pueden oxidarse sin la '
           'dependencia habitual de carnitina/CPT1. Límites: la dieta suele requerir restricción intensa de AG de cadena larga, '
           'supervisión nutricional y garantizar AG esenciales y vitaminas liposolubles; no debe sustituirse grasa larga por '
           'mezclas con laurato suponiendo que todos los MCT se comportan igual. En la quilomicronemia multifactorial, limitar '
           'azúcares refinados y alcohol también importa porque aumentan la producción de VLDL. Los MCT no curan la deficiencia de '
           'LPL ni hacen innecesario el tratamiento especializado.')


# ------------------------------------------------------------------ P5 aterogénesis
def p5a(D):
    s = pnew(D, 5, 'LDL, HDL, íntima arterial y aterogénesis', 'ATEROGÉNESIS', [1, 2])
    artery_wall(s, 0.4, 1.15, 8.2, 5.4, name='Pared arterial')
    for i, (x, y) in enumerate(((1.0, 1.4), (2.6, 1.8), (4.4, 1.3), (6.2, 1.7))):
        lipoprotein(s, x, y, 0.55, 'E67E22', 'LDL', [('2E4A9E', 180, 180, 3, None)], name='LDL luz %d' % i, tsize=8)
    lb = [chip(s, 6.9, 1.2, 'LUZ', 'FFFFFF', 12), chip(s, 6.9, 2.95, 'ENDOTELIO', 'FFFFFF', 12), chip(s, 6.9, 3.6, 'ÍNTIMA', 'FFFFFF', 12), chip(s, 6.9, 4.9, 'MEDIA (músculo liso)', 'FFFFFF', 12)]
    n = card(s, 8.9, 1.1, 4.0, 2.6, 'Las partículas con **ApoB** entregan colesterol a los tejidos vía **LDLR**, regulado por el contenido celular (SREBP-2).', MINT, 14, head='Normal', headfill=ACT)
    a = card(s, 8.9, 3.9, 4.0, 2.7, 'Exposición **acumulada** a partículas **ApoB** (LDL, remanentes VLDL/IDL, **Lp(a)**) que **atraviesan** el endotelio y quedan **retenidas** en la íntima.', LSALMON, 14, head='Alteración primaria', headfill=INH)
    s.step(*[fade(x) for x in lb]); s.step(fade(n)); s.step(fade(a))
    s.note('Patología 5. Corte de la pared arterial: luz, endotelio, íntima, media con células de músculo liso y adventicia. '
           'Normalmente, las partículas con ApoB entregan colesterol a los tejidos mediante el LDLR regulado por SREBP-2. La '
           'alteración primaria de la aterogénesis es la exposición acumulada a partículas con ApoB (LDL, remanentes de VLDL/IDL y '
           'Lp(a)) que atraviesan el endotelio y quedan retenidas por interacción con proteoglucanos de la íntima.')


def p5b(D):
    s = pnew(D, 5, 'Aterogénesis paso a paso', 'ATEROGÉNESIS', [3, 4])
    artery_wall(s, 0.4, 1.15, 8.2, 5.4, name='Pared arterial')
    ldl = lipoprotein(s, 1.0, 1.5, 0.6, 'E67E22', 'LDL', [('2E4A9E', 180, 180, 3, None)], name='LDL que entra', tsize=8)
    ret = [s.shape(1.6 + i * 0.5, 3.4 + (i % 2) * 0.3, 0.35, 0.35, 'ellipse', shade('D35400', 0.3, 0.2), ('6E2C00', 0.75), False, name='LDL retenida %d' % i) for i in range(4)]
    ox = chip(s, 3.6, 3.35, 'LDL modificada/oxidada', LSALMON, 12, name='LDL ox')
    mono = s.shape(4.2, 1.6, 0.7, 0.7, 'ellipse', shade('A569BD', 0.35, 0.2), ('4A235A', 1.0), False, 'Mono', 10, F_HEAD, WHITE, True, 'c', 'm', name='Monocito')
    foam = s.shape(5.3, 3.25, 1.5, 1.0, 'ellipse', ('rad', [(0, 'FDFEFE'), (60, 'F9E79F'), (100, 'D4AC0D')], (40, 40)), ('7E5109', 1.5), SHD, 'Célula\nespumosa', 11.5, F_HEAD, INK, True, 'c', 'm', name='Célula espumosa')
    plq = s.free(1.2, 2.35, 6.0, 1.5, smooth([(0, 1000), (200, 300), (500, 0), (800, 300), (1000, 1000)], False), ('a', 'F5CBA7', 70), ('922B21', 2.0), name='Placa')
    st = [('1', 'Entrada y **retención** por proteoglucanos de la íntima'), ('2', '**Modificación** (agregación, oxidación, enzimas) → captación por macrófagos vía **CD36, SR-A**: no se regulan a la baja → **células espumosas**'),
          ('3', '**Inflamación** crónica: monocitos, linfocitos T, citocinas, inflamasoma'), ('4', '**Placa**: muerte celular, núcleo necrótico, músculo liso y matriz fibrosa; **ruptura/erosión → trombosis**')]
    ids = []
    for i, (n, t) in enumerate(st):
        g = s.group_start('Paso atero ' + n)
        badge(s, 8.85, 1.15 + i * 1.38, n)
        s.text(9.4, 1.05 + i * 1.38, 3.5, 1.3, t, 13, F_BODY, INK, False, 'l', 'm')
        s.group_end(); ids.append(g)
    s.step(fade(ids[0]), path(ldl, 0.8, 1.9, after=True, dur=1300), *[zoom(r, after=(i == 0)) for i, r in enumerate(ret)])
    s.step(fade(ids[1]), fade(ox, after=True), fade(mono), path(mono, 1.2, 1.75, after=True, dur=1200), zoom(foam, after=True))
    s.step(fade(ids[2]), pulse(foam, after=True))
    s.step(fade(ids[3]), wipe(plq, 'b', after=True))
    s.note('1) Entrada y retención: las partículas con ApoB atraviesan el endotelio y quedan retenidas por proteoglucanos. 2) '
           'Modificación: agregación, oxidación y acción enzimática favorecen la captación por macrófagos vía receptores scavenger '
           '(CD36, SR-A), que, a diferencia del LDLR, no se regulan adecuadamente a la baja por la carga intracelular → células '
           'espumosas. 3) Inflamación: monocitos, linfocitos T, citocinas e inflamasoma participan en la lesión crónica. 4) Placa: '
           'muerte celular, núcleo necrótico, proliferación de músculo liso y matriz fibrosa; la ruptura o erosión puede '
           'desencadenar trombosis. La animación sigue la LDL desde la luz hasta la formación de la célula espumosa y la placa.')


def p5c(D):
    s = pnew(D, 5, 'HDL y la falsa dicotomía «colesterol bueno/malo»', 'ATEROGÉNESIS', [5, 6, 7, 8])
    h = card(s, 0.4, 1.1, 6.1, 2.6, '- **ApoA-I/ABCA1/ABCG1**: eflujo de colesterol de macrófagos; **LCAT** lo esterifica; **SR-BI**: retorno hepático.\n- Funciones antiinflamatorias, antioxidantes y endoteliales en **algunos modelos**.', MINT, 13.5, head='HDL: compensación')
    l = note_box(s, 6.8, 1.1, 6.1, 2.6, 'HDL-C alto **no demuestra** transporte reverso eficiente; tratamientos que **solo elevan HDL-C** no han garantizado menos eventos. Es más sólido identificar las **partículas ApoB** y su exposición acumulada como **blanco causal**.', 13.5)
    d = card(s, 0.4, 3.9, 12.5, 1.5, '«Malo» y «bueno» **no** son moléculas distintas: el **colesterol es el mismo** en transportadores distintos. La aterogenicidad depende del **número, retención, composición/modificación** de las partículas y de la respuesta arterial. **LDL-C, no-HDL-C y ApoB** se complementan.', YEL, 14)
    cl = card(s, 0.4, 5.55, 12.5, 1.05, '**Integración**: hígado (LDLR, PCSK9) · intestino (absorción, ácidos biliares) · pared arterial (retención, inflamación) · médula ósea (monocitos).', CREAM, 13.5, grow=False)
    s.step(fade(h)); s.step(fade(l)); s.step(fade(d)); s.step(fade(cl))
    s.note('HDL: ApoA-I/ABCA1/ABCG1 favorecen el eflujo de colesterol de macrófagos, la LCAT lo esterifica y SR-BI permite su '
           'retorno hepático; se describen funciones antiinflamatorias, antioxidantes y endoteliales en algunos modelos. Sin '
           'embargo, un HDL-C plasmático elevado no demuestra que el transporte reverso sea eficiente, y los tratamientos que '
           'únicamente elevan HDL-C no han garantizado menos eventos cardiovasculares. LDL y HDL no son "colesterol malo" y "bueno" '
           'como entidades químicas diferentes: el colesterol es la misma molécula en transportadores distintos.')


# ------------------------------------------------------------------ P6 hipertrigliceridemia
def p6a(D):
    s = pnew(D, 6, 'Hipertrigliceridemia y riesgo aterogénico', 'TRIGLICÉRIDOS', [1, 2, 3])
    c = chain(s, 0.5, 1.2, ['VLDL (rica en TAG)', 'Remanente (pierde TAG, conserva colesterol)', 'Entra y se retiene en la íntima'], dy=1.35, w=4.6,
              enzymes=['LPL', None], rev=[False, False], fill=['F5CBA7', 'F39C12', LSALMON], name='Remanentes', h=0.7, size=14.5)
    lp = [lipoprotein(s, 5.4, 1.1, 1.0, 'F5CBA7', 'VLDL', [('2E4A9E', 190, 150, 4, None)], name='VLDL ic'),
          lipoprotein(s, 5.6, 2.55, 0.7, 'F39C12', 'Rem', [('2E4A9E', 190, 150, 4, None)], name='Rem ic')]
    k = card(s, 7.0, 1.1, 5.9, 3.0, 'El **colesterol transportado por remanentes ApoB** —no el TAG libre dentro de una célula espumosa— es un mecanismo clave de aterogénesis.', YEL, 15, head='Mecanismo')
    m = card(s, 0.4, 4.75, 12.5, 1.85, 'La hipertrigliceridemia a menudo **señala** resistencia a la insulina, **más partículas remanentes**, **HDL bajo** y **LDL pequeñas y densas**; la relación causa/indicador es **compleja**.', CREAM, 15)
    chain_anim(s, c, per_click=1)
    s.anim[0].append(fade(lp[0])); s.anim[1].append(fade(lp[1]))
    s.step(fade(k)); s.step(fade(m))
    s.note('Patología 6. Las VLDL y los remanentes ricos en TAG pueden penetrar la íntima; tras la acción de la LPL pierden TAG pero '
           'mantienen cantidades significativas de colesterol, adquieren menor tamaño y pueden retenerse en la pared. La cantidad '
           'de colesterol transportado por remanentes ApoB, no el TAG libre dentro de una célula espumosa, es un mecanismo clave. '
           'La hipertrigliceridemia a menudo señala resistencia a la insulina, mayor número de remanentes, HDL bajo y LDL '
           'pequeñas y densas.')


def p6b(D):
    s = pnew(D, 6, 'Dos desenlaces diferentes', 'TRIGLICÉRIDOS', [6])
    heart(s, 0.6, 1.2, 1.8, name='Corazón'); pancreas(s, 7.0, 1.6, 2.6, name='Páncreas')
    a = card(s, 0.4, 3.2, 6.1, 3.4, '**Riesgo cardiovascular aterosclerótico**: sobre todo por **remanentes/ApoB** y comorbilidades.', LSALMON, 15.5, head='(a) Aterosclerosis', headfill=INH)
    b = card(s, 6.8, 3.2, 6.1, 3.4, '**Pancreatitis** cuando los TAG son muy altos: riesgo creciente **>500 mg/dL** y muy marcado desde **~1000 mg/dL** (no son umbrales absolutos).', YEL, 15.5, head='(b) Pancreatitis', headfill=ORANGE)
    m = s.text(2.6, 1.5, 4.3, 1.4, 'Modificadores: **alcohol**, descontrol glucémico, **hipotiroidismo**, fármacos y **genética**.', 14, F_BODY, INK, False, 'l', 'm')
    s.step(fade(a)); s.step(fade(b)); s.step(fade(m))
    s.note('Dos desenlaces diferentes: (a) riesgo cardiovascular aterosclerótico, sobre todo por remanentes/ApoB y comorbilidades; '
           '(b) riesgo de pancreatitis cuando los TAG alcanzan niveles muy altos, particularmente >500 mg/dL de forma creciente y muy '
           'marcado desde ~1000 mg/dL, con cifras que no son umbrales absolutos. Alcohol, descontrol glucémico, hipotiroidismo, '
           'fármacos y genética modifican los TG. No reducir la interpretación clínica de TAG elevados a "riesgo de infarto".')


def p6c(D):
    s = pnew(D, 6, 'Resistencia insulínica: el mecanismo integrador', 'TRIGLICÉRIDOS', [4, 5, 7, 8])
    adipose_tissue(s, 0.4, 1.3, 2.6, name='Adiposo resistente')
    liver(s, 4.4, 1.2, 3.2, name='Hígado')
    vessel(s, 8.3, 1.6, 4.6, 0.9, name='Plasma', rbcs=2)
    a1 = arrow_lbl(s, [(3.0, 2.2), (4.5, 2.2)], 'AG portal ↑', TRN, 4, lw=1.4, lx=3.0, ly=1.7)
    a2 = arrow_lbl(s, [(7.6, 2.0), (8.3, 2.0)], 'VLDL ↑', TRN, 4, lw=1.2, lx=7.5, ly=1.5)
    sq = flow(s, ['Lipólisis adiposa **mal suprimida**', 'AG portal → hígado', 'Reesterificación + **DNL** ↑', '**VLDL ↑** y ↓ depuración', '**Hipertrigliceridemia**'],
              0.4, 3.6, 12.5, 1.3, [YEL, LBLUE, LSALMON, LSALMON, RED], 13.5, 0.25, 'h', INH)
    k = card(s, 0.4, 5.15, 12.5, 1.45, '**CETP** redistribuye TAG y colesterol esterificado; la **lipasa hepática** remodela HDL/LDL (→ HDL bajo, LDL pequeñas). **Tratar la etiología** reduce la producción y/o mejora la depuración.', CREAM, 14)
    s.step(wipe(a1, 'l')); s.step(wipe(a2, 'l'))
    flow_anim(s, sq)
    s.step(fade(k))
    s.note('Mecanismo integrador en la resistencia insulínica: lipólisis adiposa mal suprimida → AG portales al hígado → '
           'reesterificación y VLDL ↑; aumento de la DNL y menor depuración de partículas → hipertrigliceridemia. La CETP '
           'redistribuye TAG y colesterol esterificado; la lipasa hepática remodela HDL y LDL. Tratar la etiología reduce la '
           'producción y/o mejora la depuración.')


# ------------------------------------------------------------------ P7 encefalopatía
def p7a(D):
    s = pnew(D, 7, 'Amonio: intestino, hígado, músculo y cerebro', 'ENCEFALOPATÍA', [1, 2])
    intestine(s, 0.4, 1.2, 2.2, name='Intestino'); liver(s, 3.0, 1.2, 2.8, name='Hígado'); muscle(s, 0.4, 4.2, 2.8, name='Músculo', fibers=2); brain(s, 3.6, 4.0, 2.2, name='Cerebro')
    a1 = arrow_lbl(s, [(2.6, 2.0), (3.1, 2.0)], 'NH_{3}', NIT, 4, lw=0.8, lx=2.45, ly=1.55)
    a2 = arrow_lbl(s, [(2.0, 3.3), (1.9, 4.2)], 'GS', NIT, 3, lw=0.6, lx=2.05, ly=3.55)
    n = card(s, 6.2, 1.1, 6.7, 2.5, '- **Bacterias intestinales** (ureasa) y el metabolismo de glutamina producen NH_{3}, que llega por la **porta**.\n- El **hígado** lo convierte en urea y glutamina; el **músculo** también lo captura (GS).', MINT, 14, head='Funcionamiento normal', headfill=ACT)
    a = card(s, 6.2, 3.8, 6.7, 2.8, '- **↓ ureogénesis** hepatocelular.\n- **Derivaciones portosistémicas**: el NH_{3} evita el primer paso.\n- **Sarcopenia**: el músculo pierde capacidad de incorporar NH_{4}^{+} en glutamina.', LSALMON, 14, head='Alteración en la cirrosis', headfill=INH)
    s.step(wipe(a1, 'l'), fade(n)); s.step(wipe(a2, 't'), fade(a))
    s.note('Patología 7. Normalmente el amoníaco producido por bacterias intestinales con ureasa y por el metabolismo intestinal '
           'de glutamina llega por la porta al hígado, que lo convierte en urea y glutamina; el músculo también lo capta como '
           'glutamina. En la cirrosis disminuye la ureogénesis, las derivaciones portosistémicas evitan el primer paso y la '
           'sarcopenia reduce la captación muscular de amonio.')


def p7b(D):
    s = pnew(D, 7, 'Fundamento bioquímico de la indicación histórica', 'ENCEFALOPATÍA', [3, 4])
    hist = s.shape(0.4, 1.1, 12.5, 0.75, 'rect', 'D5D8DC', (INK, 1.25), SHD, 'Consigna histórica: (a) proteína ≤ 0,8 g/kg/d · (b) neomicina intestinal · (c) lactulosa', 16, F_HEAD, INK, True, 'c', 'm', name='Consigna histórica')
    it = [('(a) Menos proteína', 'Menos sustrato proteico intestinal → menos NH_{3} bacteriano y menor carga nitrogenada hepática.', LBLUE),
          ('(b) Neomicina', 'Antibiótico poco absorbible → menos bacterias productoras de **ureasa**.', LILAC),
          ('(c) Lactulosa', 'No se hidroliza en el intestino delgado → **fermenta en el colon** → **acidifica** el contenido.', YEL)]
    ids = [card(s, 0.4 + i * 4.2, 2.1, 4.0, 2.0, '**%s**: %s' % (t, d), f, 14, anchor='m', name='Fundamento ' + t) for i, (t, d, f) in enumerate(it)]
    col = s.group_start('Colon acidificado')
    s.shape(0.4, 4.35, 8.2, 2.25, 'roundRect', ('lin', [(0, 'F5CBA7'), (100, 'EDBB99')], 90), ('A04000', 2.0), False, adj={'adj': 30000})
    s.text(0.6, 4.4, 4, 0.35, 'LUZ DEL COLON (pH ↓)', 13, F_HEAD, '6E2C00', True, 'l')
    s.group_end()
    nh3 = [mol(s, 1.0 + i * 1.3, 5.0, 'nh4', 'NH_{3}', d=0.55, name='NH3 %d' % i) for i in range(3)]
    nh4 = [mol(s, 1.0 + i * 1.3, 5.0, 'nh4', 'NH_{4}^{+}', d=0.6, name='NH4 atrapado %d' % i) for i in range(3)]
    h = [mol(s, 1.4 + i * 1.3, 4.7, 'ca', 'H^{+}', d=0.35, name='H %d' % i) for i in range(3)]
    k = card(s, 8.9, 4.35, 4.0, 2.25, 'NH_{3} difusible + H^{+} → **NH_{4}^{+} atrapado**; además se **acelera el tránsito** y la evacuación de nitrógeno.', CREAM, 13.5)
    s.step(fade(hist))
    for g in ids:
        s.step(fade(g))
    s.step(fade(col), *[fade(n, after=(i == 0)) for i, n in enumerate(nh3)])
    s.step(*[zoom(x, after=(i > 0)) for i, x in enumerate(h)], *[out(n, after=(i == 0)) for i, n in enumerate(nh3)], *[zoom(n) for n in nh4], fade(k, after=True))
    s.note('Explicación mecanística de la consigna histórica: menos sustrato proteico intestinal significa menor producción de '
           'amonio por bacterias y menor carga nitrogenada hepática; el antibiótico poco absorbible reduce las bacterias '
           'productoras de ureasa; la lactulosa, no hidrolizada por disacaridasas humanas, llega al colon, fermenta y acidifica el '
           'contenido, favoreciendo la conversión de NH3 difusible en NH4+ atrapado, y acelera el tránsito. La animación muestra '
           'la protonación del amoníaco en la luz colónica. No debe confundirse con "neutralizar amonio en sangre".')


def p7c(D):
    s = pnew(D, 7, 'Actualización clínica: explicar no es recomendar', 'ENCEFALOPATÍA', [5, 6, 7])
    old = card(s, 0.4, 1.1, 4.0, 4.2, '**≤ 0,8 g/kg/día** de proteína\n\n**Neomicina** de rutina', 'D5D8DC', 16, head='Antes', headfill='7F8C8D', anchor='m', align='c')
    ar = s.arrow([(4.5, 3.2), (5.4, 3.2)], ACT, 6)
    new_ = card(s, 5.5, 1.1, 7.4, 4.2, '- **Proteína 1,2–1,5 g/kg/día** en pacientes con encefalopatía, individualizando y **evitando ayunos largos**: restringir puede **aumentar la sarcopenia**, empeorar la depuración **muscular** de amonio y no acortar la encefalopatía.\n- **Neomicina**: nefrotoxicidad y ototoxicidad; no es de primera elección. **Rifaximina** como adyuvante y para prevenir recurrencias.\n- **Lactulosa**: tratamiento principal de la encefalopatía manifiesta, titulada (p. ej., **2–3 deposiciones blandas/día**), evitando diarrea, deshidratación y alteraciones electrolíticas.', MINT, 13.5, head='Guías actuales (2026)', headfill=ACT)
    m = note_box(s, 0.4, 5.5, 12.5, 1.1, 'Mensaje doble: «explicar el mecanismo que fundamentaba una indicación» **no es lo mismo** que «recomendar hoy esa indicación».', 15)
    s.step(fade(old)); s.step(wipe(ar, 'l'), fade(new_, after=True)); s.step(fade(m))
    s.note('Corrección clínica imprescindible (guías actuales, por ejemplo ACG 2026 sobre encefalopatía hepática): en la cirrosis '
           'con encefalopatía no se recomienda restringir rutinariamente la proteína a ≤0,8 g/kg/día, porque puede aumentar la '
           'sarcopenia, empeorar la depuración muscular de amonio y no acortar la encefalopatía; suelen recomendarse 1,2–1,5 '
           'g/kg/día individualizando y evitando ayunos largos. La neomicina puede generar nefrotoxicidad y ototoxicidad y no es de '
           'primera elección; la rifaximina se usa como adyuvante de la lactulosa y para prevenir recurrencias. La lactulosa sigue '
           'siendo el tratamiento principal, titulada para 2–3 deposiciones blandas por día. Explicar el fundamento bioquímico no '
           'equivale a recomendarlo hoy.')


def p7d(D):
    s = pnew(D, 7, 'Esquema: restricción proteica frente a enfoque actual', 'ENCEFALOPATÍA', [7, 8])
    ids = scheme(s, ['Proteína adecuada (1,2–1,5 g/kg/d)', 'Masa muscular preservada', 'Músculo captura NH_{4}^{+} como glutamina', 'Menor carga de amonio al cerebro'],
                 ['Restricción proteica crónica', 'Sarcopenia', 'Menor captación muscular de NH_{4}^{+}', 'Más amonio · peor encefalopatía'], 1,
                 ltitle='ENFOQUE ACTUAL', rtitle='RESTRICCIÓN CRÓNICA')
    s.step(fade(ids[0])); s.step(fade(ids[1]))
    s.note('Esquema final: con aporte proteico adecuado se preserva la masa muscular, que actúa como sumidero de amonio '
           '(glutamina sintetasa); la restricción crónica genera sarcopenia y menor captura muscular de amonio. Integración: '
           'intestino (producción de NH3) → hígado (urea) → músculo (glutamina) → cerebro (astrocito).')


# ------------------------------------------------------------------ P8 hiperuricemia
def p8a(D):
    s = pnew(D, 8, 'Hiperuricemia: catabolismo de purinas', 'PURINAS', [1, 2, 3])
    c = chain(s, 0.5, 1.15, ['Nucleótidos (AMP, GMP)', 'IMP · guanosina', 'Hipoxantina · guanina', 'Xantina', 'Ácido úrico'], dy=1.0, w=3.2,
              enzymes=[None, None, '**xantina oxidorreductasa**', '**xantina oxidorreductasa**'], rev=[False] * 4,
              fill=[ENE, YEL, YEL, YEL, lighten(MOL['urate'][0], 0.5)], name='Purinas', h=0.55, size=14)
    no = card(s, 6.0, 1.1, 6.9, 2.1, 'Los humanos **carecen de uricasa** funcional (urato → alantoína): dependen de la excreción **renal** y también **intestinal**.', YEL, 15, head='Normal')
    al = card(s, 6.0, 3.4, 6.9, 1.9, 'Hiperuricemia por **sobreproducción**, **subexcreción** o **ambas**.', LSALMON, 15.5, head='Alteración', headfill=INH)
    k = card(s, 6.0, 5.5, 6.9, 1.1, 'Hiperuricemia **no equivale** automáticamente a gota.', CREAM, 14.5, grow=False)
    chain_anim(s, c, per_click=2)
    s.step(fade(no)); s.step(fade(al)); s.step(fade(k))
    s.note('Patología 8. Ruta común: nucleoproteínas/nucleótidos → bases purínicas; AMP → IMP → inosina → hipoxantina; GMP → '
           'guanosina → guanina → xantina; la xantina oxidorreductasa (deshidrogenasa/oxidasa) convierte hipoxantina → xantina → '
           'ácido úrico. Los humanos carecen de uricasa funcional y dependen de la excreción renal e intestinal. La hiperuricemia '
           'puede resultar de sobreproducción, subexcreción o ambas.')


def p8b(D):
    s = pnew(D, 8, 'Cuatro escenarios de hiperuricemia', 'PURINAS', [3, 4, 5, 6])
    it = [('(a) Alta ingesta de purinas', '↑ carga que entra a rescate/catabolismo; vísceras, ciertas carnes y mariscos difieren de lácteos y fuentes vegetales.', 'intestine', LSALMON),
          ('(b) Ejercicio extremo', 'ATP → ADP → AMP; adenilato cinasa y **AMPD** → IMP → hipoxantina → urato; **lactato** y depleción de volumen ↓ excreción. No equivale a gota crónica.', 'muscle', YEL),
          ('(c) Lisis tumoral', '↑ brusco de **K^{+}, fosfato y urato**, hipocalcemia secundaria y **lesión renal aguda**; el urato precipita en túbulos. **Urgencia**.', 'tumor', RED),
          ('(d) Insuficiencia renal', '↓ filtración y manejo tubular alterado (**URAT1**, **GLUT9**, **ABCG2**); diuréticos, volumen y lactato/cetoácidos modulan.', 'kidney', LBLUE)]
    ids = []
    for i, (t, d, k, f) in enumerate(it):
        x = 0.4 + (i % 2) * 6.4; y = 1.1 + (i // 2) * 2.8
        g = s.group_start('Escenario ' + t)
        card(s, x, y, 6.1, 2.6, d, f, 13.5, head=t, color=WHITE if f == RED else INK)
        organ_icon(s, k, x + 5.0, y + 1.55, 0.9)
        s.group_end(); ids.append(g)
    for g in ids:
        s.step(fade(g))
    s.note('a) Alta ingesta de ácidos nucleicos/purinas: si la producción supera la excreción sube el urato; no todo alimento '
           'proteico contiene igual cantidad de purinas. b) Ejercicio extremo: gran hidrólisis de ATP; adenilato cinasa y AMPD → '
           'IMP → hipoxantina → urato; lactato elevado y depleción de volumen pueden reducir la excreción renal transitoriamente. '
           'c) Células tumorales: recambio rápido, especialmente en el síndrome de lisis tumoral → aumento brusco de K+, fosfato y '
           'urato, hipocalcemia secundaria y lesión renal aguda; el urato puede precipitar en los túbulos. Es una urgencia. d) '
           'Insuficiencia renal: menor filtración y alteración del manejo tubular (URAT1/SLC22A12, GLUT9/SLC2A9, ABCG2).')


def p8c(D):
    s = pnew(D, 8, 'Puente con la fructosa, clínica y esquema', 'PURINAS', [5, 6, 7, 8])
    b = card(s, 0.4, 1.1, 4.4, 2.6, 'Grandes cargas de **fructosa** consumen ATP rápido y pueden acelerar la degradación purínica hacia urato: mecanismo **demostrado**, pero de **magnitud clínica variable**.', YEL, 13.5, head='Puente con fructosa')
    c = card(s, 0.4, 3.9, 4.4, 2.7, 'Valorar **síntomas**, **función renal**, **etiología** y contexto. En lisis tumoral: **prevención y monitorización** estrechas.', CREAM, 14, head='Clínica')
    ids = scheme(s, ['Recambio de nucleótidos', 'Xantina oxidorreductasa → urato', 'Excreción renal + intestinal', 'Uricemia estable'],
                 ['↑ producción (purinas, ejercicio, tumor, fructosa)', 'Más urato formado', '↓ excreción (riñón, lactato, volumen)', 'Hiperuricemia (no siempre gota)'], 2, x0=5.1, w=3.75)
    s.step(fade(b)); s.step(fade(c)); s.step(fade(ids[0])); s.step(fade(ids[1]))
    s.note('Puente con la fructosa: grandes cargas consumen ATP rápido y pueden acelerar la degradación purínica hacia urato; es '
           'una vía propuesta y demostrada mecanísticamente, pero la magnitud clínica varía entre individuos y dosis. Clínica: '
           'hiperuricemia no equivale automáticamente a gota; valorar síntomas, función renal, etiología y contexto. Esquema final: '
           'balance entre producción y excreción, y los puntos donde cada escenario lo altera.')


def build(D):
    div(D)
    p1a(D); p1b(D); p1c(D); p1d(D); p1e(D)
    p2a(D); p2b(D); p2c(D); p2d(D)
    p3a(D); p3b(D); p3c(D)
    p4a(D); p4b(D)
    p5a(D); p5b(D); p5c(D)
    p6a(D); p6b(D); p6c(D)
    p7a(D); p7b(D); p7c(D); p7d(D)
    p8a(D); p8b(D); p8c(D)
