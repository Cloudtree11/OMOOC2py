# **GitHub 本地配置**
OS: Ubuntu 14.04
## **配置本地 GitHub 环境**

1.查看 ～/.ssh 目录下未有 SSH 公钥，`ssh-keygen -t rsa -C "mail adress"`生成本地公钥。
```
cloudtree@cloudtree-QTP6:~$ cd ~/.ssh
bash: cd: /home/cloudtree/.ssh: No such file or directory
cloudtree@cloudtree-QTP6:~$ ssh-keygen -t rsa -C "yunkun233@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/cloudtree/.ssh/id_rsa): 
Created directory '/home/cloudtree/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/cloudtree/.ssh/id_rsa.
Your public key has been saved in /home/cloudtree/.ssh/id_rsa.pub.
The key fingerprint is:
……
```

2.添加公钥到个人 GitHub 账户：个人GitHub网页“Settings -> SSH keys -> Add SSH key”，复制～/.ssh/id_rsa.pub内容到其中。

3.`ssh -T git@github.com`验证配置是否生效。
```
cloudtree@cloudtree-QTP6:~$ ssh -T git@github.com
The authenticity of host 'github.com (192.30.252.131)' can't be established.
RSA key fingerprint is ……
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.131' (RSA) to the list of known hosts.
Hi Cloudtree11! You've successfully authenticated, but GitHub does not provide shell access.
```

4.`git config --global user.name "username"`和`git config --global user.email "email adress"`设置 username 和 email。
```
cloudtree@cloudtree-QTP6:~$ git config --global user.name "Cloudtree11"
cloudtree@cloudtree-QTP6:~$ git config --global user.email "yunkun233@gmail.com"
```


---

参考：
[Linux下的GitHub安装与简单配置教程](http://www.cnblogs.com/smilejinge/p/3589479.html)
