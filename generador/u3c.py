# -*- coding: utf-8 -*-
"""UNIDAD III — temas 18 a 24"""
from base import *

U = 3


def t18a(D):
    s = new(D, U, '18 · Ácidos grasos esenciales: por qué no los fabricamos')
    def fa(y, name, lab, dbs, col):
        g = s.group_start(name)
        n = 18
        pts = [(0.9 + i * 0.36, y + (0.3 if i % 2 else 0)) for i in range(n)]
        s.arrow(pts, col, 3, tail=None)
        s.shape(0.55, y - 0.05, 0.4, 0.4, 'ellipse', shade('E74C3C', 0.4, 0.2), ('922B21', 1.0), False, 'COOH', 7, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
        for d in dbs:
            x = 0.9 + (d - 1) * 0.36
            s.shape(x + 0.04, y - 0.25, 0.3, 0.2, 'rect', ('a', col, 60), None, False)
        s.text(7.4, y - 0.1, 5.5, 0.5, lab, 15, F_HEAD, INK, True, 'l', 'm')
        return s.group_end()
    la = fa(1.6, 'Linoleico', '**Ácido linoleico (LA)** · 18:2 n-6', [9, 12], 'C0392B')
    al = fa(2.8, 'Alfa-linolénico', '**Ácido α-linolénico (ALA)** · 18:3 n-3', [9, 12, 15], '2471A3')
    lim = s.shape(0.9 + 8 * 0.36 + 0.05, 1.15, 0.12, 2.3, 'rect', ('a', '1E8449', 70), None, False, name='Límite delta9')
    lt = chip(s, 2.2, 3.55, 'Δ9: límite de nuestras desaturasas desde el extremo carboxilo', MINT, 12.5, name='Rótulo delta9')
    k = card(s, 0.4, 4.25, 6.1, 2.85, 'Los humanos **no introducimos dobles enlaces más allá de Δ9** (contando desde el carboxilo): no sintetizamos de novo las familias **n-6 y n-3** a partir de n-9.', CREAM, 14.5, head='Fundamento')
    cv = chain(s, 6.85, 4.35, ['LA (18:2 n-6) → **AA** (20:4 n-6)', 'ALA (18:3 n-3) → **EPA** → **DHA**'], dy=1.25, w=6.0, enzymes=None, rev=[True], fill=[LSALMON, LBLUE], name='Conversiones', h=0.65, size=14)
    nt = s.text(6.9, 6.35, 6.0, 0.7, 'Elongaciones y desaturaciones; conversión humana **limitada**, especialmente a DHA.', 13.5, F_BODY, INK, False, 'l', 'm')
    s.step(fade(la)); s.step(fade(al)); s.step(fade(lim), fade(lt, after=True)); s.step(fade(k)); s.step(fade(cv[0][0]), fade(cv[1][0], after=True), fade(nt))
    s.note('Ácido linoleico (LA, 18:2 n-6) y ácido α-linolénico (ALA, 18:3 n-3) son esenciales: los humanos no introducimos dobles '
           'enlaces más allá de la posición Δ9 contando desde el extremo carboxilo, por lo que no sintetizamos de novo las familias '
           'n-6 y n-3 a partir de n-9. El LA se convierte en ácido araquidónico (AA, 20:4 n-6); el ALA en EPA y DHA por '
           'elongaciones y desaturaciones, con conversión humana limitada, especialmente a DHA. En el esquema, las barras marcan '
           'los dobles enlaces y la franja verde el límite Δ9.')


def t18b(D):
    s = new(D, U, '18 · Funciones y déficit de ácidos grasos esenciales')
    fn = [('Membranas', 'fluidez y función', 'membrane'), ('Barrera cutánea', 'integridad', 'skin'), ('Crecimiento', 'desarrollo', 'grow'),
          ('Retina y SNC', '**DHA**', 'brain'), ('Eicosanoides', 'prostaglandinas, tromboxanos, leucotrienos', 'eic'), ('Mediadores proresolutivos', 'desde ciertos PUFA', 'res')]
    ids = []
    for i, (t, d, k) in enumerate(fn):
        x = 0.4 + (i % 3) * 2.75; y = 1.1 + (i // 3) * 2.1
        g = s.group_start('Función ' + t)
        s.shape(x, y, 2.6, 1.9, 'rect', LBLUE if i % 2 else MINT, (INK, 1.25), SHD)
        if k == 'brain':
            brain(s, x + 0.9, y + 0.1, 0.8)
        elif k == 'membrane':
            membrane_h(s, x + 0.3, y + 0.2, 2.0, 0.42)
        else:
            mol(s, x + 1.05, y + 0.12, 'ag', '', d=0.5)
        s.text(x + 0.1, y + 0.75, 2.4, 0.45, t, 15, F_HEAD, INK, True, 'c', 'm')
        s.text(x + 0.1, y + 1.2, 2.4, 0.65, d, 12.5, F_BODY, INK, False, 'c', 't')
        s.group_end(); ids.append(g)
    dfc = card(s, 8.85, 1.1, 4.05, 3.15, '- **Dermatitis descamativa**\n- Alteración del crecimiento\n- ↑ pérdida transepidérmica de agua\n- Anomalías reproductivas/inmunes (casos avanzados)', LSALMON, 14, head='Déficit')
    w = card(s, 8.85, 4.45, 4.05, 2.65, 'Deben garantizarse en dietas **muy bajas en grasa** (por ejemplo, quilomicronemia). DHA: **condicionalmente** importante en el desarrollo.', YEL, 13.5, head='Clínica')
    m = note_box(s, 0.4, 5.4, 8.2, 1.7, 'AA y EPA compiten parcialmente por enzimas, pero el efecto depende de **dosis y tejido**: evitar la simplificación «omega-6 malo, omega-3 bueno».', 14.5)
    s.step(*[fade(g, after=(i > 0)) for i, g in enumerate(ids)]); s.step(fade(dfc)); s.step(fade(w)); s.step(fade(m))
    s.note('Funciones: membranas y fluidez; integridad de la barrera cutánea; crecimiento; retina y tejido nervioso (DHA); '
           'eicosanoides (prostaglandinas, tromboxanos, leucotrienos) y mediadores especializados proresolutivos a partir de '
           'ciertos PUFA. AA y EPA compiten parcialmente por enzimas, pero el efecto biológico depende de dosis y tejidos. '
           'Déficit: dermatitis descamativa, alteración del crecimiento, pérdida transepidérmica de agua y anomalías '
           'reproductivas e inmunes en casos avanzados. Deben incorporarse especialmente en dietas muy bajas en grasa por '
           'quilomicronemia. El DHA se considera condicionalmente importante durante el desarrollo.')


# ------------------------------------------------------------------ TEMA 19
def t19a(D):
    s = new(D, U, '19 · Quilomicrones frente a VLDL')
    qm = lipoprotein(s, 0.6, 1.2, 2.4, 'F7DC6F', 'QM', [('2E4A9E', 200, 110, 7, 'ApoB-48'), ('27AE60', 330, 30, 5, 'C-II'), ('8E44AD', 20, 30, 5, 'E')], name='QM grande')
    vl = lipoprotein(s, 0.85, 4.3, 1.9, 'F5CBA7', 'VLDL', [('2E4A9E', 190, 150, 7, 'ApoB-100'), ('27AE60', 350, 30, 4, 'C-II'), ('8E44AD', 30, 30, 4, 'E')], name='VLDL grande')
    rows = [['', 'Quilomicrón (QM)', 'VLDL'],
            ['Origen', '**Intestino** (enterocito)', '**Hígado**'],
            ['Apolipoproteína estructural', '**ApoB-48**', '**ApoB-100**'],
            ['Lípidos transportados', 'TAG **dietarios**, colesterol, vitaminas liposolubles', 'TAG **endógenos** (DNL, AG plasmáticos, recambio)'],
            ['Vía de ingreso a la sangre', 'Linfa → conducto torácico', 'Directa (vena hepática)'],
            ['Producto tras LPL', 'Remanente (captación por **ApoE**)', '**IDL → LDL**'],
            ['Unión al receptor LDL', 'ApoB-48 **carece** de la región de unión', 'ApoB-100 es **ligando** del LDLR']]
    t, H = table(s, 3.4, 1.15, 9.5, rows, [2.5, 3.5, 3.5], size=14, rowh=0.62, name='Tabla QM VLDL')
    s.step(fade(qm), fade(vl, after=True)); s.step(fade(t))
    s.note('Quilomicrones: nacen en el intestino y contienen ApoB-48; transportan TAG dietarios, colesterol, vitaminas '
           'liposolubles y otros lípidos; pasan por la linfa a la sangre; adquieren ApoC-II y ApoE. VLDL: nacen en el hígado, '
           'contienen ApoB-100 y exportan TAG endógenos provenientes de lipogénesis de novo, AG plasmáticos y recambio hepático. '
           'La LPL transforma la VLDL en remanentes (IDL) y luego en LDL, comparativamente rica en colesterol esterificado. La '
           'ApoB-100 es ligando del receptor LDL; la ApoB-48 carece de su región de unión específica.')


def t19b(D):
    s = new(D, U, '19 · Esquema de lipoproteínas: vías exógena y endógena', 'RUTA ANIMADA')
    intestine(s, 0.3, 1.1, 1.7, name='Intestino lp')
    liver(s, 0.3, 4.4, 2.4, name='Hígado lp')
    vessel(s, 2.6, 2.05, 7.6, 0.75, name='Capilar exógena', rbcs=3)
    vessel(s, 2.6, 5.15, 7.6, 0.75, name='Capilar endógena', rbcs=3)
    s.text(2.7, 1.1, 4, 0.35, 'VÍA EXÓGENA (lípidos dietarios)', 14, F_HEAD, '7E5109', True, 'l')
    s.text(2.7, 4.2, 4, 0.35, 'VÍA ENDÓGENA (lípidos hepáticos)', 14, F_HEAD, '7E5109', True, 'l')
    qm = lipoprotein(s, 2.2, 1.6, 1.0, 'F7DC6F', 'QM', [('2E4A9E', 200, 110, 5, None)], name='QM ruta')
    lpl1 = enz(s, 5.4, 2.9, 'LPL + ApoC-II', name='LPL 1')
    ag1 = ag_chain(s, 5.6, 3.35, 0.8, 0.15, name='AG exógenos')
    rem = lipoprotein(s, 7.0, 1.75, 0.75, 'F39C12', 'Rem', [('8E44AD', 300, 60, 4, None)], name='Remanente QM')
    vl = lipoprotein(s, 2.3, 4.75, 0.9, 'F5CBA7', 'VLDL', [('2E4A9E', 190, 150, 5, None)], name='VLDL ruta')
    lpl2 = enz(s, 4.3, 6.0, 'LPL', name='LPL 2')
    idl = lipoprotein(s, 5.3, 4.85, 0.75, 'F0B27A', 'IDL', [('2E4A9E', 190, 150, 4, None)], name='IDL')
    hl = enz(s, 6.2, 6.0, 'Lipasa hepática', name='HL')
    ldl = lipoprotein(s, 7.4, 4.9, 0.65, 'E67E22', 'LDL', [('2E4A9E', 180, 180, 4, None)], name='LDL')
    ldlr = chip(s, 8.3, 6.0, 'LDLR (hígado y tejidos)', LBLUE, 12, name='LDLR')
    a1 = s.arrow([(7.6, 1.9), (2.4, 4.4)], '8E44AD', 2.5, dash='dash', name='Remanente a hígado')
    hdl = lipoprotein(s, 4.4, 3.35, 0.65, 'FDEBD0', 'HDL', [('5DADE2', 180, 160, 4, None)], name='HDL ruta')
    ex = s.arrow([(4.75, 3.35), (3.0, 2.4)], ACT, 2.0, name='HDL dona apos')
    k = card(s, 10.4, 1.1, 2.5, 6.0, '- **ApoC-II** activa LPL; **ApoC-III** y **ANGPTL3/4/8** modulan la depuración.\n- Remanentes ricos en colesterol → hígado (**ApoE**).\n- **LDL**: rica en colesterol esterificado.', CREAM, 13, head='Claves')
    s.step(fade(qm), path(qm, 1.6, 0.25, after=True, dur=1200), fade(hdl), wipe(ex, 'r', after=True))
    s.step(path(qm, 3.2, 0.25, dur=1400), fade(lpl1, after=True), fade(ag1, after=True), out(qm, after=True), fade(rem))
    s.step(wipe(a1, 'r'))
    s.step(fade(vl), path(vl, 1.2, 0.2, after=True, dur=1000), fade(lpl2, after=True), out(vl, after=True), fade(idl))
    s.step(fade(hl), out(idl, after=True), fade(ldl), fade(ldlr, after=True))
    s.step(fade(k))
    s.note('Vía exógena: el QM sale del intestino, recibe ApoC-II y ApoE de las HDL; la LPL capilar (activada por ApoC-II) '
           'hidroliza sus TAG y libera AG; el remanente rico en colesterol es captado por el hígado mediante ApoE. Vía endógena: '
           'el hígado secreta VLDL (ApoB-100); la LPL la convierte en IDL; la lipasa hepática y la LPL completan la conversión en '
           'LDL, rica en colesterol esterificado, que se capta por el receptor LDL (ApoB-100 como ligando). ApoC-III y '
           'ANGPTL3/4/8 modifican la depuración según el contexto (por ejemplo, ANGPTL4 reduce la LPL adiposa en ayuno).')


def t19c(D):
    s = new(D, U, '19 · HDL, intercambio de lípidos y cambio alimentación–ayuno')
    hdl = lipoprotein(s, 0.6, 1.2, 1.6, 'FDEBD0', 'HDL', [('5DADE2', 160, 200, 6, 'ApoA-I')], name='HDL grande')
    c1 = card(s, 2.6, 1.1, 4.3, 2.1, '- Intercambia apoproteínas y lípidos.\n- **LCAT** esterifica colesterol en la HDL.\n- **CETP** intercambia ésteres de colesterol por TAG de VLDL/remanentes.', CREAM, 13.5, head='HDL')
    n1 = note_box(s, 0.4, 3.4, 6.5, 1.0, 'El valor de **HDL-C** no resume automáticamente la **funcionalidad** de la HDL.', 14)
    al = card(s, 7.2, 1.1, 5.7, 1.9, '**Alimentación**: aparecen QM; el hígado sigue secretando VLDL; ambos **compiten** por la depuración de TAG (LPL).', MINT, 13.5, head='Alimentación')
    ay = card(s, 7.2, 3.15, 5.7, 1.9, '**Ayuno**: casi no deberían persistir QM; la **VLDL sí circula** (AG del adiposo). Un ayuno insuficiente puede mostrar QM tras una comida grasa.', LBLUE, 13.5, head='Ayuno')
    ds = card(s, 0.4, 4.6, 12.5, 2.5, '- Deficiencia de **LPL, ApoC-II, GPIHBP1 o APOA5** → **quilomicronemia** severa, hipertrigliceridemia y riesgo de **pancreatitis**.\n- **Resistencia insulínica**: exceso de AG hepáticos, DNL y alteración de la depuración → ↑ **VLDL** y partículas **remanentes**.', LSALMON, 14.5, head='Enfermedad')
    s.step(fade(hdl), fade(c1, after=True)); s.step(fade(n1)); s.step(fade(al)); s.step(fade(ay)); s.step(fade(ds))
    s.note('HDL: intercambia apoproteínas y lípidos; la LCAT esterifica colesterol en la HDL; la CETP intercambia ésteres de '
           'colesterol con TAG de VLDL y remanentes de QM. El valor de HDL-C no resume la funcionalidad de la HDL. '
           'Alimentación: aparecen QM y los AG dietarios se reparten según demanda, insulina y LPL; el hígado puede continuar '
           'secretando VLDL y las partículas compiten por la capacidad de depuración. Ayuno: casi no deberían persistir QM tras un '
           'tiempo suficiente; la VLDL circula. Enfermedad: deficiencia de LPL, ApoC-II, GPIHBP1 o APOA5 causa quilomicronemia '
           'severa con riesgo de pancreatitis; en la resistencia insulínica aumentan VLDL y remanentes.')


# ------------------------------------------------------------------ TEMA 20
def t20a(D):
    s = new(D, U, '20 · AMPK: estructura y activación')
    a = s.shape(1.0, 1.8, 2.2, 1.6, 'roundRect', shade('E74C3C', 0.35, 0.2), (INK, 1.5), SHD, 'α\n(catalítica)', 16, F_HEAD, WHITE, True, 'c', 'm', name='Subunidad alfa', adj={'adj': 30000})
    b = s.shape(3.2, 1.8, 1.4, 1.6, 'roundRect', shade('F5B041', 0.35, 0.2), (INK, 1.5), SHD, 'β', 20, F_HEAD, INK, True, 'c', 'm', name='Subunidad beta', adj={'adj': 30000})
    g = s.shape(4.6, 1.8, 1.8, 1.6, 'roundRect', shade('5DADE2', 0.35, 0.2), (INK, 1.5), SHD, 'γ\n(sensor)', 16, F_HEAD, INK, True, 'c', 'm', name='Subunidad gamma', adj={'adj': 30000})
    amp = mol(s, 5.0, 3.6, 'atp', 'AMP/ADP', d=0.5, w=1.3, name='AMP ADP')
    t172 = mol(s, 1.6, 1.25, 'atp', 'P-Thr172', d=0.45, w=1.3, name='Thr172')
    lk = enz(s, 0.4, 3.7, 'LKB1', name='LKB1'); ck = enz(s, 1.5, 3.7, 'CaMKKβ (Ca^{2+})', name='CaMKK')
    a1 = s.arrow([(0.9, 3.68), (1.6, 1.7)], ACT, 2.5); a2 = s.arrow([(2.3, 3.68), (2.1, 1.7)], ACT, 2.5)
    a3 = s.arrow([(5.6, 3.62), (5.5, 3.4)], ACT, 2.5)
    st = card(s, 0.4, 4.5, 6.2, 2.6, '- ↓ relación energética **ATP/AMP-ADP**\n- **Contracción**, **hipoxia** y otros estímulos\n- Integra también señales **lisosomales** y de nutrientes', CREAM, 14.5, head='Estímulos')
    k = card(s, 6.9, 1.1, 6.0, 3.0, '**Heterotrímero**: α catalítica; β y γ reguladoras. El **AMP/ADP** unido a γ **protege** y **facilita** la fosforilación de **Thr172** (principalmente por **LKB1**; **CaMKKβ** por Ca^{2+}).', YEL, 14.5, head='Mecanismo')
    p = note_box(s, 6.9, 4.3, 6.0, 2.8, 'Paradoja aparente: activar AMPK **no produce ATP directamente**; **reorienta rutas** para que la generación supere al consumo.', 15.5)
    s.step(fade(a), fade(b, after=True), fade(g, after=True))
    s.step(zoom(amp), wipe(a3, 't', after=True), pulse(g, after=True))
    s.step(fade(lk), fade(ck), wipe(a1, 't', after=True), wipe(a2, 't'), zoom(t172, after=True))
    s.step(fade(k)); s.step(fade(st)); s.step(fade(p))
    s.note('La proteína cinasa activada por AMP (AMPK) es un heterotrímero: subunidad α catalítica, β y γ reguladoras. El AMP y '
           'el ADP unidos a la subunidad γ protegen y facilitan la activación por fosforilación de Thr172, principalmente por LKB1; '
           'la CaMKKβ puede activarla en respuesta al Ca2+. Se activa cuando baja la relación energética ATP/AMP-ADP, ante '
           'contracción, hipoxia y otros estímulos, e integra también señales lisosomales y de nutrientes. Activar AMPK no produce '
           'ATP directamente: reorienta las rutas.')


def t20b(D):
    s = new(D, U, '20 · Mapa de AMPK y sus principales efectos')
    c = s.shape(5.15, 3.0, 3.0, 1.5, 'ellipse', shade('E74C3C', 0.35, 0.2), (INK, 2.0), SHD, 'AMPK', 30, F_HEAD, WHITE, True, 'c', 'm', name='AMPK centro', fit=False)
    eff = [('ACC1/ACC2 fosforiladas', '↓ síntesis de AG, ↓ malonil-CoA, ↑ β-oxidación', INH, 0.4, 1.1),
           ('mTORC1 inhibido', 'vía **TSC2/raptor**: ↓ síntesis proteica', INH, 0.4, 3.1),
           ('HMG-CoA reductasa', 'fosforilada/inhibida: ↓ síntesis de colesterol', INH, 0.4, 5.1),
           ('GLUT4 (ejercicio)', '↑ captación de glucosa muscular', ACT, 9.0, 1.1),
           ('PGC-1α', '**biogénesis mitocondrial** (adaptación sostenida)', ACT, 9.0, 3.1),
           ('ULK1', '**autofagia** y homeostasis mitocondrial', ACT, 9.0, 5.1)]
    ids = []
    for t, d, col, x, y in eff:
        g = s.group_start('Efecto ' + t[:14])
        if col == INH:
            s.inhib([(5.2, 3.75), (x + 3.95, y + 0.75)], w=2.5)
        else:
            s.arrow([(8.1, 3.75), (x + 0.05, y + 0.75)], ACT, 2.5)
        card(s, x, y, 3.9, 1.6, '**%s**\n%s' % (t, d), MINT if col == ACT else LSALMON, 14, anchor='m', grow=False)
        s.group_end(); ids.append(g)
    m = card(s, 4.6, 5.0, 4.1, 2.1, '**Metformina** puede activar AMPK indirectamente, pero su efecto antihiperglucémico **no se reduce** a ese mecanismo.', YEL, 13, name='Metformina')
    w = s.text(4.6, 1.15, 4.1, 1.55, 'No todas las células oxidan AG: el **eritrocito no puede**; la actividad no depende **solo** de AMPK.', 13.5, F_BODY, INK, False, 'c', 'm', name='Precisión AMPK')
    s.step(zoom(c))
    for g in ids:
        s.step(fade(g))
    s.step(fade(w)); s.step(fade(m))
    s.note('Efectos inmediatos de la AMPK: fosforila ACC1/ACC2 (menos síntesis de AG, menos malonil-CoA, mayor potencial de '
           'β-oxidación), inhibe procesos biosintéticos consumidores de ATP (síntesis de colesterol vía HMG-CoA reductasa, síntesis '
           'proteica al frenar mTORC1 directa e indirectamente vía TSC2/raptor) y regula la captación de glucosa por GLUT4 durante '
           'el ejercicio. Adaptación sostenida: promueve biogénesis mitocondrial y autofagia por redes PGC-1α, ULK1 y otras. La '
           'metformina puede activar AMPK indirectamente en ciertas condiciones, pero su efecto antihiperglucémico no se reduce a '
           'ese mecanismo y depende de concentraciones y tejidos.')


# ------------------------------------------------------------------ TEMA 21
def t21a(D):
    s = new(D, U, '21 · Biosíntesis de colesterol en el hepatocito')
    c = chain(s, 0.5, 1.15, ['Acetil-CoA (×3)', 'Acetoacetil-CoA', 'HMG-CoA (citosólico)', 'Mevalonato', 'IPP / DMAPP (isoprenoides)', 'Escualeno', 'Lanosterol', 'Colesterol'],
              dy=0.74, w=2.8, enzymes=['tiolasa', 'HMG-CoA sintasa 1', '**HMG-CoA reductasa** (2 NADPH)', 'cinasas (ATP)', None, None, 'múltiples pasos'],
              rev=[True, True, False, False, False, False, False], fill=[ENE, YEL, YEL, MINT, YEL, YEL, YEL, 'F39C12'], name='Colesterol', h=0.48, size=13.5)
    rl = s.shape(0.35, 2.55, 6.2, 0.95, 'rect', None, (INH, 2.5, 'dash'), False, name='Resalte paso limitante')
    k = card(s, 7.0, 1.1, 5.9, 2.4, 'La **HMG-CoA reductasa** (RE, citosol) es la **enzima de control clásico** de la vía; usa NADPH.', YEL, 14.5, head='Paso limitante')
    nb = note_box(s, 7.0, 3.7, 5.9, 2.0, 'No confundir: **HMG-CoA reductasa** (colesterol, citosol/RE) ≠ **HMG-CoA liasa** mitocondrial (cetogénesis).', 14.5)
    st = card(s, 7.0, 5.9, 5.9, 1.2, 'Las **estatinas** inhiben competitivamente la HMG-CoA reductasa.', MINT, 14)
    chain_anim(s, c, per_click=2)
    s.step(fade(rl), fade(k)); s.step(fade(nb)); s.step(fade(st))
    s.note('Biosíntesis hepática: acetil-CoA → acetoacetil-CoA → HMG-CoA (citosólico, HMG-CoA sintasa 1) → mevalonato, '
           'catalizado por la HMG-CoA reductasa con NADPH; siguen isoprenoides activados (IPP/DMAPP), escualeno, lanosterol y '
           'colesterol. La HMG-CoA reductasa del RE es la enzima de control clásico. No confundir con la HMG-CoA liasa '
           'mitocondrial de la cetogénesis (ni con la HMG-CoA sintasa 2 mitocondrial).')


def t21b(D):
    s = new(D, U, '21 · Regulación de la HMG-CoA reductasa')
    h = s.shape(4.65, 2.9, 4.0, 1.6, 'roundRect', 'FFFFFF', ('1F3864', 3.0), SHD, 'HMG-CoA\nREDUCTASA', 24, F_HEAD, '1F3864', True, 'c', 'm', name='HMGCR', adj={'adj': 30000})
    regs = [('SREBP-2 ↑ transcripción', 'cuando el **colesterol intracelular es bajo**', ACT, 0.4, 1.1),
            ('Insulina', 'puede **favorecer** su actividad', ACT, 0.4, 4.9),
            ('Esteroles', 'favorecen su **degradación** (Insig, ubiquitinación)', INH, 9.0, 1.1),
            ('AMPK', '**fosforila e inhibe** la enzima', INH, 9.0, 3.0),
            ('Glucagón / ayuno', 'reducen su actividad', INH, 9.0, 4.9)]
    ids = []
    for t, d, col, x, y in regs:
        g = s.group_start('Regulador ' + t[:12])
        if col == ACT:
            s.arrow([(x + 3.95, y + 0.75), (4.62, 3.7)], ACT, 3)
        else:
            s.inhib([(x + 0.0, y + 0.75), (8.68, 3.7)], w=3)
        card(s, x, y, 3.9, 1.5, '**%s**\n%s' % (t, d), MINT if col == ACT else LSALMON, 14, anchor='m', grow=False)
        s.group_end(); ids.append(g)
    k = card(s, 0.4, 2.9, 3.9, 1.6, 'Tres niveles: **transcripción**, **degradación** y **fosforilación**.', YEL, 14, anchor='m')
    s.step(zoom(h))
    for g in ids:
        s.step(fade(g))
    s.step(fade(k))
    s.note('La HMG-CoA reductasa se regula en varios niveles: SREBP-2 induce su gen cuando el colesterol intracelular es bajo; '
           'los esteroles favorecen su degradación (unión a Insig y ubiquitinación); la AMPK la fosforila e inhibe; la insulina '
           'puede favorecer su actividad frente al glucagón y el ayuno.')


def t21c(D):
    s = new(D, U, '21 · Homeostasis intracelular: SCAP/SREBP-2', 'RUTA ANIMADA')
    er = s.shape(0.4, 1.3, 3.9, 2.6, 'roundRect', ('a', 'D7BDE2', 85), ('6C3483', 2.0), False, 'RETÍCULO ENDOPLASMÁTICO', 13, F_HEAD, '4A235A', True, 'c', 't', name='RE', adj={'adj': 20000})
    go = s.shape(5.0, 1.3, 3.3, 2.6, 'roundRect', ('a', 'FAD7A0', 85), ('A04000', 2.0), False, 'GOLGI', 13, F_HEAD, '6E2C00', True, 'c', 't', name='Golgi', adj={'adj': 20000})
    nu = s.shape(9.0, 1.3, 3.9, 2.6, 'ellipse', ('a', 'BB8FCE', 80), ('4A235A', 2.0), False, 'NÚCLEO', 13, F_HEAD, '4A235A', True, 'c', 't', name='Núcleo')
    cx = s.group_start('Complejo SCAP-SREBP2')
    s.shape(1.0, 2.2, 1.4, 0.55, 'roundRect', shade('5DADE2', 0.35, 0.2), (INK, 1.25), False, 'SCAP', 13, F_HEAD, INK, True, 'c', 'm')
    s.shape(2.4, 2.2, 1.6, 0.55, 'roundRect', shade('F5B041', 0.35, 0.2), (INK, 1.25), False, 'SREBP-2', 13, F_HEAD, INK, True, 'c', 'm')
    s.group_end()
    ins = s.shape(1.3, 3.0, 1.4, 0.5, 'roundRect', 'D5D8DC', (INK, 1.0), False, 'Insig', 13, F_HEAD, INK, True, 'c', 'm', name='Insig')
    pr = enz(s, 5.5, 3.2, 'S1P / S2P (proteólisis)', name='Proteasas')
    nd = s.shape(5.9, 2.2, 1.6, 0.55, 'roundRect', shade('F5B041', 0.35, 0.2), (INK, 1.25), SHD, 'nSREBP-2', 13, F_HEAD, INK, True, 'c', 'm', name='SREBP nuclear')
    gn = chip(s, 9.6, 2.5, '↑ LDLR · ↑ HMGCR (· PCSK9)', MINT, 13, name='Genes SREBP2')
    lo = card(s, 0.4, 4.15, 6.1, 1.6, '**Colesterol bajo en el RE** → SCAP transporta SREBP-2 al Golgi → proteólisis → dominio **nuclear** → ↑ **síntesis y captación**.', LBLUE, 13.5)
    hi = card(s, 6.8, 4.15, 6.1, 1.6, '**Colesterol alto** → SCAP se une a **Insig** y retiene SREBP en el RE → ↓ síntesis/captación.', LSALMON, 13.5)
    ot = card(s, 0.4, 5.95, 12.5, 1.15, '**ACAT/SOAT** esterifica colesterol para depósito · **ABCA1/ABCG1** favorecen el eflujo a ApoA-I/HDL · **LXR** responde a oxiesteroles · **PCSK9** dirige el LDLR a degradación lisosomal.', CREAM, 13.5)
    s.step(fade(cx)); s.step(path(cx, 4.0, 0.0, dur=1400), fade(lo, after=True))
    s.step(fade(pr), fade(nd, after=True), path(nd, 3.75, 0.0, after=True, dur=1200), fade(gn, after=True))
    s.step(fade(ins), fade(hi, after=True)); s.step(fade(ot))
    s.note('Homeostasis intracelular del colesterol: cuando el colesterol es bajo en el RE, SCAP transporta SREBP-2 al Golgi, '
           'donde la proteólisis por S1P y S2P libera el dominio nuclear, que induce LDLR y HMGCR (y PCSK9). Con colesterol alto, '
           'SCAP se une a Insig y retiene SREBP en el RE. La ACAT/SOAT esterifica colesterol para su depósito; ABCA1/ABCG1 '
           'favorecen el eflujo hacia ApoA-I/HDL y LXR responde a oxiesteroles. PCSK9 dirige el LDLR a degradación lisosomal, '
           'disminuyendo su reciclado y la depuración de LDL. La animación muestra el traslado del complejo y del factor nuclear.')


def t21d(D):
    s = new(D, U, '21 · Captación de LDL por el receptor LDL', 'RUTA ANIMADA')
    membrane_h(s, 0.3, 2.0, 8.3, 0.42, name='Membrana')
    ldl = lipoprotein(s, 1.0, 0.95, 0.85, 'E67E22', 'LDL', [('2E4A9E', 180, 180, 4, None)], name='LDL')
    r = s.shape(1.25, 1.85, 0.35, 0.75, 'roundRect', shade('2E86C1', 0.35, 0.2), (INK, 1.0), False, name='LDLR', adj={'adj': 50000})
    pit = s.shape(0.8, 2.4, 1.3, 0.6, 'ellipse', None, ('A04000', 2.0, 'dash'), False, name='Fosita clatrina')
    s.text(0.3, 3.0, 2.4, 0.3, 'fosita recubierta (clatrina)', 11.5, F_HEAD, '6E2C00', True, 'c')
    en = s.shape(3.0, 3.1, 1.5, 1.2, 'ellipse', ('a', 'D6EAF8', 85), ('1F618D', 1.5), False, 'Endosoma (pH ↓)', 11.5, F_HEAD, INK, True, 'c', 'm', name='Endosoma')
    rc = s.arrow([(3.6, 3.05), (2.0, 2.45)], TRN, 2.5, curve=False, name='Reciclado LDLR')
    s.text(2.2, 2.55, 1.5, 0.3, 'LDLR recicla', 11.5, F_HEAD, TRN, True, 'c')
    ly = s.shape(5.2, 4.3, 1.6, 1.2, 'ellipse', ('a', 'F5B7B1', 85), ('922B21', 1.5), False, 'Lisosoma', 12, F_HEAD, INK, True, 'c', 'm', name='Lisosoma')
    ce = chip(s, 6.95, 4.65, 'CE → colesterol libre', YEL, 12.5, name='Hidrólisis CE')
    pc = s.shape(5.0, 1.05, 1.3, 0.55, 'roundRect', shade('C39BD3', 0.35, 0.2), (INK, 1.0), False, 'PCSK9', 13, F_HEAD, INK, True, 'c', 'm', name='PCSK9')
    pa = s.arrow([(5.4, 1.6), (5.8, 4.25)], '7D3C98', 2.5, dash='dash', name='PCSK9 a lisosoma')
    k = card(s, 8.9, 1.1, 4.0, 6.0, '- **LDL**: ApoB-100 y alto % de colesterol **esterificado**.\n- Endocitosis por **clatrina**; la acidificación libera la LDL y el **LDLR recicla**.\n- El lisosoma hidroliza ésteres de colesterol.\n- **PCSK9** desvía el LDLR al lisosoma → ↓ depuración de LDL.', CREAM, 14)
    s.step(path(ldl, 0.1, 0.85, dur=1100), pulse(r, after=True), fade(pit, after=True))
    s.step(fade(en), path(ldl, 2.15, 2.3, after=True, dur=1300), wipe(rc, 'r', after=True))
    s.step(fade(ly), path(ldl, 4.4, 3.45, after=True, dur=1200), fade(ce, after=True))
    s.step(fade(pc), wipe(pa, 't', after=True)); s.step(fade(k))
    s.note('Transporte a tejidos: el hígado exporta colesterol en VLDL y sus derivados; la LDL posee ApoB-100 y un elevado '
           'porcentaje de colesterol esterificado y es reconocida por el LDLR. Las células endocitan el complejo LDLR–LDL por '
           'fositas recubiertas de clatrina; la acidificación endosomal libera la LDL y el LDLR se recicla; los lisosomas '
           'hidrolizan los ésteres de colesterol y suministran colesterol libre. La PCSK9 se une al LDLR y lo dirige a degradación '
           'lisosomal, reduciendo su reciclado. La animación sigue la partícula LDL desde la membrana hasta el lisosoma.')


def t21e(D):
    s = new(D, U, '21 · Transporte reverso de colesterol')
    mac = s.shape(0.4, 3.0, 2.3, 2.0, 'ellipse', shade('F5CBA7', 0.4, 0.25), ('A04000', 1.75), SHD, 'Célula periférica\n(macrófago)', 13, F_HEAD, INK, True, 'c', 'm', name='Macrófago')
    ab = chip(s, 2.2, 2.6, 'ABCA1 / ABCG1', LBLUE, 12.5, name='ABCA1')
    pre = lipoprotein(s, 3.2, 3.4, 0.7, 'FDFEFE', 'ApoA-I', [('5DADE2', 180, 180, 4, None)], name='HDL naciente', tsize=9)
    lc = enz(s, 4.2, 2.55, 'LCAT', name='LCAT')
    hdl = lipoprotein(s, 4.9, 3.25, 1.1, 'FDEBD0', 'HDL madura', [('5DADE2', 160, 200, 5, None)], name='HDL madura', tsize=11)
    liver(s, 9.0, 2.6, 3.8, name='Hígado TR')
    sr = chip(s, 7.0, 2.6, 'SR-BI (selectiva)', MINT, 12.5, name='SRBI')
    ct = chip(s, 6.6, 4.9, 'CETP → lipoproteínas ApoB → hígado', LSALMON, 12.5, name='CETP')
    a1 = s.arrow([(2.65, 3.9), (3.2, 3.75)], ACT, 3); a2 = s.arrow([(3.9, 3.75), (4.9, 3.8)], ACT, 3)
    a3 = s.arrow([(6.0, 3.6), (9.2, 3.3)], ACT, 3); a4 = s.arrow([(5.6, 4.35), (6.6, 4.95)], '8E44AD', 2.5, dash='dash')
    p = note_box(s, 0.4, 5.75, 12.5, 1.35, '**Número de partículas** y **función** de la HDL son dimensiones distintas del **HDL-C** plasmático: un HDL-C alto **no garantiza causalmente** protección.', 15)
    s.step(fade(ab), wipe(a1, 'l', after=True), fade(pre, after=True))
    s.step(fade(lc), wipe(a2, 'l', after=True), zoom(hdl, after=True))
    s.step(fade(sr), wipe(a3, 'l', after=True)); s.step(wipe(a4, 'l'), fade(ct, after=True)); s.step(fade(p))
    s.note('Transporte reverso: la HDL (ApoA-I principal) recibe colesterol mediante ABCA1 (hacia ApoA-I pobre en lípidos) y '
           'ABCG1; la LCAT esterifica el colesterol en la HDL, permitiendo su maduración; el colesterol llega al hígado de forma '
           'selectiva mediante SR-BI o indirectamente por el intercambio CETP hacia lipoproteínas con ApoB. El número de '
           'partículas y la función de la HDL son dimensiones distintas del HDL-C plasmático.')


def t21f(D):
    s = new(D, U, '21 · Ácidos biliares: la vía de eliminación del colesterol')
    liver(s, 0.4, 1.2, 3.4, name='Hígado AB')
    c = chain(s, 4.2, 1.15, ['Colesterol', 'Ácidos biliares primarios (cólico, quenodesoxicólico)', 'Conjugados (glicina/taurina)'], dy=0.95, w=3.6,
              enzymes=['**CYP7A1** (7α-hidroxilasa)', 'conjugación'], rev=[False, False], fill=['F39C12', YEL, YEL], name='Ácidos biliares', h=0.55, size=13)
    intestine(s, 0.6, 4.2, 2.6, name='Intestino AB')
    eh = s.arrow([(3.1, 5.3), (4.6, 5.8), (2.4, 3.2)], TRN, 3.5, curve=True, name='Circulación enterohepática')
    s.text(3.6, 6.25, 3.2, 0.35, 'circulación enterohepática', 12.5, F_HEAD, TRN, True, 'c')
    fx = flow(s, ['FXR ileal', 'FGF19', 'FGFR4/β-Klotho hepático', '↓ CYP7A1'], 8.2, 1.15, 4.7, 3.0, [LBLUE, LBLUE, LBLUE, LSALMON], 13.5, 0.2, 'v', INH)
    k = card(s, 4.2, 4.2, 3.75, 2.9, '- La **microbiota** forma ácidos **secundarios**.\n- Reabsorción **mayoritaria** (enterohepática).\n- La excreción **fecal** es vía de eliminación **neta** de colesterol.', CREAM, 13.5)
    cl = card(s, 8.2, 4.35, 4.7, 2.75, '- **Estatinas**: ↓ HMGCR → ↓ colesterol del hepatocito → ↑ **LDLR** → ↓ LDL.\n- **Inhibidores de PCSK9**: ↑ receptores reciclados.\n- **Secuestrantes**: ↑ conversión de colesterol en ácidos biliares.', YEL, 13, head='Clínica')
    chain_anim(s, c, per_click=3)
    s.step(wipe(eh, 'l'), fade(k, after=True))
    flow_anim(s, fx)
    s.step(fade(cl))
    s.note('Ácidos biliares: el colesterol hepático se convierte en ácidos biliares primarios (cólico y quenodesoxicólico); la '
           'vía clásica comienza con CYP7A1 (colesterol 7α-hidroxilasa). La conjugación con glicina o taurina favorece la '
           'solubilidad y la función detergente; la microbiota transforma parte en ácidos secundarios, con circulación '
           'enterohepática mayoritaria. Retrocontrol: FXR ileal → FGF19 (en humanos) → receptor hepático FGFR4/β-Klotho, junto '
           'con FXR/SHP hepático, restringe CYP7A1. La excreción fecal es la vía de eliminación neta de colesterol. Clínica: '
           'estatinas, inhibidores de PCSK9 y secuestrantes de ácidos biliares. La aterosclerosis depende de la exposición '
           'acumulada a partículas aterogénicas con ApoB (Unidad V).')


# ------------------------------------------------------------------ Morph 4: cetogénesis
def m4txt(s, t, head):
    return card(s, 8.9, 1.1, 4.0, 4.0, t, CREAM, 15, name='!!Texto M4', head=head)


def m4a(D):
    s = new(D, U, '22 · Cetogénesis: el hígado en ayuno', 'SECUENCIA MORPH 4 · 1/4')
    liver(s, 0.6, 1.3, 7.6, name='!!Hígado M4')
    for i in range(3):
        ag_chain(s, 1.2 + i * 1.5, 2.3 + (i % 2) * 0.6, 1.2, 0.22, name='!!AG M4 %d' % i)
    m4txt(s, '- **Insulina baja relativa** y alta disponibilidad de **AG**.\n- ↓ malonil-CoA → **CPT1 libre**.\n- β-oxidación intensa → acetil-CoA, NADH y ATP.', 'Condiciones')
    s.note('Secuencia Morph 4 (cetogénesis): hígado → mitocondria → acetil-CoA → cetogénesis → cuerpos cetónicos → tejidos '
           'periféricos. Condiciones: baja acción insulínica relativa, elevada disponibilidad de AG, mayor entrada por CPT1 tras el '
           'descenso del malonil-CoA y β-oxidación intensa.')


def m4b(D):
    s = new(D, U, '22 · Cetogénesis en la mitocondria hepática', 'SECUENCIA MORPH 4 · 2/4', morph=True)
    liver(s, -8.0, -5.0, 26.0, name='!!Hígado M4')
    mito(s, 0.4, 1.2, 8.2, 5.8, name='!!Mitocondria M4')
    for i in range(3):
        ag_chain(s, 0.9 + i * 0.4, 1.5 + i * 0.25, 0.9, 0.18, name='!!AG M4 %d' % i)
    c = chain(s, 2.5, 1.9, ['2 Acetil-CoA', 'Acetoacetil-CoA', 'HMG-CoA', 'Acetoacetato'], dy=1.0, w=2.4, enzymes=['tiolasa', '**HMGCS2** (paso regulado)', 'HMG-CoA **liasa**'],
              rev=[True, False, False], fill=[ENE, YEL, YEL, lighten(MOL['cc'][0], 0.55)], name='Cetogénesis', h=0.5, size=14)
    bhb = s.shape(5.6, 4.9, 2.4, 0.5, 'roundRect', lighten(MOL['cc'][0], 0.55), (INK, 1.0), False, 'β-hidroxibutirato', 14, F_HEAD, INK, True, 'c', 'm', name='BHB')
    a = s.arrow([(4.92, 5.15), (5.58, 5.15)], INK, 2.5, head='triangle')
    bd = enz(s, 4.6, 5.55, 'BDH (NADH ↔ NAD^{+})', name='BDH')
    ac = chip(s, 3.2, 5.9, 'Acetona (descarboxilación espontánea)', LSALMON, 12, name='Acetona')
    oaa = card(s, 0.6, 3.3, 1.8, 1.5, 'OAA desviado a **GNG**', MINT, 12.5, name='OAA', grow=False)
    m4txt(s, '- Parte del **oxaloacetato** va a gluconeogénesis: el acetil-CoA no se condensa todo en Krebs.\n- **HMGCS2** mitocondrial (PPARα, ayuno) dirige el exceso a **cuerpos cetónicos**.', 'Mitocondria')
    s.step(fade(oaa))
    chain_anim(s, c, per_click=1)
    s.step(wipe(a, 'l'), fade(bhb, after=True), fade(bd)); s.step(fade(ac))
    s.note('Morph: el hígado se amplía hasta mostrar la mitocondria. Acetil-CoA → acetoacetil-CoA (tiolasa) → HMG-CoA '
           '(HMG-CoA sintasa 2 mitocondrial, paso regulado: su expresión aumenta en ayuno vía PPARα) → acetoacetato (HMG-CoA '
           'liasa). La β-hidroxibutirato deshidrogenasa interconvierte acetoacetato y β-hidroxibutirato según la relación '
           'NADH/NAD+ (alta en ayuno, por eso predomina el β-hidroxibutirato); la acetona deriva de la descarboxilación del '
           'acetoacetato. Parte del oxaloacetato se desvía a gluconeogénesis, lo que limita la condensación del acetil-CoA en el '
           'ciclo de Krebs.')


def m4c(D):
    s = new(D, U, '22 · Cuerpos cetónicos hacia los tejidos periféricos', 'SECUENCIA MORPH 4 · 3/4', morph=True)
    mito(s, 0.3, 1.2, 2.4, 1.6, name='!!Mitocondria M4')
    liver(s, 0.3, 2.9, 2.6, name='Hígado pequeño')
    vessel(s, 0.3, 4.75, 8.4, 0.75, name='!!Vaso M4', rbcs=4)
    ccs = [mol(s, 2.7 + i * 0.4, 4.9, 'cc', d=0.42, name='CC viajero %d' % i) for i in range(4)]
    org = [('heart', 'Corazón', 3.4, 1.2), ('muscle', 'Músculo', 5.2, 1.3), ('kidney', 'Riñón', 3.6, 5.8), ('brain', 'Cerebro', 6.0, 5.6)]
    ids = []
    for k, t, x, y in org:
        g = s.group_start('Destino ' + t)
        organ_icon(s, k, x, y, 1.1)
        s.text(x + 1.15, y + 0.35, 1.4, 0.4, t, 14, F_HEAD, INK, True, 'l', 'm')
        s.group_end(); ids.append(g)
    nl = card(s, 0.3, 5.75, 3.0, 1.35, '**Hígado**: produce pero **no usa** cetonas (sin SCOT). **Eritrocito**: sin mitocondrias.', LSALMON, 12.5, name='No usan', grow=False)
    m4txt(s, '- **Hidrosolubles**: viajan sin transportador plasmático.\n- Entran a corazón, riñón, músculo y cerebro por **MCT**.\n- Exportan el poder energético de los AG a órganos que no usan AG largos de forma significativa.', 'Exportación')
    pts = [[(1.5, -2.6), (1.7, -3.3)], [(3.0, -2.5), (3.0, -3.1)], [(1.4, 0.6), (1.4, 0.9)], [(3.5, 0.5), (3.6, 0.8)]]
    for i, (g, (k, t, x, y)) in enumerate(zip(ids, org)):
        s.step(fade(g), path(ccs[i], x + 0.4 - (2.7 + i * 0.4), (y + 0.4) - 4.9, dur=1500, after=True))
    s.step(fade(nl))
    s.note('Morph: la mitocondria se reduce y aparece la circulación. Los cuerpos cetónicos son hidrosolubles y llegan por la '
           'sangre a corazón, riñón, músculo y cerebro (transportadores MCT). Cada clic envía una ficha de cuerpo cetónico a un '
           'órgano consumidor. El hígado carece de SCOT funcional y por ello produce pero no usa cetonas; el eritrocito carece de '
           'mitocondrias y tampoco puede utilizarlas.')


def m4d(D):
    s = new(D, U, '22 · Cetólisis extrahepática', 'SECUENCIA MORPH 4 · 4/4', morph=True)
    mito(s, 0.4, 1.2, 8.2, 5.8, name='!!Mitocondria M4')
    c = chain(s, 2.4, 1.9, ['β-hidroxibutirato', 'Acetoacetato', 'Acetoacetil-CoA', '2 Acetil-CoA → Krebs'], dy=1.05, w=2.6,
              enzymes=['BDH (→ NADH)', '**SCOT/OXCT1**', 'tiolasa'], rev=[True, False, True], fill=[lighten(MOL['cc'][0], 0.55), lighten(MOL['cc'][0], 0.55), YEL, ENE], name='Cetólisis', h=0.5, size=14)
    sc = chip(s, 5.2, 3.55, 'succinil-CoA → succinato', ENE, 12, name='Succinil')
    m4txt(s, '- **SCOT** transfiere el CoA desde **succinil-CoA** al acetoacetato.\n- El **hígado carece de SCOT** funcional.\n- Error frecuente: «el hígado quema sus propias cetonas».', 'Tejidos periféricos')
    chain_anim(s, c, per_click=1)
    s.anim[2].append(fade(sc, after=True))
    s.note('Cetólisis en tejidos extrahepáticos: β-hidroxibutirato → acetoacetato (BDH, genera NADH) → acetoacetil-CoA por la '
           'succinil-CoA:3-cetoácido CoA transferasa (SCOT/OXCT1), que transfiere el CoA desde el succinil-CoA → 2 acetil-CoA por '
           'tiolasa → ciclo de Krebs. El hígado carece de SCOT funcional.')


def t22e(D):
    s = new(D, U, '22 · Cetogénesis: objetivos y precisiones')
    ob = [('Exportar energía', 'de los AG hepáticos a órganos que no usan AG largos de forma significativa (cerebro)', MINT),
          ('Preservar glucosa', 'menor consumo de glucosa periférica y cerebral', LBLUE),
          ('Ahorrar proteína', 'menor necesidad de proteólisis para gluconeogénesis prolongada', YEL)]
    ids = []
    for i, (t, d, f) in enumerate(ob):
        ids.append(card(s, 0.4 + i * 4.2, 1.1, 4.0, 2.2, '**%s**: %s' % (t, d), f, 15, anchor='m', name='Objetivo %d' % i))
    p = note_box(s, 0.4, 3.55, 12.5, 1.3, 'La cetogénesis **no convierte** los carbonos de AG pares en **glucosa neta**: provee combustible alternativo y la **energía** para fabricar glucosa desde **otros sustratos**.', 15)
    cl = card(s, 0.4, 5.05, 12.5, 2.05, '- **Cetosis fisiológica** del ayuno: pH conservado.\n- **Cetoacidosis diabética**: producción que **excede** utilización, depuración y capacidad tampón → acidosis, deshidratación, alteraciones electrolíticas.\n- Medir **β-hidroxibutirato** en sangre interpreta mejor que las tiras urinarias de acetoacetato.', CREAM, 14, head='Clínica')
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p)); s.step(fade(cl))
    s.note('Objetivos de la cetogénesis: exportar poder energético de los AG hepáticos a órganos que no pueden usar AG largos de '
           'manera significativa, preservar glucosa y reducir la necesidad de proteólisis para la gluconeogénesis prolongada. La '
           'cetogénesis no convierte los carbonos de AG pares en glucosa neta (el acetil-CoA no puede formar glucosa neta porque '
           'sus dos carbonos se pierden como CO2 en el ciclo de Krebs). Clínica: cetosis fisiológica frente a cetoacidosis; '
           'medición de β-hidroxibutirato.')


