import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def scrapyData(name,pwd):
    #PATH是我们安装的浏览器驱动路径
    PATH = "../../chromedriver"

    driver = webdriver.Chrome(PATH)

    driver.get("http://jiaowu.dlpu.edu.cn/#")

    search = driver.find_element_by_link_text("教务系统教师学生入口")
    search.send_keys(Keys.RETURN)
    # 我们现在已经进入了登陆页面 接下来我们需要输入自己的学号密码进行登陆
    # Selemium中的waiting属性保证了我们在输入自己的学号密码之前就已经点击了"教务系统教师学生入口"进行登陆
    # 这里我需要解释一下为什么一开始的driver.get中的链接为什么不直接填写登陆页面的url 因为我发现可能是由于教务处人数限制的问题
    # 教务处的登陆页面是会动态更换IP的 反映在标签中：window.open('http://210.30.62.' + (37+parseInt(String(Math.random()).substring(3, 5))%4) + ':8080/jsxsd');

    # 我在这里卡了好久 此处需要注意的问题是由于我们打开了新的tab 所以说此时我们需要对driver进行转换
    # 使用下列的函数 将driver的焦点放到我们的第二个标签页当中
    driver.switch_to.window(driver.window_handles[1])

    # 填充我们的表单

    # 用户名
    username = driver.find_element_by_name("USERNAME")
    username.send_keys(name)

    #密码
    password = driver.find_element_by_xpath(".//*[@id='pwd']")
    password.send_keys(pwd)

    btn = driver.find_element_by_xpath(".//*[@id='btnSubmit']").click()

    # 我们现在已经进入了我们的页面 接下来我们需要拿到我们的成绩页面
    # 成绩查询的 为 class = "block7"

    time.sleep(1)

    step1 = driver.find_element_by_class_name("block7").click()
    time.sleep(1)

    step2 = driver.find_element_by_xpath(".//*[@id='btn_query']").click()

    # 我们现在已经进入到成绩页面

    time.sleep(1)

    # 使用read_html读取html可以帮助我们得到一个比较感觉的表格
    df = pd.read_html(driver.page_source)[0]
    print(df)
    # 写入本地便于我们的后续处理 不用每次都爬一遍
    # 这里路径啊天 我吐了 我咋保存到根目录里面了这里需要改一下
    df.to_csv("../GPA/data.csv",sep=",",index=False)

    # time.sleep(10)
    driver.quit()


    return df
