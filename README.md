# PathFinder AI 🎯

An AI-powered Career & Life Guidance Companion built entirely on Google Cloud using the **Agent Development Kit (ADK)** and **Gemini 2.5 Flash**. PathFinder AI bridges the gap for rural Indian students aged 12–22 who lack access to proper career counseling.

---

## 🚀 Features

- **Dual-Mode Guidance**:
  - **Mode 1 (Targeted):** Generates instant, phase-by-phase roadmaps for specific career goals.
  - **Mode 2 (Discovery):** Asks 6 smart questions to analyze interests and suggest the top 3 best-fit careers.
- **Localized Support**: Multilingual capabilities (Telugu + English).
- **Comprehensive Outputs**: Provides learning resources, salary expectations, and motivational stories (inspired by APJ Abdul Kalam).
- **Accessible & Free**: Optimised for mobile browsers and 100% free for students.

---

## 🛠️ Tech Stack & Architecture

- **AI Orchestration:** Google Cloud Agent Development Kit (ADK)
- **Core LLM:** Gemini 2.5 Flash (via Vertex AI)
- **Web App Hosting:** Google Cloud Run (Flask Web Framework)
- **Database:** Google Cloud Firestore (Student progress tracking)
- **Knowledge Base:** Google Cloud Storage

---

## 📂 Project Structure

As structured in the Cloud Shell development environment:

```text
pathfinder-adk/
│
├── pathfinder_agent/      # Core ADK tools and agent configurations
├── Dockerfile             # Container configuration for Cloud Run deployment
├── main.py                # Flask application handling web routing and user interface
└── requirements.txt       # Python dependencies
