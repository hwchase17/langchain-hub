# Zero-Shot Intent Classifier

This is probably going to sound archaic in a few months, but a lot of "home assistant" type devices right now use 
a technique called "slot filling" under the hood. An "intent" classifier is the component that figures out what the relevant slots are 
and 'fills' them with values, resulting in a command being emitted and arguments passed. 
Instead of training one bespoke: you can probably just use this directly with no or very little modification.

## Use

    from langchain.chains import load_chain

    chain = load_chain("lc://chains/zero-shot-intent-classifier/chain.json")
    chain.run("how would I drive from my home to SeaTac airport?")
    ## {'intent': 'get_directions', 'arguments': {'start_location': 'home', 'end_location': 'SeaTac airport'}}

## Compiled Prompt

> Act as the intent classification component of a home assistant, similar to Amazon Alexa.  
> Common intents include: play_internet_radio, play_song_by_artist, get_weather, current_time, set_timer, remind_me  
> You receive input in json format: `{"input":...}`  
> You respond in json format: `{"intent":..., "arguments":{ ... }, }}`  
> {"input":`{spoken_request}`}
