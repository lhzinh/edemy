from langchain.chat_models import init_chat_model


def call_model(model="gemini-3.5-flash", provider="google-genai"):
    return init_chat_model(
        model=model,
        model_provider=provider,
        temperature=0,
        timeout=600,
        max_tokens=25000,
        streaming=True,
    )
