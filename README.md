Pinterest-Cloud-Data-Pipeline
Project Title
Pinterest-Like Data Processing on AWS

Table of Contents
Description
Progress in Milestone 3
Installation
Usage
File Structure
License
Description
Overview
This project aims to replicate Pinterest's data processing system on the AWS Cloud. It involves setting up an EC2 instance as a Kafka client to connect to an IAM-authenticated MSK cluster for batch processing.

Objectives
Establish a data processing system on AWS mimicking Pinterest's capabilities.
Configure the EC2 Kafka client for efficient batch processing.
Key Learnings
Secure storage and management of .pem files for EC2 instance access.
Establishing SSH connections to EC2 instances.
Installing and configuring Kafka and IAM MSK authentication packages.
Setting up IAM roles and configuring Kafka clients for AWS IAM authentication.
Creating Kafka topics with appropriate naming conventions.
Milestone 3: Batch Processing - Configure the EC2 Kafka Client
Aim
To establish a robust and scalable Kafka client on an AWS EC2 instance optimized for efficient batch processing.

Tasks
Creating PEM File Locally

Securely create and store the .pem file for EC2 instance access.
Identify the EC2 instance's Key pair name and save the .pem file accordingly.
Connecting to the EC2 Instance

Follow the SSH client instructions in the EC2 console to connect to the EC2 instance.
Setting Up Kafka on EC2 Instance

Install Kafka on the EC2 client machine, ensuring version compatibility with the MSK cluster.
Install the IAM MSK authentication package for MSK cluster access.
Configure an IAM role for MSK cluster authentication.
Modify the client.properties file to enable AWS IAM authentication for the Kafka client.
Creating Kafka Topics

Obtain Bootstrap servers and Plaintext Apache Zookeeper connection strings from the MSK Management Console.
Create Kafka topics with specified names, emphasizing precise naming to avoid permission errors.
Installation
Kafka Setup
Follow the official Kafka installation guide for Kafka setup.

AWS EC2 and Services Configuration
Refer to the AWS EC2 Configuration Guide for setting up the AWS EC2 instance and configuring AWS services.

IAM MSK Authentication Package
Install the IAM MSK authentication package as described in Task 3, Step 2.

Usage
Ensure your EC2 instance is running and connected.
Install Kafka and IAM MSK authentication packages on your EC2 client machine.
Configure the IAM role as described in Task 3, Step 3.
Modify the Kafka client's client.properties file for AWS IAM authentication.
Create Kafka topics as described in Task 4, Step 2.
File Structure
graphql
Copy code
your-project-name/
│
├── data_emulation/
│   ├── aws_db_connector        # Connects to AWS RDS and emulates Pinterest data
│   ├── data_fetchers/
│   │   ├── pin_data.py        # Fetches pin_data from AWS RDS
│   │   ├── user_data.py       # Fetches user_data from AWS RDS
│   │   └── geo_data.py        # Fetches geo_data from AWS RDS
│   └── s3_to_databricks.ipynb            # Uploads emulated data from S3 bucket to Databricks
│
├── databricks_notebooks/
│   ├── batch_preprocessing_on_databricks.ipynb    # Databricks notebook for preprocessing batch data using PySpark
│   └── streaming_data_from_kinesis_to_databricks_using_pyspark.ipynb   # Databricks notebook for preprocessing streaming data using PySpark
│
├── airflow_dags/
│   ├── 0a5afda0229f_dag.py        # Airflow DAG for batch data processing orchestration
│
├── kinesis_streaming/
│   ├── pin_streaming_data.py       # Connects to AWS Kinesis for real-time pin_data streaming
│   └── user_streaming_data.py      # Connects to AWS Kinesis for real-time user_data streaming
│   └── geo_streaming_data.py       # Connects to AWS Kinesis for real-time geo_data streaming
│
├── requirements.txt                   # List of Python dependencies
├── .env.sample                        # Sample environment file for storing sensitive data
├── README.md                          # Project description and instructions
├── LICENSE                            # License file
│
└── [other configuration and root files, like .gitignore, setup.py, etc.]
Milestone 4: Batch Processing - Connect MSK Cluster to S3 Bucket
Aim
To connect the MSK cluster to an S3 bucket, enabling automatic data storage in the designated S3 bucket.

