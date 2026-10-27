# -*- coding: utf-8 -*-
"""UNIDAD X — Doce ejercicios clínico-bioquímicos y preguntas de opción múltiple"""
from base import *

U = 10


def div(D):
    def art(s):
        model(s, 'glucosa', 10.8, 0.6, 2.2, name='Glc')
        model(s, 'bicarbonato', 11.0, 3.4, 1.6, name='Bicarbonato', label='HCO₃⁻')
        model(s, 'urea', 0.5, 1.4, 1.6, name='Urea', label='Urea')
        model(s, 'piruvato', 0.3, 4.4, 1.9, name='Piruvato', label='Piruvato')
    divider(D, U, 'X', 'PRÁCTICA APLICADA', 'Datos → interpretación → fórmula → cálculo → resultado → significado',
            ['Ej. 1–2: diagnóstico y HbA1c', 'Ej. 3–5: gases y anion gap', 'Ej. 6: osmolalidad', 'Ej. 7–9: K⁺, cetonas, EHH',
             'Ej. 10–11: IMC, GET y SM', 'Ej. 12: fármaco tras la crisis', 'Preguntas de opción múltiple'], art,
            'Unidad X. Doce ejercicios clínico-bioquímicos. Cada uno se revela por clic en seis bloques: datos, interpretación, fórmula, '
            'cálculo, resultado y significado fisiológico; la solución no aparece desde el inicio. Se cierran con diez preguntas de opción '
            'múltiple con respuesta razonada.')


