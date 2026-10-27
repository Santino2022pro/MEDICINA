# -*- coding: utf-8 -*-
"""UNIDAD I (c) — Señalización insulínica (Morph), hígado, adipocito, ejercicio, contrarreguladoras y mapas de vías"""
from base import *
from sig import *

U = 1
SEQ = 'peach'


def action(D):
    s = new(D, U, 'Acción fisiológica normal de la insulina', 'green')
    p = s.pic('pancreas', 5.2, 1.15, 2.9, name='Páncreas acción')
    ins = mbox(s, 5.65, 2.45, 2.0, 0.5, 'INSULINA', 'y', 16)
    cols = [('healthy_liver', 'HÍGADO', '- Glucógeno ↑ · glucólisis ↑\n- Lipogénesis ↑ (SREBP-1c)\n- **Producción de glucosa ↓** (FOXO1 inactivo)\n- No necesita GLUT4: usa **GLUT2**', 0.4),
            ('muscle-fiber', 'MÚSCULO', '- **GLUT4** en membrana → captación ↑\n- Síntesis de glucógeno ↑\n- Síntesis proteica ↑', 4.65),
            ('adipocyte-1', 'TEJIDO ADIPOSO', '- **GLUT4** → glicerol-3-P\n- LPL y esterificación ↑\n- **Lipólisis ↓** (PDE3B → AMPc ↓)', 8.9)]
    ids = []
    for img, h, t, x in cols:
        g = s.group_start('Órgano ' + h)
        fitpic(s, img, x + 0.6, 3.15, 2.8, 1.25)
        mbox(s, x, 4.45, 4.0, 0.45, h, 'Y', 15)
        tbox(s, x, 4.95, 4.0, 1.95, t, 14.5)
        ids.append(s.group_end())
    a = [s.arrow([(5.6, 2.75), (2.4, 3.2)], ACT, 3), s.arrow([(6.65, 2.98), (6.65, 3.2)], ACT, 3), s.arrow([(7.7, 2.75), (10.9, 3.2)], ACT, 3)]
    s.step(zoom(ins))
    for g, ar in zip(ids, a):
        s.step(wipe(ar, 'l' if ar != a[1] else 't'), fade(g, after=True))
    s.note('Acción fisiológica normal (paso 1 de la cadena de la resistencia insulínica). En el hígado, la insulina aumenta la '
           'síntesis de glucógeno, la glucólisis y la lipogénesis y reduce la producción neta de glucosa; el hepatocito capta '
           'glucosa por GLUT2 sin depender de la insulina para el transporte: la hormona regula su metabolismo. En el músculo y el '
           'adipocito, la insulina transloca GLUT4 a la membrana. En el adipocito además provee glicerol-3-fosfato, aumenta la '
           'esterificación e inhibe la lipólisis. Idea fuerza: «Insulina → RTK → IRS/PI3K/Akt → GLUT4, glucógeno y anabolismo; '
           'menos gluconeogénesis y menos lipólisis».')


def r0(D):
    s = new(D, U, 'Receptor de insulina: tirosina cinasa α₂β₂', SEQ)
    ids = sig_scene(s, 0)
    sig_panel(s, '1', 'El receptor', '- Heterotetrámero **α₂β₂** unido por puentes disulfuro.\n- Subunidades **α** extracelulares: unen insulina.\n'
              '- Subunidades **β** transmembrana con dominio **tirosina cinasa** intracelular.\n- En reposo la actividad cinasa está autoinhibida.')
    sig_progress(s, [])
    s.step(pulse(ids['rec']))
    s.step(pulse(ids['irs']), pulse(ids['pi3k'], after=True), pulse(ids['akt'], after=True), pulse(ids['ves'][0], after=True))
    s.note('Comienzo de la secuencia molecular de la señal insulínica (Morph en las seis diapositivas siguientes). El receptor de '
           'insulina es un receptor tirosina cinasa: un heterotetrámero α2β2. Las subunidades α son extracelulares y unen la '
           'hormona; las β atraviesan la membrana y contienen el dominio tirosina cinasa. En el citosol aparecen en gris los '
           'efectores todavía inactivos: IRS, PI3K, PDK1, Akt, AS160 y vesículas con GLUT4.')


