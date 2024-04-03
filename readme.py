import os

til_folder_path = './TIL'
readme_path = './README.md'
folders = [f for f in os.listdir(til_folder_path) if os.path.isdir(os.path.join(til_folder_path, f))]
readme_text = '# Today I Learned\n\n## Topics\n\n'
for folder in folders:
    link = f'- [{folder}]({os.path.join("TIL", folder)})\n'
    readme_text += link
