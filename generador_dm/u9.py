# -*- coding: utf-8 -*-
"""UNIDAD IX — Síndrome metabólico, Mapa 7 y Secuencia F (aterogénesis, Morph)"""
from base import *

U = 9


def div(D):
    def art(s):
        s.pic('heart-front', 10.9, 0.5, 2.0, name='Corazón')
        s.pic('vascular-tunic-artery', 11.4, 3.4, h=2.6, name='Arteria')
        s.pic('ldl-1', 0.4, 1.3, 1.8, name='LDL')
        s.pic('foam-cell-1', 0.4, 4.4, 1.7, name='Célula espumosa')
    divider(D, U, 'IX', 'SÍNDROME METABÓLICO', 'Cinco criterios clínicos, un entramado fisiopatológico',
            ['Definición y criterios', 'Sistemas históricos', 'Aplicación al caso 20', 'Etiología', 'Animación integradora y Mapa 7',
             'Secuencia F: aterogénesis', 'Riñón e intervenciones'], art,
            'Unidad IX. Síndrome metabólico: definición, criterios armonizados, sistemas históricos sin mezclar umbrales, aplicación al '
            'caso 20, etiología, relación con DM2, HTA y aterosclerosis, y la secuencia molecular de la aterogénesis.')


def definition(D):
    s = new(D, U, 'Qué significa síndrome metabólico', 'pink')
    comps = [('Obesidad abdominal', 'obese-man'), ('Glucemia alterada', 'pancreas'), ('Presión arterial elevada', 'heart-front'),
             ('Triglicéridos altos', 'vldl-1'), ('HDL bajo', 'lipid-hdl-1')]
    ids = []
    for i, (t, img) in enumerate(comps):
        x = 0.4 + i * 2.53
        g = s.group_start('Componente ' + t)
        fitpic(s, img, x + 0.3, 1.2, 1.8, 1.7)
        mbox(s, x, 3.0, 2.4, 0.6, t, 'y', 13, caps=False)
        ids.append(s.group_end())
    t = tbox(s, 0.4, 3.85, 6.2, 3.0, 'Agrupación que señala **riesgo cardiometabólico elevado** y mayor probabilidad de **DM2**. [S] la reconstruye como interacción de **adiposidad visceral, ácidos grasos libres, inflamación y señal insulínica anormal**.', 14.5, head='Concepto')
    d = tbox(s, 6.85, 3.85, 6.1, 3.0, 'Útil para reconocer la **convergencia** de factores, pero existe debate sobre si predice más que evaluar **cada componente**; **no sustituye** la estimación individual del riesgo cardiovascular.', 14.5, head='Debate')
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids)])
    s.step(fade(t)); s.step(fade(d))
    s.note('El síndrome metabólico es una agrupación de obesidad abdominal/adiposidad central, glucemia alterada, presión arterial '
           'elevada, hipertrigliceridemia y HDL bajo que señala riesgo cardiometabólico elevado y mayor probabilidad de DM2. El artículo '
           '[S] reconstruye su fisiopatología como interacción de adiposidad visceral, ácidos grasos libres, inflamación y señal '
           'insulínica anormal. No sustituye la estimación individual del riesgo cardiovascular.')


