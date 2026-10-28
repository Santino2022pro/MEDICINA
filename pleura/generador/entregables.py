# -*- coding: utf-8 -*-
"""Entregables 3, 4 y 5 generados desde el propio mazo (mapa de Morph, guion
de animaciones e índice académico). La auditoría científica (entregable 6)
es un documento redactado aparte."""
import os, csv
from base import MORPHMAP, UNITS

SECC = {
    'T1.1': 'Testut 1.1 · La pleura y sus capas', 'T1.2': 'Testut 1.2 · Composición normal del líquido pleural',
    'T2.1': 'Testut 2.1 · Definición de derrame', 'T2.2': 'Testut 2.2 · Mecanismos (Starling)', 'T2.3': 'Testut 2.3 · Trasudado vs. exudado',
    'T2.4': 'Testut 2.4 · Causas por tipo de derrame', 'T3.1': 'Testut 3.1 · Síntomas según el grado', 'T3.2': 'Testut 3.2 · Examen físico del derrame',
    'T3.3': 'Testut 3.3 · Radiografía y TAC', 'T4.1': 'Testut 4.1 · Toracocentesis', 'T4.2': 'Testut 4.2 · Criterios de Light',
    'T4.3': 'Testut 4.3 · Características macroscópicas', 'T4.4': 'Testut 4.4 · Otros parámetros del líquido', 'T5.1': 'Testut 5.1 · Paraneumónico y empiema',
    'T5.2': 'Testut 5.2 · Derrame maligno', 'T6.1': 'Testut 6.1 · Definición de neumotórax', 'T6.2': 'Testut 6.2 · Clasificación etiológica',
    'T6.3': 'Testut 6.3 · Clínica (normotensivo y a tensión)', 'T6.4': 'Testut 6.4 · Examen físico comparado', 'T6.5': 'Testut 6.5 · Imágenes del neumotórax',
    'T7.1': 'Testut 7.1 · Tratamiento según el grado', 'T7.2': 'Testut 7.2 · Protocolo de emergencia (tensión)', 'T7.3': 'Testut 7.3 · Trampa de agua',
    'T8.1': 'Testut 8.1 · Clasificación de tumores', 'T8.2': 'Testut 8.2 · Mesotelioma', 'T8.3': 'Testut 8.3 · Metástasis («suelta de globos»)',
    'T8.4': 'Testut 8.4 · Tumor fibroso solitario', 'T9.1': 'Testut 9.1 · Derrame vs. neumotórax', 'T9.2': 'Testut 9.2 · Trasudado vs. exudado (resumen)',
    'T9.3': 'Testut 9.3 · Datos clave',
    'P1.1': 'Picone 1.1 · Concepto de síndrome', 'P2.1': 'Picone 2.1 · Funciones de la pleura', 'P2.2': 'Picone 2.2 · Tres mecanismos (Starling)',
    'P2.3': 'Picone 2.3 · Cascada fisiopatológica del derrame', 'P2.4': 'Picone 2.4 · Síndrome nefrótico e hipercoagulabilidad',
    'P2.5': 'Picone 2.5 · Factores sistémicos vs. locales', 'P2.6': 'Picone 2.6 · Etiologías puntuales (ICC, pericarditis, cirrosis, nefrótico, neoplasias)',
    'P2.7': 'Picone 2.7 · Frémito', 'P2.8': 'Picone 2.8 · Matidez: diferencial', 'P2.9': 'Picone 2.9 · Dificultad respiratoria: niveles',
    'P2.10': 'Picone 2.10 · Tabla trasudado/exudado ampliada', 'P2.11': 'Picone 2.11 · Criterios de Light', 'P2.12': 'Picone 2.12 · Estudios del líquido',
    'P2.13': 'Picone 2.13 · Gérmenes', 'P2.14': 'Picone 2.14 · Paraneumónico complicado y empiema', 'P2.15': 'Picone 2.15 · Cuándo realizar toracocentesis',
    'P2.16': 'Picone 2.16 · Iatrogenia', 'P3.1': 'Picone 3.1 · Definición de neumotórax', 'P3.2': 'Picone 3.2 · Cuadro clínico',
    'P3.3': 'Picone 3.3 · Semiología del neumotórax', 'P3.4': 'Picone 3.4 · Estabilidad hemodinámica', 'P3.5': 'Picone 3.5 · Clasificación',
    'P3.6': 'Picone 3.6 · Principio de la ecografía', 'P3.7': 'Picone 3.7 · Signos ecográficos', 'P3.8': 'Picone 3.8 · Orden de lectura de la Rx',
    'P3.9': 'Picone 3.9 · Hallazgos radiológicos', 'P3.10': 'Picone 3.10 · Neumotórax vs. atelectasia', 'P3.11': 'Picone 3.11 · Tamaño (ACCP/BTS)',
    'P3.12': 'Picone 3.12 · TAC', 'P3.13': 'Picone 3.13 · Drenaje torácico', 'P3.14': 'Picone 3.14 · Tensión y shock obstructivo',
    'P3.15': 'Picone 3.15 · Neumopericardio', 'P4.1': 'Picone 4.1 · Cadena diagnóstica'}


