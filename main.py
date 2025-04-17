import gradio as gr
import easyocr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator
from PIL import Image

# Inicializar el lector OCR
reader = easyocr.Reader(['es', 'en'])

# Cargar el modelo y el tokenizador para análisis de emociones
tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")
model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-emotion")

# Función para detectar emoción
def detectar_emocion(texto):
    if not texto.strip():
        return "❌ No se detectó texto para analizar."

    # Traducir al inglés
    texto_en = GoogleTranslator(source='auto', target='en').translate(texto)
    
    # Generar emoción
    entrada = tokenizer.encode(f"emotion: {texto_en}", return_tensors="pt")
    salida = model.generate(entrada, max_length=20)
    emocion_en = tokenizer.decode(salida[0], skip_special_tokens=True)

    # Traducir la emoción al español si es necesario
    emocion_esp = GoogleTranslator(source='en', target='es').translate(emocion_en).capitalize()

    return f"🧠 Este texto transmite una sensación de: **{emocion_esp}**"

# Función principal
def analizar_imagen(imagen):
    # OCR con EasyOCR
    resultado = reader.readtext(imagen, detail=0)
    texto_extraido = " ".join(resultado)

    if not texto_extraido.strip():
        return "❌ No se encontró texto en la imagen.", ""

    emocion = detectar_emocion(texto_extraido)
    return texto_extraido, emocion

# Interfaz de Gradio
gr.Interface(
    fn=analizar_imagen,
    inputs=gr.Image(type="filepath", label="Sube una imagen con texto"),
    outputs=[
        gr.Textbox(label="📝 Texto extraído"),
        gr.Textbox(label="💬 Análisis emocional")
    ],
    title="🖼️ Transcriptor de Imagenes",
    description="Este sistema detecta el texto de una imagen y te dice qué emoción transmite (como alegría, tristeza, amor, etc.)."
).launch()