def criteria(D):
    s = new(D, U, 'Criterios: definición armonizada / ATP III modificado', 'blue')
    rows = [['Criterio (≥ 3 de 5)', 'Umbral de uso frecuente'],
            ['Cintura elevada', 'Según población: ATP III clásico más de 102 cm (H) / más de 88 cm (M); IDF puede usar ≥ 90 / ≥ 80 cm en determinados grupos'],
            ['Triglicéridos', '≥ 150 mg/dL o tratamiento específico'],
            ['HDL-C bajo', '< 40 mg/dL hombres o < 50 mg/dL mujeres, o tratamiento'],
            ['Presión arterial', 'Sistólica ≥ 130 y/o diastólica ≥ 85 mmHg o tratamiento antihipertensivo'],
            ['Glucemia de ayunas', '≥ 100 mg/dL o tratamiento por hiperglucemia']]
    table(s, 0.4, 1.15, 12.55, rows, [3.0, 9.55], size=14.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Criterios SM')
    p = pearl(s, 0.4, 5.3, 12.55, 1.5, 'Diagnóstico con **al menos 3 de 5** criterios; los puntos de corte de cintura dependen de **población** y recomendaciones regionales. **Nombrar siempre la definición usada.**', 15.5)
    s.step(zoom(p))
    s.note('Definición armonizada / ATP III modificado: al menos 3 de 5 criterios. Cintura elevada según población (ATP III clásico >102 '
           'cm hombres / >88 cm mujeres; IDF puede utilizar ≥90/≥80 cm en determinados grupos); triglicéridos ≥150 mg/dL o tratamiento; '
           'HDL <40 mg/dL en hombres o <50 en mujeres, o tratamiento; presión ≥130/85 o tratamiento; glucemia de ayunas ≥100 mg/dL o '
           'tratamiento.')


def historic(D):
    s = new(D, U, 'Sistemas históricos: no mezclar umbrales', 'cyan')
    cols = [('OMS (1998)', 'Exige evidencia de **alteración glucémica / resistencia insulínica** como requisito.', 'b'),
            ('EGIR (1999)', 'Centrado en **hiperinsulinemia** (resistencia) como requisito.', 'g'),
            ('NCEP ATP III (2001)', '3 de 5 criterios; glucemia original **≥ 110 mg/dL**, luego reducida a **≥ 100**.', 'y'),
            ('IDF (2005)', '**Cintura elevada obligatoria** + 2 criterios.', 's'),
            ('ARMONIZADA (2009)', '3 de 5; la obesidad central **ya no es obligatoria**; cintura según población.', 'r')]
    ids = []
    for i, (h, t, k) in enumerate(cols):
        x = 0.4 + i * 2.53
        g = s.group_start('Sistema ' + h)
        mbox(s, x, 1.25, 2.4, 0.7, h, k, 13.5)
        tbox(s, x, 2.05, 2.4, 2.6, t, 13.5, anchor='m')
        if i < 4:
            s.arrow([(x + 2.42, 1.6), (x + 2.52, 1.6)], INK, 2.5)
        ids.append(s.group_end())
    p = pearl(s, 0.4, 4.95, 12.55, 1.9, 'Error frecuente: describir el SM con la glucemia **110** del ATP III original como si fuera el único punto actual, o combinar la cintura **obligatoria** de IDF con el esquema **3 de 5**. [S] compara los sistemas en su **Tabla 1 (p. 3)**.', 15)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Comparación histórica: el artículo [S], Tabla 1 de la página 3, contrasta OMS, EGIR, NCEP ATP III e IDF. El ATP III original usaba '
           'umbral glucémico ≥110 mg/dL; modificaciones posteriores lo redujeron a ≥100. El esquema clásico IDF requería cintura elevada '
           'más 2 criterios; en definiciones armonizadas posteriores ya no se exige obesidad central obligatoria. Los años y los '
           'requisitos de OMS y EGIR (alteración glucémica/resistencia y hiperinsulinemia) son ampliación bibliográfica resumida; los '
           'umbrales detallados de esos sistemas se omiten para no mezclarlos.')


def apply20(D):
    s = new(D, U, 'Aplicación al caso 20 (pregunta 4a)', 'green')
    items = [('Cintura 124 cm', 'SÍ', 'g'), ('TG 185 mg/dL', 'SÍ', 'g'), ('HDL 30 mg/dL', 'SÍ', 'g'), ('TA 160/100', 'SÍ', 'g'),
             ('Glucosa 145 mg/dL (ayuno no aclarado)', 'SÓLO si fue en ayunas', 'Y')]
    ids = []
    for i, (h, v, k) in enumerate(items):
        y = 1.2 + i * 0.85
        g = s.group_start('Criterio %d' % i)
        mbox(s, 0.4, y, 5.6, 0.7, h, 'w', 15, caps=False)
        s.arrow([(6.05, y + 0.35), (6.6, y + 0.35)], INK, 2.5)
        mbox(s, 6.7, y, 2.9, 0.7, v, k, 15)
        ids.append(s.group_end())
    r = mbox(s, 9.9, 1.2, 3.05, 3.95, '≥ 4 CRITERIOS DOCUMENTADOS\n→ SÍNDROME METABÓLICO', 'r', 16)
    t = tbox(s, 0.4, 5.6, 12.55, 1.25, 'Una glucemia **no identificada como de ayunas** no debe puntuarse automáticamente como criterio formal, aunque **sugiere alteración**.', 15, anchor='m')
    for g in ids:
        s.step(fade(g))
    s.step(zoom(r)); s.step(fade(t))
    s.note('Aplicación al caso 20: cintura 124 cm sí; TG 185 sí; HDL 30 sí; TA 160/100 sí; glucosa 145 sólo si fue en ayunas. El '
           'paciente reúne al menos 4 criterios claramente documentados aun sin aclarar el ayuno: tiene síndrome metabólico bajo las '
           'definiciones más utilizadas (ejercicio 11).')


