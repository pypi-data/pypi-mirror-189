## About
The docset must comply with the following format.
```python
## Classification
doc = {
    'filename'      : str,        # 图像文件名  
    'size'          : list,       # 图像大小 [height, wight, channel
    'image'         : bytes,      # 图像数据  
    'label'         : int,        # 标签id
    'label_name'    : str         # 标签名称
}

## Detection
doc = {
    'filename'      : str,        # 图像文件名    
    'size'          : list,       # 图像大小 [height, wight, channel]
    'image'         : bytes,      # 图像数据        
    'bbox': [{
        'box'       : list,       # box [xmin, ymin, xmax, ymax]
        'label'     : int,        # box的标签id
        'label_name': str         # box的标签名称
    }]               
}

## Segmentation
doc = { 
    'filename'      : str,        # 图像文件名 
    'size'          : list,       # 图像大小 [height, wight, channel]
    'image'         : bytes,      # 图像数据  
    'mask'          : np.ndarray, # int64
    'heatmap'       : np.ndarray  # float32
}
```


## Installation
#### Get from PyPI
```shell
pip install docsetviz
docsetviz
```

#### Build from source
##### Ubuntu
```shell
git clone https://gitlab.edgeai.org:8888/yannan1/datavisualization.git
cd docsetviz
pip install -r requirements.txt
python main.py
```
#### Windows
```shell
# Git clone source
git clone https://gitlab.edgeai.org:8888/yannan1/datavisualization.git

# Open cmd and go to the docsetviz directory
pip install -r requirements.txt
python main.py
```

## Usage
![usage.png](pictures%2Fusage.png)
##### 打开远程文件
click "打开远程文件", Enter the following information
![remote.png](pictures%2Fremote.png)

### Hotkeys
| function |    Hotkey    |
|:--------:|:------------:|
|   打开文件   |    Ctrl+O    |
|  打开远程文件  |    Ctrl+U    |
|  上一个图像   |      a       |
|  下一个图像   |      d       |
|   放大图像   |    Ctrl++    |
|   缩小画面   |    Ctrl+-    |
|   适配屏幕   |    Ctrl+F    |
|   适配图像   | Ctrl+Shift+F |

## Error
##### 1. opencv and pyqt5 conflict
```
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/yannan/anaconda3/lib/python3.9/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl.
```
##### resolution
```shell
## 方法1: 对opencv-python的版本没有特殊要求可采用此方法
pip uninstall opencv-python
pip install opencv-python-headless

## 方法2: conda安装pyqt
pip uninstall pyqt5
conda install pyqt
```