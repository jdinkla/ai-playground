# ai-playground

Install with `init.sh`


```shell
$ export OPENAI_API_KEY=""
```


- [OpenAI](https://platform.openai.com/docs/introduction)


[Easiest Way to Use GPT In Your Products | LangChain Basics Tutorial](https://www.youtube.com/watch?v=fLy0VenZyGc)


## Issues

docarray needs an old version of pydantic (at the time of writing)

    $ pip install pydantic==1.10.9
    $ python src/langchain_rag.py
    $ pip install -U pydantic

See also the [langchain wiki](https://python.langchain.com/docs/guides/pydantic_compatibility).