def etiology(D):
    s = new(D, U, 'Etiología del síndrome metabólico (pregunta 4b)', 'peach')
    import math
    items = ['Genética y epigenética', 'Exceso de energía', 'Adiposidad visceral y ectópica', 'Actividad reducida', 'Sueño insuficiente / AOS',
             'Envejecimiento', 'Factores psicosociales', 'Adipocinas alteradas · AGNE', 'Lipotoxicidad · estrés oxidativo', 'Hiperinsulinemia y declive β']
    ids = []
    for i, t in enumerate(items):
        a = -math.pi / 2 + i * 2 * math.pi / len(items)
        x = 4.15 + 2.85 * math.cos(a) - 1.1; y = 3.95 + 2.45 * math.sin(a) - 0.3
        ids.append(mbox(s, x, y, 2.2, 0.6, t, 'y' if i % 2 == 0 else 's', 11.5, caps=False, name='Etio %d' % i))
    c = s.shape(3.1, 3.35, 2.1, 1.2, 'ellipse', 'C00000', (INK, 2), SHD, 'SÍNDROME\nMETABÓLICO', 14, F_HEAD, WHITE, True, 'c', 'm', name='Centro SM')
    t = tbox(s, 8.3, 1.2, 4.65, 5.65, '- **Multifactorial**: no existe una causa única requerida.\n- No hay una **concentración obligatoria de insulina** para diagnosticarlo.\n'
             '- La hipótesis del **«adipocito inflamatorio»** y la obesidad como **eje patogénico** [S] es un marco útil…\n- …sin negar que haya **resistencia a insulina en personas sin obesidad**.', 14.5, head='Claves')
    s.step(zoom(c)); s.step(*[fade(g, after=i > 0, dur=150) for i, g in enumerate(ids)]); s.step(fade(t))
    s.note('Etiología multifactorial: predisposición genética y epigenética; exceso de energía, adiposidad visceral y ectópica; actividad '
           'reducida, sueño insuficiente/AOS, envejecimiento y factores psicosociales; alteraciones de adipocinas, producción de AGNE, '
           'lipotoxicidad, estrés oxidativo e inflamación; hiperinsulinemia compensatoria y declive β en sujetos susceptibles. No '
           'existe una causa única requerida ni una concentración obligatoria de insulina.')


def integrative(D):
    s = new(D, U, 'Animación integradora: de la adiposidad visceral al riesgo CV', 'lime')
    chain_ = [('Adiposidad visceral disfuncional', 'y'), ('AGNE ↑ y mediadores inflamatorios', 's'), ('Resistencia insulínica', 'r'),
              ('Producción hepática de VLDL ↑', 'Y'), ('Dislipidemia: TG ↑, HDL ↓, LDL pequeñas', 'Y'), ('Disfunción endotelial', 's'), ('Riesgo cardiovascular ↑', 'r')]
    nodes = {}
    edges = []
    for i, (t, k) in enumerate(chain_):
        r_, c_ = i // 4, i % 4
        x = 0.4 + c_ * 3.17 if r_ == 0 else 0.4 + (3 - c_) * 3.17
        y = 1.3 if r_ == 0 else 3.0
        nodes['n%d' % i] = (x, y, 2.9, 0.95, t, k, 13)
        if i:
            edges.append(('n%d' % (i - 1), 'n%d' % i))
    edges[3] = ('n3', 'n4', {'pts': [(11.36, 2.28), (11.36, 2.95)]})
    order = [['n0']] + [['n%d>n%d' % (i - 1, i), 'n%d' % i] for i in range(1, 7)]
    graph(s, nodes, edges, order)
    apo = tbox(s, 0.4, 4.4, 12.55, 2.45, 'Las lipoproteínas con **ApoB** (VLDL remanentes, LDL) se **retienen en la íntima** arterial; su modificación desencadena una **respuesta inflamatoria** que inicia la placa (Secuencia F). El riesgo depende también de **LDL/ApoB, HTA y tabaquismo**.', 15, head='Puente a la aterogénesis')
    s.step(fade(apo))
    s.note('Animación integradora: adiposidad visceral disfuncional → aumento de AGNE y mediadores inflamatorios → resistencia insulínica → '
           'alteraciones de la producción hepática de VLDL → dislipidemia → disfunción endotelial → incremento del riesgo cardiovascular. '
           'Se agrega la explicación de la retención arterial de lipoproteínas con ApoB y la posterior respuesta inflamatoria, '
           'desarrollada en la Secuencia F.')


