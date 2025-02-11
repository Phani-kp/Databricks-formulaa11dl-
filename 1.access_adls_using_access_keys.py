# Set Azure Data Lake account key
spark.conf.set(
    "fs.azure.account.key.formula1dl.dfs.core.windows.net",
    "YOUR_ACCOUNT_KEY"
)

# List files in the 'demo' container
display(dbutils.fs.ls("abfss://demo@formula1dl.dfs.core.windows.net"))

# Read data from 'circuits.csv' in the 'demo' container
display(spark.read.csv("abfss://demo@formula1dl.dfs.core.windows.net/circuits.csv"))

