import openai

# Set OpenAI API Key
openai.api_key = "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"

def summarize_paper(abstract):
    prompt = f"Summarize the following research paper abstract:\n\n{abstract}"

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()
