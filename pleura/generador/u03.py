# -*- coding: utf-8 -*-
"""UNIDAD IV (trasudado y exudado) y UNIDAD V (etiologías del derrame)."""
from base import *


def div4(D):
    def art(s):
        chest(s, 6.9, 0.7, 3.1, 3.0, {'fluidR': 0.3, 'fluidL': 0.25}, names=False)
        chest(s, 10.0, 0.7, 3.1, 3.0, {'fluidR': 0.45, 'exud': 1}, names=False)
        tube(s, 7.9, 4.1, 0.75, 2.5, 'F7E7A6', 'Trasudado', 'clear', fill=0.6)
        tube(s, 11.1, 4.1, 0.75, 2.5, 'E3B448', 'Exudado', 'turbid', fill=0.6)
    divider(D, 'IV', 'Trasudado y exudado', 'La gran división: ¿problema sistémico o pleura enferma?',
            ['Definiciones', 'Factores sistémicos y factores locales', 'Formación de un trasudado (paso a paso)',
             'Formación de un exudado (paso a paso)', 'Comparación lado a lado', 'Una clasificación que no es taxativa'], art,
            src=['T2.3', 'P2.5'])


def definiciones(D):
    s = new(D, 'Trasudado / exudado', 'Dos perfiles fisiopatológicos', 'torax', src=['T2.3', 'P2.5'])
    l = box(s, 0.4, 1.0, 6.1, 2.2, '**La pleura está SANA.** El problema es **sistémico**: presiones desbalanceadas (↑ hidrostática o '
            '↓ oncótica). El líquido «se escapa» sin que la membrana esté dañada.', C_FLUID, 15, name='Def trasudado', bold=False,
            head='Trasudado', headfill=WHITE)
    r = box(s, 6.85, 1.0, 6.1, 2.2, '**La pleura está ENFERMA.** El problema es **local**: ↑ permeabilidad (inflamación, infección, '
            'tumor) o bloqueo linfático. La pleura «deja pasar» más de lo normal.', C_EXUD, 15, name='Def exudado', bold=False,
            head='Exudado', headfill=WHITE)
    a = starling(s, 0.4, 3.4, 3.0, 3.5, {'show': {'pc', 'onc'}, 'pc': 1.8, 'acc': 0.3, 'drops': False})
    tl = tube(s, 3.75, 3.6, 0.8, 2.6, 'F7E7A6', 'Claro', 'clear', name='Tubo trasudado')
    lt = box(s, 4.85, 3.4, 1.65, 3.5, 'Poca proteína\nPoca LDH\nPocas células', WHITE, 14, name='Trasudado contenido')
    b = starling(s, 6.85, 3.4, 3.0, 3.5, {'show': {'pc', 'onc'}, 'perm': 1, 'acc': 0.3, 'prot': 14, 'wbc': 4, 'drops': False})
    tr = tube(s, 10.2, 3.6, 0.8, 2.6, 'E3B448', 'Turbio', 'turbid', name='Tubo exudado')
    rt = box(s, 11.3, 3.4, 1.65, 3.5, 'Más proteína\nMás LDH\nMás células', WHITE, 14, name='Exudado contenido')
    s.step(fade(l))
    s.step(fade(r))
    s.step(fade(tl), fade(lt, after=True))
    s.step(fade(tr), fade(rt, after=True))


