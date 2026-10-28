# -*- coding: utf-8 -*-
"""Plantillas de diapositiva reutilizadas en todas las unidades."""
from dibujos import *


def divisor(D, unit, roman, text, sub, temas, arte, src=(), notas=''):
    """separador de unidad: título manuscrito gigante + temario + gran ilustración"""
    s = D.new(BLANCO)
    s.unit = unit; s.morph = False
    f = UNIT[unit][1]
    s.set_bg(BLANCO)
    s.shape(0, 0, 6.6, SH, 'rect', f, None, False, name='Fondo panel')
    s.shape(6.6, 0, SW - 6.6, SH, 'rect', CREMA, None, False, name='Fondo panel der')
    rotulo(s, 0.5, 0.45, 'UNIDAD ' + roman, NAVY, 20, name='Unidad')
    t = s.shape(0.4, 1.05, 6.0, 2.6, 'rect', None, None, False, smart_upper(text), 34, F_TITLE, TBLUE, True, 'l', 'm', (0, 0, 0, 0),
                name='Título unidad', minsize=22, reff=GLOW_W, lnspc=0.9)
    st = texto(s, 0.45, 3.7, 6.0, 0.6, sub, 18, INK, True, name='Subtítulo unidad')
    n = len(temas)
    if n > 6:
        h1 = (n + 1) // 2
        g = s.group_start('Temario')
        caja(s, 0.45, 4.4, 2.95, 2.75, '\n'.join('- ' + t_ for t_ in temas[:h1]), BLANCO, 14, spc=3)
        caja(s, 3.5, 4.4, 2.95, 2.75, '\n'.join('- ' + t_ for t_ in temas[h1:]), BLANCO, 14, spc=3)
        tb = s.group_end()
    else:
        tb = caja(s, 0.45, 4.4, 6.0, 2.75, '\n'.join('- ' + t_ for t_ in temas), BLANCO, 16, spc=4, name='Temario')
    ids = arte(s)
    s.meta = {'titulo': plain(smart_upper(text)), 'unit': unit, 'src': list(src)}
    s.step(fade(tb))
    if notas:
        s.note(notas)
    return s


def caso_cabecera(s, x, y, w, edad, motivo, color=ROJO, name='!!Paciente'):
    """ficha de paciente (silueta + datos)"""
    g = s.group_start(name)
    caja(s, x, y, w, 1.55, '', BLANCO, 14, lw=2.0)
    person(s, x + 0.15, y + 0.12, 1.3, name='Silueta', fill='AEB6BF')
    texto(s, x + 1.35, y + 0.15, w - 1.5, 0.5, edad, 20, color, True, name='Edad y sexo')
    texto(s, x + 1.35, y + 0.65, w - 1.5, 0.85, motivo, 15, INK, False, name='Motivo')
    return s.group_end()


def signos_vitales(s, x, y, items, w=1.45, h=0.95, gap=0.12, name='Signos vitales'):
    """chips de signos vitales: items = [(etiqueta, valor, alterado)]; devuelve lista de ids"""
    ids = []
    for i, (lab, val, alt) in enumerate(items):
        xx = x + i * (w + gap)
        g = s.group_start('%s %s' % (name, plain(lab)))
        s.shape(xx, y, w, h, 'roundRect', ROSA if alt else 'EAF5EA', (ROJO if alt else VERDE_OSC, 1.75), False, adj={'adj': 14000})
        texto(s, xx, y + 0.06, w, 0.3, lab, 12, '5D6D7E', True, 'c')
        texto(s, xx, y + 0.36, w, 0.52, val, 18, ROJO if alt else VERDE_OSC, True, 'c', 'm', minsize=11)
        ids.append(s.group_end())
    return ids


def lab_tabla(s, x, y, colw, filas, size=14, head=('Parámetro', 'Paciente', 'Referencia', 'Lectura'), name='Laboratorio', rowh=0.4,
              alt_col=1):
    """tabla de laboratorio animable fila por fila; filas = [(param, valor, ref, lectura, alterado)]"""
    rows = [list(head)] + [[p, v, r, l] for (p, v, r, l, a) in filas]
    ids, H = tabla_filas(s, x, y, colw, rows, rowh=rowh, size=size, name=name)
    return ids, H


def conclusion(s, x, y, w, h, text, title='Conclusión', fill=VERDE_OSC, name='Conclusión', size=17):
    return caja(s, x, y, w, h, text, fill, size, head=title, headfill=AMA2, name=name)


def perla(s, x, y, w, h, text, size=15, name='Perla', head='Para recordar'):
    return caja(s, x, y, w, h, text, ROJO, size, head=head, headfill=AMA2, name=name)


def rigor(s, x, y, w, h, text, size=13.5, name='Nota de rigor'):
    """aclaración procedente de la revisión científica (visualmente distinguida del contenido base)"""
    return caja(s, x, y, w, h, text, 'EAF2F8', size, head='Nota de rigor', headfill='5B7DB1', name=name, lw=1.5)
