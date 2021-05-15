"""
    该py文件是将5个学期的成绩进行分类 再进行作图处理
"""
import pandas as pd
import numpy as np
from matplotlib.figure import Figure



def score_map(tem):
    if tem == "优":
        tem = 90
    elif tem == '良':
        tem = 80
    elif tem == '中':
        tem = 70
    elif tem == '及格' or tem == '合格':
        tem = 60
    elif tem == '不及格':
        tem = 0
    return tem


def scoreSub(series):
    temp = float(series["成绩"]) * float(series["学分"])
    return temp

def countScore(x):
    return sum(x["scoreSub"]) / sum(x["学分"])


def avgPlot():
    # 此函数不需要传入函数 我们使用读入的本地文件 test.csv
    # 我们先读入csv文件
    df = pd.read_csv("../GPA/data.csv",index_col=False)
    # 我们针对成绩当中的“优 良 中 及格 ....”等等我们需要先进行处理
    # 优：90 良：80 中：70 及格：60 不及格：0


    df["成绩"] = df["成绩"].map(score_map)

    # print(df["成绩"])

    # 这里我认为分组之前可以先给数据新添加一列 成绩乘以学分 计算我们


    df["scoreSub"] = df.apply(scoreSub, axis=1)
    # print(df["scoreSub"])
    # print(df)
    # 我们已经完成了上述的操作 以及处理好了成绩中的文字 并且我们使用apply函数增加了一列学分乘以成绩的值

    # 接下来我们需要进行分组

    avgScore = df.groupby("首修学期", as_index=False).apply(countScore)
    # 我们现在相当于已经得到了这个五个学期的绩点成绩
    # 接下我们需要针对这五个成绩的绩点进行作图

    # 我们需要进行作图

    # 把变量放好
    # Semster = tuple(df["首修学期"].unique())
    # print(len(Semster))
    Score = avgScore.values.tolist()
    Semster, Grade = map(list, zip(*Score))
    Semster = tuple(Semster)
    # Grade = np.array(Grade)
    demoGrade = []
    for i in Grade:
        i = round(i,2)
        demoGrade.append(i)
    print(Semster)
    print(Grade)

    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)

    # Example data
    y_pos = np.arange(len(Semster))

    hbars = ax.barh(y_pos, demoGrade , align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(Semster)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Score')
    ax.set_title('Average Score For Individual Semster')

    # # Label with specially formatted floats
    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right=100)  # adjust xlim to fit labels
    fig.tight_layout()
    return fig