def seq_trasudado(D):
    Q = Seq(D, 'Formación de un trasudado (Unidad IV)', '!!Capilar, !!Albumina, !!Intersticio, !!VasoLinfatico, flechas de fuerza, '
            '!!LiquidoAcumulado, !!Leyenda; luego tubo y tórax de referencia', 'Pc se engrosa (o π_c se adelgaza), aumenta el filtrado '
            'pobre en proteínas y sube el nivel del líquido; al final aparece el tubo claro.')
    allf = {'pc', 'onc', 'net', 'lym'}
    st = [({'show': allf}, 'Capilar normal', 'Fuerzas equilibradas; endotelio íntegro.'),
          ({'show': allf, 'pc': 2}, 'Modificación de fuerzas', '↑ P_{c} (insuficiencia cardíaca) o ↓ π_{c} (hipoalbuminemia).'),
          ({'show': allf, 'pc': 2, 'acc': 0.2}, 'Filtración de líquido', 'Sale **agua** con muy pocas proteínas: la barrera sigue intacta (σ ≈ 1).'),
          ({'show': allf, 'pc': 2, 'acc': 0.55}, 'Acumulación', 'El filtrado supera la reabsorción linfática: el volumen pleural crece.'),
          ({'show': allf, 'pc': 2, 'acc': 0.55}, 'Composición', 'Pocas proteínas · poca LDH · pocas células (predominio de macrófagos).'),
          ({'show': allf, 'pc': 2, 'acc': 0.55}, 'Aspecto macroscópico', 'Líquido **claro, seroso, transparente**.'),
          ({'show': allf, 'pc': 2, 'acc': 0.55}, 'Interpretación', 'Pleura sana + causa sistémica = **trasudado**. Criterios de Light negativos.')]
    for i, (sst, ttl, cap) in enumerate(st):
        s = new(D, 'Trasudado', ttl, 'azul', morph=i > 0, src=['T2.3', 'T9.2', 'P2.5'])
        A = starling(s, 0.3, 0.95, 7.6, 5.5, sst)
        step_badge(s, i + 1, len(st))
        lg = legend(s, cap, 0.3, 6.6, 7.6, h=0.62, size=14)
        if i < 4:
            txt = ['Endotelio íntegro, albúmina dentro del vaso y linfáticos permeables: el volumen pleural es mínimo.',
                   'La causa es **sistémica**: la pleura no está lesionada; cambian las **presiones**.',
                   'Como σ ≈ 1, el filtrado es **pobre en proteínas** y en células.',
                   'El nivel de líquido sube en ambos hemitórax: típico **bilateral**.'][i]
            cb = box(s, 8.2, 1.0, 4.8, 2.5, txt, [WHITE, ORANGE, GREEN, C_FLUID][i], 16, name='Explicación %d' % i, bold=False)
            ch = chest(s, 9.0, 3.7, 3.2, 3.2, {'fluidR': [0, 0, 0.1, 0.3][i], 'fluidL': [0, 0, 0.08, 0.27][i]})
            s.step(fade(cb))
        if i >= 4:
            rows = [['PARÁMETRO', 'TRASUDADO'], ['Proteínas', 'Bajas'], ['LDH', 'Baja'], ['Células', 'Pocas; macrófagos']]
            ids, h = gtable(s, 8.2, 1.0, 4.8, rows, [1, 1.3], 15, head_fill=C_FLUID, name='!!TablaTrasudado')
        if i >= 5:
            t = tube(s, 8.4, 3.3, 1.0, 3.0, 'F7E7A6', 'Claro, seroso', 'clear', name='!!TuboTrasudado')
            c = chest(s, 9.9, 3.3, 3.1, 3.0, {'fluidR': 0.3, 'fluidL': 0.25}, names=False)
        if i == 4:
            table_anim(s, ids, 3)
        if i == 5:
            s.step(fade(t))
        if i == 6:
            w = box(s, 8.2, 3.3, 4.8, 3.3, '**Trasudado**: pleura **sana**, causa **sistémica** (ICC, cirrosis, síndrome nefrótico, '
                    'hipoalbuminemia).\nLa respuesta se dirige a la **enfermedad de base**.', CEL, 15, name='Interpretación trasudado', bold=False)
            s.step(zoom(w))
        if i == 2:
            s.step(fade(A['drops']))
        if i == 3 and A.get('acc'):
            s.step(wipe(A['acc'], 'b', dur=900))
    Q.close()


def seq_exudado(D):
    Q = Seq(D, 'Formación de un exudado (Unidad IV)', '!!PleuraParietal, !!CapilarSistemico, !!VasoLinfatico, !!LiquidoPleural, '
            '!!Leucocitos, !!Proteinas, !!PleuraVisceral, !!Alveolos', 'La hoja parietal se inflama, el capilar se dilata, el espacio '
            'se ensancha con líquido turbio cargado de proteínas y células.')
    st = [({'gap': 0.06}, 'Tejido pleural', 'Corte de ambas hojas en condiciones normales.'),
          ({'gap': 0.06, 'inflam': 1}, 'Alteración local', '**Inflamación, infección o neoplasia** de la pleura.'),
          ({'gap': 0.06, 'inflam': 1, 'hl': {'CapilarSistemico'}}, 'Cambio vascular', 'El capilar se **dilata** y su endotelio se vuelve **permeable**.'),
          ({'gap': 0.3, 'inflam': 1, 'kind': 'exud', 'prot': 25, 'cells': 8}, 'Salida de componentes', 'Salen agua, **proteínas** y **células** inflamatorias.'),
          ({'gap': 0.62, 'inflam': 1, 'kind': 'exud', 'prot': 50, 'cells': 22, 'lymph': 'block'}, 'Acumulación', 'Si además se bloquean los linfáticos, el líquido se acumula aún más.'),
          ({'gap': 0.62, 'inflam': 1, 'kind': 'exud', 'prot': 50, 'cells': 22, 'lymph': 'block'}, 'Composición', '**Más proteínas · más LDH · más células** (PMN o linfocitos).'),
          ({'gap': 0.62, 'inflam': 1, 'kind': 'exud', 'prot': 50, 'cells': 22, 'lymph': 'block'}, 'Interpretación', 'Pleura enferma + causa local = **exudado**. Al menos un criterio de Light positivo.')]
    for i, (sst, ttl, cap) in enumerate(st):
        s = new(D, 'Exudado', ttl, 'azul', morph=i > 0, src=['T2.3', 'T9.2', 'P2.5'])
        A = pleura_zoom(s, 0.3, 0.95, 7.6, 5.55, sst)
        step_badge(s, i + 1, len(st))
        lg = legend(s, cap, 0.3, 6.6, 7.6, h=0.62, size=14)
        cs = []
        if i <= 4:
            txt = ['La hoja parietal (verde azulada) y la visceral (morada), separadas por una lámina mínima de líquido.',
                   'La lesión es **local**: la membrana ya no está sana.',
                   'Aumenta el coeficiente de filtración y cae el coeficiente de reflexión de proteínas (↑ K, ↓ σ).',
                   'Las proteínas (amarillas) y los leucocitos atraviesan la barrera.',
                   'El espacio pleural se transforma en una cavidad **real** ocupada por exudado.'][i]
            cs.append(box(s, 8.2, 1.0, 4.8, 3.0, txt, [WHITE, ORANGE, RED, C_EXUD, GOLD][i], 16, name='Explicación %d' % i, bold=False))
        if i <= 4:
            ch = chest(s, 9.05, 4.15, 3.1, 2.85, {'fluidR': [0, 0, 0, 0.25, 0.45][i], 'exud': 1})
        if i >= 5:
            rows = [['PARÁMETRO', 'EXUDADO'], ['Proteínas', 'Altas'], ['LDH', 'Alta'], ['Células', 'Muchas: PMN o linfocitos']]
            ids, h = gtable(s, 8.2, 1.0, 4.8, rows, [1, 1.3], 15, head_fill=C_EXUD, name='!!TablaExudado')
            t = tube(s, 8.5, 3.4, 1.0, 2.9, 'E3B448', 'Turbio (variable)', 'turbid', name='!!TuboExudado')
            if i == 5:
                table_anim(s, ids, 3)
                s.step(fade(t))
        if i == 6:
            w = box(s, 9.9, 3.3, 3.1, 3.2, '**Exudado**: buscar la **causa local** (infección, TBC, tumor, colagenopatía, pancreatitis…).',
                    CEL, 15, name='Interpretación exudado', bold=False)
            s.step(zoom(w))
        reveal(s, cs, 1)
    Q.close()


