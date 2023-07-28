# burp_jsonx

用于自动化处理burp返回的json格式数据

格式化后，自动索引节点并提供选择，选择特定的节点可以写入CSV文件，方便后续操作

1、发送请求包得到burp的响应，将响应包保存成txt文本文件

![image](https://github.com/source-xu/burp_jsonx/assets/56073532/dc1f93ba-8666-48f9-befa-0a2392305393)

2、选择存储多个数据的节点如list:[["name":"zhangsan","age":21],["name":"lisi","age":22]]
![image](https://github.com/source-xu/burp_jsonx/assets/56073532/fc1defd8-afdc-4d48-9fc9-dfe2dd1582b7)

3、自动识别该节点子元素个数和字段并写入csv文件中
![image](https://github.com/source-xu/burp_jsonx/assets/56073532/925cd984-64a5-4c06-8583-8e748b68576b)

![image](https://github.com/source-xu/burp_jsonx/assets/56073532/064f0c70-ecc8-4688-a04f-5ce899510a69)

![image](https://github.com/source-xu/burp_jsonx/assets/56073532/b0443060-169a-46f1-8397-fa452bceb3c5)

