# 🗑️ Garbage & Face Detection using YOLOv7 + OpenCV
This project detects garbage thrown outside dustbins and identifies the person responsible using **YOLOv7** + **OpenCV**. If someone throws garbage in the wrong place, the system detects their face and sends an **automated SMS alert** using **Twilio**, notifying them that they will pay a fine.
.
- People
- Four categories of garbage (plastic, metal, paper, organic)
- Faces with name labeling

Built using **YOLOv7** and **OpenCV**, the system is optimized for **high accuracy** and **fast inference speed**, making it suitable for **smart surveillance** and **automated waste management applications**.  
Additionally, if someone throws garbage outside the dustbin, the system **detects their face and sends an SMS alert using Twilio**, notifying them of a fine.

---

## 🎯 Problem Statement
Traditional waste detection systems are often slow, inaccurate, and require manual supervision.  
This project aims to:  
- Automate waste classification in real time  
- Detect people and faces for identity-based monitoring  
- Optimize detection speed for live video streams  

---

## ⚙️ Tech Stack
- **Programming Language:** Python  
- **Frameworks & Libraries:** PyTorch, YOLOv7, OpenCV, LabelImg  
- **Dataset:** Custom dataset with 2,000+ annotated images  
- **Tools:** Google Colab, Jupyter Notebook, Twilio  

---

## 📊 Dataset & Preprocessing
- Collected **2,000+ images** (garbage + people + faces)  
- Annotated using **LabelImg**  
- Applied **data augmentation** (rotation, flipping, brightness adjustments) to improve generalization  

---

## 🚀 Implementation
**Model Training**  
- Trained YOLOv7 on custom dataset  
- Optimized hyperparameters for garbage + face detection  

**Inference Optimization**  
- Reduced model size for faster real-time predictions  
- Integrated OpenCV to process video streams at **20 FPS**  

**Deployment**  
- Live detection of 4 waste categories + faces + people  
- System outputs bounding boxes with confidence scores  
- Sends **automatic SMS alert** via **Twilio** when garbage is thrown outside dustbins  

---

## 📈 Results
- **92% mAP** on test dataset  
- **25% faster** inference compared to baseline YOLOv7 model  
- **20 FPS** achieved in real-time video streams  

---

## 📷 Demo Screenshot

---![mg](https://github.com/user-attachments/assets/1034f756-4820-4815-b3a5-688c078ffc9d)
![detetction](https://github.com/user-attachments/assets/b469f62b-e957-4e59-a3c3-cadf13e5b007)


## 🔗 Future Improvements
- Deploy model on edge devices (Raspberry Pi / Jetson Nano)  
- Expand dataset to cover more waste categories  
- Integrate with smart bins for automated sorting  

---
