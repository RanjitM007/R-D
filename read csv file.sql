LOAD DATA INFILE 'file.csv'
INTO TABLE your_table
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
