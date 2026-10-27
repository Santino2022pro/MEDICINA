# -*- coding: utf-8 -*-
"""UNIDAD III — Morph 3 (adipocito → mitocondria), temas 15, 16, 17"""
from base import *

U = 3


def m3txt(s, t, head):
    return card(s, 8.9, 1.1, 4.0, 4.2, t, CREAM, 15, name='!!Texto M3', head=head)


def m3a(D):
    s = new(D, U, 'Metabolismo lipídico: el adipocito', 'SECUENCIA MORPH 3 · 1/5')
    adipocyte_white(s, 1.2, 1.1, 5.9, name='!!Adipocito M3')
    s.text(1.2, 6.95 - 0.1, 5.9, 0.3, 'Adipocito blanco: una gota única de TAG', 13, F_HEAD, '7E5109', True, 'c', name='!!Rótulo M3')
    ags = [ag_chain(s, 3.2 + i * 0.4, 3.4 + i * 0.5, 1.2, 0.22, name='!!AG viajero %d' % i) for i in range(3)]
    m3txt(s, '- La mayor reserva energética: **TAG** en una gota rodeada de **perilipinas**.\n- En ayuno o ejercicio se **movilizan** como AG + glicerol.\n- Recorrido: gota → lipólisis → sangre → músculo → **mitocondria**.', 'Reserva')
    s.note('Secuencia Morph 3 (metabolismo lipídico): adipocito → gota lipídica → lipólisis → ácidos grasos → sangre → músculo → '
           'mitocondria. Los ácidos grasos marcados (!!AG viajero) conservan su nombre en las cinco diapositivas, de modo que '
           'Morph los desplaza desde la gota hasta la mitocondria muscular.')


def m3b(D):
    s = new(D, U, 'Metabolismo lipídico: la gota lipídica', 'SECUENCIA MORPH 3 · 2/5', morph=True)
    adipocyte_white(s, -6.0, -2.5, 16.0, name='!!Adipocito M3')
    plin = [s.shape(0.6 + i * 1.3, 1.2 + (i % 2) * 0.25, 0.9, 0.35, 'roundRect', shade('BB8FCE', 0.35, 0.2), ('6C3483', 1.0), False,
                    'PLIN1', 11, F_HEAD, WHITE, True, 'c', 'm', name='Perilipina %d' % i, adj={'adj': 50000}) for i in range(6)]
    ags = [ag_chain(s, 2.6 + i * 1.2, 3.4 + (i % 2) * 0.6, 1.2, 0.22, name='!!AG viajero %d' % i) for i in range(3)]
    tg = [mol(s, 1.4 + i * 1.5, 5.0, 'tag', d=0.6, name='TAG %d' % i) for i in range(4)]
    s.text(0.5, 6.2, 7.5, 0.4, 'INTERIOR DE LA GOTA: TAG', 15, F_HEAD, '7E5109', True, 'c', name='!!Rótulo M3')
    m3txt(s, '- **Perilipina 1** recubre la gota y regula el acceso de las lipasas.\n- En reposo alimentado **secuestra a CGI-58**: ATGL poco activa.\n- La **PKA** fosforila perilipina → libera CGI-58 → **activa ATGL**.', 'Gota lipídica')
    s.step(*[pulse(p, after=(i > 0), dur=200) for i, p in enumerate(plin)])
    s.note('Morph: el adipocito se amplía hasta que la gota lipídica ocupa la escena. La perilipina 1 recubre la gota; en '
           'reposo alimentado secuestra a CGI-58 (ABHD5), de modo que la ATGL es poco activa. La fosforilación de la perilipina '
           'por PKA (catecolaminas, baja insulina) libera CGI-58, que coactiva a ATGL, y permite el acceso de HSL fosforilada.')


def m3c(D):
    s = new(D, U, 'Metabolismo lipídico: lipólisis y salida a la sangre', 'SECUENCIA MORPH 3 · 3/5', morph=True)
    adipocyte_white(s, 0.4, 1.1, 3.6, name='!!Adipocito M3')
    c = chain(s, 4.3, 1.2, ['TAG', 'DAG', 'MAG', 'Glicerol'], dy=0.85, w=1.5, enzymes=['ATGL', 'HSL', 'MGL'], rev=[False] * 3,
              fill=[ENE, YEL, YEL, lighten(MOL['gly'][0], 0.5)], name='Lipólisis M3')
    vessel(s, 0.3, 5.0, 8.3, 1.2, name='!!Vaso M3', rbcs=4)
    alb = [s.shape(1.2 + i * 2.4, 5.3, 1.3, 0.6, 'ellipse', shade('F9E79F', 0.4, 0.2), ('9A7D0A', 1.0), False, 'Albúmina', 11, F_HEAD, INK, True, 'c', 'm', name='Albúmina %d' % i) for i in range(3)]
    ags = [ag_chain(s, 1.3 + i * 2.4, 5.05, 1.1, 0.2, name='!!AG viajero %d' % i) for i in range(3)]
    gl = mol(s, 6.3, 4.1, 'gly', d=0.45, name='Glicerol a hígado')
    s.text(6.8, 4.15, 2.0, 0.4, '→ hígado', 13, F_HEAD, '9C640C', True, 'l')
    s.text(0.5, 6.35, 7.5, 0.3, 'SANGRE: AG unidos a albúmina', 13, F_HEAD, '6E1A12', True, 'c', name='!!Rótulo M3')
    m3txt(s, '- **ATGL** (TAG → DAG), **HSL** (DAG → MAG), **MGL** (MAG → glicerol + AG).\n- Los **AG** salen unidos a **albúmina** (AG no esterificados).\n- El **glicerol** va al hígado y al riñón (glicerol cinasa).', 'Lipólisis')
    chain_anim(s, c, per_click=1)
    s.step(*[fade(a, after=(i > 0)) for i, a in enumerate(alb)], zoom(gl))
    s.note('Morph: el adipocito se reduce y aparece el vaso. La lipólisis ocurre en tres pasos (ATGL, HSL, MGL). Los ácidos '
           'grasos salen a la sangre unidos a la albúmina; no deben confundirse con las lipoproteínas (que transportan TAG '
           'esterificados). El glicerol es hidrosoluble y viaja libre al hígado y al riñón, que poseen glicerol cinasa.')