def comparacion(D):
    s = new(D, 'Trasudado / exudado', 'Dos pulmones, dos mecanismos', 'blanco', src=['T2.3', 'T9.2', 'P2.5'])
    a = chest(s, 0.2, 1.1, 3.5, 3.5, {'fluidR': 0.32, 'fluidL': 0.28})
    b = chest(s, 9.6, 1.1, 3.5, 3.5, {'fluidR': 0.5, 'exud': 1})
    tag(s, 0.45, 4.75, 'TRASUDADO · ICC', C_FLUID, 15, w=3.0)
    tag(s, 9.85, 4.75, 'EXUDADO · NEUMONÍA', C_EXUD, 15, w=3.0)
    rows = [('Mecanismo', '↑ P_{c} / ↓ π_{c}', '↑ permeabilidad / bloqueo linfático'),
            ('Pleura', 'Sana', 'Enferma'),
            ('Proteínas y LDH', 'Bajas', 'Altas'),
            ('Células', 'Pocas (macrófagos)', 'Muchas (PMN o linfocitos)'),
            ('Aspecto', 'Claro, seroso', 'Turbio, lechoso, hemorrágico o purulento'),
            ('Lateralidad típica', 'Bilateral', 'Según el foco')]
    ids = []
    for i, (k, l, r) in enumerate(rows):
        y = 1.0 + i * 0.95
        g = s.group_start('Comparación ' + k)
        box(s, 3.85, y, 1.85, 0.85, l, C_FLUID, 13, bold=False)
        box(s, 5.75, y, 1.85, 0.85, smart_upper(k), WHITE, 12)
        box(s, 7.65, y, 1.85, 0.85, r, C_EXUD, 12, bold=False)
        ids.append(s.group_end())
    w = box(s, 0.3, 5.75, 12.7, 1.2, 'Una causa sistémica puede generar un líquido **mixto**, y una pleura con trasudado no siempre es '
            '«absolutamente normal»: la clasificación es una **orientación**.', RED, 15, name='Advertencia comparación', bold=False)
    reveal(s, ids, 1)
    s.step(fade(w))


