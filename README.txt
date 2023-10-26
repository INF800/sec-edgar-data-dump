This project creates a database of all files avalable in EDGAR from 1994 to 11th october 2023.

1. Install dependencies.
2. Run download_idx_files.py to download idx files. Alternatively, extract idx_files.zip in ./idx_files directory. 
3. Run write_idx_files_to_db.py create merged csv file and sqlite database in output_folder.

Note: To access big files like ./output/AllDataUntil20231011.csv and ./idx_files.zip you may need GIT LFS.

Remove the `.txt` extension and the hyphens in the original path to get folder path. For example, change "edgar/data/1022570/0001013762-10-001847.txt" to "edgar/data/1022570/000101376210001847".
