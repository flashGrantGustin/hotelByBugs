
from DrissionPage import ChromiumPage
from DrissionPage import SessionPage
from DrissionPage import WebPage
from DrissionPage import ChromiumOptions
from DataRecorder import Recorder
import csv
import time
import http_Proxy


# 创建记录器对象
recorder = Recorder('dataall.csv')
# 打开CSV文件，并创建一个CSV reader对象  
recorder.add_data(('酒店名称','未预定房间数量','已预定房间数量'))
with open('data.csv', 'r', newline='') as file:  
	reader = csv.reader(file)  
      
	# 遍历CSV文件的每一行  	
	while True:
		for row in reader:  
	    # row是一个列表，包含了当前行的所有字段 
	    # 创建页面对象
			page = ChromiumPage()
			page.get(str(row)[2:-2])
			name = page.ele('.base').child(1).text
			list1 = page.eles('报价列表')
			list2 = page.eles('全部订完')
			print(str(name)+'的报价列表是'+str(len(list1))+'个')
			print(str(name)+'的全部订完是'+str(len(list2))+'个')
			recorder.add_data((str(name),str(len(list1)),str(len(list2))))
			time.sleep(4)
print('处理完成')
recorder.record()

 
        
        
