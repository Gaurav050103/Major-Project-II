from transformers import MarianMTModel, MarianTokenizer
import torch

def translate_segments(segments, target_lang="hi"):
    model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
    print(f"[MarianMT] Initializing transformer architecture: {model_name}")
    
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    translated_segments = []
    
    for seg in segments:
        text = seg["text"]
        if not text:
            continue
            
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        with torch.no_grad():
            translated_tokens = model.generate(**inputs)
        
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        translated_segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": translated_text
        })
        print(f"[Translation Engine] Map ({seg['start']}s - {seg['end']}s) -> {translated_text}")
        
    return translated_segments