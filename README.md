# 🚗 Procesamiento de imágenes con OpenCV

Ejemplo práctico de cómo se aplicó en el taller el procesamiento de imágenes con Python y OpenCV. El programa toma una fotografía, la redimensiona, la convierte a escala de grises y resalta sus bordes con el algoritmo **Canny**.

## ⚙️ Instalación

Requiere Python 3.8 o superior.

```bash
git clone https://github.com/jhederith/sistemas_multiagente.git
cd sistemas_multiagente
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Uso

La imagen de ejemplo se encuentra en `media/bmw.jpg`. Ejecuta:

```bash
python main.py
```

Se abrirán dos ventanas: la imagen original redimensionada y la imagen procesada con los bordes detectados. Presiona cualquier tecla dentro de una ventana para cerrar el programa.

## 🧪 ¿Qué se practicó?

- Lectura y validación de una imagen.
- Redimensionamiento para facilitar su procesamiento.
- Conversión a escala de grises.
- Detección de bordes con Canny.
- Visualización del resultado con OpenCV.

> Este repositorio funciona como una demostración sencilla y reproducible de la práctica realizada durante el taller.
