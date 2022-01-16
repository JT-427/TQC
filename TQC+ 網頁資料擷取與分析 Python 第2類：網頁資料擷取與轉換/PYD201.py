# 載入模組
import requests
import re

url = 'http://tqc.codejudger.com:3000/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    intput_ = input("請輸入欲搜尋的字串 : ")
    find_ = re.findall(intput_, htmlfile.text)
    if intput_ in htmlfile.text:
        print(intput_, "搜尋成功")
        print(intput_, "出現 %d 次" % len(find_))
    else:
        print(intput_, "搜尋失敗")
        print(intput_, "出現 0 次")
else:
    print("網頁下載失敗")
