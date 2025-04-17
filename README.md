# Proyecto-final-transcriptor-de-imagenes-
# 🖼️ Transcriptor y Analizador de Emociones desde Imágenes

Este proyecto es una aplicación interactiva creada con **Gradio** que utiliza **OCR (EasyOCR)** para extraer texto de imágenes y un modelo de **Deep Learning (T5 fine-tuned for emotion detection)** para identificar las emociones que transmite ese texto. Además, se traduce automáticamente cualquier texto extraído para permitir un análisis preciso con modelos preentrenados en inglés.

---

## 🚀 Funcionalidades

- 📤 **Sube una imagen** con texto (impreso o manuscrito).
- 🔍 **Detecta el texto** dentro de la imagen usando OCR.
- 🧠 **Analiza las emociones** que transmite el contenido textual.
- 🌐 **Traduce automáticamente** entre idiomas para entender mejor el texto.
- 🧾 Resultado claro y en español que indica emociones como: alegría, tristeza, amor, enfado, miedo, entre otros.

---

## 🧰 Tecnologías Utilizadas

| Tecnología      | Uso principal                               |
|----------------|----------------------------------------------|
| `Gradio`        | Interfaz gráfica para usuario                |
| `EasyOCR`       | OCR para reconocimiento de texto en imágenes |
| `Transformers`  | Modelo preentrenado T5 para emociones        |
| `Hugging Face`  | Plataforma de modelos de IA                  |
| `Deep Translator` | Traducción automática de texto               |
| `PIL`           | Manejo básico de imágenes                    |
| `Python 3.8+`   | Lenguaje base del proyecto                   |

---

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

## Instala las dependencias necesarias:

pip install gradio easyocr transformers deep-translator torch

## Ejecuta la aplicación:
python main.py

## Requisitos
Python 3.8 o superior

Conexión a Internet (para descargar el modelo y traducir)

Sistema operativo compatible (Windows, Linux, macOS)

## 📝 Ejemplo de uso
Al ejecutar la app, se abrirá una interfaz web local.

Sube una imagen que contenga texto.

La aplicación:

Extraerá el texto.

Lo analizará con un modelo de emociones.

Mostrará el texto y la emoción detectada en pantalla.

## 📌 Nota
Este sistema no detecta emociones directamente desde imágenes sin texto. Está orientado a imágenes que contienen mensajes, frases, o textos emocionales.

## 📝 Créditos

- **Desarrollo**: Yuleisy Carmona Vasquez (22-SISN-2-016)
- **Materia**: Inteligencia Artificial
