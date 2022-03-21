import Data.Utilities as Data
import pandas as pd

df = Data.dataFrame

wsm_df = Data.WSM(df)

class_df = df.copy()

class_df = pd.merge(class_df, wsm_df['classified'], left_index=True, right_index=True)

print(class_df.head().to_string())
