# -*- coding: utf-8 -*-
"""Integración final entre las cinco unidades y cierre."""
from plantillas import *


def integracion_b(D):
    s = nueva(D, 0, 'Integración B: metabolismo y daño celular', src=['VB 1.2 C Enzimas', 'PA 1.1 Mecanismo general de liberación', 'IAM 5.1 Regla de oro', 'AN 8.1 LDH'],
              tipo='bandas', c1=CELESTE, c2=AMA)
    pasos = [('Actividad enzimática normal', 'Las enzimas catalizan reacciones dentro de la célula (CK, LDH, transaminasas, enzimas pancreáticas).', 'cel', VERDE_CL),
             ('Alteración del tejido', 'Isquemia (IAM), autodigestión (pancreatitis), hemólisis (anemia), lesión hepática.', 'les', SALM),
             ('Liberación de marcadores', 'Pérdida de permeabilidad → moléculas citoplasmáticas; necrosis → también estructurales y mitocondriales.', 'lib', AMA),
             ('Aumento en sangre', 'La concentración o actividad sérica sube con una **cinética** propia de cada marcador.', 'cur', LAVANDA)]
    ids = []
    for k, (t, d, kind, f) in enumerate(pasos):
        x = 0.45 + k * 3.2
        g = s.group_start('Integración B %d' % (k + 1))
        if kind == 'cel':
            hepatocyte(s, x + 0.55, 1.2, 1.9, name='Hep B')
        elif kind == 'les':
            cardiomiocito(s, x + 0.1, 1.4, 2.8, 1.2, name='Cel B', detalle=False)
            s.shape(x + 1.2, 1.9, 0.6, 0.6, 'irregularSeal1', ('a', '4A235A', 70), None, False)
        elif kind == 'lib':
            for j, (m, c) in enumerate((('CK', 'F39C12'), ('ALT', '2E86C1'), ('LDH', 'E59866'), ('Lipasa', 'C0560E'))):
                ficha(s, x + 0.15 + (j % 2) * 1.4, 1.45 + (j // 2) * 0.6, m, c, w=1.25, h=0.42, size=12)
        else:
            curva(s, x + 0.1, 1.2, 2.8, 1.6, [(0, 900), (150, 880), (300, 150), (600, 600), (1000, 880)], '7D3C98', 3.5, name='Curva B')
        caja(s, x, 3.15, 3.0, 2.5, '**%s**\n%s' % (t, d), f, 14)
        if k < 3:
            s.arrow([(x + 3.02, 4.4), (x + 3.18, 4.4)], INK, 3)
        ids.append(s.group_end())
    c = caja(s, 0.45, 5.9, 12.45, 1.15, 'El mismo razonamiento sirve para el **corazón**, el **hígado**, el **páncreas** y la **sangre**: qué enzima, de qué compartimiento, cuánto y **cuándo**.', NAVY, 15.5,
             anchor='m', name='Síntesis B')
    for g in ids:
        s.step(fade(g))
    s.step(zoom(c))


def mapa_final(D):
    s = nueva(D, 0, 'Mapa integrador de la clase', src=['VB 1 Variables bioquímicas', 'TM 10 Complejo PDH', 'AN 12 Cuadro resumen', 'IAM 9 Tabla comparativa', 'PA 7 Tabla maestra'],
              tipo='der', c1=AMA, c2=BLANCO)
    cx, cy = 4.6, 4.1
    centro = s.shape(cx - 1.5, cy - 0.75, 3.0, 1.5, 'ellipse', shade(NAVY, 0.25, 0.3), (INK, 2.0), SH_I, 'LABORATORIO\nINTERPRETADO', 16, F_HEAD, BLANCO, True, 'c', 'm', name='Centro mapa')
    nodos = [('I · Variables', 'muestra, unidad, S/E, referencia, calidad', CELESTE, -150), ('II · Metabolismo', 'ΔG, redox, acetil-CoA, PDH', VERDE_CL, -90),
             ('III · Anemias', 'Hb, índices, reticulocitos, B_{12}', SALM, -30), ('IV · IAM', 'troponina, CK-MB, cinética', AZUL_M, 30),
             ('V · Hepatopancreático', 'ALT/AST, FAL/GGT, amilasa/lipasa', DURAZNO, 150), ('Integración', 'enzima → lesión → sangre → tiempo', LAVANDA, 90)]
    ids = []
    for k, (t, d, f, ang) in enumerate(nodos):
        a = math.radians(ang)
        x = cx + 3.2 * math.cos(a) - 1.35; y = cy + 2.35 * math.sin(a) - 0.6
        g = s.group_start('Nodo ' + t)
        s.arrow([(cx + 1.5 * math.cos(a), cy + 0.75 * math.sin(a)), (cx + 2.5 * math.cos(a), cy + 1.75 * math.sin(a))], INK, 2.5)
        caja(s, x, y, 2.7, 1.2, '**%s**\n%s' % (t, d), f, 12.5, anchor='m', align='c', minsize=10)
        ids.append(s.group_end())
    deco = s.group_start('Deco mapa')
    corazon_anat(s, 9.6, 1.2, 1.5, name='c'); liver(s, 11.2, 1.5, 1.7, name='h'); eritrocito(s, 9.7, 3.0, 1.1, name='e'); pancreas(s, 10.9, 3.2, 2.0, name='p')
    mitocondria_grande(s, 9.6, 4.4, 3.3, 1.6, name='m')
    tubo(s, 12.4, 4.6, 0.45, 1.8, [(0.45, 'B3261E', 'r'), (0.35, 'F7DC6F', 'p')], tapa='8E44AD', name='t')
    s.group_end()
    s.step(zoom(centro), fade(deco, after=True))
    for g in ids:
        s.step(fade(g))


def cierre(D):
    s = D.new(BLANCO)
    s.unit = 0; s.morph = False
    s.shape(0, 0, 5.2, SH, 'rect', AMA, None, False, name='Fondo panel')
    s.shape(10.4, 0, SW - 10.4, SH, 'rect', CELESTE, None, False, name='Fondo panel der')
    corazon_anat(s, 0.5, 0.9, 3.0, name='Corazón cierre')
    pancreas(s, 0.3, 5.3, 3.4, name='Páncreas cierre')
    molecula3d(s, 10.6, 0.8, 2.4, 'acetil', name='Acetilo cierre')
    for i, (xx, yy, d) in enumerate(((10.8, 3.6, 1.2), (11.9, 4.6, 1.0), (10.9, 5.6, 0.9))):
        eritrocito(s, xx, yy, d, name='GR cierre %d' % i)
    t = s.shape(5.0, 1.4, 5.6, 2.6, 'rect', None, None, False, 'DE LA MOLÉCULA AL DIAGNÓSTICO', 40, F_TITLE, TBLUE, True, 'c', 'm', (0, 0, 0, 0), name='Título cierre',
                reff=GLOW_W, lnspc=0.88, minsize=24)
    sub = caja(s, 5.3, 4.3, 5.0, 2.3, 'Cada valor de laboratorio cuenta una historia molecular: **dónde estaba** la molécula, **qué la liberó** y **cuándo** llegó a la sangre.', BLANCO, 16,
               name='Mensaje final')
    s.meta = {'titulo': 'CIERRE', 'unit': 0, 'src': []}
    s.step(fade(t))
    s.step(fade(sub))


def build(D):
    integracion_b(D)
    mapa_final(D)
    cierre(D)
