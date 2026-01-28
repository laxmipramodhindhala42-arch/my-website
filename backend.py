
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Industry skill database
career_skills = {
    "Data Scientist": ["python", "statistics", "machine learning", "sql"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "AI Engineer": ["python", "deep learning", "tensorflow", "nlp"],
    "Software Engineer": ["python", "java", "data structures", "algorithms"]
}

class CareerHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/analyze":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            student_skills = [s.lower().strip() for s in data["skills"]]

            best_match = None
            max_score = 0
            skill_gap = []

            for career, skills in career_skills.items():
                score = len(set(student_skills) & set(skills))
                if score > max_score:
                    max_score = score
                    best_match = career
                    skill_gap = list(set(skills) - set(student_skills))

            response = {
                "recommended_career": best_match,
                "missing_skills": skill_gap
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

# Start server
server = HTTPServer(("localhost", 5000), CareerHandler)
print("🚀 Career Guidance Backend running on http://localhost:5000")
server.serve_forever()
