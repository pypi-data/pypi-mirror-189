这是一个读写properties工具
示例:见测试用例pr_properties/test_case/test_properties.py

```python
from pr_properties import pr_properties

# 创建Properties对象
p = pr_properties.Properties()
# 读取字符
str_p = """# 读取字符=1
master.initialSize=4
master.minIdle=10=20=kk"""
p.loads(str_p)
# 修改
p['master.initialSize'] = 5
# 增加
p['master.cc'] = 5
# 输出对象的字符
print(p.dumps())
# 删除
del p['master.cc']
print(p.dumps())

# 读取properties文件
p = pr_properties.Properties()
p.read(path=r'./pool.properties')
print(p['master.initialSize'])  # 4
# 修改
p['master.initialSize'] = 5
# 写入,写入后会关闭文件
p.write()
p.read(path=r'D:\WORK\PYTHON\my-python-tools\auto_exe\app\pool.properties')
# 验证是否修改
print(p['master.initialSize'])  # 5
```