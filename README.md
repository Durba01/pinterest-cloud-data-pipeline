# Pinterest-Cloud-Data-Pipeline

## Project Title

Pinterest-Like Data Processing on AWS

## Table of Contents

- [Description](#description)
- [Objectives](#objectives)
- [Key Learnings](#key-learnings)
- [Milestones](#milestones)
  - [Milestone 3: Batch Processing - Configure the EC2 Kafka Client](#milestone-3-batch-processing---configure-the-ec2-kafka-client)
  - [Milestone 4: Batch Processing - Connect MSK Cluster to S3 Bucket](#milestone-4-batch-processing---connect-msk-cluster-to-s3-bucket)
  - [Milestone 5: Batch Processing - Configuring an API Gateway](#milestone-5-batch-processing---configuring-an-api-gateway)
  - [Milestone 6: Batch Processing - Databricks](#milestone-6-batch-processing---databricks)
  - [Milestone 7: Batch Processing - Spark on Databricks](#milestone-7-batch-processing---spark-on-databricks)
  - [Milestone 8: Batch Processing - AWS MWAA](#milestone-8-batch-processing---aws-mwaa)
  - [Milestone 9: Stream Processing - AWS Kinesis](#milestone-9-stream-processing---aws-kinesis)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

This project aims to replicate Pinterest's data processing capabilities using AWS services. It involves setting up a robust, scalable data pipeline leveraging AWS EC2, MSK (Managed Streaming for Apache Kafka), S3, Databricks, and other AWS services to handle batch and stream processing efficiently.

## Objectives

- Establish a data processing system on AWS mimicking Pinterest's capabilities.
- Configure EC2 instances and Kafka for batch processing.
- Connect MSK to S3 for automatic data storage.
- Implement an API Gateway for data transfer.
- Transfer and process data using Databricks.
- Orchestrate tasks using AWS MWAA (Managed Workflow for Apache Airflow).
- Ingest and process streaming data using AWS Kinesis.

## Key Learnings

- **Secure and Efficient Data Management:** Ensuring secure storage of access credentials and configuring IAM roles and policies for secure data access and processing.
- **Scalable Data Processing:** Setting up a scalable Kafka client and MSK cluster for handling large data volumes.
- **Seamless Data Transfer:** Implementing API Gateways and Kafka REST Proxy for smooth data transfer between components.
- **Advanced Data Analytics:** Leveraging Databricks and Spark for comprehensive data cleaning, transformation, and analysis.
- **Automation and Orchestration:** Utilizing AWS MWAA to automate and orchestrate data processing tasks, enhancing efficiency.
- **Real-time Data Processing:** Integrating AWS Kinesis for real-time data ingestion and processing, ensuring timely data updates and analysis.

## Milestones

### Milestone 3: Batch Processing - Configure the EC2 Kafka Client

**Objective:** Establish a Kafka client on an AWS EC2 instance for efficient batch processing.

**Tasks:**

1. **Creating PEM File Locally:**
   - Generate and securely store a .pem file for EC2 access.
   - Identify the EC2 instance's Key pair name.

2. **Connecting to the EC2 Instance:**
   - Follow SSH client instructions to connect to the EC2 instance.

3. **Setting Up Kafka on EC2 Instance:**
   - Install Kafka and ensure compatibility with the MSK cluster.
   - Install IAM MSK authentication package for access.
   - Configure IAM roles for MSK cluster authentication.
   - Modify `client.properties` for AWS IAM authentication.

4. **Creating Kafka Topics:**
   - Obtain Bootstrap servers and connection strings from MSK.
   - Create Kafka topics with specific names to avoid permission errors.

### Milestone 4: Batch Processing - Connect MSK Cluster to S3 Bucket

**Objective:** Enable automatic data storage in S3 from the MSK cluster.

**Tasks:**

1. **Connect MSK to S3:**
   - Configure IAM roles and policies for access.
   - Set up MSK Connect with custom plugins and connectors.
   - Ensure data flows from Kafka topics to the S3 bucket.

### Milestone 5: Batch Processing - Configuring an API Gateway

**Objective:** Facilitate data transfer from an API to the MSK cluster and S3.

**Tasks:**

1. **Set Up API Gateway:**
   - Configure Kafka REST Proxy integration.
   - Install and configure Kafka REST Proxy on EC2.
   - Modify scripts to send data from the API to Kafka topics.
   - Verify data flow from the API to Kafka and storage in S3.

### Milestone 6: Batch Processing - Databricks

**Objective:** Transfer and prepare data from S3 to Databricks for analysis.

**Tasks:**

1. **Mount S3 Bucket to Databricks:**
   - Use credentials to access S3 data.
   - Read data into Databricks DataFrames.
   - Organize and prepare data for further analysis.

### Milestone 7: Batch Processing - Spark on Databricks

**Objective:** Perform data cleaning and computation using Spark on Databricks.

**Tasks:**

1. **Clean and Transform Data:**
   - Use Spark to clean and transform data.
   - Analyze data for insights into category popularity, user behavior, and trends.

### Milestone 8: Batch Processing - AWS MWAA (Managed Workflow for Apache Airflow)

**Objective:** Orchestrate Databricks workloads using AWS MWAA, automating data processing tasks and scheduling Databricks Notebooks.

**Tasks:**

1. **Create and Upload Airflow DAGs:**
   - Automate and schedule data processing tasks.
   - Trigger Databricks Notebooks execution via Airflow DAGs.

### Milestone 9: Stream Processing - AWS Kinesis

**Objective:** Ingest and process real-time data streams using AWS Kinesis.

**Tasks:**

1. **Create and Manage Data Streams:**
   - Set up Kinesis data streams for different data types.
   - Configure REST APIs for interaction with Kinesis.
   - Send and process streaming data, storing results in Delta Tables.

## Installation

### Kafka Setup

Follow the [official Kafka installation guide](https://kafka.apache.org/quickstart) for Kafka setup.

### AWS EC2 and Services Configuration

Refer to the [AWS EC2 Configuration Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) for setting up the AWS EC2 instance and configuring AWS services.

### IAM MSK Authentication Package

Install the IAM MSK authentication package as described in [Task 3, Step 2](#milestone-3-batch-processing---configure-the-ec2-kafka-client).

## Usage

1. Ensure your EC2 instance is running and connected.
2. Install Kafka and IAM MSK authentication packages on your EC2 client machine.
3. Configure the IAM role as described in [Task 3, Step 3](#milestone-3-batch-processing---configure-the-ec2-kafka-client).
4. Modify the Kafka client's `client.properties` file for AWS IAM authentication.
5. Create Kafka topics as described in [Task 4, Step 2](#milestone-3-batch-processing---configure-the-ec2-kafka-client).

## File Structure

Pinterest-Cloud-Data-Pipelines/
│
├── data_emulation/
│ ├── aws_db_connector # Connects to AWS RDS and emulates Pinterest data
│ ├── data_fetchers/
│ │ ├── pin_data.py # Fetches pin_data from AWS RDS
│ │ ├── user_data.py # Fetches user_data from AWS RDS
│ │ └── geo_data.py # Fetches geo_data from AWS RDS
│ └── s3_to_databricks.ipynb # Uploads emulated data from S3 bucket to Databricks
│
├── databricks_notebooks/
│ ├── batch_preprocessing_on_databricks.ipynb # Databricks notebook for preprocessing batch data using PySpark
│ └── streaming_data_from_kinesis_to_databricks_using_pyspark.ipynb # Databricks notebook for preprocessing streaming data using PySpark
│
├── airflow_dags/
│ ├── 0a5afda0229f_dag.py # Airflow DAG for batch data processing orchestration
│
├── kinesis_streaming/
│ ├── pin_streaming_data.py # Connects to AWS Kinesis for real-time pin_data streaming
│ └── user_streaming_data.py # Connects to AWS Kinesis for real-time user_data streaming
│ └── geo_streaming_data.py # Connects to AWS Kinesis for real-time geo_data streaming
│
├── requirements.txt # List of Python dependencies
├── .env.sample # Sample environment file for storing sensitive data
├── README.md # Project description and instructions
├── LICENSE # License file
│
└── [other configuration and root files, like .gitignore, setup.py, etc.]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

