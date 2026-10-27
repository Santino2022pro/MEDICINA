# INTEGRACION_METABOLICA_AVANZADA_ANIMADA.pptx

Presentación PowerPoint 16:9 de **224 diapositivas** con formas, textos, tablas y gráficos editables y notas del presentador en todas las diapositivas.

## Contenido
- Portada, índice visual, código visual y mapa general.
- Unidad I (temas 1–6), II (7–12), III (13–24), IV (25–35).
- Unidad V: las 8 patologías, analizadas en 8 etapas (normal → … → esquema comparativo).
- Unidad VI: casos A–F (3 diapositivas cada uno, 8 etapas), red de enzimas reguladoras, 5 preguntas maestras, 12 errores frecuentes, 12 distinciones clave, mapa integrador final, bibliografía y cierre.

## Animaciones (nativas de PowerPoint, guardadas en `p:timing`)
- 208 diapositivas animadas, 1842 efectos: Aparecer, Desvanecer, Barrido, Zoom, Énfasis (crecer/encoger, giro), Salida y **trayectorias de movimiento** (glucosa por GLUT, Ca²⁺ entrando, gránulos y exocitosis, lactato/alanina/glucosa en Cori y glucosa–alanina, LDL en la íntima, NH₄⁺ en el ácino, etc.).
- Todas se disparan por clic; dentro de cada clic hay efectos encadenados («después de la anterior»).

## Transiciones Morph reales (`p159:morph`, 31 diapositivas)
| Secuencia | Diapositivas |
|---|---|
| Destino de glucosa (intestino → porta → hepatocito → G6P) | 13–15 |
| Secreción de insulina (célula β, pasos 1–10) | 22–28 |
| Señal de insulina (organismo → hígado → hepatocito → membrana → receptor → señalización) | 36–41 |
| Hígado por fases (tablero) | 76–79 |
| Adaptación al ayuno (reservas: alimentado → 8–12 h → 24–48 h → >3 días) | 80–83 |
| Malonil-CoA: escenario alimentado → ayuno/ejercicio | 90–91 |
| Metabolismo lipídico (adipocito → gota → lipólisis → sangre → músculo → mitocondria) | 97–101 |
| Cetogénesis (hígado → mitocondria → cuerpos cetónicos → tejidos → cetólisis) | 126–129 |
| Nitrógeno (músculo → AA → hígado/urea → riñón → excreción) | 139–143 |

Los objetos que se transforman llevan nombres con el prefijo `!!` (coincidencia forzada de Morph). Cada transición incluye un respaldo «Desvanecer» para versiones sin Morph (PowerPoint 2016 sin suscripción, LibreOffice).

## Tipografía
Familia **Bahnschrift** (Windows 10/11 y Microsoft 365): títulos en Bahnschrift SemiBold Condensed, texto en Bahnschrift. Subíndices y superíndices (NAD⁺, FADH₂, Ca²⁺, NH₄⁺, HCO₃⁻) se escriben con formato de línea base, no con caracteres especiales, para evitar cuadros vacíos. En macOS sin Bahnschrift, PowerPoint sustituirá la fuente: conviene instalarla o reemplazarla desde *Diseño → Fuentes*.

## Verificación realizada
- Las 224 diapositivas validan contra el esquema PresentationML (ISO/IEC 29500) incluida la estructura de animación.
- Sin identificadores duplicados, todos los destinos de animación existen.
- Revisión visual de todas las diapositivas renderizadas (LibreOffice). LibreOffice no reproduce Morph ni animaciones: conviene una pasada final en PowerPoint de escritorio.

## Regenerar
```
python3 generador/build.py
```