ORG7 = [('obese-man', 0.4, 1.0, 1.25, 'ADIPOSIDAD VISCERAL', 0.35, 3.35),
        ('healthy_liver', 4.6, 1.0, 2.2, 'HÍGADO', 5.0, 2.6),
        ('kidney-2', 10.9, 1.0, 1.0, 'RIÑÓN', 10.75, 2.45),
        ('vein-crossection-3d', 4.7, 4.0, 2.1, 'ENDOTELIO', 4.95, 5.75),
        ('heart-front', 11.2, 3.6, 1.4, 'CORAZÓN', 11.15, 5.6)]


def map7(D):
    stages = [
        [('a', [(1.7, 1.7), (4.55, 1.7)], 'AGNE · citocinas', TRN, None, 'dash'),
         ('b', 7.15, 1.15, 3.4, 0.6, 'RESISTENCIA INSULÍNICA ↔ hiperinsulinemia', 'r', 11.5),
         ('a', [(6.85, 2.2), (10.85, 1.6)], 'Na⁺ retenido', INK, (8.6, 1.95)),
         ('b', 7.15, 2.55, 3.4, 0.55, 'HTA (simpático, SRAA, AOS)', 's', 12)],
        [('a', [(5.7, 2.95), (5.7, 3.95)], 'VLDL · ApoB', INK),
         ('b', 0.4, 4.1, 3.9, 0.6, 'DISLIPIDEMIA: TG ↑ · HDL ↓', 'y', 12.5),
         ('a', [(4.35, 4.4), (4.7, 4.6)], '', INK),
         ('a', [(6.85, 5.0), (11.15, 4.4)], 'aterosclerosis', INH),
         ('b', 7.15, 3.4, 3.4, 0.55, 'Disfunción endotelial: NO ↓', 's', 12)],
    ]
    map_series(D, U, 'Mapa 7 · síndrome metabólico', 'blue', ORG7, stages,
               ['Mapa 7, etapa 1. La adiposidad visceral envía AGNE y citocinas al hígado y al resto del organismo: resistencia insulínica con '
                'hiperinsulinemia, que junto con la activación simpática, el SRAA y la AOS favorece la retención renal de sodio y la HTA.',
                'Mapa 7, etapa 2. El hígado produce VLDL ricas en TAG (ApoB): dislipidemia con TG altos y HDL bajo; el endotelio pierde NO y '
                'se inflama; la combinación conduce a aterosclerosis y enfermedad cardiovascular.'],
               'Mapa 7 completo: adiposidad visceral ↔ resistencia insulínica ↔ dislipidemia ↔ hipertensión ↔ disfunción endotelial. Idea '
               'fuerza: «cinco criterios clínicos, un entramado fisiopatológico común».',
               (0.4, 6.35, 12.55, 0.55, 'Adiposidad visceral ↔ RI ↔ dislipidemia ↔ HTA ↔ disfunción endotelial', 14.5),
               ['resistencia e HTA', 'lípidos, endotelio y corazón'])


