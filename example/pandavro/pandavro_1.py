import numpy as np
import pandas as pd
import pandavro

df = pd.DataFrame(
    {
        "String": ["one", "two", "three", "four"],
        "DateTime64": [
            pd.Timestamp("20210709"),
            pd.Timestamp("20210710"),
            pd.Timestamp("20210711"),
            pd.Timestamp("20210712"),
        ],
        "Boolean": [True, False, True, False],
        "Float32": np.random.randn(4),
        "Float64": np.random.randn(4),
        "Int64": np.random.randint(0, 10, 4),
    }
)

pandavro.to_avro("./data/csv/example.avro", df)
