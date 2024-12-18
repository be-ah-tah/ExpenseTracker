{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ## Directory Contents\
- `README.md` Instructions\
- `requirements.txt` Python dependencies\
\
#### Application Files\
- `expense_tracker.py`\
- `manual_inputs.py`\
- `statements_upload.py`\
- `apply_filters.py`\
- `transform_data.py`\
\
####Additional Files\
- \'91categories.csv\'92\
\
## Requirements\
- Python 3.9\
\
## Launch Instructions\
1. Navigate your current working directory to directory of this readme\
2. Install python requirements\
`pip install -r requirements.txt`\
3. Launch application using `python -m streamlit run expense_tracker.py`. The application by default will listen by default on port `8501`, this can be changed if required by running with the additional argument `--server.port=X`. \
4. View application by navigating a web browser to http://localhost:8501/\
\
### Virtual Environment Helper\
Running this application in a virtual environment is not required, but is advisable to reduce the risk of clashing dependencies in the existing python install. Example setup using `virtualenv`:\
1. Navigate you current working directory to the directory of this file\
2. Create a new virtual environment `python -m venv ./venv`\
3. Activate environment:\\\
  (On older python installs the scripts may be under `\\Scripts` rather than `\\bin`:\\\
  Linux/Mac: `source venv/bin/activate`\\\
  Windows (powershell): `.\\venv\\bin\\Activate.ps1`\
4. Follow 'Launch Instructions' from the current terminal\
\
}