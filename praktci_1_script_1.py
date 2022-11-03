import pymysql.cursors
# Подключиться к базе данных.
connection = pymysql.connect(host='5.183.188.132',
                             user='db_vgu_student',
                             password='thasrCt3pKYWAYcK',
                             db='db_vgu_test2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    # SQL
    sql = "SELECT * FROM country"
    # Выполнить команду запроса (Execute Query).
    cursor.execute(sql)
    print (f'cursor.description:  {cursor.description} \n')
    for row in cursor:
        if row['name'] == 'Russian Federation':
            print(row)


connection.close()