def r1(D):
    s = new(D, U, 'Unión de insulina y autofosforilación', SEQ, morph=True)
    ids = sig_scene(s, 1)
    sig_panel(s, '2', 'Autofosforilación', '- La insulina se une a las subunidades α → **cambio conformacional**.\n- Los dominios cinasa β se **transfosforilan** en tirosinas.\n'
              '- Las fosfotirosinas (P) son **sitios de anclaje** para proteínas con dominios PTB/SH2.')
    sig_progress(s, [1, 2])
    i0 = mol(s, 1.42, 0.95, 'ins', d=0.5, name='Insulina llega')
    s.step(fade(i0), path(i0, 0.0, 0.65, dur=900), out(i0, after=True, dur=150))
    s.step(*[zoom(p, after=i > 0) for i, p in enumerate(ids['py'])])
    s.note('Paso 2. La insulina se une a las subunidades α (la ficha desciende hasta el receptor), lo que provoca un cambio '
           'conformacional que libera la autoinhibición: los dominios cinasa de las subunidades β se transfosforilan en residuos de '
           'tirosina. Esas fosfotirosinas aumentan la actividad cinasa y crean sitios de anclaje para los sustratos.')


def r2(D):
    s = new(D, U, 'Reclutamiento y fosforilación de IRS', SEQ, morph=True)
    ids = sig_scene(s, 2)
    sig_panel(s, '3', 'IRS-1 / IRS-2', '- Los **sustratos del receptor de insulina** se anclan a las fosfotirosinas.\n- El receptor los fosforila en **tirosinas** (P amarilla).\n'
              '- IRS funciona como **plataforma**: reúne efectores con dominios SH2.\n- La fosforilación en **serina/treonina** de IRS es inhibitoria (resistencia).')
    sig_progress(s, [3])
    s.step(pulse(ids['irs']), zoom(ids['irsp'], after=True))
    s.note('Paso 3. Mediante Morph, IRS-1/2 se desplaza desde el citosol hasta el receptor activado y es fosforilado en tirosinas. '
           'IRS actúa como plataforma de anclaje para proteínas con dominios SH2, en particular la subunidad reguladora de PI3K. '
           'Conviene retener desde ahora que la fosforilación de IRS en serina/treonina (por JNK, IKKβ o PKC) tiene el efecto '
           'opuesto: desacopla la señal (Unidad V, resistencia insulínica).')


def r3(D):
    s = new(D, U, 'Activación de PI3K y producción de PIP₃', SEQ, morph=True)
    ids = sig_scene(s, 3)
    sig_panel(s, '4–5', 'PI3K → PIP₃', '- La subunidad reguladora p85 se une a IRS-P; la catalítica p110 queda junto a la membrana.\n'
              '- PI3K fosforila **PIP₂ → PIP₃** (fosfatidilinositol-3,4,5-trisfosfato).\n- PIP₃ recluta proteínas con dominio **PH** a la membrana.')
    sig_progress(s, [4])
    s.step(pulse(ids['pi3k']), pulse(ids['pip'], after=True))
    s.note('Pasos 4 y 5. PI3K se une a IRS fosforilado y queda yuxtapuesta a la membrana, donde fosforila el fosfatidilinositol-4,5-'
           'bisfosfato (PIP2) en la posición 3 del inositol, generando PIP3 (Morph: la etiqueta PIP2 cambia a PIP3). El PIP3 es un '
           'lípido señalizador que recluta proteínas con dominio de homología a pleckstrina (PH), como PDK1 y Akt (ampliación '
           'bibliográfica sobre p85/p110 y dominios PH).')


def r4(D):
    s = new(D, U, 'PDK1 activa Akt', SEQ, morph=True)
    ids = sig_scene(s, 4)
    sig_panel(s, '6', 'Akt (PKB): el nodo metabólico', '- PDK1 y Akt se reclutan sobre PIP₃.\n- PDK1 (y mTORC2) **fosforilan Akt**.\n'
              '- Akt fosforila múltiples blancos: **AS160** (GLUT4), **GSK3** (glucógeno), **FOXO1** (gluconeogénesis), **PDE3B** (lipólisis), mTORC1.')
    sig_progress(s, [5])
    s.step(pulse(ids['pdk']), pulse(ids['akt'], after=True), zoom(ids['aktp'], after=True))
    s.note('Paso 6. PDK1 y Akt son reclutados a la membrana por el PIP3; PDK1 fosforila a Akt (la fosforilación completa requiere '
           'también mTORC2, ampliación bibliográfica). Akt activa es el nodo de la rama metabólica: fosforila AS160/TBC1D4 '
           '(translocación de GLUT4), GSK3 (desinhibe la glucógeno sintasa), FOXO1 (reduce la transcripción de PEPCK y '
           'glucosa-6-fosfatasa), PDE3B (frena la lipólisis) y la vía mTORC1–SREBP-1c (lipogénesis).')


