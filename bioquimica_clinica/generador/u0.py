# -*- coding: utf-8 -*-
"""Portada, mapa de la clase, hilo conductor y código visual."""
from plantillas import *


def portada(D):
    s = D.new(BLANCO)
    s.unit = 0; s.morph = False
    s.shape(0, 0, 5.2, SH, 'rect', AMA, None, False, name='Fondo panel')
    s.shape(10.4, 0, SW - 10.4, SH, 'rect', CELESTE, None, False, name='Fondo panel der')
    # gran ilustración central: corazón, hígado, páncreas, sangre
    ids = corazon_anat(s, 0.35, 0.9, 3.2)
    liv = liver(s, 2.7, 4.6, 3.6, name='!!Higado')
    pan = pancreas(s, 0.2, 5.9, 3.0, name='!!Pancreas')
    for i, (xx, yy, d) in enumerate(((10.7, 0.6, 1.3), (11.7, 1.7, 1.1), (10.9, 2.6, 0.9), (12.1, 3.3, 0.8))):
        eritrocito(s, xx, yy, d, name='Eritrocito portada %d' % i)
    m1 = molecula3d(s, 10.6, 4.5, 2.4, 'piruvato', name='Molécula piruvato')
    m2 = molecula3d(s, 4.5, 0.15, 1.3, 'aa', name='Molécula aminoácido', rot=20)
    t = s.shape(5.0, 1.2, 5.6, 3.0, 'rect', None, None, False, 'BIOQUÍMICA CLÍNICA Y METABOLISMO', 44, F_TITLE, TBLUE, True, 'c', 'm',
                (0, 0, 0, 0), name='Título principal', reff=GLOW_W, lnspc=0.88, minsize=26)
    sub = manuscrito(s, 5.0, 4.25, 5.6, 0.9, 'De los mecanismos moleculares a la interpretación del laboratorio', 19, INK, name='Subtítulo')
    chips = s.group_start('Unidades portada')
    for i, (txt, f) in enumerate((('Laboratorio', CELESTE), ('Metabolismo', VERDE_CL), ('Anemias', SALM), ('IAM', AZUL_M), ('Hepatopancreático', DURAZNO))):
        rotulo(s, 5.25 + (i % 3) * 1.8, 5.35 + (i // 3) * 0.6, txt, f, 14, w=1.7)
    cg = s.group_end()
    s.meta = {'titulo': 'PORTADA', 'unit': 0, 'src': []}
    s.step(fade(t), fade(sub, after=True))
    s.step(fade(cg))
    s.note('Clase integrada de Bioquímica Clínica y Metabolismo en cinco unidades: laboratorio clínico, termodinámica y metabolismo '
           'intermedio (complejo PDH), anemias, infarto agudo de miocardio y enzimología hepatopancreática.')


def mapa(D):
    s = nueva(D, 0, 'Mapa de la clase: cinco unidades, un mismo razonamiento', tipo='der', c1=AMA, c2=BLANCO)
    data = [
        ('I', 'Variables bioquímicas y laboratorio', 'Analitos, sangre, suero y plasma, unidades, sensibilidad, especificidad, precisión, intervalos de referencia y control de calidad.', CELESTE),
        ('II', 'Termodinámica y metabolismo intermedio', 'ΔG, reacciones acopladas, redox, catabolismo y anabolismo, acetil-CoA, piruvato y complejo PDH.', VERDE_CL),
        ('III', 'Bioquímica clínica de las anemias', 'Hemoglobina, índices hematimétricos, reticulocitos, anemia megaloblástica, biomarcadores y casos.', SALM),
        ('IV', 'Infarto agudo de miocardio', 'ECG, cardiomiocito, troponinas, CK-MB, mioglobina, LDH, cinética y seguimiento.', AZUL_M),
        ('V', 'Pancreatitis y enzimología hepatopancreática', 'Transaminasas, De Ritis, FAL, GGT, bilirrubina, amilasa, lipasa, zimógenos y diagnóstico diferencial.', DURAZNO),
    ]
    ids = []
    for i, (r, t, d, f) in enumerate(data):
        y = 1.15 + i * 1.2
        g = s.group_start('Unidad %s' % r)
        s.shape(0.45, y, 0.95, 1.05, 'roundRect', NAVY, (INK, 1.75), False, r, 30, F_TITLE, BLANCO, True, 'c', 'm', (0, 0, 0, 0), fit=False,
                adj={'adj': 14000})
        caja(s, 1.5, y, 7.3, 1.05, '**%s**\n%s' % (t, d), f, 14.5, spc=1, minsize=11)
        s.group_end(); ids.append(g)
    # ilustraciones en el panel derecho
    ic = s.group_start('Íconos de unidades')
    tubo(s, 9.55, 1.15, 0.5, 1.6, [(0.5, 'B3261E', 'Rojo m'), (0.4, 'F9E79F', 'Plasma m')], name='Tubo mapa')
    mitocondria_grande(s, 10.4, 1.25, 2.6, 1.4, name='Mitocondria mapa')
    eritrocito(s, 9.5, 3.2, 1.2, name='Eritrocito mapa'); eritrocito(s, 10.4, 3.7, 0.9, 'hipo', name='Eritrocito hipo mapa')
    corazon_anat(s, 11.3, 2.95, 1.6, name='Corazón mapa', coronarias=True)
    liver(s, 9.4, 5.3, 2.3, name='Hígado mapa'); pancreas(s, 11.0, 6.2, 2.1, name='Páncreas mapa')
    s.group_end()
    for g in ids:
        s.step(fade(g))
    s.meta['src'] = []


def hilo(D):
    s = nueva(D, 0, 'Hilo conductor: de la molécula al dato de laboratorio', tipo='bandas', c1=CELESTE, c2=AMA)
    pasos = [('Función molecular normal', 'Enzimas, proteínas y metabolitos cumplen su función dentro de la célula.', VERDE_CL),
             ('Alteración del tejido', 'Isquemia, autodigestión, hemólisis, obstrucción o déficit de cofactores.', SALM),
             ('Liberación / cambio de concentración', 'El analito pasa a la sangre o cambia su concentración plasmática.', AMA),
             ('Medición', 'Muestra adecuada (suero o plasma), unidad correcta y método preciso y exacto.', CELESTE),
             ('Interpretación', 'Intervalo de referencia, cinética temporal, sensibilidad, especificidad y clínica del paciente.', LAVANDA)]
    ids = []
    for i, (t, d, f) in enumerate(pasos):
        x = 0.4 + i * 2.55
        y = 1.6 + (i % 2) * 0.55
        g = s.group_start('Paso %d' % (i + 1))
        num(s, x + 0.95, y - 0.3, i + 1)
        caja(s, x, y + 0.25, 2.3, 2.3, '**%s**\n%s' % (t, d), f, 15, spc=3, minsize=11)
        if i < 4:
            s.arrow([(x + 2.32, y + 1.4), (x + 2.53, y + 1.4 + (0.55 if i % 2 == 0 else -0.55))], INK, 3)
        s.group_end(); ids.append(g)
    ilu = s.group_start('Ilustraciones hilo')
    cardiomiocito(s, 0.5, 4.95, 3.3, 1.5, name='Cardiomiocito hilo')
    tubo(s, 4.6, 4.75, 0.55, 2.2, [(0.48, 'B3261E', 'Rojo h'), (0.04, 'F2F3F4', 'Buffy h'), (0.38, 'F9E79F', 'Plasma h')], name='Tubo hilo')
    centrifuga(s, 5.6, 4.95, 1.55, name='Centrífuga hilo')
    s.group_end()
    c = caja(s, 7.8, 4.85, 5.1, 2.2, 'Un solo biomarcador no alcanza: la **integración de varios biomarcadores con la clínica** es la que permite localizar el daño y '
             'razonar el diagnóstico.', AMA, 16, head='Idea central', name='Idea central')
    s.step(fade(ilu))
    for g in ids:
        s.step(fade(g))
    s.step(zoom(c))
    s.meta['src'] = ['PA 1 Marco conceptual']


def codigo(D):
    s = nueva(D, 0, 'Código visual de la presentación', tipo='izq', c1=CREMA, c2=BLANCO)
    items = [
        (lambda s, x, y: ficha(s, x, y, 'Sustrato', 'F5B041', w=1.6, name='Ej sustrato'), 'Sustratos, productos y metabolitos: fichas redondeadas de color.'),
        (lambda s, x, y: enzima_globular(s, x + 0.2, y - 0.25, 1.1, 0.9, 'E59866', 'E', 'Ej enzima'), 'Enzimas: formas globulares sombreadas.'),
        (lambda s, x, y: rotulo(s, x, y, 'Biomarcador', NAVY, 14, w=1.6, name='Ej rótulo'), 'Biomarcadores y conceptos clave: rótulos azul marino.'),
        (lambda s, x, y: s.arrow([(x, y + 0.2), (x + 1.6, y + 0.2)], ACT, 3.5, name='Ej activa'), 'Flecha verde: activación / conversión.'),
        (lambda s, x, y: s.inhib([(x, y + 0.2), (x + 1.6, y + 0.2)], name='Ej inhibe'), 'Flecha roja con barra: inhibición.'),
        (lambda s, x, y: caja(s, x, y - 0.1, 1.6, 0.6, '', 'EAF2F8', 12, name='Ej rigor'), '«Nota de rigor»: precisiones de la revisión científica, distinguidas del contenido base.'),
    ]
    ids = []
    for i, (fn, t) in enumerate(items):
        y = 1.35 + i * 0.98
        g = s.group_start('Código %d' % (i + 1))
        fn(s, 0.7, y)
        caja(s, 2.9, y - 0.15, 6.0, 0.8, t, BLANCO, 16, anchor='m')
        s.group_end(); ids.append(g)
    mo = s.group_start('Moléculas decorativas')
    molecula3d(s, 9.5, 1.0, 2.6, 'glucosa', name='Molécula glucosa')
    molecula3d(s, 10.3, 3.7, 2.2, 'acetil', name='Molécula acetilo', rot=-15)
    s.group_end()
    m = caja(s, 9.3, 6.0, 3.8, 1.15, 'Los objetos con prefijo **!!** se conservan entre diapositivas para la transición **Morph**.', AMA, 13.5, name='Nota morph')
    for g in ids:
        s.step(fade(g))
    s.step(fade(m))


def build(D):
    portada(D)
    mapa(D)
    hilo(D)
    codigo(D)