# ------------------------------------------------------------------ TEMA 23
def t23a(D):
    s = new(D, U, '23 · Tres escalas de control metabólico')
    sc = [('1', 'ALOSTÉRICO', 'segundos', 'Citrato → PFK-1; acetil-CoA → PC; malonil-CoA → CPT1; AMP → fosforilasa b', '58D68D'),
          ('2', 'COVALENTE', 'segundos–minutos', 'PKA, Akt, AMPK: fosforilación/desfosforilación de ACC, GS, fosforilasa, PFK-2', 'F5B041'),
          ('3', 'TRANSCRIPCIONAL', 'horas–días', 'CREB, FOXO1, ChREBP, SREBP-1c, SREBP-2, GR, PPARα: cambian la **cantidad** de enzima', '5DADE2')]
    ids = []
    for i, (n, t, tm, d, col) in enumerate(sc):
        y = 1.15 + i * 1.75
        g = s.group_start('Escala ' + t)
        s.shape(0.4, y, 12.5, 1.55, 'rect', lighten(col, 0.6), (INK, 1.25), SHD)
        badge(s, 0.6, y + 0.45, n, 0.6)
        s.text(1.4, y + 0.1, 3.4, 0.6, t, 20, F_HEAD, INK, True, 'l', 'm')
        chip(s, 1.4, y + 0.85, tm, 'FFFFFF', 13, h=0.45, line=(INK, 1.0))
        s.text(4.8, y + 0.1, 7.9, 1.35, d, 15, F_BODY, INK, False, 'l', 'm')
        s.group_end(); ids.append(g)
    p = note_box(s, 0.4, 6.4, 12.5, 0.75, 'Los factores de transcripción modulan **capacidad** enzimática, pero **no determinan solos el flujo**.', 15)
    for g in ids:
        s.step(fade(g))
    s.step(fade(p))
    s.note('Distinguir escalas: (1) control alostérico inmediato; (2) fosforilación/desfosforilación; (3) cambios de '
           'transcripción y abundancia proteica. Los factores de transcripción modulan la capacidad enzimática pero no determinan '
           'por sí solos el flujo, que también depende de sustratos, compartimentos, hormonas y energía. Esta es la distinción '
           '"regulación alostérica frente a fosforilación y regulación génica".')


