from pathlib import Path
from io import StringIO
import pandas as pd
import sqlite3

def convert_idx_file_to_df(input_idx_file: Path):
    _, year, qtr = input_idx_file.stem.split("-")
    new_data = ""
    with open(str(input_idx_file), 'r') as fi:
        data = fi.read()
        starting_idx = data.find("\nCIK")+1
        new_data = data[starting_idx:starting_idx+47]+data[starting_idx+47+81:]

    df = pd.read_csv(StringIO(new_data), sep="|")
    df['Quarter'] = qtr
    df['Year'] = year
    return df

def merge_idx_files(idx_folder: Path):
    idx_files = sorted([*idx_folder.glob('*.idx')])        
    big_df = pd.DataFrame({
        'CIK': [],
        'Company Name': [], 
        'Form Type': [],
        'Date Filed': [],
        'Filename': [],
        'Quarter': [],
        'Year': [],
    })

    for i, idx_file in enumerate(idx_files):
        df = convert_idx_file_to_df(idx_file)
        print(f'file {i}/{len(idx_files)}: adding {len(df)} records from {idx_file.name}')
        assert list(df.columns) == ['CIK', 'Company Name', 'Form Type', 'Date Filed', 'Filename', 'Quarter', 'Year']
        big_df = pd.concat([big_df, df], ignore_index=True)

    return big_df

def main():
    INPUT_FOLDER = './idx_files'
    OUTPUT_CSV = './output/AllDataUntil20231011.csv.gz'
    OUTPUT_DB = './output/AllDataUntil20231011.sqlite'

    df_merged = merge_idx_files(Path(INPUT_FOLDER))
 
    print(f"Writing: {OUTPUT_CSV}")
    df_merged.to_csv(OUTPUT_CSV, index=False, compression='gzip')

    print(f"Writing: {OUTPUT_DB}")
    conn = sqlite3.connect(OUTPUT_DB)
    df_merged.to_sql(name='AllDataUntil20231011', con=conn)
    conn.close()


if __name__=='__main__':
    main()