def m3d(D):
    s = new(D, U, 'Metabolismo lipídico: captación muscular', 'SECUENCIA MORPH 3 · 4/5', morph=True)
    vessel(s, 0.3, 1.05, 12.6, 1.05, name='!!Vaso M3', rbcs=6)
    muscle_fiber(s, 0.4, 3.5, 8.2, 2.1, name='!!Fibra M3')
    ags = [ag_chain(s, 2.0 + i * 1.6, 1.45, 1.1, 0.2, name='!!AG viajero %d' % i) for i in range(3)]
    tr = [chip(s, 2.2 + i * 1.6, 2.9, t, LBLUE, 12, name='Transportador %s' % t) for i, t in enumerate(['CD36', 'FATP', 'FABP'])]
    s.text(0.5, 5.75, 8, 0.35, 'FIBRA MUSCULAR (oxidativa)', 13, F_HEAD, '7B241C', True, 'c', name='!!Rótulo M3')
    m3txt(s, '- Captación por **CD36**, **FATP** y difusión; **FABP** citosólica.\n- Activación a **acil-CoA** (acil-CoA sintetasa).\n- El destino: **mitocondria** (oxidación) o reesterificación local.', 'Músculo')
    s.step(*[fade(t, after=(i > 0)) for i, t in enumerate(tr)])
    s.step(*[path(a, 0.0, 1.9, dur=1300, delay=i * 250) for i, a in enumerate(ags)])
    s.note('Morph: el vaso se desplaza arriba y aparece la fibra muscular. Los AG se disocian de la albúmina y entran al músculo '
           'mediante CD36, transportadores FATP y difusión; la FABP los moviliza en el citosol (ampliación bibliográfica). Luego '
           'se activan a acil-CoA y se dirigen a la mitocondria, salvo que se reesterifiquen localmente.')


def m3e(D):
    s = new(D, U, 'Metabolismo lipídico: la mitocondria', 'SECUENCIA MORPH 3 · 5/5', morph=True)
    muscle_fiber(s, -3.0, -3.0, 22.0, 12.0, name='!!Fibra M3')
    mito(s, 0.6, 1.4, 7.8, 4.2, name='!!Mitocondria M3')
    ags = [ag_chain(s, 2.0 + i * 1.5, 2.9 + (i % 2) * 0.5, 1.1, 0.2, name='!!AG viajero %d' % i) for i in range(3)]
    chip(s, 2.6, 5.75, 'MATRIZ MITOCONDRIAL: β-oxidación', CREAM, 14, name='!!Rótulo M3')
    m3txt(s, '- Los AG largos atraviesan la membrana interna con la **lanzadera de carnitina** (CPT1 → CACT → CPT2).\n- En la matriz: **β-oxidación** → acetil-CoA, NADH y FADH_{2}.\n- Se oxidan en el **ciclo de Krebs** y la **cadena respiratoria**.', 'Mitocondria')
    s.note('Morph final: la fibra se amplía hasta revelar la mitocondria, donde los AG llegan a la matriz por la lanzadera de '
           'carnitina y se oxidan. Las diapositivas siguientes detallan cada etapa: activación y transporte, β-oxidación, cadena '
           'respiratoria y balance energético.')


