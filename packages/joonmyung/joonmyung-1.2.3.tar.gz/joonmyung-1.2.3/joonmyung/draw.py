from matplotlib import pyplot as plt, axes
import torch.utils.data.distributed
import torch.nn.parallel
import torch.utils.data
from PIL import Image
import seaborn as sns
import pandas as pd
import numpy as np
import torch.optim
import pickle
import pprint
import torch
import cv2
import PIL



def drawHeatmap(matrixes, col=1, title=[], fmt=1, p=False,
                vmin=None, vmax=None, xticklabels=False, yticklabels=False,
                linecolor=None, linewidths=0.1, fontsize=30,
                cmap="Greys", cbar=True):
    row = (len(matrixes) - 1) // col + 1
    annot = True if fmt > 0 else False


    if p:
        print("|- Parameter Information")
        print("  |- Data Info (G, H, W)")
        print("    |- G : Graph Num")
        print("    |- H : height data dimension")
        print("    |- W : weidth data dimension")
        print("  |- AXIS Information")
        print("    |- col        : 컬럼 갯수")
        print("    |- row : {}, col : {}".format(row, col))
        print("    |- height : {}, width : {}".format(row * 8, col * 8))
        print("    |- title      : 컬럼별 제목")
        print("    |- p          : 정보 출력")
        print()
        print("  |- Graph Information")
        print("    |- vmin/vmax  : 히트맵 최소/최대 값")
        print("    |- linecolor  : black, ...   ")
        print("    |- linewidths : 1.0...   ")
        print("    |- fmt        : 숫자 출력 소숫점 자릿 수")
        print("    |- cmap        : Grey")
        print("    |- cbar        : 오른쪽 바 On/Off")
        print("    |- xticklabels : x축 간격 (False, 1,2,...)")
        print("    |- yticklabels : y축 간격 (False, 1,2,...)")
    if title:
        title = title + list(range(len(title), len(matrixes) - len(title)))
    fig, axes = plt.subplots(nrows=row, ncols=col, squeeze=False)
    fig.set_size_inches(col * 8, row * 8)

    for e, matrix in enumerate(matrixes):
        if type(matrix) == torch.Tensor:
            matrix = matrix.detach().cpu().numpy()
        ax = axes[e // col][e % col]
        sns.heatmap(pd.DataFrame(matrix), annot=annot, fmt=".{}f".format(fmt), cmap=cmap
                    , vmin=vmin, vmax=vmax, yticklabels=yticklabels, xticklabels=xticklabels
                    , linewidths=linewidths, linecolor=linecolor, cbar=cbar, annot_kws={"size": fontsize / np.sqrt(len(matrix))}
                    , ax=ax)
        if title:
            ax.set(title="{} : {}".format(title, e))
        ax.spines[["bottom", "top", "left", "right"]].set_visible(True)
    plt.show()


def makeSample(shape, min=None, max=None, dataType=int, outputType=np, columns=None):
    if dataType == int:
        d = np.random.randint(min, max, size=shape)
    elif dataType == float:
        d = np.random.uniform(low=min, high=max, size=shape)

    if outputType == np:
        return d
    elif outputType == pd:
        return pd.DataFrame(d, columns=None)
    elif outputType == torch:
        return torch.from_numpy(d)


def drawLinePlot(datas, index, col=1, title=[], xlabels=None, ylabels=None, markers=False, columns=None, p=False):
    row = (len(datas) - 1) // col + 1
    title = title + list(range(len(title), len(datas) - len(title)))
    fig, axes = plt.subplots(nrows=row, ncols=col, squeeze=False)
    fig.set_size_inches(col * 8, row * 8)

    if p:
        print("|- Parameter Information")
        print("  |- Data Info (G, D, C)")
        print("    |- G : Graph Num")
        print("    |- D : x data Num (Datas)")
        print("    |- C : y data Num (Column)")
        print("  |- Axis Info")
        print("    |- col   : 컬럼 갯수")
        print("    |- row : {}, col : {}".format(row, col))
        print("    |- height : {}, width : {}".format(row * 8, col * 8))
        print("    |- title : 컬럼별 제목")
        print("    |- p     : 정보 출력")
        print("  |- Graph Info")
        print("    |- vmin/row  : 히트맵 최소/최대 값")
        print("    |- linecolor  : black, ...   ")
        print("    |- linewidths : 1.0...   ")
        print("    |- fmt        : 숫자 출력 소숫점 자릿 수")
        print("    |- cmap        : Grey")
        print("    |- cbar        : 오른쪽 바 On/Off")
        print("    |- xticklabels : x축 간격 (False, 1,2,...)")
        print("    |- yticklabels : y축 간격 (False, 1,2,...)")
        print()

    for e, data in enumerate(datas):
        ax = axes[e // col][e % col]
        d = pd.DataFrame(data, index=index, columns=columns).reset_index()
        d = d.melt(id_vars=["index"], value_vars=columns)
        p = sns.lineplot(x="index", y="value", data=d, hue="variable", markers=markers, ax=ax)
        p.set_xlabel(xlabels, fontsize=20)
        p.set_ylabel(ylabels, fontsize=20)

        ax.set(title=title[e])
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()

def drawBarChart(df, x, y, splitColName, col=1, title=[], fmt=1, p=False, c=False, c_sites={}, showfliers=True):
    d2s = df[splitColName].unique()
    d1 = df['d1'].unique()[0]
    d2s = [d2 for d2 in d2s for c_site in c_sites[d1].keys() if c_site in d2]

    row = (len(d2s) - 1) // col + 1

    fig, axes = plt.subplots(nrows=row, ncols=col, squeeze=False)
    fig.set_size_inches(col * 12, row * 12)
    for e, d2 in enumerate(tqdm(d2s)):
        plt.title(d2, fontsize=20)
        ax = axes[e // col][e % col]
        temp = df.loc[df['d2'].isin([d2])]
        if temp["Date_m"].max() != temp["Date_m"].min():
            ind = pd.date_range(temp["Date_m"].min(), temp["Date_m"].max(), freq="M").strftime("%Y-%m")
        else:
            pd.to_datetime(temp["Date_m"].max()).strftime("%Y-%m")
        g = sns.boxplot(x=x, y=y, data=temp, order=ind, ax=ax, showfliers=showfliers)
        g.set(title=d2)
        g.set_xticklabels(ind, rotation=45, fontsize=15)
        g.set(xlabel=None)
        for c_site, c_dates in c_sites[d1].items():
            if c_site in d2:
                for c_date in c_dates:
                    c_ind = (pd.to_datetime(c_date, format='%Y%m%d') - pd.to_datetime(temp["Date_m"].min())).days / 30
                    if c_ind >= 0:
                        g.axvline(c_ind, ls='--', c="red")
    plt.show()






def showImg(image):
    if type(image) == torch.tensor:
        plt.imshow(image.permute(1, 2, 0))
        plt.show()
    elif type(image) == PIL.Image.Image:
        plt.imshow(image)
        plt.show()
    elif type(image) == np.array:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # 0.29
        # plt.imshow(Image.fromarray(image))  # 0.32

# import torch
# import torch.nn as nn
# from torchviz import make_dot
# from torch.autograd import Variable
#
# model = nn.Sequential()
# model.add_module('W0', nn.Linear(8, 16))
# model.add_module('tanh', nn.Tanh())
#
# # Variable을 통하여 Input 생성
# x = Variable(torch.randn(1, 8))
#
# # 앞에서 생성한 model에 Input을 x로 입력한 뒤 (model(x))  graph.png 로 이미지를 출력합니다.
# make_dot(model(x), params=dict(model.named_parameters())).render("graph", format="png")
