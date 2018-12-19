# controlM_api

contrlM_api api testing repo

## ctm cli
```Bash
# Get the all the jobs in the server via ctm cli
ctm deploy jobs::get xml -s "ctm=*&folder=NDIA*"

# Run the order
ctm run order workbench NDIA_IDS2_#env#_011_ST_SRCI_11

# Get a login session via ctm cli
ctm login session
```

## Python run
```bash
# Load the test data to the local contrlM workbench
python controlM.py test_data.xml
```

