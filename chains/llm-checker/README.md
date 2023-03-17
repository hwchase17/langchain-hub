# LLMCheckerChain

## Description

The LLMCheckerChain is designed to generate better answers to factual questions. The chain works by first generating a draft answer based on the question. The model is then asked to list its assumptions for this statement. The model is then asked to determine whether each assertion is true or false, and explain why if it is false. Finally, the model is prompted to revise their answer based on the above checks and assertions.

## Chain type

LLMCheckerChain

## Input Variables

question: the question to answer