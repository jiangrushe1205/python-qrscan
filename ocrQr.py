import cv2  
import os

"""
    作者：姜汝社
    这个程序使用了微信开源的二维码扫码模型，
    git地址： https://github.com/WeChatCV/opencv_3rdparty/tree/wechat_qrcode
    在使用之前：
    使用前需要安装opencv-contrib-python包，注意安装的包不能低于4.5.2版本。
    pip3 install opencv-contrib-python
"""


def proccess(dirPath):
    files = os.listdir(dirPath)

    # 遍历文件夹
    for file in files:

        if ".DS_Store" == file:
            continue

        if not os.path.isdir(file):
            filePath = dirPath+"/"+file
            # 判断是否是文件夹，不是文件夹才打开
            try:
                # 扫描二维码
                scanQr(filePath)
            except UnboundLocalError:
                print("没有匹配到二维码")


def scanQr(path):
    print('文件路径 >>> ' + path)
    # 加载微信二维码扫描殷勤
    detect_obj = cv2.wechat_qrcode_WeChatQRCode('./wechatqr/detect.prototxt','./wechatqr/detect.caffemodel','./wechatqr/sr.prototxt','./wechatqr/sr.caffemodel')
    img = cv2.imread(path)
    res, points = detect_obj.detectAndDecode(img)
    print('res:', res)
    print('points:', points)
    return res


if __name__ == '__main__':
    proccess("/Users/jiangrushe/Downloads/invoice-3")