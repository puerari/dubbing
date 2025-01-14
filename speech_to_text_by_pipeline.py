from transformers import pipeline, AutoProcessor
import librosa
import torch


def extract_speech_by_pipeline(audio_path, text_path):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model_id = "openai/whisper-large-v3"

    processor = AutoProcessor.from_pretrained(model_id)

    # Carregue o modelo e o processador
    whisper = pipeline(
        "automatic-speech-recognition",
        model_id,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device,
        return_timestamps=True
    )

    # transcription = whisper(audio_path, return_timestamps=False)
    # transcription = whisper(audio_path, generate_kwargs={"language": "portuguese", "task": "translate"})
    transcription = whisper(audio_path)


    # Imprime a tradução para o português
    # print(transcription[0])  # Deve ser a tradução do áudio em inglês para português
    print(transcription)
    with open(text_path, "w") as f:
        f.write(transcription["text"])
