# Switch Github Accounts  
eval$(ssh-agent -s)  
ssh-add ~/.ssh/<public_key>  
ssh -T git@github.com