# Switch Github Accounts  
eval$(ssh-agent -s)  
ssh-add ~/.ssh/<private_key>  
ssh -T git@github.com