# -*- coding: utf-8 -*-
"""UNIDAD XI — Errores frecuentes, datos faltantes, conclusión, bibliografía, créditos y cierre"""
from base import *

U = 11


def div(D):
    def art(s):
        s.pic('Human_male', 11.3, 0.5, h=5.6, name='Organismo cierre')
        model(s, 'glucosa', 0.2, 1.2, 2.2, name='Glc')
        s.pic('adipocyte-1', 0.3, 4.5, 2.0, name='Adipocitos')
    divider(D, None if False else 11, 'XI', 'FUENTES, LÍMITES\nE INTEGRACIÓN', 'Lo que los datos permiten y no permiten concluir',
            ['Errores frecuentes', 'Datos faltantes por caso', 'Conclusión integradora', 'Bibliografía', 'Créditos de ilustraciones'], art,
            'Unidad XI. Cierre: errores frecuentes en examen y exposición, datos que faltan en cada caso y cómo condicionan las '
            'conclusiones, conclusión integradora, bibliografía primaria y contemporánea, y créditos de las ilustraciones.')


ERR = ['Afirmar que pCO₂ 24, HCO₃⁻ 13 y pH 7,15 forman una gasometría consistente.', 'Sostener que el bicarbonato reemplaza a la insulina en la CAD.',
       'Confundir cetosis fisiológica del ayuno con CAD acidémica.', 'Decidir la resolución por la cetonuria aislada sin β-OHB.',
       'Olvidar el K⁺ total depletado detrás de una kalemia «normal».', 'Creer que todo EHH carece absolutamente de cetonas o nunca se combina con CAD.',
       'Sostener que toda acción de la insulina pasa por GLUT4, incluido el hepatocito.', 'Identificar la LPL capilar con la HSL intracelular.',
       'Reducir la obesidad a «voluntad».', 'Suponer que una leptina elevada asegura saciedad normal.',
       'Diagnosticar diabetes con 145 mg/dL sin aclarar ayuno/confirmación.', 'Interpretar AST normal como ausencia de MASLD.',
       'Tomar Sokolow–Lyon positivo como confirmación de HVI.', 'Presentar sibutramina y rimonabant como vigentes en Argentina.',
       'Copiar artículos vetados de la Ley 26.396 como promulgados.', 'Usar la glucemia 110 del ATP III original como único punto actual.']


def errors(D, part):
    items = ERR[:8] if part == 0 else ERR[8:]
    s = new(D, U, 'Errores frecuentes que deben evitarse (%d/2)' % (part + 1), 'pink' if part == 0 else 'peach')
    ids = []
    for i, t in enumerate(items):
        c = i % 2; r = i // 2
        x = 0.4 + c * 6.35; y = 1.2 + r * 1.38
        g = s.group_start('Error %d' % (i + 1 + part * 8))
        s.shape(x, y, 6.15, 1.2, 'rect', WHITE, (INK, 1.5), SHD)
        s.shape(x + 0.12, y + 0.3, 0.6, 0.6, 'ellipse', 'C00000', (INK, 1.25), False, '×', 22, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False)
        s.text(x + 0.85, y + 0.08, 5.2, 1.05, t, 14.5, F_BODY, INK, False, 'l', 'm')
        ids.append(s.group_end())
    for k in range(0, 8, 2):
        s.step(fade(ids[k]), fade(ids[k + 1], after=True))
    s.note('Errores frecuentes (material de cátedra, apartado 59), %d a %d. ' % (part * 8 + 1, part * 8 + 8) + ' '.join(items))


def missing(D):
    s = new(D, U, 'Qué datos faltan y cómo condicionan las conclusiones', 'cyan')
    cols = [('CASO 11', 'Na⁺, K⁺, Cl⁻, albúmina, lactato, función renal, **β-OHB cuantitativo** y detalle de la insulinoterapia. La primera gasometría es **matemáticamente discordante**: el trastorno mixto no puede afirmarse.', 'y'),
            ('CASO 12', '**Sodio, BUN, creatinina** y especificación de osmolalidad **total/efectiva**: no puede calcularse tonicidad con certeza ni déficit de agua.', 's'),
            ('CASO 20', 'Condición de **ayuno** de la glucosa 145, HbA1c, LDL/ApoB confirmatorio, composición corporal, función ventilatoria y **estudio de sueño**, ingesta, actividad objetiva y evaluación psicológica.', 'g')]
    ids = []
    for i, (h, t, k) in enumerate(cols):
        x = 0.4 + i * 4.2
        g = s.group_start('Falta ' + h)
        mbox(s, x, 1.2, 4.0, 0.65, h, k, 17)
        tbox(s, x, 1.95, 4.0, 3.3, t, 14.5, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 5.5, 12.55, 1.35, '**No se deben inventar parámetros ausentes.** Cuando los datos no alcanzan, la conclusión correcta es **«no puede determinarse»** y qué medir.', 17)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Datos faltantes (apartado 62). Caso 11: faltan Na⁺, K⁺, Cl⁻, albúmina, lactato, función renal, β-OHB cuantitativo y detalle de '
           'insulinoterapia; la primera gasometría es discordante. Caso 12: faltan sodio, BUN, creatinina y la especificación de '
           'osmolalidad total/efectiva. Caso 20: faltan condición de ayuno para la glucosa 145, HbA1c, LDL/ApoB confirmatorio, composición '
           'corporal, función ventilatoria y evaluación de AOS, datos de ingesta, actividad objetiva y trabajo clínico-psicológico.')


