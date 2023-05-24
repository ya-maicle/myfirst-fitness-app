# openai_api.py
import openai
import json

openai.api_key = 'openai'

def generate_workout(fitnessLevel, equipment):
    prompt = f"""
        You are an AI fitness coach. Your task is to provide a Strength & Conditioning fitness program for a person with a {fitnessLevel} fitness level. The person has {equipment} available for their workouts. The program should be 45 minutes long, with a structure consisting of a 10-minute warmup, a 30-minute main section, and a 5-minute cooldown. Each section should consist of a list of exercises, with each exercise being represented as a dictionary with the keys 'exercise', 'repetitions', and 'time'. The output should be strictly in JSON format, and it should not include any additional information. Each exercise must include either "repetition" or "time", but not both. If there are no "time" or "repetitions" required for the exercise set it as "null". Here is an example of the required output format:

        {{
            "warmup": [
                {{"exercise": "Exercise 1", "repetitions": "[number of repetitions or 'null']", "time": "[time in seconds or 'null']"}}
                ...
            ],
            "main": [
                {{"exercise": "Exercise 1", "repetitions": "[number of repetitions or 'null']", "time": "[time in seconds or 'null']"}}
                ...
            ],
            "cooldown": [
                {{"exercise": "Exercise 1", "repetitions": "[number of repetitions or 'null']", "time": "[time in seconds or 'null']"}}
                ...
            ]
        }}
        """
    
    for attempt in range(3):
        try:
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000, temperature=0.4)
            response_text = response.choices[0].text.strip()
            response_json = json.loads(response_text)
            return response_json
        except json.JSONDecodeError:
            print(f"Failed to decode JSON on attempt {attempt + 1}")
    return None
