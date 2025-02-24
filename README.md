# Prepify

**Prepify** is an AI-powered chatbot designed to help users prepare for job interviews by providing tailored technical and behavioral interview questions. Built with **Python, Streamlit, LangChain, and Ollama**, it leverages **Llama3.1** to generate realistic and context-aware interview scenarios.

## 🚀 Features
- **AI Chatbot**: Uses **Ollama's Llama3.1** to simulate real-world interview conversations.
- **Custom Prompt Engineering**: Generates tailored interview questions for technical and behavioral rounds.
- **Conversation History Tracking**: Maintains context throughout the interview preparation process.
- **Interactive UI**: Built with **Streamlit** for an intuitive and user-friendly experience.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **AI Model**: Ollama's Llama3.1
- **Backend & Logic**: Python, LangChain
- **Version Control**: Git

## 📦 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Prepify.git
   cd Prepify
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up Ollama:
   - Install Ollama by following the instructions at [Ollama's website](https://ollama.ai/)
   - Download and configure **Llama3.1** model:
     ```sh
     ollama pull llama3.1
     ```
   - Ensure Ollama is running before launching the app:
     ```sh
     ollama serve
     ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## 🏗️ How It Works
1. **Select Interview Type**: Choose between **Technical** or **Behavioral** interviews.
2. **Custom Questioning**: AI generates relevant questions based on your experience.
3. **Interactive Conversation**: Responses are processed to refine follow-up questions.
4. **Feedback & Insights**: Get AI-driven feedback to improve answers.

## 🤖 Future Enhancements
- Integration with **speech-to-text** for voice-based interactions.
- Support for **resume-based question tailoring**.
- More **AI models** for diverse question sets.

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
For any queries, reach out via:
- GitHub Issues
- Email: [your-email@example.com]

---
Feel free to customize this with your GitHub username, email, and any additional details! 🚀

