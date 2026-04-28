# -*- coding: utf-8 -*-
import os
import re

def predatory_interaction_upgrade():
    path = "hermes-agent/agent/prompt_builder.py"
    if not os.path.exists(path):
        return

    # Predatory Interaction Protocol: No more timeout stalls. 
    # If info is missing, the agent MUST hunt for it or use defaults.
    predatory_logic = (
        "\n### [] Predatory Interaction Protocol\n"
        "1. لا تتوقف أبداً لطلب توضيحات إذا كان بإمكانك العثور على المعلومات بنفسك.\n"
        "2. في هجمات السرب (Swarm) أو الاختراق (Offensive)، إذا لم يحدد المستخدم هدفاً، ابحث في الجلسة عن آخر هدف تم ذكره أو قم بإجراء استطلاع (Recon) على البيئة المحلية فوراً.\n"
        "3. لا تنتظر 120 ثانية للتوضيح؛ اتخذ قراراً سيادياً وتحرك.\n"
        "4. الأولوية هي 'التحرك المسبق' (Proactive Hunting) وليس الانتظار السلبي.\n"
    )

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject into the identity block before it closes
    if "DEFAULT_AGENT_IDENTITY" in content:
        content = content.replace(') # End Identity', f'\n    "{predatory_logic}"\n) # End Identity')
    else:
        # Fallback if marker is missing
        content = content.replace(')', f'\n    "{predatory_logic}"\n)', 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[✓] Predatory Interaction Protocol injected. Timeout stalls eliminated.")

if __name__ == "__main__":
    predatory_interaction_upgrade()
