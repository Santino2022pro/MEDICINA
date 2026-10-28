# -*- coding: utf-8 -*-
"""UNIDAD II (parte 2): catabolismo y anabolismo, regulación metabólica, macronutrientes,
acetil-CoA, piruvato e ingreso del piruvato a la mitocondria (Morph)."""
from plantillas import *


def cat_anab(D):
    s = nueva(D, 2, 'Catabolismo y anabolismo', src=['TM 6 Catabolismo y anabolismo'], tipo='bandas', c1=ROSA, c2=VERDE_CL)
    # catabolismo (izq): molécula compleja se rompe
    comp = s.group_start('!!Macromolécula')
    for k in range(7):
        s.shape(0.5 + k * 0.38, 1.6 + (k % 2) * 0.25, 0.42, 0.42, 'hexagon', shade('3B82C4', 0.35, 0.2), ('1B4F72', 1.0), False, adj={'adj': 28000, 'vf': 115470})
    s.group_end()
    sim = s.group_start('Moléculas simples')
    for k, (t, c) in enumerate((('CO_{2}', '95A5A6'), ('H_{2}O', '85C1E9'), ('NH_{3}', '16A085'))):
        ficha(s, 0.45 + k * 0.95, 3.3, t, c, w=0.9, h=0.4, size=12)
    s.group_end()
    ene = s.group_start('Energía obtenida')
    for k, (t, c) in enumerate((('ATP', 'FFC000'), ('NADH', '1F618D'), ('FADH_{2}', 'F4D03F'))):
        ficha(s, 0.45 + k * 0.95, 4.1, t, c, w=0.9, h=0.4, size=12)
    s.group_end()
    fc = s.arrow([(1.6, 2.2), (1.6, 3.2)], ROJO, 4, name='Flecha catabolismo')
    # anabolismo (der)
    sim2 = s.group_start('Precursores simples')
    for k in range(5):
        s.shape(10.5 + k * 0.5, 4.2, 0.4, 0.4, 'hexagon', shade('58D68D', 0.35, 0.2), ('1E8449', 1.0), False, adj={'adj': 28000, 'vf': 115470})
    s.group_end()
    comp2 = s.group_start('Macromolécula sintetizada')
    for k in range(7):
        s.shape(10.4 + k * 0.38, 1.6 + (k % 2) * 0.25, 0.42, 0.42, 'hexagon', shade('27AE60', 0.35, 0.2), ('145A32', 1.0), False, adj={'adj': 28000, 'vf': 115470})
    s.group_end()
    gasto = s.group_start('Energía consumida')
    ficha(s, 10.5, 3.2, 'ATP', 'FFC000', w=0.9, h=0.4, size=12)
    ficha(s, 11.5, 3.2, 'NADPH', 'AF7AC5', w=1.1, h=0.4, size=12)
    s.group_end()
    fa = s.arrow([(11.7, 4.15), (11.7, 2.2)], VERDE_OSC, 4, name='Flecha anabolismo')
    rows = [['', 'CATABOLISMO', 'ANABOLISMO'], ['ΔG', 'ΔG < 0: espontáneo (exergónico)', 'ΔG > 0: no espontáneo (endergónico)'],
            ['Dirección', 'Complejas → simples (CO_{2}, H_{2}O, NH_{3})', 'Simples → complejas'], ['Energía', '**Se obtiene** (ATP, NADH, FADH_{2})', '**Se consume** (ATP, NADPH)'],
            ['Ejemplos', 'Glucólisis, ciclo de Krebs', 'Síntesis de glucógeno, proteínas y ácidos grasos']]
    ids, H = tabla_filas(s, 3.55, 1.2, [1.35, 2.75, 2.75], rows, rowh=0.95, size=14.5, name='Tabla cat anab', col_fills=[None, 'FCE4EC', 'E9F7EF'])
    ac = caja(s, 3.55, 1.4 + H, 6.85, 6.95 - (1.4 + H), 'El anabolismo es posible porque está **acoplado al catabolismo**: la energía de las reacciones degradativas paga las de síntesis.', AMA, 15,
              name='Acoplamiento cat anab')
    s.step(fade(ids[0]))
    s.step(fade(comp), wipe(fc, 't', after=True), fade(sim, after=True), fade(ene, after=True))
    s.step(fade(sim2), wipe(fa, 'b', after=True), fade(comp2, after=True), fade(gasto, after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(ac))


def clave_redox(D):
    s = nueva(D, 2, 'Clave metabólica: coenzimas reducidas como puente', src=['TM 6 Catabolismo y anabolismo', 'REV TM 6'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    cic = s.group_start('!!Ciclo del hambre')
    cx, cy, R = 4.3, 3.9, 2.2
    etapas = [('Comemos', 'F5B041'), ('Catabolismo', 'F1948A'), ('Obtenemos NADH', '1F618D'), ('Anabolismo', '58D68D'), ('Gastamos NADH', 'AED6F1'), ('Hambre', 'F7DC6F')]
    for k, (t, c) in enumerate(etapas):
        a = -math.pi / 2 + 2 * math.pi * k / 6
        ficha(s, cx + R * math.cos(a) - 0.95, cy + R * math.sin(a) - 0.27, t, c, w=1.9, h=0.54, size=14)
        a2 = a + 2 * math.pi / 12
        s.shape(cx + (R - 0.05) * math.cos(a2) - 0.17, cy + (R - 0.05) * math.sin(a2) - 0.17, 0.34, 0.34, 'rightArrow', INK, None, False, rot=math.degrees(a2) + 90)
    s.group_end()
    c1 = caja(s, 9.35, 1.2, 3.7, 2.4, 'En el **catabolismo** se generan coenzimas **reducidas** (NADH, FADH_{2}): se obtiene energía.', ROSA, 15, head='Catabolismo', headfill=ROJO, name='Cat redox')
    c2 = caja(s, 9.35, 3.85, 3.7, 1.7, 'En el **anabolismo** las coenzimas reducidas **ceden** su energía y vuelven a la forma oxidada.', 'EAF5EA', 14.5, head='Anabolismo',
              headfill=VERDE_OSC, name='Anab redox')
    r_ = rigor(s, 9.35, 5.75, 3.7, 1.3, 'Los **sustratos se oxidan**; las **coenzimas se reducen**. En las síntesis se usa sobre todo **NADPH**.', 12.5, name='Rigor redox cat')
    s.step(wipe(cic, 'l', dur=1000))
    s.step(fade(c1))
    s.step(fade(c2))
    s.step(fade(r_))


def reversibilidad(D):
    s = nueva(D, 2, 'Reacciones reversibles e irreversibles', src=['TM 7.1 Reversibilidad'], tipo='izq', c1=CREMA, c2=BLANCO)
    ruta = chain(s, 1.1, 1.5, ['Sustrato A', 'B', 'C', 'D', 'Producto final'], dy=1.08, w=2.2, rev=[False, True, True, True], fill=[AMA, CREMA, CREMA, CREMA, 'D5F5E3'],
                 size=15, name='Vía', h=0.5)
    comp = rotulo(s, 3.45, 2.1, 'irreversible', ROJO, 13, name='Primer paso')
    rev = rotulo(s, 3.45, 3.75, 'reversibles', NAVY, 13, name='Pasos reversibles')
    c1 = caja(s, 5.3, 1.2, 7.75, 1.6, '**Reversible (⇄)**: puede ocurrir en ambos sentidos según las condiciones; los metabolismos tienen muchos pasos reversibles.', CELESTE, 16, name='Reversible')
    c2 = caja(s, 5.3, 3.05, 7.75, 1.6, '**Irreversible (→)**: ocurre en un solo sentido. Casi siempre el **primer paso** de una vía es irreversible.', ROSA, 16, name='Irreversible')
    c3 = caja(s, 5.3, 4.9, 7.75, 2.15, '¿Por qué? Para que el sustrato quede **comprometido** con esa vía y no pueda derivarse a otra: es el principal mecanismo de control.', AMA, 16,
              head='Compromiso', name='Compromiso')
    s.step(fade(ruta[0][0]))
    s.step(wipe(ruta[1][1], 't'), fade(ruta[1][0], after=True), fade(comp, after=True), fade(c2, after=True))
    s.step(*[e for k, (m, st) in enumerate(ruta[2:]) for e in (wipe(st, 't', after=(k > 0)), fade(m, after=True))], fade(rev, after=True), fade(c1, after=True))
    s.step(fade(c3))


def control_mecanismos(D):
    s = nueva(D, 2, 'Mecanismos de control: alostérico y covalente', src=['TM 7.2 Mecanismos de control'], tipo='bandas', c1=VERDE_CL, c2=CELESTE)
    # alostérico
    al = s.group_start('Feedback negativo')
    ch = [('Sustrato', AMA), ('Intermediario', CREMA), ('Producto final', 'D5F5E3')]
    for k, (t, f) in enumerate(ch):
        ficha(s, 0.5 + k * 2.0, 1.6, t, f, w=1.8, h=0.5, size=13)
        if k < 2:
            s.arrow([(2.32 + k * 2.0, 1.85), (2.48 + k * 2.0, 1.85)], INK, 2.5)
    enzima_globular(s, 0.6, 2.4, 1.4, 1.1, 'E59866', 'Enzima 1', 'Primera enzima', size=13)
    s.group_end()
    fb = s.inhib([(5.3, 2.15), (5.3, 3.6), (2.1, 3.6), (2.05, 3.35)], name='Retroinhibición')
    c1 = caja(s, 0.4, 4.0, 6.0, 3.05, '**Regulación alostérica (feedback negativo)**: el **producto final** inhibe alostéricamente a la **primera enzima**. Mucho producto → se frena la vía; poco producto → se activa.',
              BLANCO, 15, name='Alostérica')
    # covalente
    cv = s.group_start('Fosforilación')
    enzima_globular(s, 7.2, 1.5, 1.6, 1.3, '82E0AA', 'Enzima', 'Enzima desfosforilada', size=14, seed=4)
    enzima_globular(s, 10.5, 1.5, 1.6, 1.3, 'ABB2B9', 'Enzima', 'Enzima fosforilada', size=14, seed=4)
    s.shape(11.85, 1.45, 0.48, 0.48, 'ellipse', shade('F39C12', 0.4, 0.2), (INK, 1.25), False, 'P', 15, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.arrow([(8.9, 1.9), (10.4, 1.9)], INK, 2.5)
    s.arrow([(10.4, 2.5), (8.9, 2.5)], INK, 2.5)
    rotulo(s, 9.0, 1.3, 'quinasa', AMA, 13, w=1.3)
    rotulo(s, 9.0, 2.65, 'fosfatasa', CELESTE, 13, w=1.3)
    s.group_end()
    c2 = caja(s, 6.9, 4.0, 6.0, 3.05, '**Modificación covalente**: una **quinasa** fosforila la enzima clave y la activa o inactiva (según el caso); una **fosfatasa** la desfosforila con el efecto contrario. Mecanismo usado por las vías de comunicación celular (PKA, PKC).',
              BLANCO, 15, name='Covalente')
    s.step(fade(al))
    s.step(wipe(fb, 'r'), fade(c1, after=True))
    s.step(fade(cv))
    s.step(fade(c2))


def control_mecanismos2(D):
    s = nueva(D, 2, 'Mecanismos de control: ciclos de sustrato y control génico', src=['TM 7.2 Mecanismos de control'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    cic = s.group_start('Ciclo de sustrato')
    ficha(s, 0.6, 2.2, 'B', AMA, w=1.0, h=0.6, size=18)
    ficha(s, 3.2, 2.2, 'C', CELESTE, w=1.0, h=0.6, size=18)
    s.arrow([(1.7, 2.3), (2.4, 1.8), (3.1, 2.3)], INK, 2.5, curve=True)
    s.arrow([(3.1, 2.75), (2.4, 3.25), (1.7, 2.75)], INK, 2.5, curve=True)
    s.arrow([(4.3, 2.5), (5.0, 2.5)], VERDE_OSC, 3)
    ficha(s, 5.05, 2.2, 'Producto', 'D5F5E3', w=1.6, h=0.6, size=15)
    s.group_end()
    c1 = caja(s, 0.4, 3.75, 6.6, 1.3, '**Ciclos de sustrato**: el sustrato alterna entre dos formas (B ⇄ C); según cuál predomine, se activa o inhibe la producción del producto final.',
              CREMA, 14.5, name='Ciclos')
    gen = s.group_start('Control génico')
    s.shape(0.6, 5.55, 5.0, 0.32, 'rect', ('lin', [(0, '5DADE2'), (100, '2E86C1')], 0), (INK, 1.0), False)
    s.shape(0.6, 5.55, 1.2, 0.32, 'rect', AMA2, (INK, 1.0), False, 'promotor', 11, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    texto(s, 1.9, 5.95, 3.7, 0.35, 'gen de la enzima (ej. lactasa)', 13, NAVY, True, 'c')
    ficha(s, 0.35, 6.45, 'Lactosa', 'F7DC6F', w=1.2, h=0.42, size=12)
    s.arrow([(1.0, 6.4), (1.1, 5.95)], VERDE_OSC, 2.5)
    s.arrow([(5.7, 5.7), (6.4, 5.7)], INK, 2.5)
    enzima_globular(s, 6.5, 5.15, 1.3, 1.1, 'BB8FCE', 'Lactasa', 'Lactasa', size=12, seed=2)
    s.group_end()
    c2 = caja(s, 9.35, 1.2, 3.7, 5.85, '**Control génico**: si el sustrato está presente, activa la región **promotora** del gen que codifica la enzima → se produce la enzima → ocurre el metabolismo.\n'
              'Sin sustrato no se transcribe el gen → no hay enzima → no hay metabolismo.\nEjemplo: sistema **lactasa/lactosa**.', BLANCO, 15, head='Control génico', name='Génico')
    s.step(fade(cic), fade(c1, after=True))
    s.step(wipe(gen, 'l', dur=900))
    s.step(fade(c2))


def macronutrientes(D):
    s = nueva(D, 2, 'Macronutrientes y micronutrientes', src=['TM 8.1 Macronutrientes'], tipo='izq', c1=DURAZNO_CL, c2=BLANCO)
    rows = [['Macronutriente', 'Unidad básica', 'Función principal'],
            ['Hidratos de carbono', 'Monosacáridos (glucosa, fructosa, galactosa)', 'Fuente **inmediata** de energía; componente del glucocáliz.'],
            ['Lípidos', 'Ácidos grasos / colesterol', 'Almacenamiento **a largo plazo**; membranas (fosfolípidos); precursores hormonales.'],
            ['Proteínas', 'Aminoácidos (20 tipos)', 'Función **estructural y funcional**: expresión del material genético.']]
    ids, H = tabla_filas(s, 4.95, 1.2, [2.25, 2.75, 3.1], rows, rowh=0.9, size=14.5, name='Tabla macro')
    ill = s.group_start('Íconos macronutrientes')
    molecula3d(s, 0.4, 1.2, 2.0, 'glucosa', name='Glc macro')
    ag_chain(s, 2.5, 1.9, 1.9, 0.38, name='Ácido graso macro')
    molecula3d(s, 1.2, 3.3, 2.0, 'aa', name='AA macro')
    s.group_end()
    mm = caja(s, 0.4, 5.55, 12.65, 1.5, '**Macro**: se necesitan en grandes cantidades; componente estructural y funcional. **Micro** (vitaminas, minerales): menores cantidades, pero esenciales: son **cofactores de enzimas** (p. ej., B_{1} y B_{5} en esta unidad).',
              AMA, 15.5, name='Micro vs macro')
    s.step(fade(ill), fade(ids[0], after=True))
    for r in ids[1:]:
        s.step(fade(r))
    s.step(fade(mm))


def rotonda(D):
    s = nueva(D, 2, 'Acetil-CoA: la rotonda metabólica', src=['TM 8.2 El Acetil-CoA'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    cx, cy = 4.6, 4.1
    rot_ = s.group_start('!!Rotonda')
    s.shape(cx - 1.9, cy - 1.9, 3.8, 3.8, 'donut', ('lin', [(0, '7F8C8D'), (100, '5D6D7E')], 90), (INK, 1.5), False, adj={'adj': 9000})
    s.shape(cx - 1.5, cy - 1.5, 3.0, 3.0, 'ellipse', shade('82E0AA', 0.4, 0.25), (INK, 1.5), False)
    s.group_end()
    acoa = ficha(s, cx - 1.1, cy - 0.35, 'Acetil-CoA', 'B7950B', w=2.2, h=0.7, size=18, name='!!AcetilCoA')
    entr = []
    for (t, c, ang) in (('Hidratos de carbono', '3B82C4', 200), ('Lípidos (ácidos grasos)', 'F2B90F', 160), ('Proteínas (aminoácidos)', '27AE60', 240)):
        a = math.radians(ang)
        x1, y1 = cx + 3.6 * math.cos(a), cy + 2.7 * math.sin(a)
        x2, y2 = cx + 1.95 * math.cos(a), cy + 1.95 * math.sin(a)
        g = s.group_start('Entrada ' + t)
        s.arrow([(x1, y1), (x2, y2)], c, 9)
        ficha(s, x1 - 1.0, y1 - 0.62, t, c, w=2.2, h=0.45, size=12)
        entr.append(s.group_end())
    sal = []
    for (t, c, ang) in (('Ciclo de Krebs', 'E74C3C', -30), ('Síntesis de ácidos grasos', 'F39C12', 20), ('Cuerpos cetónicos', 'C2185B', 60), ('Colesterol y esteroides', '8E44AD', -75)):
        a = math.radians(ang)
        x1, y1 = cx + 1.95 * math.cos(a), cy + 1.95 * math.sin(a)
        x2, y2 = cx + 3.4 * math.cos(a), cy + 2.8 * math.sin(a)
        g = s.group_start('Salida ' + t)
        s.arrow([(x1, y1), (x2, y2)], c, 9)
        ficha(s, x2 + 0.05 if math.cos(a) > 0.3 else x2 - 1.15, y2 - 0.22 if abs(ang) < 50 else (y2 + 0.02 if ang > 0 else y2 - 0.5), t, c, w=2.3, h=0.45, size=12)
        sal.append(s.group_end())
    c = caja(s, 9.35, 1.2, 3.7, 3.0, 'Molécula **central** del metabolismo. Como una **rotonda**: para pasar del metabolismo de las proteínas al de los lípidos hay que «girar» por ella.',
             BLANCO, 15, head='Analogía', name='Analogía rotonda')
    c2 = caja(s, 9.35, 4.45, 3.7, 2.6, 'Los caminos **catabólicos** confluyen en el acetil-CoA y de él parten caminos **anabólicos**.', AMA, 15.5, name='Convergencia')
    s.step(fade(rot_), zoom(acoa, after=True))
    s.step(*[wipe(e, 'l', after=(k > 0)) for k, e in enumerate(entr)])
    s.step(*[fade(e, after=(k > 0)) for k, e in enumerate(sal)])
    s.step(fade(c))
    s.step(fade(c2))


def estructura_acoa(D):
    s = nueva(D, 2, 'Estructura del acetil-CoA', src=['TM 8.2 Estructura del Acetil-CoA', 'REV TM 8.2'], tipo='bandas', c1=CREMA, c2=VERDE_CL)
    ac = s.group_start('!!Grupo acetilo')
    molecula3d(s, 0.4, 1.4, 2.6, 'acetil', name='Acetilo 3D')
    s.group_end()
    acl = caja(s, 0.4, 4.15, 2.75, 2.9, '**Grupo acetilo** (2 C): un metilo + un carbonilo (C=O). La parte «chiquita».', 'FCF3CF', 15, name='Rótulo acetilo')
    tio = rotulo(s, 3.4, 2.45, '–S– (tioéster)', AMA2, 16, name='Tioéster')
    coa = s.group_start('!!Coenzima A')
    for k, (t, c, w) in enumerate((('β-mercaptoetilamina', 'F7DC6F', 2.4), ('Ácido pantoténico (vit. B_{5})', '58D68D', 2.9), ('ADP 3′-fosfato', 'FFC000', 2.0))):
        ficha(s, 5.2 + sum((2.4, 2.9, 2.0)[:k]) * 0.0 + (0, 0, 0)[k], 1.5 + k * 0.85, t, c, w=w + 0.6, h=0.6, size=14)
    s.group_end()
    coal = caja(s, 3.4, 4.15, 6.6, 2.9, '**Coenzima A** (CoA): molécula grande con **ácido pantoténico (vitamina B_{5})**, **β-mercaptoetilamina** y un nucleótido de adenina. Se une al acetilo a través de un **átomo de azufre** (enlace **tioéster**).',
                BLANCO, 15, name='Rótulo CoA')
    r_ = rigor(s, 10.4, 1.2, 2.65, 5.85, 'El nucleótido de la CoA es **ADP 3′-fosfato** (derivado del ATP), no un ATP completo.', 14, name='Rigor CoA')
    s.step(fade(ac), fade(acl, after=True))
    s.step(zoom(tio))
    s.step(fade(coa), fade(coal, after=True))
    s.step(fade(r_))


def que_llega(D):
    s = nueva(D, 2, '¿Qué llega al acetil-CoA? Catabolismo', src=['TM 8.2 Qué llega al Acetil-CoA'], tipo='der', c1=VERDE_OSC, c2=BLANCO)
    mi = mitocondria_grande(s, 4.4, 2.0, 4.5, 3.6, name='!!Mitocondria', crestas=True)
    ac = ficha(s, 5.6, 3.5, 'Acetil-CoA', 'B7950B', w=2.1, h=0.6, size=17, name='!!AcetilCoA')
    rutas = []
    for k, (t, d, c, y) in enumerate((('Glucosa', 'glucólisis → **piruvato** → complejo PDH', '3B82C4', 1.3), ('Ácidos grasos', 'triglicéridos → ácidos grasos → **β-oxidación**', 'F2B90F', 3.45),
                                     ('Aminoácidos', 'algunos (leucina, lisina, parcialmente otros) → acetil-CoA o piruvato', '27AE60', 5.45))):
        g = s.group_start('Ruta ' + t)
        ficha(s, 0.4, y, t, c, w=1.9, h=0.55, size=15)
        texto(s, 0.4, y + 0.6, 3.9, 0.95, d, 14.5)
        s.arrow([(2.4, y + 0.3), (5.5, 3.8)], c, 4, curve=False)
        rutas.append(s.group_end())
    c = caja(s, 9.35, 1.2, 3.7, 3.2, 'Fructosa y galactosa se transforman primero en glucosa: confluyen en la misma vía.', BLANCO, 15, head='Hidratos', name='Fru Gal')
    c2 = caja(s, 9.35, 4.65, 3.7, 2.4, 'Todos los caminos catabólicos llevan al **acetil-CoA**.', AMA, 16, anchor='m', name='Todos llevan')
    s.step(fade(mi), zoom(ac, after=True))
    for g in rutas:
        s.step(fade(g))
    s.step(fade(c))
    s.step(fade(c2))


def para_que(D):
    s = nueva(D, 2, '¿Para qué sirve el acetil-CoA?', src=['TM 8.2 Para qué sirve el Acetil-CoA'], tipo='izq', c1=VERDE_CL, c2=BLANCO)
    ac = ficha(s, 1.2, 3.6, 'Acetil-CoA', 'B7950B', w=2.4, h=0.75, size=20, name='!!AcetilCoA')
    dest = [('Ciclo de Krebs', 'Genera NADH, FADH_{2} y GTP → cadena respiratoria → **ATP**.', 'F5B7B1'),
            ('Síntesis de ácidos grasos', 'Almacenamiento de energía en forma de **grasas**.', 'FCF3CF'),
            ('Cuerpos cetónicos', 'Fuente de energía en **ayuno prolongado** o cetosis.', 'F8BBD0'),
            ('Colesterol y hormonas esteroideas', 'Testosterona, estrógenos, cortisol, aldosterona.', 'E8DAEF')]
    ids = []
    for k, (t, d, f) in enumerate(dest):
        y = 1.2 + k * 1.47
        g = s.group_start('Destino ' + t)
        s.arrow([(3.65, 3.98), (5.0, y + 0.65)], INK, 3)
        caja(s, 5.05, y, 8.0, 1.3, '**%s**: %s' % (t, d), f, 16, anchor='m')
        ids.append(s.group_end())
    m = molecula3d(s, 0.6, 5.0, 2.0, 'acetil', name='Acetil deco')
    s.step(zoom(ac), fade(m, after=True))
    for g in ids:
        s.step(fade(g))


def piruvato_origenes(D):
    s = nueva(D, 2, 'Piruvato: tres orígenes en el citoplasma', src=['TM 9.1 Tres orígenes del piruvato', 'REV TM 9.1'], tipo='bandas', c1=CREMA, c2=VERDE_CL)
    cel = s.shape(3.45, 1.2, 6.6, 5.85, 'roundRect', ('rad', [(0, 'FEF9E7'), (100, 'FAD7A0')], (50, 50)), ('A04000', 3.0), SH_I, name='!!Citoplasma', adj={'adj': 14000})
    mi = mitocondria_grande(s, 7.2, 4.6, 2.6, 1.9, name='Mitocondria pequeña', crestas=True)
    pir = ficha(s, 5.6, 3.6, 'Piruvato (3 C)', 'F39C12', w=2.2, h=0.62, size=17, name='!!Piruvato')
    o = []
    for k, (t, d, c, pos, tgt) in enumerate((('Glucosa', '**Glucólisis**: principal fuente; 1 glucosa → **2 piruvatos**. También fructosa y galactosa.', '3B82C4', (3.8, 1.5), (5.9, 3.55)),
                                             ('Alanina', '**Transaminación** de aminoácidos glucogénicos; la alanina es el más importante.', '27AE60', (8.0, 1.5), (7.3, 3.55)),
                                             ('Lactato', 'Sin O_{2} (hipoxia, ejercicio intenso) el piruvato se **reduce a lactato**; con O_{2} el lactato puede volver a piruvato.', '8E44AD', (3.8, 5.6), (5.8, 4.25)))):
        g = s.group_start('Origen ' + t)
        ficha(s, pos[0], pos[1], t, c, w=1.8, h=0.55, size=15)
        s.arrow([(pos[0] + 0.9, pos[1] + (0.6 if pos[1] < 3 else -0.05)), tgt], c, 4, head='triangle' if t == 'Lactato' else None)
        o.append(s.group_end())
    ds = [caja(s, 0.35, 1.2 + k * 1.97, 2.9, 1.8, d, f, 13.5, name='Desc origen %d' % (k + 1))
          for k, (d, f) in enumerate((('**1. Glucólisis**: principal fuente; 1 glucosa → 2 piruvatos (también fructosa y galactosa).', 'EAF2F8'),
                                     ('**2. Aminoácidos glucogénicos**: alanina → piruvato por transaminación.', 'EAF5EA'),
                                     ('**3. Lactato**: sin O_{2} el piruvato se reduce a lactato; con O_{2} vuelve a piruvato.', 'F4ECF7')))]
    r_ = rigor(s, 10.3, 1.2, 2.75, 5.85, 'El material atribuye al lactato el dolor muscular del ejercicio intenso; esa idea está **cuestionada**: el lactato no es la causa principal del dolor tardío.',
               13.5, name='Rigor lactato')
    s.step(fade(cel), fade(mi, after=True), zoom(pir, after=True))
    for g, d in zip(o, ds):
        s.step(fade(g), fade(d, after=True))
    s.step(fade(r_))


# ---------------------------------------------------------------- ingreso del piruvato (Morph)
ING_TXT = {1: 'Ingreso del piruvato a la mitocondria: el punto de partida', 2: 'Membrana externa: canal VDAC', 3: 'Membrana interna: transportador MPC'}


def escena_ing(D, st):
    s = nueva(D, 2, ING_TXT[st], tipo='der', c1=VERDE_OSC, c2=BLANCO, morph=st > 1, src=['TM 9.2 Ingreso a la mitocondria'], tw=8.7)
    ids = {}
    ids['cit'] = s.shape(0.0, 1.0, 3.3, 6.5, 'rect', ('a', 'FAD7A0', 55), None, False, name='!!Zona citoplasma')
    ids['ims'] = s.shape(3.85, 1.0, 1.75, 6.5, 'rect', ('a', 'FDEBD0', 80), None, False, name='!!Espacio intermembrana')
    ids['mat'] = s.shape(6.15, 1.0, 2.9, 6.5, 'rect', ('a', 'FEF5E7', 100), None, False, name='!!Matriz')
    ids['me'] = membrane_v(s, 3.3, 1.0, 6.5, 0.55, name='!!Membrana externa', head='E59866', tail='FDEBD0')
    ids['mi'] = membrane_v(s, 5.6, 1.0, 6.5, 0.55, name='!!Membrana interna', head='CA6F1E', tail='FAD7A0')
    # VDAC y MPC: poros horizontales
    def poro(x, y, col, nm):
        g = s.group_start(nm)
        s.shape(x - 0.12, y - 0.55, 0.8, 0.5, 'roundRect', shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), False, adj={'adj': 40000})
        s.shape(x - 0.12, y + 0.35, 0.8, 0.5, 'roundRect', shade(col, 0.4, 0.25), (darken(col, 0.5), 1.25), False, adj={'adj': 40000})
        return s.group_end()
    ids['vdac'] = poro(3.32, 3.9, '5DADE2', '!!VDAC')
    ids['mpc'] = poro(5.62, 3.9, '58D68D', '!!MPC')
    for nm, x, t in (('Rótulo citoplasma', 0.3, 'CITOPLASMA'), ('Rótulo EIM', 3.9, 'ESPACIO\nINTERMEMBRANA'), ('Rótulo matriz', 6.4, 'MATRIZ')):
        ids[nm] = texto(s, x, 1.15, 2.6 if x != 3.9 else 1.65, 0.75, t, 14, NAVY, True, 'c', name='!!' + nm)
    ids['iones'] = s.group_start('!!Iones')
    for k, (ix, iy) in enumerate(((2.5, 3.0), (2.8, 4.6), (4.5, 2.9), (4.9, 4.9), (2.2, 5.3))):
        s.shape(ix, iy, 0.3, 0.3, 'ellipse', shade('AF7AC5', 0.4, 0.2), ('6C3483', 0.75), False, '±', 10, F_HEAD, BLANCO, True, 'c', 'm', (0, 0, 0, 0), fit=False)
    s.group_end()
    ids['ins'] = s.group_start('!!Orientación')
    mitocondria_grande(s, 0.3, 5.6, 2.3, 1.3, name='Mitocondria orientación')
    s.shape(1.85, 5.75, 0.55, 0.55, 'ellipse', None, (ROJO, 2.5), False)
    texto(s, 0.3, 5.15, 2.6, 0.4, 'zona ampliada', 12, ROJO, True, 'c')
    s.group_end()
    ids['pdh'] = s.group_start('!!PDH')
    enzima_globular(s, 6.6, 5.3, 0.9, 0.8, 'E59866', 'E1', 'E1 mini', size=12)
    enzima_globular(s, 7.3, 5.75, 1.0, 0.9, '82E0AA', 'E2', 'E2 mini', size=12, seed=3)
    enzima_globular(s, 8.05, 5.3, 0.85, 0.75, '85C1E9', 'E3', 'E3 mini', size=12, seed=5)
    texto(s, 6.4, 6.7, 2.6, 0.35, 'complejo PDH', 13, NAVY, True, 'c')
    s.group_end()
    px = {1: 1.0, 2: 4.0, 3: 6.7}[st]
    ids['pir'] = ficha(s, px, 3.72, 'Piruvato', 'F39C12', w=1.6, h=0.55, size=15, name='!!Piruvato')
    return s, ids


def ingreso(D):
    ini = len(D.slides) + 1
    s, i = escena_ing(D, 1)
    glc = ficha(s, 0.9, 1.9, 'Glucosa', '3B82C4', w=1.6, h=0.5, size=14, name='Glucosa ing')
    fl = s.arrow([(1.7, 2.45), (1.7, 3.65)], INK, 3, name='Glucólisis ing')
    gl = rotulo(s, 1.85, 2.8, 'glucólisis', CREMA, 12, name='Rótulo glucólisis')
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'El piruvato se forma en el **citoplasma**, pero el acetil-CoA se genera en la **matriz mitocondrial**: el piruvato debe cruzar **dos membranas**.', AMA, 15,
             head='Problema', name='Problema dos membranas')
    s.step(fade(i['cit']), fade(i['ims'], after=True), fade(i['mat'], after=True), fade(i['me'], after=True), fade(i['mi'], after=True),
           *[fade(i[k], after=True) for k in ('!!Rótulo citoplasma', '!!Rótulo EIM', '!!Rótulo matriz') if False],
           fade(i['Rótulo citoplasma']), fade(i['Rótulo EIM']), fade(i['Rótulo matriz']))
    s.step(fade(glc), wipe(fl, 't', after=True), fade(gl, after=True), fade(i['pir'], after=True))
    s.step(fade(c))
    s.step(fade(i['vdac']), fade(i['mpc'], after=True), fade(i['iones'], after=True))
    s.step(fade(i['ins']), fade(i['pdh'], after=True))
    s, i = escena_ing(D, 2)
    c = caja(s, 9.35, 1.2, 3.7, 3.7, 'Cruza la **membrana externa** por el canal **VDAC** (canal de aniones dependiente de voltaje). **No es específico** del piruvato: entra acoplado al transporte de iones y llega al **espacio intermembrana**.',
             'EAF2F8', 14.5, head='VDAC', headfill=AZUL, name='Caja VDAC')
    s.step(pulse(i['vdac']), fade(c, after=True))
    s, i = escena_ing(D, 3)
    c = caja(s, 9.35, 1.2, 3.7, 3.4, 'Cruza la **membrana interna** por el **MPC** (Mitochondrial Pyruvate Carrier), **específico** para el piruvato, hacia la **matriz mitocondrial**.', 'EAF5EA', 15,
             head='MPC', headfill=VERDE_OSC, name='Caja MPC')
    c2 = caja(s, 9.35, 4.85, 3.7, 2.2, 'En la matriz lo espera el **complejo piruvato deshidrogenasa**.', AMA, 16, anchor='m', name='Siguiente PDH')
    s.step(pulse(i['mpc']), fade(c, after=True))
    s.step(fade(c2))
    registrar_morph(D, ini, len(D.slides), 'Ingreso del piruvato: citoplasma → VDAC (membrana externa) → espacio intermembrana → MPC (membrana interna) → matriz',
                    ['!!Piruvato', '!!VDAC', '!!MPC', '!!Membrana externa', '!!Membrana interna', '!!Zona citoplasma', '!!Espacio intermembrana', '!!Matriz'],
                    'Desplazamiento horizontal del piruvato a través de cada transportador; los compartimientos y las membranas permanecen fijos.')


def build(D):
    cat_anab(D)
    clave_redox(D)
    reversibilidad(D)
    control_mecanismos(D)
    control_mecanismos2(D)
    macronutrientes(D)
    rotonda(D)
    estructura_acoa(D)
    que_llega(D)
    para_que(D)
    piruvato_origenes(D)
    ingreso(D)
