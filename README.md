# ai-playground

This project contains my examples exploring the APIs of [OpenAI](https://platform.openai.com/playground) 
and [langchain](https://python.langchain.com/docs/get_started/introduction).

The `src` folder contains example scripts.

Some of these scripts need command line arguments. You can call the program with the `-h` flag to get an explanation. For example

    $ python src/openai_dialogue.py -h                          
    usage: openai_dialogue.py [-h] filename turns [{gpt-3.5-turbo-1106,gpt-4-32k-0613,gpt-4-1106-preview}]

    positional arguments:
    filename              the name of a json file
    turns                 the number of turns
    {gpt-3.5-turbo-1106,gpt-4-32k-0613,gpt-4-1106-preview}
                            the OpenAI model

    options:
    -h, --help            show this help message and exit

There are the following examples

| File  | Description |
| ------------- | ------------- |
| langchain_chain.py  | Example for chain |
| langchain_conversation_chain.py | Example for a conversation |
| langchain_llm.py | Simple example  |
| langchain_prompt_text2image.py | Example for prompt |
| langchain_rag.py | Example for chain with retrieval |
| langchain_rag_extended.py | Example for querying text with RAG  |
| openai_chat.py | Example for chat |
| openai_completion.py | Example for completion  |
| openai_detective.py | Solve a mystery, test for GTP4.5 Turbo |
| openai_dialogue_generic.py | Create a dialogue, see below |
| openai_image.py | Create an image from a prompt |
| openai_speak.py | Create audio from a prompt |

## Creating dialogues

A more advanced example is the creation of dialogues of two or more agents.
The scene of a dialog can be specified in a `yaml` or `json` file. See the `examples` folder.

The following example is specification of a scene.

```yaml
description: >
  This is the balcony scene similiar to 'Romeo and Juliet' by William Shakespeare but in 2023.
  Do not say more than 4 sentences.
persons:
- name: Romeo
  prompt: You are Romeo but more like a gangsta rapper, you speak short and precise. You want a date with Juliet.
  voice: onyx
- name: Juliet
  prompt: You are Julie but more like a Curt Cobain and you do not like to talk much.
  voice: nova
```

And this is an example session


    $ python src/openai_dialogue.py examples/modern_romeo_and_juliet.yaml 2 "gpt-4-1106-preview"
    ----------------------------------------------------
    [Romeo] Yo, Jules, peepin' ya still, queen of my world – fly high in them skies.
    Light it up, my night’s delight; how 'bout we roll, just you and I?
    Words ain’t enough, babe, gotta show; let's bounce, hit the town, it's our time.
    Drop a pin, I’ll scoop you fast; together, we'll set this night on fire, make it sublime.

    ----------------------------------------------------
    [Juliet] Yeah, it's me. What's up?

    ----------------------------------------------------
    Yo, Jules, it's me, 'Romeo';
    I'm down here dreamin' 'bout us, solo.
    Holla at your window, let's not wait,
    Slide down, girl, it's fate – don't be late.

    ----------------------------------------------------
    [Juliet] Not much to say; let's flee the talk.
    Beneath your pane, I'll meet you—walk?
    This night's ours, no need for light.
    Let's vanish, just feels right.

## Installation

Install with

    $ ./init.sh

Set the OPENAI-API key.

    $ export OPENAI_API_KEY="<INSERT-YOUR-KEY-HERE>"

## Issues

### docarray needs old version of pydantic

The examples for RAG use `docarray` and this needs an old version of pydantic (at the time of writing).

    $ pip install pydantic==1.10.9
    $ python src/langchain_rag.py

Install the new version again with.

    $ pip install -U pydantic

See also the [langchain wiki](https://python.langchain.com/docs/guides/pydantic_compatibility).

