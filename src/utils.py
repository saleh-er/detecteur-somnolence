from scipy.spatial import distance as dist

def calculate_ear(eye):
    # Calcul des distances verticales entre les points de repère de l'œil
    # 
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # Calcul de la distance horizontale
    C = dist.euclidean(eye[0], eye[3])

    # Formule de l'Eye Aspect Ratio
    ear = (A + B) / (2.0 * C)
    return ear