def conclusion(D):
    s = new(D, U, 'Conclusión integradora', 'green')
    rows = [('pancreas', 'La **insulina** decide el sentido metabólico de los flujos entre órganos.'),
            ('adipocyte-1', 'El **tejido adiposo** amortigua excedentes y comunica reservas.'),
            ('brain-2', 'El **hipotálamo** integra energía con saciedad y recompensa.'),
            ('healthy_liver', 'El **hígado** redistribuye glucosa y lípidos; el **músculo** determina gran parte de su utilización.'),
            ('kidney-2', 'El **riñón** convierte hiperglucemia en pérdidas osmóticas y participa en HTA y daño crónico.')]
    ids = []
    for i, (img, t) in enumerate(rows):
        y = 1.2 + i * 1.12
        g = s.group_start('Concl %d' % i)
        fitpic(s, img, 0.45, y, 0.95, 0.95)
        tbox(s, 1.55, y, 6.25, 0.95, t, 15, anchor='m')
        ids.append(s.group_end())
    tri = [('CAD', 'Lo que ocurre cuando **falta el freno insulínico** de la lipólisis y la cetogénesis.', 'r'),
           ('EHH', 'La acción residual **limita las cetonas** pero no evita hiperglucemia y deshidratación extrema.', 's'),
           ('OBESIDAD VISCERAL', 'La resistencia crónica se convierte en **SM, DM2, HTA, MASLD y aterosclerosis**.', 'y')]
    tid = []
    for i, (h, t, k) in enumerate(tri):
        y = 1.2 + i * 1.85
        g = s.group_start('Tri ' + h)
        mbox(s, 8.1, y, 4.85, 0.55, h, k, 15)
        tbox(s, 8.1, y + 0.62, 4.85, 1.05, t, 14.5, anchor='m')
        tid.append(s.group_end())
    for g in ids + tid:
        s.step(fade(g))
    s.note('Conclusión integradora (apartado 63). La insulina decide el sentido metabólico de los flujos entre órganos; el tejido adiposo '
           'amortigua excedentes y comunica reservas; el hipotálamo integra señales de energía con saciedad y recompensa; el hígado '
           'redistribuye glucosa y lípidos; el músculo determina gran parte de su utilización; y el riñón convierte la hiperglucemia en '
           'pérdidas osmóticas y participa en HTA y daño crónico. La CAD demuestra lo que sucede cuando falta el freno insulínico; el EHH, '
           'cuando la acción residual limita las cetonas pero no la hiperglucemia y la deshidratación; la obesidad visceral disfuncional '
           'explica por qué la resistencia crónica se convierte en síndrome metabólico, DM2, hipertensión, enfermedad hepática y '
           'aterosclerosis.')


def biblio(D):
    s = new(D, U, 'Bibliografía primaria y contemporánea', 'peachW', tsize=30)
    refs1 = ('**[T]** Valenzuela BA, Sanhueza CJ. El tejido adiposo: algo más que un reservorio de energía. Grasas y Aceites. 2009;60(5):437–450. doi:10.3989/gya.043209\n'
             '**[S]** Martínez RG, Alonso KR, Novik AV. Síndrome metabólico. Bases clínicas y fisiopatológicas para un enfoque terapéutico racional. Rev Méd Chile. 2009;137:685–694.\n'
             '**[A]** Vásquez-Machado M, Ulate-Montero G. Regulación del peso corporal y del apetito. Acta Méd Costarric. 2010;52(2):79–89.')
    refs2 = ('**[ADA26]** ADA Professional Practice Committee. Standards of Care in Diabetes—2026 (secciones 2, 6, 8, 9 y 16). Diabetes Care, suplemento ene-2026.\n'
             '**[C24]** Umpierrez GE et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. 2024. doi:10.2337/dci24-0032\n'
             '**[ASMBS]** Eisenberg D et al. 2022 ASMBS and IFSO Indications for Metabolic and Bariatric Surgery. SOARD. 2022. doi:10.1016/j.soard.2022.08.013\n'
             '**[ANMAT]** Disposiciones 6533/2010 (sibutramina) y 6238/2008 (rimonabant); comunicado semaglutida (Wegovy) 07/08/2023.\n'
             '**[LEY]** Ley 26.396 y Decreto 1395/2008 (promulgación parcial).\n'
             '**ACP 2026**: Pharmacologic Treatments With Lifestyle Modifications in Adults With Overweight or Obesity: A Living Clinical Guideline. Ann Intern Med, abril 2026. doi:10.7326/ANNALS-25-02714')
    a = tbox(s, 0.4, 1.15, 12.55, 2.35, refs1, 13, head='Revisiones de la cátedra')
    b = tbox(s, 0.4, 3.75, 12.55, 3.1, refs2, 12, head='Referencias clínicas y normativas', hkind='s')
    s.step(fade(a)); s.step(fade(b))
    s.note('Bibliografía (apartados 60 y 61). [T] es la fuente base de los capítulos 21–27; [S], de 25–27 y 50–55; [A], de 28–31. Las '
           'revisiones antiguas se emplean como base conceptual, no como autoridad sobre fármacos vigentes ni criterios diagnósticos '
           'actuales. Ampliaciones bibliográficas señaladas en las notas (estructura del canal K_ATP, exocitosis, glucación, AGE/RAGE, '
           'PKC isoformas, aterogénesis): textos de bioquímica y fisiología médica de referencia (p. ej., Lehninger, Guyton y Hall). '
           'Enlaces: doi.org/10.2337/dc26-s002, dc26-s008, dc26-S009, dc26-s016; argentina.gob.ar/normativa (ANMAT y Ley 26.396).')


