# 土木在线标准

本项目将土木工程的相关标准电子化，方便查阅和学习。通过PaddleOCR-VL对PDF格式的标准进行文字识别和排版，生成Markdown格式的电子文档。

## 特性

 - 数学公式的latex复制
 - 公式、章节跳转

## 收录的标准
---

 - [x] 《钢结构设计标准》GB 50017-2017
 - [x] 《混凝土结构设计规范》GB 50010-2010
 - [ ] 《建筑结构荷载规范》GB 50009-2012
 - [x] 《建筑抗震设计规范》GB 50011-2010
 - [ ] 《工程结构通用规范》GB 55001-2021

## PaddleOCR-VL 使用 ([官方文档](https://www.paddleocr.ai/main/version3.x/pipeline_usage/PaddleOCR-VL.html))
---

### 直接使用官方网站上传文件识别

现在官方出了在线文档识别服务：https://aistudio.baidu.com/paddleocr

可以直接上传文件进行识别，识别结果可以下载为Markdown格式。不是大量文件识别的话，可以直接使用这个服务。自己搭建服务的话，使用下面的Autodl云端方式。

### Autodl云端使用步骤

#### Autodl租用服务器并克隆镜像

如果不熟悉Autodl怎么租服务器，需要去查一下官方资料。

在社区镜像中搜索`PaddlePaddle/PaddleOCR/PaddleOCR-VL-WEB`这个镜像，然后克隆开卡。


#### 执行任务

 1. 将本地的`client_vllm.py`和`files_in`文件夹拖拽上传到远程服务器的目录下
 1. 在命令行运行下列命令启动API服务（`VScode`中`ctrl+~`就可以添加终端）：
    ```bash
    paddlex_genai_server --model_name PaddleOCR-VL-0.9B --backend vllm --port 8118
    ```
    看到最后一行`Application startup complete.`表示运行成功
 1. 打开一个新的终端窗口，运行下列命令调用`client_vllm.py`执行任务：
    ```python
    python client_vllm.py --in_dir "./files_in" --out_dir "./output" --skip_processed
    ```
    其中`--in_dir`参数指定输入文件夹路径，`--out_dir`参数指定输出文件夹路径，会提取文件夹所有的pdf文件进行识别，`--skip_processed`参数表示跳过已经处理过的文件（即输出目录中已经存在对应结果文件的文件）
 1. 任务完成后，识别结果会保存在`output`文件夹中
 1. 通过`scp`命令或者`VScode`下载`output`文件夹到本地电脑。在本地电脑输入类似下面的`scp`命令（假设Autodl服务器SSH端口是`43668`，从Autodl实例可以复制具体的登录指令查看端口）：
    ```bash
    scp -rP 43668 root@connect.westc.gpuhub.com:"/root/output/*" <本地文件/文件夹>
    ```


#### （可选）通过VScode远程连接Autodl服务器下载文件

`jupyterlab`下载不了文件夹，只能下载文件

 - 打开`VScode`，安装`Remote - SSH`插件
 - 点击左下角的绿色按钮，选择`Remote-SSH: Connect to Host...`
 - 输入Autodl服务器的SSH连接信息，就是在Autodl实例界面的登录指令比如`ssh -p 9090 root@connect.westc.gpuhub.com`，连接到服务器
 - 中间需要输入密码，也在Autodl实例界面可以复制
 - 然后可以进入根目录
 - 可以在命令行测试`pip show paddleocr`，如果能显示版本信息说明连接成功

### 本地电脑使用

简单的文档可以运行，但是复杂的文件会内存爆满导致死机。

 1. 命令行中启动容器：
    ```bash
    docker run -it -p 9001:9001 --gpus all --user root ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddleocr-vl:latest-offline /bin/bash
    ```
 1. 进入`PaddleOCR-VL`容器
     - 从`VScode`的`Container`插件`Attach Visual Studio Code`进入容器
     - 进入`/PaddleOCR-VL`目录
 2. 将需要识别的文件和代码文件`clent_demo.py`放入`/PaddleOCR-VL/`目录下
 3. 执行代码
     - 从命令行运行代码
        ```bash
        python client_demo.py
        ```
     - 识别结果会保存在`/PaddleOCR-VL/`目录下的`output`文件夹中
     - 右键下载`output`文件夹到本地

## MkDocs搭建电子书网站
---

### 生成静态文件
   1. 安装MkDocs和Material主题
      ```bash
      pip install mkdocs-material
      ```
   2. 在项目根目录下创建`mkdocs.yml`配置文件，参考本项目中的`Books/mkdocs.yml`
   3. 在项目根目录下创建`docs`文件夹，将Markdown文件放入`docs`文件夹中，参考本项目中的`Books/docs/`
   4. 在`mkdocs.yml`文件中添加目录`nav`，参考本项目中的`Books/mkdocs.yml`
   5. 数学公式支持，需要修改`mkdocs.yml`文件和添加`javascript`文件，参考本项目中的`Books/mkdocs.yml`和`Books/docs/javascripts/config.js`
   6. 运行本地预览
      ```bash
      cd Books
      mkdocs serve
      ```

### 部署到服务器

   1. `1panel`中创建一个新的网站，设置域名`standards.youtian95.cn`，选择`静态网站`类型
   2. 阿里云中解析域名`standards.youtian95.cn`到服务器IP地址
   3. 如果阿里云安全组没有开放`80`和`443`端口，需要去阿里云控制台开放这两个端口
   4. `1panel`中申请SSL证书，验证方式选择`DNS验证`
   5. `1panel`网站启用`https`，SSL选择刚才申请的证书
   6. 直接执行`deploy.py`脚本部署
      ```bash
      cd Books
      python deploy.py
      ```
      或者手动部署：
      1. 生成静态文件
         ```bash
         mkdocs build
         ```
      2. 上传`site`文件夹到服务器网站根目录，可以使用SCP命令上传
         ```bash
         # 先清空远程目录，再上传新文件
         ssh -i "C:/Users/youti/.ssh/id_ed25519_1panel" root@youtian95.cn "rm -rf /opt/1panel/www/sites/standards.youtian95.cn/index/*"
         scp -r -i "C:/Users/youti/.ssh/id_ed25519_1panel" ./site/* root@youtian95.cn:/opt/1panel/www/sites/standards.youtian95.cn/index/
         ```
         其中`-i`参数指定SSH密钥文件路径，id_ed25519_1panel密钥文件的本地路径在`1panel`中找到