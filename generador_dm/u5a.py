# -*- coding: utf-8 -*-
"""UNIDAD V (a) — Tejido adiposo: histología, tipos, termogénesis, adipogénesis, captación, esterificación, lipogénesis y lipólisis"""
from base import *

U = 5


def div(D):
    def art(s):
        s.pic('adipocyte-1', 10.5, 0.5, 2.6, name='Adipocitos')
        s.pic('fat-tissue', 10.8, 3.6, 2.0, name='Tejido adiposo')
        model(s, 'tag', 0.15, 1.0, 2.5, hs=False, name='TAG 3D', label='Triacilglicerol')
        model(s, 'glicerol', 0.5, 4.6, 1.6, name='Glicerol 3D', label='Glicerol')
    divider(D, U, 'V', 'TEJIDO ADIPOSO', 'Histología, señalización y metabolismo de un órgano endocrino',
            ['Órgano endocrino y expansibilidad', 'Subcutáneo, visceral y ectópico', 'Blanco, pardo, beige · UCP1', 'Adipogénesis: PPARγ y C/EBP',
             'LPL, captación y esterificación', 'Lipogénesis de novo', 'Lipólisis: ATGL → HSL → MGL', 'Adipocinas e inflamación',
             'Secuencia B y lipotoxicidad', 'Mapas 4 y 5'], art,
            'Unidad V. El tejido adiposo es un órgano difuso, vascularizado, inervado y metabólicamente activo. Se recorren su '
            'histología, la termogénesis, la adipogénesis, el almacenamiento y la movilización de triglicéridos, las adipocinas y el '
            'nexo molecular entre expansión disfuncional, lipotoxicidad, inflamación y resistencia insulínica.')


def organ(D):
    s = new(D, U, 'El tejido adiposo no es un depósito pasivo', 'green')
    s.pic('fat-tissue', 0.4, 1.2, 3.2, name='Tejido adiposo histología')
    cells = [('Adipocitos', 'adipocyte-1'), ('Preadipocitos y células madre estromales', None), ('Fibroblastos · matriz extracelular', None),
             ('Endotelio (muy vascularizado)', 'capillary'), ('Macrófagos y linfocitos', 'macrophage'), ('Inervación simpática', 'Pyramidal_Neuron')]
    ids = []
    for i, (t, img) in enumerate(cells):
        y = 1.2 + i * 0.72
        g = s.group_start('Componente %d' % i)
        if img:
            fitpic(s, img, 3.95, y, 0.75, 0.62)
        else:
            sphere(s, 4.1, y + 0.05, 0.5, 'C39BD3')
        mbox(s, 4.85, y + 0.04, 3.4, 0.56, t, 'g', 12.5, caps=False)
        ids.append(s.group_end())
    fn = tbox(s, 8.55, 1.2, 4.4, 4.25, '- **Reserva energética** (TAG)\n- **Aislamiento térmico**\n- **Amortiguación mecánica**\n- **Regulación del flujo de ácidos grasos**\n'
              '- Señalización **endocrina, paracrina y autocrina** (adipocinas)', 15.5, head='Funciones')
    p = pearl(s, 0.4, 5.65, 12.55, 1.2, 'No todo tejido adiposo tiene el mismo riesgo metabólico: importan **localización, capacidad de expansión, especies lipídicas y estado inflamatorio**.', 15.5)
    s.step(*[fade(g, after=i > 0, dur=250) for i, g in enumerate(ids)])
    s.step(fade(fn)); s.step(zoom(p))
    s.note('El tejido adiposo es un órgano difuso altamente vascularizado, inervado y metabólicamente activo, con adipocitos, '
           'preadipocitos, células madre estromales, fibroblastos, endotelio, macrófagos, linfocitos y matriz extracelular. Aporta '
           'reserva energética, aislamiento térmico, amortiguación mecánica, regulación de ácidos grasos y señalización endocrina, '
           'paracrina y autocrina [T]. La figura 2 de la página 3 de [T] contrasta la localización subcutánea y visceral; la figura '
           '1 de la página 5 de [S] representa cómo ácidos grasos, inflamación y resistencia insulínica se potencian.')


def expansion(D):
    s = new(D, U, 'Expansibilidad: expansión saludable frente a disfuncional', 'peach')
    l = s.group_start('Saludable')
    mbox(s, 0.4, 1.2, 6.0, 0.6, 'EXPANSIÓN RELATIVAMENTE SALUDABLE', 'g', 15)
    for i, (x, y, d) in enumerate([(0.7, 2.0, 1.0), (1.8, 2.1, 1.05), (2.95, 2.0, 1.0), (4.05, 2.1, 1.0), (5.1, 2.0, 1.0), (1.2, 3.1, 1.0), (2.35, 3.15, 1.05), (3.5, 3.1, 1.0), (4.6, 3.15, 1.05)]):
        adipocyte_white(s, x, y, d, name='Adipocito sano %d' % i)
    vessel(s, 0.6, 4.25, 5.6, 0.35, rbcs=6, name='Capilar sano')
    tbox(s, 0.4, 4.8, 6.0, 2.05, '- Hipertrofia **moderada** + reclutamiento de adipocitos nuevos (**hiperplasia**)\n- **Angiogénesis** apropiada · matriz **flexible**\n- TAG almacenados con seguridad', 14.5)
    s.group_end()
    r = s.group_start('Disfuncional')
    mbox(s, 6.95, 1.2, 6.0, 0.6, 'EXPANSIÓN DISFUNCIONAL', 'r', 15)
    for i, (x, y, d) in enumerate([(7.1, 1.95, 1.9), (9.05, 1.95, 2.0), (11.1, 2.0, 1.75)]):
        adipocyte_white(s, x, y, d, name='Adipocito grande %d' % i)
    s.pic('macrophage', 10.6, 3.2, 0.9, name='Macrófago disf')
    tbox(s, 6.95, 4.8, 6.0, 2.05, '- Adipocitos **muy hipertrofiados** · **hipoxia** regional · **fibrosis**\n- Estrés del **RE** · **inflamación**\n- **Derrame de lípidos** a hígado, músculo, páncreas y corazón', 14.5)
    s.group_end()
    s.step(fade(l)); s.step(fade(r))
    s.note('Concepto de expansibilidad. Un tejido adiposo sano aumenta su capacidad mediante hipertrofia moderada y reclutamiento de '
           'adipocitos nuevos (hiperplasia), angiogénesis apropiada y matriz flexible. Si supera su capacidad de expansión aparecen '
           'adipocitos muy hipertrofiados, hipoxia regional, fibrosis, estrés del retículo endoplásmico, inflamación y derrame de '
           'lípidos a órganos no diseñados para almacenarlos. Esto ayuda a explicar por qué personas con IMC similar pueden tener '
           'riesgo metabólico distinto: no todo aumento de tejido adiposo implica idéntico riesgo.')