def nuc_scene(s, ttl_nucleus='NÚCLEO DEL HEPATOCITO'):
    s.shape(0.3, 1.05, 8.4, 6.05, 'roundRect', ('a', 'F5CBA7', 60), ('A04000', 2.0), False, name='Hepatocito', adj={'adj': 6000})
    s.shape(3.6, 3.3, 4.8, 3.6, 'ellipse', ('a', 'BB8FCE', 75), ('4A235A', 2.5), False, name='Núcleo')
    s.text(4.3, 3.45, 3.4, 0.35, ttl_nucleus, 12.5, F_HEAD, '4A235A', True, 'c')
    dna = s.free(4.1, 5.6, 3.8, 0.6, [('M 0 500 C 125 0 250 0 375 500 C 500 1000 625 1000 750 500 C 875 0 1000 0 1000 500', False, True),
                                      ('M 0 500 C 125 1000 250 1000 375 500 C 500 0 625 0 750 500 C 875 1000 1000 1000 1000 500', False, True)], None, ('4A235A', 2.0), name='ADN')


def t23b(D):
    s = new(D, U, '23 · Ayuno: CREB y FOXO1 inducen la gluconeogénesis')
    nuc_scene(s)
    gcg = mol(s, 0.5, 1.2, 'gcg', d=0.5, name='Glucagón')
    pka = enz(s, 0.6, 2.0, 'GCGR → AMPc → PKA', name='PKA')
    creb = s.shape(4.5, 4.0, 1.4, 0.55, 'roundRect', shade('F5B041', 0.35, 0.2), (INK, 1.25), SHD, 'CREB-P', 13, F_HEAD, INK, True, 'c', 'm', name='CREB')
    crtc = chip(s, 4.6, 4.65, 'CRTC2', LBLUE, 12, name='CRTC2')
    fox = s.shape(6.2, 4.0, 1.4, 0.55, 'roundRect', shade('EC7063', 0.35, 0.2), (INK, 1.25), SHD, 'FOXO1', 13, F_HEAD, INK, True, 'c', 'm', name='FOXO1')
    gr = s.shape(6.4, 4.75, 1.3, 0.5, 'roundRect', shade('A569BD', 0.35, 0.2), (INK, 1.25), SHD, 'GR', 13, F_HEAD, WHITE, True, 'c', 'm', name='GR')
    gn = chip(s, 4.4, 6.25, '↑ PCK1 (PEPCK) · ↑ G6PC (G6Pasa)', MINT, 13, name='Genes GNG')
    a1 = s.arrow([(1.5, 2.35), (4.6, 4.0)], ACT, 2.5)
    akt = enz(s, 0.6, 5.2, 'Insulina → Akt', name='Akt')
    ex = s.arrow([(7.0, 3.95), (8.0, 2.4)], INH, 2.5, dash='dash', name='Exclusión nuclear')
    k1 = card(s, 8.95, 1.1, 3.95, 2.55, '**CREB**: glucagón → PKA → fosforilación en **Ser133**; **CRTC2** se incorpora → ↑ PCK1 y G6PC.', CREAM, 13.5, head='CREB')
    k2 = card(s, 8.95, 3.8, 3.95, 3.3, '**FOXO1**: con poca insulina permanece **nuclear**. En saciedad, **Akt** lo fosforila → **exclusión nuclear** → reprime el programa gluconeogénico (no de forma instantánea ni total).', LSALMON, 13.5, head='FOXO1')
    s.step(fade(gcg), fade(pka, after=True), wipe(a1, 'l', after=True), fade(creb, after=True), fade(crtc, after=True), fade(k1))
    s.step(fade(fox), fade(gr), fade(gn, after=True))
    s.step(fade(akt), fade(k2, after=True), path(fox, 1.0, -1.7, after=True, dur=1300), wipe(ex, 'b'))
    s.note('CREB (ayuno): glucagón → GCGR–AMPc–PKA → fosforilación de CREB en Ser133; el coactivador CRTC2 se incorpora al '
           'programa gluconeogénico → ↑ PCK1 (PEPCK citosólica) y G6PC (glucosa-6-fosfatasa). La insulina y la realimentación '
           'limitan esta señal; los glucocorticoides pueden cooperar (GR). FOXO1 (ayuno): cuando Akt cae por baja insulina, FOXO1 '
           'permanece nuclear y promueve PCK1/G6PC. En saciedad, receptor de insulina → PI3K → Akt fosforila FOXO1 y promueve su '
           'exclusión nuclear (la animación lo desplaza fuera del núcleo). No equivale a una supresión instantánea total de la '
           'gluconeogénesis.')


