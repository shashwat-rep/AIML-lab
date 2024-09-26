# Experiment - 5 : Using Python language do the exploratory data analysis of dataset imported in the lab 4.

import pandas as pd
from google.colab import files
upload=files.upload()
import io
df = pd.read_csv(io.BytesIO(upload['sample.csv']))
