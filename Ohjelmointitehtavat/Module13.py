from flask import Flask, request
import mysql.connector

app = Flask(__name__)


# 1
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


@app.route('/alkuluku/<int:number>')
def is_prime_number(number):
    is_prime_result = is_prime(number)
    response = {"Number": number, "isPrime": is_prime_result}
    return response


# 2

connection = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="1234",
    database="flight_game"
)


def get_airport_info(icao):
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, municipality FROM airport WHERE ident='{icao}'")
    airport = cursor.fetchone()
    cursor.close()

    if airport:
        response = {"ICAO": icao, "Name": airport[0], "Municipality": airport[1]}
        return response


@app.route('/kenttä/<icao>')
def airport_info(icao):
    response = get_airport_info(icao)
    return response


# run

if __name__ == '__main__':
    app.config['JSON_SORT_KEYS'] = False
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