def t23c(D):
    s = new(D, U, '23 · Abundancia: ChREBP y SREBP-1c inducen la lipogénesis')
    nuc_scene(s)
    glc = mol(s, 0.5, 1.2, 'glc', d=0.5, name='Glucosa'); fru = mol(s, 1.1, 1.2, 'fru', d=0.5, name='Fructosa')
    met = chip(s, 0.5, 1.9, 'Metabolitos glucídicos', YEL, 12.5, name='Metabolitos')
    ch = s.shape(4.4, 4.0, 1.8, 0.55, 'roundRect', shade('58D68D', 0.35, 0.2), (INK, 1.25), SHD, 'ChREBP/MLX', 13, F_HEAD, INK, True, 'c', 'm', name='ChREBP')
    ins = mol(s, 0.5, 4.3, 'ins', d=0.5, name='Insulina')
    mt = enz(s, 1.1, 4.35, 'Akt · mTORC1', name='mTORC1')
    sr = s.shape(6.3, 4.8, 1.8, 0.55, 'roundRect', shade('F5B041', 0.35, 0.2), (INK, 1.25), SHD, 'SREBP-1c', 13, F_HEAD, INK, True, 'c', 'm', name='SREBP1c')
    gn = chip(s, 4.1, 6.25, '↑ ACC (ACACA) · ↑ FASN · ↑ SCD1 · glucólisis', MINT, 12.5, name='Genes lipogénicos')
    a1 = s.arrow([(1.5, 2.25), (4.8, 4.0)], ACT, 2.5); a2 = s.arrow([(2.6, 4.55), (6.28, 5.05)], ACT, 2.5)
    k1 = card(s, 8.95, 1.1, 3.95, 2.6, '**ChREBP**: productos del metabolismo glucídico favorecen su activación y localización nuclear. Glucosa y fructosa activan programas lipogénicos por vías **parcialmente distintas**.', CREAM, 13, head='ChREBP')
    k2 = card(s, 8.95, 3.85, 3.95, 3.25, '**SREBP-1c**: insulina y mTORC1 favorecen su procesamiento/expresión. Es **lipogénico**, no el regulador principal del **LDLR**. La ruta DAG → TAG (**DGAT**) responde a control **multigénico**.', LSALMON, 13, head='SREBP-1c')
    s.step(fade(glc), fade(fru), fade(met, after=True), wipe(a1, 'l', after=True), fade(ch, after=True), fade(k1))
    s.step(fade(ins), fade(mt, after=True), wipe(a2, 'l', after=True), fade(sr, after=True), fade(k2))
    s.step(fade(gn))
    s.note('ChREBP (abundancia de carbohidratos): productos del metabolismo glucídico favorecen la activación y localización '
           'nuclear de ChREBP/MLX, que induce ACC (ACACA), FASN y otros genes de glucólisis y lipogénesis, en interacción con el '
           'estado hormonal; glucosa y fructosa pueden activar programas lipogénicos por vías parcialmente distintas; la '
           'regulación exacta involucra múltiples metabolitos y modificaciones. SREBP-1c (insulina y nutrientes): insulina y '
           'mTORC1 favorecen su procesamiento y expresión; induce ACC, FASN, SCD1 y otros genes de AG. La ruta DAG → TAG (DGAT1/2) '
           'responde a control transcripcional multigénico (SREBP-1c, ChREBP y PPAR según tejido). SREBP-1c es lipogénico, no el '
           'principal regulador del LDLR.')


