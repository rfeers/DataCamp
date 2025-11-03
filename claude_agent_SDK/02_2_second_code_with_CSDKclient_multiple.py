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
    
    # ****************************************************** First question
    # input prompt
    input_prompt = "What's the capital of France?"
    print(f"User: {input_prompt}")

    async with ClaudeSDKClient(options=options) as client:

        # Send a query
        await client.query(input_prompt)

        # Receive messages including ResultMessage
        async for message in client.receive_response():
            print(message) 
    
    # ****************************************************** Follow-up question
    # input prompt 
        input_prompt = "What's the population of that city?"
        print(f"User: {input_prompt}")

        # Send a query
        await client.query(input_prompt)

        # Receive messages including ResultMessage
        async for message in client.receive_response():
            print(message) 
        
    # ****************************************************** Final follow-up question
    # input prompt 
        input_prompt = "What are some famous landmarks there?"
        print(f"User: {input_prompt}")

        # Send a query
        await client.query(input_prompt)

        # Receive messages including ResultMessage
        async for message in client.receive_response():
            print(message) 


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())