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

