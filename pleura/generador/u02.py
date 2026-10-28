# -*- coding: utf-8 -*-
"""UNIDAD II (Starling: formación y reabsorción) y UNIDAD III (mecanismos del derrame)."""
from base import *

SX, SY, SWd, SHt = 0.3, 0.95, 7.7, 6.3   # escena del capilar
TX, TW = 8.3, 4.75                        # columna de texto


def div2(D):
    def art(s):
        starling(s, 7.0, 0.6, 6.0, 6.2, {'show': {'pc', 'onc', 'net', 'lym'}})
    divider(D, 'II', 'Formación y reabsorción del líquido pleural', 'El equilibrio de Starling y el drenaje linfático',
            ['Presión hidrostática capilar', 'Presión oncótica (albúmina)', 'Permeabilidad y coeficiente de reflexión',
             'Filtración neta', 'Drenaje linfático de la pleura parietal', 'Qué ocurre cuando se altera una fuerza'], art,
            src=['T2.2', 'P2.2'])


def ecuacion(D):
    s = new(D, 'Starling', 'La ecuación de Starling', 'mesotelio', src=['P2.2', 'T2.2'])
    eq = s.shape(0.5, 1.0, 12.3, 1.25, 'rect', WHITE, BORDER, False,
                 'Filtración = K · [ (P_{c} − P_{i}) − σ · (π_{c} − π_{i}) ]', 34, F_TITLE, INK, True, 'c', 'm', name='Ecuación', fit=False)
    vs = [('K', 'Coeficiente de filtración: permeabilidad al agua × superficie del capilar', GREEN),
          ('P_{c}', 'Presión hidrostática capilar: **empuja** líquido fuera del vaso', 'F4A6A6'),
          ('P_{i}', 'Presión hidrostática del intersticio / espacio pleural: se opone a la salida', 'F9D5D3'),
          ('σ', 'Coeficiente de reflexión de proteínas: 1 = membrana impermeable a proteínas; menor = fuga proteica', GOLD),
          ('π_{c}', 'Presión oncótica capilar (sobre todo **albúmina**): **retiene** líquido dentro del vaso', '9CC3E8'),
          ('π_{i}', 'Presión oncótica del intersticio: atrae líquido hacia afuera', 'D6EAF8')]
    ids = []
    for i, (k, t, c) in enumerate(vs):
        x = 0.5 + (i % 2) * 6.2; y = 2.55 + (i // 2) * 1.12
        g = s.group_start('Variable ' + plain(k))
        s.shape(x, y, 1.1, 0.95, 'rect', c, BORDER, False, k, 26, F_TITLE, INK, True, 'c', 'm', fit=False)
        box(s, x + 1.15, y, 4.95, 0.95, t, WHITE, 14, align='l', bold=False)
        ids.append(s.group_end())
    n = box(s, 0.5, 5.95, 12.3, 1.0, 'Tres situaciones rompen el equilibrio: **↑ P_{c}**, **↓ π_{c}** y **falla del drenaje linfático**; '
            'a ellas se suma el **↑ de permeabilidad** (↑ K, ↓ σ) de la pleura enferma.', ORANGE, 15, name='Rupturas', bold=False)
    s.step(zoom(eq))
    reveal(s, ids, 2)
    s.step(fade(n))
    s.note('Las fuerzas que sacan líquido del capilar son la presión hidrostática capilar y la oncótica intersticial; las que lo '
           'retienen son la oncótica capilar y la hidrostática intersticial. El coeficiente sigma pondera cuánto «cuentan» las '
           'proteínas: si la membrana se vuelve permeable, la diferencia oncótica deja de retener agua.')


def seq_starling(D):
    Q = Seq(D, 'Fuerzas de Starling: capilar → membrana → intersticio → fuerzas → linfa → equilibrio → alteración (Unidad II)',
            '!!Capilar, !!Albumina, !!Intersticio, !!VasoLinfatico, !!FlechaPc, !!FlechaOnc, !!FlechaNeta, !!FlechaLinfa, '
            '!!LiquidoAcumulado, !!GotasFiltrado, !!Leyenda',
            'Aparición progresiva de las flechas de fuerza con grosor proporcional; en la alteración la flecha de Pc se engrosa y '
            'el líquido acumulado sube de nivel.')
    steps = [
        ('Capilar pleural', {}, 'La pleura está irrigada por capilares: los de la hoja parietal dependen de la circulación sistémica.',
         [('Capilar', 'Tubo de endotelio con eritrocitos, plasma y **albúmina** (esferas amarillas).', CEL)]),
        ('La membrana capilar', {'hl': {'Capilar'}}, 'El endotelio es una barrera semipermeable: deja pasar agua y retiene proteínas.',
         [('Endotelio', 'Células unidas entre sí: barrera **semipermeable**.', GREEN), ('σ ≈ 1', 'En condiciones normales las proteínas **no atraviesan** la barrera.', GOLD)]),
        ('Espacio intersticial y pleural', {'hl': set()}, 'Debajo, el compartimento que recibe el filtrado: intersticio y espacio pleural.',
         [('Compartimento receptor', 'Recibe el agua filtrada; su presión (P_{i}) y su oncótica (π_{i}) también participan.', CEL)]),
        ('Presión hidrostática', {'show': {'pc'}}, 'P_{c} empuja el plasma hacia afuera del capilar.',
         [('P_{c}', 'Fuerza de **salida**. Depende de la presión venosa/capilar.', 'F4A6A6')]),
        ('Presión oncótica', {'show': {'pc', 'onc'}, 'hl': {'Albumina'}}, 'π_{c}, generada sobre todo por la albúmina, retiene agua dentro del vaso.',
         [('π_{c}', 'Fuerza de **retención**: las proteínas plasmáticas «atraen» agua.', '9CC3E8')]),
        ('Movimiento neto', {'show': {'pc', 'onc', 'net'}}, 'El balance de fuerzas produce una pequeña filtración neta hacia el espacio pleural.',
         [('Filtración neta', 'Resultado de (P_{c} − P_{i}) − σ(π_{c} − π_{i}): **pequeño flujo de salida** continuo.', GREEN)]),
        ('Drenaje linfático', {'show': {'pc', 'onc', 'net', 'lym'}}, 'Los linfáticos de la pleura parietal son la principal vía de reabsorción.',
         [('Linfáticos', 'Reabsorben el líquido a través de **estomas** de la pleura parietal.', LGREEN)]),
        ('Situación fisiológica', {'show': {'pc', 'onc', 'net', 'lym'}, 'acc': 0}, 'Equilibrio: lo que se filtra se drena; el volumen pleural se mantiene mínimo.',
         [('Equilibrio', '**Producción = reabsorción**. El volumen permanece en ~0,13 ml/kg.', CEL)]),
        ('Alteración de una fuerza', {'show': {'pc', 'onc', 'net', 'lym'}, 'pc': 2, 'hl': set()}, 'Ejemplo: aumenta P_{c}. La filtración supera la capacidad de reabsorción.',
         [('Ruptura del equilibrio', 'Cualquier fuerza que aumente la salida o reduzca la reabsorción desplaza el balance.', ORANGE)]),
        ('Consecuencia sobre el volumen', {'show': {'pc', 'onc', 'net', 'lym'}, 'pc': 2, 'acc': 0.55, 'hl': {'LiquidoAcumulado'}},
         'El líquido se acumula: aparece el derrame pleural.',
         [('Derrame', '**Aumento del líquido pleural** por encima de lo normal: es una **manifestación**, no un diagnóstico.', RED)]),
    ]
    for i, (ttl, st, cap, cards) in enumerate(steps):
        s = new(D, 'Starling', ttl, 'azul', morph=i > 0, src=['P2.2', 'T2.2'] + (['T2.1'] if i == 9 else []))
        A = starling(s, SX, SY, SWd, SHt, st)
        step_badge(s, i + 1, len(steps))
        cs = two_cards(s, [(h, t, c) for h, t, c in cards], TX, 1.0, TW, 4.1, 0.2, 16)
        lg = legend(s, cap, TX, 5.3, TW, h=1.65)
        new_arrow = {3: 'f_pc', 4: 'f_onc', 5: 'f_net', 6: 'f_lym'}.get(i)
        if new_arrow and A.get(new_arrow):
            s.step(wipe(A[new_arrow], 'b' if new_arrow == 'f_onc' else ('t' if new_arrow != 'f_lym' else 'b')))
        if i == 4:
            s.step(pulse(A['alb']))
        if i == 9 and A.get('acc'):
            s.step(wipe(A['acc'], 'b', dur=900))
        reveal(s, cs, 1)
    Q.close()


def compartimentos(D):
    s = new(D, 'Starling', 'Derrame pleural ≠ edema intersticial ≠ edema alveolar', 'torax', src=['T1.1', 'P2.2', 'P2.3'])
    A = chest(s, 0.3, 0.95, 5.6, 5.5, {'fluidR': 0.35})
    Z = pleura_zoom(s, 6.1, 0.95, 3.2, 5.5, {'gap': 0.25})
    cs = two_cards(s, [('Derrame pleural', 'Líquido **entre las hojas** (espacio pleural).', C_FLUID),
                       ('Edema intersticial', 'Líquido en el **intersticio pulmonar**, dentro del parénquima.', 'F9D5D3'),
                       ('Edema alveolar', 'Líquido **dentro de los alvéolos**: altera directamente la hematosis.', 'F4A6A6')],
                   9.5, 0.95, 3.5, 4.4, 0.15, 13.5)
    w = box(s, 0.3, 6.55, 12.7, 0.6, 'Pueden coexistir (p. ej., en la insuficiencia cardíaca), pero uno **no implica obligatoriamente** al otro.',
            RED, 14, name='No confundir')
    n = box(s, 9.5, 5.5, 3.5, 0.9, 'Progresión derrame → alvéolo: **revisar** (Auditoría).', GOLD, 12.5, name='Revisión')
    reveal(s, cs, 1)
    s.step(fade(w))
    s.step(fade(n))
    s.note('Es esencial no confundir compartimentos. El derrame pleural ocupa el espacio entre las hojas; el edema intersticial y '
           'el alveolar ocupan el pulmón. El material describe un desborde linfático que «inunda los alvéolos» a partir del '
           'derrame: esa progresión no es obligatoria y se registra en la auditoría científica.')


# ------------------------------------------------------------------ UNIDAD III
def div3(D):
    def art(s):
        chest(s, 7.1, 0.6, 6.0, 6.0, {'fluidR': 0.4, 'fluidL': 0.25})
    divider(D, 'III', 'Mecanismos del derrame pleural', 'Cuatro maneras de romper el equilibrio',
            ['A · Aumento de la presión hidrostática', 'B · Disminución de la presión oncótica', 'C · Alteración del drenaje linfático',
             'D · Aumento de la permeabilidad capilar', 'Comparación integradora', 'Repercusión fisiopatológica del derrame'], art,
            src=['T2.2', 'P2.2'])


def mech(D, letter, ttl, states, caps, cards_list, src, inset, extra=None):
    Q = Seq(D, 'Mecanismo %s · %s' % (letter, ttl), '!!Capilar, !!Albumina, !!VasoLinfatico, flechas de fuerza, !!LiquidoAcumulado, '
            'tórax de referencia (!!PulmonDerecho, !!LiquidoPleuralD)', 'Mismo capilar en tres estados: normal → alteración → acumulación.')
    for i, st in enumerate(states):
        s = new(D, 'Mecanismo ' + letter, ttl + ['', ' · alteración', ' · acumulación'][i], 'azul', morph=i > 0, src=src)
        A = starling(s, 0.3, 0.95, 7.3, 6.25, st)
        tag(s, 0.4, 1.05, ['NORMAL', 'ALTERACIÓN', 'CONSECUENCIA'][i], [WHITE, ORANGE, RED][i], 14, name='!!Estado')
        C = chest(s, 7.85, 0.95, 2.4, 2.4, inset[i], names=True)
        cs = two_cards(s, cards_list[i], 10.4, 0.95, 2.65, 5.35, 0.15, 13)
        lg = legend(s, caps[i], 7.85, 3.55, 2.4, h=2.75, size=13)
        if extra:
            extra(s, A, i)
        reveal(s, cs, 1)
    Q.close()


def mechs(D):
    allf = {'pc', 'onc', 'net', 'lym'}
    mech(D, 'A', 'Aumento de la presión hidrostática',
         [{'show': allf}, {'show': allf, 'pc': 2}, {'show': allf, 'pc': 2, 'acc': 0.55}],
         ['Fuerzas en equilibrio.', '↑ P_{c}: la presión dentro del capilar empuja más líquido hacia afuera.',
          'La filtración supera el drenaje: derrame **bilateral** en la insuficiencia cardíaca.'],
         [[('Estado basal', 'P_{c} y π_{c} equilibradas; la linfa drena el filtrado.', CEL)],
          [('Causa', '↑ presión **venosa** pulmonar y sistémica: **insuficiencia cardíaca congestiva**.', ORANGE),
           ('Pleura', 'La pleura está **sana**: el problema es **sistémico**.', GREEN)],
          [('Resultado', 'Líquido claro, pocas proteínas: **trasudado**.', C_FLUID),
           ('ICC', 'Causa más frecuente de derrame; típicamente **bilateral**.', GOLD)]],
         ['T2.2', 'P2.2', 'P2.6'], [{}, {}, {'fluidR': 0.3, 'fluidL': 0.25}])
    s = new(D, 'Mecanismo A', '¿Qué capilar se altera primero en la insuficiencia cardíaca?', 'torax', src=['P2.2'])
    A = chest(s, 0.3, 0.95, 5.8, 5.6, {'fluidR': 0.2, 'fluidL': 0.18, 'hl': {'Corazon'}})
    res = flow(s, ['Falla de la bomba izquierda', '↑ presión en venas y capilares **pulmonares** (circulación funcional)',
                   'Alteración de la **función**: intercambio gaseoso', 'Después, con repercusión establecida, la circulación **bronquial** (nutricia)'],
               6.4, 0.95, 6.6, 4.4, [WHITE, ORANGE, GREEN, CEL], 14.5, 0.25, 'v')
    w = box(s, 6.4, 5.6, 6.6, 1.35, 'Lo primero que se altera es la **función** (hematosis), no la irrigación nutricia. La secuencia '
            'exacta entre circulaciones se registra para revisión.', GOLD, 13.5, name='Función primero', bold=False)
    flow_anim(s, res, 1, 'v')
    s.step(fade(w))
    mech(D, 'B', 'Disminución de la presión oncótica',
         [{'show': allf, 'alb': 30}, {'show': allf, 'alb': 8, 'onc': 0.35, 'hl': {'Albumina'}}, {'show': allf, 'alb': 8, 'onc': 0.35, 'acc': 0.5}],
         ['Albúmina normal: π_{c} retiene el agua.', '↓ albúmina → ↓ π_{c}: la fuerza de retención se debilita.',
          'El líquido sale y se acumula: **trasudado**.'],
         [[('Albúmina', 'Principal proteína responsable de π_{c}.', GOLD)],
          [('Causas', '**Hipoalbuminemia** severa · **síndrome nefrótico** · **cirrosis** hepática.', ORANGE),
           ('Pleura', '**Sana**: problema sistémico.', GREEN)],
          [('Resultado', '**Trasudado** (pocas proteínas, poca LDH, pocas células).', C_FLUID),
           ('Nefrótico', 'Derrame habitualmente **pequeño, bilateral y asintomático**.', CEL)]],
         ['T2.2', 'P2.2', 'P2.6'], [{}, {}, {'fluidR': 0.18, 'fluidL': 0.18}])
    mech(D, 'C', 'Alteración del drenaje linfático',
         [{'show': allf}, {'show': {'pc', 'onc', 'net'}, 'lymph': 'block'}, {'show': {'pc', 'onc', 'net'}, 'lymph': 'block', 'acc': 0.5, 'prot': 10}],
         ['Los linfáticos parietales reabsorben el filtrado.', 'Obstrucción (tumor, inflamación) o capacidad superada.',
          'El filtrado normal ya no se elimina: se acumula.'],
         [[('Reabsorción', 'Linfáticos de la **pleura parietal**: **principal vía** de salida.', LGREEN)],
          [('Bloqueo', '**Tumor** (metástasis) o **inflamación** ocluyen los estomas y vasos.', ORANGE),
           ('Capacidad', 'Un filtrado excesivo puede **superar** la capacidad linfática conservada.', CEL)],
          [('Resultado', 'Las proteínas que normalmente drenan quedan retenidas: suele dar **exudado**.', C_EXUD),
           ('No taxativo', 'El mismo razonamiento aplica a procesos sistémicos: **no existe el cuadro puro**.', GOLD)]],
         ['T2.2', 'P2.2', 'P2.10'], [{}, {}, {'fluidR': 0.35}])
    mech(D, 'D', 'Aumento de la permeabilidad capilar',
         [{'show': {'pc', 'onc', 'net'}}, {'show': {'pc', 'onc', 'net'}, 'perm': 1}, {'show': {'pc', 'onc', 'net'}, 'perm': 1, 'acc': 0.5, 'prot': 26, 'wbc': 6}],
         ['Endotelio íntegro: σ ≈ 1.', 'Inflamación, infección o neoplasia abren uniones endoteliales.',
          'Salen agua, **proteínas** y **células**: **exudado**.'],
         [[('Barrera', 'Uniones intactas: proteínas y células **quedan en el vaso**.', CEL)],
          [('Lesión local', '**Inflamación · infección · neoplasia** → ↑ permeabilidad (↑ K, ↓ σ).', ORANGE),
           ('Pleura', '**Enferma**: el problema es **local**.', RED)],
          [('Resultado', 'Líquido con **más proteínas, más LDH y más células** inflamatorias.', C_EXUD),
           ('Células', 'PMN en procesos agudos; linfocitos en TBC o tumores.', GOLD)]],
         ['T2.2', 'T2.3'], [{}, {}, {'fluidR': 0.35, 'exud': 1}])


def mech_tabla(D):
    s = new(D, 'Mecanismos', 'Comparación integradora de los cuatro mecanismos', 'mesotelio', src=['T2.2', 'T2.3', 'P2.10'])
    rows = [['MECANISMO', 'FUERZA ALTERADA', 'PLEURA', 'LÍQUIDO HABITUAL', 'EJEMPLOS'],
            ['A · Hidrostático', '↑ P_{c}', 'Sana', 'Trasudado', 'Insuficiencia cardíaca congestiva'],
            ['B · Oncótico', '↓ π_{c} (albúmina)', 'Sana', 'Trasudado', 'Síndrome nefrótico · cirrosis · hipoalbuminemia'],
            ['C · Linfático', '↓ reabsorción', 'Enferma (habitual)', 'Exudado', 'Metástasis · inflamación'],
            ['D · Permeabilidad', '↑ K, ↓ σ', 'Enferma', 'Exudado', 'Infección · inflamación · neoplasia']]
    ids, h = gtable(s, 0.4, 1.0, 12.5, rows, [1.5, 1.4, 1.2, 1.3, 2.6], 15.5, fill_to=5.6,
                    col_fills=[None, None, None, None, None])
    w = box(s, 0.4, 5.8, 12.5, 1.15, 'En derrames importantes **suelen combinarse** mecanismos: la clasificación orienta, pero '
            '«**no existe el cuadro puro**».', RED, 16, name='Mixtura')
    table_anim(s, ids, 1)
    s.step(fade(w))


def repercusion(D):
    Q = Seq(D, 'Repercusión fisiopatológica del derrame (volumen creciente)', '!!PulmonDerecho, !!LiquidoPleuralD, !!Mediastino, '
            '!!Corazon, !!Traquea, !!Leyenda', 'El líquido sube, el pulmón se comprime hacia el hilio y, en el derrame masivo, el '
            'mediastino se desplaza al lado sano.')
    sts = [({'fluidR': 0.2}, 'Derrame pequeño', 'Puede ser **asintomático**: el pulmón apenas se comprime.'),
           ({'fluidR': 0.5}, 'Derrame moderado', 'El líquido **comprime el pulmón** subyacente y **restringe su expansión**.'),
           ({'fluidR': 0.88, 'shift': 70, 'widenR': 1}, 'Derrame masivo', 'Desplazamiento del **mediastino hacia el lado sano**; '
            'disnea marcada.')]
    for i, (st, ttl, txt) in enumerate(sts):
        s = new(D, 'Repercusión', 'Repercusión del derrame: ' + ttl.lower(), 'azul', morph=i > 0, src=['P2.3', 'T3.1', 'T3.3'])
        A = chest(s, 0.3, 0.95, 6.4, 6.2, st)
        step_badge(s, i + 1, 3)
        items = [('Mecánica', 'Menos volumen pulmonar disponible → menor **expansión**.', GREEN),
                 ('Ventilación', 'Compromiso **ventilatorio** proporcional al volumen y a la reserva del paciente.', CEL),
                 ('Clínica', ['Hallazgo incidental en la radiografía.', 'Disnea cuando ocupa > 1/3 del hemitórax.',
                              'Disnea intensa; posible compromiso hemodinámico.'][i], ORANGE)]
        cs = two_cards(s, items, 7.0, 1.0, 6.0, 4.0, 0.18, 14)
        lg = legend(s, txt, 7.0, 5.2, 6.0, h=0.85)
        if i == 2:
            w = box(s, 7.0, 6.15, 6.0, 0.95, 'Si al derrame se **suma aire** puede instalarse un neumotórax a tensión → **shock obstructivo**.',
                    RED, 13.5, name='Riesgo tensión')
            reveal(s, cs, 1)
            s.step(zoom(w))
        else:
            reveal(s, cs, 1)
    Q.close()
    s = new(D, 'Repercusión', 'Una consecuencia variable: depende del volumen, la causa y el paciente', 'torax', src=['P2.3', 'T3.1'])
    res = flow(s, ['Acumulación de líquido', 'Compresión del pulmón subyacente', 'Restricción de la expansión',
                   'Compromiso de la ventilación', 'Posible hipoxemia'], 0.4, 1.05, 12.5, 1.5, [C_FLUID, WHITE, CEL, GREEN, ORANGE], 14, 0.3)
    b1 = box(s, 0.4, 2.9, 6.1, 2.4, 'La repercusión **no es fija**: un derrame pequeño en un paciente sano puede pasar inadvertido; el '
             'mismo volumen en un paciente con poca reserva puede descompensarlo.', WHITE, 15, name='Variable', bold=False,
             head='Repercusión variable', headfill=CEL)
    b2 = box(s, 6.8, 2.9, 6.1, 2.4, 'Una **cascada** propuesta (derrame → inundación alveolar → falla respiratoria → '
             'claudicación del ventrículo izquierdo) **no es obligatoria** y mezcla compartimentos.', WHITE, 15,
             name='Cascada revisión', bold=False, head='Para revisión', headfill=RED)
    b3 = box(s, 0.4, 5.55, 12.5, 1.35, 'Conclusión: el derrame **no es solo** «líquido en la pleura»: puede alterar la mecánica, la '
             'ventilación y, en situaciones extremas, la hemodinamia.', GOLD, 16, name='Es un todo', bold=False)
    flow_anim(s, res, 1)
    s.step(fade(b1))
    s.step(fade(b2))
    s.step(zoom(b3))


def build(D):
    unit_start(D, 'II', 'Formación y reabsorción del líquido: Starling')
    div2(D)
    ecuacion(D)
    seq_starling(D)
    compartimentos(D)
    unit_end(D, 'II')
    unit_start(D, 'III', 'Mecanismos del derrame pleural')
    div3(D)
    mechs(D)
    mech_tabla(D)
    repercusion(D)
    unit_end(D, 'III')