def t23d(D):
    s = new(D, U, '23 · SREBP-2, receptor glucocorticoide y mapa de genes')
    k1 = card(s, 0.4, 1.1, 6.1, 2.35, '**SREBP-2** (esterol intracelular bajo): ↑ **HMGCR** y **LDLR** (también PCSK9). Un hepatocito con poco colesterol **aumenta a la vez síntesis y captación**. Las estatinas provocan compensación de SREBP-2 pero inhiben la enzima: resultado neto **↑ depuración de LDL**.', LBLUE, 13.5, head='SREBP-2')
    k2 = card(s, 0.4, 3.6, 6.1, 2.15, '**GR**: el cortisol activa un receptor intracelular que se transloca al núcleo (GRE); coopera con CREB/FOXO1 → ↑ **PCK1, G6PC** y disponibilidad de **aminoácidos**. Exceso crónico: hiperglucemia, resistencia insulínica, proteólisis.', LILAC, 13.5, head='Receptor glucocorticoide')
    rows = [['Gen', 'Factor predominante', 'Estado'],
            ['**ACC (ACACA), FASN**', 'ChREBP · SREBP-1c', 'Alimentado'],
            ['**DGAT1/2**', 'rutas lipogénicas + otros (no exclusivo)', 'Alimentado'],
            ['**PCK1 (PEPCK), G6PC**', 'CREB + FOXO1 + GR', 'Ayuno / estrés'],
            ['**LDLR, HMGCR**', 'SREBP-2', 'Colesterol intracelular bajo'],
            ['**HMGCS2**, genes de β-oxidación', 'PPARα', 'Ayuno']]
    t, H = table(s, 6.8, 1.15, 6.1, rows, [2.2, 2.3, 1.6], size=13, rowh=0.55, name='Mapa de genes')
    ex = note_box(s, 0.4, 5.95, 12.5, 1.15, '«Insulina ↑ Akt, expulsa FOXO1 y ↓ PEPCK/G6Pasa; glucosa → ChREBP e insulina → SREBP-1c (↑ ACC/FASN); si baja el colesterol, SREBP-2 ↑ HMGCR y LDLR».', 14)
    s.step(fade(k1)); s.step(fade(k2)); s.step(fade(t)); s.step(fade(ex))
    s.note('SREBP-2 (esterol intracelular bajo): SCAP/SREBP-2 se procesa → ↑ HMGCR y LDLR (también PCSK9); colesterol y '
           'oxiesteroles inhiben el procesamiento vía Insig/SCAP. Receptor glucocorticoide: coopera con CREB/FOXO1 para inducir '
           'PCK1 y G6PC y favorecer la disponibilidad de sustratos aminoacídicos; los efectos dependen del tejido y la duración. '
           'Mapa de genes: las asociaciones son predominantes, no exhaustivas. El recuadro rojo resume la frase de examen oral.')


