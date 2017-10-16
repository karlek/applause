# Create the database

I used `sqlite3` to create my database. Probably not the best idea since a lot
of tweaking was needed to get it working.

Download all database files from: https://data.riksdagen.se/data/anforanden/
Is around 300MiB~

```shell
$ mkdir data
$ cd data
$ wget https://data.riksdagen.se/dataset/anforande/anforande-201617.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-201516.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-201415.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-201314.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-201213.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-201112.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200910.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200809.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200708.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200607.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200506.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200405.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200304.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200203.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200102.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-200001.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-19992000.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-199899.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-199798.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-199697.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-199596.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-199495.sql.zip
$ wget https://data.riksdagen.se/dataset/anforande/anforande-199394.sql.zip
$ unzip *
```

```shell
$ sqlite3 norm.db '.read create_table.sql'  # Create our tables.
$ sqlite3 norm.db '.read insert.sql'		# Insert all the data.
$ sqlite3 norm.db '.read normalize.sql'		# Fix inconsistencies.
$ sqlite3 norm.db '.read create_views.sql'  # Add convenient views.
# Recompile ./icu.so, never use someone elses binaries.
```

**NOTE:**
Remeber to `.load ./icu` before using functions like `lower` or `upper`, otherwise å, ä and ö will be unaffected.

