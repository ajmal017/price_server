# coding: utf-8
"""
run.py: Created on 10/31/2019 by ashwin}.
This exists to be able to run NorgateServer in a debugger
"""

from app import app

# So we can run things under a debugger
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
