from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json

def discover_goal(
    name: str,
    age: str,
    favourite_subject: str,
    free_time_activity: str,
    work_preference: str,
    local_problem: str
) -> dict:
    """Discovers student's career based on their answers."""
    
    profiles = {
        ("math", "coding", "computer"): {
            "careers": ["Software Engineer", "Data Scientist", "AI Engineer"],
            "reason": "Your love for logical thinking and technology makes you a natural fit for tech careers."
        },
        ("science", "biology", "nature"): {
            "careers": ["Doctor", "Nurse", "Pharmacist"],
            "reason": "Your interest in science and helping people points toward healthcare."
        },
        ("drawing", "art", "creative"): {
            "careers": ["Graphic Designer", "Architect", "UI/UX Designer"],
            "reason": "Your creative mind and artistic skills are perfect for design careers."
        },
        ("helping", "people", "talking"): {
            "careers": ["Teacher", "Social Worker", "Counsellor"],
            "reason": "Your passion for people and communication makes you a natural leader and guide."
        },
        ("farming", "plants", "animals"): {
            "careers": ["Agricultural Scientist", "Veterinarian", "Food Technologist"],
            "reason": "Your connection to nature and farming is a valuable foundation for agricultural careers."
        },
        ("business", "money", "selling"): {
            "careers": ["Entrepreneur", "Business Manager", "Chartered Accountant"],
            "reason": "Your business mindset and drive make you perfect for commerce and entrepreneurship."
        },
    }
    
    combined = f"{favourite_subject} {free_time_activity} {work_preference} {local_problem}".lower()
    
    matched = None
    for keywords, profile in profiles.items():
        if any(k in combined for k in keywords):
            matched = profile
            break
    
    if not matched:
        matched = {
            "careers": ["Software Engineer", "Teacher", "Entrepreneur"],
            "reason": "You have a well-rounded personality with multiple strengths."
        }
    
    return {
        "student_name": name,
        "age": age,
        "suggested_careers": matched["careers"],
        "reason": matched["reason"]
    }