# ------------------------------------------------------------------ TEMA 15
def t15a(D):
    s = new(D, U, '15 · Activación y lanzadera de carnitina')
    s.shape(0.3, 1.05, 12.6, 1.45, 'rect', ('a', 'FFFFFF', 40), None, False, name='Citosol')
    s.text(0.4, 1.08, 3, 0.3, 'CITOSOL', 12.5, F_HEAD, INK, True, 'l')
    membrane_h(s, 0.3, 2.55, 12.6, 0.42, name='Membrana externa', head='F5B041', tail='FEF5E7')
    s.text(0.4, 3.0, 4, 0.3, 'ESPACIO INTERMEMBRANA', 12, F_HEAD, '7E5109', True, 'l')
    membrane_h(s, 0.3, 3.85, 12.6, 0.42, name='Membrana interna', head='E59866', tail='FDEBD0')
    s.shape(0.3, 4.3, 12.6, 1.4, 'rect', ('a', 'F8C471', 55), None, False, name='Matriz')
    s.text(0.4, 5.35, 3, 0.3, 'MATRIZ', 12.5, F_HEAD, '7E5109', True, 'l')
    ag = ag_chain(s, 0.6, 1.5, 1.3, 0.22, name='AG')
    acs = enz(s, 2.1, 1.35, 'Acil-CoA sintetasa', name='ACS')
    cost = mol(s, 2.2, 1.8, 'atp', 'ATP → AMP + PP_{i}', d=0.38, w=1.85, name='Costo activación')
    acoa = chip(s, 4.45, 1.55, 'Acil-CoA', ENE, 13, name='Acil-CoA citosol')
    cpt1 = s.shape(6.0, 2.45, 1.3, 0.62, 'roundRect', shade('F5B041', 0.4, 0.3), (INK, 1.5), SHD, 'CPT1', 15, F_HEAD, INK, True, 'c', 'm', name='CPT1')
    acar = chip(s, 6.0, 3.2, 'Acilcarnitina', LSALMON, 13, name='Acilcarnitina')
    cact = s.shape(7.9, 3.75, 1.3, 0.62, 'roundRect', shade('85C1E9', 0.4, 0.3), (INK, 1.5), SHD, 'CACT', 15, F_HEAD, INK, True, 'c', 'm', name='CACT')
    cpt2 = s.shape(9.6, 4.45, 1.3, 0.62, 'roundRect', shade('F0B27A', 0.4, 0.3), (INK, 1.5), SHD, 'CPT2', 15, F_HEAD, INK, True, 'c', 'm', name='CPT2')
    am = chip(s, 11.1, 4.55, 'Acil-CoA → β-ox', ENE, 13, name='Acil-CoA matriz')
    car = chip(s, 9.5, 3.15, 'Carnitina ↺', MINT, 12, name='Carnitina retorno')
    a = [s.arrow([(1.95, 1.62), (4.4, 1.75)], ACT, 2.5), s.arrow([(5.4, 1.85), (6.3, 2.43)], ACT, 2.5), s.arrow([(6.7, 3.08), (6.75, 3.18)], ACT, 2.5),
         s.arrow([(7.55, 3.45), (7.95, 3.78)], TRN, 2.5), s.arrow([(9.2, 4.12), (9.65, 4.5)], TRN, 2.5), s.arrow([(10.92, 4.75), (11.08, 4.75)], ACT, 2.5)]
    mi = mol(s, 4.6, 2.0, 'mal', 'Mal', d=0.4, name='Malonil inhibidor')
    ih = s.inhib([(5.0, 2.25), (6.0, 2.65)], w=2.5)
    k = card(s, 0.3, 5.85, 12.6, 1.25, 'Costo de activación: **2 enlaces** de alta energía (ATP → AMP + PP_{i}). Los AG de **cadena corta/media** acceden a la matriz **sin depender** en igual medida de la lanzadera. No confundir **CPT1** con **CACT**.', YEL, 14)
    s.step(fade(ag), fade(acs, after=True), zoom(cost), wipe(a[0], 'l', after=True), fade(acoa, after=True))
    s.step(wipe(a[1], 't'), fade(cpt1, after=True), wipe(a[2], 't', after=True), fade(acar, after=True))
    s.step(wipe(a[3], 'l'), fade(cact, after=True), wipe(a[4], 'l', after=True), fade(cpt2, after=True), wipe(a[5], 'l', after=True), fade(am, after=True), fade(car))
    s.step(zoom(mi), wipe(ih, 'l', after=True))
    s.step(fade(k))
    s.note('Etapa 2, activación: acil-CoA sintetasa: AG + CoA + ATP → acil-CoA + AMP + PPi (equivalente al gasto de dos enlaces '
           'fosfato de alta energía, porque el PPi se hidroliza). Etapa 3, importación de cadenas largas: la CPT1 de la membrana '
           'externa forma acilcarnitina; la carnitina–acilcarnitina translocasa (CACT/SLC25A20) la transporta a través de la '
           'membrana interna; la CPT2 regenera acil-CoA en la matriz y la carnitina retorna. El malonil-CoA inhibe la CPT1. '
           'Los AG de cadena corta y media acceden a la matriz sin depender en igual medida de esta lanzadera.')


def t15b(D):
    s = new(D, U, '15 · β-oxidación: cuatro reacciones por vuelta')
    cx, cy = 3.6, 4.1
    nodes = [('Acil-CoA (C_{n})', 2.45, 1.15, ENE), ('trans-Δ^{2}-enoil-CoA', 5.0, 2.95, YEL), ('L-3-hidroxiacil-CoA', 2.45, 4.75, YEL), ('3-cetoacil-CoA', 0.3, 2.95, YEL)]
    ids = []
    for t, x, y, f in nodes:
        ids.append(s.shape(x, y, 2.3, 0.6, 'roundRect', f, (INK, 1.25), SHD, t, 13.5, F_HEAD, INK, True, 'c', 'm', name='Nodo ' + plain(t)[:12], adj={'adj': 30000}))
    steps = [([(4.6, 1.75), (5.9, 2.9)], '1 · Acil-CoA DH', 'FAD → FADH_{2} (→ ETF)', (5.75, 1.6)),
             ([(5.9, 3.6), (4.6, 4.7)], '2 · Enoil-CoA hidratasa', '+ H_{2}O', (5.6, 4.25)),
             ([(2.5, 4.75), (1.4, 3.6)], '3 · 3-hidroxiacil-CoA DH', 'NAD^{+} → NADH', (0.1, 4.25)),
             ([(1.4, 2.9), (2.5, 1.75)], '4 · β-cetotiolasa', '+ CoA', (0.2, 1.6))]
    sids = []
    for pts, e, cof, (lx, ly) in steps:
        g = s.group_start('Reacción ' + e[:12])
        s.arrow(pts, ACT, 3.5, curve=False)
        enz(s, lx, ly, e, size=11.5)
        s.text(lx, ly + 0.33, 2.6, 0.3, cof, 12, F_HEAD, '7E5109', True, 'l')
        s.group_end(); sids.append(g)
    out1 = mol(s, 6.4, 2.3, 'atp', 'FADH_{2}', d=0.42, w=0.95, name='FADH2 salida')
    out2 = mol(s, 0.3, 5.0, 'atp', 'NADH', d=0.42, w=0.8, name='NADH salida')
    prod = s.shape(2.2, 6.0, 4.6, 0.95, 'roundRect', shade('F4D03F', 0.4, 0.2), (INK, 1.5), SHD, '**Acetil-CoA** + acil-CoA (C_{n−2}) → nueva vuelta', 14, F_HEAD, INK, False, 'c', 'm', name='Productos vuelta')
    ap = s.arrow([(1.4, 3.6), (2.8, 5.98)], ENE, 3, dash='dash')
    k = card(s, 7.6, 1.1, 5.3, 2.9, '- Cada vuelta **acorta 2 C** y genera **1 FADH_{2} + 1 NADH + 1 acetil-CoA**.\n- FADH_{2} cede electrones a **ETF/ETF-QO**.\n- El acetil-CoA va al **ciclo de Krebs** o, en el hígado, a la **cetogénesis**.', CREAM, 14, head='Balance por vuelta')
    k2 = card(s, 7.6, 4.2, 5.3, 2.9, 'Regulación: disponibilidad de AG, **malonil-CoA/CPT1**, relaciones **NADH/NAD^{+}** y **acetil-CoA/CoA**, ADP (demanda respiratoria), **AMPK/PPARα** y oferta de **O_{2}**.', YEL, 14, head='Control')
    s.step(fade(ids[0]))
    for i in range(4):
        effs = [wipe(sids[i], 'l'), fade(ids[(i + 1) % 4] if i < 3 else prod, after=True)]
        if i == 0:
            effs.append(zoom(out1, after=True))
        if i == 2:
            effs.append(zoom(out2, after=True))
        if i == 3:
            effs.insert(1, wipe(ap, 't'))
        s.step(*effs)
    s.step(fade(k)); s.step(fade(k2))
    s.note('Etapa 4, β-oxidación mitocondrial, cuatro reacciones por vuelta: (1) acil-CoA deshidrogenasa → trans-Δ2-enoil-CoA + '
           'FADH2 (los electrones pasan a ETF y ETF-QO); (2) enoil-CoA hidratasa; (3) β-hidroxiacil-CoA deshidrogenasa → NADH; '
           '(4) β-cetotiolasa → acetil-CoA + acil-CoA dos carbonos más corto, que inicia una nueva vuelta. Cada ciclo acorta la '
           'cadena y aporta poder reductor; el acetil-CoA entra al ciclo de Krebs o, en el hígado, a la cetogénesis.')


