# GitHub
OS:Ubuntu 14.04
## 配置本地 GitHub 环境
参考：
[Linux下的GitHub安装与简单配置教程](http://www.cnblogs.com/smilejinge/p/3589479.html)
或[ubuntu 下 github 简单的使用教程](http://blog.chinaunix.net/uid-29040159-id-3799719.html)

发现缺少 ssh 公钥，使用 ssh-keygen 生成公钥。
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

添加公钥到 GitHub 账户后，验证配置是否生效。
```
cloudtree@cloudtree-QTP6:~$ ssh -T git@github.com
The authenticity of host 'github.com (192.30.252.131)' can't be established.
RSA key fingerprint is ……
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.131' (RSA) to the list of known hosts.
Hi Cloudtree11! You've successfully authenticated, but GitHub does not provide shell access.
```

设置 username 和 email。
```
cloudtree@cloudtree-QTP6:~$ git config --global user.name "Cloudtree11"
cloudtree@cloudtree-QTP6:~$ git config --global user.email "yunkun233@gmail.com"
```
## Git 操作

克隆已有分支到本地。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py$ git clone https://github.com/Cloudtree11/OMOOC2py.git
Cloning into 'OMOOC2py'...
remote: Counting objects: 118, done.
remote: Total 118 (delta 0), reused 0 (delta 0), pack-reused 118
Receiving objects: 100% (118/118), 14.16 KiB | 0 bytes/s, done.
Resolving deltas: 100% (21/21), done.
Checking connectivity... done.
```

使用 git 命令提交修改。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git diff
diff --git a/README.md b/README.md
index 7bf92a4..444a092 100644
--- a/README.md
+++ b/README.md
@@ -6,3 +6,5 @@
 
 - 一个 gitbook 最小图书框架
 - 一个 配合课程每周开发任务的目录树
+
+Hello Gitboot!
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ vi README.md 
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git add .
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git commit -m "First commit test!"
[master 63372f3] First commit test!
 1 file changed, 2 insertions(+)
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git push orignal master
```
