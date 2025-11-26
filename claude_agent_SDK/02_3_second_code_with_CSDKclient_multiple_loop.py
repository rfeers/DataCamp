"""
************** 02_2 USING CLAUDESDKCLIENT() WITH MULTIPLE PROMPTS *******************************************************
Basic example of querying with the Claude Agent SDK using the ClaudeSDKClient() command. 

Use `ClaudeSDKClient` for continuous conversations and stateful sessions.It persist the interactions. 

For more details, see: https://docs.claude.com/en/api/agent-sdk/python#choosing-between-query-and-claudesdkclient 
"""

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
from rich import print

MODEL="haiku"

async def main():
    # Use ClaudeAgentOptions to configure the agent's behavior -> we define the model haiku
    options = ClaudeAgentOptions(
        model=MODEL
        )

    async with ClaudeSDKClient(options=options) as client:
        for prompt in [
            "What's the capital of France?",
            "What's the population of that city?",
            "What are some famous landmarks there?"
        ]:
            await client.query(prompt)
            async for message in client.receive_response():
                print(message)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())