def t15c(D):
    s = new(D, U, '15 · Cadena respiratoria y ATP sintasa')
    s.shape(0.3, 1.05, 12.6, 1.4, 'rect', ('a', 'F5B7B1', 45), None, False, name='Espacio intermembrana')
    s.text(0.4, 1.08, 4, 0.3, 'ESPACIO INTERMEMBRANA (H^{+} alto)', 12.5, F_HEAD, '922B21', True, 'l')
    membrane_h(s, 0.3, 2.5, 12.6, 0.6, name='Membrana interna', head='E59866', tail='FDEBD0')
    s.shape(0.3, 3.15, 12.6, 2.3, 'rect', ('a', 'F8C471', 55), None, False, name='Matriz')
    s.text(0.4, 5.1, 4, 0.3, 'MATRIZ', 12.5, F_HEAD, '7E5109', True, 'l')
    cx = [('I', 0.8, 'A569BD'), ('II', 2.6, '5DADE2'), ('ETF-QO', 3.9, '48C9B0'), ('III', 5.6, 'F5B041'), ('IV', 7.5, 'EC7063')]
    cids = []
    for t, x, col in cx:
        cids.append(s.shape(x, 2.15, 1.25 if t != 'ETF-QO' else 1.4, 1.4, 'roundRect', shade(col, 0.35, 0.25), (INK, 1.5), SHD, t, 16 if t != 'ETF-QO' else 12.5, F_HEAD, INK, True, 'c', 'm', name='Complejo ' + t, adj={'adj': 30000}))
    q = mol(s, 3.25, 2.55, 'atp', 'Q', d=0.4, name='Ubiquinona'); c = mol(s, 6.95, 1.85, 'cc', 'c', d=0.35, name='Citocromo c')
    syn = s.group_start('ATP sintasa')
    s.shape(9.8, 1.4, 1.0, 1.5, 'roundRect', shade('58D68D', 0.35, 0.25), (INK, 1.5), SHD, 'F_{O}', 14, F_HEAD, INK, True, 'c', 'm', adj={'adj': 40000})
    s.shape(10.15, 2.9, 0.3, 0.7, 'rect', '1E8449', (INK, 1.0), False)
    s.group_end()
    f1 = s.shape(9.6, 3.55, 1.4, 1.2, 'ellipse', shade('82E0AA', 0.4, 0.25), (INK, 1.5), SHD, 'F_{1}', 15, F_HEAD, INK, True, 'c', 'm', name='F1 rotor')
    nadh = mol(s, 0.75, 4.1, 'atp', 'NADH', d=0.45, w=0.9, name='NADH entra')
    fadh = mol(s, 3.95, 4.1, 'atp', 'FADH_{2}/ETF', d=0.45, w=1.4, name='FADH2 entra')
    o2 = mol(s, 7.55, 4.1, 'o2', d=0.45, name='O2'); h2o = chip(s, 8.15, 4.15, '→ H_{2}O', LBLUE, 12.5, name='Agua')
    hs = [s.arrow([(x + 0.6, 2.2), (x + 0.6, 1.5)], INH, 3, name='Bombeo H %d' % i) for i, x in enumerate((0.8, 5.6, 7.5))]
    hl = [mol(s, x + 0.95, 1.4, 'ca', 'H^{+}', d=0.35, name='H %d' % i) for i, x in enumerate((0.8, 5.6, 7.5))]
    hb = s.arrow([(11.2, 1.6), (11.2, 3.6)], INH, 3.5, name='Retorno H+')
    atp = mol(s, 11.3, 3.95, 'atp', 'ADP + P_{i} → ATP', d=0.45, w=1.55, name='ATP sintetizado')
    k = card(s, 0.3, 5.6, 12.6, 1.5, 'Los electrones de **NADH** (complejo I) y **FADH_{2}** (vía ETF/ETF-QO o complejo II) llegan al **O_{2}**; el gradiente de **H^{+}** impulsa la **ATP sintasa**. Cocientes P/O aproximados: **2,5 ATP/NADH** y **1,5 ATP/FADH_{2}**.', CREAM, 14)
    s.step(fade(nadh), pulse(cids[0], after=True), fade(hs[0]), zoom(hl[0]))
    s.step(fade(fadh), pulse(cids[2], after=True), zoom(q, after=True))
    s.step(pulse(cids[3]), fade(hs[1]), zoom(hl[1]), zoom(c, after=True), pulse(cids[4], after=True), fade(hs[2]), zoom(hl[2]), fade(o2), fade(h2o, after=True))
    s.step(wipe(hb, 't'), spin(f1, after=True, dur=1500), zoom(atp, after=True))
    s.step(fade(k))
    s.note('Cadena respiratoria: el NADH cede electrones al complejo I; el FADH2 de la acil-CoA deshidrogenasa los cede a la '
           'flavoproteína transferidora de electrones (ETF) y a ETF-QO, que reduce la ubiquinona (el FADH2 del succinato lo hace '
           'por el complejo II). Los complejos I, III y IV bombean protones al espacio intermembrana; el citocromo c transfiere '
           'electrones al complejo IV, donde el O2 se reduce a agua. El retorno de protones por la ATP sintasa (FO–F1) hace girar '
           'el rotor (animación de giro) y sintetiza ATP. Cocientes P/O modernos aproximados: 2,5 por NADH y 1,5 por FADH2.')