# ------------------------------------------------------------------ TEMA 24
def t24a(D):
    s = new(D, U, '24 · Estrés fisiológico: dos ejes y distintos tiempos')
    brain(s, 0.4, 1.1, 2.2, name='Cerebro estrés')
    ax1 = flow(s, ['Simpático', 'Médula suprarrenal', 'Adrenalina / noradrenalina'], 3.0, 1.15, 6.0, 0.9, [LSALMON, LSALMON, RED], 13.5, 0.3, 'h', INK)
    t1 = chip(s, 9.3, 1.35, 'SEGUNDOS', TAG, 14, name='Tiempo 1')
    ax2 = flow(s, ['CRH', 'ACTH', 'Cortisol'], 3.0, 2.55, 6.0, 0.9, [LBLUE, LBLUE, TRN], 13.5, 0.3, 'h', INK)
    t2 = chip(s, 9.3, 2.75, 'MINUTOS–HORAS', TAG, 14, name='Tiempo 2')
    ot = card(s, 0.4, 3.85, 6.1, 1.6, 'Además: **citocinas** inflamatorias, **glucagón** y **GH** según el estímulo.', CREAM, 14)
    ob = card(s, 6.8, 3.85, 6.1, 1.6, '**Objetivo**: garantizar combustible y **perfusión** a cerebro, corazón y músculo durante la amenaza.', MINT, 14)
    p = note_box(s, 0.4, 5.65, 12.5, 1.45, 'No confundir el **estrés agudo adaptativo** con el **estrés crónico**, que puede producir resistencia a la insulina, pérdida muscular, hígado graso y disfunción metabólica.', 14.5)
    flow_anim(s, ax1); s.anim[-1].append(fade(t1))
    flow_anim(s, ax2); s.anim[-1].append(fade(t2))
    s.step(fade(ot)); s.step(fade(ob)); s.step(fade(p))
    s.note('El estrés agudo activa el eje simpático–médula suprarrenal (adrenalina/noradrenalina en segundos) y el eje '
           'CRH → ACTH → cortisol (minutos a horas), con citocinas inflamatorias, glucagón y GH según el estímulo. Objetivo: '
           'garantizar combustible y perfusión a cerebro, corazón y músculo. No confundir estrés agudo adaptativo con estrés '
           'crónico.')


