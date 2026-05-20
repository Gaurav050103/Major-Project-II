# Major-Project-II

AutoDub AI : AI-Powered Video Localization: Transcription, Translation,and Multi-Language Dubbing System

🎬 AutoDub AI

AI-Powered Video Localization System
Transcription • Translation • Multi-Language Dubbing

📌 Overview

AutoDub AI is an end-to-end AI-driven video localization platform that automates the traditionally manual and time-intensive process of:
* 🎤 Speech-to-Text Transcription
* 🌍 Neural Machine Translation
* 🔊 AI Voice Dubbing (Text-to-Speech)
* 🎞️ Audio-Video Synchronization
The system transforms a single-language video into multiple localized versions while preserving context, tone, emotion, and timing.

🚀 Key Features

* ✅ Fully Automated Localization Pipeline
* 🌐 Multi-language Support (40+ languages)
* 🎙️ High-accuracy Speech Recognition (Whisper)
* 🧠 Context-aware Translation (MarianMT)
* 🗣️ Natural Voice Generation (Tacotron 2 + WaveGlow)
* 🎬 Frame-level Audio-Video Synchronization
* ⚡ Real-time Progress Tracking (WebSockets)
* 📦 Batch Processing Support
* 🔐 Secure User Authentication & Storage

🏗️ System Architecture

The system follows a modular pipeline:
Input Video
    ↓
Audio Extraction (FFmpeg)
    ↓
Speech-to-Text (Whisper)
    ↓
Translation (MarianMT)
    ↓
Text-to-Speech (Tacotron 2)
    ↓
Synchronization (MoviePy + FFmpeg)
    ↓
Final Localized Video Output

🧠 Core Technologies

Component
Technology Used
Programming Language
Python 3.9+
Backend Framework
Flask
Frontend
HTML, CSS, JavaScript
AI Models
Whisper, MarianMT, Tacotron 2
Libraries
HuggingFace Transformers, NumPy
Video Processing
FFmpeg, MoviePy
Database
SQLite / MySQL
Real-Time Updates
WebSockets
Deployment
AWS EC2 / HuggingFace Spaces

⚙️ Installation Guide

🔧 Prerequisites

* Python 3.9+
* FFmpeg installed
* GPU (recommended: NVIDIA RTX 3060 or above)
* pip / virtualenv🔑 Setup Environment Variables

📥 Clone Repository

git clone https://github.com/your-username/autodub-ai.git
cd autodub-ai

📦 Install Dependencies

pip install -r requirements.txt

🔑 Setup Environment Variables

Create a .env file:
FLASK_APP=app.py
FLASK_ENV=development
MODEL_PATH=./models/

▶️ Run Application

python app.py

Open in browser:
http://localhost:5000

🖥️ Usage Guide

🧑‍💻 Step-by-Step Workflow

1. Login/Register
2. Upload Video File
3. Select Target Language(s)
4. Click Process
5. System executes:
    * Transcription
    * Translation
    * Voice Generation
    * Synchronization
6. Preview Output
7. Download Localized Video

📌 Example Scenario

Input: English Lecture Video
Output:
* Hindi Dubbed Version
* Spanish Dubbed Version

📊 Database Schema

Key Entities:
* User
* Video
* Localization Task
* Transcript
* Audio Track
* Feedback
* Admin Logs
* Subscription Plans

🔁 Algorithm Workflow

1. Video Input
2. Audio Extraction
3. Speech Recognition (ASR)
4. Translation (NMT)
5. Voice Synthesis (TTS)
6. Audio-Video Sync
7. Output Rendering

💡 Applications

🎓 Education

* Multilingual lectures
* Global e-learning platforms

 
🎥 Entertainment

* Movie/OTT dubbing
* YouTube content localization

🏢 Corporate

* Training videos
* Global communication

🌍 Accessibility

* Content for non-native speakers
* Inclusive media distribution

📈 Performance Highlights

* ⏱️ 70% faster than manual localization
* 🎯 High transcription accuracy (Whisper)
* 🌐 Scalable to multiple languages simultaneously
* 💰 Reduced production cost significantly

🔮 Future Scope

* 🔴 Real-time live translation & dubbing
* 🎭 Emotion-aware voice synthesis
* 👄 AI lip-sync generation (Wav2Lip integration)
* 📱 Mobile application (Android/iOS)
* ☁️ Cloud-edge hybrid deployment
* 🎥 Multimodal translation (video + text + visuals)

🔐 Security Features

* User authentication system
* Secure file handling
* Encrypted data storage
* Controlled access to resources

👨‍💻 Contributors

* Dakshesh Singh Sherawat
* Gaurav Luniya
* Piyush Jain
* Ishan Jain

🎓 Guide

Prof. Manish Vyas
Department of Information Technology
Acropolis Institute of Technology & Research, Indore

📚 References

* Vaswani et al. – Attention Is All You Need
* OpenAI – Whisper
* Helsinki NLP – MarianMT
* NVIDIA – Tacotron 2 & WaveGlow
* HuggingFace Transformers

🔗 GitHub Profiles


* https://github.com/daksheshsinghsherawat
* https://github.com/ishan78983
* https://github.com/piyushjain1310
* https://github.com/gaurav050103

📜 License


This project is developed for academic and research purposes.
You can extend and modify it with proper attribution.

💬 Final Note

AutoDub AI is not just a tool — it’s a step toward breaking language barriers at scale.
It enables creators, educators, and organizations to communicate globally with clarity, emotion, and efficiency.


Conclusion

AutoDub AI demonstrates how modern artificial intelligence can fundamentally transform video localization by automating transcription, translation, and dubbing within a unified, scalable pipeline. By integrating advanced models such as Whisper for speech recognition, MarianMT for neural translation, and Tacotron 2 for natural voice synthesis, the system achieves a high level of linguistic accuracy, contextual understanding, and audio-visual synchronization.
The project successfully addresses the limitations of traditional localization methods—reducing time, cost, and manual effort while maintaining quality and consistency across multiple languages. Beyond its technical implementation, AutoDub AI highlights the broader potential of AI in breaking language barriers, enabling inclusive access to digital content, and enhancing global communication.
As the system evolves with future advancements such as real-time processing, emotion-aware synthesis, and improved lip synchronization, it holds the potential to become a powerful tool across industries including education, entertainment, and corporate communication. Ultimately, AutoDub AI is not just a technological solution, but a step toward a more connected and linguistically inclusive digital world.






















































































































