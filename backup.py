# copy from given path last modified by one day
# run every day in a task scheduler

import os, re
import datetime as dt
    
# /s copy subdirs
# /e copy empty subdirs
# /xd exclude dirs
# /maxage: exclude files older than days
# /v verbose

source_path = "z:"

os.system(f"robocopy {source_path} d:\\sotr_backup_{dt.datetime.now().strftime('%d.%m.%Y_%H.%M.%S')} *.doc *.xls *.pdf *.rtf /s /v /maxage:1")

