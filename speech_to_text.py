from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

def extract_speech(audio_path, text_path):
    # Carregue o modelo e o processador
    processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")
    #model.cuda()

    # Configure o decoder para traduzir do inglês para o português brasileiro
    forced_decoder_ids = processor.get_decoder_prompt_ids(language="portuguese", task="translate", no_timestamps=False)
    #print(forced_decoder_ids)


    # Carrega o áudio usando librosa (obtendo a taxa de amostragem automaticamente)
    # Certifique-se de que o áudio esteja em inglês!
    audio, sampling_rate = librosa.load(audio_path, sr=16000) # Reamostra para 16kHz
    #print(sampling_rate)

    # Pré-processa o áudio
    input_features = processor(audio, sampling_rate=sampling_rate, return_tensors="pt").input_features

    # Gera a tradução
    predicted_ids = model.generate(input_features, forced_decoder_ids=forced_decoder_ids)

    # Decodifica a transcrição para texto
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

    # Imprime a tradução para o português
    #print(transcription[0])  # Deve ser a tradução do áudio em inglês para português
    print(transcription)
    with open(text_path, "w") as f:
        f.write(transcription[0])
