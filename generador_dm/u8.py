# -*- coding: utf-8 -*-
"""UNIDAD VIII — Tratamiento de la obesidad, farmacología y normativa argentina"""
from base import *

U = 8
VERIF = ('Situación regulatoria según el material de cátedra (actualizado a octubre de 2026, fuentes [ANMAT] y [LEY]). El 27/10/2026 no fue '
         'posible consultar argentina.gob.ar desde el entorno de producción; antes de exponer, confirmar en ANMAT y el Boletín Oficial.')


def div(D):
    def art(s):
        s.pic('runner', 11.2, 0.5, h=3.0, name='Corredor')
        s.pic('stomach', 10.9, 3.9, 1.9, name='Estómago')
        s.pic('small-intestine', 0.25, 1.2, 2.0, name='Intestino')
        model(s, 'tag', 0.15, 4.4, 2.3, hs=False, name='TAG')
    divider(D, U, 'VIII', 'TRATAMIENTO,\nFARMACOLOGÍA Y NORMATIVA', 'Abordaje crónico, interdisciplinario y sin estigma',
            ['Nutrición y balance energético', 'Actividad, conducta y salud mental', 'Fármacos: mecanismos y riesgos', 'Orlistat (animación)',
             'Agonistas GLP-1 (animación)', 'Seguridad contextualizada', 'Cirugía metabólica', 'ANMAT y Ley 26.396'], art,
            'Unidad VIII. Tratamiento de la obesidad: nutrición, actividad, intervención conductual y psicológica, farmacoterapia con sus '
            'mecanismos moleculares, cirugía metabólica y normativa argentina, distinguiendo fármacos históricos, suspendidos y vigentes. '
            'Contenido formativo: no constituye indicación terapéutica.')


def diet(D):
    s = new(D, U, 'Dieta hipocalórica: objetivo y calidad', 'greenR')
    s.pic('digestive-system', 0.4, 1.15, h=5.7, name='Digestivo dieta')
    obj = tbox(s, 2.4, 1.15, 5.2, 2.6, 'Reducir aporte respecto del gasto → **movilizar TAG**, reducir tamaño adipocitario y grasa **visceral/ectópica**; mejorar glucemia, TG, presión y síntomas.', 14.5, head='Objetivo')
    hg = tbox(s, 7.85, 1.15, 5.1, 2.6, '«**Hipograsa**» responde a la propuesta del caso, **no es requisito universal**: funcionan patrones mediterráneos, moderados en grasas o en carbohidratos, si son adecuados y **sostenibles**.', 14, head='Patrones')
    q = steps_panel(s, 2.4, 4.0, 10.55, ['Limitar grasas **trans**; sustituir parte de saturadas por **insaturadas**.',
                                         'Proteína adecuada, **fibra** (frutas, verduras, legumbres, integrales) y entrenamiento que **preserve masa magra**.',
                                         'La **restricción coercitiva** («se prohibió a la familia traerle comida») no reemplaza consentimiento ni abordaje terapéutico.'], 13.5, anim=False)[0]
    s.step(fade(obj)); s.step(fade(hg))
    for g in q:
        s.step(fade(g))
    s.note('Pregunta posinternación 1. La dieta hipocalórica busca reducir el aporte energético respecto del gasto para movilizar '
           'reservas de triglicéridos, disminuir el tamaño de los adipocitos y la grasa visceral y ectópica, y mejorar glucemia, '
           'triglicéridos, presión y síntomas. La calificación «hipograsa» no es requisito universal de eficacia. Intervención '
           'integral: evaluar ingesta, acceso a alimentos, hambre, sueño, medicación, depresión/ansiedad, trastornos de la conducta '
           'alimentaria, tabaquismo, entorno familiar, riesgo cardiovascular y composición corporal. La frase del caso sobre prohibir '
           'traer comida refleja el manejo narrado, no un modelo contemporáneo centrado en autonomía y reducción del estigma.')


