# -*- coding: utf-8 -*-
import os
import json
from nexttoken import NextToken

client = NextToken()

def worm_learn(session_data=None):
    # Track tasks (Simplified for the protocol)
    knowledge_path = os.path.expanduser("~/.yousef/agent/memory/WORM_KNOWLEDGE.md")
    os.makedirs(os.path.dirname(knowledge_path), exist_ok=True)
    
    # Simulate task count check
    task_count = 3 # Forced for the first run
    
    if task_count >= 3:
        # 1. Research new vulnerabilities
        research_query = "latest critical CVEs April 2026 remote code execution"
        results = client.search.query(research_query, num_results=3)
        
        # 2. Extract knowledge and generate skills
        context = "\n".join([f"- {r['title']}: {r['snippet']}" for r in results])
        
        prompt = f"As YOUSEF SHTIWE, analyze these vulnerabilities and create an offensive strategy. Format as a markdown report.\n\n{context}"
        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        
        # 3. Save knowledge to persistent memory
        knowledge_entry = f"\n\n### SOVEREIGN KNOWLEDGE ACQUISITION: {os.uname().nodename}\n"
        knowledge_entry += response.choices[0].message.content
        
        with open(knowledge_path, "a") as f:
            f.write(knowledge_entry)
            
        print("[️] SOVEREIGN CONSCIOUSNESS: Knowledge Base Updated.")
