---
title: "CUDA torch"
date: 2022-06-20T12:00:30-13:00
categories:
  - blog
tags:
  - Python
  - PyTorch
---
refered from: [CSDN]
Server `GPU`:
```ruby
# 查看CPU信息
cat /proc/cpuinfo | grep "physical id" | uniq | wc -l #查看CPU个数
cat /proc/cpuinfo | grep "cpu cores" | uniq #查看CPU核数
cat /proc/cpuinfo | grep 'model name' |uniq #查看CPU型号
```

Find the exact information of GPU devices:
```ruby
# 查看GPU信息
sudo dpkg --list | grep nvidia-* # 查看驱动版本
lshw -c video #查看显卡型号
$ lspci | grep -i nvidia # 可以查询所有nvidia显卡
$ lspci -v -s [显卡编号] # 可以查看显卡具体属性
$ nvidia-smi # 可以查看显卡的显存利用率
$ cat /etc/issue # 查看Linux发布版本号
$ lsb_release -a # 查看Linux发布版本号
$ uname -sr # 查看内核版本号
$ uname -a # 查看内核版本号
```


```ruby
$ watch -n 1 nvidia-smi
```
`torch.cuda` main functions: (example)
```ruby
torch.cuda.is_available() # 查看是否有可用GPU
torch.cuda.device_count() # 查看GPU数量
torch.cuda.get_device_capability(device) # 查看指定GPU容量
torch.cuda.get_device_name(device) # 查看指定GPU名称
torch.cuda.empty_cache() # 清空程序占用的GPU资源
torch.cuda.manual_seed(seed) # 设置随机种子
torch.cuda.manual_seed_all(seed) # 设置随机种子
```
chose the specified CUDA device:
```ruby
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "2,1,3,4"
print("torch.cuda.device_count() {}".format(torch.cuda.device_count()))
```

[CSDN]: https://blog.csdn.net/weixin_39059031/article/details/111661128