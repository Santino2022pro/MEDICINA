# ENFERMEDADES_PLEURALES_ANIMADA.pptx

Presentación universitaria de Medicina Interna y Fisiopatología Respiratoria sobre **enfermedades pleurales**. Es un PowerPoint 16:9 de **262 diapositivas**, completamente editable: formas, textos, flechas, recuadros y tablas son objetos nativos, y no hay diapositivas aplanadas en una imagen.

## Entregables

| # | Archivo | Contenido |
|---|---|---|
| 1 | `ENFERMEDADES_PLEURALES_ANIMADA.pptx` | La presentación. |
| 2 | (dentro del PPTX) | Animaciones internas **nativas**: 1078 efectos en 250 diapositivas. |
| 3 | `MAPA_MORPH.md` | Intervalos de diapositivas preparados para Morph, con objetos reutilizados y transformación esperada. |
| 4 | `GUION_ANIMACIONES.md` / `.csv` | Diapositiva · objeto · efecto · orden (clic) · duración · disparador, efecto por efecto. |
| 5 | `INDICE_ACADEMICO.md` | Correspondencia entre los apartados de ambos apuntes y las diapositivas. |
| 6 | `AUDITORIA_CIENTIFICA.md` | Discrepancias, simplificaciones y datos para verificar (afirmación original, fuente, motivo, corrección propuesta). |

## Estructura (19 unidades)

La presentación abre con la portada, el índice, el código visual y el concepto de síndrome, y sigue con estas unidades:

- I: Anatomía y fisiología
- II: Starling
- III: Mecanismos del derrame
- IV: Trasudado y exudado
- V: Etiologías
- VI: Semiología del derrame
- VII: Imágenes del derrame
- VIII: Toracocentesis
- IX: Criterios de Light
- X: Análisis del líquido
- XI: Paraneumónico y empiema
- XII: Neumotórax
- XIII: Semiología comparada
- XIV: Ecografía
- XV: Radiografía y TAC del neumotórax
- XVI: Neumotórax a tensión
- XVII: Drenaje y sello de agua
- XVIII: Tumores
- XIX: Integración y cierre

Los rangos exactos de diapositivas están en `INDICE_ACADEMICO.md`.

## Identidad visual (tomada del modelo «Ontogenia»)

- **Recuadros:** etiqueta de sección blanca con borde negro y barra de título celeste pálido con viñeta, como en la referencia. Los recuadros planos de colores intensos (celeste, verde, rojo, amarillo, naranja, turquesa) llevan contorno negro grueso.
- **Fondos:** fondos anatómicos desenfocados en la carpeta `generador/fondos/`: tórax colorido, azul medio con un pulmón gigante y membranas, mesotelio en empedrado, parénquima rosado y blanco con formas orgánicas.
- **Tipografía:** la manuscrita gruesa **Mali** (licencia SIL OFL 1.1, texto en `generador/fuentes/OFL.txt`) reemplaza a «Readson» de la referencia, que no es libre. **Va incrustada en el PPTX** (`ppt/fonts`, en formato EOT, el que usa PowerPoint). Si un equipo no la muestra, se instalan `generador/fuentes/Mali-Regular.ttf` y `Mali-Bold.ttf`.
- **Código anatómico constante:** pleura parietal en verde azulado, visceral en morado, trasudado celeste, exudado ámbar, pus amarillo, sangre roja y aire casi blanco con borde punteado.
- **Ilustraciones:** todas son originales y se construyen con formas vectoriales nativas. Se dibujan el tórax completo, el corte de la pared con ambas hojas, el capilar de Starling, la radiografía esquemática (con **la misma geometría** que la ilustración), la TAC axial, la ecografía en modo B y M, el sello de agua, los tubos de laboratorio, el riñón, el abdomen y las manos del examinador.

## Texto e interlineado

- Cada párrafo lleva **interlineado exacto en puntos** (1,22 × tamaño de letra, o un poco menos en títulos). PowerPoint en Windows y Mac, Google Slides y LibreOffice lo aplican igual, sin depender de las métricas de la fuente.
- La Mali original declara métricas verticales «Win» enormes (2,12 em) para cubrir el tailandés. Con ellas Office puede separar mucho las líneas. Por eso la versión incluida unifica las métricas (1050/270 unidades); cubre todos los caracteres latinos que usa la presentación. Las versiones sin modificar están en `generador/fuentes/originales/`.
- El tamaño de letra de cada recuadro se ajusta midiendo cada tramo con su peso real (regular o **negrita**). Si una palabra no cabe en el ancho del recuadro, se reduce la letra para que PowerPoint no la corte a la mitad.
- Si editás un recuadro y agrandás la letra, ajustá también el interlineado desde *Párrafo → Interlineado*, porque queda fijo en puntos.

## Morph

Cada secuencia reutiliza **el mismo modelo anatómico**: el tórax se recalcula con otro estado (líquido, aire, colapso, mediastino, cavas) y conserva los mismos nombres de objeto con el prefijo `!!`, que se pueden ver en *Inicio → Organizar → Panel de selección*.

Aunque no era obligatorio, **la transición Morph ya está aplicada** en 137 diapositivas, con respaldo «Desvanecer» para versiones sin Morph. Si preferís aplicarla a mano, seleccioná esas diapositivas y elegí otra transición en *Transiciones*. Los intervalos están en `MAPA_MORPH.md`.

## Animaciones internas

Las animaciones están configuradas en el nodo `p:timing` de cada diapositiva:

- **Entradas:** aparecer, desvanecer, barrido y zoom.
- **Énfasis:** pulso.
- **Salida.**
- **Trayectorias de movimiento:** deslizamiento de la hoja visceral, percusión, pulso ultrasónico y eco, aguja de toracocentesis, aire que viaja por el tubo de drenaje, burbujas, columna de agua del sello y desplazamiento del émbolo.

Cada clic introduce un concepto. Dentro de cada clic, los efectos «con la anterior» y «después de la anterior» completan la secuencia automática. Duraciones: 300-700 ms para las entradas y 700-1200 ms para los movimientos.

## Verificación realizada

- 262 diapositivas sin identificadores duplicados, con todos los destinos de animación existentes y con nombres `!!` únicos dentro de cada diapositiva.
- Control automático al generar (`build.py`): no se admite interlineado proporcional; el interlineado y los tamaños de letra deben estar en rango, todo el texto debe caber en su recuadro y la fuente incrustada debe ser EOT válido. La generación se detiene si falla.
- Revisión visual de todas las diapositivas renderizadas con LibreOffice. LibreOffice **no reproduce Morph ni la mayoría de las animaciones**, así que conviene una pasada final en PowerPoint de escritorio (Microsoft 365) antes de la clase.
- Búsqueda de expresiones prohibidas («el docente», «según el apunte», nombres de autores, inteligencia artificial): no figuran en el texto de las diapositivas. Las discrepancias se rotulan «en revisión» y se detallan en la auditoría.

## Regenerar

```bash
pip install python-pptx lxml pillow shapely fonttools
```

```bash
python3 pleura/generador/build.py
```
