设计思路
1. 通过一个list显示所有的脚本
2. 基本的布局为
```
|      脚本信息需要拖拽的文件    |
-------------------
|初始隐藏，拖拽或点击后显示参数输入|
```
3. 脚本的描述通过一个json的描述文件进行控制

实施步骤
1. 尝试写一个基础的页面，不用配置文件，但是点击或拖拽后可以显示
2. 减去download直接下载
3. 如何区分两个item？闭包写入 target 元素 
4. 上传完成后返回的json数据是什么样子的
```
{
    "scriptname":"",
    "uploadfilename":"",
    "detail":{
        "name":"1.py",
        "needargs":True,
        "output":True,
        "args":[
            {
                "id":"",
                "name":"",
                "type":"string",
                "defaultvalue":""
            }
        ]
    }
}
```

5. 产出的文件的下载

{
    "scriptlist":[
        {
            "name":"1.py",
            "id":"000000",
            "desc","desc1111"
        },
        {
            "name":"2.py",
            "id":"000001",
            "desc","desc2222"
        }
    ],
    "itemdetail":{
        "000000":{
            "name":"1.py",
            "needargs":True,
            "output":True,
            "args":[
                {
                    "id":"",
                    "name":"",
                    "type":"string",
                    "defaultvalue":""
                }
            ]
        },
        "000001":{

        }
    }
}

6. 目前已经完成了数据的基本传递，从文件上传到文件的下载，下一步。
剩下的还有什么是未完成的呢。
    a. 文件的拓展 [doing][*] 
        - 参数使用dict
        - 文件名称的处理提取函数
        - 按照新的标准完成脚本的数据，尝试只是文件的复制 OK
    b. 参数的显示
        - 网页显示参数的设置和参数的传递
        - 先网页显示样式,再进行网页的进一步显示 OK
        - 网页动态显示参数 OK
        - 上传之后显示和隐藏的问题 OK
        - 参数添加顺序的问题
    c. 文件的模板的显示
        - 配置档的编写 OK
        - 根据配置档动态生成html [doing]

7. 特效和界面的添加

整体路线
upload -> return script detail -> input agrs -> run script 
-> return result -> start download 

最终效果参考，卡片式
http://cr.kunlun.com/

参考资料：
https://www.html5rocks.com/en/tutorials/file/xhr2/
https://imququ.com/post/a-downloader-with-filesystem-api.html
http://stackoverflow.com/questions/13752984/html5-file-api-downloading-file-from-server-and-saving-it-in-sandbox\
https://scarletsky.github.io/2016/07/03/download-file-using-javascript/
