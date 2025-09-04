# interview-tool
A rework of PeterTKD/interview-tool

# Model use
Model: `gpt-4o`

Moderations: `omni-moderation-latest`

User prompts would be sanitized for potentially harmful content using the [moderations endpoint](https://platform.openai.com/docs/guides/moderation)

We would be streaming responses using `client.responses` instead of `client.chat.completions`, as [recommended by OpenAI](https://platform.openai.com/docs/guides/migrate-to-responses).

## NOTE:

Before deploying the streamlit app, don't forget to set your OpenAI API key in `secrets.toml` and ensure that the key itself is not visible in any public repository.

# Decisions

## Self-hosting vs. using an API
We will proceed with using an API. 
1. While self-hosting could be relevant, it could be more expensive than API usage even using a cloud provider because of massive training data requirements in terms of both monetary costs and compute requirements.
2. Furthermore, we are not having any training data or proprietary use case which makes this a good choice.
3. It is usually better to start with closed-source and then shift to open-source based on project traction when it comes to LLMs. For example, you start with GPT-4o-mini and when the project has a significant user base and niche requirements such as training on proprietary data or when an open-source model would perform much better, we can shift from GPT-4o-mini to an open-source model.

## Open-source vs. closed source models.
We will proceed with closed-sourced GPT-4o.
1. While GPT-5 is OpenAI's latest flagship model, only verified organizations may stream the models. Clearly out of scope for personal use.
2. We have already decided to proceed with an API use as above, hence proceeding with closed-source model.
