import sys
import streamlit.web.cli as stcli

def streamlit_run():
    sys.argv = ["streamlit", "run", "streamlit_main.py", "--global.developmentMode=false"]
    sys.exit(stcli.main())


if __name__ == "__main__":
    streamlit_run()