# Character_classification

 一个根据人脸分类人物图片的软件

# 效果

![248af981d96c024fb40485ac1c546f87](https://github.com/user-attachments/assets/2f225b5f-533d-48f3-9df4-8c505bc09d8d)


![988d13e97a22eab86ec359697ea981f4](https://github.com/user-attachments/assets/6921bc0d-ef4f-4489-9d31-1fc345851286)


# 安装

测试环境python3.12.4

```
git clone https://github.com/fallingmeteorite/Character_classification.git

cd Character_classification

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

mkdir Categorize_pictures

mkdir Recognize_faces
```
# 准备
Categorize_pictures文件夹存放要分类图片

Recognize_faces文件夹放入筛选对比人脸

注意分类效果跟对比人脸有较大联系，请保证对比人脸图片的质量

# 运行

```
python run.py -process_number xxx -confidence xxx -body_cut 1
```

# 可添加参数
process_number 启用线程数 默认为 1 根据电脑性能添加

confidence 置信度 默认为 0.5 越小越准确

body_cut 是否开启人物裁剪 不填写为False填写为True

