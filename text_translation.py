from transformers import T5Tokenizer, T5ForConditionalGeneration

def translate_text(caminho_do_texto, caminho_da_traducao, task_prefix="Translate text from English to Brazilian Portuguese: "):
    try:
        # 1. Load the T5-base model and tokenizer
        tokenizer = T5Tokenizer.from_pretrained("t5-base", legacy=False)
        model = T5ForConditionalGeneration.from_pretrained("t5-base")

        # 2. Read the text from the file
        with open(caminho_do_texto, "r", encoding="utf-8") as file:
            input_text = file.read()

        # 3. Preprocess the input
        input_ids = tokenizer(task_prefix + input_text, return_tensors="pt").input_ids

        # 4. Generate the output
        output_ids = model.generate(input_ids, max_length=150, num_beams=4, early_stopping=True)

        # 5. Decode the generated output
        output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # 6. Print and optionally save the output
        print(f"Input Text:\n{input_text}\n")
        print(f"Generated Text:\n{output_text}")

        if caminho_da_traducao:
            with open(caminho_da_traducao, "w", encoding="utf-8") as outfile:
                outfile.write(output_text)
            print(f"\nTranslated text saved to {caminho_da_traducao}")

    except FileNotFoundError:
        print(f"Error: File not found at {caminho_do_texto}")
    except Exception as e:
        print(f"An error occurred: {e}")
