# groq_api_key="TO BE REPLACED"


import os


from groq import Groq


def prepare_message(system_prompt=str, user_prompt=str) -> list:

    msg = []
    # msg.append({"role":"Assistant", "content": system_prompt})
    msg.append({"role": "user", "content": user_prompt})

    return msg


def generate_response(system_prompt=str, user_prompt=str, model=str):
    # print(model, system_prompt, user_prompt)

    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=prepare_message(system_prompt, user_prompt),
        model=model,
    )

    return chat_completion.choices[0].message.content