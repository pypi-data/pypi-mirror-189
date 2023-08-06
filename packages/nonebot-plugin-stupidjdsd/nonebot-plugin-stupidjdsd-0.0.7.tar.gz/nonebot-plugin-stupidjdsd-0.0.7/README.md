<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>
<div align="center">
A plugin for dealing with JDSD of Guangzhou University！
<br><br><a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Monarchdos/nonebot_plugin_soup.svg" alt="license">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</a>


</div>

## 📖 介绍

<br />广州大学的经典诵读为广大青年带来了不可描述的烦恼
<br />为了解决这个大家的这个烦恼
<br />我在过去两个月里致力于寻找各种更加简便的方式
<br />这是其中之一！

## 💿 安装

**使用 nb-cli 安装**  
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装  

```bash
nb plugin install nonebot-plugin-stupidjdsd
```

**使用 pip 安装**  
```bash
pip install nonebot-plugin-stupidjdsd
```

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入
```python
nonebot.load_plugin('nonebot-plugin-stupidjdsd')
```
注意:在版本更新后可以手动生成bot.py这个入口文件，但是不生成这个也是可以的~

## 🎉 使用

  <br />1.第一次使用本插件需要绑定Key，寻找Key的方法放在了[这里](https://liu1272.github.io/2023/01/07/20220107/)
  <br />2.插件默认使用的是不带有匹配和邮件通知功能的
  <br />3.若需要使用匹配功能请在__init__文件中更改被注释的文件路径
  <br />4.若需要使用邮件通知功能请在完成第三步之后按照Original_Script.py文件内的指引更改
  
<table> 
  <tr align="center">
    <th>   触发指令   </th>
    <th>   指令说明   </th>
  </tr>
  <tr align="center">
    <td>   经典诵读   </td>
    <td>   执行脚本   </td>
  </tr>
    <tr align="center">
    <td>   jdsd   </td>
    <td>   执行脚本   </td>
  </tr>
  
  <br />执行脚本后会返回FINISH或ERROR
  <br />若是FINISH则为成功，ERROR则需要检查Key或代码
  
  **如果您有发现bug或是存在任何疑问都可以在issues中提问！**
</table>



## 📝 更新日志

<details>
<summary>展开/收起</summary>

## **2023-02-04 V0.0**


  * 插件制作完毕！

</details>

