from pycomm3 import LogixDriver
import pyodbc

try:
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=TCLT087\SQLSERVER2023;Database=TrusscoreControls;UID=sa;PWD=qwerty;")
    print("Connected to SQL")
except:
    print("Not connected to SQL")

# List of IP addresses to check
ip_addresses = ["192.168.202.{}".format(i) for i in range(1, 2)]

# Loop through each IP address and check the connection
for ip_address in ip_addresses:
    plc = LogixDriver(ip_address)
    if plc.open():
        print("{} - Connected".format(ip_address))
        # Do whatever you need to do with the connected PLC here

        # read specific tag values
        tag1_value = plc.read('Actual_Board_length_in_Meters')[1]
        tag2_value = plc.read('DataLog_Order_Description')[1]

        # log the tag values
        #logger.info(f"IP Address: {ip_address} || Tag1 Value: {tag1_value} || Tag2 Value: {tag2_value}")

        # print the tag values on console
        print(f"Tag1 Value: {tag1_value}")
        print(f"Tag2 Value: {tag2_value}")
        plc.close()
    else:
        print("{} - Not connected".format(ip_address))
