
spark.conf.set("fs.azure.account.auth.type.formula1dl.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dl.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dl.dfs.core.windows.net", "")
display(dbutils.fs.ls("abfss://demo@formula1dl.dfs.core.windows.net"))

display(spark.read.csv("abfss://demo@formula1dl.dfs.core.windows.net/circuits.csv")

