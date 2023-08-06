# nonebot_plugin_xiuxian_GCDI
修仙模拟器--QQ-群与QQ频道数据互通
## 简介

本插件主要为实现群聊修仙功能,最近经常封号，请自行判断后再使用，已默认转成图片模式，如需关闭，可在config.py处调整img字段为false
并适配了频道与群聊数据互通

## 设定征集中，有好的想法可以推送给我哦~~~

## 安装
1、下载插件文件

- 使用github处拉取源码使用
无镜像：
```
git clone https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI
```
镜像：https://ghproxy.com/
```
git clone https://ghproxy.com/https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI
```

2、下载数据文件

使用git clone后，进入插件目录，把data文件夹中的全部内容移动到bot的数据文件夹中<br>

3、安装频道补丁：

```
频道补丁
pip install nonebot_plugin_guild_patch -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

4、如果遇到问题，请先百度和查看下方的 【一些问题】

5、如解决不了进交流群：588907147 提问，提问请贴上完整的日志

## 配置文件
1、配置文件一般在data/xiuxian文件夹下，自行按照json格式修改即可，一些字段的含义可以进群交流<br>
2、子插件的配置会在插件运行后在子插件文件中生成config.json文件，该文件字段含义在同级目录的xxxconfig.py有备注。注意：修改配置只需要修改json即可，修改.py文件的话需要删除json文件才会生效，任何修改都需要重启bot

## 更新
使用github处拉取源码使用的
进入插件目录执行命令：
```
git pull
```


## 群聊与频道部分功能展示

![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E7%BE%A4%E8%81%8A%E7%B4%A0%E6%9D%901.png)
![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E7%BE%A4%E8%81%8A%E7%B4%A0%E6%9D%902.png)
![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E9%A2%91%E9%81%93%E7%B4%A0%E6%9D%901.png)
![image](https://raw.githubusercontent.com/QingMuCat/qm/master/xiuxian/%E9%A2%91%E9%81%93%E7%B4%A0%E6%9D%902.png)
## 一些问题

- 当前首次使用，未自动创建json文件及sql文件，请在[github](https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI)处，目录data -> xiuxian
处下载的文件，放置于bot目录，data -> xiuxian文件夹处
- 当为放置为plugins目录使用时，请修改根目录下__init__.py文件中的42行：src=''中的内容，填写的是存放插件的目录，一般情况下 src='src.plugins.'  如有不同请按照格式修改
## 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)：本插件实装的开发框架，NB天下第一可爱。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：稳定完善的 CQHTTP 实现。
- [nonebot_plugin_xiuxian](https://github.com/s52047qwas/nonebot_plugin_xiuxian)：原版修仙

## 插件依赖

- nonebot2
- nonebot-adapter-onebot
- go-cqhttp

## 支持

大家喜欢的话可以给这个项目点个star

有bug、意见和建议都欢迎提交 [Issues](https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI/issues) 
或者联系进入QQ交流群：588907147

## 许可证
本项目使用 [MIT](https://choosealicense.com/licenses/mit/) 作为开源许可证
