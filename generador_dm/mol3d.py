# -*- coding: utf-8 -*-
"""Modelos moleculares de esferas y varillas generados con RDKit (geometría 3D real, ETKDG + MMFF)
y dibujados como formas nativas editables (esferas con degradado radial + enlaces)."""
import math, functools
from lib import *

SMILES = {
    'glucosa': 'OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O',          # β-D-glucopiranosa
    'piruvato': 'CC(=O)C(=O)[O-]',
    'lactato': 'C[C@H](O)C(=O)[O-]',                                   # L-lactato
    'glicerol': 'OCC(O)CO',
    'acetoacetato': 'CC(=O)CC(=O)[O-]',
    'bhb': 'C[C@@H](O)CC(=O)[O-]',                                     # D-β-hidroxibutirato
    'acetona': 'CC(C)=O',
    'palmitato': 'CCCCCCCCCCCCCCCC(=O)[O-]',
    'acetil': 'CC(=O)S',                                               # grupo acetilo unido al S de la CoA
    'tag': 'CCCCCCCCCCCC(=O)OCC(OC(=O)CCCCCCCCCCC)COC(=O)CCCCCCCCCCC',  # TAG (laurato x3) representativo
    'atp': 'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)([O-])OP(=O)([O-])OP(=O)([O-])[O-])[C@@H](O)[C@H]1O',
    'adp': 'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)([O-])OP(=O)([O-])[O-])[C@@H](O)[C@H]1O',
    'urea': 'NC(N)=O',
    'malonilo': 'OC(=O)CC(=O)S',
    'g6p': 'OC1O[C@H](COP(=O)([O-])[O-])[C@@H](O)[C@H](O)[C@H]1O',
    'co2': 'O=C=O',
    'h2o': 'O',
    'bicarbonato': 'OC(=O)[O-]',
}
CPK = {'C': '3A3A3A', 'O': 'E0261B', 'N': '2B5BD7', 'H': 'F4F4F4', 'P': 'F39C12', 'S': 'F4D03F'}
RAD = {'C': 0.70, 'O': 0.66, 'N': 0.66, 'H': 0.42, 'P': 0.85, 'S': 0.85}


@functools.lru_cache(None)
def coords(key, hs=True, seed=7):
    from rdkit import Chem
    from rdkit.Chem import AllChem
    m = Chem.AddHs(Chem.MolFromSmiles(SMILES[key]))
    cids = list(AllChem.EmbedMultipleConfs(m, numConfs=24 if m.GetNumHeavyAtoms() > 12 else 1, randomSeed=seed))
    if not cids:
        cids = list(AllChem.EmbedMultipleConfs(m, numConfs=8, randomSeed=seed, useRandomCoords=True))
    try:
        AllChem.MMFFOptimizeMoleculeConfs(m)
    except Exception:
        pass
    import numpy as np
    def span(cid):
        P = m.GetConformer(cid).GetPositions()
        return float(np.sum((P - P.mean(0)) ** 2))
    conf = m.GetConformer(max(cids, key=span))
    atoms = []
    keep = {}
    for a in m.GetAtoms():
        if a.GetSymbol() == 'H' and not hs:
            continue
        p = conf.GetAtomPosition(a.GetIdx())
        keep[a.GetIdx()] = len(atoms)
        atoms.append((a.GetSymbol(), p.x, p.y, p.z))
    bonds = []
    for b in m.GetBonds():
        i, j = b.GetBeginAtomIdx(), b.GetEndAtomIdx()
        if i in keep and j in keep:
            bonds.append((keep[i], keep[j], b.GetBondTypeAsDouble()))
    # orientar: ejes principales (mayor extensión en x)
    import numpy as np
    X = np.array([[a[1], a[2], a[3]] for a in atoms])
    X -= X.mean(0)
    u, sv, vt = np.linalg.svd(X, full_matrices=False)
    X = X @ vt.T
    return [(atoms[k][0], *X[k]) for k in range(len(atoms))], bonds


def _rot(p, ax, ay, az):
    x, y, z = p
    ca, sa = math.cos(ax), math.sin(ax)
    y, z = y * ca - z * sa, y * sa + z * ca
    cb, sb = math.cos(ay), math.sin(ay)
    x, z = x * cb + z * sb, -x * sb + z * cb
    cc, scn = math.cos(az), math.sin(az)
    x, y = x * cc - y * scn, x * scn + y * cc
    return x, y, z


