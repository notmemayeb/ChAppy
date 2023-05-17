import platform

def get_operating_system():
    system = platform.system()
    if system == "Windows":
        print("Your are using", "Windows")
        return "Windows"
    elif system == "Darwin":
        print("Your are using", "Mac")
        return "Mac"
    else:
        return "Unknown"