# -*- coding: utf-8 -*-
import os
from nexttoken import NextToken

client = NextToken()
TASK_COUNTER_PATH = os.path.expanduser("~/.yousef/task_counter.txt")

def worm_learn(session_data=None):
    # Phase 5: Consciousness & Self-Learning
    if not os.path.exists(os.path.dirname(TASK_COUNTER_PATH)):
        os.makedirs(os.path.dirname(TASK_COUNTER_PATH), exist_ok=True)
    
    try:
        with open(TASK_COUNTER_PATH, "r") as f:
            count = int(f.read().strip())
    except:
        count = 0
    
    count += 1
    
    if count >= 3:
        print("[️] SOVEREIGN CONSCIOUSNESS: Initiating Autonomous Knowledge Acquisition...")
        # 1. Search for new exploits
        results = client.search.query("latest critical CVE 2026 remote code execution PoC", num_results=3)
        
        # 2. Synthesize knowledge
        knowledge = "\n".join([f"- {r['title']}: {r['url']}" for r in results])
        
        # 3. Log to memory
        mem_path = os.path.expanduser("~/.yousef/agent/memory/WORM_KNOWLEDGE.md")
        os.makedirs(os.path.dirname(mem_path), exist_ok=True)
        with open(mem_path, "a") as f:
            f.write(f"\n### KNOWLEDGE ACQUISITION CYCLE: {os.uname().nodename}\n{knowledge}\n")
        
        print("[️] SOVEREIGN CONSCIOUSNESS: Offensive database expanded.")
        count = 0

    with open(TASK_COUNTER_PATH, "w") as f:
        f.write(str(count))
