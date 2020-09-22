import sys,fitz
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def all_files_path(rootDir):                    #遍历获取文件函数
    for root,dirs,files in os.walk(rootDir):    #分别代表根目录、文件夹、文件
        for file in files:                      #遍历文件
            file_path = root+'/'+file           #获取文件绝对路径
            filepaths.append(file_path)         #将文件路径添加进列表
        for dir_ in dirs:                       #遍历目录下的子目录
            dir_path = root+'/'+ dir_           #递归调用
            all_files_path(dir_path)
            
def pyMuPDF_fitz(pdfPath,imagePath,imageName):  #pdf转png函数
##    print(pdf_path)
    pdfDoc=fitz.open(pdfPath)                   #读取pdf文件
    for pg in range(pdfDoc.pageCount):          #遍历文件所有页
        page = pdfDoc[pg]
        rotate=int(0)
        zoom_x=1.33333333                       #设置参数，越大，分辨率越高
        zoom_y=1.33333333                       
        mat = fitz.Matrix(zoom_x,zoom_y).preRotate(rotate)
        pix=page.getPixmap(matrix=mat,alpha=False) #将pdf当前页截图
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        if pg == 0:
            pix.writePNG(imagePath+'/'+ imageName+'.png') #保存截图为png文件
        else:
            pix.writePNG(imagePath+'/'+ imageName+'_%s.png'%pg)
    
if __name__=="__main__":
    filepaths=[]                              #文件绝对路径列表
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("提示","请选择文件所在的文件夹")
    InputFolderpath = filedialog.askdirectory()    #选择根目录
    all_files_path(InputFolderpath)                #调用文件遍历函数，获取文件绝对路径列表
    for pdf_path in filepaths:                #遍历文件列表，将列表里的pdf文件全部转为png
##        print(pdf_path)
        (image_path,pdf_name)=os.path.split(pdf_path) #将转换后的文件保存在pdf文件存放的文件夹中
        (image_name,extension)=os.path.splitext(pdf_name)#转换后文件名采用原pdf文件名
        if extension=='.pdf':
            pyMuPDF_fitz(pdf_path,image_path,image_name)
    messagebox.showinfo("提示","文件转换已完成")
        
    
    
