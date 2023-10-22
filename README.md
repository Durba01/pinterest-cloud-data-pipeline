# pinterest-cloud-data-pipeline
# Project Title

Pinterest-Like Data Processing on AWS

## Table of Contents

- [Description](#description)
- [Progress in Milestone 3](#progress-in-milestone-3)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

### What it Does

This project aims to replicate Pinterest's data processing system on the AWS Cloud. It involves setting up an EC2 instance as a Kafka client to connect to an IAM authenticated MSK cluster for batch processing.

### Aim of the Project

The primary goal of this project is to create a data processing system on AWS that emulates Pinterest's data processing capabilities. In Milestone 3, we configure the EC2 Kafka client for this purpose.

### What You Learned

- The importance of securely storing .pem files for EC2 instance access.
- Establishing an SSH connection to an EC2 instance.
- Installing Kafka and IAM MSK authentication packages, ensuring compatibility with the MSK cluster.
- Configuring IAM roles and the Kafka client for AWS IAM authentication.
- Creating Kafka topics with precise naming to avoid permission errors.

## MILESTONE 3: BACTH PROCESSING: CONFIGURE THE EC2 KAFKA CLIENT 

### Task 1: Creating PEM File Locally

- In Step 1, we successfully created a .pem file and highlighted the need for secure storage.
- In Step 2, we identified the EC2 instance's Key pair name and saved the .pem file accordingly.

### Task 2: Connecting the EC2 Instance

- We followed the provided SSH client instructions in the EC2 console, successfully connecting to the EC2 instance.

### Task 3: Setting Up Kafka on EC2 Instance

- In Step 1, we installed Kafka on the EC2 client machine, ensuring version compatibility with the MSK cluster (e.g., Kafka 2.12-2.8.1).
- In Step 2, we installed the IAM MSK authentication package for MSK cluster access.
- In Step 3, we configured an IAM role, allowing us to assume the <your_UserId>-ec2-access-role for MSK cluster authentication.
- In Step 4, we modified the client.properties file to enable AWS IAM authentication for the Kafka client.

### Task 4: Creating Kafka Topics

- In Step 1, we obtained Bootstrap servers and Plaintext Apache Zookeeper connection strings from the MSK Management Console.
- In Step 2, we created three Kafka topics with the specified names: <your_UserId>.pin, <your_UserId>.geo, and <your_UserId>.user.
- We emphasized the importance of precise topic naming to avoid permission errors.

## Installation

To set up Kafka, please follow the [official Kafka installation guide](https://kafka.apache.org/quickstart).

For setting up AWS EC2 instance and configuring AWS services, please refer to the [AWS EC2 Configuration Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).

Ensure that you have also installed the IAM MSK authentication package on your EC2 client machine as described in [Task 3, Step 2](#task-3-setting-up-kafka-on-ec2-instance).

## Usage

1. Ensure that your EC2 instance is running and connected.
2. Install Kafka and IAM MSK authentication packages on your EC2 client machine.
3. Configure the IAM role as described in [Task 3, Step 3](#task-3-setting-up-kafka-on-ec2-instance).
4. Modify the Kafka client's `client.properties` file for AWS IAM authentication.
5. Create Kafka topics as described in [Task 4, Step 2](#task-4-creating-kafka-topics).

## File Structure

- **Your_Project_Folder/**
  - **Milestone3/**
    - `user_posting_emulation.py`
    - `client.properties`
  - **kafka_folder/**
    - **bin/**
      - Kafka related binaries and configurations.
  - **Your_Documents/**
    - Any other project-related files or documentation.


## MILESTONE 4: BACTH PROCESSING: CONNNECT MSK CLUSTER TO S3 BUCKET

### Aim of Milestone 4

Milestone 4 focuses on connecting the MSK cluster to an S3 bucket. This integration ensures that any data passing through the IAM authenticated MSK cluster is automatically saved in the designated S3 bucket. This capability enhances the data processing and storage capabilities of the project.

### Milestone Takeaway

- The process of connecting an IAM authenticated MSK cluster to an S3 bucket, enabling automatic data storage.
- Configuring and creating custom plugins and connectors within the MSK Connect console.
- The importance of IAM roles for authentication and the role of connectors in efficient data management.

## Installation

For detailed installation, please refer to the following resources:

- To configure your AWS S3 bucket, IAM roles, and MSK cluster, please follow the [AWS S3 Configuration Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro.html) and [Amazon MSK Documentation](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html).

- Download the Confluent.io Amazon S3 Connector to your EC2 client machine. The connector can be found at [Confluent Hub](https://www.confluent.io/hub/). Copy this connector to the S3 bucket specified in your project configuration.

## Usage

1. Ensure that your IAM authenticated MSK cluster is operational and configured.
2. Verify that your S3 bucket is correctly set up as per AWS documentation.
3. Download the Confluent.io Amazon S3 Connector to your EC2 client machine and copy it to your S3 bucket.
4. Create a custom plugin with the name <your_UserId>-plugin in the MSK Connect console.
5. In the MSK Connect console, build a connector named <your_UserId>-connector.
6. Configure the connector to specify the correct bucket name as user-<your_UserId>-bucket. Ensure that the `topics.regex` field follows the structure: <your_UserId>.*.
7. Choose the IAM role used for authentication to the MSK cluster, which should follow the format <your_UserId>-ec2-access-role.

## File Structure

- **Your_Project_Folder/**
  - **Milestone4/**
    - Any files related to this milestone.
  - **Your_Documents/**
    - Any other project-related files or documentation.


## MILESTONE 5: BACTH PROCESSING: CONFIGURING AN API GATEWAY

### Aim of Milestone 5

Milestone 5 focuses on configuring an API Gateway to enable data transfer from the API to the MSK cluster and automatic storage in an S3 bucket. The project establishes a complete data processing pipeline, from data ingestion to storage.

### What You Learned

- Setting up a Kafka REST Proxy integration method for an API Gateway.
- Installing and configuring the Kafka REST Proxy on an EC2 client.
- Sending data from the API to Kafka topics and verifying data flow to the MSK cluster and storage in the S3 bucket.

## Installation

For detailed installation, please refer to the following resources:

- To set up your API Gateway and integrate the Kafka REST Proxy, follow the [AWS API Gateway Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-getting-started.html).

- Install the Confluent package for the Kafka REST Proxy on your EC2 client machine. You can find the package [here](https://www.confluent.io/hub/).

Ensure that your IAM roles, MSK cluster, and the connector for S3 storage are configured as per Milestone 4 documentation.

## Usage

1. Ensure that your API Gateway is configured, and the Kafka REST Proxy integration is in place.
2. Install the Confluent package for the Kafka REST Proxy on your EC2 client machine and configure it to enable IAM authentication to the MSK cluster.
3. Modify the `user_posting_emulation.py` script to send data from the API to your Kafka topics using the API's Invoke URL.
4. Verify data transmission by running a Kafka consumer for each topic. Ensure messages are being consumed.
5. Check the S3 bucket for data storage, observing the folder organization created by your connector.


## MILESTONE 6: BACTH PROCESSING: DATABRICKS
### Aim of Milestone 6

Milestone 6 involves setting up data transfer from an S3 bucket to Databricks, a vital step for data preparation within the Databricks platform.

### What You Learned

- Mounting an S3 bucket to Databricks for data access.
- Reading data from S3 into Databricks DataFrames.
- Data organization and preparation for further analysis.

## Installation

For this milestone, you don't need to perform additional installations as your Databricks account already has full access to S3, with the necessary credentials provided in the "authentication_credentials.csv" file.

Ensure that you specify the complete path to JSON objects when reading data from S3, following the S3 bucket's structure (e.g., topics/<your_UserId>.pin/partition=0/).

## Usage

1. Ensure your Databricks account is operational.
2. Mount your S3 bucket to Databricks using the provided credentials in "authentication_credentials.csv."
3. Read data from S3 into Databricks DataFrames.
4. Create three separate DataFrames: `df_pin` for Pinterest post data, `df_geo` for geolocation data, and `df_user` for user data.
5. Use these DataFrames for data cleaning and querying as needed.



## MILESTONE 7: BACTH PROCESSING: SPARK ON DATABRICKS

### Aim of Milestone 7

Milestone 7 focuses on data cleaning and computation using Spark on Databricks. It involves a series of tasks that transform and analyze the project's data, providing valuable insights.

### What You Learned

- Advanced data cleaning and computation using Spark on Databricks.
- Data transformations for improved analysis.
- Insights into category popularity, user followers, and joining patterns.

## Data Cleaning and Computation Tasks

**Task 1: Clean DataFrame Containing Pinterest Posts**

- Transformation of data to ensure consistency and data quality.

**Task 2: Clean DataFrame Containing Geo Locations**

- Creation of a new "coordinates" column and data type conversion for geographic data.

**Task 3: Clean Data Containing User Info**

- Combining user names, date conversion, and data organization.

**Task 4: Find the Most Popular Category in Each Country**

- Determining the most popular Pinterest category in each country.

**Task 5: Find the Most Popular Category Each Year**

- Tracking category popularity annually between 2018 and 2022.

**Task 6: Find the User with the Most Followers in Each Country**

- Identifying users with the highest followers in each country.

**Task 7: Find the Country with the User Having the Most Followers**

- Determining the country where the user with the most followers resides.

**Task 8: Find the Most Popular Category for Different Age Groups**

- Identifying popular categories among different age groups.

**Task 9: Find How Many Users Joined Each Year**

- Tracking user registrations between 2015 and 2020.

**Task 10: Find the Median Follower Count of Users by Joining Year**

- Calculating the median follower count for users who joined between 2015 and 2020.

**Task 11: Find the Median Follower Count Based on Joining Year and Age Group**

- Analyzing the median follower count for users who joined between 2015 and 2020, categorized by age group.

In Milestone 7, data cleaning and computation using Spark on Databricks significantly enhance the project's analytical capabilities. A series of tasks provide insights into data quality, user behavior, and category popularity, ensuring that the project's data remains actionable for further analysis.


## MILESTONE 8: BACTH PROCESSING: AWS MWAA (MANAGED WORKFLOW FOR APACHE AIRFLOW)
### Aim of Milestone 8

Milestone 8 focuses on orchestrating Databricks workloads using AWS MWAA (Managed Workflow for Apache Airflow). It streamlines the automation of data processing tasks and scheduling Databricks Notebooks.

### What You Learned

- Orchestrating Databricks workloads with AWS MWAA.
- Creating and uploading Airflow DAGs.
- Triggering orchestrated tasks.

## Orchestrating Databricks Workloads with AWS MWAA

**Task 1: Create and Upload DAG to MWAA Environment**

In Milestone 8, the project advances to orchestrating Databricks workloads using AWS MWAA. This task requires the creation of an Airflow DAG that triggers Databricks Notebooks on a specified schedule. Access to the MWAA environment and its associated S3 bucket has been granted, simplifying setup.

**Task 2: Trigger DAG to Run on Databricks Notebook**

This step involves manually triggering the previously uploaded DAG, ensuring successful execution. The project now benefits from orchestrated Databricks workloads, enhancing automation and efficiency.

Milestone 8 marks a significant milestone in the project's evolution, allowing for orchestrated and automated Databricks workloads using AWS MWAA. The creation and upload of Airflow DAGs streamline the scheduling and execution of Databricks Notebooks, advancing the project's data processing capabilities.


## MILESTONE 9: STREAM PROCESSING: AWS KINESIS

### Aim of Milestone 9

Milestone 9 is all about stream processing using AWS Kinesis. It focuses on ingesting streaming data into the project and processing it in real-time.

### What You Learned

- Ingesting and processing streaming data with AWS Kinesis.
- Configuring REST APIs for Kinesis interaction.
- Cleaning and storing streaming data in Delta Tables.

## Stream Processing with AWS Kinesis

**Task 1: Create Data Streams Using Kinesis Data Streams**

In Milestone 9, the project advances to stream processing with AWS Kinesis. The first task involves creating three dedicated data streams for different Pinterest tables. Specific permissions are granted for stream creation.

**Task 2: Configure an API with Kinesis Proxy Integration**

This task revolves around configuring a REST API to interact with Kinesis, with permissions to perform various Kinesis actions. An access role is designated for API integration.

**Task 3: Send Data to Kinesis Streams**

A new script, "user_posting_emulation_streaming.py," is introduced to send data requests to the API. These requests add records to the Kinesis streams, handling data from different Pinterest tables.

**Task 4: Read Data from Kinesis Streams to Databricks**

This step includes reading data from the Kinesis streams into Databricks. Access credentials are obtained, data ingestion is executed, and data is fetched in a Databricks Notebook.

**Task 5: Transform Kinesis Data Streams in Databricks**

The streaming data is cleaned and processed in a manner similar to batch data.

**Task 6: Write the Streaming Data to Delta Tables**

The final step involves saving the cleaned streaming data into Delta Tables, ensuring real-time data storage and analysis.

Milestone 9 marks a significant stride in the project's development, allowing it to harness real-time streaming data with AWS Kinesis. The creation of data streams, API configuration, data ingestion, and storage in Delta Tables enhance the project's capabilities for processing and analyzing streaming data.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

