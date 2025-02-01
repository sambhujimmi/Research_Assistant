import openai
import os


client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_paper(abstract):
    prompt = f"Summarize the following research paper abstract:\n\n{abstract}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant that summarizes research paper abstracts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    return response.choices[0].message.content.strip()
