check 

```bash
lsb_release -a
```
version should be greater than 16


```bash
sudo apt-get update
```
```bash
sudo apt install docker.io
```
```bash
sudo systemctl enable docker
```
```bash
sudo systemctl status docker
```

**IF service not active**

```bash
sudo systemctl start docker
```


check 

```bash

sudo docker run hello-world
```