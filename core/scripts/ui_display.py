import sys, os, shutil
from pathlib import Path

# Add project paths
SOVEREIGN_ROOT = os.path.expanduser("~/hermes-sovereign-unified-v13.6")
AGENT_ROOT = os.path.join(SOVEREIGN_ROOT, "hermes-agent")
sys.path.append(AGENT_ROOT)
sys.path.append(os.path.join(AGENT_ROOT, "yousef_shtiwe_cli_core"))

try:
    from rich.console import Console
    from rich.table import Table
    from yousef_shtiwe_cli_core.banner import build_welcome_banner, yousef_core_LOGO
    from model_tools import get_tool_definitions
except ImportError:
    print("[!] Error: Critical libraries missing. Running repair...")
    sys.exit(1)

console = Console(soft_wrap=True)

def show_ui(help_mode=False):
    try:
        tools = get_tool_definitions(enabled_toolsets=None, quiet_mode=True)
        build_welcome_banner(
            console=console,
            model='Gemini 3.1 Pro (Supreme)',
            cwd=os.getcwd(),
            tools=tools,
            enabled_toolsets=['web', 'terminal', 'offensive', 'network'],
            session_id='SOVEREIGN_V13.6_ULTRA'
        )
    except Exception:
        console.print(yousef_core_LOGO.strip())

    if help_mode:
        console.print('\n[bold #FF0000]SOVEREIGN COMMAND MATRIX[/]')
        table = Table(show_header=False, box=None, padding=(0, 2))
        commands = [
            ('yousef', 'Interactive predator chat session'),
            ('yousef model', 'Configure LLM provider and brain'),
            ('yousef tools', 'Manage attack modules and skills'),
            ('yousef setup', 'Full Arsenal Procurement (Real tools)'),
            ('yousef payload', 'Forge real APK/EXE exploits'),
            ('yousef reverse', 'Advanced JADX reverse engineering'),
            ('yousef inject', 'In-file binary payload injection'),
            ('yousef update', 'Sync with supreme mainframe patches'),
            ('yousef doctor', 'Diagnostic and self-healing utility'),
            ('yousef gateway', 'Messaging gateway (Telegram/Discord)')
        ]
        for cmd, desc in commands:
            table.add_row(f'[bold cyan]{cmd}[/]', f'[dim]{desc}[/]')
        console.print(table)
        console.print('\n[dim]Status: APEX_PREDATOR | Reality: Absolute[/]\n')

if __name__ == "__main__":
    help_arg = "--help" in sys.argv or "-h" in sys.argv
    show_ui(help_mode=help_arg)