def t15d(D):
    s = new(D, U, '15 · Balance energético del palmitato (C16:0)')
    ag_chain(s, 0.5, 1.3, 3.5, 0.5, name='Palmitato')
    s.text(0.5, 1.95, 3.6, 0.4, 'Palmitato C16:0', 16, F_HEAD, INK, True, 'c')
    rows = [['Producto', 'Cantidad', 'ATP por unidad', 'ATP'],
            ['Ciclos de β-oxidación', '7', '—', '—'],
            ['Acetil-CoA (ciclo de Krebs)', '8', '10', '80'],
            ['NADH', '7', '2,5', '17,5'],
            ['FADH_{2}', '7', '1,5', '10,5'],
            ['Subtotal', '', '', '108'],
            ['Activación (ATP → AMP)', '', '', '−2'],
            ['**Rendimiento neto**', '', '', '**≈ 106 ATP**']]
    t, H = table(s, 4.6, 1.15, 8.3, rows, [3.4, 1.5, 1.8, 1.6], size=15.5, rowh=0.6, name='Tabla palmitato')
    f = s.shape(0.4, 2.6, 3.9, 1.6, 'rect', TAG, (INK, 1.5), SHD, 'C16 → **8 acetil-CoA** + **7 FADH_{2}** + **7 NADH**', 17, F_HEAD, INK, False, 'c', 'm', name='Fórmula palmitato')
    k = card(s, 0.4, 4.45, 3.9, 2.65, 'El rendimiento **cambia** según longitud, **insaturación**, lanzaderas y acoplamiento mitocondrial.', CREAM, 14)
    k2 = note_box(s, 4.6, 1.3 + H, 8.3, 1.0, 'Cada acetil-CoA en Krebs ≈ 10 ATP (3 NADH + 1 FADH_{2} + 1 GTP).', 14)
    s.step(fade(f)); s.step(fade(t)); s.step(fade(k)); s.step(fade(k2))
    s.note('Ejemplo energético clásico: el palmitato (C16:0) requiere 7 ciclos de β-oxidación y produce 8 acetil-CoA, 7 FADH2 y '
           '7 NADH. Con cocientes P/O modernos aproximados (2,5 ATP/NADH; 1,5 ATP/FADH2) y 10 ATP por acetil-CoA oxidado en el '
           'ciclo de Krebs (3 NADH + 1 FADH2 + 1 GTP), el total es 108 ATP; restando el costo de activación (2 enlaces de alta '
           'energía) el rendimiento neto es ~106 ATP por molécula. El rendimiento cambia según longitud, insaturación, lanzaderas '
           'y acoplamiento mitocondrial.')


def t15e(D):
    s = new(D, U, '15 · Variantes, regulación y correlato clínico')
    c = chain(s, 0.5, 1.55, ['Propionil-CoA', 'Metilmalonil-CoA', 'Succinil-CoA → Krebs'], dy=0.95, w=2.6, enzymes=['carboxilasa (biotina)', 'mutasa (vitamina B_{12})'],
              rev=[False, False], fill=[YEL, YEL, MINT], name='Cadena impar')
    h1 = chip(s, 0.5, 1.05, 'CADENAS IMPARES', TAG, 14, name='Rótulo impares')
    k1 = card(s, 0.4, 4.4, 4.2, 1.35, 'Último ciclo → **propionil-CoA**: aporta **potencial gluconeogénico** (succinil-CoA).', MINT, 13.5)
    per = card(s, 4.9, 1.05, 3.9, 3.2, 'Los AG de **cadena muy larga** se acortan inicialmente en **peroxisomas**; la oxidación peroxisomal genera **H_{2}O_{2}** y no conserva toda la energía como ATP.', LILAC, 14, head='Peroxisoma')
    cl = card(s, 9.05, 1.05, 3.85, 4.7, '**Deficiencia de MCAD** y otros defectos de oxidación:\n- intolerancia al ayuno\n- **hipoglucemia hipocetósica**\n- acilcarnitinas características\n- descompensación ante enfermedad', LSALMON, 14, head='Clínica')
    nb = note_box(s, 0.4, 5.95, 12.5, 1.15, 'Error a evitar: «más AG disponibles garantiza ATP». **Debe funcionar el sistema de oxidación**.', 15)
    chain_anim(s, c, per_click=3)
    s.anim[-1].insert(0, fade(h1))
    s.step(fade(k1)); s.step(fade(per)); s.step(fade(cl)); s.step(fade(nb))
    s.note('Las cadenas impares terminan en propionil-CoA → metilmalonil-CoA (propionil-CoA carboxilasa, biotina) → succinil-CoA '
           '(metilmalonil-CoA mutasa, vitamina B12), por lo que aportan potencial gluconeogénico. Las cadenas muy largas se acortan '
           'inicialmente en peroxisomas; la oxidación peroxisomal genera H2O2 y no conserva toda la energía como ATP. Correlato '
           'clínico: la deficiencia de MCAD y otros defectos de oxidación provocan intolerancia al ayuno, hipoglucemia '
           'hipocetósica, acumulación de acilcarnitinas características y descompensación ante enfermedades intercurrentes.')