def no_taxativo(D):
    s = new(D, 'Trasudado / exudado', 'Factores sistémicos y factores locales', 'mesotelio', src=['P2.5', 'P2.10'])
    rows = [['TRASUDADO — FACTORES SISTÉMICOS', 'EXUDADO — FACTORES LOCALES'],
            ['Insuficiencia cardíaca congestiva', 'Infección pleural: pleuritis bacteriana'],
            ['Pericarditis constrictiva', 'Micobacterias (TBC): ADA elevada + linfocitosis'],
            ['Cirrosis hepática con hidrotórax hepático', 'Infecciones fúngicas y víricas'],
            ['Síndrome nefrótico', 'Neoplasias malignas'],
            ['Hipoalbuminemia de otras causas', 'Lesiones torácicas abiertas'],
            ['Entrada de líquido peritoneal (ascitis)', 'Vasculitis autoinmunes: lupus, Churg-Strauss'],
            ['Alteración de presión hidrostática u oncótica', 'Disminución del drenaje linfático local']]
    ids, h = gtable(s, 0.4, 1.0, 8.6, rows, [1, 1], 14.5, head_fill=[C_FLUID, C_EXUD], first_fill=None, first_bold=False, fill_to=6.95)
    k = box(s, 9.3, 1.0, 3.7, 3.1, '«Trasudado = sistémico» es la gran clasificación, **pero no es taxativa**. En grandes '
            'acumulaciones **siempre hay mezcla**.', GOLD, 15, name='Clave teórica', bold=False)
    l = box(s, 9.3, 4.3, 3.7, 2.65, 'El drenaje linfático aparece en la columna local, pero su razonamiento también encaja en lo '
            'sistémico: **no existe el cuadro puro**.', CEL, 14.5, name='Linfático ambas', bold=False)
    table_anim(s, ids, 2)
    s.step(fade(k))
    s.step(fade(l))
    s.note('Las neoplasias aparecen con mecanismos distintos según la etapa y el mecanismo dominante (Unidad V). La ubicación de '
           '«neoplasias avanzadas» como causa sistémica de trasudado en el material se registra para revisión.')


# ------------------------------------------------------------------ UNIDAD V
def div5(D):
    def art(s):
        chest(s, 6.9, 0.6, 3.2, 3.1, {'fluidR': 0.3, 'fluidL': 0.3, 'heart': -1}, names=False)
        abdomen(s, 10.1, 0.6, 3.0, 3.1, {'asc': 0.5, 'pfl': 0.4, 'defect': 1})
        glomerulus(s, 7.2, 3.9, 2.6, 2.6, {'leak': 16})
        chest(s, 10.1, 3.9, 3.0, 3.0, {'fluidR': 0.4, 'mass': (250, 300, 60)}, names=False)
    divider(D, 'V', 'Etiologías del derrame pleural', 'Del mecanismo a la causa',
            ['Causas de trasudado y de exudado', 'Las causas más frecuentes', 'Insuficiencia cardíaca · pericarditis constrictiva',
             'Hidrotórax hepático (secuencia)', 'Síndrome nefrótico, hipercoagulabilidad y TEP', 'Neoplasias, infecciones, autoinmunes y abdominales'],
            art, src=['T2.4', 'P2.6'])


