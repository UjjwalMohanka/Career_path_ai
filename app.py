from flask import Flask, request, jsonify, render_template
import openai, json
from utils.gpt_prompts import get_resume_tips, get_path_recommendation

app = Flask(__name__)
openai.api_key = 'YOUR_OPENAI_KEY'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    skills = data['skills']
    goal = data['goal']

    resume_tips = get_resume_tips(skills, goal)
    path_reco = get_path_recommendation(skills, goal)

    return jsonify({
        "resume_tips": resume_tips,
        "career_paths": path_reco
    })

if __name__ == '__main__':
    app.run(debug=True)
