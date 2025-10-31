import platform, shutil

def check_dependencies():
    system = platform.system().lower()

    if system == "windows":
        return "unsupported operating system"

    # path = shutil.which("cdparanoia")
    # if path == None:
    #     return "system must have 'cdparanoia' on PATH"
    
    # path = shutil.which("flac")
    # if path == None:
    #     return "system must have 'flac' on PATH"

    return None