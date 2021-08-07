import win32api
import win32con
import win32gui
import os
import time
import random

print('开始！！！！')

def Windows_img(paperPath):
    k=win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control panel\\Desktop",0,win32con.KEY_SET_VALUE)
    # 在注册表中写入属性值
    win32api.RegSetValueEx(k,"wapaperStyle",0,win32con.REG_SZ,"2")  # 0 代表桌面居中 2 代表拉伸桌面
    win32api.RegSetValueEx(k,"Tilewallpaper",0,win32con.REG_SZ,"0")

    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,paperPath,win32con.SPIF_SENDWININICHANGE) # 刷新桌面


def getImage():
    path = 'C:\\change\\image\\'
    loction=os.listdir(path=path)  # 得到文件路径下的图片，列表类型
    return loction

def changeWallpaper():
    # path=input('请输入文件路径:')
    path = 'C:\\change\\image\\'
    rand = random.randint(0,1000)
    L1 = getImage()
    i = rand%len(L1)

    print('开始',i)
    while True:
        L2 = getImage()
        if i >= len(L2):  # 如果是最后一张图片，则重新到第一张
            i=0
        print (i,len(L2))
        Windows_img(path+'\{}'.format(L2[i]))
        time.sleep(10)  # 设置壁纸更换间隔，这里为600秒，根据用户自身需要自己设置秒数
        i += 1

if __name__ == '__main__':
    changeWallpaper()

