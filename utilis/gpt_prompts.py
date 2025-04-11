import openai

def get_resume_tips(skills, goal):
    prompt = f"I have the following skills: {skills}. I want to become a {goal}. Give resume tips."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def get_path_recommendation(skills, goal):
    prompt = f"I have skills: {skills}. Suggest 3 career paths related to {goal} with short description for each."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
