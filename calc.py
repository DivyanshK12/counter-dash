from flask import Flask, request, Response
import csv
from datetime import datetime, timedelta, date

app = Flask(__name__)

@app.route("/receiver", methods=["GET", "POST"])
def receiver():
    data = request.get_json(force = True)
    with open("data.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        td = getdate()
        print(td.__dir__())
        savedate = date(day=td.day, month=td.month, year=td.year)
        writer.writerow([data['user'], int(data['count']), savedate])
    response = Response(status=200)
    return response

def getdate():
    time = timedelta(hours=5, minutes=30)
    date = datetime.utcnow()+time
    return date

if __name__ == "__main__":
    with open("data.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["User", "Count", "Date"])
    app.run()