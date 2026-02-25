import os


class Config:
    # 基础路径
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    RESULT_FOLDER = os.path.join(BASE_DIR, 'static', 'results')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # 模型配置将在应用初始化时动态设置
    MODELS = {
        'detection': {},
        'adversarial': {}
    }

    # 默认模型
    DEFAULT_MODEL = 'yolov8n'
