# Bioquímica clínica y metabolismo — de los mecanismos moleculares a la interpretación del laboratorio

**Archivo principal:** `BIOQUIMICA_CLINICA_Y_METABOLISMO.pptx` (16:9, 270 diapositivas, totalmente editable).

## Entregables

| N.º | Entregable | Archivo |
|---|---|---|
| 1 | PowerPoint final | `BIOQUIMICA_CLINICA_Y_METABOLISMO.pptx` |
| 2 | Animaciones internas nativas | dentro del PPTX (`p:timing`): 2147 efectos en las 270 diapositivas |
| 3 | Mapa de Morph | `ENTREGABLE_3_MAPA_MORPH.md` (14 secuencias) |
| 4 | Guion de animaciones | `ENTREGABLE_4_GUION_ANIMACIONES.md` y `.csv` (diapositiva, clic, objeto, efecto, duración, disparador) |
| 5 | Índice académico | `ENTREGABLE_5_INDICE_ACADEMICO.md` |
| 6 | Revisión científica | `ENTREGABLE_6_REVISION_CIENTIFICA.md` (42 observaciones) |
| 7 | Archivo editable | todas las ilustraciones son formas nativas agrupadas (sin imágenes aplanadas); textos, tablas y flechas son independientes |

## Estructura

| Unidad | Diapositivas | Contenido |
|---|---|---|
| Introducción | 1–4 | portada, mapa, hilo conductor, código visual |
| I · Variables bioquímicas | 5–54 | variables, sangre, unidades, **Morph suero/plasma** (27–35), S/E, VPP/VPN, precisión/exactitud, intervalos de referencia, control de calidad, integración A |
| II · Termodinámica y metabolismo | 55–114 | ΔH, ΔS, ΔG, **Morph reacción acoplada** (65–70), sistemas, redox, NAD/FAD, catabolismo/anabolismo, acetil-CoA, piruvato, **Morph ingreso a la mitocondria** (93–95), PDH en 10 clics (97), **Morph PDH** (98–107), **Morph regulación** (109–110) |
| III · Anemias | 115–177 | Hb, **Morph volumen plasmático** (119–121), índices, clasificaciones, tabla integradora, megaloblástica (**Morph** 143–145), **Morph absorción de B12** (147–155), biomarcadores, casos 1 y 2, integración C |
| IV · IAM | 178–221 | caso inicial progresivo, criterios, **Morph fisiopatología** (184–187), ECG, biomarcadores, **Morph liberación** (201–208), curvas de cinética, reinfarto, **Morph seguimiento a 8 días** (216–217), integración D |
| V · Hepatopancreático | 222–267 | transaminasas (**Morph hepatocito** 225–227), De Ritis, FAL, GGT, bilirrubina, **Morph colestasis** (235–237), amilasa, lipasa, zimógenos, **Morph pancreatitis** (244–253), casos 3 y 4, diagnóstico diferencial, integración E |
| Cierre | 268–270 | integración B, mapa integrador, cierre |

## Morph
Los objetos que se transforman llevan el prefijo `!!` (coincidencia forzada) y son únicos dentro de cada diapositiva. Ya dejé aplicada la transición **Transformación (Morph)** en las diapositivas 2…n de cada secuencia, con respaldo «Desvanecer» para PowerPoint sin Morph. Podés quitarla o volver a aplicarla desde *Transiciones*.

Dentro de las secuencias Morph, los objetos que pasan de una diapositiva a la siguiente **no** tienen animaciones de entrada, trayectoria ni salida (solo énfasis), para que no haya «saltos». El movimiento lo hace Morph.

## Tipografía
- Títulos: **Segoe Print** en negrita, azul oscuro (equivalente manuscrito disponible en Windows/Office). En macOS sin Segoe Print, reemplazala desde *Diseño → Variantes → Fuentes* por otra letra manuscrita gruesa.
- Texto: **Calibri**. Subíndices y superíndices (NAD⁺, FADH₂, Ca²⁺, B₁₂) se escriben con formato de línea base, no con caracteres especiales.

## Verificación realizada
- Validación del esquema OOXML (`validate.py`): **aprobada**.
- Sin identificadores duplicados; todas las animaciones apuntan a objetos existentes; sin nombres `!!` repetidos en una misma diapositiva.
- Render completo con LibreOffice e inspección visual de todas las diapositivas. **LibreOffice no reproduce Morph ni las animaciones y sustituye Segoe Print**: conviene hacer una pasada final en PowerPoint de escritorio.

## Regenerar
```
python3 generador/build.py
```