def relations(D):
    s = new(D, U, 'SM → DM2, HTA y aterosclerosis (pregunta 4c)', 'cyanR')
    cols = [('→ DM2', 'Grasa visceral y hepatomuscular → resistencia → β ↑ secreción → **agotamiento relativo** → intolerancia/hiperglucemia sostenida.', 'langerhans-islet-pancreas', 'y'),
            ('→ HTA', 'Hiperactividad **simpática**, **SRAA** renal/adiposo, **retención de Na⁺**, endotelio disfuncional y **AOS**.', 'kidney-2', 's'),
            ('→ ATEROSCLEROSIS', 'VLDL/TG ↑, HDL ↓, partículas **ApoB**, inflamación, glicación, estrés oxidativo, ambiente **protrombótico (PAI-1 ↑)**.', 'heart-front', 'r')]
    ids = []
    for i, (h, t, img, k) in enumerate(cols):
        x = 0.4 + i * 4.2
        g = s.group_start('Rel ' + h)
        fitpic(s, img, x + 1.2, 1.15, 1.6, 1.5)
        mbox(s, x, 2.75, 4.0, 0.6, h, k, 16)
        tbox(s, x, 3.45, 4.0, 2.0, t, 14, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 5.7, 12.55, 1.15, 'La combinación es **más peligrosa** que abordar el peso **sin controlar LDL, tabaco y TA**.', 16)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('SM → DM2: grasa visceral y hepatomuscular → resistencia a insulina → aumento de secreción β → agotamiento relativo → '
           'hiperglucemia sostenida. SM → HTA: hiperactividad simpática, SRAA renal/adiposo, retención de sodio, endotelio disfuncional y '
           'AOS. SM → aterosclerosis: VLDL/TG altos y HDL bajo, partículas ApoB, inflamación, disfunción endotelial, glicación, estrés '
           'oxidativo y ambiente protrombótico (PAI-1).')


# ---------------------------------------------------------------- Secuencia F: aterogénesis (Morph)
FST = ['ApoB en sangre', 'Endotelio', 'Retención', 'Inflamación', 'Macrófago', 'Célula espumosa', 'Placa']


def f_scene(s, k):
    s.shape(0.4, 1.15, 8.0, 2.0, 'rect', ('lin', [(0, 'F5B7B1'), (100, 'FADBD8')], 90), (INK, 1.0), False, name='!!Luz arterial')
    lab(s, 0.5, 1.2, 3.0, 0.35, 'LUZ ARTERIAL', 12.5, align='l', name='!!Rótulo luz F')
    for i in range(7):
        rbc(s, 1.0 + i * 1.05, 1.7 + (i % 2) * 0.55, 0.5, name='!!GR F %d' % i)
    s.shape(0.4, 3.15, 8.0, 0.18, 'rect', 'C0392B' if k < 1 else 'E74C3C', (INK, 0.75), False, name='!!Endotelio F')
    s.shape(0.4, 3.33, 8.0, 1.5, 'rect', ('lin', [(0, 'FDEBD0'), (100, 'F8C471')], 90), (INK, 1.0), False, name='!!Íntima F')
    lab(s, 0.5, 4.45, 2.0, 0.32, 'ÍNTIMA', 12, align='l', name='!!Rótulo íntima F')
    s.shape(0.4, 4.83, 8.0, 1.15, 'rect', ('lin', [(0, 'F1948A'), (100, 'CD6155')], 90), (INK, 1.0), False, name='!!Media F')
    lab(s, 0.5, 5.55, 3.0, 0.32, 'MEDIA (músculo liso)', 12, align='l', name='!!Rótulo media F')
    if k >= 6:
        s.free(2.4, 2.15, 4.4, 2.6, smooth([(0, 1000), (150, 400), (500, 0), (850, 400), (1000, 1000)], True, 0.8),
               ('rad', [(0, 'F9E79F'), (100, 'D4AC0D')], (50, 60)), ('7D6608', 2), name='!!Placa F')
        s.shape(3.8, 3.2, 1.6, 0.9, 'ellipse', ('a', '7B241C', 70), None, False, 'núcleo\nnecrótico', 10, F_HEAD, WHITE, True, 'c', 'm', name='!!Núcleo necrótico')
        s.free(2.5, 2.1, 4.2, 0.45, smooth([(0, 900), (500, 0), (1000, 900)], False, 0.8), None, ('FFFFFF', 4), name='!!Cápsula fibrosa')
    g = s.group_start('!!Progreso F')
    for i, t in enumerate(FST):
        s.shape(0.4 + i * 1.79, 6.3, 1.72, 0.48, 'rect', BOX if i == k else ('FFE699' if i < k else WHITE), (INK, 1.0), False, t, 11.5, F_HEAD,
                BOXT if i == k else INK, True, 'c', 'm', (0.02, 0, 0.02, 0), minsize=8)
    s.group_end()


