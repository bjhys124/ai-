# 2. get3d_runner.py - GET3D 호출 (사전 학습된 모델 필요)
import torch
import os

def generate_3d_model():
    from get3d.scripts.generate_mesh import generate_mesh  # GET3D repo 내 함수 사용

    os.makedirs("generated", exist_ok=True)

    latent = torch.randn(1, 512)  # 예시 latent. 추후 encoder로 대체 가능
    generate_mesh(latent, output_path="./generated/face.glb")