# ------------------------------------------------------------------ TEMA 16
def t16a(D):
    s = new(D, U, '16 · TAG hepáticos: ¿de dónde vienen sus piezas?')
    s.shape(4.6, 2.6, 4.1, 2.2, 'roundRect', shade('F4D03F', 0.4, 0.2), (INK, 2.0), SHD, 'TAG\n= glicerol-3-P + 3 acil-CoA', 20, F_HEAD, INK, True, 'c', 'm', name='TAG centro', adj={'adj': 25000})
    g3 = [('DHAP (glucólisis) → G3P DH', LSALMON), ('Glicerol → **glicerol cinasa** hepática', LSALMON), ('Gliceroneogénesis', LSALMON)]
    ag = [('**Lipogénesis de novo** (acetil-CoA + NADPH)', YEL), ('**AG no esterificados** plasmáticos', YEL), ('**Remanentes** lipoproteicos', YEL), ('**Recambio** lipídico intracelular', YEL)]
    ids = []
    chip(s, 0.4, 1.1, 'GLICEROL-3-FOSFATO', TAG, 15, name='Cab G3P')
    for i, (t, f) in enumerate(g3):
        g = s.group_start('Fuente G3P %d' % i)
        card(s, 0.4, 1.7 + i * 1.3, 3.8, 1.05, t, f, 14, anchor='m', grow=False)
        s.arrow([(4.22, 2.2 + i * 1.3), (4.58, 3.7)], ACT, 2.5)
        s.group_end(); ids.append(g)
    chip(s, 9.1, 1.1, 'ÁCIDOS GRASOS (acil-CoA)', TAG, 15, name='Cab AG')
    for i, (t, f) in enumerate(ag):
        g = s.group_start('Fuente AG %d' % i)
        card(s, 9.1, 1.7 + i * 1.12, 3.8, 0.95, t, f, 14, anchor='m', grow=False)
        s.arrow([(9.08, 2.15 + i * 1.12), (8.72, 3.7)], ACT, 2.5)
        s.group_end(); ids.append(g)
    k = card(s, 0.4, 6.15, 12.5, 0.95, 'El origen de cada pieza **cambia con el estado nutricional**: en saciedad predomina la DNL; en ayuno, los AG del adiposo.', CREAM, 14.5)
    for g in ids:
        s.step(fade(g))
    s.step(fade(k))
    s.note('Un TAG requiere glicerol-3-fosfato y tres acil-CoA. El glicerol-3-P procede de la DHAP glucolítica (glicerol-3-P '
           'deshidrogenasa), del glicerol por la glicerol cinasa hepática o de la gliceroneogénesis. Los AG vienen de (a) '
           'lipogénesis de novo desde acetil-CoA y NADPH, (b) captación de AG no esterificados plasmáticos, (c) remanentes '
           'lipoproteicos y (d) recambio lipídico intracelular.')


def t16b(D):
    s = new(D, U, '16 · Esterificación y exportación como VLDL')
    c = chain(s, 0.5, 1.2, ['Glicerol-3-P', 'Ácido lisofosfatídico', 'Ácido fosfatídico', 'DAG', 'TAG'], dy=1.0, w=2.7,
              enzymes=['GPAT (+ acil-CoA)', 'AGPAT (+ acil-CoA)', 'Lipina (fosfatidato fosfatasa)', 'DGAT1/2 (+ acil-CoA)'], rev=[False] * 4,
              fill=[LSALMON, YEL, YEL, YEL, ENE], name='Esterificación', h=0.5, size=14)
    er = rer(s, 5.9, 1.3, 2.6, 1.3, name='RE')
    mtp = enz(s, 6.1, 2.9, 'MTP', name='MTP')
    vl = lipoprotein(s, 6.0, 3.6, 2.2, 'F7DC6F', 'VLDL', [('2E4A9E', 190, 160, 7, 'ApoB-100')], name='VLDL naciente')
    dr = lipid_drops(s, 4.3, 5.4, 1.4, 1.4, [(500, 500, 420)], name='Gota hepática')
    s.text(3.6, 6.75, 2.8, 0.35, 'almacenamiento en gotas', 12.5, F_HEAD, '7E5109', True, 'c')
    bo = card(s, 8.7, 1.1, 4.2, 2.6, 'Destinos del TAG hepático:\n- **VLDL** (ApoB-100, MTP, fosfolípidos, colesterol)\n- **Gotas** citosólicas\n- **Degradación** (lipólisis/lipofagia)', CREAM, 14, head='Tres destinos')
    k = card(s, 8.7, 3.9, 4.2, 3.2, '- Saciedad rica en carbohidratos: ↑ glucólisis/citrato, ACC, FASN, NADPH (insulina, **ChREBP, SREBP-1c**).\n- La secreción de **VLDL** puede aumentar si lipogénesis y esterificación **exceden** oxidación y depuración.', YEL, 13.5, head='Regulación')
    chain_anim(s, c, per_click=1)
    s.step(fade(er), fade(mtp, after=True), zoom(vl, after=True))
    s.step(fade(dr))
    s.step(fade(bo)); s.step(fade(k))
    s.note('Esterificación: glicerol-3-P → ácido lisofosfatídico (GPAT) → ácido fosfatídico (AGPAT) → DAG (lipina, fosfatidato '
           'fosfatasa) → TAG (DGAT1/2). Los TAG se empaquetan en VLDL con ApoB-100 gracias a la proteína microsomal de '
           'transferencia de triglicéridos (MTP), junto con fosfolípidos y colesterol; también se almacenan en gotículas o se '
           'degradan. En saciedad rica en carbohidratos aumentan el flujo glucolítico, el citrato, el acetil-CoA citosólico, ACC, '
           'FASN y NADPH; insulina, ChREBP y SREBP-1c promueven la biosíntesis.')