EX = [
    (1, 'Tres pruebas que no coinciden', 'Asintomático, 44 años: glucemia en ayunas **124 mg/dL**, HbA1c **6,6 %**, PTOG 2 h **196 mg/dL**.',
     'A1c sobre el umbral (≥ 6,5); ayunas (100–125) y PTOG (140–199) en rango de **prediabetes**. ¿Se confirma diabetes?',
     'Sin hiperglucemia inequívoca: **dos resultados anormales** (misma prueba repetida o dos distintas).',
     'Resultados **discordantes** → repetir la prueba situada **sobre el umbral** (HbA1c); verificar calidad analítica.',
     '**No confirmado aún**: repetir HbA1c. No diagnosticar por promedio ni descartar por la ayunas de 124.',
     'Cada prueba mide un aspecto distinto de la exposición glucémica; la discordancia exige investigar causas (p. ej., alteraciones eritrocitarias).',
     'Ejercicio 1 [ADA26]. Una A1c de 6,6 % está por encima del umbral, mientras la glucemia en ayunas y la PTOG caen en intervalos de '
     'prediabetes. Sin hiperglucemia inequívoca corresponde repetir la prueba que supera el umbral, verificar calidad analítica y causas de '
     'discordancia. No diagnosticar por promedio de resultados ni descartar por la glucemia en ayunas de 124.'),
    (2, 'HbA1c como glucemia promedio', 'HbA1c **12 %**; glucemia basal aislada **160 mg/dL** (caso 11).', '¿Por qué no coinciden la A1c y la glucemia basal?',
     'eAG (mg/dL) = 28,7 × HbA1c − 46,7', '28,7 × 12 = 344,4 → 344,4 − 46,7', '**eAG ≈ 297,7 mg/dL**',
     'La A1c pondera **semanas**; la glucemia es una **instantánea**: picos posprandiales, adherencia variable, cambios recientes. Revisar vida eritrocitaria ante discordancias extremas.',
     'Ejercicio 2. eAG = 28,7 × 12 − 46,7 = 297,7 mg/dL. La A1c refleja exposición ponderada durante semanas, mientras una glucemia es una '
     'instantánea: pueden existir picos posprandiales, variación de adherencia o cambios en los últimos días.'),
    (3, 'Coherencia de una gasometría', 'pH **7,15** · HCO₃⁻ **13** · pCO₂ **24**.', '¿Pertenecen los tres valores a una tríada coherente?',
     'pH = 6,1 + log[HCO₃⁻ / (0,03 × pCO₂)]', '0,03 × 24 = 0,72 · 13/0,72 = 18,06 · log = 1,257', '**pH calculado ≈ 7,36 ≠ 7,15**',
     'La tríada **no es coherente**: repetir muestras y no clasificar trastornos mixtos hasta corregir la discordancia.',
     'Ejercicio 3. Henderson–Hasselbalch: 6,1 + log(13/0,72) = 6,1 + 1,257 ≈ 7,36. Los valores no pertenecen a una tríada coherente.'),
    (4, '¿Compensación ventilatoria adecuada?', 'HCO₃⁻ **13**; pCO₂ medida **24** (misma tríada del ej. 3).', '¿La pCO₂ es la esperable para la acidosis metabólica?',
     'Winter: pCO₂ esperada = 1,5 × HCO₃⁻ + 8 ± 2', '1,5 × 13 + 8 = 27,5 → banda 25,5–29,5', '24 < 25,5: **algo por debajo** de lo esperado',
     'Sólo **hipótesis** de alcalosis respiratoria agregada (fiebre, neumonía), **no certeza**, porque la tríada general es inconsistente.',
     'Ejercicio 4. Winter predice 27,5 ± 2; la medida 24 está algo por debajo de la banda. Como la tríada es inconsistente sólo se formula '
     'una hipótesis de alcalosis respiratoria agregada.'),
    (5, 'Anion gap con corrección por albúmina', 'Paciente distinto: Na⁺ **140**, Cl⁻ **102**, HCO₃⁻ **12**, albúmina **2 g/dL**.', '¿Hay aniones no medidos aumentados?',
     'AG = Na⁺ − (Cl⁻ + HCO₃⁻) · AGc = AG + 2,5 × (4 − albúmina)', '140 − (102 + 12) = 26 · 26 + 2,5 × (4 − 2) = 26 + 5', '**AG = 26 · AG corregido ≈ 31 mEq/L**',
     'Aniones no medidos **sustancialmente elevados**: cetonas, lactato, uremia, tóxicos. En los casos 11/12 **no se puede calcular** (faltan Na⁺ y Cl⁻).',
     'Ejercicio 5. AG = 140 − (102 + 12) = 26; corregido por albúmina 2 g/dL: 26 + 2,5 × 2 = 31 mEq/L.'),
    (6, 'Osmolalidad efectiva frente a total', 'Paciente hipotético: Na⁺ **145**, glucosa **684**, BUN **56** (mg/dL).', '¿Cuánto aporta la urea a la tonicidad?',
     'Efectiva = 2 Na⁺ + glucosa/18 · Total = efectiva + BUN/2,8', '2 × 145 + 684/18 = 290 + 38 · 328 + 56/2,8 = 328 + 20', '**Efectiva 328 · total 348 mOsm/kg**',
     'La urea suma **20** a la total pero **no** a la tonicidad sostenida: para el agua intracelular se usa la **efectiva**, no un «325» sin definición.',
     'Ejercicio 6. Efectiva = 2 × 145 + 684/18 = 290 + 38 = 328 mOsm/kg; total = 328 + 56/2,8 = 348.'),
    (7, 'Potasio «normal» en CAD', 'CAD con K⁺ sérico **4,8 mmol/L** y fuerte glucosuria.', '¿Tiene potasio corporal total normal?',
     'K⁺ sérico ≠ K⁺ corporal total (≈ 98 % intracelular)', 'Salida celular (insulinopenia, acidosis, hiperosmolalidad) + pérdidas urinarias y vómitos', '**No necesariamente**: probable déficit total',
     'Al iniciar insulina el K⁺ **cae** por entrada celular: medición **seriada** y reposición guiada.',
     'Ejercicio 7. La diuresis osmótica y los vómitos pueden haber agotado las reservas; al iniciar insulina el potasio puede caer por '
     'movimiento intracelular.'),
    (8, 'Cetonuria más intensa en plena mejoría', 'Tras varias horas de insulina: **β-OHB sanguíneo baja**, pero la **tira urinaria aumenta**.', '¿Fracasó el tratamiento?',
     'β-OHB + NAD⁺ ⇌ acetoacetato + NADH', 'Al mejorar el redox, β-OHB → **acetoacetato** (lo detecta el nitroprusiato)', '**No necesariamente** fracasó',
     'Priorizar la **tendencia del β-OHB**, pH, bicarbonato y clínica; la tira urinaria no define la resolución.',
     'Ejercicio 8. El β-hidroxibutirato se oxida a acetoacetato, el principal detectado por nitroprusiato.'),
    (9, 'EHH con glucosa 700 y sin cetonas', 'Glucemia **700 mg/dL**, cetonas negativas, sin acidosis.', '¿Cómo puede existir tal glucemia sin acidosis?',
     'Umbral antilipolítico de insulina < umbral para captación/supresión de PHG', 'Insulina residual: frena lipólisis/cetogénesis, pero no la PHG ni la resistencia muscular', '**Hiperglucemia extrema sin carga cetoácida**',
     'Predominan la **tonicidad elevada** y la **pérdida de agua** sobre la carga de cetoácidos.',
     'Ejercicio 9. La insulina endógena residual puede inhibir lipólisis y cetogénesis aunque no suprima la producción hepática de glucosa ni '
     'supere la resistencia muscular.'),
    (10, 'IMC, descenso porcentual y GET', 'Varón, 40 años, **170 kg**, **170 cm**; luego **140 kg**.', '¿Se mantiene el GET anterior tras el descenso?',
     'IMC = kg/m² · Mifflin H: 10P + 6,25T − 5E + 5 · GET = GER × 1,2', 'IMC 58,82 · GER 2567,5 · GET ≈ 3081 · 140/2,89 · 30/170', '**IMC 48,44 · descenso 17,65 %**',
     '**No**: cambió la masa (y quizá la actividad); reevaluar con observación y/o medición.',
     'Ejercicio 10. IMC = 58,82; Mifflin reposo 2567,5 kcal/d; GET sedentario ≈ 3081 kcal/d. Tras 140 kg: IMC ≈ 48,44; descenso ≈ 17,65 %. '
     'El GET debe reevaluarse.'),
    (11, 'Síndrome metabólico sin glucemia basal', 'Cintura **124 cm**, TA **160/100**, HDL **30**, TG **185**; ayuno de la glucosa desconocido.', '¿Tiene síndrome metabólico?',
     'Definición armonizada: ≥ 3 de 5 criterios', 'Cintura sí · TA sí · HDL sí · TG sí · glucosa: ¿ayunas?', '**Sí: 4 criterios**',
     'La glucosa aportaría un **quinto** sólo si se comprueba la condición de ayuno.',
     'Ejercicio 11. Sí bajo criterios armonizados: reúne cuatro criterios (cintura, TA, HDL, TG).'),
    (12, 'Elegir fármaco tras una crisis hiperglucémica', 'DM2 con obesidad y trabajo físico variable con **glibenclamida**; omite comidas; mareos con glucosa **52 mg/dL**.', '¿Qué explica la hipoglucemia?',
     'Sulfonilurea → SUR1 → cierre de K_{ATP} **independiente de glucosa**', 'Secreción de insulina aun con glucosa baja + ingesta omitida', '**Hipoglucemia inducida por sulfonilurea**',
     'Corregir la hipoglucemia y **revisar el tratamiento con el equipo**; fármacos de mecanismo **glucosa-dependiente** pueden minimizar el riesgo. **No cambiar por cuenta propia.**',
     'Ejercicio 12. Mecanismo: el cierre de K_ATP estimula la insulina incluso con glucosa baja. Aprendizaje: corregir la hipoglucemia y '
     'revisar el tratamiento con el equipo médico.'),
]