def depots(D):
    s = new(D, U, 'Subcutáneo, visceral y ectópico', 'yellow')
    s.pic('obese-man', 0.5, 1.15, h=5.75, name='Cuerpo depósitos')
    sc = s.shape(0.9, 3.1, 2.4, 2.2, 'ellipse', None, ('F39C12', 5, 'dash'), False, name='Marca subcutánea')
    vi = s.shape(1.45, 3.45, 1.3, 1.2, 'ellipse', ('a', 'C00000', 45), ('C00000', 2), False, name='Marca visceral')
    a = s.group_start('Subcutáneo')
    mbox(s, 4.1, 1.2, 4.3, 0.55, 'SUBCUTÁNEO', 'Y', 15)
    tbox(s, 4.1, 1.82, 4.3, 1.9, 'Bajo la piel, abdominal o **glúteo-femoral**. Protección, aislamiento, almacenamiento **relativamente seguro**; el glúteo-femoral se asocia con **menor riesgo** para igual adiposidad global.', 13.5)
    s.group_end()
    b = s.group_start('Visceral')
    mbox(s, 8.65, 1.2, 4.3, 0.55, 'VISCERAL', 'r', 15)
    tbox(s, 8.65, 1.82, 4.3, 1.9, 'Omental/mesentérico. **Mayor actividad lipolítica e inflamatoria**; parte drena al **hígado por la porta**: resistencia hepática, dislipidemia aterogénica, ECV.', 13.5)
    s.group_end()
    port = s.group_start('Porta')
    s.pic('healthy_liver', 4.3, 4.0, 2.2, name='Hígado porta')
    s.arrow([(2.8, 4.0), (4.3, 4.5)], TRN, 4, dash='dash')
    lab(s, 2.75, 3.55, 1.7, 0.35, 'AGNE · citocinas por porta', 11, TRN)
    s.group_end()
    ec = tbox(s, 6.85, 3.95, 6.1, 1.65, '**Grasa ectópica**: TAG e intermediarios lipídicos en **hígado, músculo, páncreas y corazón**: base de la **lipotoxicidad**.', 14.5, head='Ectópico')
    p = pearl(s, 4.1, 5.85, 8.85, 1.0, 'Subcutánea abdominal ≠ visceral. La **cintura estima** adiposidad central, pero **no mide** grasa visceral. Son tendencias, no dicotomías absolutas.', 14)
    s.step(zoom(sc), fade(a, after=True)); s.step(zoom(vi), fade(b, after=True)); s.step(fade(port)); s.step(fade(ec)); s.step(zoom(p))
    s.note('Subcutánea: bajo la piel, en región abdominal o glúteo-femoral; contribuye a protección, aislamiento y almacenamiento '
           'relativamente seguro; la región glúteo-femoral suele asociarse con menor riesgo cardiometabólico para una adiposidad '
           'global comparable. Visceral: omental/mesentérica, profunda; mayor actividad lipolítica e inflamatoria, con parte de su '
           'drenaje hacia el hígado por el sistema porta; su exceso se asocia a resistencia hepática, dislipidemia aterogénica y '
           'enfermedad cardiovascular. Son tendencias, no dicotomías absolutas [T][S]. El perímetro de cintura estima adiposidad '
           'central pero no mide grasa visceral; la clasificación de riesgo depende de población, sexo, etnicidad y perfil. Grasa '
           'ectópica: clave para el concepto de lipotoxicidad. Las marcas sobre la ilustración son esquemáticas.')