def t24b(D):
    s = new(D, U, '24 · Estrés: respuesta multiorgánica')
    data = [('liver', 'HÍGADO', '- Catecolaminas y glucagón: **glucogenólisis**\n- Cortisol: ↑ capacidad de **GNG**\n- Sustratos: lactato, alanina, glicerol', MINT),
            ('muscle', 'MÚSCULO', '- Adrenalina y Ca^{2+}: glucogenólisis\n- Cortisol sostenido: **proteólisis** → alanina y glutamina', LSALMON),
            ('heart', 'MIOCARDIO', '- ↑ trabajo y consumo de O_{2}\n- Oxida AG/lactato/glucosa\n- ↑ cronotropismo e inotropismo', PINK),
            ('adipose', 'ADIPOSO', '- **Lipólisis** β-adrenérgica (AMPc–PKA), modulada por α_{2}\n- La insulina contrarregula', YEL),
            ('brain', 'SNC', '- Mantener **glucosa** cerebral y alerta\n- Exceso crónico de cortisol: sueño, apetito', LILAC),
            ('adrenal', 'SUPRARRENAL', '- Corteza: cortisol desde **colesterol** (StAR)\n- Médula: catecolaminas desde **tirosina**\n- El cortisol induce **PNMT** → adrenalina', LBLUE)]
    ids = organ_tiles(s, data, cols=3, tw=4.1, th=2.9)
    for g in ids:
        s.step(fade(g))
    s.note('Hígado: catecolaminas y glucagón facilitan la glucogenólisis; el cortisol aumenta la capacidad de gluconeogénesis; '
           'lactato, alanina y glicerol aportan sustratos. Músculo: adrenalina y Ca2+ activan la glucogenólisis; el cortisol '
           'sostenido promueve proteólisis y exportación de alanina/glutamina. Miocardio: aumenta trabajo, consumo de O2 y '
           'oxidación de AG/lactato/glucosa; las catecolaminas incrementan cronotropismo e inotropismo. Adiposo: lipólisis '
           'β-adrenérgica (AMPc–PKA) modulada por receptores α2; la insulina contrarregula. SNC: mantener el aporte de glucosa, '
           'actividad autonómica y alerta. Suprarrenal: la corteza produce cortisol desde colesterol (StAR facilita la entrada '
           'mitocondrial); la médula libera catecolaminas derivadas de tirosina; el cortisol cortical induce PNMT en la médula.')


