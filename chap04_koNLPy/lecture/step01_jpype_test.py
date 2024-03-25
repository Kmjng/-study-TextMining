# -*- coding: utf-8 -*-
"""
java 가상 머신 사용을 위한 패키지 설치 
"""

import jpype

path = jpype.getDefaultJVMPath() #자바버츄얼머신

print(path)
# C:\Program Files\Java\jdk-19\bin\server\jvm.dll