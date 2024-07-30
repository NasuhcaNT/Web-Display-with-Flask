# data_sender.py

import pandas as pd
import threading
from flask import Flask, render_template_string

data_frame_lock = threading.Lock()
data_frame = pd.DataFrame()

app = Flask(__name__)

@app.route("/data")
def get_data():
    global data_frame
    with data_frame_lock:
        data = data_frame.to_dict(orient="records")
    return {"data": data}

@app.route("/")
def index():
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DataFrame Table</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5">DataFrame Table</h1>
            <div id="table-container"></div>
        </div>
        <script>
            function fetchData() {
                $.ajax({
                    url: "/data",
                    type: "GET",
                    success: function(data) {
                        var tableHtml = '<table class="table table-striped"><thead><tr>';
                        var columns = Object.keys(data.data[0]);
                        columns.forEach(function(column) {
                            tableHtml += '<th>' + column + '</th>';
                        });
                        tableHtml += '</tr></thead><tbody>';
                        data.data.forEach(function(row) {
                            tableHtml += '<tr>';
                            columns.forEach(function(column) {
                                tableHtml += '<td>' + row[column] + '</td>';
                            });
                            tableHtml += '</tr>';
                        });
                        tableHtml += '</tbody></table>';
                        $('#table-container').html(tableHtml);
                    }
                });
            }
            $(document).ready(function() {
                fetchData();
                setInterval(fetchData, 1000); // 1 saniyede bir veriyi yenile
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template)

def send_data_to_web(new_data, df_columns):
    global data_frame
    with data_frame_lock:
        data_frame = pd.concat([pd.DataFrame([new_data]), data_frame], ignore_index=True)
        print(f"Generated random data: {new_data}")

def start_flask_app():
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=5000)


