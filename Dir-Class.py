'''
Name:Dir_Class.py
Explain:
    未添加异常处理.
    未读取用户的文件列表
'''
import os 
import shutil

formats = {
    "音频": [".mp3",".wav"],
    "视频": [".mp4",".avi",".mov"],
    "图片": [".jpeg",".jpg",".png",".gif",".bmp"],
    "文档": [".txt",".pdf",".doc",".docx",".emmx",".xlsx",".yaml"],
    "程序": [".exe",".msi",".bat"],
    "压缩": [".zip",".rar"]
}

os.chdir(r"C:\Users\Mr_Gu\Downloads")

for file in os.listdir():
    ext = os.path.splitext(file)[-1].lower()

    for d, exts in formats.items():
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(file,'{0}/{1}'.format(d,file))

print (' 整理完成'.center(20,'_'))