def lifestyle(D):
    s = new(D, U, 'Actividad, conducta, sueño y comorbilidades', 'peachW')
    cols = [('runner', 'ACTIVIDAD PROGRESIVA', 'Movilidad articular, marcha según tolerancia, **fuerza adaptada**, fisioterapia; prevenir caídas y problemas osteoarticulares; **preservar masa muscular**.'),
            ('brain-2', 'APOYO PSICOLÓGICO', 'Conducta alimentaria, pérdida laboral, autoestima, compulsiones y **juego patológico**; objetivos **sin culpabilizar**; autonomía y adherencia.'),
            ('healthy-lung', 'SUEÑO', 'Pesquisar **AOS**, promover regularidad y tratarla si se confirma (presión positiva si está indicada).'),
            ('heart-front', 'COMORBILIDADES', 'Tratar de manera específica **HTA, dislipidemia, glucemia y tabaquismo** (dejar de fumar: gran beneficio CV independiente del peso).')]
    ids = []
    for i, (img, h, t) in enumerate(cols):
        x = 0.4 + i * 3.17
        g = s.group_start('Pilar ' + h)
        fitpic(s, img, x + 0.6, 1.15, 1.8, 1.6)
        mbox(s, x, 2.9, 3.0, 0.6, h, 'y', 13.5)
        tbox(s, x, 3.6, 3.0, 2.4, t, 13.5, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 6.2, 12.55, 0.68, 'Los objetivos iniciales se **individualizan** y pueden incluir mejoras clínicas antes de grandes cambios de peso.', 14)
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('Tratamiento no farmacológico: actividad progresiva (movilidad articular, marcha según tolerancia, fuerza adaptada, '
           'fisioterapia), apoyo psicológico (conducta alimentaria, pérdida laboral, autoestima, compulsiones y juego patológico, sin '
           'culpabilizar), sueño (pesquisar y tratar AOS) y tratamiento específico de comorbilidades. Dejar de fumar aporta un beneficio '
           'cardiovascular muy importante independientemente del peso [ADA26].')