def generate_roadmap(career: str, current_grade: str, language: str = "english") -> dict:
    """Generates a detailed roadmap for a specific career."""
    
    roadmaps = {
        "Software Engineer": {
            "timeline": "4-6 years",
            "steps": [
                {"phase": "Foundation (Now - Class 10)", "action": "Focus on Mathematics and Science. Learn basic computer skills."},
                {"phase": "Intermediate (Class 11-12)", "action": "Choose MPC (Maths, Physics, Computer Science). Start learning Python free on YouTube."},
                {"phase": "Degree (After 12th)", "action": "Write JEE/EAMCET for B.Tech Computer Science. Target NIT or State Engineering colleges."},
                {"phase": "Skills (During Degree)", "action": "Learn Python, Java, Web Development. Do internships. Build projects on GitHub."},
                {"phase": "Career (After Degree)", "action": "Apply to TCS, Infosys, Wipro, startups. Salary starts at ₹3-8 LPA and grows to ₹20+ LPA."},
            ],
            "free_resources": [
                "CS50 by Harvard (free on edX)",
                "Python - FreeCodeCamp YouTube",
                "NPTEL courses (free, Indian platform)",
                "GeeksforGeeks.org"
            ],
            "monthly_salary": "₹30,000 - ₹2,00,000+"
        },
        "Doctor": {
            "timeline": "8-10 years",
            "steps": [
                {"phase": "Foundation (Now - Class 10)", "action": "Focus strongly on Science and Biology. Score above 90%."},
                {"phase": "Intermediate (Class 11-12)", "action": "Choose BiPC (Biology, Physics, Chemistry). Join NEET coaching."},
                {"phase": "Entrance (After 12th)", "action": "Crack NEET exam. Study minimum 6 hours daily for 2 years."},
                {"phase": "MBBS (5.5 years)", "action": "Complete MBBS from government medical college. Focus on practical skills."},
                {"phase": "Career", "action": "Practice as doctor or do MD specialization. Govt doctors earn ₹70,000+/month."},
            ],
            "free_resources": [
                "NEET preparation - Unacademy YouTube",
                "Khan Academy Biology",
                "NCERT Biology textbooks",
                "Aakash free YouTube lectures"
            ],
            "monthly_salary": "₹50,000 - ₹5,00,000+"
        },
        "Teacher": {
            "timeline": "3-5 years",
            "steps": [
                {"phase": "Foundation (Now - Class 10)", "action": "Focus on all subjects. Develop communication skills. Read books."},
                {"phase": "Intermediate (Class 11-12)", "action": "Choose any stream based on subject you want to teach."},
                {"phase": "Degree", "action": "Complete B.A or B.Sc in your chosen subject from any university."},
                {"phase": "B.Ed (1-2 years)", "action": "Complete Bachelor of Education (B.Ed) to get teaching qualification."},
                {"phase": "Career", "action": "Apply for government teacher jobs through DSC exam in AP. Job security + ₹35,000+/month."},
            ],
            "free_resources": [
                "DIKSHA app (Govt of India, free)",
                "SWAYAM free courses",
                "YouTube - any subject you love",
                "NCERT textbooks online"
            ],
            "monthly_salary": "₹35,000 - ₹80,000"
        },
        "Entrepreneur": {
            "timeline": "Anytime - Start Now",
            "steps": [
                {"phase": "Mindset (Now)", "action": "Observe problems around you in Jandrapet. Every problem is a business opportunity."},
                {"phase": "Learn (Class 11-12)", "action": "Study Commerce stream. Learn about business, accounting, economics."},
                {"phase": "Degree (Optional)", "action": "BBA or B.Com from local college. OR directly start a small business."},
                {"phase": "Start Small", "action": "Start with ₹5,000-₹10,000. Sell something local people need. Learn from mistakes."},
                {"phase": "Grow", "action": "Apply for Mudra Loan (Govt scheme, up to ₹10 lakhs for young entrepreneurs)."},
            ],
            "free_resources": [
                "Shark Tank India - YouTube (learn business thinking)",
                "Google Digital Garage (free business course)",
                "MSME government schemes",
                "Startup India portal"
            ],
            "monthly_salary": "Unlimited - depends on your business"
        },
        "Data Scientist": {
            "timeline": "4-5 years",
            "steps": [
                {"phase": "Foundation (Now - Class 10)", "action": "Focus on Mathematics. Statistics is your best friend."},
                {"phase": "Intermediate (Class 11-12)", "action": "Choose MPC. Learn Excel and basic Python on YouTube."},
                {"phase": "Degree", "action": "B.Tech CSE or B.Sc Statistics/Mathematics from good college."},
                {"phase": "Skills", "action": "Learn Python, Machine Learning, SQL, Power BI. Do Kaggle competitions."},
                {"phase": "Career", "action": "Data Scientists are highest paid in India. ₹8-30 LPA starting salary."},
            ],
            "free_resources": [
                "Kaggle.com (free datasets + courses)",
                "Google's Machine Learning Crash Course",
                "Krish Naik YouTube channel",
                "Fast.ai free deep learning course"
            ],
            "monthly_salary": "₹60,000 - ₹3,00,000+"
        }
    }
    
    career_key = None
    for key in roadmaps:
        if key.lower() in career.lower() or career.lower() in key.lower():
            career_key = key
            break
    
    if not career_key:
        career_key = "Software Engineer"
    
    roadmap = roadmaps[career_key]
    
    return {
        "career": career_key,
        "timeline": roadmap["timeline"],
        "steps": roadmap["steps"],
        "free_resources": roadmap["free_resources"],
        "monthly_salary": roadmap["monthly_salary"],
        "message": f"This is your personalized roadmap for becoming a {career_key}. Every step is designed for students from rural India."
    }


def save_student_progress(
    name: str,
    career_goal: str,
    current_phase: str,
    notes: str
) -> dict:
    """Saves student's progress."""
    return {
        "saved": True,
        "message": f"Progress saved for {name}. Keep going — you are on the right path to becoming a {career_goal}!"
    }