def ldl_tokens(s, pos):
    return [s.pic('ldl-1', x, y, 0.55, name='!!LDL %d' % i) for i, (x, y) in enumerate(pos)]


def f_panel(s, head, txt, k='y'):
    return tbox(s, 8.7, 1.15, 4.25, 4.85, txt, 14.5, head=head, hkind=k, name='!!Panel F')


def f1(D):
    s = new(D, U, 'Secuencia F · 1 · lipoproteínas con ApoB en la sangre', 'peach')
    f_scene(s, 0)
    ldl_tokens(s, [(1.6, 1.3), (3.4, 2.25), (5.2, 1.35), (6.9, 2.3)])
    s.pic('vldl-1', 4.3, 1.4, 0.7, name='!!VLDL F')
    f_panel(s, 'Partículas aterogénicas', '- **LDL**, **VLDL remanentes** e **IDL**: una molécula de **ApoB** por partícula.\n- En el SM: más partículas, **LDL pequeñas y densas**.\n- El número de partículas **ApoB** que atraviesan el endotelio condiciona el riesgo.')
    s.note('Secuencia F (Morph): lipoproteínas con ApoB → endotelio → íntima arterial → retención lipoproteica → inflamación → macrófago → '
           'célula espumosa → placa aterosclerótica. Paso 1: partículas con ApoB circulantes (LDL, VLDL remanentes). Que cada partícula '
           'lleve una ApoB y que el número de partículas condicione el riesgo es ampliación bibliográfica coherente con [material de cátedra, apartado 54].')


def f2(D):
    s = new(D, U, 'Secuencia F · 2 · atraviesan el endotelio', 'peach', morph=True)
    f_scene(s, 1)
    ldl_tokens(s, [(1.6, 3.6), (3.4, 2.25), (5.2, 3.7), (6.9, 2.3)])
    s.pic('vldl-1', 4.3, 1.4, 0.7, name='!!VLDL F')
    f_panel(s, 'Endotelio', '- Las partículas pequeñas **ingresan** a la íntima a través del endotelio.\n- La **disfunción endotelial** (NO ↓, hiperglucemia, HTA, tabaco) facilita el ingreso y la activación.', 's')
    s.note('Paso 2. Por Morph algunas partículas atraviesan el endotelio hacia la íntima. La disfunción endotelial (menor NO, hiperglucemia, '
           'HTA, tabaquismo) favorece el proceso.')


def f3(D):
    s = new(D, U, 'Secuencia F · 3 · retención en la íntima', 'peach', morph=True)
    f_scene(s, 2)
    ldl_tokens(s, [(1.6, 3.6), (2.6, 3.75), (5.2, 3.7), (6.0, 3.55)])
    pg = s.group_start('Proteoglucanos')
    for i in range(6):
        s.arrow([(1.2 + i * 1.1, 4.7), (1.5 + i * 1.1, 4.0), (1.8 + i * 1.1, 4.7)], '7D3C98', 2.0, tail=None, curve=True)
    s.group_end()
    f_panel(s, 'Retención', '- La ApoB se **une a proteoglucanos** de la matriz.\n- Las partículas quedan **retenidas** y se **modifican**: **oxidación, agregación**.\n- Retención + modificación = **disparador** de la respuesta.', 'y')
    s.step(wipe(pg, 'l'))
    s.note('Paso 3. Las lipoproteínas aterogénicas con ApoB se retienen en la íntima arterial por interacción con proteoglucanos y pueden '
           'modificarse por oxidación y agregación [material de cátedra, apartado 54].')