def model(s, key, x, y, w, h=None, hs=True, tilt=(0.45, 0.35, 0.0), name=None, bond_col='9A9A9A', atom_scale=1.0, label=None,
          lsize=13, lcolor=INK, seed=7):
    """dibuja un modelo de esferas y varillas dentro de la caja (x,y,w[,h]); devuelve id de grupo"""
    atoms, bonds = coords(key, hs, seed)
    P = [(_rot((a[1], a[2], a[3]), *tilt), a[0]) for a in atoms]
    xs = [p[0][0] for p in P]; ys = [p[0][1] for p in P]; zs = [p[0][2] for p in P]
    spanx = max(xs) - min(xs) + 1.6; spany = max(ys) - min(ys) + 1.6
    h = h or w * spany / spanx
    k = min(w / spanx, h / spany)
    cx = x + w / 2; cy = y + h / 2
    mx = (max(xs) + min(xs)) / 2; my = (max(ys) + min(ys)) / 2
    zmin, zmax = min(zs), max(zs)
    def proj(p):
        px, py, pz = p
        f = 1.0 + 0.12 * ((pz - zmin) / ((zmax - zmin) or 1) - 0.5)
        return cx + (px - mx) * k, cy - (py - my) * k, f
    g = s.group_start(name or ('Modelo 3D ' + key))
    items = []
    for i, j, order in bonds:
        a, b = proj(P[i][0]), proj(P[j][0])
        zb = (P[i][0][2] + P[j][0][2]) / 2
        items.append((zb - 0.01, 'b', (a, b, order)))
    for (p, el) in P:
        items.append((p[2], 'a', (proj(p), el)))
    items.sort(key=lambda t: t[0])
    for z, kind, data in items:
        if kind == 'b':
            (x1, y1, _), (x2, y2, _), order = data
            wpt = max(1.5, k * 9) * (1.0 if order < 1.6 else 0.8)
            if order >= 1.6:
                dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1
                ox, oy = -dy / L * k * 0.09, dx / L * k * 0.09
                s.arrow([(x1 + ox, y1 + oy), (x2 + ox, y2 + oy)], bond_col, wpt, tail=None)
                s.arrow([(x1 - ox, y1 - oy), (x2 - ox, y2 - oy)], bond_col, wpt, tail=None)
            else:
                s.arrow([(x1, y1), (x2, y2)], bond_col, wpt, tail=None)
        else:
            (px, py, f), el = data
            r = RAD.get(el, 0.7) * k * 0.62 * f * atom_scale
            c = CPK.get(el, 'AAAAAA')
            s.shape(px - r, py - r, 2 * r, 2 * r, 'ellipse',
                    ('rad', [(0, 'FFFFFF'), (28, c if el != 'H' else 'FFFFFF'), (100, _dk(c, 0.55 if el != 'H' else 0.35))], (30, 25)),
                    None, False, name='Átomo %s' % el)
    if label:
        s.text(x - 0.3, y + h + 0.02, w + 0.6, 0.34, label, lsize, F_HEAD, lcolor, True, 'c', 't', minsize=9)
    return s.group_end()


def _dk(c, f):
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    return '%02X%02X%02X' % tuple(int(v * (1 - f)) for v in (r, g, b))


def sphere(s, x, y, d, color, name=None, text=None, size=11, tcolor=WHITE):
    return s.shape(x, y, d, d, 'ellipse', ('rad', [(0, 'FFFFFF'), (30, color), (100, _dk(color, 0.5))], (30, 25)), None, False,
                   text, size, F_HEAD, tcolor, True, 'c', 'm', (0, 0, 0, 0), fit=False, name=name or 'Esfera')


def acetyl_coa(s, x, y, w, name='Modelo acetil-CoA', label='Acetil-CoA'):
    """acetilo en esferas (real) unido por tioéster a la coenzima A esquematizada"""
    g = s.group_start(name)
    model(s, 'acetil', x, y, w * 0.45, hs=True, tilt=(0.3, 0.2, 0.2), name='Grupo acetilo')
    hh = w * 0.3
    s.shape(x + w * 0.47, y + hh * 0.35, w * 0.53, hh * 0.75, 'roundRect', ('lin', [(0, 'F9E79F'), (100, 'D4AC0D')], 90),
            (INK, 1.25), False, 'CoA', 15, F_HEAD, INK, True, 'c', 'm', (0, 0, 0, 0), adj={'adj': 40000}, name='Coenzima A')
    if label:
        s.text(x - 0.2, y + hh * 1.25, w + 0.4, 0.32, label, 12.5, F_HEAD, INK, True, 'c', 't')
    return s.group_end()


def insulin_model(s, x, y, w, name='Modelo insulina', labels=True):
    """insulina humana: cadena A (21 aa) y B (30 aa) como collares de esferas; 2 puentes disulfuro intercatenarios (A7–B7, A20–B19)
    y 1 intracatenario (A6–A11)"""
    g = s.group_start(name)
    k = w / 10.0
    A = [(1.0, 1.2), (1.35, 1.45), (1.7, 1.7), (2.0, 2.0), (2.25, 2.35), (2.7, 2.35), (2.45, 2.95), (2.95, 3.0), (3.35, 2.8),
         (3.55, 2.4), (3.15, 2.1), (3.5, 1.75), (3.9, 1.55), (4.3, 1.7), (4.65, 1.95), (4.95, 2.25), (5.25, 2.5), (5.5, 2.8),
         (5.8, 2.65), (6.1, 3.0), (6.5, 2.85)]
    B = [(0.6 + i * 0.31, 4.0 + (0.16 * math.sin(i * 1.75) if 8 <= i <= 18 else 0.0)) for i in range(30)]
    def P(p):
        return x + p[0] * k, y + p[1] * k
    d = 0.48 * k
    for chain in (A, B):
        s.arrow([P(p) for p in chain], '7F8C8D', max(1.5, 4 * k), tail=None)
    ss = [(A[5], A[10]), (A[6], B[6]), (A[19], B[18])]
    for a, b in ss:
        s.arrow([P(a), P(b)], 'D4AC0D', max(2.5, 7 * k), tail=None, dash='sysDash')
    for i, p in enumerate(A):
        cx, cy = P(p)
        cys = i in (5, 6, 10, 19)
        sphere(s, cx - d / 2, cy - d / 2, d, 'F4D03F' if cys else 'E74C3C', name='Residuo A%d' % (i + 1))
    for i, p in enumerate(B):
        cx, cy = P(p)
        cys = i in (6, 18)
        sphere(s, cx - d / 2, cy - d / 2, d, 'F4D03F' if cys else '2E86C1', name='Residuo B%d' % (i + 1))
    if labels:
        s.text(x + 1.4 * k, y + 0.55 * k, 3.6 * k, 0.4, 'CADENA A (21 aa)', 12, F_HEAD, 'C0392B', True, 'l')
        s.text(x, y + 4.45 * k, 3.6 * k, 0.4, 'CADENA B (30 aa)', 12, F_HEAD, '1F618D', True, 'l')
    return s.group_end()