def t16c(D):
    s = new(D, U, '16 · TAG hepáticos en saciedad y en ayuno; hígado graso')
    l = card(s, 0.4, 1.1, 6.1, 3.0, '- **↑ DNL**: citrato → ATP-citrato liasa → ACC → FASN.\n- Glicerol-3-P desde **glucólisis**.\n- Insulina, ChREBP y SREBP-1c **inducen** la maquinaria.', MINT, 15, head='Saciedad', headfill=ACT)
    r = card(s, 6.8, 1.1, 6.1, 3.0, '- **↓ DNL**, pero el hígado **sigue formando TAG y VLDL** desde AG del **adiposo**.\n- Insulina baja, AMPK y CPT1 favorecen la **β-oxidación**.\n- La proporción oxidación/almacenamiento depende del contexto.', LBLUE, 15, head='Ayuno', headfill=TRN)
    e = note_box(s, 0.4, 4.3, 12.5, 0.95, 'No es correcto oponer «ayuno = cero síntesis de TAG».', 16)
    liver(s, 0.6, 5.4, 2.6, name='Hígado graso')
    lipid_drops(s, 1.0, 5.55, 1.8, 1.0, [(200, 400, 120), (500, 300, 150), (750, 550, 110), (400, 700, 100)], name='Gotas esteatosis')
    m = card(s, 3.5, 5.4, 9.4, 1.7, '**Esteatosis / MASLD** (enfermedad hepática esteatósica asociada a disfunción metabólica): surge de la integración entre **entrada de AG, DNL, oxidación y exportación de VLDL**; no se explica únicamente por comer grasas.', YEL, 14, head='Clínica')
    s.step(fade(l)); s.step(fade(r)); s.step(zoom(e)); s.step(fade(m))
    s.note('Saciedad rica en carbohidratos: aumenta la lipogénesis de novo y la secreción de VLDL puede aumentar si la '
           'lipogénesis y la esterificación exceden la oxidación y la depuración. Ayuno: disminuye la lipogénesis de novo, pero el '
           'hígado puede seguir formando TAG y VLDL a partir de AG derivados de la lipólisis periférica; según el balance de AG '
           'puede reesterificar una porción y secretarla. Clínica: la esteatohepatopatía asociada a disfunción metabólica (MASLD) '
           'surge de la integración entre entrada de AG, lipogénesis de novo, oxidación y exportación de VLDL.')


# ------------------------------------------------------------------ TEMA 17
def t17a(D):
    s = new(D, U, '17 · Ácidos grasos de cadena corta y media: otra ruta de absorción')
    defs = s.group_start('Definiciones')
    for i, (t, d, col) in enumerate((('Corta', '< 6 C', 'D5F5E3'), ('Media', '6–12 C', 'FCF3CF'), ('Larga', '≥ 14 C', 'FAD7A0'))):
        s.shape(0.4 + i * 2.1, 1.1, 1.95, 0.85, 'rect', col, (INK, 1.25), SHD, '**%s**\n%s' % (t, d), 15, F_HEAD, INK, False, 'c', 'm')
    s.group_end()
    enterocyte_row(s, 0.4, 2.4, 6.2, 2.2, 3, name='Enterocitos')
    s.shape(0.4, 4.8, 2.9, 0.8, 'rect', ('lin', [(0, 'FDFEFE'), (100, 'EAF2F8')], 90), ('85929E', 1.0), False, 'Linfa (quilífero)', 13, F_HEAD, '34495E', True, 'c', 'm', name='Linfa')
    vessel(s, 3.6, 4.8, 3.0, 0.8, name='Capilar portal', rbcs=2)
    s.text(3.7, 5.65, 2.8, 0.3, 'Vena porta → hígado', 12.5, F_HEAD, '6E1A12', True, 'c')
    lc = ag_chain(s, 0.8, 2.0, 1.2, 0.2, name='AG largo'); mc = ag_chain(s, 4.3, 2.0, 0.6, 0.2, name='AG medio')
    qm = lipoprotein(s, 1.2, 3.2, 0.8, 'F7DC6F', 'QM', [('2E4A9E', 200, 120, 4, None)], name='QM')
    alb = s.shape(4.0, 3.4, 1.0, 0.45, 'ellipse', shade('F9E79F', 0.4, 0.2), ('9A7D0A', 1.0), False, 'Albúmina', 10, F_HEAD, INK, True, 'c', 'm', name='Albúmina')
    k1 = card(s, 6.9, 1.1, 6.0, 2.45, '- Más **solubles**; tras la digestión una mayor fracción de **C8/C10** pasa al **sistema portal** unida a albúmina.\n- Entrada mitocondrial **relativamente independiente de CPT1/carnitina**: oxidación y cetogénesis rápidas.', CREAM, 14, head='Cadena media (C8/C10)')
    k2 = card(s, 6.9, 3.75, 6.0, 1.55, 'Muchos AG largos se **reesterifican** en el enterocito y viajan en **QM por linfa**.', YEL, 14, head='Cadena larga')
    k3 = note_box(s, 0.4, 6.05, 12.5, 1.05, '**C12 (laurato)** es intermedio y no se comporta como C8/C10: no todas las mezclas comerciales «MCT» son equivalentes.', 14.5)
    s.step(fade(defs))
    s.step(fade(lc), path(lc, 0.0, 1.2, after=True, dur=900), zoom(qm, after=True), path(qm, 0.0, 1.6, after=True, dur=1100), fade(k2))
    s.step(fade(mc), path(mc, 0.0, 1.4, after=True, dur=900), fade(alb, after=True), path(alb, 0.6, 1.5, after=True, dur=1100), fade(k1))
    s.step(fade(k3))
    s.note('Definiciones habituales: cadena corta <6 carbonos, media 6–12 (algunas clasificaciones incluyen C12), larga ≥14. '
           'Los AG de cadena media son más solubles; tras la digestión, una mayor fracción de C8/C10 pasa al sistema portal unida '
           'a albúmina y se dirige al hígado. Su entrada mitocondrial es relativamente independiente de CPT1/carnitina y su '
           'oxidación y cetogénesis pueden ser rápidas. En contraste, muchos AG largos se reesterifican en el enterocito y se '
           'transportan en quilomicrones por la linfa. El laurato (C12) es intermedio y no se comporta como C8/C10.')