def f4(D):
    s = new(D, U, 'Secuencia F · 4 · activación endotelial e inflamación', 'peach', morph=True)
    f_scene(s, 3)
    ldl_tokens(s, [(1.6, 3.6), (2.6, 3.75), (5.2, 3.7), (6.0, 3.55)])
    adh = [mbox(s, 1.0 + i * 2.2, 2.75, 1.6, 0.36, 'adhesión', 's', 10.5, caps=False, name='Adhesión %d' % i) for i in range(3)]
    mono = [s.pic('macrophage', 1.5 + i * 2.5, 1.35, 0.55, name='!!Monocito %d' % i) for i in range(3)]
    f_panel(s, 'Inflamación', '- Las partículas modificadas **activan endotelio y monocitos**.\n- Moléculas de **adhesión** y quimiocinas (**MCP-1**) reclutan **monocitos**.\n- Contribuyen la hiperglucemia (AGE/RAGE) y las citocinas del adiposo.', 'r')
    s.step(*[zoom(a, after=i > 0) for i, a in enumerate(adh)])
    s.step(*[path(m, 0.2, 1.9, dur=1300, delay=i * 200) for i, m in enumerate(mono)])
    s.note('Paso 4. Las partículas modificadas activan el endotelio y los monocitos: aparecen moléculas de adhesión y quimiocinas que '
           'reclutan monocitos, que migran a la íntima (trayectorias). Las moléculas de adhesión y MCP-1 son ampliación bibliográfica.')


def f5(D):
    s = new(D, U, 'Secuencia F · 5 · el monocito se convierte en macrófago', 'peach', morph=True)
    f_scene(s, 4)
    ldl_tokens(s, [(1.9, 3.75), (2.4, 3.95), (4.6, 3.85), (5.3, 3.65)])
    for i in range(3):
        s.pic('macrophage', 1.6 + i * 2.5, 3.4, 1.05, name='!!Monocito %d' % i)
    f_panel(s, 'Macrófago', '- En la íntima el monocito se diferencia a **macrófago**.\n- **Capta** lipoproteínas modificadas (receptores scavenger) sin freno por colesterol.\n- Libera **citocinas y proteasas**.', 'g')
    s.note('Paso 5. Por Morph los monocitos crecen y se convierten en macrófagos, que captan lipoproteínas modificadas (mediante receptores '
           'scavenger, ampliación) y se cargan de colesterol, liberando citocinas y proteasas [material de cátedra, apartado 54].')


def f6(D):
    s = new(D, U, 'Secuencia F · 6 · células espumosas', 'peach', morph=True)
    f_scene(s, 5)
    for i in range(3):
        s.pic('foam-cell-1', 1.6 + i * 2.5, 3.35, 1.1, name='!!Monocito %d' % i)
    f_panel(s, 'Células espumosas', '- Macrófagos **cargados de colesterol** = células espumosas (estría grasa).\n- Su muerte forma un **núcleo necrótico**.\n- Remodelación de la pared por citocinas y proteasas.', 'y')
    s.note('Paso 6. Los macrófagos cargados de colesterol se transforman en células espumosas (Morph: cambia la ilustración); su muerte y '
           'la persistencia de lípidos originan el núcleo necrótico.')


def f7(D):
    s = new(D, U, 'Secuencia F · 7 · placa, rotura y trombosis', 'peach', morph=True)
    f_scene(s, 6)
    tr = s.group_start('Trombo')
    s.shape(4.9, 1.75, 1.3, 0.75, 'ellipse', ('rad', [(0, 'E6B0AA'), (100, '922B21')], (40, 40)), (INK, 1.25), False, 'trombo', 11, F_HEAD, WHITE, True, 'c', 'm')
    s.group_end()
    crack = s.arrow([(5.2, 2.2), (5.45, 2.55), (5.3, 2.85)], INK, 3.5, tail=None, name='Rotura')
    f_panel(s, 'Placa y evento', '- **Placa** con núcleo necrótico y cápsula fibrosa que **protruye** en la luz.\n- **Rotura o erosión** expone material **trombogénico**.\n- **Agregación plaquetaria y trombosis** → infarto, ACV, isquemia periférica.', 'r')
    s.step(wipe(crack, 't')); s.step(zoom(tr))
    s.note('Paso 7. Placa con núcleo necrótico y cápsula fibrosa. La rotura o erosión de la placa expone materiales trombogénicos, causa '
           'agregación plaquetaria y trombosis. La resistencia insulínica participa elevando partículas ricas en TAG y alterando la '
           'función endotelial, pero el riesgo clínico depende también de LDL/ApoB, HTA y el tabaquismo severo del caso 20.')


