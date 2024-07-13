# Using Git Inside Docker: Enhancing Flexibility and Security
## Ideal Use Cases:

### ● Multiple Accounts Management: Enables seamless code push operations across different accounts without altering default configuration details.

### ● Remote Access: Facilitates secure access to your Git repositories from remote or unfamiliar devices by leveraging contained environments.

### ● Efficient Remote Machine Operations: Ensures consistent and secure repository management on remote machines, maintaining data integrity and security protocols.
#
#
## ✪ FIRST OPEN THE TERMINAL 

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"

```
PLACE YOUR EMAIL in the ```your_email@example.com``` which is used in github
![alt text](<Screenshot 2024-07-13 232411-1.png>)

***GO TO THE PATH SHOWN THERE***

![alt text](<Screenshot 2024-07-13 232827.png>)


***COPY THESE TWO FILES IN THE SAME DIRECTORY OF THE IDE WHICH CONTAINS CODE***


![alt text](<Screenshot 2024-07-13 233347.png>)



**! NOW OPEN THE ```id_ed25519.pub```**

**AND COPY THE SHA KEY IN THAT**

**FOR EXAMPLE** 

```ssh-ed25519AAAAC3NzaC1lZD63NTE5AAAAIGgRRTk93ulHM0wJ48mnpAzByB89Qn/ERVdppblKx123 yourname@gmail.com```



 ## ✪ SECOND GO TO GITHUB

 ### GO TO SETTINGS AND  UNDER ``SSH and GPG keys`` 

 **CLICK NEW ``SSH KEY``**

![alt text](<Screenshot 2024-07-13 234116.png>)


**After that Make a ``dockerfile`` in your directory**
AND paste the content form the Dockerfile

#
 ## ✪ THIRD OPEN TERMINAL IN THE SAME DIRCTORY AS THE CODE

 **MAKE SURE YOU HAVE DOCKER DESKTOP RUNNING IN BACKGROUND**

**IN TERMINAL PASTE THE FOLLOWING COMMANDS**

```bash
docker build -t test  .
```
replace the name ``test`` with your desired name and also change it iin further use case 


```bash
docker run -d -it --rm -v ${PWD}:/workspace test
```

```bash
docker ps 
```
**COPY THE CONTAINER ID (first 3-4char are fine)**

```bash
docker exec -it <container_id> sh
```

#### NOW YOU SHOULD BE IN THE WORKSPACE ```/workspace #```  
```bash
git init
```
```bash
git checkout -b main
```
```bash
git add .
```
**GO TO GITHUB AND GET THE SSH LINK**

![alt text](<Screenshot 2024-07-14 003236.png>)

```bash
git remote add origin git@github.com:yourusername/final.git
```

replace ```git@github.com:yourusername/final.git``` with your ssh 


```bash
 git rm --cached id_ed25519
 ```
```bash
 git rm --cached id_ed25519.pub
 ```

 ```bash
 git config --global user.email "you@example.com"
 ```
-your github email
 ```bash
  git config --global user.name "userName"
```
-your github username
```bash
git commit -m "your message"
```
```bash
 git pull origin main --allow-unrelated-histories
 ```

 ```bash
  git push origin --force --all
```

If you get error then try 
```bash
git config pull.rebase true
```
and then again push 

**GO TO GITHUB AND RELOAAD YOU MIGHT SEE THE RESULT**

****IGNORE THE COMMIT MESSSAGE IN THE IDE IT WILL SAY AS NOT PUSHED BUT IT IS DONE FROMT THE DOCKER****
#
#
#


**IF PROBLEM PERSISTS TRY DOING THIS**
```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch id_ed25519 id_ed25519.pub' --prune-empty --tag-name-filter cat -- --all
```

```bash
rm -rf .git/refs/original
```

```bash
git reflog expire --expire=now --all
```

```bash
git gc --prune=now
```

```bash
git gc --aggressive --prune=now
```

```bash
git push origin --force --all
```