def causas(D):
    s = new(D, 'Etiologías', 'Causas de trasudado', 'mesotelio', src=['T2.4', 'P2.5'])
    items = [('ICC', 'Principal causa de **trasudado**.', 'heart'), ('Hipoalbuminemia severa', 'Cae la presión oncótica.', 'alb'),
             ('Síndrome nefrótico · glomerulonefritis', 'Pérdida renal de proteínas.', 'kid'), ('Cirrosis con ascitis', 'Hidrotórax hepático.', 'liv'),
             ('Pericarditis constrictiva', 'Congestión sistémica.', 'heart'), ('Diálisis peritoneal', 'Paso de líquido peritoneal.', 'liv'),
             ('Otras causas', 'Sarcoidosis · posparto · cirugía de revascularización miocárdica (clasificación en revisión).', None),
             ('TEP', 'Puede dar **trasudado o exudado**.', 'emb')]
    ids = []
    for i, (h, t, ic) in enumerate(items):
        x = 0.4 + (i % 4) * 3.18; y = 1.0 + (i // 4) * 2.95
        g = s.group_start('Causa ' + h)
        box(s, x, y, 3.0, 2.75, t, C_FLUID if i < 7 else GOLD, 13.5, head=h, headfill=WHITE, bold=False, anchor='b', grow=False)
        if ic == 'heart':
            chest(s, x + 0.85, y + 0.5, 1.3, 1.25, {'heart': -1, 'fluidR': 0.2, 'fluidL': 0.2}, names=False)
        elif ic == 'kid':
            glomerulus(s, x + 0.95, y + 0.5, 1.1, 1.15, {'leak': 8})
        elif ic == 'liv':
            abdomen(s, x + 0.8, y + 0.5, 1.4, 1.2, {'asc': 0.6})
        elif ic == 'alb':
            starling(s, x + 0.75, y + 0.5, 1.5, 1.2, {'alb': 6, 'drops': False})
        elif ic == 'emb':
            chest(s, x + 0.85, y + 0.5, 1.3, 1.25, {'emb': 1}, names=False)
        ids.append(s.group_end())
    reveal(s, ids, 2)
    s = new(D, 'Etiologías', 'Causas de exudado', 'mesotelio', src=['T2.4', 'P2.5'])
    items = [('Neoplasias', 'Cáncer de **mama**, **pulmón**, **linfomas**; mesotelioma.', 'mass'),
             ('Infecciones', '**TBC** · neumonías bacterianas o virales (Mycoplasma, Pneumocystis) · hongos.', 'pneu'),
             ('TEP con infarto', 'Cuando produce **infarto pulmonar**.', 'emb'),
             ('Colagenopatías', '**Artritis reumatoidea** · **LES** · vasculitis (Churg-Strauss).', None),
             ('Intraabdominales', '**Absceso subfrénico** · **pancreatitis** (amilasa elevada en el líquido).', 'liv'),
             ('Postraumático', 'Lesión torácica abierta: entrada de líquido externo.', None),
             ('Idiopático', 'Sin causa identificada tras el estudio.', None),
             ('Linfático', '**Disminución del drenaje** local (metástasis).', None)]
    ids = []
    for i, (h, t, ic) in enumerate(items):
        x = 0.4 + (i % 4) * 3.18; y = 1.0 + (i // 4) * 2.95
        g = s.group_start('Causa ' + h)
        box(s, x, y, 3.0, 2.75, t, C_EXUD, 13 if ic else 14.5, head=h, headfill=WHITE, bold=False, anchor='b' if ic else 'm', grow=not ic)
        if ic == 'mass':
            chest(s, x + 0.85, y + 0.5, 1.3, 1.25, {'fluidR': 0.35, 'mass': (250, 300, 60), 'exud': 1}, names=False)
        elif ic == 'pneu':
            chest(s, x + 0.85, y + 0.5, 1.3, 1.25, {'fluidR': 0.3, 'exud': 1, 'lungcolR': 'C9575F'}, names=False)
        elif ic == 'emb':
            chest(s, x + 0.85, y + 0.5, 1.3, 1.25, {'emb': 1, 'fluidR': 0.2, 'exud': 1}, names=False)
        elif ic == 'liv':
            abdomen(s, x + 0.8, y + 0.5, 1.4, 1.2, {'asc': 0.3})
        ids.append(s.group_end())
    reveal(s, ids, 2)


def frecuentes(D):
    s = new(D, 'Etiologías', 'Las ocho causas más frecuentes de derrame', 'torax', src=['T2.4', 'T9.3'])
    items = [('Insuficiencia cardíaca congestiva', 'La más frecuente · trasudado bilateral y simétrico', C_FLUID),
             ('Neumonía', 'Derrame paraneumónico · exudado', C_EXUD), ('Enfermedades malignas', 'Metástasis, mesotelioma · exudado a menudo hemorrágico', C_EXUD),
             ('Tromboembolismo pulmonar', 'Trasudado o exudado', GOLD), ('Enfermedades virales', 'Exudado', C_EXUD),
             ('Cirrosis hepática', 'Hidrotórax hepático · trasudado', C_FLUID), ('Enfermedades del colágeno', 'LES, artritis reumatoidea · exudado', C_EXUD),
             ('Tuberculosis', 'Exudado linfocítico con ADA elevada', C_EXUD)]
    ids = []
    for i, (h, t, c) in enumerate(items):
        x = 0.4 + (i // 4) * 6.4; y = 1.0 + (i % 4) * 1.5
        g = s.group_start('Frecuente %d' % (i + 1))
        badge(s, x, y + 0.3, i + 1, 0.7)
        box(s, x + 0.85, y, 5.35, 1.35, '**%s**\n%s' % (h, t), c, 15, bold=False, align='l')
        ids.append(s.group_end())
    reveal(s, ids, 2)


def icc(D):
    s = new(D, 'Etiologías', 'Insuficiencia cardíaca congestiva', 'azul', src=['T4.4', 'P2.6', 'P2.15'])
    A = chest(s, 0.3, 0.95, 5.7, 5.6, {'fluidR': 0.3, 'fluidL': 0.27, 'heart': -1, 'hl': {'Corazon'}})
    tag(s, 1.6, 6.6, 'CARDIOMEGALIA + DERRAME BILATERAL', GOLD, 14)
    cs = [box(s, 6.3, 1.0, 3.25, 1.6, '~**40 %** de los derrames se asocian a ICC; ~**80 %** son **bilaterales**.', GOLD, 14.5, name='Cifras ICC', bold=False),
          box(s, 9.75, 1.0, 3.25, 1.6, 'Típico: **bilateral y simétrico**, **sin fiebre**, **trasudado**.', C_FLUID, 14.5, name='Típico ICC', bold=False),
          box(s, 6.3, 2.8, 3.25, 1.75, 'La **cardiomegalia** en la radiografía **apoya** el diagnóstico, pero **no es obligatoria** para el trasudado.',
              WHITE, 14, name='Cardiomegalia', bold=False),
          box(s, 9.75, 2.8, 3.25, 1.75, 'Puede producir **exudados**, sobre todo tras **diuresis intensiva** o prolongada.', ORANGE, 14,
              name='Pseudoexudado', bold=False),
          box(s, 6.3, 4.75, 3.25, 2.2, 'Tiempo de respuesta a **diuréticos**: se citan **72 h** y **75 % en 48 h** → dato **en revisión**.', RED, 13.5, name='Discrepancia diuréticos', bold=False),
          box(s, 9.75, 4.75, 3.25, 2.2, 'Si es **unilateral, asimétrico**, con **fiebre** o **no responde** → sospechar otra causa y realizar '
              '**toracocentesis**.', CEL, 13.5, name='Cuándo dudar', bold=False)]
    reveal(s, cs, 1)
    s.note('El material también propone medir BNP en el líquido pleural con un umbral de 1500 pg/ml y sensibilidad y especificidad '
           'superiores al 90 %. El marcador pleural validado en la literatura es el NT-proBNP; el dato se registra para revisión '
           'antes de enseñarlo como regla.')
    s = new(D, 'Etiologías', 'Pericarditis constrictiva', 'azul', src=['P2.6'])
    A = chest(s, 0.3, 0.95, 5.7, 5.6, {'fluidR': 0.22, 'fluidL': 0.2, 'peric': 1})
    co = callout(s, [A['heart'], (6.4, 1.3)], 'Pericardio engrosado y calcificado', 6.4, 1.0, 3.6, 0.6, '#D5D8DC'[1:], 14)
    cs = two_cards(s, [('Mecanismo', 'El pericardio rígido impide el llenado → **congestión sistémica** → ↑ presión hidrostática.', GREEN),
                       ('Líquido', 'Produce **trasudado**.', C_FLUID),
                       ('Examen físico', 'Dato específico: **golpe (knock) pericárdico**.', TURQ),
                       ('Imágenes', '**Calcificaciones** pericárdicas y **engrosamiento** del pericardio.', LBLUE)], 6.4, 1.8, 6.6, 5.15, 0.15, 14.5)
    s.step(fade(co))
    reveal(s, cs, 1)


def hidrotorax(D):
    Q = Seq(D, 'Hidrotórax hepático: de la ascitis al espacio pleural (Unidad V)', '!!Higado, !!Ascitis, !!Diafragma, !!Intestino, '
            '!!LiquidoPleuralD, !!PulmonDerecho, !!PleuraParietalD, !!Leyenda', 'La ascitis asciende, el diafragma muestra un defecto, '
            'el líquido pasa y llena la cavidad pleural derecha comprimiendo el pulmón.')
    st = [({}, 'Hígado', 'Hígado cirrótico bajo la cúpula diafragmática derecha.'),
          ({'hl': {'Intestino'}}, 'Cavidad abdominal', 'Cavidad peritoneal con asas intestinales.'),
          ({'asc': 0.55, 'hl': {'Ascitis'}}, 'Ascitis', 'La cirrosis genera **ascitis**: líquido en la cavidad peritoneal.'),
          ({'asc': 0.55, 'hl': {'Diafragma'}}, 'Diafragma', 'El líquido ascítico busca **derivación ascendente** hacia el diafragma.'),
          ({'asc': 0.55, 'defect': 1}, 'Comunicación', 'Un **defecto diafragmático** «abre paso» al líquido.'),
          ({'asc': 0.45, 'defect': 1, 'pfl': 0.2, 'hl': {'LiquidoPleuralD'}}, 'Espacio pleural', 'El líquido invade la cavidad pleural.'),
          ({'asc': 0.4, 'defect': 1, 'pfl': 0.55}, 'Acumulación', 'Derrame **habitualmente derecho**: **trasudado**.')]
    for i, (sst, ttl, cap) in enumerate(st):
        s = new(D, 'Hidrotórax hepático', ttl, 'azul', morph=i > 0, src=['P2.6', 'T2.4'])
        A = abdomen(s, 0.3, 0.95, 7.4, 6.1, sst)
        step_badge(s, i + 1, len(st))
        lg = legend(s, cap, 8.0, 1.0, 5.0, h=1.6, size=16)
        info = [('Origen', 'Cirrosis → hipertensión portal e hipoalbuminemia → **ascitis**.', ORANGE),
                ('Paso', 'Ascitis crónica → **defecto diafragmático** → paso pleuroperitoneal.', GREEN),
                ('Nombre exacto', '**Hidrotórax hepático** por defecto diafragmático secundario a ascitis crónica.', CEL)]
        k = [1, 1, 2, 2, 3, 3, 3][i]
        cs = two_cards(s, info[:k], 8.0, 2.8, 5.0, 4.15 * k / 3, 0.15, 14)
        if i == 4:
            ar = s.arrow([A['F'].p(330, 560), A['F'].p(305, 470), A['F'].p(290, 380)], TRN, 6, name='Flecha paso', curve=True)
            s.step(wipe(ar, 'b'))
        if i in (0, 2, 4):
            s.step(fade(cs[-1]))
    Q.close()


def nefrotico(D):
    Q = Seq(D, 'Síndrome nefrótico: dos cadenas distintas (derrame y TEP) (Unidad V)', '!!Glomerulo, !!ProteinasOrina, !!Capilar, '
            '!!Albumina, !!Leyenda, tórax, !!VenaProfunda, !!Trombo, !!Embolo', 'Tablero fijo de tres escenas (riñón, capilar, tórax) '
            'donde se encienden por pasos la rama oncótica (derrame) y la rama de hipercoagulabilidad (TVP → TEP).')
    st = [('Riñón', {}, {}, {}, 'El **glomérulo** filtra el plasma y normalmente retiene las proteínas.'),
          ('Pérdida urinaria de proteínas', {'leak': 22}, {}, {}, '**Proteinuria masiva**: las proteínas pasan a la orina.'),
          ('Disminución de la albúmina', {'leak': 22}, {'alb': 7, 'hl': {'Albumina'}, 'drops': False}, {}, '**Hipoalbuminemia**.'),
          ('Presión oncótica', {'leak': 22}, {'alb': 7, 'show': {'pc', 'onc'}, 'onc': 0.35, 'drops': False}, {}, '↓ π_{c}: menos fuerza de retención.'),
          ('Acumulación de líquido', {'leak': 22}, {'alb': 7, 'show': {'pc', 'onc'}, 'onc': 0.35, 'acc': 0.4}, {'fluidR': 0.18, 'fluidL': 0.18},
           'Derrame **pequeño, bilateral, a menudo asintomático**: trasudado.'),
          ('Hipercoagulabilidad', {'leak': 22}, {'alb': 7, 'show': {'pc', 'onc'}, 'onc': 0.35, 'acc': 0.4}, {'fluidR': 0.18, 'fluidL': 0.18},
           'También se pierden **anticoagulantes** naturales (antitrombina III, proteínas C y S) → estado procoagulante.'),
          ('Riesgo tromboembólico', {'leak': 22}, {'alb': 7, 'show': {'pc', 'onc'}, 'onc': 0.35, 'acc': 0.4}, {'fluidR': 0.18, 'fluidL': 0.18, 'emb': 1},
           '**TVP → TEP**: descartarlo siempre en el síndrome nefrótico.')]
    for i, (ttl, gk, sk, ck, cap) in enumerate(st):
        s = new(D, 'Síndrome nefrótico', ttl, 'azul', morph=i > 0, src=['P2.4', 'P2.6', 'T2.2'])
        G = glomerulus(s, 0.3, 1.0, 3.6, 3.6, gk)
        S = starling(s, 4.15, 1.0, 4.4, 3.6, sk)
        C = chest(s, 8.8, 1.0, 4.2, 3.6, ck)
        step_badge(s, i + 1, len(st))
        for x, t in ((0.3, 'RIÑÓN'), (4.15, 'CAPILAR'), (8.8, 'TÓRAX')):
            tag(s, x, 4.7, t, WHITE, 13)
        lg = legend(s, cap, 0.3, 5.2, 8.25 if i >= 5 else 12.7, h=1.75, size=16)
        if i >= 5:
            V = vein_dvt(s, 8.95, 5.15, 1.1, 2.1, {'clot': 1, 'emb': i == 6})
            b = box(s, 10.2, 5.2, 2.8, 1.75, 'Cadena **distinta** del derrame: hipercoagulabilidad → TVP → TEP.', RED, 13.5,
                    name='Rama trombótica', bold=False)
            s.step(fade(V['clot']), fade(b, after=True))
            if i == 6:
                s.step(path(V['emb'], 0, -0.4, dur=900))
        if i == 1 and G.get('prot'):
            s.step(fade(G['prot']))
    Q.close()
    s = new(D, 'Síndrome nefrótico', 'Diferenciar el mecanismo del derrame del mecanismo del TEP', 'mesotelio', src=['P2.4'])
    a = flow(s, ['Proteinuria masiva', 'Hipoalbuminemia', '↓ presión oncótica', 'Derrame pleural (trasudado)'], 0.4, 1.0, 6.0, 5.2,
             [WHITE, GOLD, CEL, C_FLUID], 16, 0.3, 'v')
    b = flow(s, ['Pérdida de anticoagulantes', 'Estado hipercoagulable', 'Trombosis venosa profunda', 'Tromboembolismo pulmonar'], 6.9, 1.0, 6.0, 5.2,
             [WHITE, ORANGE, RED, RED], 16, 0.3, 'v')
    t1 = tag(s, 0.4, 6.35, 'RAMA ONCÓTICA', C_FLUID, 15, w=6.0)
    t2 = tag(s, 6.9, 6.35, 'RAMA TROMBÓTICA', RED, 15, w=6.0)
    flow_anim(s, a, 2, 'v')
    flow_anim(s, b, 2, 'v')
    s.step(fade(t1), fade(t2))


def otras(D):
    s = new(D, 'Etiologías', 'Tromboembolismo pulmonar', 'azul', src=['T2.4', 'P2.4'])
    A = chest(s, 0.3, 0.95, 5.7, 5.6, {'emb': 1, 'fluidR': 0.2, 'hl': {'Embolo'}})
    co = callout(s, [A['hilR'], (6.4, 1.3)], 'Émbolo en la arteria pulmonar', 6.4, 1.0, 3.6, 0.6, WHITE, 14)
    cs = two_cards(s, [('Líquido', 'El TEP puede producir **trasudado o exudado**.', GOLD),
                       ('Exudado', 'Cuando provoca **infarto pulmonar** con inflamación pleural.', C_EXUD),
                       ('Contexto', 'Buscarlo en estados **hipercoagulables** (síndrome nefrótico).', CEL),
                       ('Citología', 'Leucocitos con **neutrófilos**: pleuritis aguda (infección bacteriana, TEP, infarto).', TURQ)],
                   6.4, 1.8, 6.6, 5.15, 0.15, 14.5)
    s.step(fade(co))
    reveal(s, cs, 1)
    s = new(D, 'Etiologías', 'Neoplasias: cómo una masa produce derrame', 'azul', src=['P2.6', 'T5.2'])
    A = chest(s, 0.3, 0.95, 5.7, 5.6, {'fluidR': 0.4, 'mass': (230, 330, 70), 'hl': {'Tumor'}})
    res = flow(s, ['**Ocupa espacio** y modifica la estructura', '↑ presión sobre capilares vecinos', '↑ **permeabilidad** capilar',
                   'Requiere **vascularización propia**: altera los vasos adyacentes', 'Puede bloquear **linfáticos**'],
               6.4, 1.0, 6.6, 4.7, [WHITE, CEL, ORANGE, GREEN, LGREEN], 14.5, 0.2, 'v')
    w = box(s, 6.4, 5.9, 6.6, 1.05, 'Según el mecanismo dominante puede dar **trasudado o exudado**.', GOLD, 15, name='Trasudado o exudado')
    flow_anim(s, res, 1, 'v')
    s.step(fade(w))
    s = new(D, 'Etiologías', 'Infecciones: bacterias, micobacterias, hongos y virus', 'rosa', src=['T2.4', 'P2.13', 'P2.5'])
    A = chest(s, 0.3, 0.95, 5.0, 4.9, {'fluidR': 0.35, 'exud': 1, 'lungcolR': 'C9575F'})
    g = box(s, 0.3, 6.0, 5.0, 1.0, 'Neumonía → **derrame paraneumónico** (Unidad XI).', C_EXUD, 14, name='Paraneumónico')
    rows = [['AGENTES DE EXUDADOS INFECCIOSOS'], ['Streptococcus sp. · Staphylococcus aureus'], ['Pseudomonas aeruginosa · Haemophilus influenzae'],
            ['Bacteroides sp. (anaerobios)'], ['Mycobacterium tuberculosis (bacilo de Koch)'], ['Hongos · virus (Mycoplasma, Pneumocystis)']]
    ids, h = gtable(s, 5.6, 1.0, 7.4, rows, [1], 15, first_fill=None, first_bold=False, fill_to=5.0)
    t = box(s, 5.6, 5.2, 7.4, 1.75, '**TBC**: exudado **linfocítico** con **ADA elevada** (criterios en Unidad X).', GOLD, 15, name='TBC')
    s.step(fade(g))
    table_anim(s, ids, 2)
    s.step(fade(t))
    s = new(D, 'Etiologías', 'Autoinmunes, abdominales y otras causas', 'mesotelio', src=['T2.4', 'T4.4', 'P2.12'])
    cs = [box(s, 0.4, 1.0, 4.05, 2.9, '**Artritis reumatoidea** · **LES** · vasculitis (**Churg-Strauss**).\nANA/FR en pleura > sangre.',
              LILAC, 14.5, head='Colagenopatías', bold=False),
          box(s, 4.65, 1.0, 4.05, 2.9, '**Pancreatitis** → derrame **izquierdo**, amilasa pleural > sangre.\n**Absceso subfrénico** · '
              '**perforación esofágica**.', ORANGE, 14.5, head='Intraabdominales', bold=False),
          box(s, 8.9, 1.0, 4.05, 2.9, '**Quilotórax**: rotura del conducto torácico (triglicéridos > 110 mg/dl).', 'F4F1E6', 14.5,
              head='Linfa en la pleura', bold=False),
          box(s, 0.4, 4.1, 4.05, 2.85, '**Urinotórax**: creatinina pleural > plasmática.', 'FCF3CF', 14.5, head='Orina en la pleura', bold=False),
          box(s, 4.65, 4.1, 4.05, 2.85, '**Fístula duro-pleural**: β-2 transferrina (LCR en la pleura).', CEL, 14.5, head='LCR en la pleura', bold=False),
          box(s, 8.9, 4.1, 4.05, 2.85, '**Postraumático** · lesiones torácicas abiertas · **idiopático** (sin causa tras el estudio).', WHITE, 14.5,
              head='Otras', bold=False)]
    reveal(s, cs, 1)


def build(D):
    unit_start(D, 'IV', 'Trasudado y exudado')
    div4(D)
    definiciones(D)
    seq_trasudado(D)
    seq_exudado(D)
    comparacion(D)
    no_taxativo(D)
    unit_end(D, 'IV')
    unit_start(D, 'V', 'Etiologías del derrame pleural')
    div5(D)
    causas(D)
    frecuentes(D)
    icc(D)
    hidrotorax(D)
    nefrotico(D)
    otras(D)
    unit_end(D, 'V')