def r5(D):
    s = new(D, U, 'AS160 → translocación de GLUT4 → entrada de glucosa', SEQ, morph=True)
    ids = sig_scene(s, 5)
    sig_panel(s, '7', 'GLUT4 a la membrana', '- Akt fosforila **AS160/TBC1D4** (una GAP de Rab) → Rab-GTP activos.\n'
              '- Las **vesículas con GLUT4** se mueven y **fusionan** con la membrana.\n- La glucosa entra por **difusión facilitada**.\n'
              '- Al cesar la señal, GLUT4 se reinternaliza por endocitosis.')
    sig_progress(s, [6, 7])
    gl = [mol(s, 6.95 + (i % 2) * 0.7, 1.15 + (i // 2) * 0.32, 'glc', d=0.42, name='Glc entra %d' % i) for i in range(4)]
    s.step(pulse(ids['as']))
    s.step(*[fade(m, after=i > 0, dur=150) for i, m in enumerate(gl)])
    s.step(*[path(m, 0.15, 2.4 + (i // 2) * 0.35, dur=1400, delay=i * 250) for i, m in enumerate(gl)])
    s.note('Paso 7. Akt fosforila AS160 (TBC1D4), una proteína activadora de GTPasa de Rab; al inhibirla, aumentan las Rab-GTP que '
           'dirigen las vesículas con GLUT4. En la transición Morph las vesículas viajan desde el citosol y se incorporan a la '
           'membrana; luego las fichas de glucosa ingresan a través de los transportadores. Este es el mecanismo de captación '
           'estimulada por insulina en músculo esquelético, músculo cardíaco y adipocitos. El hepatocito no depende de este '
           'mecanismo (diapositiva siguiente sobre hígado).')


def r6(D):
    s = new(D, U, 'Segunda rama: Ras–Raf–MEK–ERK', SEQ, morph=True)
    ids = sig_scene(s, 6)
    sig_panel(s, '8', 'Rama mitogénica', '- IRS/Shc reclutan **Grb2–SOS** → **Ras-GTP**.\n- Cascada **Raf → MEK → ERK** (MAPK).\n'
              '- ERK entra al núcleo: **expresión génica, crecimiento y proliferación**.\n- La rama PI3K–Akt es **principalmente metabólica**; la MAPK, mitogénica.')
    sig_progress(s, [])
    s.step(wipe(ids['mapk'], 't', dur=900))
    s.note('Dos grandes ramas explican los efectos de la insulina: IRS–PI3K–PIP3–PDK1–Akt, principalmente metabólica, y '
           'Ras–Raf–MEK–ERK, vinculada a proliferación y expresión génica. En estados de resistencia insulínica la rama metabólica '
           'suele estar más afectada que la mitogénica, de modo que la hiperinsulinemia compensatoria puede seguir estimulando '
           'la vía MAPK (ampliación bibliográfica; concepto de resistencia selectiva).')


def liver_branch(D):
    s = new(D, U, 'Hepatocito: la insulina regula el metabolismo, no el transporte', 'blue')
    hepatocyte(s, 0.35, 1.25, 3.4, name='Hepatocito señal')
    g2 = mbox(s, 0.6, 4.25, 2.9, 0.55, 'GLUT2: entrada sin insulina', 'g', 13.5, caps=False)
    nodes = {
        'ak': (4.3, 1.3, 1.6, 0.6, 'Akt', 'g', 18),
        'fx': (6.6, 1.3, 2.0, 0.6, 'FOXO1-P', 'w', 15),
        'fx2': (9.3, 1.3, 3.6, 0.6, 'PEPCK (PCK1) · G6Pasa (G6PC) ↓', 'Y', 13.5),
        'gsk': (6.6, 2.55, 2.0, 0.6, 'GSK3', 'w', 15),
        'gs': (9.3, 2.55, 3.6, 0.6, 'Glucógeno sintasa activa', 'Y', 14),
        'mt': (6.6, 3.8, 2.0, 0.6, 'mTORC1', 'g', 15),
        'sr': (9.3, 3.8, 3.6, 0.6, 'SREBP-1c → lipogénesis', 'Y', 14),
        'o1': (4.3, 5.2, 4.3, 0.75, 'Gluconeogénesis ↓ · glucogenólisis ↓', 'r', 15),
        'o2': (8.85, 5.2, 4.05, 0.75, 'Glucógeno ↑ · TAG/VLDL ↑', 'r', 15),
    }
    edges = [('ak', 'fx', {'lab': 'fosforila → exclusión nuclear', 'ls': 10, 'oy': -0.32}), ('fx', 'fx2', {'inh': True}),
             ('ak', 'gsk', {'inh': True, 'pts': [(5.1, 1.95), (5.1, 2.85), (6.55, 2.85)]}), ('gsk', 'gs', {'inh': True}),
             ('ak', 'mt', {'pts': [(4.9, 1.95), (4.9, 4.1), (6.55, 4.1)], 'col': ACT}), ('mt', 'sr', {'col': ACT}),
             ('fx2', 'o1', {'pts': [(11.1, 1.95), (11.1, 2.2), (6.45, 2.2), (6.45, 5.15)], 'dash': 'dash'}),
             ('gs', 'o2', {'pts': [(12.6, 3.2), (12.6, 5.15)]}), ('sr', 'o2', {'pts': [(10.5, 4.45), (10.5, 5.15)]})]
    graph(s, nodes, edges, [['ak'], ['ak>fx', 'fx', 'fx>fx2', 'fx2'], ['ak>gsk', 'gsk', 'gsk>gs', 'gs'], ['ak>mt', 'mt', 'mt>sr', 'sr'],
                            ['fx2>o1', 'o1', 'gs>o2', 'sr>o2', 'o2']])
    pp = pearl(s, 0.4, 6.1, 12.5, 0.8, 'Error frecuente: «toda acción de la insulina pasa por GLUT4». En el hígado el transporte es por **GLUT2**; la insulina cambia **qué hace** el hepatocito con la glucosa.', 14.5)
    s.step(fade(g2)); s.step(zoom(pp))
    s.note('Rama hepática. El hepatocito utiliza predominantemente GLUT2, de alta capacidad: la entrada de glucosa no depende de la '
           'insulina. Allí la insulina regula la utilización y la producción de glucosa. Akt inactiva funcionalmente a FOXO1 '
           '(fosforilación y exclusión nuclear), lo que reduce la transcripción de PEPCK (PCK1) y glucosa-6-fosfatasa (G6PC). Akt '
           'inhibe a GSK3, de modo que la glucógeno sintasa queda activa. Por la vía mTORC1–SREBP-1c favorece los programas '
           'lipogénicos. Resultado: menos gluconeogénesis y glucogenólisis, más glucógeno y más síntesis de triglicéridos/VLDL.')


def adipo_branch(D):
    s = new(D, U, 'Adipocito: la insulina frena la lipólisis', 'yellow' if False else 'green')
    s.pic('adipocyte-1', 0.35, 1.3, 3.2, name='Adipocito señal')
    nodes = {
        'ak': (4.1, 1.35, 1.7, 0.6, 'Akt', 'g', 18),
        'pde': (6.4, 1.35, 2.2, 0.6, 'PDE3B', 'g', 17),
        'camp': (9.2, 1.35, 3.6, 0.6, 'AMPc → 5′-AMP', 'y', 15),
        'pka': (9.2, 2.6, 3.6, 0.6, 'PKA ↓', 'w', 16),
        'hsl': (9.2, 3.85, 3.6, 0.6, 'HSL y perilipina 1 sin fosforilar', 'Y', 13.5),
        'o': (4.1, 3.85, 4.5, 0.6, 'LIPÓLISIS ↓ · salida de AGNE ↓', 'r', 15),
        'g4': (4.1, 2.6, 4.5, 0.6, 'GLUT4 → glicerol-3-P · esterificación ↑', 'Y', 13.5),
    }
    edges = [('ak', 'pde', {'col': ACT}), ('pde', 'camp', {'lab': 'degrada', 'ls': 10}), ('camp', 'pka'), ('pka', 'hsl'), ('hsl', 'o'),
             ('ak', 'g4', {'col': ACT, 'pts': [(4.95, 1.98), (4.95, 2.56)]})]
    graph(s, nodes, edges, [['ak'], ['ak>pde', 'pde', 'pde>camp', 'camp'], ['camp>pka', 'pka', 'pka>hsl', 'hsl'], ['hsl>o', 'o'], ['ak>g4', 'g4']])
    t = tbox(s, 0.4, 4.75, 12.5, 2.1, '- La lipólisis fisiológica permite sobrevivir entre comidas; el problema aparece cuando el freno insulínico falla.\n'
             '- **CAD**: el freno desaparece → gran flujo de AGNE al hígado → cetogénesis.\n- **EHH**: la insulina residual suele **conservar el freno** → pocas cetonas aun con glucemia muy alta.', 15,
             head='Una vía, dos emergencias')
    s.step(fade(t))
    s.note('En el adipocito la insulina activa, vía Akt, la fosfodiesterasa 3B, que degrada el AMPc; disminuye la actividad de PKA y '
           'quedan sin fosforilar la lipasa sensible a hormonas y la perilipina 1: la lipólisis se frena. Simultáneamente aumenta '
           'GLUT4 y el aporte de glicerol-3-fosfato para esterificar ácidos grasos. Ejemplo integrador: en la CAD desaparece el freno '
           'insulínico y el hígado recibe sustrato para cetogénesis; en el EHH la insulina residual suele frenar lo suficiente a las '
           'lipasas como para reducir las cetonas, aun sin lograr euglucemia. Una sola vía del adipocito explica la diferencia '
           'entre los dos casos clínicos.')


def exercise_glut4(D):
    s = new(D, U, 'Ejercicio: GLUT4 sin depender de la insulina', 'cyanR')
    s.pic('runner', 0.5, 1.2, h=4.0, name='Corredor')
    nodes = {
        'c': (2.9, 1.35, 3.0, 0.6, 'Contracción muscular', 's', 16),
        'ca': (2.9, 2.5, 1.4, 0.6, 'Ca^{2+} ↑ · CaMK', 'g', 13),
        'am': (4.5, 2.5, 1.4, 0.6, 'AMP/ATP ↑ · AMPK', 'g', 13),
        'me': (2.9, 3.65, 3.0, 0.55, 'Señales mecánicas', 'g', 14),
        'g4': (6.6, 2.5, 3.0, 0.65, 'Translocación GLUT4', 'y', 16),
        'o': (10.2, 2.5, 2.75, 0.65, 'Glucemia ↓', 'r', 17),
        'o2': (6.6, 3.65, 6.35, 0.6, 'Sostenido: sensibilidad insulínica ↑ · capacidad mitocondrial ↑', 'Y', 14),
    }
    edges = [('c', 'ca'), ('c', 'am'), ('ca', 'g4', {'pts': [(3.6, 3.12), (3.6, 3.35), (6.3, 3.35), (6.6, 3.0)], 'col': ACT}),
             ('am', 'g4', {'col': ACT}), ('me', 'g4', {'pts': [(5.95, 3.92), (6.4, 3.15)], 'col': ACT}), ('g4', 'o'), ('g4', 'o2')]
    graph(s, nodes, edges, [['c'], ['c>ca', 'ca', 'c>am', 'am', 'me'], ['ca>g4', 'am>g4', 'me>g4', 'g4'], ['g4>o', 'o'], ['g4>o2', 'o2']])
    t = tbox(s, 0.4, 5.3, 12.5, 1.55, 'Fuerza: preserva masa magra y depósito de glucosa como glucógeno · aeróbico: capacidad oxidativa, función endotelial y gasto. '
             'Nunca se inicia ejercicio durante una **crisis hiperglucémica descompensada**; se evalúan riesgo CV, neuropatía, retinopatía, pies e hipoglucemia.', 14.5, head='Aplicación clínica')
    s.step(fade(t))
    s.note('El ejercicio muscular puede llevar GLUT4 a la membrana por vías AMPK, Ca²⁺/CaMK y señales mecánicas, relativamente '
           'independientes de la insulina: por eso la glucemia desciende durante la actividad aun con baja señal insulínica, y el '
           'entrenamiento sostenido mejora la sensibilidad a la insulina y la capacidad mitocondrial. Es la base fisiológica de la '
           'pregunta 9 del caso 12 (actividad física moderada) y de la pregunta 7 de opción múltiple.')


def counter(D):
    s = new(D, U, 'Hormonas contrarreguladoras', 'pink')
    data = [('GLUCAGÓN', 'Gs → AMPc → PKA en hígado: **glucogenólisis y gluconeogénesis ↑**, síntesis de glucógeno ↓, modula oxidación de lípidos.', 'pancreas'),
            ('CATECOLAMINAS', 'Movilizan reservas: **lipólisis ↑** (β-adrenérgicos), glucogenólisis; ajustan flujo sanguíneo.', 'heart-front'),
            ('CORTISOL', 'Induce **enzimas gluconeogénicas**, resistencia a insulina y **proteólisis** en escenarios crónicos.', 'kidney-2'),
            ('HORMONA DE CRECIMIENTO', 'Reduce la utilización periférica de glucosa y favorece la **lipólisis**.', 'brain-2')]
    ids = []
    for i, (h, t, img) in enumerate(data):
        x = 0.4 + (i % 2) * 6.35; y = 1.2 + (i // 2) * 2.2
        g = s.group_start('Contrarreg ' + h)
        fitpic(s, img, x, y + 0.1, 1.4, 1.75)
        mbox(s, x + 1.55, y, 4.55, 0.5, h, 'y', 15)
        tbox(s, x + 1.55, y + 0.6, 4.55, 1.35, t, 14.5, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 5.75, 12.5, 1.05, '**Menos insulina + más señales contrarreguladoras** = catabolismo: explica la CAD y por qué una **infección** (estrés) puede descompensar a una persona con diabetes.', 16)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Hormonas contrarreguladoras. El glucagón actúa en el hígado por Gs → adenilil ciclasa → AMPc → PKA: favorece '
           'glucogenólisis y gluconeogénesis, reduce la síntesis de glucógeno y modula la oxidación de lípidos. Las catecolaminas '
           'movilizan reservas, aumentan la lipólisis y ajustan el flujo sanguíneo. El cortisol induce enzimas gluconeogénicas, '
           'resistencia a la insulina y proteólisis en escenarios crónicos. La hormona de crecimiento reduce la utilización '
           'periférica de glucosa y favorece la lipólisis. La combinación de menos insulina y más señales contrarreguladoras '
           'explica el catabolismo de la cetoacidosis (los íconos de órganos indican fuente o blanco representativo).')


def glyco_gng(D):
    s = new(D, U, 'Glucólisis y gluconeogénesis: pasos regulados', 'cyan')
    m = model(s, 'glucosa', 0.35, 1.0, 1.45, name='Glucosa 3D vía')
    nodes = {
        'g': (2.0, 1.2, 2.2, 0.55, 'GLUCOSA', 'y', 15),
        'g6p': (2.0, 2.35, 2.2, 0.55, 'GLUCOSA-6-P', 'y', 14),
        'f6p': (2.0, 3.45, 2.2, 0.55, 'FRUCTOSA-6-P', 'y', 14),
        'fbp': (2.0, 4.55, 2.2, 0.55, 'FRUCTOSA-1,6-BP', 'y', 13),
        'pep': (2.0, 5.65, 2.2, 0.55, 'FOSFOENOLPIRUVATO', 'y', 12.5),
        'pyr': (5.6, 5.65, 2.0, 0.55, 'PIRUVATO', 'y', 15),
        'oaa': (5.6, 4.3, 2.0, 0.55, 'OXALACETATO', 'y', 14),
        'acoa': (8.6, 5.65, 2.0, 0.55, 'ACETIL-COA', 'y', 15),
        'lac': (4.9, 6.6, 2.0, 0.42, 'Lactato (Cori)', 's', 12.5),
        'ala': (7.25, 6.6, 2.2, 0.42, 'Alanina (Cahill)', 's', 12.5),
        'gly': (8.6, 2.9, 4.3, 0.5, 'Glicerol (lipólisis) → DHAP', 's', 13),
    }
    edges = [('g', 'g6p', {'lab': 'Hexocinasa / GCK', 'ls': 10, 'ox': -1.15}), ('g6p', 'g', {'lab': 'G6Pasa (hígado)', 'ls': 10, 'ox': 1.2, 'col': '0070C0',
              'pts': [(3.6, 2.33), (3.6, 1.77)]}), ('g6p', 'f6p'), ('f6p', 'fbp', {'lab': 'PFK-1 (regulador)', 'ls': 10, 'ox': -1.2}),
             ('fbp', 'f6p', {'lab': 'FBPasa-1', 'ls': 10, 'ox': 0.95, 'col': '0070C0', 'pts': [(3.6, 4.53), (3.6, 4.02)]}),
             ('fbp', 'pep'), ('pep', 'pyr', {'lab': 'PK', 'ls': 10, 'oy': -0.3}), ('pyr', 'oaa', {'lab': 'Piruvato carboxilasa (PC)', 'ls': 10, 'ox': -1.25, 'col': '0070C0'}),
             ('oaa', 'pep', {'lab': 'PEPCK', 'ls': 10, 'col': '0070C0', 'pts': [(5.55, 4.6), (4.25, 5.8)], 'oy': -0.25}),
             ('pyr', 'acoa', {'lab': 'PDH', 'ls': 10, 'oy': -0.3}), ('acoa', 'oaa', {'pts': [(9.2, 5.62), (9.2, 4.57), (7.65, 4.57)], 'col': ACT}),
             ('lac', 'pyr', {'pts': [(5.95, 6.6), (6.1, 6.23)], 'dash': 'dash', 'col': TRN}), ('ala', 'pyr', {'pts': [(8.0, 6.6), (7.0, 6.23)], 'dash': 'dash', 'col': TRN}),
             ('gly', 'fbp', {'pts': [(8.55, 3.15), (4.6, 3.15), (4.6, 4.8), (4.25, 4.8)], 'dash': 'dash', 'col': TRN})]
    ids = graph(s, nodes, edges, [['g', 'g>g6p', 'g6p', 'g6p>f6p', 'f6p', 'f6p>fbp', 'fbp', 'fbp>pep', 'pep', 'pep>pyr', 'pyr'],
                                  ['pyr>acoa', 'acoa'], ['pyr>oaa', 'oaa', 'oaa>pep', 'fbp>f6p', 'g6p>g'],
                                  ['acoa>oaa'], ['lac', 'lac>pyr', 'ala', 'ala>pyr', 'gly', 'gly>fbp']])
    inh = s.inhib([(10.65, 5.92), (11.1, 5.92), (11.1, 6.55), (8.15, 6.55), (8.15, 6.0)], name='Acetil-CoA inhibe PDH')
    tl = lab(s, 9.65, 6.6, 1.5, 0.3, '− inhibe PDH', 11, INH)
    ta = lab(s, 9.3, 4.85, 1.6, 0.3, '+ activa PC', 11, ACT)
    s.step(fade(ta), wipe(inh, 'r'), fade(tl, after=True))
    s.note('Glucólisis: glucosa → glucosa-6-P (hexocinasa/glucocinasa) → fructosa-1,6-bisfosfato (PFK-1, paso regulador) → '
           'piruvato; aporta ATP y NADH. Gluconeogénesis (flechas azules): lactato (ciclo de Cori), alanina (ciclo de Cahill), '
           'glicerol y otros precursores → glucosa, rodeando los pasos irreversibles con piruvato carboxilasa, PEPCK, '
           'fructosa-1,6-bisfosfatasa y glucosa-6-fosfatasa. La acetil-CoA generada por β-oxidación activa la piruvato '
           'carboxilasa e inhibe la piruvato deshidrogenasa, desviando el carbono hacia la gluconeogénesis. Animación: primero el '
           'eje glucolítico, luego la PDH, luego los rodeos gluconeogénicos, la regulación por acetil-CoA y los precursores.')


def betaox_keto(D):
    s = new(D, U, 'β-oxidación y cetogénesis: el freno del malonil-CoA', 'green')
    model(s, 'palmitato', 0.3, 1.05, 3.4, hs=False, name='Palmitato 3D', label='Ácido graso (palmitato)')
    nodes = {
        'ac': (4.2, 1.3, 2.3, 0.55, 'ACIL-COA', 'y', 15),
        'cpt': (4.2, 2.45, 2.3, 0.6, 'CPT1 · carnitina', 'g', 14),
        'mal': (0.5, 2.45, 2.6, 0.6, 'MALONIL-COA', 'y', 14),
        'box': (4.2, 3.6, 2.3, 0.55, 'β-oxidación', 'w', 15),
        'acoa': (4.2, 4.7, 2.3, 0.55, 'ACETIL-COA', 'y', 15),
        'k': (7.3, 4.7, 2.3, 0.55, 'Krebs (con OAA)', 'w', 14),
        'hmg': (4.2, 5.85, 2.3, 0.55, 'HMG-CoA', 'y', 15),
        'aca': (7.3, 5.85, 2.3, 0.55, 'ACETOACETATO', 'y', 13.5),
        'bhb': (10.5, 5.85, 2.45, 0.55, 'β-HIDROXIBUTIRATO', 'y', 12.5),
        'per': (10.5, 4.55, 2.45, 0.75, 'Tejidos periféricos:\nSCOT → acetil-CoA', 'g', 12.5),
    }
    edges = [('ac', 'cpt'), ('mal', 'cpt', {'inh': True}), ('cpt', 'box'), ('box', 'acoa'), ('acoa', 'k'), ('acoa', 'hmg', {'lab': 'HMGCS2', 'ls': 10.5, 'ox': -0.95}),
             ('hmg', 'aca', {'lab': 'HMG-CoA liasa', 'ls': 10, 'oy': -0.3}), ('aca', 'bhb', {'lab': 'NADH', 'ls': 10, 'oy': -0.3, 'both': True}),
             ('bhb', 'per', {'col': TRN, 'dash': 'dash'})]
    graph(s, nodes, edges, [['ac', 'ac>cpt', 'cpt'], ['mal', 'mal>cpt'], ['cpt>box', 'box', 'box>acoa', 'acoa', 'acoa>k', 'k'],
                            ['acoa>hmg', 'hmg', 'hmg>aca', 'aca', 'aca>bhb', 'bhb'], ['bhb>per', 'per']])
    t = tbox(s, 7.25, 1.25, 5.7, 3.05, '- **Insulina alta** → ACC activa → malonil-CoA ↑ → CPT1 frenada.\n- **Insulina/glucagón baja** → malonil-CoA ↓ → los ácidos grasos entran a la mitocondria.\n'
             '- Acetil-CoA ↑ + OAA desviado a gluconeogénesis → **cetogénesis**.\n- La acetona deriva de la descarboxilación del acetoacetato.\n- El **hígado no oxida** sus cuerpos cetónicos: carece de **SCOT** (OXCT1).', 14, head='Regulación')
    s.step(fade(t))
    s.note('β-oxidación y cetogénesis. El ácido graso activado como acil-CoA entra a la mitocondria por la lanzadera de carnitina, '
           'regulada por CPT1; el malonil-CoA (producto de la acetil-CoA carboxilasa, favorecida por la insulina) inhibe la CPT1. '
           'Con relación insulina/glucagón reducida disminuye la señal lipogénica y aumenta la entrada de ácidos grasos a la '
           'mitocondria. El exceso de acetil-CoA, junto al desvío de oxalacetato hacia la gluconeogénesis, favorece la síntesis de '
           'acetoacetato y β-hidroxibutirato mediante HMG-CoA sintasa mitocondrial (HMGCS2) y HMG-CoA liasa; la acetona deriva de '
           'la descarboxilación del acetoacetato. El hígado no oxida sus cuerpos cetónicos por ausencia de SCOT/OXCT1; los tejidos '
           'periféricos sí los utilizan para regenerar acetil-CoA.')


def key_idea(D):
    s = new(D, U, 'Clave integradora: ayuno extremo en medio de la abundancia', 'band')
    a = s.group_start('Exterior')
    mbox(s, 0.5, 1.3, 5.8, 0.75, 'MUCHA GLUCOSA EXTRACELULAR', 'y', 19)
    for i in range(12):
        mol(s, 0.7 + (i % 6) * 0.95, 2.25 + (i // 6) * 0.55, 'glc', d=0.45, name='Glc exterior %d' % i)
    s.group_end()
    b = s.group_start('Interior')
    s.shape(7.0, 1.3, 5.85, 2.0, 'roundRect', ('lin', [(0, 'FDEDEC'), (100, 'F5B7B1')], 90), ('B03A2E', 2.5), SHD, adj={'adj': 15000})
    mbox(s, 7.3, 1.55, 5.25, 0.65, 'ESCASA SEÑAL INSULÍNICA INTRACELULAR', 's', 15)
    s.text(7.3, 2.35, 5.25, 0.8, 'La célula «interpreta» ayuno: lipólisis, cetogénesis, gluconeogénesis y proteólisis.', 15, F_BODY, INK, False, 'c', 'm')
    s.group_end()
    c = pearl(s, 0.5, 4.3, 12.35, 1.1, 'En la DM1 descompensada el problema **no es falta de glucosa corporal**: coexisten hiperglucemia con un **metabolismo de ayuno extremo**.', 18)
    d = tbox(s, 0.5, 5.65, 12.35, 1.2, 'Detalle fino: el hígado mantiene entrada de glucosa por GLUT2 aun sin insulina — el problema allí es la **regulación hormonal**. '
             'El músculo **no posee glucosa-6-fosfatasa** funcional para liberar glucosa al plasma.', 15)
    s.step(fade(a)); s.step(fade(b)); s.step(zoom(c)); s.step(fade(d))
    s.note('Clave integradora: en la DM1 descompensada hay mucha glucosa extracelular y escasez de señal insulínica intracelular; '
           'coexisten hiperglucemia y un metabolismo de ayuno extremo. No toda vía opera igual en todos los órganos: el hígado '
           'mantiene entrada de glucosa por GLUT2 sin insulina (el problema es la regulación de su metabolismo) y el músculo no '
           'posee glucosa-6-fosfatasa funcional, por lo que su glucógeno no aporta glucosa libre a la sangre.')


def build(D):
    action(D)
    r0(D)
    r1(D)
    r2(D)
    r3(D)
    r4(D)
    r5(D)
    r6(D)
    liver_branch(D)
    adipo_branch(D)
    exercise_glut4(D)
    counter(D)
    glyco_gng(D)
    betaox_keto(D)
    key_idea(D)
