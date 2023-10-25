# fetch all index files
# ---------------------
import datetime

start_year = 1994
current_year = datetime.date.today().year
current_quarter = (datetime.date.today().month - 1) // 3 + 1
years = list(range(start_year, current_year))
quarters = ['QTR1', 'QTR2', 'QTR3', 'QTR4']
history = [(y, q) for y in years for q in quarters]
for i in range(1, current_quarter + 1):
    history.append((current_year, 'QTR%d' % i))
urls = ['https://www.sec.gov/Archives/edgar/full-index/%d/%s/master.idx' % (x[0], x[1]) for x in history]
urls.sort()

# download idx files
# ------------------
import os
os.system('rm -rf ./idx_files/*.idx')
for url in urls:
  print(f'downloading {url} ...')
  year, qtr = url.split('full-index/')[1].split('/master.idx')[0].split("/")
  command = f'curl -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36" {url} -o ./idx_files/master-{year}-{qtr}.idx'
  os.system(command)