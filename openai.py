import config
import openai

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        temperature=1
    )

    response_dict = response.get("choice")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]("text")
    return prompt_response