def rng(nums):
    nums = sorted(set(nums)); out = []; a = b = None
    for n in nums:
        if a is None:
            a = b = n
        elif n == b + 1:
            b = n
        else:
            out.append((a, b)); a = b = n
    if a is not None:
        out.append((a, b))
    return ', '.join(('%d' % x) if x == y else ('%d–%d' % (x, y)) for x, y in out)


def write(D, outdir):
    # mapa de Morph
    L = ['# Mapa de Morph — ENFERMEDADES_PLEURALES_ANIMADA.pptx', '',
         'Cada intervalo es una escena continua: las diapositivas consecutivas comparten objetos con el **mismo nombre** (prefijo `!!` en el Panel de selección), '
         'de modo que Morph los interpola. La transición Morph ya viene aplicada a la 2.ª y siguientes diapositivas de cada intervalo (con respaldo «Desvanecer» '
         'para versiones sin Morph); puede quitarse o cambiarse desde *Transiciones*.', '',
         '| # | Diapositivas | Mecanismo | Objetos reutilizados | Transformación visual esperada |', '|---|---|---|---|---|']
    for i, (a, b, m, o, t) in enumerate(MORPHMAP, 1):
        L.append('| %d | %d–%d | %s | %s | %s |' % (i, a, b, m, o.replace('|', '/'), t))
    L += ['', 'Total de secuencias: %d · diapositivas con transición Morph: %d.' % (len(MORPHMAP), D.stats['morph'])]
    open(os.path.join(outdir, 'MAPA_MORPH.md'), 'w').write('\n'.join(L) + '\n')
    # guion de animaciones
    rows = D.anim_log()
    with open(os.path.join(outdir, 'GUION_ANIMACIONES.csv'), 'w', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['Diapositiva', 'Orden (clic)', 'Objeto', 'Efecto', 'Duración (ms)', 'Disparador'])
        for r in rows:
            w.writerow(r)
    L = ['# Guion de animaciones — ENFERMEDADES_PLEURALES_ANIMADA.pptx', '',
         'Todas las animaciones están **configuradas de forma nativa** en el archivo (nodo `p:timing` de cada diapositiva). Esta tabla las lista tal como '
         'PowerPoint las muestra en el *Panel de animación*: «Orden» es el número de clic; dentro de cada clic, los efectos «Con la anterior» y '
         '«Después de la anterior» completan la secuencia automática. La misma tabla está en `GUION_ANIMACIONES.csv` (separador «;»).', '',
         'Efectos: %d · diapositivas animadas: %d.' % (len(rows), D.stats['anim_slides']), '',
         '| Diap. | Clic | Objeto | Efecto | Duración (ms) | Disparador |', '|---|---|---|---|---|---|']
    for r in rows:
        L.append('| %d | %d | %s | %s | %d | %s |' % (r[0], r[1], r[2].replace('|', '/'), r[3], r[4], r[5]))
    open(os.path.join(outdir, 'GUION_ANIMACIONES.md'), 'w').write('\n'.join(L) + '\n')
    # índice académico
    idx = {}
    for n, s in enumerate(D.slides, 1):
        for k in getattr(s, 'src', []):
            idx.setdefault(k, []).append(n)
    L = ['# Índice académico — correspondencia entre los apuntes y las diapositivas', '',
         '## Unidades de la presentación', '', '| Unidad | Diapositivas | Título |', '|---|---|---|']
    order = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX']
    for u in order:
        if u in UNITS:
            a, b, t = UNITS[u]
            L.append('| %s | %d–%d | %s |' % (u, a, b, t))
    for pref, titulo in (('T', 'PLEURA TESTUT.pdf'), ('P', 'Apunte — Enfermedades de la Pleura (Picone)')):
        L += ['', '## ' + titulo, '', '| Apartado | Diapositivas |', '|---|---|']
        keys = sorted([k for k in SECC if k.startswith(pref)], key=lambda k: [int(x) for x in k[1:].split('.')])
        for k in keys:
            L.append('| %s | %s |' % (SECC[k], rng(idx[k]) if k in idx else '— (ver nota)'))
    L += ['', '### Apartados no convertidos en diapositivas', '',
          '- Picone 1.2–1.3 y 4.2–4.4 (debate con la inteligencia artificial, frases textuales, organización de la cátedra): su contenido médico se integró '
          'en las diapositivas correspondientes (funciones de la pleura, «no existe el cuadro puro», «nunca la imagen sola», vigilancia del paciente) sin '
          'referencias al docente, a la clase ni a la IA.',
          '- Testut 2.1 (definición de derrame) se desarrolla en la Unidad II (paso 10 de Starling) y en la Unidad III.']
    open(os.path.join(outdir, 'INDICE_ACADEMICO.md'), 'w').write('\n'.join(L) + '\n')
