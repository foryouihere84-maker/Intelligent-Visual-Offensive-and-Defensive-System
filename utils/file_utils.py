import os
from werkzeug.utils import secure_filename
import glob


def allowed_file(filename, allowed_extensions):
    """
    检查文件是否具有允许的扩展名
    :param filename: 上传的文件名
    :param allowed_extensions: 允许的扩展名集合（如 {'png', 'jpg', 'jpeg'}）
    :return: 布尔值
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions


# 可选：封装 secure_filename 以统一处理
def safe_filename(filename):
    """
    生成安全的文件名
    """
    return secure_filename(filename)


def scan_model_files(model_dir, extension='.pt'):
    """
    扫描指定目录下的模型文件
    :param model_dir: 模型目录路径
    :param extension: 模型文件扩展名
    :return: 模型文件名列表（不含扩展名）
    """
    if not os.path.exists(model_dir):
        print(f"Model directory not found: {model_dir}")
        return []

    pattern = os.path.join(model_dir, f'*{extension}')
    files = glob.glob(pattern)
    # 提取文件名（不含扩展名）作为模型名称
    model_names = [os.path.splitext(os.path.basename(f))[0] for f in files]
    print(f"Found models in {model_dir}: {model_names}")
    return sorted(model_names)


def get_detection_models():
    """
    获取检测模型列表
    :return: 模型名称列表
    """
    from flask import current_app
    detection_model_dir = os.path.join(current_app.config['BASE_DIR'], 'models', 'detection')
    return scan_model_files(detection_model_dir, '.pt')




def get_classification_models():
    """
    获取分类模型列表
    :return: 分类模型名称列表
    """
    # 返回常见的预训练分类模型
    return [
        'resnet18',
        'resnet34', 
        'resnet50',
        'resnet101',
        'resnet152',
        'vgg16',
        'vgg19',
        'mobilenet_v2',
        'efficientnet_b0'
    ]


def get_adversarial_models():
    """
    获取对抗攻击模型列表
    :return: 模型名称列表
    """
    from flask import current_app
    adversarial_model_dir = os.path.join(current_app.config['BASE_DIR'], 'models', 'adversarial')
    return scan_model_files(adversarial_model_dir, '.pth')
