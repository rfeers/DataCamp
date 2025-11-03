"""
************** 04 AGENT WITH PROMPT USING CSDKClient() *******************************************************
Advanced example using the model with ClaudeSDKClient() and a specific tool. 
"""


from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AssistantMessage, ToolUseBlock
from rich import print
import asyncio

MODEL="haiku"

async def create_project():
    options = ClaudeAgentOptions(
        model = MODEL,
        allowed_tools=["Read", "Write", "Bash"],
        permission_mode='acceptEdits',
        cwd="/Users/josepferrersanchez/PRO/DataCamp/claude_agent_SDK"
    )

    # ****************************************************** First question
    # input prompt
    input_prompt = "Create a Python project structure with setup.py contained in a dummy_project_2 folder."
    print(f"User: {input_prompt}")

    async with ClaudeSDKClient(options=options) as client:

        # Send a query
        await client.query(input_prompt)

        # Receive messages including ResultMessage
        async for message in client.receive_response():
            print(message) 
    
    # ****************************************************** Follow-up question
    # input prompt 
        input_prompt = "Now change the name of the folder to python_project."
        print(f"User: {input_prompt}")

        # Send a query
        await client.query(input_prompt)

        # Receive messages including ResultMessage
        async for message in client.receive_response():
            print(message) 

asyncio.run(create_project())