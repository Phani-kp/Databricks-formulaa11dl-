spark.conf.set(
    "fs.azure.account.key.formula1dl.dfs.core.windows.net",
    "")
display(dbutils.fs.ls("abfss://demo@formula1dl.dfs.core.windows.net"))
display(spark.read.csv("abfss://demo@formula1dl.dfs.core.windows.net/circuits.csv"))