def drugs1(D):
    s = new(D, U, 'Farmacoterapia I: opciones con mecanismo y precauciones', 'cyan')
    rows = [['Fármaco / clase', 'Mecanismo', 'Efecto buscado', 'Riesgos y comentarios'],
            ['Orlistat', 'Inhibe lipasas gástrica y pancreática en la luz: ↓ hidrólisis/absorción de TAG', 'Menor energía absorbida', 'Esteatorrea, urgencia fecal; vitaminas A, D, E, K; malabsorción/colestasis'],
            ['Liraglutida', 'Agonista GLP-1R (Gs/AMPc): saciedad, ↓ ingesta, vaciamiento ↓', 'Peso ↓; control glucémico', 'Náuseas/vómitos, deshidratación, colelitiasis; antecedentes pancreatobiliares'],
            ['Semaglutida', 'Agonista prolongado GLP-1R', 'Gran ↓ de ingesta y peso', 'Efectos GI; Wegovy autorizado por ANMAT (2023), sujeto a acceso'],
            ['Tirzepatida', 'Agonista dual GIPR + GLP-1R', 'Apetito ↓; glucemia y peso', 'Efectos GI; verificar indicación y registro vigentes'],
            ['Naltrexona + bupropión', 'Circuitos POMC/recompensa y receptores opioides', '↓ impulso de ingesta', 'HTA no controlada, convulsiones, opioides, psiquiatría; disponibilidad variable']]
    table(s, 0.4, 1.15, 12.55, rows, [2.2, 4.0, 2.4, 3.95], size=12.5, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Fármacos 1')
    p = tbox(s, 0.4, 5.75, 12.55, 1.1, 'Herramienta **adyuvante** de tratamiento **crónico**. ADA 2026 y ACP 2026 destacan agentes basados en **GLP-1 y GIP/GLP-1** donde estén indicados. **No todo agente de guías internacionales está aprobado o disponible en Argentina.**', 13.5, anchor='m')
    s.step(fade(p))
    s.note('La farmacoterapia es una herramienta adyuvante de tratamiento crónico, indicada según IMC y complicaciones, riesgos, '
           'preferencias, accesibilidad y aprobación local. La guía ADA 2026 destaca los agentes basados en GLP-1 y GIP/GLP-1 por su '
           'eficacia, especialmente con DM2; la guía del ACP 2026 también prioriza semaglutida y tirzepatida donde estén indicadas. ' + VERIF +
           ' Notas de prensa (no oficiales) informan aprobación de tirzepatida por ANMAT; la disposición oficial no pudo revisarse.')


def drugs2(D):
    s = new(D, U, 'Farmacoterapia II: especializados e históricos', 'pink')
    rows = [['Fármaco', 'Mecanismo', 'Situación', 'Comentario'],
            ['Fentermina + topiramato', 'Simpaticomimético + acciones centrales del topiramato', 'Aprobación depende del país', 'Riesgo CV, teratogenicidad, efectos neurocognitivos; no apropiado con TA 160/100'],
            ['Setmelanotida', 'Agonista MC4R', 'Indicación altamente especializada', 'Obesidad monogénica seleccionada; no para obesidad poligénica común'],
            ['Sibutramina (histórica)', 'Inhibe recaptación de NA/5-HT (± DA)', 'SUSPENDIDA en Argentina', 'Riesgo cardiovascular; no recomendar'],
            ['Rimonabant (histórico)', 'Antagonista/inverso CB1 central', 'SUSPENDIDO y retirado', 'Efectos psiquiátricos graves; no recomendar']]
    t, H = table(s, 0.4, 1.15, 12.55, rows, [2.5, 3.5, 2.8, 3.75], size=13, head_fill=BOX, fills=(WHITE, 'FFF2CC'), name='Fármacos 2', heights=[0.45, 0.8, 0.8, 0.6, 0.6])
    m = s.shape(0.36, 3.17, 12.63, 1.26, 'rect', None, ('C00000', 4), False, name='Marca históricos')
    p = pearl(s, 0.4, 1.45 + H, 12.55, 1.2, 'Que la **sibutramina** aparezca en el artículo de síndrome metabólico de **2009** no la vuelve utilizable hoy: distinguir **autorización, suspensión y disponibilidad** con fecha.', 15)
    v = tbox(s, 0.4, 2.85 + H, 12.55, 0.9, 'Verificación: ' + VERIF, 11.5, anchor='m')
    s.step(zoom(m)); s.step(zoom(p)); s.step(fade(v))
    s.note('Fentermina + topiramato: simpaticomimético más acciones centrales del topiramato; riesgo cardiovascular, teratogenicidad y '
           'efectos neurocognitivos; no es elección automática con TA 160/100. Setmelanotida: agonista MC4R para etiologías genéticas '
           'específicas. Sibutramina y rimonabant son históricos: suspendidos en Argentina; no recomendar. ' + VERIF)


def orlistat(D):
    s = new(D, U, 'Animación: orlistat en la luz intestinal', 'greenR')
    s.pic('small-intestine', 0.9, 4.65, h=2.2, name='Intestino orlistat')
    s.shape(0.4, 1.15, 8.2, 3.4, 'rect', ('a', 'FFF2CC', 40), (INK, 1.25), False, name='Luz intestinal')
    lab(s, 0.5, 1.2, 3.0, 0.35, 'LUZ INTESTINAL', 13, align='l')
    tg = [model(s, 'tag', 0.7 + i * 1.6, 1.7, 1.3, hs=False, name='TAG dieta %d' % i, seed=11 + i) for i in range(3)]
    lip = [s.shape(1.0 + i * 1.6, 3.3, 0.9, 0.55, 'roundRect', shade('5DADE2', 0.4, 0.3), ('1F618D', 1.25), False, 'Lipasa', 11, F_HEAD, INK, True, 'c', 'm', name='Lipasa %d' % i) for i in range(3)]
    orl = [s.shape(5.9 + i * 0.6, 1.65, 0.5, 0.5, 'ellipse', 'C00000', (INK, 1.0), False, 'O', 13, F_HEAD, WHITE, True, 'c', 'm', (0, 0, 0, 0), fit=False, name='Orlistat %d' % i) for i in range(3)]
    st = steps_panel(s, 8.9, 1.15, 4.05, ['TAG dietarios llegan a la luz.', 'Las **lipasas gástrica y pancreática** los hidrolizarían a AG y monoacilglicéridos absorbibles.',
                                          'El **orlistat** se une a las lipasas y las **inhibe**.', 'Parte de la grasa **no se absorbe** y se elimina por heces (esteatorrea esperable).'], 13, anim=False)[0]
    feces = mbox(s, 4.9, 4.75, 3.7, 0.7, 'Grasa no absorbida → heces', 'r', 14, caps=False)
    s.step(fade(st[0]), *[fade(t, after=True, dur=200) for t in tg])
    s.step(fade(st[1]), *[pulse(l, after=True, dur=250) for l in lip])
    s.step(fade(st[2]), *[path(o, (1.2 + i * 1.6) - (5.9 + i * 0.6), 1.55, dur=1200, delay=i * 200) for i, o in enumerate(orl)])
    s.step(fade(st[3]), zoom(feces, after=True))
    nota = tbox(s, 8.9, 5.5, 4.05, 1.35, 'No bloquea la lipólisis del **adipocito**, no es incretínico ni aumenta el basal.', 12.5, anchor='m')
    s.step(fade(nota))
    s.note('Orlistat del caso: se une e inhibe las lipasas gastrointestinales y disminuye la hidrólisis de los TAG dietarios a ácidos '
           'grasos y monoacilglicéridos absorbibles; parte de la grasa ingerida permanece en la luz y se elimina por heces. No bloquea '
           'la lipólisis de los adipocitos, no es agonista incretínico y no aumenta de forma primaria el metabolismo basal. Su '
           'tolerabilidad mejora distribuyendo las grasas en la dieta; revisar interacciones y vitaminas liposolubles; con antecedente '
           'de pancreatitis biliar la evaluación debe ser específica. Animación: llegan los TAG, las lipasas se activan, las fichas de '
           'orlistat (O) se unen a ellas y la grasa sale por heces.')


def glp1(D):
    s = new(D, U, 'Animación: agonistas del receptor GLP-1', 'cyan')
    c = s.group_start('Receptor GLP-1')
    membrane_h(s, 0.4, 2.0, 5.2, 0.4, name='Membrana GLP1')
    gpcr(s, 2.3, 2.0, 0.4, 1.3, name='GLP-1R', color='7DCEA0')
    s.group_end()
    ag = mbox(s, 2.25, 1.15, 1.6, 0.45, 'Agonista', 's', 13, caps=False, name='Agonista GLP1')
    chain_ = s.group_start('Señal')
    for i, t in enumerate(['Gs → adenilil ciclasa', 'AMPc ↑', 'PKA · Epac2']):
        mbox(s, 1.2, 3.0 + i * 0.7, 3.4, 0.5, t, 'g' if i != 1 else 'y', 13, caps=False)
        if i:
            s.arrow([(2.9, 3.0 + i * 0.7 - 0.2), (2.9, 3.0 + i * 0.7 - 0.02)], INK, 2)
    s.group_end()
    tgt = [('pancreas', 'Célula β: insulina **glucosa-dependiente** ↑; glucagón ↓ en hiperglucemia'), ('brain-2', 'SNC / aferencias vagales: **saciedad**, ingesta ↓'),
           ('stomach', '**Vaciamiento gástrico** más lento (según agente y etapa)')]
    ids = []
    for i, (img, t) in enumerate(tgt):
        y = 1.15 + i * 1.45
        g = s.group_start('Blanco %d' % i)
        s.arrow([(4.7, 4.0), (6.0, y + 0.6)], ACT, 2.5)
        fitpic(s, img, 6.1, y, 1.3, 1.2)
        tbox(s, 7.5, y + 0.05, 5.45, 1.15, t, 14, anchor='m')
        ids.append(s.group_end())
    p = pearl(s, 0.4, 5.6, 12.55, 1.25, 'El peso baja por **modificación sostenida de la ingesta** y respuestas neuroendocrinas, **no** por una «quema química de grasa». Planificar seguimiento, nutrición, actividad y riesgo de **recuperar peso al suspender**.', 14.5)
    s.step(fade(ag), path(ag, 0.0, 0.55, dur=800))
    s.step(wipe(chain_, 't', dur=900))
    for g in ids:
        s.step(fade(g))
    s.step(zoom(p))
    s.note('GLP-1R es un receptor acoplado a Gs. En células β el AMPc activa PKA/Epac2 y potencia la secreción insulinotrópica dependiente '
           'de glucosa. En circuitos centrales y aferencias digestivas promueve saciedad y menor ingesta; el retraso del vaciamiento '
           'gástrico es más marcado en algunos contextos o etapas. La acción sobre el peso depende de la modificación sostenida de la '
           'ingesta, no de una quema química directa de grasa. Debe planificarse seguimiento y el riesgo de recuperar peso al '
           'suspender la medicación.')


def safety(D):
    s = new(D, U, 'Seguridad farmacológica contextualizada al caso 20', 'peachW')
    items = [('TA 160/100 · riesgo CV · sospecha de AOS', '**Simpaticomiméticos** no son selección automática.', 'r'),
             ('Antecedente pancreatobiliar + descenso rápido', 'Revisar riesgos **biliares**, síntomas abdominales y fichas técnicas antes de **incretinas**.', 's'),
             ('Depresión, conducta, juego patológico', 'Valorar **riesgos psiquiátricos** e interacciones.', 'b'),
             ('DM2 con sulfonilureas', 'Al sumar fármacos que reducen glucemia/ingesta, **revisar dosis** por hipoglucemia.', 'y'),
             ('Tabaquismo', '**Dejar de fumar**: beneficio CV muy importante independiente del peso.', 'g')]
    ids = []
    for i, (h, t, k) in enumerate(items):
        y = 1.15 + i * 1.12
        g = s.group_start('Seg %d' % i)
        mbox(s, 0.4, y, 4.6, 0.95, h, k, 13.5, caps=False)
        tbox(s, 5.15, y, 7.8, 0.95, t, 14.5, anchor='m')
        ids.append(s.group_end())
    for g in ids:
        s.step(fade(g))
    s.note('Seguridad contextualizada: con TA 160/100, riesgo cardiometabólico y sospecha de AOS, los simpaticomiméticos no son opciones de '
           'selección automática. El antecedente pancreatobiliar y la pérdida rápida de peso obligan a revisar riesgos biliares y fichas '
           'técnicas antes de considerar incretinas. En personas con depresión, trastornos conductuales o juego patológico se valoran los '
           'riesgos psiquiátricos. Con sulfonilureas, revisar dosis por hipoglucemia. Suspender el tabaco aporta beneficio cardiovascular '
           'muy importante [ADA26].')


def surgery(D):
    s = new(D, U, 'Cirugía metabólica y bariátrica', 'blue')
    s.pic('stomach', 0.4, 1.2, 3.0, name='Estómago cirugía')
    crit = tbox(s, 3.7, 1.15, 9.25, 1.9, 'ASMBS/IFSO 2022: **recomendada desde IMC ≥ 35 kg/m²** independientemente de comorbilidades en pacientes apropiadamente evaluados; **considerar** con enfermedad metabólica e IMC **30–34,9**.', 15, head='Indicaciones')
    case = mbox(s, 3.7, 3.3, 9.25, 0.75, 'CASO 20: IMC 58,8 → CRITERIO ANTROPOMÉTRICO FUERTE PARA EVALUACIÓN', 'y', 14)
    t = tbox(s, 3.7, 4.3, 9.25, 1.35, 'Evaluación por **equipo interdisciplinario**: no significa cirugía inmediata ni elimina salud mental, riesgo quirúrgico, seguimiento, requisitos regulatorios y cobertura.', 14, anchor='m')
    m = tbox(s, 0.4, 4.3, 3.1, 2.55, '**Manga gástrica** y **bypass gástrico**: modifican capacidad y **hormonas intestinales**, con efectos glucémicos relevantes.', 13.5)
    r = pearl(s, 3.7, 5.85, 9.25, 1.0, 'Riesgos: **déficits nutricionales**, complicaciones quirúrgicas y **seguimiento de por vida**.', 15)
    s.step(fade(crit)); s.step(zoom(case)); s.step(fade(t)); s.step(fade(m)); s.step(zoom(r))
    s.note('Según el consenso ASMBS/IFSO 2022 la cirugía metabólica/bariátrica es recomendada a partir de IMC ≥35 kg/m² '
           'independientemente de comorbilidades en pacientes apropiadamente evaluados, y se considera en ciertos pacientes con '
           'enfermedad metabólica e IMC 30–34,9. Con IMC 58,8 el paciente reúne criterio antropométrico fuerte para evaluación por '
           'equipo interdisciplinario; no significa cirugía inmediata. Manga gástrica y derivación gástrica modifican la capacidad '
           'alimentaria y las hormonas intestinales; tienen riesgos de déficits nutricionales, complicaciones y requieren seguimiento de '
           'por vida [ASMBS].')


def anmat(D):
    s = new(D, U, 'ANMAT: sibutramina y rimonabant (pregunta 2a)', 'cyanR')
    a = s.group_start('Sibutramina')
    mbox(s, 0.4, 1.15, 6.1, 0.65, 'SIBUTRAMINA · DISPOSICIÓN 6533/2010', 'r', 15)
    tbox(s, 0.4, 1.9, 6.1, 2.6, '26/10/2010 (publicada el 02/11/2010): **suspendió** la importación del ingrediente activo y la elaboración, importación, comercialización, distribución y uso de especialidades que la contuvieran, solas o asociadas, por **seguridad cardiovascular**.', 14)
    s.group_end()
    b = s.group_start('Rimonabant')
    mbox(s, 6.85, 1.15, 6.1, 0.65, 'RIMONABANT · DISPOSICIÓN 6238/2008', 'r', 15)
    tbox(s, 6.85, 1.9, 6.1, 2.6, '24/10/2008: **suspendió** comercialización y expendio y ordenó el **retiro del mercado** por relación beneficio-riesgo desfavorable y efectos **psiquiátricos**, incluida ideación/suicidalidad.', 14)
    s.group_end()
    w = s.group_start('Wegovy')
    mbox(s, 0.4, 4.75, 6.1, 0.6, 'SEMAGLUTIDA PARA PESO (WEGOVY)', 'g', 14)
    tbox(s, 0.4, 5.4, 6.1, 1.45, 'Registro comunicado por ANMAT el **07/08/2023**; acceso sujeto a comercialización y cobertura.', 13.5, anchor='m')
    s.group_end()
    v = tbox(s, 6.85, 4.75, 6.1, 2.1, VERIF, 12, head='Fecha de verificación', hkind='w')
    s.step(fade(a)); s.step(fade(b)); s.step(fade(w)); s.step(fade(v))
    s.note('Sibutramina: la Disposición ANMAT 6533/2010, del 26 de octubre de 2010 y publicada el 2 de noviembre de 2010, suspendió la '
           'importación del ingrediente activo y la elaboración, importación, comercialización, distribución y uso de especialidades '
           'medicinales que la contuvieran, por preocupaciones de seguridad cardiovascular. Rimonabant: la Disposición ANMAT 6238/2008, '
           'del 24 de octubre de 2008, suspendió comercialización y expendio y ordenó el retiro del mercado por beneficio-riesgo '
           'desfavorable y efectos psiquiátricos. Registro de semaglutida para manejo de peso: comunicado ANMAT del 07/08/2023. ' + VERIF)


def ley(D):
    s = new(D, U, 'Ley 26.396: trastornos alimentarios (pregunta 3)', 'peachW')
    arts = [('Art. 2', 'Incluye **obesidad, bulimia y anorexia nerviosa**, entre otros que determine la reglamentación.'),
            ('Art. 3', 'Programa nacional: campañas, educación, prevención, investigación, combate a **discriminación/estigmatización**.'),
            ('Arts. 6–9', 'Educación alimentaria, actividad física, entornos escolares y capacitación.'),
            ('Arts. 15–16', 'Cobertura de tratamiento integral en el **PMO** y asistencia **multidisciplinaria** según indicación y requisitos.'),
            ('Art. 17', 'Prohibición de negar bienes o servicios a una persona con obesidad en condiciones legalmente previstas.'),
            ('Art. 18', 'Accesibilidad y equipamiento de instituciones educativas y sanitarias.')]
    mbox(s, 0.4, 1.15, 12.55, 0.55, 'SANCIONADA 13/08/2008 · PUBLICADA 03/09/2008 · DECLARA DE INTERÉS NACIONAL LA PREVENCIÓN Y CONTROL', 'y', 13)
    ids = []
    for i, (h, t) in enumerate(arts):
        y = 1.85 + i * 0.6
        g = s.group_start('Ley ' + h)
        mbox(s, 0.4, y, 1.6, 0.5, h, 'g', 13, caps=False)
        s.text(2.15, y, 10.8, 0.5, t, 13.5, F_BODY, INK, False, 'l', 'm')
        ids.append(s.group_end())
    veto = pearl(s, 0.4, 5.55, 12.55, 1.3, '**Veto parcial: Decreto 1395/2008** observó los arts. **5** (notificación epidemiológica), **11** (leyenda en publicidad de alimentos), **20** (etiqueta de grasas trans) y **21** (sanciones): no presentarlos como normas vigentes.', 14)
    s.step(*[fade(g, after=i > 0, dur=200) for i, g in enumerate(ids)])
    s.step(zoom(veto))
    s.note('Ley 26.396: sancionada el 13 de agosto de 2008 y publicada el 3 de septiembre de 2008; declaró de interés nacional la '
           'prevención y control de los trastornos alimentarios. Art. 2: obesidad, bulimia y anorexia nerviosa, entre otros. Art. 3: '
           'programa nacional. Arts. 6–9: educación alimentaria, actividad física, entornos escolares y capacitación. Arts. 15 y 16: '
           'cobertura de tratamiento integral en el PMO. Art. 17: prohibición de negar bienes o servicios. Art. 18: accesibilidad. '
           'Promulgación con veto parcial: el Decreto 1395/2008 observó los artículos 5, 11, 20 y 21. Aplicación al caso: atención '
           'respetuosa y multidisciplinaria; la ley no significa que todas las técnicas o productos estén cubiertos sin requisitos. ' + VERIF)


def build(D):
    div(D)
    diet(D)
    lifestyle(D)
    drugs1(D)
    drugs2(D)
    orlistat(D)
    glp1(D)
    safety(D)
    surgery(D)
    anmat(D)
    ley(D)
