# -*- coding: utf-8 -*-
"""Genera BIOQUIMICA_CLINICA_Y_METABOLISMO.pptx y los entregables derivados
(mapa Morph, guion de animaciones, índice académico)."""
import sys, importlib, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'BIOQUIMICA_CLINICA_Y_METABOLISMO.pptx')
MODS = sys.argv[2].split(',') if len(sys.argv) > 2 else ['u0', 'u1', 'u1b', 'u2', 'u2b', 'u2c', 'u3', 'u3b', 'u4', 'u4b', 'u5', 'u5b', 'u6']

D = Deck()
for m in MODS:
    importlib.import_module(m).build(D)
for i, s in enumerate(D.slides):
    if i > 0:
        pagenum(s, i + 1)
D.save(OUT)
print('diapositivas:', len(D.slides), D.stats)
for w in WARN:
    print('AVISO', w)

if len(sys.argv) > 2:
    sys.exit(0)

# ---------------------------------------------------------------- entregables derivados
EF = {'appear': 'Aparecer', 'fade': 'Desvanecer', 'zoom': 'Zoom', 'grow': 'Zoom', 'path': 'Trayectoria de movimiento',
      'out': 'Salida: Desvanecer', 'outnow': 'Salida: Desaparecer', 'pulse': 'Énfasis: Aumentar/Encoger (pulso)',
      'spin': 'Énfasis: Girar', 'color': 'Énfasis: Color de relleno', 'float': 'Flotar hacia dentro'}
DIR = {'l': 'desde la izquierda', 'r': 'desde la derecha', 't': 'desde arriba', 'b': 'desde abajo'}
rows = []
for n, s in enumerate(D.slides, 1):
    for c, st in enumerate(s.anim, 1):
        for k, e in enumerate(st):
            trig = 'Al hacer clic' if k == 0 else ('Después de la anterior' if e['after'] else 'Con la anterior')
            ef = EF.get(e['kind'], e['kind']) if e['kind'] != 'wipe' else 'Barrido ' + DIR[e['dir']]
            if e['kind'] == 'path':
                ef += ' (Δx %.2f", Δy %.2f")' % (e['dx'], e['dy'])
            rows.append((n, c, s.sidname.get(e['sid'], str(e['sid'])), ef, '%.1f s' % (e['dur'] / 1000), trig))
with open(os.path.join(ROOT, 'ENTREGABLE_4_GUION_ANIMACIONES.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Diapositiva', 'Clic (orden)', 'Objeto (Panel de selección)', 'Efecto', 'Duración', 'Disparador'])
    w.writerows(rows)
with open(os.path.join(ROOT, 'ENTREGABLE_4_GUION_ANIMACIONES.md'), 'w', encoding='utf-8') as f:
    f.write('# Entregable 4 — Guion de animaciones internas\n\n')
    f.write('Animaciones **nativas** guardadas en cada diapositiva (`p:timing`). Total: %d efectos en %d diapositivas.\n\n'
            % (len(rows), len({r[0] for r in rows})))
    f.write('Columnas: diapositiva · clic en que se dispara · nombre del objeto tal como figura en *Inicio → Organizar → Panel de selección* · efecto · duración · disparador.\n'
            'La tabla completa (filtrable) está en `ENTREGABLE_4_GUION_ANIMACIONES.csv`.\n\n')
    last = None
    for r in rows:
        if r[0] != last:
            f.write('\n## Diapositiva %d — %s\n\n| Clic | Objeto | Efecto | Duración | Disparador |\n|---|---|---|---|---|\n'
                    % (r[0], D.slides[r[0] - 1].meta.get('titulo', '')))
            last = r[0]
        f.write('| %d | %s | %s | %s | %s |\n' % (r[1], r[2].replace('|', '/'), r[3], r[4], r[5]))

with open(os.path.join(ROOT, 'ENTREGABLE_3_MAPA_MORPH.md'), 'w', encoding='utf-8') as f:
    f.write('# Entregable 3 — Mapa de secuencias Morph\n\n')
    f.write('Cada secuencia fue construida duplicando la diapositiva anterior: los objetos conservan **el mismo nombre** (prefijo `!!`, '
            'coincidencia forzada de Morph) y solo cambian posición, escala, rotación o color; los objetos nuevos se agregan encima.\n\n')
    f.write('La transición **Transformación (Morph)** ya quedó aplicada en la segunda y siguientes diapositivas de cada secuencia, con respaldo '
            '«Desvanecer» para versiones de PowerPoint sin Morph. Si preferís aplicarla manualmente, seleccioná esas diapositivas → *Transiciones → Transformación → Opciones: Objetos*.\n\n')
    f.write('| # | Diapositivas | Mecanismo | Objetos conservados (`!!`) | Transformaciones previstas |\n|---|---|---|---|---|\n')
    for i, m in enumerate(REG['morph'], 1):
        f.write('| %d | %d → %d | %s | %s | %s |\n' % (i, m['ini'], m['fin'], m['mec'], ', '.join('`%s`' % o for o in m['obj']), m['trans']))

DOCS = {'VB': 'Apunte — Variables Bioquímicas', 'TM': 'Apunte — Termodinámica y Metabolismo Intermedio, PDH', 'AN': 'Apunte — Anemia',
        'IAM': 'Apunte — IAM', 'PA': 'Apunte — Pancreatitis Aguda (Abdomen agudo)', 'REV': 'Revisión científica (complemento señalado)'}
idx = {}
for n, s in enumerate(D.slides, 1):
    for ref in s.meta.get('src', []):
        doc, _, sec = ref.partition(' ')
        idx.setdefault(doc, {}).setdefault(sec, []).append(n)
def rng(lst):
    out = []; a = b = None
    for v in sorted(set(lst)):
        if a is None:
            a = b = v
        elif v == b + 1:
            b = v
        else:
            out.append('%d' % a if a == b else '%d–%d' % (a, b)); a = b = v
    if a is not None:
        out.append('%d' % a if a == b else '%d–%d' % (a, b))
    return ', '.join(out)
def seckey(sec):
    import re
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', sec)]
with open(os.path.join(ROOT, 'ENTREGABLE_5_INDICE_ACADEMICO.md'), 'w', encoding='utf-8') as f:
    f.write('# Entregable 5 — Índice académico\n\nCorrespondencia entre cada apartado de los cinco apuntes y las diapositivas que lo desarrollan.\n\n')
    for doc in ('VB', 'TM', 'AN', 'IAM', 'PA', 'REV'):
        if doc not in idx:
            continue
        f.write('\n## %s\n\n| Apartado | Diapositivas |\n|---|---|\n' % DOCS[doc])
        for sec in sorted(idx[doc], key=seckey):
            f.write('| %s | %s |\n' % (sec.replace('_', ' '), rng(idx[doc][sec])))
    f.write('\n## Lista de diapositivas\n\n| N.º | Unidad | Título |\n|---|---|---|\n')
    for n, s in enumerate(D.slides, 1):
        f.write('| %d | %s | %s |\n' % (n, UNIT[s.meta.get('unit', 0)][0], s.meta.get('titulo', '')))
print('entregables escritos')
