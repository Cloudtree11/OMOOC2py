# **Git 简单操作**
OS: Ubuntu 14.04
## **简易 Git 操作**

1.`git clone`克隆已有分支到本地。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py$ git clone https://github.com/Cloudtree11/OMOOC2py.git
Cloning into 'OMOOC2py'...
remote: Counting objects: 118, done.
remote: Total 118 (delta 0), reused 0 (delta 0), pack-reused 118
Receiving objects: 100% (118/118), 14.16 KiB | 0 bytes/s, done.
Resolving deltas: 100% (21/21), done.
Checking connectivity... done.
```
注意：可以有两种获取远程仓库的方式：https 和 ssh
https 方式：`git clone https://github.com/Cloudtree11/OMOOC2py.git`
ssh 方式：`git clone git@github.com:Cloudtree11/OMOOC2py.git`
两个方式的url地址不同，认证方式也不同。ssh 方式保存密钥对以后提交修改可以不再输入帐号密码，而 https 方式每次都需要输入用户名和密码。

2.`git status`查看本地已修改的文件。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```
3.`git diff`查看本地已修改内容。
```
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
```
4.`git add`添加本地修改文件，`git commit"`提交修改到本地仓库，`git push`将修改推送至远程仓库。经由此三步，本地的修改就同步到服务器上了。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git add .
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git commit -m "First commit test!"
[master 63372f3] First commit test!
 1 file changed, 2 insertions(+)
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ git push orignal master
```
---
参考

[ubuntu 下 github 简单的使用教程](http://blog.chinaunix.net/uid-29040159-id-3799719.html)

[让git push命令不再每次都输入密码](http://yansu.org/2013/04/22/ignore-password-in-git-push.html)
