import os

til_folder_path = './til'  # 'til' 폴더의 상대 경로
readme_path = './README.md'
# os.listdir로 'til' 폴더의 내용을 가져오고, 그 중에서 폴더만을 선택
folders = [f for f in os.listdir(til_folder_path) if os.path.isdir(os.path.join(til_folder_path, f))]

readme_text = '# Today I Learned\n\n## Topics\n\n'
for folder in folders:
    # 각 폴더에 대한 링크 생성 시, 실제 폴더 이름('til')을 사용
    link = f'- [{folder}](./til/{folder})\n'
    readme_text += link

# README.md 파일 업데이트
with open(readme_path, 'w') as readme_file:
    readme_file.write(readme_text)

print("README.md has been updated with links to TIL subfolders.")