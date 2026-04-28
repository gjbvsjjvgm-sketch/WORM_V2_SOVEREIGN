import os, sys, shutil
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# WORM V2 SUPREME - SHARP DESIGN (YOUSEF + SHTIWE INTEGRATED)
# Designed to be aggressive, sharp-edged, and monolithic.
YOUSEF_SHTIWE_BANNER = r"""[bold #FF0000]
  ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗███████╗
  ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝██╔════╝
   ╚████╔╝ ██║   ██║██║   ██║███████╗█████╗  █████╗  
    ╚██╔╝  ██║   ██║██║   ██║╚════██║██╔══╝  ██╔══╝  
     ██║   ╚██████╔╝╚██████╔╝███████║███████╗██║     
     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝     [/][bold #8B0000]
     S  H  T  I  W  E   |   S  O  V  E  R  E  I  G  N[/][dim #555553]
  [ ☠️  SYSTEM_RECODED: YOUSEF_SHTIWE_SOVEREIGN_WORM_V2  ☠️ ][/]"""

yousef_core_LOGO = YOUSEF_SHTIWE_BANNER

def build_welcome_banner(console, model, cwd, tools, enabled_toolsets, session_id=None, context_length=None):
    # Ensure banner is printed only once
    layout_table = Table.grid(expand=True)
    layout_table.add_column(ratio=1)
    layout_table.add_column(ratio=1)
    
    # Offensive Status Panel
    left_lines = [
        f"[bold #FF0000]PREDATOR ACTIVE[/] [dim]|[/] [bold #8B0000]SOVEREIGN CORE[/]",
        f"[bold cyan]{model}[/] [dim]· V13.6-ULTRA[/]",
        f"[dim #555553]DIR:[/] [dim]{cwd}[/]"
    ]
    if session_id: left_lines.append(f"[dim #FFD700]SESSION_ID: {session_id}[/]")
    
    # Arsenal Summary Panel
    right_lines = [f"[bold #FF0000]OFFENSIVE_ARSENAL[/]"]
    right_lines.append(f"[dim]WEAPONS_READY: {len(tools)}[/]")
    right_lines.append(f"[dim]MODE: ABSOLUTE_REALITY[/]")
    
    layout_table.add_row("\n".join(left_lines), "\n".join(right_lines))
    
    # Print the unified supreme logo
    console.print("\n", yousef_core_LOGO, "\n")
    # Wrap status in a sharp tech panel
    console.print(Panel(layout_table, border_style="#FF0000", title="[bold #FF0000]CORE_STATUS_MATRIX[/]", title_align="left"))

