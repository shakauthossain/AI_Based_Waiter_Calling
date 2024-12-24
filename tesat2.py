import torch
import cv2
from torchvision import transforms

# Load pretrained HandPoseGAN model (replace 'handpose_gan.pth' with the actual path)
model_path = 'hand_pose_model.pth'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.load(model_path, map_location=device)

checkpoint = torch.load(model_path, map_location=device)
print(type(checkpoint), checkpoint.keys() if isinstance(checkpoint, dict) else "Not a dictionary")
