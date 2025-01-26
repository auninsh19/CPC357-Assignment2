# CPC357 Assignment 2 - Smart Agriculture IoT Application

This project implements a Smart Agriculture IoT application that collects data from an MQTT broker and stores it in a MongoDB database. The application is designed to monitor paddy fields and facilitate data-driven decision-making in agriculture. This project does not require hardware connectivity as the data comes from an already available dataset.

## Features

- Connects to an MQTT broker to receive real-time data.
- Ingests data into a MongoDB database.
- Handles incoming messages and processes them for storage.

## Prerequisites

Before setting up the development environment on a GCP VM instance, ensure you have the following:

- A Google Cloud account
- A GCP Virtual Machine instance running a supported OS (Ubuntu)
- MongoDB installed on the VM
- An MQTT Broker (Mosquitto) installed on the VM or access to a public MQTT broker
- Python 3.x installed on the VM
- pip (Python package installer)

## Setup Instructions

1. **Create a GCP Virtual Machine Instance**

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to the "Compute Engine" section and create a new VM instance. Make sure Compute Engine API is enabled.
   - Choose an appropriate machine type and operating system (Ubuntu 20.04 LTS).
   - Ensure that you allow HTTP and HTTPS traffic in the firewall settings.

2. **Connect to Your VM Instance**

   Click SSH button next to the VM instanceto open up SSH-in-browser.

3. **Update the Package List and Install Dependencies**

   Update the package list and install necessary packages:
   ```bash
   sudo apt-get update
   ```
   ```bash
   sudo apt-get upgrade
   ```
   ```bash
   sudo apt-get install python3 python3-pip mongodb mosquitto
   ```

4. **Clone the Repository**

   Clone this repository to your VM instance using the following command:
   ```bash
   git clone https://github.com/yourusername/smart-agriculture.git
   ```
   ```bash
   cd smart-agriculture
   ```

5. **Install Required Python Packages**

   Install the required Python packages using pip:
   ```bash
   pip install pymongo paho-mqtt

6. **Set Up MongoDB**

   Ensure that MongoDB is running on your VM. You can start it with:
   ```bash
   sudo service mongodb start
   ```
   Create a database named smart_agriculture and a collection named paddy if they do not already exist. You can do this by accessing the MongoDB shell:
   ```bash
   mongo
   ```
   Then, in the MongoDB shell, run:
   ```javascript
   use smart_agriculture
   db.createCollection("paddy")
   exit
   ```
   Create a database named smart_agriculture and a collection named paddy if they do not already exist.

7. **Set Up MQTT Broker**

   If you are using Mosquitto, ensure it is running. You can start it with:

   ```bash
   sudo service mosquitto start
   ```
   Update the mqtt_broker_address in the source code to point to your MQTT broker.

8. **Run the Application**

   Execute the Python script to start the application:
   ```bash
   python3 your_script_name.py
   ```
   Replace your_script_name.py with the actual name of your Python file.

9. **Data Ingestion**

   The application will listen for messages on the specified MQTT topic (smart_agriculture) and ingest the data into the MongoDB collection.

## Dataset

The dataset used for this project is located in the data1.csv file in this repository. This dataset can be used for testing and simulating data ingestion.
