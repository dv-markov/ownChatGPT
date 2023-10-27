import asyncio
import g4f

_providers = [
    # g4f.Provider.Aichat,
    # g4f.Provider.ChatBase,
    # g4f.Provider.Bing,
    # g4f.Provider.GptGo,
    # g4f.Provider.You,
    # g4f.Provider.Yqcloud,
    g4f.Provider.AItianhu,
    g4f.Provider.AItianhuSpace,
    g4f.Provider.AiAsk,
    g4f.Provider.ChatBase,
    g4f.Provider.ChatgptX,
    g4f.Provider.FreeGpt,
    g4f.Provider.GPTalk,
    g4f.Provider.GptForLove,
    g4f.Provider.GptGo,
    g4f.Provider.Llama2,
    g4f.Provider.NoowAi,
    # g4f.Provider.OpenaiChat,
    g4f.Provider.You,
]


async def run_provider(provider):
    try:
        response = await g4f.ChatCompletion.create_async(
            # model=g4f.models.default,
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())
