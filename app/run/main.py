"""
    这里针对的是我们的GPA进行WES换算的程序
    这里是已经写好的 但是我们需要想办法进行动态登陆过程
    使用selenium方法实现动态登陆
"""

# 加载我们需要的模块
import Scrapy


def rundemo(name,pwd):
    df = Scrapy.scrapyData(name,pwd)

    """
        下列的是我们对代码进行比较大的程度的修改
        我们不能是简单的将绩点进行WES的简单转换 我们应该先对五个学期的成绩进行分类 然后再计算每一个学科的平均成绩进行计算 再做个图
    """
    # 我们需要的一共是三列 第一列是课程名称 第二列是绩点 第三列是学分
    # 因为我们需要先对数据进行处理 所以我们可以先把课程名称和绩点作为字典
    # key:课程名称 values:字典
    column_dict = dict(zip(df['课程名称'],df['学分']))
    list1 = ["军事理论与训练","形势与政策","大学生职业生涯与规划","体育1","体育2","体育3","体育4"]
    list2 = ["思想道德修养与法律基础","政治经济学","中国近现代史纲要","毛泽东思想和中国特色社会主义理论体系概论","马克思主义基本原理概论","书法鉴赏","道德修养和法律基础","英语口语"]
    for key in column_dict.keys():
        if key in list1:
            column_dict[key] = 0.0
        elif key in list2:
            column_dict[key] = 1.0
        elif key in ["大学英语1","大学英语2","大学英语3","大学英语4"]:
            column_dict[key] = 2.0
    # print(column_dict)
    # 我们修改完学分之后需要对此成绩列做对应 我们可以把学分列取出来 然后和成绩共同组成一个列表
    # w为了保证正确 我们可以现判断一下长度是否一致
    print(column_dict)
    list3 = []
    for val in column_dict.keys():
        list3.append(float(column_dict[val]))
    # 我们接下来需要根据成绩修正绩点
    list4 = []
    for tem in df['成绩']:
        if tem in ['优','良','中','合格','及格','不及格']:
            # 此时说我们该项课程的成绩是五级分制
            if tem == "优":
                list4.append(4)
                continue
            elif tem =='良':
                list4.append(3)
                continue
            elif tem =='中':
                list4.append(2)
                continue
            elif tem =='及格' or tem =='合格':
                list4.append(2)
                continue
            else:
                list4.append(0)
                continue
        else:
            tem =  float(tem)
            if tem >= 85:
                list4.append(4)
            elif tem>=75 and tem <= 84:
                list4.append(3)
            elif tem>=60 and tem <=74:
                list4.append(2)
            elif  tem <60:
                list4.append(0)
    # print(list4)
    # 我们现在已经得到修正过后的绩点列 现在把学分和绩点整合到一个list中
    # print(list3)
    list_final = [list4,list3]
    sum_score=0.0
    for i in list3:
        sum_score+=i
    print(sum_score)
    sum = 0.0
    for i in range(0,len(list4)):
        sum += list_final[0][i] * list_final[1][i]
    print(sum)
    # final是WES绩点计算系统的值
    final = float(sum)/float(sum_score)
    print(">>>欢迎来到XXX的WES绩点换算系统>>>")
    print(final)
    return final







