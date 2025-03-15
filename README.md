# Plant Disease Detection System

## 📌 Project Overview
The **Plant Disease Detection System** is an AI-powered application designed to assist farmers and agricultural professionals in detecting plant diseases early. By leveraging **Convolutional Neural Networks (CNNs)**, the system classifies plant diseases from leaf images with high accuracy. Users can access the system through a **Flask-based web application** or via **WhatsApp integration using Twilio**, making it accessible and user-friendly.

## 🚀 Features
- **AI-Based Image Classification:** Utilizes deep learning (CNNs) to detect and classify plant diseases.
- **Web Application:** Built with **Flask**, allowing users to upload images for real-time analysis.
- **WhatsApp Integration:** Uses **Twilio API** to let users send plant images via WhatsApp for instant disease detection.
- **Scalable and Efficient:** Designed to handle large datasets and provide quick predictions.
- **User-Friendly Interface:** Accessible through both web and mobile platforms.

## 🏗️ Tech Stack
- **Backend:** Flask, FastAPI, TensorFlow, OpenCV
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** Convolutional Neural Networks (CNNs)
- **Database:** Firebase (for storing image data)
- **API Integration:** Twilio API for WhatsApp communication

## 🛠️ Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/your-repo-name.git
cd plant-disease-detection
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Run the Flask App**
```sh
python app.py
```
Access the web application at `http://127.0.0.1:5000/`.

### **4. WhatsApp Bot Setup (Twilio Integration)**
1. Sign up on [Twilio](https://www.twilio.com/)
2. Get your **Twilio Account SID** and **Auth Token**
3. Set up a Twilio sandbox for WhatsApp
4. Configure Twilio to send images to your Flask server

## 🔍 How It Works
### **Web Application Flow:**
1. User uploads an image of a plant leaf.
2. The image is preprocessed and sent to the deep learning model.
3. The model predicts the disease and returns the result.
4. The result is displayed on the web application.

### **WhatsApp Bot Flow:**
1. User sends an image via WhatsApp.
2. The Flask backend receives and processes the image.
3. The deep learning model predicts the disease.
4. The result is sent back to the user on WhatsApp.

## 📊 Dataset
- **Source:** Kaggle (Plant Disease Dataset)
- **Images:** 10,000+ plant leaf images
- **Classes:** Various plant diseases and healthy leaves
- **Processing:** Resized, normalized, and augmented for training

## ✅ Advantages
- **Early Disease Detection:** Helps prevent large-scale crop losses.
- **Automation:** Reduces dependency on manual inspection.
- **User-Friendly:** Accessible via both web and mobile platforms.
- **Scalability:** Can be extended to detect more plant diseases.

## 🚧 Limitations
- **Dataset Dependency:** Accuracy relies on the quality of training data.
- **Environmental Factors:** Lighting and image quality may affect predictions.
- **No Treatment Suggestions:** The system only provides disease classification.

## 📌 Future Enhancements
- **Expand Dataset:** Add more plant species and disease types.
- **Mobile App Development:** Create an Android/iOS application.
- **IoT Integration:** Use drones or sensors for real-time field monitoring.
- **Multilingual Support:** Make the system accessible in multiple languages.

## 🤝 Contributors
- **Kunal Gautam**  
- **Sweta Singh**  
- **Sayan Golder**  

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact
For any queries or collaborations, feel free to reach out:  
📧 Email: kunalgautam489@gmail.com  
🔗 LinkedIn: [Kunal Gautam](https://www.linkedin.com/in/kunal-gautam-2981b2292/)  
📂 GitHub: [kunal654](https://github.com/kunal654)  

---
⭐ If you find this project helpful, don't forget to star the repository on GitHub! ⭐

