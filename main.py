from flask import Flask, render_template, request, jsonify
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from pathfinder_agent.agent import root_agent
import asyncio
import uuid

app = Flask(__name__, template_folder='pathfinder_agent/templates')

session_service = InMemorySessionService()
APP_NAME = "pathfinder_ai"
runners = {}

async def get_response(user_id: str, message: str) -> str:
    session_id = f"session_{user_id}"
    
    if user_id not in runners:
        await session_service.create_session(
            app_name=APP_NAME,
            user_id=user_id,
            session_id=session_id
        )
        runners[user_id] = Runner(
            agent=root_agent,
            app_name=APP_NAME,
            session_service=session_service
        )
    
    runner = runners[user_id]
    content = types.Content(role='user', parts=[types.Part(text=message)])
    
    final_response = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response = event.content.parts[0].text
    
    return final_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    session_id = data.get('session_id', str(uuid.uuid4()))
    
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(get_response(session_id, message))
        loop.close()
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
