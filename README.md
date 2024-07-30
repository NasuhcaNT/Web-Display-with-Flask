# Web-Display-with-Flask
This repository contains a simple implementation of a random data generator for example and a Flask web application to display the generated data in real-time. The project is divided into two main parts: data_sender.py and random name generator.py

How to Run:

Clone this repository to your local machine.

Ensure you have the necessary Python packages installed:

pip install pandas flask

Run the random name generator.py file to start the Flask application and begin generating and displaying random data:
python random name generator.py

Open a web browser and navigate to http://localhost:5000 to see the real-time updated table.

Explanation of send_data_to_web(new_data, df_columns)
The send_data_to_web function is designed to update the global data frame with new data. Here's a breakdown of its parameters and functionality:

Parameters:

new_data (dict): A dictionary containing the new data to be added.

df_columns (list): A list of column names for the data frame.


Functionality:

The function acquires a lock using data_frame_lock to ensure thread-safe access to the global data_frame.
It concatenates the new data, converted into a DataFrame, to the existing global data_frame.
Finally, it prints the newly added data to the console for verification.
This ensures that any new data generated is safely and consistently added to the global data frame, which is then served via the Flask web application.

Contributing
Feel free to open an issue or submit a pull request if you have suggestions or improvements. Contributions are welcome!









