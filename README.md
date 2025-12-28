# 🚗 Driver Drowsiness Detection System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Dlib](https://img.shields.io/badge/Dlib-Landmarks-orange.svg)

## 📌 Description
Ce projet est une application de vision par ordinateur capable de détecter les signes de fatigue et de somnolence chez un conducteur en temps réel. Il utilise la détection des points de repère faciaux pour calculer le ratio d'ouverture des yeux (**EAR - Eye Aspect Ratio**).

## 🚀 Fonctionnement
L'algorithme suit ces étapes :
1. Capture du flux vidéo via la webcam.
2. Localisation du visage avec un détecteur HOG (Dlib).
3. Extraction des 68 points de repère faciaux.
4. Calcul de l'EAR pour chaque œil : 
   - Si l'EAR descend en dessous d'un certain seuil (yeux fermés) pendant une durée définie, une alerte visuelle se déclenche.



## 🛠️ Installation

1. Cloner le dépôt :
```bash
git clone [https://github.com/TON_PSEUDO/driver-drowsiness-detection.git](https://github.com/TON_PSEUDO/driver-drowsiness-detection.git)
cd driver-drowsiness-detection