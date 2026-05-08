import json

def get_llm_response(client, *, system_prompt='', few_shot_prompt='', user_prompt='', model='qwen3-max', stream=False):
    messages = []
    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
    if few_shot_prompt:
        messages += json.loads(few_shot_prompt)
    if user_prompt:
        messages.append({'role': 'user', 'content': user_prompt})

    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    if not stream:
        return resp.choices[0].message.content
    return resp
