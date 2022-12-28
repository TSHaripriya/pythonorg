import pyodbc

    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
server = 'HCL-02-53\SQLEXPRESS04'
database = 'FileSearchResults2'
username = 'capstone'
password = 'Capstone@123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
print(cnxn)
cursor = cnxn.cursor()
print(cursor)
cursor.execute('''
                    INSERT INTO FileSearchResults2_table (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('E:\A\Dummy\Dummy1\Sample1.txt',1,'sample.txt') ''')
cnxn.commit()

values = cursor.execute('select * from FileSearchResults2_table')
for i in values:
    print(i)
    