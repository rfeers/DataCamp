"""
************** 01_2 FIRST CODE USING QUERY()*******************************************************
Basic example of querying with the Claude Agent SDK using the query() command. 

Use `query()` for one-off questions, independent tasks, new sessions each time.
You can think about a single-shot query, where there's no persistance between different queries. 

For more details, see: https://docs.claude.com/en/api/agent-sdk/python#choosing-between-query-and-claudesdkclient

We will import print from rich to better understand the messages we see in the terminal.
"""

from claude_agent_sdk import query, ClaudeAgentOptions
from rich import print

MODEL="haiku"

async def main():
    # Use ClaudeAgentOptions to configure the agent's behavior -> we define the model haiku
    options = ClaudeAgentOptions(
        #system_prompt="You are a website help assistant.",
        #permission_mode='acceptEdits',
        #cwd="/Users/josepferrersanchez/PRO/DataCamp/claude_agent_SDK",
        model=MODEL
        )

    # input prompt
    input_prompt = "Hello!"
    print(f"User: {input_prompt}")

    async for message in query(prompt=input_prompt, options=options):
        print(message)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())