def t24c(D):
    s = new(D, U, '24 · Sepsis, trauma y quemaduras')
    seq = flow(s, ['Inflamación · cortisol · catecolaminas', 'Hiperglucemia de estrés', 'Proteólisis y resistencia a la insulina', 'Balance nitrogenado negativo'],
               0.4, 1.2, 12.5, 1.4, [LSALMON, YEL, PINK, RED], 14.5, 0.35, 'h', INH)
    k = card(s, 0.4, 3.0, 6.1, 2.4, 'La **glucemia** no revela necesariamente la disponibilidad energética **intracelular**, la **perfusión** ni la **función mitocondrial**.', CREAM, 15, head='Precisión')
    k2 = card(s, 6.8, 3.0, 6.1, 2.4, 'La sepsis tiene **heterogeneidad metabólica** y requiere interpretación clínica específica.', LBLUE, 15, head='Clínica')
    p = note_box(s, 0.4, 5.6, 12.5, 1.5, 'Glucemia ≠ flujo metabólico de glucosa: una cifra plasmática no informa por sí sola cuánta glucosa se produce, se capta o se oxida.', 15)
    flow_anim(s, seq)
    s.step(fade(k)); s.step(fade(k2)); s.step(fade(p))
    s.note('En sepsis, trauma y quemaduras, inflamación, cortisol y catecolaminas producen hiperglucemia de estrés, proteólisis, '
           'resistencia a la insulina y balance nitrogenado negativo. La glucemia no necesariamente revela la disponibilidad '
           'energética intracelular, la perfusión ni la función mitocondrial. La sepsis tiene heterogeneidad metabólica y requiere '
           'interpretación clínica específica.')


def build(D):
    t18a(D); t18b(D)
    t19a(D); t19b(D); t19c(D)
    t20a(D); t20b(D)
    t21a(D); t21b(D); t21c(D); t21d(D); t21e(D); t21f(D)
    m4a(D); m4b(D); m4c(D); m4d(D); t22e(D)
    t23a(D); t23b(D); t23c(D); t23d(D)
    t24a(D); t24b(D); t24c(D)
