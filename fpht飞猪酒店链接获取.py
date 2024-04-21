
from DrissionPage import ChromiumPage
from DrissionPage import SessionPage
from DrissionPage import WebPage
from DrissionPage import ChromiumOptions
from DataRecorder import Recorder

# 创建页面对象
page = ChromiumPage()
# 创建记录器对象
recorder = Recorder('data.csv')
page.get('https://hotel.fliggy.com/hotel_list3.htm?_input_charset=utf-8&_output_charset=utf-8&searchBy=&market=0&previousChannel=&cityName=%E8%A5%BF%E5%AE%89&city=610100&_fmd.h._0.r=&checkIn=2024-03-25&checkOut=2024-03-26&keywords=%E7%94%B5%E7%AB%9E')
while True:
    print('开始处理')
    for mov in page.eles('查看详情'):
        recorder.add_data(mov.href)
    # 获取下一页按钮，有就点击
    btn = page('下一页', timeout=2)
    print('完成一条')
    if btn.parent(1).tag!='span':
        btn.click()
        page.wait.load_start()
    # 没有则退出程序
    else:
        break
print('处理完成')
recorder.record()