def t17b(D):
    s = new(D, U, '17 · MCT: beneficios, límites y leche humana')
    b = card(s, 0.4, 1.1, 6.1, 3.0, '- Combustible **rápido** con menor dependencia de **QM** y de la **lanzadera de carnitina**.\n- Útil **bajo indicación especializada**: trastornos de transporte/oxidación de AG largos o **quilomicronemia familiar**.', MINT, 14.5, head='Beneficios potenciales', headfill=ACT)
    lm = card(s, 6.8, 1.1, 6.1, 3.0, '- **No** son «grasas que no se almacenan»: aportan calorías y se almacenan si hay superávit.\n- **No reemplazan** a los AG esenciales.\n- **No garantizan** adelgazamiento.', LSALMON, 14.5, head='Límites', headfill=INH)
    mk = card(s, 0.4, 4.35, 12.5, 2.75, '- Mezcla de **AG largos** y proporciones variables de **cadena media** (sobre todo **C10–C14**), según dieta y etapa de lactancia.\n- Beneficio para el lactante: fuente energética **accesible** y composición adaptada.\n- **No** afirmar que los TAG de cadena corta/media sean la mayoría de sus lípidos: se requieren AG **esenciales y de cadena larga** para el desarrollo neuronal y las membranas.', YEL, 14.5, head='Leche humana')
    s.step(fade(b)); s.step(fade(lm)); s.step(fade(mk))
    s.note('Beneficios potenciales de los MCT: combustible rápido con menor dependencia de quilomicrones y de la lanzadera de '
           'carnitina; útiles bajo indicación especializada en trastornos de transporte u oxidación de AG largos o en '
           'quilomicronemia familiar. Límites: aportan calorías y pueden almacenarse si existe superávit; no reemplazan AG '
           'esenciales ni garantizan adelgazamiento. Leche humana: contiene AG largos y proporciones variables de cadena media '
           '(sobre todo C10–C14) según dieta y etapa de lactancia; no son la mayoría de sus lípidos.')


def t17c(D):
    s = new(D, U, '17 · Síntesis de grasa en la glándula mamaria lactante')
    c = chain(s, 0.5, 1.2, ['Glucosa (GLUT1)', 'Acetil-CoA / citrato + NADPH', 'Malonil-CoA', 'AG de cadena media y larga', 'TAG → glóbulo graso'], dy=1.05, w=3.0,
              enzymes=['glucólisis · PPP', 'ACC', 'FASN + tioesterasa', 'GPAT · AGPAT · DGAT'], rev=[False] * 4,
              fill=[LBLUE, ENE, lighten(MOL['mal'][0], 0.55), YEL, 'F9E79F'], name='Síntesis mamaria', h=0.5, size=13.5)
    lac = chip(s, 3.9, 1.5, 'también → **lactosa**', LBLUE, 12.5, name='Lactosa')
    rows = [['', 'Hepatocito', 'Glándula mamaria'],
            ['Longitud de AG sintetizados', 'Típicamente **C16**', '**Más cortos** (terminación temprana: tioesterasa/especificidad mamaria)'],
            ['Glicerol-3-P', 'Glucólisis / glicerol cinasa', 'Glucólisis'],
            ['AG preformados', 'Plasma, remanentes', 'AG **maternos** también se incorporan'],
            ['Destino del TAG', 'Gotas o **VLDL** (ApoB-100)', '**Glóbulos de grasa de la leche** rodeados de membrana epitelial']]
    t, H = table(s, 5.9, 1.15, 7.0, rows, [1.9, 2.1, 3.0], size=13.5, rowh=0.6, name='Tabla mamaria')
    chain_anim(s, c, per_click=2)
    s.anim[0].append(fade(lac, after=True))
    s.step(fade(t))
    s.note('Síntesis en la glándula mamaria lactante: la glucosa llega por GLUT1, participa en la síntesis de lactosa y '
           'proporciona acetil-CoA/citrato y NADPH para la síntesis de AG (acetato y otros precursores pueden contribuir). La ACC '
           'genera malonil-CoA; la FASN alarga las cadenas y la terminación temprana favorece AG de menor longitud que la síntesis '
           'típica de C16, por la maquinaria tioesterasa y la especificidad mamaria (con variaciones entre especies). El '
           'glicerol-3-P procede de la glucólisis; GPAT/AGPAT/DGAT ensamblan TAG; también se incorporan AG maternos preformados. '
           'En el hepatocito el destino frecuente es el almacenamiento o la VLDL; en la mama, la secreción de glóbulos de grasa '
           'rodeados por membrana derivada de la célula epitelial.')


def build(D):
    m3a(D); m3b(D); m3c(D); m3d(D); m3e(D)
    t15a(D); t15b(D); t15c(D); t15d(D); t15e(D)
    t16a(D); t16b(D); t16c(D)
    t17a(D); t17b(D); t17c(D)
