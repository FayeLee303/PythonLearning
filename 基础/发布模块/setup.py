from distutils.core import setup

setup(name= "test",    # 包名
      version="1.0",   # 版本
      description="test for message",  # 描述信息
      long_description="测试发布模块",   # 完整信息
      author="faye",   # 作者
      author_email="fayelee303@163.com",   # 作者邮箱
      url="www.fayelee.com",   # 主页
      py_modules=["m_message.receive_message",
                  "m_message.send_message"]
      )
