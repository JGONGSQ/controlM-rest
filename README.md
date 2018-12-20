# controlM_api

contrlM REST API repo

## Run examples
### ctm cli
```Bash
# Get the all the jobs in the server via ctm cli
ctm deploy jobs::get xml -s "ctm=*&folder=NDIA*"

# Run the order <ctm> <folder>
ctm run order workbench NDIA_IDS2_#env#_011_ST_SRCI_11

# Check the status of the run with <runId>
ctm run status 2003409f-b2d7-4266-b013-04668db18a59

# Check all the job status with query string
ctm run jobs:status::get -s "jobname=LX*"

# Get a login session via ctm cli
ctm login session
```

### Python run
```bash
# Load the test data and deploy jobs to the local contrlM workbench
python ctrlM.py data/test_folder.xml

# run order the deployed jobs
python ctrlM.py
```

