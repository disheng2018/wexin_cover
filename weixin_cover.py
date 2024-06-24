# -*- coding: utf-8 -*-
# @Author: zhang zicheng
# @Date:   2024-06-24 12:11:38
# @Last Modified by:   zhang zicheng
# @Last Modified time: 2024-06-24 12:23:06
import requests
import re
import streamlit as st

st.title('公众号封面提取')
st.subheader("【基于Streamlit搭建】")

# url = 'https://mp.weixin.qq.com/s/d7DUHB-hT8DExjpxsEncQw'
url = st.text_input('请输入公众号文章链接：')

if st.button('提交'):
    if url:
        response = requests.get(url)

        if response.status_code == 200:
            # print(response.text)

            source_code = response.text
            url_pattern = re.compile(r'cdn_url_1_1 = "(.*?)"')
            matches = url_pattern.findall(source_code)
            if matches:
                st.write(f"封面链接（请点击链接打开或保存）：\n{matches[0]}")
                # st.image(matches[0])
            else:
                st.write("没找到封面图网址！")
    else:
        st.write("请输入有效的公众号链接！")
