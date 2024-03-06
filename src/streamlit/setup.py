from cx_Freeze import setup,Executable


setup(
    name="GestoLingo",
    version="1.0",
    description="GestoLingo",
    executables = [Executable("run.py",base=None)],
    options={
        "build_exe":{
            "include_files":["streamlit_main.py","./images/","./models/","style.css"],
            "packages":["streamlit","cv2","mediapipe","tensorflow","boto3","numpy","base64","io","os"]
        }
    }
)