### 코드 목적 ###
## 4 가지 분류 기법 알아보기
# 1. 이진 분류
# 2. 다중 분류
# 3. 다중 레이블 분류
# 4. 다중 출력 분류

### 코드 순서 ###
# 1. 데이터 준비
# 2. 데이터 전처리
# 3. 이진분류
# 3.1 
# 4. 다중 분류
# 4.
# 5. 다중 레이블 분류
# 5.
# 6. 다중 출력 분류
# 6.

## 1. 데이터 준비 

# 파이썬 2와 파이썬 3 지원
from __future__ import division, print_function, unicode_literals

# 공통
import numpy as np
import os

# 일관된 출력을 위해 유사난수 초기화
np.random.seed(42)

# 오픈 데이터셋에서 fetch_openml 데이터 가져오기.
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1)
print(mnist)