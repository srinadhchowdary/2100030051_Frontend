import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='sqlconnection'
)


if conn.is_connected():
    print("Connected to MySQL database successfully.")
    cursor = conn.cursor()

  
    query = """
    SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
    FROM locations l
    JOIN countries c ON l.country_id = c.country_id
    WHERE c.country_name = 'Canada'
    """


    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

   
    cursor.close()
    conn.close()
    print("Close Connection.")
else:
    print("Failed to connect to MySQL database")