def types(D):
    s = new(D, U, 'Adipocitos blancos, pardos y beige', 'cyanR')
    adipocyte_white(s, 0.6, 1.25, 2.0, name='Blanco tipo')
    adipocyte_brown(s, 0.6, 3.35, 2.0, name='Pardo tipo')
    g = s.group_start('Beige tipo')
    adipocyte_white(s, 0.45, 5.35, 1.4)
    adipocyte_brown(s, 1.55, 5.45, 1.25)
    s.group_end()
    rows = [['Tipo', 'Morfología y marcadores', 'Función predominante'],
            ['Blanco (WAT)', 'Unilocular: gota grande, núcleo periférico; perilipinas', 'Almacenar/ceder TAG; adipocinas; amortiguar flujos de AG'],
            ['Pardo (BAT)', 'Multilocular, muchas mitocondrias, UCP1 alta; muy vascularizado e inervado', 'Termogénesis sin escalofríos por desacoplamiento mitocondrial'],
            ['Beige / brite', 'Termogénicos inducibles dentro de depósitos blancos; UCP1 variable', 'Termogénesis adaptativa (frío, simpático); interés experimental']]
    table(s, 2.9, 1.25, 10.05, rows, [1.7, 4.2, 4.15], size=13.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Tabla tipos', heights=[0.5, 1.6, 1.6, 1.6])
    s.note('Tipos de adipocitos. Blanco: unilocular, gota grande con núcleo periférico y perilipinas; almacena y cede TAG, produce '
           'adipocinas y amortigua flujos de ácidos grasos. Pardo: multilocular, muchas mitocondrias, UCP1 alta, rico en '
           'vascularización e inervación; termogénesis sin escalofríos por desacoplamiento mitocondrial. Beige o brite: termogénicos '
           'inducibles dentro de depósitos blancos, con UCP1 variable; termogénesis adaptativa con señales simpáticas o frío, campo '
           'de interés experimental [T][A].')


def ucp1(D):
    s = new(D, U, 'UCP1: protones que vuelven sin fabricar ATP', 'blue')
    s.shape(0.4, 1.2, 8.0, 1.6, 'rect', ('a', 'FADBD8', 70), (INK, 1.0), False, name='Espacio intermembrana')
    lab(s, 0.5, 1.25, 4.0, 0.35, 'ESPACIO INTERMEMBRANA (H⁺ alto)', 12, align='l')
    membrane_h(s, 0.4, 2.8, 8.0, 0.5, name='Membrana interna')
    s.shape(0.4, 3.3, 8.0, 2.4, 'rect', ('a', 'FCF3CF', 70), (INK, 1.0), False, name='Matriz')
    lab(s, 0.5, 5.3, 3.0, 0.35, 'MATRIZ', 12, align='l')
    cad = s.shape(0.8, 2.55, 2.0, 1.0, 'roundRect', shade('5DADE2', 0.4, 0.3), ('1F618D', 1.5), False, 'Cadena\nrespiratoria', 12, F_HEAD, INK, True, 'c', 'm', name='Cadena resp')
    ats = s.shape(3.6, 2.45, 1.4, 1.25, 'roundRect', shade('F5B041', 0.4, 0.3), ('9C640C', 1.5), False, 'ATP\nsintasa', 12, F_HEAD, INK, True, 'c', 'm', name='ATP sintasa')
    u = s.shape(6.0, 2.5, 1.2, 1.1, 'roundRect', shade('C0392B', 0.4, 0.3), ('641E16', 1.5), False, 'UCP1', 15, F_HEAD, WHITE, True, 'c', 'm', name='UCP1')
    hs = [s.shape(0.9 + i * 0.55, 1.7, 0.36, 0.36, 'ellipse', 'C00000', (INK, 1.0), False, 'H⁺', 10, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                  name='H mito %d' % i) for i in range(6)]
    atp = mol(s, 4.05, 4.2, 'atp', d=0.55, name='ATP formado')
    heat = s.group_start('Calor')
    flame(s, 6.2, 4.0, 0.9, name='Llama')
    lab(s, 5.6, 5.0, 2.2, 0.35, 'CALOR', 15, INH)
    s.group_end()
    st = steps_panel(s, 8.7, 1.2, 4.25, ['La cadena respiratoria **expulsa H⁺** al espacio intermembrana.', 'Normalmente el gradiente vuelve por la **ATP sintasa** → ATP.',
                                         '**UCP1** permite el retorno de H⁺ **sin** sintetizar ATP → la energía se **disipa como calor**.',
                                         'Los **ácidos grasos** liberados por lipólisis activan UCP1.'], 13.5, anim=False)[0]
    s.step(fade(st[0]), *[zoom(h, after=True, dur=150) for h in hs])
    s.step(fade(st[1]), path(hs[0], 4.25 - 0.9, 1.6, dur=1200), zoom(atp, after=True))
    s.step(fade(st[2]), path(hs[3], 6.45 - 2.55, 1.5, dur=1200), path(hs[4], 6.45 - 3.1, 1.5, dur=1200, delay=200), fade(heat, after=True))
    s.step(fade(st[3]))
    s.note('Mecanismo de UCP1. En mitocondrias normales la cadena respiratoria expulsa protones y la ATP sintasa usa el gradiente para '
           'formar ATP; UCP1 permite el retorno de protones sin sintetizar ATP y disipa la energía como calor. Los ácidos grasos '
           'pueden activar UCP1 [T][A]. Animación: aparecen los H⁺ bombeados; uno regresa por la ATP sintasa y genera ATP; otros '
           'regresan por UCP1 y aparece la llama de calor.')


def thermo(D):
    s = new(D, U, 'Termogénesis adaptativa: del frío a UCP1', 'pink')
    nodes = {
        'f': (0.4, 1.3, 2.0, 0.6, 'Frío', 's', 17),
        'h': (2.9, 1.3, 2.3, 0.6, 'Hipotálamo', 'w', 16),
        'sn': (5.7, 1.3, 2.6, 0.6, 'Sistema simpático', 'w', 15),
        'na': (8.8, 1.3, 2.2, 0.6, 'Noradrenalina', 's', 15),
        'b': (8.8, 2.4, 2.2, 0.6, 'Receptores β', 'g', 15),
        'c': (5.7, 2.4, 2.6, 0.6, 'AMPc → PKA', 'w', 16),
        'l': (2.9, 2.4, 2.3, 0.6, 'Lipólisis', 'Y', 16),
        'ag': (0.4, 2.4, 2.0, 0.6, 'AG activan UCP1', 'y', 13),
        'p': (2.9, 3.5, 5.4, 0.6, 'Programa termogénico: PGC-1α · PPAR · hormonas tiroideas → biogénesis mitocondrial', 'g', 12.5),
    }
    edges = [('f', 'h'), ('h', 'sn'), ('sn', 'na'), ('na', 'b'), ('b', 'c'), ('c', 'l'), ('l', 'ag'), ('c', 'p')]
    graph(s, nodes, edges, [['f', 'f>h', 'h', 'h>sn', 'sn', 'sn>na', 'na'], ['na>b', 'b', 'b>c', 'c'], ['c>l', 'l', 'l>ag', 'ag'], ['c>p', 'p']])
    adipocyte_brown(s, 11.2, 2.3, 1.7, name='Pardo termo')
    p = pearl(s, 0.4, 4.6, 12.55, 1.2, '**Matiz de evidencia**: la grasa parda activa existe en adultos, pero «convertir blanco en pardo» para tratar obesidad sigue siendo **investigación**, no tratamiento estándar. Las «futuras estrategias» de 2009 se leen en su contexto histórico.', 14.5)
    s.step(zoom(p))
    s.note('Frío → hipotálamo → sistema simpático → noradrenalina → receptores β-adrenérgicos → AMPc/PKA → lipólisis y activación del '
           'programa termogénico. Los ácidos grasos pueden activar UCP1. PGC-1α, PPAR y hormonas tiroideas participan en la '
           'biogénesis y regulación mitocondrial [T][A]. Matiz de evidencia: la activación de grasa parda en humanos adultos existe, '
           'pero la importancia terapéutica de transformar tejido blanco en pardo sigue siendo un campo de investigación.')


def adipogenesis(D):
    s = new(D, U, 'Adipogénesis: de célula mesenquimal a adipocito maduro', 'green')
    stg = [('Progenitora mesenquimal', 'C39BD3', 0.9, 0.4), ('Preadipocito comprometido', 'F5CBA7', 1.0, 3.4), ('Diferenciación', 'F8C471', 1.15, 6.4)]
    ids = []
    for i, (t, c, d, x) in enumerate(stg):
        g = s.group_start('Etapa %d' % i)
        sphere(s, x + 0.7, 1.35, d * 1.2, c, name='Célula %d' % i)
        lab(s, x, 2.75, 2.7, 0.5, t, 13)
        ids.append(s.group_end())
    g = s.group_start('Adipocito maduro')
    adipocyte_white(s, 9.95, 1.15, 1.6)
    lab(s, 9.4, 2.75, 2.7, 0.5, 'Adipocito con gota', 13)
    ids.append(s.group_end())
    ar = [s.arrow([(2.75, 1.85), (3.95, 1.85)], INK, 3), s.arrow([(5.75, 1.85), (6.95, 1.85)], INK, 3), s.arrow([(8.95, 1.85), (9.85, 1.85)], INK, 3)]
    nodes = {
        'cb': (0.4, 3.55, 3.0, 0.6, 'C/EBPβ · C/EBPδ (tempranos)', 'b', 13),
        'pp': (4.0, 3.55, 3.0, 0.6, 'PPARγ : RXR', 'y', 17),
        'ca': (7.6, 3.55, 2.6, 0.6, 'C/EBPα', 'b', 16),
        'gn': (4.0, 4.6, 8.95, 0.65, 'Genes adipocitarios: adiponectina · FABP4 · LPL · GLUT4 · perilipinas · enzimas de esterificación', 'Y', 13),
        'in': (10.5, 3.55, 2.45, 0.6, 'Insulina · IGF-1', 'g', 13.5),
        'wn': (0.4, 4.6, 3.0, 0.65, 'Wnt/β-catenina', 's', 14),
    }
    edges = [('cb', 'pp'), ('pp', 'ca', {'both': True}), ('pp', 'gn'), ('in', 'ca', {'col': ACT}), ('wn', 'pp', {'inh': True, 'pts': [(3.45, 4.9), (3.75, 4.9), (3.75, 4.2), (4.6, 4.2)]})]
    graph(s, nodes, edges, [['cb', 'cb>pp', 'pp'], ['pp>ca', 'ca'], ['pp>gn', 'gn'], ['in', 'in>ca'], ['wn', 'wn>pp']])
    s.anim = [[fade(ids[0])], [wipe(ar[0], 'l'), fade(ids[1], after=True)], [wipe(ar[1], 'l'), fade(ids[2], after=True)], [wipe(ar[2], 'l'), fade(ids[3], after=True)]] + s.anim
    t = tbox(s, 0.4, 5.5, 12.55, 1.35, '**PPARγ** es el regulador central: factor de transcripción nuclear que **heterodimeriza con RXR**. C/EBPβ/δ actúan temprano; **C/EBPα** consolida el programa junto con PPARγ. Wnt/β-catenina puede **oponerse** en determinados contextos.', 14)
    s.step(fade(t))
    s.note('Adipogénesis: célula progenitora mesenquimal → preadipocito comprometido → diferenciación → adipocito con gotas de lípidos. '
           'El regulador central es PPARγ, que heterodimeriza con RXR y promueve la expresión de genes adipocitarios (adiponectina, '
           'FABP4, LPL, GLUT4, perilipinas, enzimas de esterificación). C/EBPβ y C/EBPδ actúan relativamente temprano; C/EBPα '
           'consolida el programa maduro junto con PPARγ (refuerzo mutuo). Insulina e IGF-1 son señales permisivas/anabólicas; las vías '
           'Wnt/β-catenina pueden oponerse a la adipogénesis en determinados contextos [T].')


def hyper(D):
    s = new(D, U, 'Hipertrofia frente a hiperplasia', 'peach')
    l = s.group_start('Hipertrofia')
    mbox(s, 0.4, 1.2, 6.0, 0.6, 'HIPERTROFIA: más volumen por célula', 's', 15)
    adipocyte_white(s, 0.9, 2.05, 1.3, name='Antes h')
    s.arrow([(2.4, 2.7), (3.1, 2.7)], INK, 3)
    adipocyte_white(s, 3.3, 1.95, 2.6, name='Después h')
    tbox(s, 0.4, 4.75, 6.0, 2.1, 'Excesiva → irrigación relativa ↓, manejo de **O₂** alterado, **matriz** rígida y secreción de adipocinas **desfavorable**.', 15)
    s.group_end()
    r = s.group_start('Hiperplasia')
    mbox(s, 6.95, 1.2, 6.0, 0.6, 'HIPERPLASIA: más células desde precursores', 'g', 15)
    adipocyte_white(s, 7.3, 2.05, 1.3, name='Antes p')
    s.arrow([(8.8, 2.7), (9.5, 2.7)], INK, 3)
    for i, (x, y) in enumerate([(9.7, 1.95), (11.05, 1.95), (9.7, 3.3), (11.05, 3.3)]):
        adipocyte_white(s, x, y, 1.3, name='Hija %d' % i)
    tbox(s, 6.95, 4.75, 6.0, 2.1, 'Reparte el exceso energético en **más células con menos estrés** por célula. No interpretar automáticamente «más adipocitos = peor metabolismo».', 15)
    s.group_end()
    s.step(fade(l)); s.step(fade(r))
    s.note('Hipertrofia: aumento de volumen de adipocitos existentes; hiperplasia: aumento del número de adipocitos a partir de '
           'precursores. Cuando el adipocito se hipertrofia en exceso se alteran la irrigación relativa, el manejo de oxígeno, la '
           'matriz extracelular y la secreción de adipocinas. La hiperplasia funcional puede repartir el exceso energético en más '
           'células con menos estrés por célula [T].')


def lpl_hsl(D):
    s = new(D, U, 'LPL frente a HSL: dos lipasas, dos compartimentos', 'cyan')
    vessel(s, 0.4, 1.2, 12.55, 1.1, rbcs=10, name='Capilar LPL')
    lab(s, 0.5, 2.35, 2.5, 0.35, 'LUZ CAPILAR', 12, align='l')
    lp = lipoprotein(s, 2.3, 1.3, 0.85, text='QM', name='Quilomicrón')
    vl = lipoprotein(s, 4.2, 1.35, 0.75, core='F5CBA7', text='VLDL', name='VLDL')
    lpl = mbox(s, 3.15, 2.35, 1.0, 0.45, 'LPL', 'g', 15, name='LPL')
    s.shape(0.4, 2.85, 12.55, 0.12, 'rect', 'C0392B', None, False, name='Endotelio')
    ad = s.shape(0.9, 3.25, 6.0, 3.55, 'ellipse', shade('F6D7B0', 0.4, 0.25), ('8C5A2B', 2), SHD, name='Adipocito LPL')
    drop = s.shape(1.9, 3.75, 4.0, 2.55, 'ellipse', ('rad', [(0, 'FFF8D0'), (50, 'F7DC6F'), (100, 'D4AC0D')], (35, 30)), ('B7950B', 1.25), False, 'TAG', 18, F_HEAD, '7D6608', True, 'c', 'm', fit=False, name='Gota LPL')
    hsl = mbox(s, 5.15, 5.5, 1.0, 0.45, 'HSL', 's', 15, name='HSL')
    ags = [mol(s, 4.35 + i * 0.42, 2.42, 'ag', d=0.32, name='AG LPL %d' % i) for i in range(3)]
    t1 = tbox(s, 7.3, 3.25, 5.65, 1.65, '**LPL**: sobre el **endotelio capilar**; hidroliza TAG de **quilomicrones y VLDL** → AG que entran al adipocito (CD36/FATP). La **insulina** la favorece en el adiposo.', 13.5, head='Espacio vascular')
    t2 = tbox(s, 7.3, 5.15, 5.65, 1.7, '**HSL**: **dentro** del adipocito; hidroliza lípidos de la **gota** (lipólisis intracelular) junto con ATGL y MGL. **Catecolaminas** la activan; la insulina la frena.', 13.5, head='Intracelular', hkind='s')
    s.step(pulse(lpl), *[fade(a, after=True, dur=150) for a in ags])
    s.step(*[path(a, 0.0, 1.9, dur=1200, delay=i * 200) for i, a in enumerate(ags)], fade(t1, after=True))
    s.step(pulse(hsl), fade(t2, after=True))
    s.note('LPL frente a HSL. La lipoproteína lipasa, localizada funcionalmente sobre el endotelio capilar, hidroliza los TAG de '
           'quilomicrones y VLDL liberando ácidos grasos que entran al adipocito por transporte facilitado y difusión (CD36/FATP). '
           'La lipasa hormonosensible actúa sobre lípidos dentro del adipocito. No deben confundirse: LPL actúa en el espacio '
           'vascular; HSL, en la gota lipídica intracelular (pregunta 4 de opción múltiple). La regulación recíproca por insulina '
           '(LPL adiposa ↑, HSL ↓) es parte del estado alimentado.')


def g3p(D):
    s = new(D, U, 'Glicerol-3-fosfato: el esqueleto del triglicérido', 'greenR')
    nodes = {
        'g': (0.4, 1.3, 2.2, 0.55, 'Glucosa', 'y', 15),
        'g4': (0.4, 2.2, 2.2, 0.55, 'GLUT4 (insulina)', 'g', 13),
        'gl': (3.1, 2.2, 2.4, 0.55, 'Glucólisis', 'w', 14),
        'dh': (3.1, 3.2, 2.4, 0.55, 'DHAP', 'y', 15),
        'g3': (3.1, 4.4, 2.4, 0.65, 'GLICEROL-3-P', 'y', 15),
        'py': (6.2, 3.2, 2.6, 0.55, 'Piruvato y otros', 'w', 13),
        'gc': (0.4, 4.4, 2.2, 0.65, 'Glicerol', 'y', 15),
        'bl': (0.4, 5.6, 2.2, 0.6, 'Sangre → hígado', 's', 13),
    }
    edges = [('g', 'g4'), ('g4', 'gl'), ('gl', 'dh'), ('dh', 'g3', {'lab': 'G3P deshidrogenasa', 'ls': 10.5, 'ox': 1.35}),
             ('py', 'dh', {'lab': 'gliceroneogénesis (PEPCK)', 'ls': 10, 'oy': -0.38}), ('gc', 'g3', {'lab': 'glicerol cinasa BAJA', 'ls': 10, 'dash': 'dash', 'oy': -0.36, 'col': INH}),
             ('gc', 'bl', {'col': TRN})]
    graph(s, nodes, edges, [['g', 'g>g4', 'g4', 'g4>gl', 'gl', 'gl>dh', 'dh', 'dh>g3', 'g3'], ['py', 'py>dh'], ['gc', 'gc>g3'], ['gc>bl', 'bl']])
    model(s, 'glicerol', 9.4, 1.25, 1.9, name='Glicerol 3D', label='Glicerol')
    t = tbox(s, 6.2, 4.25, 6.75, 2.6, '- Fuente principal: **glucólisis vía DHAP** (por eso la insulina y GLUT4 favorecen el almacenamiento).\n- También **gliceroneogénesis** desde piruvato.\n'
             '- La **glicerol cinasa** del adiposo blanco es **baja** frente al hígado: el glicerol de la lipólisis sale en gran proporción a la **circulación** (sustrato gluconeogénico).', 13.5, head='Claves')
    s.step(fade(t))
    s.note('El adipocito obtiene glicerol-3-fosfato sobre todo a partir de la glucólisis vía DHAP y glicerol-3-P deshidrogenasa; también '
           'por gliceroneogénesis desde precursores como piruvato. La actividad de glicerol cinasa en el tejido adiposo blanco suele '
           'ser baja respecto del hígado, por lo que el glicerol liberado en la lipólisis se dirige en gran proporción a la '
           'circulación [T]. La participación de PEPCK en la gliceroneogénesis es ampliación bibliográfica.')


def esterif(D):
    s = new(D, U, 'Esterificación: del glicerol-3-P al triacilglicerol', 'cyanR')
    items = [('Glicerol-3-P', 'y'), ('Ácido lisofosfatídico', 'Y'), ('Ácido fosfatídico', 'Y'), ('Diacilglicerol', 'Y'), ('TRIACILGLICEROL', 'y')]
    enz_ = ['GPAT + acil-CoA', 'AGPAT + acil-CoA', 'Lipina (fosfatasa de PA)', 'DGAT + acil-CoA']
    ids = []
    for i, (t, k) in enumerate(items):
        y = 1.2 + i * 1.08
        g = s.group_start('Est %d' % i)
        mbox(s, 0.6, y, 3.6, 0.62, t, k, 15)
        if i:
            s.arrow([(2.4, y - 0.43), (2.4, y - 0.03)], INK, 2.5)
            elabel(s, 2.6, y - 0.38, enz_[i - 1], 11)
            mol(s, 5.5, y - 0.45, 'ag', d=0.36, name='AG est %d' % i) if 'acil' in enz_[i - 1] else None
        ids.append(s.group_end())
    m = model(s, 'tag', 6.5, 1.2, 3.4, hs=False, name='TAG 3D est', label='Triacilglicerol (modelo)')
    drop = s.group_start('Gota con perilipinas')
    s.shape(10.3, 1.3, 2.6, 2.6, 'ellipse', ('rad', [(0, 'FFF8D0'), (50, 'F7DC6F'), (100, 'D4AC0D')], (35, 30)), ('B7950B', 1.5), False, 'TAG', 16, F_HEAD, '7D6608', True, 'c', 'm', fit=False)
    import math
    for k in range(10):
        a = k * 2 * math.pi / 10
        s.shape(11.6 + 1.3 * math.cos(a) - 0.12, 2.6 + 1.3 * math.sin(a) - 0.12, 0.24, 0.24, 'ellipse', '7D3C98', None, False)
    lab(s, 10.2, 3.95, 2.8, 0.35, 'Perilipinas en la superficie', 11.5)
    s.group_end()
    t = tbox(s, 6.5, 4.45, 6.45, 2.4, 'La insulina promueve el almacenamiento: GLUT4, glicerol-3-P, captación y esterificación de AG e **inhibición** de la lipólisis. '
             'La glucosa **no** se «convierte toda en grasa» inevitablemente: el flujo depende del estado hormonal, la dieta y el balance sostenido.', 13.5, head='Regulación')
    for g in ids:
        s.step(fade(g))
    s.step(fade(m)); s.step(fade(drop)); s.step(fade(t))
    s.note('Los acil-CoA se esterifican secuencialmente sobre glicerol-3-P por GPAT (ácido lisofosfatídico), AGPAT (ácido '
           'fosfatídico), la fosfatasa de ácido fosfatídico lipina (diacilglicerol) y DGAT (triacilglicerol), formando TAG en gotas '
           'delimitadas por perilipinas. El modelo 3D representa un triacilglicerol con tres cadenas acilo (molécula representativa). '
           'La insulina promueve el almacenamiento; la glucosa no se convierte toda en grasa de forma inevitable [T].')


def dnl(D):
    s = new(D, U, 'Lipogénesis de novo: de citrato a palmitato', 'yellow')
    nodes = {
        'ci': (0.4, 1.3, 2.4, 0.6, 'CITRATO (mitocondria)', 'y', 12.5),
        'ac': (3.3, 1.3, 2.4, 0.6, 'ACETIL-COA citosólico', 'y', 12.5),
        'ma': (6.2, 1.3, 2.4, 0.6, 'MALONIL-COA', 'y', 14),
        'pa': (9.1, 1.3, 2.4, 0.6, 'PALMITATO', 'y', 15),
        'np': (9.1, 2.5, 3.85, 0.55, 'NADPH (pentosas fosfato / enzima málica)', 'b', 12),
        'sr': (0.4, 2.65, 5.3, 0.6, 'SREBP-1c (insulina) · ChREBP (carbohidratos) → inducen enzimas', 'g', 12.5),
        'am': (3.3, 3.8, 2.4, 0.55, 'AMPK (baja energía)', 's', 13),
        'cp': (6.2, 3.8, 2.4, 0.55, 'CPT1', 'g', 15),
    }
    edges = [('ci', 'ac', {'lab': 'ACLY', 'ls': 11, 'oy': -0.34}), ('ac', 'ma', {'lab': 'ACC', 'ls': 11, 'oy': -0.34}), ('ma', 'pa', {'lab': 'FASN', 'ls': 11, 'oy': -0.34}),
             ('np', 'pa', {'pts': [(10.3, 2.48), (10.3, 1.95)]}), ('sr', 'ma', {'col': ACT, 'pts': [(5.75, 2.95), (6.9, 2.95), (6.9, 1.95)]}),
             ('am', 'ma', {'inh': True, 'pts': [(5.75, 4.07), (6.0, 4.07), (6.0, 2.2), (6.6, 2.2), (6.6, 1.95)]}), ('ma', 'cp', {'inh': True, 'pts': [(7.4, 1.95), (7.4, 3.75)]})]
    graph(s, nodes, edges, [['ci', 'ci>ac', 'ac', 'ac>ma', 'ma', 'ma>pa', 'pa'], ['np', 'np>pa'], ['sr', 'sr>ma'], ['am', 'am>ma'], ['cp', 'ma>cp']])
    m = model(s, 'palmitato', 8.9, 3.45, 4.05, hs=True, name='Palmitato 3D', label='Palmitato (C16:0)')
    t = tbox(s, 0.4, 4.7, 8.2, 2.15, '- El **malonil-CoA** inhibe CPT1: coordina **más síntesis con menos oxidación** simultánea.\n- La DNL es central en el **hígado** con exceso de carbohidratos/energía; el adipocito humano también participa.\n'
             '- Exceso crónico de sustrato hepático → **VLDL ↑** → hipertrigliceridemia.', 13.5, head='Coordinación')
    s.step(fade(m)); s.step(fade(t))
    s.note('Lipogénesis de novo: el citrato exportado del ciclo de Krebs se escinde por ATP-citrato liasa (ACLY) en acetil-CoA '
           'citosólico; la acetil-CoA carboxilasa (ACC) genera malonil-CoA; la ácido graso sintasa (FASN) sintetiza palmitato '
           'utilizando NADPH (vía de las pentosas fosfato y enzima málica). SREBP-1c y ChREBP inducen las enzimas lipogénicas en '
           'respuesta a insulina y carbohidratos. AMPK fosforila e inhibe ACC en contextos de baja energía. El malonil-CoA inhibe CPT1, '
           'coordinando mayor síntesis con menor oxidación. La DNL tiene papel hepático importante con exceso de carbohidratos; el '
           'exceso crónico de sustrato hepático eleva la producción de VLDL [T]. Modelo 3D: palmitato con hidrógenos.')


# ---------------------------------------------------------------- Ejemplo 5: lipólisis (Morph, la gota se reduce)
def lipo_scene(s, k):
    s.shape(0.4, 1.15, 7.9, 5.7, 'ellipse', shade('F6D7B0', 0.4, 0.25), ('8C5A2B', 2.5), SHD, name='!!Adipocito lipo')
    d = [3.6, 3.1, 2.5][k]
    cx, cy = 4.35, 4.15
    s.shape(cx - d / 2, cy - d / 2, d, d, 'ellipse', ('rad', [(0, 'FFF8D0'), (50, 'F7DC6F'), (100, 'D4AC0D')], (35, 30)), ('B7950B', 1.5), False,
            'TAG', 18, F_HEAD, '7D6608', True, 'c', 'm', fit=False, name='!!Gota lipo')
    import math
    for i in range(8):
        a = i * 2 * math.pi / 8
        s.shape(cx + d / 2 * math.cos(a) - 0.13, cy + d / 2 * math.sin(a) - 0.13, 0.26, 0.26, 'ellipse', '7D3C98', None, False, name='!!PLIN %d' % i)
    gpcr(s, 3.2, 1.2, 0.36, 1.0, name='!!Receptor β', color='7DCEA0')
    lab(s, 1.5, 1.05, 1.6, 0.35, 'β-AR (Gs)', 12, name='!!Rótulo βAR')


def lipo_panel(s, n, txt):
    g = s.group_start('!!Panel lipo')
    s.shape(8.6, 1.15, 4.35, 4.0, 'rect', WHITE, (INK, 1.5), SHD)
    s.shape(8.75, 1.27, 0.75, 0.55, 'rect', BOX, (INK, 1.5), False, n, 15, F_HEAD, BOXT, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.text(9.6, 1.22, 3.25, 0.65, 'Lipólisis', 17, F_HEAD, INK, True, 'l', 'm')
    s.text(8.8, 1.95, 4.0, 3.1, txt, 14, F_BODY, INK, False, 'l', 't', spc=5)
    return s.group_end()


def lipo1(D):
    s = new(D, U, 'Ejemplo 5 · lipólisis 1: señal hormonal y PKA', 'green')
    lipo_scene(s, 0)
    lipo_panel(s, '1', '- **Catecolaminas** → receptores **β-adrenérgicos** → Gs → adenilil ciclasa → **AMPc** → **PKA**.\n- **α₂-adrenérgicos/Gi** reducen AMPc y pueden oponerse según depósito.\n- La **insulina** frena vía Akt → **PDE3B** → AMPc ↓.')
    na = mol(s, 0.75, 1.55, 'gcg', d=0.45, text='NA', name='Noradrenalina')
    camp = [s.shape(4.5 + i * 0.55, 1.75, 0.5, 0.35, 'roundRect', 'D4E6F1', ('1F618D', 1.0), False, 'AMPc', 9, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                    name='AMPc %d' % i) for i in range(3)]
    pka = mbox(s, 6.25, 1.7, 1.0, 0.45, 'PKA', 'g', 14, name='!!PKA')
    pp = [s.shape(4.35 + 1.8 * c - 0.15, 4.15 + 1.8 * sn - 0.15, 0.3, 0.3, 'ellipse', BOX, (INK, 1.0), False, 'P', 9, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                  name='P PLIN %d' % i) for i, (c, sn) in enumerate([(0.0, -1.0), (0.71, -0.71), (-0.71, -0.71)])]
    ins = s.group_start('Freno insulina')
    mbox(s, 0.6, 6.0, 3.4, 0.5, 'Insulina → PDE3B → AMPc ↓', 'r', 12.5)
    s.group_end()
    s.step(fade(na), path(na, 2.75, -0.35, dur=900))
    s.step(*[zoom(c, after=i > 0, dur=200) for i, c in enumerate(camp)], pulse(pka, after=True))
    s.step(*[zoom(p, after=i > 0, dur=200) for i, p in enumerate(pp)])
    s.step(fade(ins))
    s.note('Ejemplo 5, paso 1 (secuencia Morph de tres diapositivas: la gota lipídica disminuye progresivamente). La noradrenalina '
           'se une a receptores β-adrenérgicos acoplados a Gs: adenilil ciclasa → AMPc → PKA, que fosforila HSL y perilipina 1 '
           '(fichas P sobre la gota). Los receptores α₂/Gi reducen el AMPc y pueden oponerse según el depósito. La insulina inhibe '
           'la lipólisis vía Akt → PDE3B → degradación del AMPc [T].')


def lipo2(D):
    s = new(D, U, 'Ejemplo 5 · lipólisis 2: perilipina, CGI-58 y ATGL', 'green', morph=True)
    lipo_scene(s, 1)
    lipo_panel(s, '2', '- La perilipina 1 fosforilada **libera CGI-58 (ABHD5)**.\n- CGI-58 **coactiva a ATGL (PNPLA2)**.\n- **TAG → DAG + ácido graso**: primer paso, limitante.')
    cgi = mbox(s, 5.7, 2.3, 1.2, 0.45, 'CGI-58', 'b', 12.5, name='!!CGI58')
    atgl = mbox(s, 5.7, 3.05, 1.2, 0.45, 'ATGL', 'g', 14, name='!!ATGL')
    dag = mbox(s, 2.0, 5.85, 1.3, 0.45, 'DAG', 'y', 14, name='!!DAG')
    ag = mol(s, 3.6, 5.85, 'ag', d=0.42, name='!!AG lipo 1')
    s.step(fade(cgi), path(cgi, -0.4, 0.5, dur=900), pulse(atgl, after=True))
    s.step(zoom(dag), zoom(ag, after=True))
    s.note('Paso 2. La perilipina 1 fosforilada libera al coactivador CGI-58 (ABHD5) de los complejos de la superficie de la gota; '
           'CGI-58 activa a la ATGL (PNPLA2), que hidroliza el triacilglicerol a diacilglicerol + ácido graso. Por Morph la gota '
           'ya es más pequeña [T].')


def lipo3(D):
    s = new(D, U, 'Ejemplo 5 · lipólisis 3: HSL, MGL y salida de productos', 'green', morph=True)
    lipo_scene(s, 2)
    lipo_panel(s, '3', '- **HSL (LIPE)**: DAG → **MAG** + AG.\n- **MGL (MGLL)**: MAG → **glicerol** + AG.\n- Salida: **AGNE unidos a albúmina** · **glicerol** al hígado (gluconeogénesis).')
    chain = s.group_start('Cadena lipasas')
    for i, (t, k) in enumerate([('DAG', 'y'), ('MAG', 'y'), ('Glicerol', 'y')]):
        mbox(s, 1.3 + i * 2.2, 5.85, 1.4, 0.45, t, k, 13.5, name='!!Lip prod %d' % i)
    elabel(s, 2.65, 5.55, 'HSL', 12); elabel(s, 4.85, 5.55, 'MGL', 12)
    s.arrow([(2.72, 6.07), (3.48, 6.07)], INK, 2.5); s.arrow([(4.92, 6.07), (5.68, 6.07)], INK, 2.5)
    s.group_end()
    ags = [mol(s, 3.6 + i * 0.5, 4.6, 'ag', d=0.42, name='!!AG lipo %d' % (i + 1)) for i in range(3)]
    out_ = s.group_start('Salida')
    s.arrow([(7.9, 4.2), (8.9, 5.7)], TRN, 4, dash='dash')
    mbox(s, 8.6, 5.75, 4.35, 0.95, 'Sangre: AGNE–albúmina + glicerol', 's', 14, caps=False)
    s.group_end()
    s.step(fade(chain))
    s.step(*[path(a, 4.6 - i * 0.5, 0.0, dur=1200, delay=i * 200) for i, a in enumerate(ags)], fade(out_, after=True))
    s.note('Paso 3. La lipasa hormonosensible (HSL, LIPE) hidroliza el DAG a monoacilglicerol + ácido graso y la monoacilglicerol '
           'lipasa (MGL, MGLL) libera glicerol + ácido graso. Proceso completo: TAG → (ATGL) DAG + AG → (HSL) MAG + AG → (MGL) glicerol '
           '+ AG. Los AGNE viajan unidos a albúmina y el glicerol contribuye a la gluconeogénesis hepática. La lipólisis fisiológica '
           'permite sobrevivir entre comidas; la disfunción aparece cuando el tejido adiposo libera un exceso crónico de AGNE y '
           'señales inflamatorias [T]. La gota, ahora más pequeña, ilustra la movilización de reservas.')


def build(D):
    div(D)
    organ(D)
    expansion(D)
    depots(D)
    types(D)
    ucp1(D)
    thermo(D)
    adipogenesis(D)
    hyper(D)
    lpl_hsl(D)
    g3p(D)
    esterif(D)
    dnl(D)
    lipo1(D)
    lipo2(D)
    lipo3(D)
