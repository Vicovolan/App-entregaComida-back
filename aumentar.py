import cv2
import numpy as np
import os
import albumentations as A
from albumentations.pytorch import ToTensorV2


input_dir =  "prescricoes"
output_dir = "prescricoes_augmentadas/"


os.makedirs(output_dir, exist_ok=True)

transformacoes = A.Compose([
    A.RandomBrightnessContrast(p=0.5), 
    A.GaussNoise(var_limit=(10, 50), p=0.5),  
    A.MotionBlur(blur_limit=5, p=0.3), 
    A.RandomShadow(p=0.4), 
    A.ImageCompression(quality_lower=30, quality_upper=70, p=0.3),  
    ToTensorV2()
])


for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    
    image = cv2.imread(img_path)
    if image is None:
        continue
    
    augmented = transformacoes(image=image)['image']
    augmented = augmented.permute(1, 2, 0).cpu().numpy()
    output_path = os.path.join(output_dir, f"aug_{img_name}")
    cv2.imwrite(output_path, augmented)

print("Processo de aumento de dados concluído! As novas imagens estão em 'prescricoes_augmentadas/'")
