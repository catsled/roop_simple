import onnxruntime

use_gpu = False
# providers = onnxruntime.get_available_providers()
providers = ['CPUExecutionProvider']

if 'TensorrtExecutionProvider' in providers:
    providers.remove('TensorrtExecutionProvider')
