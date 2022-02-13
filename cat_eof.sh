#!/usr/bin/bash
cat <<EOF > start.sh
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
git remotes -v 
# git clone git@github.com:lightarrow/auto-deploy.git --depth 10
#git add cat_eof.sh
#add ssh key on new session. 
# make sure its running
eval "$(ssh-agent -s)"
#add key
ssh-add ~/.ssh/my_private_key 
#promts for key passphrase
EOF