def credits(D):
    s = new(D, U, 'Créditos de ilustraciones y modelos', 'blue')
    t = tbox(s, 0.4, 1.15, 12.55, 4.2,
             '- Ilustraciones de órganos, células y lipoproteínas: **Servier Medical Art** (smart.servier.com), licencia **CC BY 3.0/4.0**, obtenidas del repositorio Bioicons; se usan con atribución y sin modificar su contenido.\n'
             '- Ilustraciones adicionales del repositorio **Bioicons**: nefrona 2D (EmilyADaniel, CC0), neurona piramidal (Fabian Mikulasch, CC0), hígado (Jan Clusmann, CC0), silueta de paciente (Marcel Tisch, CC0), cuerpo humano (DBCLS, CC BY 4.0).\n'
             '- **Modelos moleculares 3D**: geometrías calculadas con **RDKit** (ETKDG + MMFF) y dibujadas como formas nativas editables (código CPK).\n'
             '- Insulina: modelo **esquemático** de cadenas A/B y puentes disulfuro (no coordenadas cristalográficas).\n'
             '- Diagramas, mapas, células y animaciones: formas nativas de PowerPoint, totalmente editables.', 14.5, head='Atribuciones')
    for i, img in enumerate(['pancreas', 'healthy_liver', 'adipocyte-1', 'kidney-2', 'brain-2', 'heart-front', 'macrophage', 'ldl-1']):
        fitpic(s, img, 0.5 + i * 1.57, 5.6, 1.35, 1.2)
    s.step(fade(t))
    s.note('Créditos: Servier Medical Art (Les Laboratoires Servier), licencias Creative Commons BY 3.0 y 4.0, distribuidas a través de '
           'Bioicons (bioicons.com). Modelos moleculares generados con RDKit. Fuentes tipográficas: Permanent Marker (Apache 2.0), Fira Sans '
           'Condensed y Bangers (SIL OFL), incrustadas en el archivo.')


def close(D):
    s = D.new(WHITE)
    s.unit = 11; s.morph = False
    background(s, 'cover')
    model(s, 'glucosa', 2.5, 0.5, 2.6, name='Glc cierre')
    model(s, 'palmitato', 5.6, 5.7, 4.6, hs=False, name='AG cierre')
    model(s, 'bhb', 8.6, 0.6, 1.9, name='BHB cierre')
    s.pic('adipocyte-1', 0.1, 4.9, 2.3, name='Adipocitos cierre')
    s.pic('brain-2', 10.85, 0.9, 2.3, name='Cerebro cierre')
    s.pic('heart-front', 11.2, 4.1, 1.8, name='Corazón cierre')
    t = btitle(s, 'LA ENERGÍA NO CIRCULA\nPOR ÓRGANOS AISLADOS', 46, y=2.2, x=2.6, w=8.1, name='Título cierre')
    sub = s.text(2.8, 4.35, 7.7, 0.9, 'El organismo funciona como una red metabólica, hormonal, neuronal y vascular.', 19, F_HEAD, INK, True, 'c', 'm',
                 name='Frase final', reff=GLOWW)
    s.step(fade(sub))
    s.note('Frase final: «La energía no circula por órganos aislados: el organismo funciona como una red metabólica, hormonal, '
           'neuronal y vascular». Cierre de la clase.')


def build(D):
    div(D)
    errors(D, 0)
    errors(D, 1)
    missing(D)
    conclusion(D)
    biblio(D)
    credits(D)
    close(D)
