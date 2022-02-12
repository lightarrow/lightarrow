git config --global user.name ${name}
git config --global user.email ${email} 
git clone git@github.com:lightarrow/auto-deploy.git
echo "# auto-deploy" >> README.md
git init
git add README.md
message='starting'
git commit -m "${message}"
git branch -M main
git remote add origin git@github.com:lightarrow/auto-deploy.git
git push --set-upstream origin main


