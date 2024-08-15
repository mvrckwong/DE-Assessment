# DE-Assessment

This is the solution set for technical exam. All outputs are within ".images" folder. The project implements the following:
- Transformation from raw schema to staging schema
- Transformation using python.

### Data Architecture
Here is the data architecture guide to the Medallion Architecture, plus the technical stack. I almost always use this deployment strategy and data architecture in building the foundation of the data pipeline.
![alt text](.images/data_architecture.jpg)

### Data Processes
There are 4 python data processes implemented. 

- 00_setup_db.py - Setup the database to the Medallion Architecture
- 01_ingest.py - Ingest the data to the database.
- 02_transform.py - Transform the data from raw schema database, to staging schema database. This involve denormalization techniques, cleaning the data, processing the data, etc.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tech Stack
- Python
- Pandas
- Docker / Container
- PostgreSQL
- Virtual Environment

### Roadmap
- Improve database service and infrastructure. 
- Improve the security. (Azure Key Vault, AWS Secret Manager, HashiCorp Vault)
- Improve the observability and monitoring. (Airflow, Mage)
- Improve the performance. Consider other python libraries.


## Getting Started / Implementation

### Prerequisite

Before running the python streamlit application, you should have the following installed in your local machine. 

1. Install the Python 3.9 or higher version, until 3.11. Also, install the latest version of the docker. We will be using docker-compose to run the airflow application (future) and the streamlit application.
2. Install the poetry library. The library will handle all your python dependencies and virtual environment in your local machine.
    ``` bash
    pip install poetry
    ```
3. Install the project dependencies by installing. Poetry will handle all your python dependencies and virtual environment in your local machine.
    ``` bash
    poetry install
    ```

### Running the Data Pipeline

Right now, some python functions are not 100% working in Airflow Deployment. For now, we will be using the command line with poetry to run the data-pipeline.

- Running the pretest.py
    ``` bash
    poetry run python src/pretest.py
    ```
- Running the transform.py
    ``` bash
    poetry run python src/transform.py
    ```
- Running the ingest.py
    ``` bash
    poetry run python src/ingest.py
    ```
- Running the validate_ingest.py
    ``` bash
    poetry run python src/validate_ingest.py
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Other Outputs

### Data Modeling
![alt text](.images/erd.png)

### DB Raw Schema
![alt text](.images/db_raw_schema.png)

### DB Staging Schema
![alt text](.images/db_stg_schema.png)

### Others (Docker, Connection Details)
![alt text](.images/docker.png)
![alt text](.images/connection_details.png)

