import psutil

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    return {
        'cpu': cpu_usage,
        'memory': memory_info.percent,
        'disk': disk_usage.percent
    }
