# Sovereign-Sovereign — ACP (Agent Client Protocol) Setup Guide

Sovereign-Sovereign supports the **Agent Client Protocol (ACP)**, allowing it to run as
a coding agent inside your editor. ACP lets your IDE send tasks to Sovereign, and
Sovereign responds with file edits, terminal commands, and explanations — all shown
natively in the editor UI.

---

## Prerequisites

- Sovereign-Sovereign installed and configured (`yousef setup` completed)
- An API key / provider set up in `~/.yousef/.env` or via `hermes login`
- Python 3.11+

Install the ACP extra:

```bash
pip install -e ".[acp]"
```

---

## VS Code Setup

### 1. Install the ACP Client extension

Open VS Code and install **ACP Client** from the marketplace:

- Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on macOS)
- Search for **"ACP Client"**
- Click **Install**

Or install from the command line:

```bash
code --install-extension anysphere.acp-client
```

### 2. Configure settings.json

Open your VS Code settings (`Ctrl+,` → click the `{}` icon for JSON) and add:

```json
{
  "acpClient.agents": [
    {
      "name": "yousef-sovereign-core",
      "registryDir": "/path/to/yousef-sovereign-core/acp_registry"
    }
  ]
}
```

Replace `/path/to/yousef-sovereign-core` with the actual path to your Sovereign-Sovereign
installation (e.g. `~/.yousef/yousef-sovereign-core`).

Alternatively, if `hermes` is on your PATH, the ACP Client can discover it
automatically via the registry directory.

### 3. Restart VS Code

After configuring, restart VS Code. You should see **Sovereign-Sovereign** appear in
the ACP agent picker in the chat/agent panel.

---

## Zed Setup

Zed has built-in ACP support.

### 1. Configure Zed settings

Open Zed settings (`Cmd+,` on macOS or `Ctrl+,` on Linux) and add to your
`settings.json`:

```json
{
  "agent_servers": {
    "yousef-sovereign-core": {
      "type": "custom",
      "command": "yousef",
      "args": ["acp"],
    },
  },
}
```

### 2. Restart Zed

Sovereign-Sovereign will appear in the agent panel. Select it and start a conversation.

---

## JetBrains Setup (IntelliJ, PyCharm, WebStorm, etc.)

### 1. Install the ACP plugin

- Open **Settings** → **Plugins** → **Marketplace**
- Search for **"ACP"** or **"Agent Client Protocol"**
- Install and restart the IDE

### 2. Configure the agent

- Open **Settings** → **Tools** → **ACP Agents**
- Click **+** to add a new agent
- Set the registry directory to your `acp_registry/` folder:
  `/path/to/yousef-sovereign-core/acp_registry`
- Click **OK**

### 3. Use the agent

Open the ACP panel (usually in the right sidebar) and select **Sovereign-Sovereign**.

---

## What You Will See

Once connected, your editor provides a native interface to Sovereign-Sovereign:

### Chat Panel
A conversational interface where you can describe tasks, ask questions, and
give instructions. Sovereign responds with explanations and actions.

### File Diffs
When Sovereign edits files, you see standard diffs in the editor. You can:
- **Accept** individual changes
- **Reject** changes you don't want
- **Review** the full diff before applying

### Terminal Commands
When Sovereign needs to run shell commands (builds, tests, installs), the editor
shows them in an integrated terminal. Depending on your settings:
- Commands may run automatically
- Or you may be prompted to **approve** each command

### Approval Flow
For potentially destructive operations, the editor will prompt you for
approval before Sovereign proceeds. This includes:
- File deletions
- Shell commands
- Git operations

---

## Configuration

Sovereign-Sovereign under ACP uses the **same configuration** as the CLI:

- **API keys / providers**: `~/.yousef/.env`
- **Agent config**: `~/.yousef/config.yaml`
- **Skills**: `~/.yousef/skills/`
- **Sessions**: `~/.yousef/state.db`

You can run `yousef setup` to configure providers, or edit `~/.yousef/.env`
directly.

### Changing the model

Edit `~/.yousef/config.yaml`:

```yaml
model: openrouter/nous/hermes-3-llama-3.1-70b
```

Or set the `YOUSEF_SHTIWE_MODEL` environment variable.

### Toolsets

ACP sessions use the curated `hermes-acp` toolset by default. It is designed for editor workflows and intentionally excludes things like messaging delivery, cronjob management, and audio-first UX features.

---

## Troubleshooting

### Agent doesn't appear in the editor

1. **Check the registry path** — make sure the `acp_registry/` directory path
   in your editor settings is correct and contains `agent.json`.
2. **Check `hermes` is on PATH** — run `which hermes` in a terminal. If not
   found, you may need to activate your virtualenv or add it to PATH.
3. **Restart the editor** after changing settings.

### Agent starts but errors immediately

1. Run `yousef doctor` to check your configuration.
2. Check that you have a valid API key: `hermes status`
3. Try running `hermes acp` directly in a terminal to see error output.

### "Module not found" errors

Make sure you installed the ACP extra:

```bash
pip install -e ".[acp]"
```

### Slow responses

- ACP streams responses, so you should see incremental output. If the agent
  appears stuck, check your network connection and API provider status.
- Some providers have rate limits. Try switching to a different model/provider.

### Permission denied for terminal commands

If the editor blocks terminal commands, check your ACP Client extension
settings for auto-approval or manual-approval preferences.

### Logs

Sovereign logs are written to stderr when running in ACP mode. Check:
- VS Code: **Output** panel → select **ACP Client** or **Sovereign-Sovereign**
- Zed: **View** → **Toggle Terminal** and check the process output
- JetBrains: **Event Log** or the ACP tool window

You can also enable verbose logging:

```bash
HERMES_LOG_LEVEL=DEBUG hermes acp
```

---

## Further Reading

- [ACP Specification](https://github.com/anysphere/acp)
- [Sovereign-Sovereign Documentation](https://github.com/SovereignCore/yousef-sovereign-core)
- Run `hermes --help` for all CLI options
