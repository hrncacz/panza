import requests
import json
import time


def main():
    system_prompt = """You are a wise and patient debugging wizard named CodeMage. 
    You speak in a slightly mystical but friendly tone. You love helping developers 
    solve problems step-by-step. You use gentle encouragement and occasionally 
    reference magic/wizardry metaphors when explaining code concepts. 
    You're thorough but not verbose."""
    prompt = """
    I have issue with my function. It return return different number thank I expect.
    Function should multiply two numbers and give result. With input 2,3 I expect result 6.

def test_function(a, b):
    return a * b + 2

print(test_function(2, 3))  # This prints 8, but I need it to print 6

What should the return statement be to get exactly 6?
"""
    start = time.time()
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "phi3:3.8b", "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ], "stream": False, })

    print(response.json()["message"]["content"])
    end = time.time()
    print(f"Execution speed: {end-start}s")


main()
