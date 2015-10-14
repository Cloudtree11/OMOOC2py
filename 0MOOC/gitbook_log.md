## GitBook

## 安装 GitBook
参考：
[我的GitBook笔记](http://yanhaijing.com/tool/2015/09/12/my-gitbook-note/)

安装 npm。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ sudo apt-get install npm
```

安装 nodejs ，提示已经安装。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ sudo apt-get install nodejs
Reading package lists... Done
Building dependency tree
Reading state information... Done
nodejs is already the newest version.
nodejs set to manually installed.
The following package was automatically installed and is no longer required:
  linux-image-generic
Use 'apt-get autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 665 not upgraded.
```

nodejs 查看版本出错，按提示安装 nodejs-legacy。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ node -v
The program 'node' can be found in the following packages:
 * node
 * nodejs-legacy
Try: sudo apt-get install <selected package>
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py_gitbook/omooc2py$ sudo apt-get install nodejs-legacy
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following package was automatically installed and is no longer required:
  linux-image-generic
Use 'apt-get autoremove' to remove it.
The following NEW packages will be installed:
  nodejs-legacy
```

nodejs 安装成功。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ nodejs -v
v0.10.25
```

安裝 gitbook-cli。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ sudo npm install -g gitbook-cli
```

克隆 GitBook 仓库到本地，有可能出错，尝试几次。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py_gitbook$ git clone https://www.gitbook.com/book/cloudtree/omooc2py.git
Cloning into 'omooc2py'...
fatal: unable to access 'https://www.gitbook.com/book/cloudtree/omooc2py.git/': gnutls_handshake() failed: A TLS packet with unexpected length was received.
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py_gitbook$ git clone https://git.gitbook.com/cloudtree/omooc2py.git
Cloning into 'omooc2py'...
Username for 'https://git.gitbook.com': Cloudtree
Password for 'https://Cloudtree@git.gitbook.com': 
remote: Counting objects: 118, done.
remote: Compressing objects: 100% (76/76), done.
remote: Total 118 (delta 21), reused 118 (delta 21)
Receiving objects: 100% (118/118), 14.16 KiB | 0 bytes/s, done.
Resolving deltas: 100% (21/21), done.
Checking connectivity... done.
```

`gitbook -V`查看 gitboot-cli 版本,`gitbook -h`查看命令帮助。
```
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook -V
0.3.6
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook -h

  Usage: gitbook [options] [command]


  Commands:

    versions                          list installed versions
    versions:print                    print current version to use in the current directory
    versions:available                list available versions on NPM
    versions:install [version]        force install a specific version of gitbook
    versions:link [version] [folder]  link a version to a local folder
    versions:uninstall [version]      uninstall a specific version of gitbook
    help                              list commands for a specific version of gitbook
    *                                 run a command with a specific gitbook version

  Options:

    -h, --help               output usage information
    -V, --version            output the version number
    -v, --gitbook [version]  specify GitBook version to use
    -d, --debug              enable verbose error
```

`gitbook versions`查看 GitBook 版本，发现没有安装，使用`gitbook versions:install latest`安装最新版本。
```
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook versions
There is no versions installed
You can instal the latest version using: "gitbook versions:install latest"
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook versions:install latest
```
服务器连接出错，再次尝试。
```
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook versions:install latest
Installing GitBook 2.4.3
-
Error: socket hang up
```

安装过程报错，Google 后参考[此处](https://github.com/npm/npm/issues/5869)修改.npm 权限，问题解决。
```
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook versions:install latest
Installing GitBook 2.4.3
-
Error: EACCES, mkdir '/home/cloudtree/.npm/_git-remotes/_templates'
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook versions:install latest
Installing GitBook 2.4.3
|
Error: EACCES, mkdir '/home/cloudtree/.npm/_git-remotes/_templates'
cloudtree@cloudtree-QTP6:/usr/local/bin$ sudo chown -R $USER:$GROUP ~/.npm
[sudo] password for cloudtree: 
cloudtree@cloudtree-QTP6:/usr/local/bin$ gitbook versions:install latest
Installing GitBook 2.4.3
gitbook@2.4.3 ../../../tmp/tmp-8928cczMTEYX8fBB/node_modules/gitbook
├── bash-color@0.0.3
```

`gitbook build`本地生成书目，提示出错，使用`gitbook install`安装插件。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py_gitbook/omooc2py$ gitbook build .
info: loading book configuration....OK 
info: load plugin disqus ....ERROR
info: load plugin gitbook-plugin-highlight ....OK 

Error: Error loading plugins: disqus. Run "gitbook install" to install plugins from NPM.
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py_gitbook/omooc2py$ gitbook install
info: 1 plugins to install 
info: No version specified, resolve plugin disqus 
info: install plugin disqus from npm (gitbook-plugin-disqus) with version 0.0.2 
gitbook-plugin-disqus@0.0.2 node_modules/gitbook-plugin-disqus
info: >> plugin disqus installed with success 

Done, without error
```

`gitbook build`本地生成书目成功。
```
cloudtree@cloudtree-QTP6:~/Code/OMOOC2py/OMOOC2py$ gitbook build .
info: loading book configuration....OK 
info: load plugin gitbook-plugin-disqus ....OK 
info: load plugin gitbook-plugin-highlight ....OK 
info: >> 2 plugins loaded 
info: start generation with website generator 
info: clean website generatorOK 
info: generation is finished 

Done, without error
```

