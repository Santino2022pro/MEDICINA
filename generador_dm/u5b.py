# -*- coding: utf-8 -*-
"""UNIDAD V (b) — Adipocinas, Secuencia B (Morph), lipotoxicidad, resistencia insulínica por etapas, Mapas 4 y 5"""
from base import *
from sig import *

U = 5


def adipokines1(D):
    s = new(D, U, 'Adipocinas I: leptina, adiponectina, TNF-α, IL-6, PAI-1', 'cyanR', tsize=30)
    rows = [['Mediador', 'Fuente / receptor', 'Efectos principales', 'En adiposidad disfuncional'],
            ['Leptina', 'Adipocito blanco; LEPR → JAK2–STAT3', 'Señal de reservas; modula POMC/AgRP; reproducción e inmunidad', 'Elevada, con resistencia funcional frecuente'],
            ['Adiponectina', 'Adipocito; AdipoR1/R2 → AMPK/PPARα', 'Sensibiliza a insulina; oxidación de lípidos; antiinflamatoria', 'Generalmente disminuida'],
            ['TNF-α', 'Macrófagos y otras células del tejido', 'JNK/IKK; inflamación; altera la señal de IRS', 'Aumentado en contextos inflamatorios'],
            ['IL-6', 'Adipocitos, macrófagos y músculo', 'Inflamatoria o mioquina: efecto contexto-dependiente', 'Elevación crónica frecuente'],
            ['PAI-1', 'Adiposo, endotelio, hígado', 'Menor fibrinólisis: entorno protrombótico', 'Frecuentemente aumentado']]
    table(s, 0.4, 1.15, 12.55, rows, [1.7, 3.3, 4.2, 3.35], size=13, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Adipocinas 1')
    p = pearl(s, 0.4, 5.55, 12.55, 1.3, 'La adiponectina converge en **AMPK/PPARα** (sensibilizante); la leptina informa **reservas**. La **hiperleptinemia** de la obesidad **no** asegura una supresión del apetito proporcional.', 15.5)
    s.step(zoom(p))
    s.note('Tejido adiposo como órgano endocrino [T][S]. Leptina: adipocito blanco, receptor LEPR con JAK2–STAT3; señal de reservas, '
           'modula POMC/AgRP, reproducción e inmunidad; en obesidad suele estar elevada con resistencia funcional. Adiponectina: '
           'AdipoR1/R2 con AMPK/PPARα; sensibiliza a la insulina, favorece oxidación lipídica, antiinflamatoria; generalmente '
           'disminuida. TNF-α: macrófagos; JNK/IKK, inflamación y alteración de IRS. IL-6: efecto contexto-dependiente (mioquina en '
           'el ejercicio). PAI-1: menor fibrinólisis, entorno protrombótico.')


def adipokines2(D):
    s = new(D, U, 'Adipocinas II y precisión conceptual', 'peach')
    rows = [['Mediador', 'Fuente / receptor', 'Efectos principales', 'En adiposidad disfuncional'],
            ['Resistina', 'En humanos: células inmunes (macrófagos)', 'Asociación con inflamación y metabolismo; causalidad humana compleja', 'Puede elevarse; evidencia menos directa que en roedores'],
            ['Angiotensinógeno', 'Hígado y adiposo', 'Sistema renina–angiotensina local/sistémico', 'Actividad local relacionada con adiposidad'],
            ['MCP-1/CCL2', 'Adipocitos y estroma', 'Recluta monocitos → infiltración de macrófagos', 'Puede aumentar'],
            ['FGF21', 'Principalmente hígado', 'Respuesta energética y lipídica; no es adipocina clásica', 'Variable; no atribuir al adipocito'],
            ['Omentina / visfatina', 'Estroma o depósitos específicos', 'Sensibilidad insulínica / inmunidad; evidencia variable', 'Interpretación heterogénea']]
    table(s, 0.4, 1.15, 12.55, rows, [1.9, 3.1, 4.25, 3.3], size=13, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Adipocinas 2')
    p = pearl(s, 0.4, 5.7, 12.55, 1.15, 'La **resistina** descrita en modelos animales **no puede extrapolarse linealmente** a humanos. Muchas adipocinas tienen evidencia heterogénea.', 15.5)
    s.step(zoom(p))
    s.note('Resistina: en humanos destaca su origen en células inmunes; causalidad humana compleja. Angiotensinógeno: hígado y adiposo, '
           'sistema renina–angiotensina. MCP-1/CCL2: recluta monocitos y favorece la infiltración de macrófagos. FGF21: '
           'principalmente hepático, no es adipocina clásica. Omentina, visfatina y otras: evidencia variable [T][S].')


# ---------------------------------------------------------------- Secuencia B (Morph)
CENTRAL = ['Adipocito funcional', 'Expansión', 'Hipertrofia', 'Hipoxia', 'Inflamación', 'Resistencia insulínica', 'Sistémico']


def b_progress(s, k):
    g = s.group_start('!!Progreso B')
    for i, t in enumerate(CENTRAL):
        s.shape(0.4 + i * 1.8, 6.38, 1.72, 0.5, 'rect', BOX if i == k else ('FFE699' if i < k else WHITE), (INK, 1.0), False, t, 11.5, F_HEAD,
                BOXT if i == k else INK, True, 'c', 'm', (0.02, 0, 0.02, 0), minsize=8)
        if i:
            s.arrow([(0.4 + i * 1.8 - 0.08, 6.63), (0.4 + i * 1.8 + 0.0, 6.63)], INK, 1.5)
    return s.group_end()


def b_tissue(s, k):
    """tejido: 6 adipocitos cuyo tamaño crece; capilar; macrófagos según etapa"""
    sizes = {0: 1.15, 1: 1.45, 2: 1.95, 3: 1.95, 4: 1.95}[min(k, 4)]
    pos = [(0.9, 1.4), (3.0, 1.35), (5.1, 1.45), (1.6, 3.4), (3.8, 3.45), (6.0, 3.4)]
    for i, (x, y) in enumerate(pos):
        adipocyte_white(s, x - (sizes - 1.15) / 2, y - (sizes - 1.15) / 2, sizes, name='!!Adipocito B %d' % i)
    vessel(s, 0.4, 5.55, 7.6, 0.45, rbcs=7, name='!!Capilar B')
    if k >= 4:
        for i, (x, y) in enumerate([(2.35, 2.55), (4.45, 2.6), (6.65, 2.55), (3.05, 4.5)]):
            s.pic('macrophage', x, y, 0.75, name='!!Macrófago B %d' % i)


def b_panel(s, head, txt, kind='y'):
    return tbox(s, 8.55, 1.15, 4.4, 5.0, txt, 14.5, head=head, hkind=kind, name='!!Panel B')


def seqB0(D):
    s = new(D, U, 'Secuencia B · 1 · tejido adiposo funcional', 'lime' if False else 'green')
    b_tissue(s, 0)
    b_progress(s, 0)
    b_panel(s, 'Funcional', '- Adipocitos de tamaño moderado.\n- **Capilares** suficientes: buena oxigenación.\n- Insulina **frena la lipólisis**; adiponectina adecuada.\n- Macrófagos residentes de **remodelación**.', 'g')
    s.note('Secuencia B (Morph) y animación central: adipocito funcional → expansión del depósito → hipertrofia patológica → hipoxia '
           'local → inflamación → resistencia insulínica → alteraciones sistémicas. Punto de partida: tejido funcional, con adipocitos '
           'de tamaño moderado y capilares suficientes.')


def seqB1(D):
    s = new(D, U, 'Secuencia B · 2 · expansión del depósito', 'green', morph=True)
    b_tissue(s, 1)
    b_progress(s, 1)
    b_panel(s, 'Expansión', '- Balance energético **positivo sostenido**: más TAG por célula.\n- Si hay **reclutamiento** (hiperplasia) y **angiogénesis**, la expansión puede ser relativamente segura.\n- La capacidad de expansión varía entre personas y depósitos.', 'g')
    s.note('Paso 2. Con balance energético positivo sostenido los adipocitos almacenan más TAG (Morph: crecen). Si el tejido recluta '
           'adipocitos nuevos y forma vasos, la expansión puede ser relativamente saludable.')


def seqB2(D):
    s = new(D, U, 'Secuencia B · 3 · hipertrofia patológica e hipoxia', 'green', morph=True)
    b_tissue(s, 3)
    b_progress(s, 3)
    hyp = [s.shape(x, y, 0.55, 0.55, 'ellipse', ('a', '5DADE2', 30), ('1F618D', 1.5, 'dash'), False, 'O₂↓', 10, F_HEAD, '1F618D', True, 'c', 'm', (0, 0, 0, 0), fit=False,
                   name='Hipoxia %d' % i) for i, (x, y) in enumerate([(2.55, 2.75), (4.75, 2.8), (3.3, 4.75)])]
    fib = s.group_start('Fibrosis')
    for i in range(5):
        s.arrow([(0.6 + i * 1.5, 3.2), (1.3 + i * 1.5, 3.05), (1.9 + i * 1.5, 3.25)], '8E44AD', 2.0, tail=None, curve=True)
    s.group_end()
    b_panel(s, 'Hipertrofia e hipoxia', '- Adipocitos **muy grandes**: mayor distancia al capilar → **hipoxia** regional.\n- Estrés del **RE**, **fibrosis** de la matriz (rígida).\n- Muerte de adipocitos dañados.', 's')
    s.step(*[zoom(h, after=i > 0) for i, h in enumerate(hyp)])
    s.step(wipe(fib, 'l'))
    s.note('Paso 3. Por Morph los adipocitos alcanzan un tamaño excesivo: aumenta la distancia al capilar y aparece hipoxia regional '
           '(fichas O₂↓), estrés del retículo endoplásmico y fibrosis de la matriz extracelular (trazos violetas). La señalización '
           'por HIF ante hipoxia es ampliación bibliográfica.')


def seqB3(D):
    s = new(D, U, 'Secuencia B · 4 · infiltración macrofágica', 'green', morph=True)
    b_tissue(s, 4)
    b_progress(s, 4)
    mcp = [mbox(s, 0.6 + i * 2.3, 5.05, 1.2, 0.42, 'MCP-1', 's', 12, caps=False, name='MCP %d' % i) for i in range(3)]
    crown = s.shape(4.15, 2.45, 2.4, 2.4, 'ellipse', None, ('C00000', 3.5, 'dash'), False, name='Estructura en corona')
    b_panel(s, 'Metainflamación', '- **MCP-1/CCL2** recluta monocitos → **macrófagos**.\n- **Estructuras en corona** alrededor de adipocitos dañados.\n- ROS, fibrosis, señales de estrés.\n- M1/M2 es una **simplificación** de un continuo; no todo macrófago es perjudicial.', 's')
    s.step(*[zoom(m, after=i > 0) for i, m in enumerate(mcp)])
    s.step(zoom(crown))
    s.note('Paso 4. En la expansión disfuncional cambia el ambiente inmunitario: MCP-1 recluta monocitos que se diferencian en '
           'macrófagos (Morph: aparecen las ilustraciones) y forman agregados alrededor de adipocitos dañados, las «estructuras en '
           'corona» (círculo rojo). Aumentan las señales de estrés, la fibrosis y las ROS. No todo macrófago es perjudicial: el tejido '
           'normal contiene células inmunitarias de remodelación; los estados M1/M2 son simplificaciones de un continuo [S].')


def seqB4(D):
    s = new(D, U, 'Secuencia B · 5 · mediadores que salen del tejido', 'green', morph=True)
    b_tissue(s, 4)
    b_progress(s, 5)
    meds = [('TNF-α', 's'), ('IL-6', 's'), ('AGNE ↑', 'y'), ('Adiponectina ↓', 'g'), ('Leptina ↑ (resistencia)', 'w')]
    pos = [(0.5, 2.55), (2.7, 4.55), (4.9, 2.6), (0.6, 4.6), (5.4, 4.65)]
    ids = []
    for i, (t, k) in enumerate(meds):
        ids.append(mbox(s, pos[i][0], pos[i][1], 2.25, 0.5, t, k, 13, caps=False, name='Mediador %d' % i))
    s.anim = []
    b_panel(s, 'Señales sistémicas', '- Citocinas **TNF-α, IL-6** · **AGNE** por lipólisis inapropiada.\n- **Adiponectina ↓** (pierde acción sensibilizante).\n- Hacia **hígado, músculo, páncreas, endotelio y SNC**.', 'r')
    for i, m in enumerate(ids):
        s.step(zoom(m), path(m, 6.0 - pos[i][0], 0.2 - pos[i][1] + 1.0 + i * 0.75, dur=1300, delay=200))
    s.note('Paso 5. El tejido inflamado libera TNF-α e IL-6, aumenta la salida de AGNE por lipólisis inapropiada (la insulina ya no '
           'la frena bien), disminuye la adiponectina y mantiene la leptina alta con resistencia funcional. Las fichas viajan fuera '
           'del tejido hacia los órganos blanco: hígado, músculo, páncreas, endotelio y SNC.')


def seqB5(D):
    s = new(D, U, 'Secuencia B · 6 · el receptor recibe la interferencia', 'peach')
    ids = sig_scene(s, 5, impaired=True)
    s.anim = []
    kin = [mbox(s, 3.0 + i * 1.25, 4.55, 1.15, 0.45, t, 's', 12.5, caps=False, name='Cinasa %s' % t) for i, t in enumerate(['JNK', 'IKKβ', 'PKC'])]
    socs = mbox(s, 3.0, 5.2, 1.6, 0.45, 'SOCS', 'w', 12.5, caps=False, name='SOCS')
    sig_panel(s, '!', 'Desacople de la señal', '- **JNK, IKKβ y PKC** fosforilan IRS en **serina/treonina** (S roja).\n- **SOCS** favorece la degradación de IRS.\n'
              '- La fosforilación en tirosina queda **funcionalmente desacoplada**: Akt y AS160 poco activos.\n- **Menos vesículas GLUT4** llegan a la membrana.')
    sig_progress(s, [], labels=('Insulina', 'RTK-P', 'IRS-Ser', 'PI3K ↓', 'Akt ↓', 'GLUT4 ↓', 'Glc ↓'))
    s.step(*[zoom(k, after=i > 0) for i, k in enumerate(kin)])
    s.step(pulse(ids['irsp']), fade(socs, after=True))
    s.step(pulse(ids['akt']), pulse(ids['as'], after=True))
    s.note('Paso 6 (final de la secuencia B): mediador inflamatorio → receptor de insulina → alteración de IRS/Akt. El exceso de AGNE, '
           'lípidos ectópicos y citocinas activa JNK, IKKβ/NF-κB y PKC, que fosforilan IRS en serina/treonina (ficha S roja), además '
           'de mecanismos de degradación de IRS por SOCS. La fosforilación fisiológica en tirosina queda funcionalmente desacoplada de '
           'la respuesta metabólica: Akt y AS160 permanecen poco activos y llegan menos vesículas con GLUT4 a la membrana. La '
           'inflamación es causa y consecuencia de las alteraciones del adipocito: retroalimentación, no proceso unidireccional [S].')


def lipotox(D):
    s = new(D, U, 'Lipotoxicidad: DAG, ceramidas, PKC, JNK e IKK', 'cyan')
    nodes = {
        'ex': (0.4, 1.25, 1.85, 0.62, 'Excedente energético crónico', 's', 12),
        'sat': (2.45, 1.25, 1.85, 0.62, 'Capacidad adiposa saturada', 'Y', 12),
        'ag': (4.5, 1.25, 1.85, 0.62, 'Lipólisis inapropiada: AGNE ↑', 'Y', 12),
        'ect': (6.55, 1.25, 1.75, 0.62, 'Hígado · músculo · páncreas', 'w', 12),
        'dag': (0.4, 2.35, 1.85, 0.55, 'DAG', 'y', 16),
        'cer': (2.45, 2.35, 1.85, 0.55, 'Ceramidas', 'y', 14),
        'er': (4.5, 2.35, 1.85, 0.55, 'Estrés del RE', 'g', 13),
        'jnk': (6.55, 2.35, 1.75, 0.55, 'JNK · IKKβ/NF-κB', 'g', 11.5),
        'pkc': (0.4, 3.3, 3.9, 0.6, 'PKCθ / PKCε → IRS-Ser/Thr-P', 'r', 13),
        'akt': (4.5, 3.3, 3.8, 0.6, 'PP2A / PKCζ → Akt ↓', 'r', 13),
        'o': (0.4, 4.25, 7.9, 0.6, 'MENOR SEÑAL DE INSULINA', 'y', 15),
    }
    edges = [('ex', 'sat'), ('sat', 'ag'), ('ag', 'ect'), ('ect', 'dag', {'pts': [(7.0, 1.9), (1.3, 2.32)]}), ('ect', 'cer', {'pts': [(7.2, 1.9), (3.4, 2.32)]}),
             ('ect', 'er', {'pts': [(7.3, 1.9), (5.4, 2.32)]}), ('ect', 'jnk'), ('dag', 'pkc', {'pts': [(1.3, 2.93), (1.3, 3.27)]}),
             ('jnk', 'pkc', {'pts': [(6.9, 2.93), (3.6, 3.27)]}), ('cer', 'akt', {'pts': [(3.4, 2.93), (5.3, 3.27)]}), ('er', 'akt', {'pts': [(5.9, 2.93), (6.4, 3.27)]}),
             ('pkc', 'o'), ('akt', 'o')]
    graph(s, nodes, edges, [['ex', 'ex>sat', 'sat', 'sat>ag', 'ag', 'ag>ect', 'ect'], ['ect>dag', 'dag', 'ect>cer', 'cer', 'ect>er', 'er', 'ect>jnk', 'jnk'],
                            ['dag>pkc', 'jnk>pkc', 'pkc', 'cer>akt', 'er>akt', 'akt'], ['pkc>o', 'akt>o', 'o']])
    org = s.group_start('Órganos lipotoxicidad')
    for i, (img, h, t) in enumerate([('muscle-fiber', 'Músculo', 'Captación de glucosa y glucógeno ↓; disfunción mitocondrial relativa'),
                                      ('healthy_liver', 'Hígado', 'Gluconeogénesis mal suprimida + lipogénesis/VLDL: esteatosis'),
                                      ('langerhans-islet-pancreas', 'Páncreas', 'Gluco/lipotoxicidad, estrés del RE, inflamación de islotes'),
                                      ('vein-crossection-3d', 'Endotelio', 'NO ↓, vasoconstricción, inflamación, aterosclerosis')]):
        y = 1.2 + i * 1.18
        s.shape(8.6, y, 4.35, 1.08, 'rect', WHITE, (INK, 1.25), SHD)
        fitpic(s, img, 8.68, y + 0.08, 0.95, 0.9)
        s.text(9.75, y + 0.05, 3.1, 0.35, h, 14, F_HEAD, BOXT, True, 'l', 'm')
        s.text(9.75, y + 0.42, 3.1, 0.62, t, 11.5, F_BODY, INK, False, 'l', 't')
    s.group_end()
    p = pearl(s, 0.4, 5.15, 7.9, 1.7, 'El TAG en una gota relativamente **inerte** puede ser **protector** frente a intermediarios lipídicos más señalizadores: «la grasa es tóxica» es impreciso; importan **localización, especies lipídicas, capacidad oxidativa e inflamación**.', 14.5)
    s.step(fade(org)); s.step(zoom(p))
    s.note('Secuencia completa de la lipotoxicidad: excedente energético crónico y predisposición → saturación relativa de la capacidad '
           'adiposa → lipólisis inapropiadamente elevada y mayor salida de AGNE → captación por hígado, músculo y páncreas → aumento '
           'de intermediarios lipídicos (ciertas especies de DAG y ceramidas) → activación de PKC específicas, estrés del retículo, '
           'inflamación y alteración de Akt/IRS → menor señal de insulina. Las isoformas PKCθ (músculo) y PKCε (hígado) y la vía '
           'ceramidas → PP2A/PKCζ son ampliación bibliográfica. Músculo: menos captación y glucógeno. Hígado: la insulina deja de '
           'suprimir la gluconeogénesis mientras la lipogénesis puede seguir alta (resistencia selectiva, VLDL, esteatosis). '
           'Páncreas: glucotoxicidad, lipotoxicidad, estrés del RE e inflamación de islotes. Endotelio: menor NO, más '
           'vasoconstricción e inflamación. El TAG almacenado en una gota relativamente inerte puede ser protector.')


def selective(D):
    s = new(D, U, 'Resistencia hepática selectiva', 'blue')
    s.pic('healthy_liver', 0.4, 1.3, 3.6, name='Hígado selectivo')
    l = s.group_start('Rama glucosa')
    mbox(s, 4.4, 1.25, 4.15, 0.6, 'RAMA FOXO1 (glucosa): RESISTENTE', 'r', 13.5)
    tbox(s, 4.4, 1.92, 4.15, 1.6, 'La insulina **no suprime** bien PEPCK/G6Pasa → **producción hepática de glucosa** inapropiada → hiperglucemia en ayunas.', 14)
    s.group_end()
    r = s.group_start('Rama lípidos')
    mbox(s, 8.8, 1.25, 4.15, 0.6, 'RAMA SREBP-1c (lípidos): ACTIVA', 'y', 13.5)
    tbox(s, 8.8, 1.92, 4.15, 1.6, 'La **lipogénesis** sigue estimulada (hiperinsulinemia, sustratos) → **VLDL ↑** y **esteatosis**.', 14)
    s.group_end()
    o = pearl(s, 4.4, 3.8, 8.55, 1.15, 'Lo peor de dos mundos: **hiperglucemia + hipertrigliceridemia** con hiperinsulinemia compensatoria.', 15.5)
    t = tbox(s, 0.4, 5.25, 12.55, 1.6, 'Explica por qué en la DM2 y el síndrome metabólico coexisten **producción de glucosa alta** y **producción de VLDL alta**, y por qué el hígado graso es frecuente.', 15, head='Conexión clínica')
    s.step(fade(l)); s.step(fade(r)); s.step(zoom(o)); s.step(fade(t))
    s.note('Alteración de la supresión de la producción hepática de glucosa (paso 11 de la cadena de resistencia). En el hígado '
           'resistente la insulina deja de suprimir adecuadamente la gluconeogénesis mientras los flujos de sustratos y la '
           'lipogénesis pueden seguir elevados: resistencia selectiva, producción de VLDL y esteatosis [material de cátedra, apartado 26]. La '
           'separación en «ramas FOXO1 y SREBP-1c» es la interpretación molecular habitual (ampliación bibliográfica).')


ORG4 = [('langerhans-islet-pancreas', 5.35, 1.0, 1.75, 'ISLOTE β', 5.6, 2.85),
        ('healthy_liver', 0.4, 3.3, 2.4, 'HÍGADO', 0.85, 5.05),
        ('muscle-fiber', 10.4, 3.4, 2.5, 'MÚSCULO', 10.9, 4.65),
        ('adipocyte-1', 10.8, 1.0, 1.7, 'ADIPOSO', 10.95, 2.75),
        ('diabetic-retinopathy-eye', 5.4, 4.2, 1.4, 'ÓRGANOS BLANCO', 5.0, 5.45)]


def map4(D):
    stages = [
        [('t', 2.95, 1.1, 2.15, 1.5, '**Resistencia** en hígado, músculo y adiposo', 12.5),
         ('a', [(10.75, 1.8), (7.2, 1.8)], 'AGNE · citocinas', TRN, None, 'dash'),
         ('b', 7.45, 2.35, 2.7, 0.55, 'HIPERINSULINEMIA compensadora', 'y', 11.5),
         ('a', [(7.2, 2.6), (10.35, 3.75)], '', ACT), ('a', [(5.3, 2.4), (2.85, 3.6)], '', ACT)],
        [('b', 2.95, 2.75, 2.15, 0.85, 'Gluco/lipotoxicidad · estrés RE', 's', 11.5),
         ('b', 7.45, 3.1, 2.7, 0.6, 'Disfunción β progresiva', 'r', 12.5),
         ('t', 2.95, 3.85, 2.25, 1.25, 'Glucemia ↑ sostenida (PHG ↑, captación ↓)', 12),
         ('a', [(5.22, 4.45), (5.5, 4.7)], '', INK),
         ('t', 7.2, 4.35, 3.0, 1.05, 'Micro y macroangiopatía', 12.5)],
    ]
    map_series(D, U, 'Mapa 4 · diabetes tipo 2', 'peach', ORG4, stages,
               ['Mapa 4, etapa 1. La resistencia insulínica en hígado, músculo y tejido adiposo (alimentada por AGNE y citocinas) obliga a '
                'la célula β a secretar más: la hiperinsulinemia compensadora mantiene durante años una glucemia casi normal.',
                'Mapa 4, etapa 2. La glucotoxicidad, la lipotoxicidad, el estrés del RE y factores genéticos producen disfunción β '
                'progresiva: la compensación fracasa y aparece la hiperglucemia sostenida, que daña microvasos y macrovasos.'],
               'Mapa 4 completo: resistencia insulínica → compensación pancreática → disfunción β progresiva → hiperglucemia sostenida y '
               'daño orgánico. Corresponde a los pasos 12 a 14 de la cadena: compensación de células β, hiperinsulinemia y fracaso '
               'secretor progresivo, manifestaciones clínicas.',
               (0.4, 6.15, 12.55, 0.7, 'Resistencia → **compensación β** → **fracaso secretor** → hiperglucemia sostenida → **daño orgánico**.', 14.5),
               ['resistencia y compensación', 'fracaso β y daño'])


ORG5 = [('adipocyte-1', 0.4, 1.05, 2.1, 'ADIPOSO VISCERAL', 0.4, 3.15),
        ('healthy_liver', 4.6, 1.05, 2.4, 'HÍGADO', 5.05, 2.8),
        ('muscle-fiber', 9.9, 1.15, 2.6, 'MÚSCULO', 10.4, 2.45),
        ('langerhans-islet-pancreas', 9.95, 3.3, 1.5, 'PÁNCREAS', 11.55, 3.9),
        ('heart-front', 4.9, 3.75, 1.4, 'CORAZÓN · VASOS', 6.4, 4.4)]


def map5(D):
    stages = [
        [('b', 0.4, 3.75, 2.9, 0.55, 'Hipertrofia · hipoxia · macrófagos', 's', 11.5),
         ('a', [(2.55, 1.6), (4.55, 1.6)], 'AGNE (porta) · TNF-α · IL-6', TRN, (2.3, 1.15), 'dash'),
         ('a', [(2.5, 2.3), (9.85, 1.9)], 'AGNE · citocinas', TRN, (6.6, 2.35), 'dash'),
         ('a', [(2.3, 3.05), (9.9, 3.9)], 'lípidos ectópicos', TRN, (6.95, 3.35), 'dash')],
        [('t', 7.15, 1.0, 2.6, 1.05, '**Hígado**: PHG ↑, VLDL ↑, esteatosis', 12),
         ('t', 10.0, 4.85, 2.9, 1.0, '**β**: secreción ↓ progresiva', 12),
         ('t', 0.4, 4.45, 4.2, 1.15, '**Músculo**: captación de glucosa ↓ (DAG/PKC)', 12),
         ('a', [(6.0, 2.85), (5.7, 3.7)], 'VLDL · ApoB', INK),
         ('t', 4.75, 5.25, 4.9, 0.85, '**Endotelio**: NO ↓, inflamación, PAI-1 ↑ → aterosclerosis', 12)],
    ]
    map_series(D, U, 'Mapa 5 · obesidad disfuncional', 'yellow', ORG5, stages,
               ['Mapa 5, etapa 1. El adipocito visceral hipertrofiado, hipóxico e infiltrado por macrófagos libera AGNE (en parte por la '
                'vena porta), citocinas y lípidos que se depositan en órganos no diseñados para almacenarlos.',
                'Mapa 5, etapa 2. Consecuencias: el hígado produce glucosa y VLDL en exceso y acumula grasa; el músculo capta menos '
                'glucosa; la célula β pierde capacidad secretora; el endotelio pierde NO, se inflama y el ambiente se vuelve '
                'protrombótico.'],
               'Mapa 5 completo: adipocito hipertrofiado → inflamación y lípidos ectópicos → resistencia insulínica → alteraciones '
               'hepáticas, cardiovasculares y pancreáticas. Idea fuerza: «del adipocito sano al disfuncional: almacenar TAG protege; '
               'desbordar la capacidad libera AGNE, DAG, ceramidas e inflamación que deterioran hígado, músculo y páncreas».',
               (0.4, 6.3, 12.55, 0.6, 'Almacenar TAG **protege**; desbordar la capacidad libera **AGNE, DAG, ceramidas e inflamación**.', 14),
               ['señales que salen del adiposo', 'daño en órganos'])


def integration(D):
    s = new(D, U, 'Integración adipocito–hígado–riñón–músculo–SNC', 'cyanR')
    cols = [('DESPUÉS DE COMER', 'Incretinas y glucosa → insulina: suprime PHG, ↑ captación muscular, almacenamiento adiposo, lipólisis ↓.', 'g'),
            ('AYUNO', 'Insulina ↓, glucagón/insulina ↑: hígado sostiene la glucemia; adipocito libera AGNE y glicerol; músculo oxida lípidos.', 'Y'),
            ('OBESIDAD VISCERAL', 'Adiposo inflexible; hígado acumula lípidos y produce glucosa/VLDL; músculo capta menos; riñón reabsorbe hasta saturarse; SNC menos sensible a leptina/insulina.', 's'),
            ('DM1 SIN INSULINA', 'Las adaptaciones del ayuno se exacerban patológicamente hasta la **CAD**.', 'r')]
    ids = []
    for i, (h, t, k) in enumerate(cols):
        y = 1.2 + i * 1.32
        g = s.group_start('Estado ' + h)
        mbox(s, 0.4, y, 3.3, 1.15, h, k, 15)
        tbox(s, 3.85, y, 9.1, 1.15, t, 14.5, anchor='m')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Integración metabólica adipocito–hígado–riñón–músculo–SNC (apartado 27). Después de comer: el intestino absorbe '
           'carbohidratos y grasas, incretinas y glucosa estimulan la célula β y la insulina suprime la producción hepática de '
           'glucosa, aumenta la captación muscular, facilita el almacenamiento adiposo y limita la lipólisis. En ayuno: disminuye la '
           'insulina y el hígado sostiene la glucosa plasmática mientras el adipocito libera AGNE y glicerol. En la obesidad visceral: '
           'el tejido adiposo pierde flexibilidad, el hígado acumula lípidos y produce glucosa/VLDL, el músculo capta menos glucosa, '
           'el riñón mantiene la reabsorción de glucosa hasta saturarse y el SNC puede ser menos sensible a leptina e insulina. En la '
           'DM1 sin insulina estas adaptaciones de ayuno se exacerban hasta la CAD.')


def build(D):
    adipokines1(D)
    adipokines2(D)
    seqB0(D)
    seqB1(D)
    seqB2(D)
    seqB3(D)
    seqB4(D)
    seqB5(D)
    lipotox(D)
    selective(D)
    map4(D)
    map5(D)
    integration(D)