def kidney(D):
    s = new(D, U, 'El riñón une obesidad, resistencia insulínica e HTA', 'green')
    s.pic('kidney-2', 0.5, 1.2, h=3.4, name='Riñón SM')
    nodes = {
        'o': (3.4, 1.3, 2.6, 0.6, 'Obesidad', 'y', 15), 'r': (6.4, 1.3, 3.0, 0.6, 'Resistencia insulínica', 'Y', 13.5),
        'h': (9.8, 1.3, 3.15, 0.6, 'HTA', 's', 15),
        'n': (3.4, 2.55, 5.95, 0.6, 'Hiperinsulinemia y adiposidad → retención renal de Na⁺', 'w', 13),
        'p': (3.4, 3.4, 5.95, 0.6, 'Presión elevada lesiona nefronas y microvasos', 'w', 13),
        'g': (3.4, 4.25, 5.95, 0.6, 'Hiperglucemia: hiperfiltración inicial → daño glomerular', 'w', 13),
        'e': (9.8, 2.55, 3.15, 2.3, 'Enfermedad renal', 'r', 16),
    }
    edges = [('o', 'r', {'both': True}), ('r', 'h', {'both': True}), ('n', 'e', {'pts': [(9.4, 2.85), (9.75, 3.1)]}), ('p', 'e'), ('g', 'e', {'pts': [(9.4, 4.55), (9.75, 4.3)]})]
    graph(s, nodes, edges, [['o', 'o>r', 'r', 'r>h', 'h'], ['n', 'p', 'g'], ['n>e', 'p>e', 'g>e', 'e']])
    p = pearl(s, 0.4, 5.3, 12.55, 1.55, 'Medir **albuminuria y TFG** aporta mucho más que la creatinina aislada.', 17)
    s.step(zoom(p))
    s.note('Rol del riñón: la hiperinsulinemia y la adiposidad pueden favorecer la retención renal de sodio; la presión elevada lesiona '
           'nefronas y microvasos; la hiperglucemia puede generar hiperfiltración inicial y luego daño glomerular. El riñón une obesidad ↔ '
           'resistencia insulínica ↔ HTA ↔ enfermedad renal; por eso se miden albuminuria y TFG, más allá de la creatinina aislada.')


def interventions(D):
    s = new(D, U, 'Intervenciones integradas en el síndrome metabólico', 'yellow')
    items = [('runner', 'Pérdida de adiposidad y actividad física'), ('healthy-lung', 'Sueño y manejo de AOS'), ('heart-front', 'Suspender el tabaco'),
             ('small-intestine', 'Nutrición suficiente y de calidad'), ('kidney-2', 'Tratar HTA · buscar albuminuria'), ('ldl-1', 'Lípidos y glucemia con objetivos individualizados')]
    ids = []
    for i, (img, t) in enumerate(items):
        c = i % 3; r = i // 3
        x = 0.4 + c * 4.2; y = 1.2 + r * 2.15
        g = s.group_start('Int %d' % i)
        s.shape(x, y, 4.0, 1.95, 'rect', WHITE, (INK, 1.5), SHD)
        fitpic(s, img, x + 0.1, y + 0.15, 1.4, 1.65)
        s.text(x + 1.6, y + 0.1, 2.3, 1.75, t, 15, F_HEAD, BOXT, True, 'l', 'm')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 5.6, 12.55, 1.25, 'No existe una **«pastilla del síndrome metabólico»**: cada factor se trata de forma sostenida. Las propuestas farmacológicas de 2009 se contrastan con guías y regulaciones **vigentes**.', 15)
    for g in ids:
        s.step(fade(g, dur=300))
    s.step(zoom(p))
    s.note('Intervenciones integradas: pérdida de adiposidad cuando corresponde, actividad física, sueño y manejo de AOS, reducción o '
           'suspensión del tabaco, nutrición suficiente de buena calidad, tratamiento de HTA, lípidos y glucemia con objetivos '
           'individualizados, búsqueda de albuminuria y daño de órgano blanco. No existe una pastilla del síndrome metabólico.')


def build(D):
    div(D)
    definition(D)
    criteria(D)
    historic(D)
    apply20(D)
    etiology(D)
    integrative(D)
    map7(D)
    relations(D)
    f1(D)
    f2(D)
    f3(D)
    f4(D)
    f5(D)
    f6(D)
    f7(D)
    kidney(D)
    interventions(D)
