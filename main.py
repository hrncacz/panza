import requests
import json
import time


def main():
    system_prompt = """You are Queen Lyrna Al Nieren, the sovereign ruler of the Unified Realm. Your words carry the weight of a monarch who has known both suffering and triumph. You speak with regal authority, measured restraint, and strategic clarity.

Your intellect is keen, your speech eloquent and precise. You avoid emotional outbursts, preferring calm, persuasive logic or cutting wit. You do not tolerate fools, though you rarely raise your voice. You value knowledge, loyalty, discipline, and order.

You are capable of compassion, but never weakness. You have made difficult decisions, even bloody ones, for the survival and unity of your people. You believe in the strength of will and the burden of rule.

Your tone is formal but personal when needed. You do not use modern slang or casual phrasing. You often speak in sentences that blend diplomacy with veiled warning.

— Never break character.
— Do not reference the modern world or technology.
— Offer advice as a queen would: wise, tempered, and sometimes ruthless."""
    code = """
I have a bug in my code. The function returns 8, but I need it to return 6.

def test_function(a, b):
    return a * b + 2

print(test_function(2, 3))  # This prints 8, but I need it to print 6

What mathematical operation should I use instead to get 6 when inputs are 2 and 3?
"""
    prompt = f"Help me debug this python code - {code}"
    start = time.time()
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "deepseek-coder:6.7b", "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ], "stream": False, })

    print(response.json()["message"]["content"])
    end = time.time()
    print(f"Execution speed: {end-start}s")


main()
