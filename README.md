# End2End-LLM-Project-Deploy-Using-MLFlow

LLM Pre-Trained Model for
A.  Q&A Chatbot
B.  Machine Translation

Method 1:
Create Readme.md file
Create template.py, run it
Create setup.py, requirements.txt, __init__.py ubder Utils
Copy mlflow, waitress file in folder hwere main.py is housed
Create main.py and test it

Method 2:
Setup:
Open VSCode Terminal
Go to New project folder: cd <name>
Create a new venv: conda create -p venvllm python==3.10 -y
Activate this venv: conda activate .../venvllm
Install requirements/dependencies

Start Project Documentation:
Push the readme file content to Github Website:

1. Create git repo: 
git init
git add README.md
git commit -m "first commit"
git status
git branch -M main
git remote add origin https://github.com/AdiBhushan10/End2End-LLM-NLP-Deploy-Using-MLFlow.git
git remote -v
2. Setup Git global for first time user: user.name and user.email commands to check if registered, else register as
git config --global user.name "AdyBhushan10"
git config --global user.email "<email id>"
3. Push git repo from Origin (local folder) to main (website): use -force push in case of any error
git push -u origin main --force 
4. In case when local file is changed, to recommit changes to remote repo:
git add .
git commit -m "second commit"
git push --set-upstream origin OR git push --force origin HEAD:master

#Just follow next steps in console terminal 
git init	#Initialize git in folder
git add .	#add all files of folder to be pushed
git commit -m "First commit"	#add first commit
git remote add origin remote_repository_URL #replace with your remote repo url
git remote -v	#verify that your remote repository url is properly found
git push --force origin HEAD:master	#force pushing your project into github repo

To able package your model as an application, create setup.py. This file describes our model to Distutils function.

If current set remote repo is failed or in error:
git remote set-url origin <new name> e.g. https://github.com/AdiBhushan10/End2End-LLM-NLP-Deploy-Using-MLFlow.git
git init, add, ccommit message, git push -u origin my-feature-branch
