# Claude Agent SDK — DataCamp Tutorial

This repository contains the example scripts used in the DataCamp tutorial **“From Claude Code to Claude Agent SDK”**.  
You’ll learn how to build and extend your own Claude agents using the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/python), from simple prompts to multi-tool autonomous loops.

---

## 🧰 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-repo>/claude-agent-sdk-tutorial.git
cd claude-agent-sdk-tutorial
```

### 2. Create your virtual environment `.venv`
After navigating to the directory where you want your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Dependencies
- **Python 3.10+** (you’re already using it if the venv was created)
- **Node.js 18+** (needed for Claude Code CLI)
- **Claude Code CLI**:  
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```
  This installs the `claude` CLI on your computer.

Install the Python dependencies:
```bash
pip install claude-agent-sdk rich
```

If you plan to use **Playwright MCP** (for browser automation), also install:
```bash
npm install -g @playwright/mcp
```

### 4. Set your Anthropic API key
Create a `.env` file in your project root containing your Anthropic API key:

```bash
ANTHROPIC_API_KEY=sk-yourkeyhere
```

### 5. Verify installation
Run a quick query test to confirm everything works:

```bash
python 01_1_first_code_with_query.py
```

---

## 📚 Script Overview

| File | Description |
|------|--------------|
| **01_1_first_code_with_query.py** | Minimal example using `query()`. Sends a one-off prompt (“Hello!”) and prints Claude’s response. |
| **01_2_first_code_with_query_rich.py** | Same as above, but with [`rich`](https://github.com/Textualize/rich) for styled terminal output. |
| **02_1_second_code_with_CSDKclient.py** | Demonstrates `ClaudeSDKClient()` for stateful sessions. The client persists context across turns. |
| **02_2_second_code_with_CSDKclient_multiple.py** | Multi-turn conversation: the agent remembers earlier messages (capital of France → population → landmarks). |
| **03_agent_with_tool_with_query.py** | Adds tool use (`Read`, `Write`, `Bash`) to let Claude interact with the local environment while using `query()`. |
| **04_agent_with_tool_with_CSDKclient.py** | Stateful agent with tools — shows how Claude iteratively edits files (e.g., renaming a generated project folder). |
| **05_conversation_loop.py** | A fully interactive console loop. Type messages and chat with Claude using `Read`, `Write`, `WebSearch`, and `WebFetch` tools. |
| **06_agent_with_mcp.py** | Advanced setup using **MCP (Model Context Protocol)** to connect to external tools. Demonstrates browser automation via Playwright. |

---

## 💡 Example Mini-Project

Try this with the interactive loop (`05_conversation_loop.py`):

> “Go to [datacamp.com/blog](https://datacamp.com/blog) and check the latest 5 articles.  
> Generate a document listing each title, URL, and summary.”

Claude will use its tools to fetch data, summarize, and create the output automatically.

---

## 🔒 Safety, Permissions & Evaluation

- **Permissions:** The examples use `permission_mode='acceptEdits'` — adjust if you prefer to confirm Claude’s actions.
- **Logs:** You can track agent actions by printing tool use blocks (`ToolUseBlock`) or saving them to a file.
- **Edge cases:** Try unexpected prompts or missing permissions to observe how Claude handles errors.

---

## 🚀 Next Steps
Once comfortable with these basics, explore:
- Multi-tool orchestration and sub-agents
- Memory management and state persistence
- MCP integrations for databases, browsers, and APIs

For full documentation, see the [Claude Agent SDK Docs](https://docs.claude.com/en/api/agent-sdk/python).

---

**Author:** Josep Ferrer  
**Platform:** [DataCamp](https://www.datacamp.com)  
**License:** MIT
