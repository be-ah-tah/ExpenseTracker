#### Directory Contents
- `README.md` Instructions
- `requirements.txt` Python dependencies

#### Application Files\
- `expense_tracker.py`
- `manual_inputs.py`
- `statements_upload.py`
- `apply_filters.py`
- `transform_data.py`

#### Additional Files
- `categories.csv`

## Requirements
- Python 3.9

## Launch Instructions
1. Navigate your current working directory to directory of this readme
2. Install python requirements
`pip install -r requirements.txt`
3. Launch application using `python -m streamlit run expense_tracker.py`. The application by default will listen by default on port `8501`, this can be changed if required by running with the additional argument `--server.port=X`. 
4. View application by navigating a web browser to http://localhost:8501/

### Virtual Environment Helper\
Running this application in a virtual environment is not required, but is advisable to reduce the risk of clashing dependencies in the existing python install. Example setup using `virtualenv`:
1. Navigate you current working directory to the directory of this file
2. Create a new virtual environment `python -m venv ./venv`
3. Activate environment:\\
  (On older python installs the scripts may be under `\\Scripts` rather than `\\bin`:\\
  Linux/Mac: `source venv/bin/activate`\\
  Windows (powershell): `.\\venv\\bin\\Activate.ps1`
4. Follow 'Launch Instructions' from the current terminal