Key Learnings
Configuring an IAM authenticated MSK cluster to connect to an S3 bucket.
Creating custom plugins and connectors within the MSK Connect console.
The importance of IAM roles for authentication and efficient data management.
Installation
Refer to the following resources for detailed installation:

AWS S3 Configuration Guide
Amazon MSK Documentation
Download the Confluent.io Amazon S3 Connector from Confluent Hub and copy it to your S3 bucket.

Usage
Ensure your IAM authenticated MSK cluster is operational.
Verify your S3 bucket setup.
Download and copy the Confluent.io Amazon S3 Connector to your S3 bucket.
Create a custom plugin in the MSK Connect console.
Build a connector in the MSK Connect console.
Configure the connector with the appropriate bucket name and IAM role.
Milestone 5: Batch Processing - Configuring an API Gateway
Aim
To configure an API Gateway to enable data transfer from the API to the MSK cluster and automatic storage in an S3 bucket.

Key Learnings
Setting up a Kafka REST Proxy integration for an API Gateway.
Installing and configuring the Kafka REST Proxy on an EC2 client.
Sending data from the API to Kafka topics and verifying data flow.
Installation
Refer to the following resources for detailed installation:

AWS API Gateway Documentation
Confluent package for the Kafka REST Proxy available here.
Usage
Ensure your API Gateway is configured.
Install and configure the Kafka REST Proxy on your EC2 client machine.
Modify the user_posting_emulation.py script to send data from the API to Kafka topics.
Verify data transmission and storage in the S3 bucket.
Milestone 6: Batch Processing - Databricks
Aim
To set up data transfer from an S3 bucket to Databricks for data preparation.

Key Learnings
Mounting an S3 bucket to Databricks.
Reading data from S3 into Databricks DataFrames.
Data organization and preparation for further analysis.
Usage
Ensure your Databricks account is operational.
Mount your S3 bucket to Databricks using provided credentials.
Read data from S3 into Databricks DataFrames.
Create and use DataFrames for data cleaning and querying.
Milestone 7: Batch Processing - Spark on Databricks
Aim
To perform data cleaning and computation using Spark on Databricks.

Key Learnings
Advanced data cleaning and computation using Spark.
Data transformations for improved analysis.
Insights into category popularity, user followers, and joining patterns.
Data Cleaning and Computation Tasks
Clean DataFrame containing Pinterest posts.
Clean DataFrame containing geo locations.
Clean DataFrame containing user info.
Determine the most popular category in each country.
Track category popularity annually.
Identify users with the highest followers in each country.
Determine the country with the user having the most followers.
Identify popular categories among different age groups.
Track user registrations by year.
Calculate the median follower count by joining year.
Analyze the median follower count by joining year and age group.
Milestone 8: Batch Processing - AWS MWAA (Managed Workflow for Apache Airflow)
Aim
To orchestrate Databricks workloads using AWS MWAA, automating data processing tasks and scheduling Databricks Notebooks.

Key Learnings
Orchestrating Databricks workloads with AWS MWAA.
Creating and uploading Airflow DAGs.
Triggering orchestrated tasks.
Usage
Create and upload DAG to MWAA environment.
Trigger DAG to run on Databricks Notebook.
Milestone 9: Stream Processing - AWS Kinesis
Aim
To ingest and process streaming data with AWS Kinesis in real-time.

Key Learnings
Ingesting and processing streaming data with AWS Kinesis.
Configuring REST APIs for Kinesis interaction.
Cleaning and storing streaming data in Delta Tables.
Stream Processing Tasks
Create data streams using Kinesis Data Streams.
Configure an API with Kinesis proxy integration.
Send data to Kinesis streams.
Read data from Kinesis streams to Databricks.
Transform Kinesis data streams in Databricks.
Write the streaming data to Delta Tables.
License
This project is licensed under the MIT License - see the LICENSE file for details.
