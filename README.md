# CPC357 Assignment 2 - Smart Agriculture IoT Application

This project implements a Smart Agriculture IoT application that collects data from an MQTT broker and stores it in a MongoDB database. The application is designed to monitor paddy fields and facilitate data-driven decision-making in agriculture.

## Features

- Connects to an MQTT broker to receive real-time data.
- Ingests data into a MongoDB database with a UTC timestamp.
- Handles incoming messages and processes them for storage.

## Prerequisites

Before setting up the development environment on a GCP VM instance, ensure you have the following:

- A Google Cloud account
- A GCP Virtual Machine instance running a supported OS (e.g., Ubuntu)
- MongoDB installed on the VM or access to a MongoDB Atlas instance
- An MQTT Broker (e.g., Mosquitto) installed on the VM or access to a public MQTT broker
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
   ```bash
   sudo apt-get upgrade
   ```bash
   sudo apt install python3 python3-pip mongodb mosquitto