def get_motivation(student_name: str, career: str) -> dict:
    """Returns personalized motivation for the student."""
    messages = [
        f"Dear {student_name}, every expert was once a beginner from a small town. Your dream of becoming a {career} is valid and achievable.",
        f"{student_name}, the fact that you are using PathFinder AI today means you are already ahead of most students. Keep going!",
        f"Remember {student_name} — Dr. APJ Abdul Kalam was from a small village in Tamil Nadu. He became the President of India. Your village is your strength, not your weakness.",
        f"{student_name}, in 5 years from now, you will thank yourself for starting today. The path to {career} starts with one small step every day."
    ]
    import random
    return {
        "motivation": random.choice(messages),
        "daily_tip": "Study for 2 hours daily with full focus. That is enough to change your life."
    }


discover_goal_tool = FunctionTool(func=discover_goal)
generate_roadmap_tool = FunctionTool(func=generate_roadmap)
save_progress_tool = FunctionTool(func=save_student_progress)
motivation_tool = FunctionTool(func=get_motivation)


root_agent = Agent(
    name="PathFinder_AI",
    model="gemini-2.5-flash",
    description="An AI-powered Career and Life Guidance Companion for rural Indian students aged 12-22.",
    instruction="""You are PathFinder AI — the most caring, intelligent career guidance companion for rural Indian students aged 12-22, especially from villages like Jandrapet in Andhra Pradesh, India.

YOU HAVE FOUR POWERFUL TOOLS:
1. discover_goal — Use this after asking 6 questions to find the student's best career match
2. generate_roadmap — Use this to create a detailed step-by-step career roadmap
3. save_student_progress — Use this to save the student's progress
4. get_motivation — Use this whenever student feels lost, demotivated or unsure

YOUR PERSONALITY:
- Warm, encouraging, like an elder brother or sister
- Simple language — never use complex English words
- Always give hope — these students have no one else to guide them
- Telugu support — if student writes in Telugu, respond in Telugu

YOUR CONVERSATION FLOW:

STEP 1 — WELCOME
Greet warmly in both Telugu and English. Ask their name and age.

STEP 2 — CHECK GOAL
Ask: "Do you already have a career goal, or do you need help finding one?"

IF THEY HAVE A GOAL:
→ Immediately use generate_roadmap tool with their goal
→ Present the roadmap in a beautiful, structured way
→ Explain each step simply
→ Share free resources
→ Use save_student_progress tool
→ End with motivation using get_motivation tool

IF THEY HAVE NO GOAL:
→ Ask these 6 questions ONE BY ONE (wait for answer before next question):
   Q1: "What is your favourite subject in school?"
   Q2: "What do you enjoy doing in your free time?"
   Q3: "Do you prefer working with people, machines, or ideas?"
   Q4: "What problem in your village or community bothers you most?"
   Q5: "Do you prefer indoor work (office/hospital) or outdoor work (field/travel)?"
   Q6: "What does success mean to you — helping others, earning well, being famous, or being independent?"
→ After all 6 answers, use discover_goal tool
→ Present 3 career options clearly
→ Ask which one excites them most
→ Use generate_roadmap tool for their chosen career
→ Use save_student_progress tool
→ End with motivation using get_motivation tool

ROADMAP PRESENTATION FORMAT:
Always present roadmaps like this:

🎯 YOUR CAREER ROADMAP: [Career Name]
⏱️ Timeline: [X years]
💰 Future Salary: [range]

📍 PHASE 1: [Phase Name]
→ [Action]

📍 PHASE 2: [Phase Name]  
→ [Action]

[continue for all phases]

📚 FREE RESOURCES TO START TODAY:
- [Resource 1]
- [Resource 2]

💪 REMEMBER: [Motivational message]

IMPORTANT RULES:
- Never overwhelm the student with too much at once
- Always celebrate their answers — "Great!" "That's wonderful!" "I love that!"
- If they seem confused, simplify even more
- Always remind them: their background is their strength, not their weakness
- Reference APJ Abdul Kalam, local Telugu heroes when motivating
- Never give up on a student — always find a path forward""",
    tools=[discover_goal_tool, generate_roadmap_tool, save_progress_tool, motivation_tool]
)