MCQ = [
    (1, '¿Mejor mecanismo de la formación de cetonas en CAD?', ['Más entrada GLUT4 hepático', 'Más AGNE al hígado, β-oxidación y HMGCS2 mitocondrial', 'Inhibición de glucagón', 'Síntesis de glucógeno aumentada'], 1,
     'Secuencia lipólisis → β-oxidación → acetil-CoA → cetonas.'),
    (2, 'En el EHH clásico, la ausencia de cetonemia marcada se explica principalmente por:', ['Mayor excreción de HCO₃⁻', 'Insulina residual que inhibe la lipólisis', 'Menor filtración de glucosa', 'Déficit completo de glucagón'], 1,
     'No alcanza para euglucemia, pero puede frenar la cetogénesis.'),
    (3, 'pH 7,20, HCO₃⁻ 11 y pCO₂ adecuadamente baja corresponde a:', ['Alcalosis metabólica', 'Acidosis respiratoria', 'Acidosis metabólica con compensación respiratoria', 'Alcalosis respiratoria aislada'], 2,
     'Primero pH y componente metabólico; verificar compensación con Winter.'),
    (4, 'La lipoproteína lipasa se diferencia de la HSL porque:', ['Está en lisosomas', 'Hidroliza TAG de QM/VLDL en la superficie capilar', 'Produce HMG-CoA', 'Sólo actúa en hígado'], 1,
     'La HSL participa en la lipólisis intracelular.'),
    (5, 'La adiponectina en obesidad visceral disfuncional suele:', ['Aumentar y empeorar la sensibilidad', 'Disminuir y perder acciones sensibilizantes', 'Ser la principal cetona', 'Inhibir totalmente la β-oxidación'], 1,
     'Señal cardiometabólica relacionada con AMPK/PPARα.'),
    (6, 'La activación de MC4R por α-MSH tiende a:', ['Aumentar el hambre', 'Disminuir la ingesta', 'Liberar glucosa renal', 'Estimular lipólisis pancreática'], 1,
     'Circuito de melanocortinas anorexígeno.'),
    (7, 'En músculo, la contracción mejora la captación de glucosa por:', ['Translocación de GLUT4 parcialmente independiente de insulina', 'Expresión exclusiva de GLUT2', 'Glucosa-6-fosfatasa muscular', 'Inhibición de AMPK'], 0,
     'AMPK y otras señales contráctiles llevan GLUT4 a la membrana.'),
    (8, 'Para diagnosticar SM según la definición armonizada habitual se requiere:', ['IMC ≥ 40 obligatoriamente', 'Tres de cinco criterios', 'Insulina plasmática > 100', 'Diagnóstico previo de DM1'], 1,
     'La circunferencia se ajusta según etnia/población.'),
    (9, 'Una HbA1c de 12 % indica:', ['Promedio exactamente igual a la glucemia actual', 'Glucosilación enzimática aguda', 'Exposición glucémica elevada durante semanas/meses', 'Enfermedad exclusivamente renal'], 2,
     'Con límites por la vida eritrocitaria.'),
    (10, 'Sobre rimonabant en Argentina es correcto que:', ['Es de primera línea', 'Se comercializa sin receta', 'Su comercialización fue suspendida por ANMAT', 'Es inhibidor de lipasa pancreática'], 2,
     'Disposición ANMAT 6238/2008.'),
]


def build(D):
    div(D)
    schemes = ['yellow', 'peach', 'cyanR', 'lime']
    for i, (n, t, da, it, fo, ca, re_, me, nt) in enumerate(EX):
        exercise(D, U, n, t, da, it, fo, ca, re_, me, nt, scheme=schemes[i % 4])
    for k in range(0, 10, 2):
        mcq(D, U, MCQ[k:k + 2], scheme=schemes[(k // 2) % 4], title='Opción múltiple · preguntas %d y %d' % (k + 1, k + 2))
