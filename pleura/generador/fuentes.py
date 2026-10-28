# -*- coding: utf-8 -*-
"""Preparación de la fuente manuscrita Mali (SIL OFL 1.1, sin nombre reservado).

1. Métricas verticales unificadas. La Mali original declara usWinAscent/usWinDescent
   enormes (1523/599, para cubrir los diacríticos apilados del tailandés), mientras que
   hhea y OS/2 typo dan 1050/250. Microsoft Office en Windows puede usar los valores
   «Win» para el interlineado, lo que produce líneas de 2,12 em en PowerPoint y 1,3 em
   en otros programas. Se igualan los tres juegos a 1050/270 (cubren todos los glifos
   latinos usados: +963/−264), de modo que el interlineado es el mismo en todas partes.
2. Conversión a EOT (Embedded OpenType, versión 0x00020001, sin compresión), que es el
   formato que PowerPoint escribe y lee en ppt/fonts/*.fntdata.
"""
import os, struct, io
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'fuentes', 'originales')
DST = os.path.join(HERE, 'fuentes')
FILES = ('Mali-Regular.ttf', 'Mali-Bold.ttf')
ASC, DESC = 1050, 270


def prepare():
    """escribe fuentes/Mali-*.ttf con métricas verticales unificadas (idempotente)"""
    for fn in FILES:
        out = os.path.join(DST, fn)
        if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(__file__):
            continue
        t = TTFont(os.path.join(SRC, fn))
        os2 = t['OS/2']; hh = t['hhea']
        os2.usWinAscent, os2.usWinDescent = ASC, DESC
        os2.sTypoAscender, os2.sTypoDescender, os2.sTypoLineGap = ASC, -DESC, 0
        os2.fsSelection |= 1 << 7          # USE_TYPO_METRICS
        hh.ascent, hh.descent, hh.lineGap = ASC, -DESC, 0
        name = t['name']
        for rec in name.names:
            if rec.nameID == 5:
                rec.string = str(rec.toUnicode()) + '; vertical metrics unified (1050/270)'
        t.save(out)


def _name(t, nid):
    n = t['name'].getName(nid, 3, 1, 0x409) or t['name'].getName(nid, 1, 0, 0)
    return (n.toUnicode() if n else '').encode('utf-16-le')


def to_eot(path):
    """TTF -> EOT 0x00020001 sin compresión ni cifrado (Flags = 0)"""
    data = open(path, 'rb').read()
    t = TTFont(io.BytesIO(data))
    os2 = t['OS/2']; head = t['head']
    p = os2.panose
    panose = bytes([p.bFamilyType, p.bSerifStyle, p.bWeight, p.bProportion, p.bContrast, p.bStrokeVariation,
                    p.bArmStyle, p.bLetterForm, p.bMidline, p.bXHeight])
    fixed = struct.pack('<IIII', 0, len(data), 0x00020001, 0)          # EOTSize se completa al final
    fixed += panose
    fixed += struct.pack('<BBIHH', 1, 1 if os2.fsSelection & 1 else 0, os2.usWeightClass, os2.fsType, 0x504C)
    fixed += struct.pack('<IIII', os2.ulUnicodeRange1, os2.ulUnicodeRange2, os2.ulUnicodeRange3, os2.ulUnicodeRange4)
    fixed += struct.pack('<II', getattr(os2, 'ulCodePageRange1', 0), getattr(os2, 'ulCodePageRange2', 0))
    fixed += struct.pack('<I', head.checkSumAdjustment & 0xFFFFFFFF)
    fixed += struct.pack('<IIII', 0, 0, 0, 0)
    var = b''
    for nid in (1, 2, 5, 4):                                              # familia, estilo, versión, nombre completo
        s = _name(t, nid)
        var += struct.pack('<HH', 0, len(s)) + s
    var += struct.pack('<HH', 0, 0)                                       # Padding5 + RootStringSize = 0
    eot = bytearray(fixed + var + data)
    struct.pack_into('<I', eot, 0, len(eot))
    return bytes(eot)


def panose_hex(path):
    p = TTFont(path)['OS/2'].panose
    return ''.join('%02X' % v for v in (p.bFamilyType, p.bSerifStyle, p.bWeight, p.bProportion, p.bContrast,
                                        p.bStrokeVariation, p.bArmStyle, p.bLetterForm, p.bMidline, p.bXHeight))


if __name__ == '__main__':
    prepare()
    for fn in FILES:
        e = to_eot(os.path.join(DST, fn))
        print(fn, 'EOT', len(e), 'bytes')
