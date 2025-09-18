import pandas as pd

FILE_ID = "1odXw81javPy4RwmYhj4IZts80g-3rMOv"

file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)

print(raw_data.head(10))