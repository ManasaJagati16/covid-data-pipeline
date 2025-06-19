import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv("include/config.env")

def load_to_snowflake():
    try:
        # Load .env variables
        user = os.getenv("SNOWFLAKE_USER")
        password = os.getenv("SNOWFLAKE_PASSWORD")
        account = os.getenv("SNOWFLAKE_ACCOUNT")
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
        database = os.getenv("SNOWFLAKE_DATABASE")
        schema = os.getenv("SNOWFLAKE_SCHEMA")

        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        cursor = conn.cursor()

        # Read the CSV
        df = pd.read_csv("data/covid_data.csv")

        # Create table if not exists
        create_table_sql = """
        CREATE OR REPLACE TABLE covid_data (
            updated NUMBER,
            cases NUMBER,
            todayCases NUMBER,
            deaths NUMBER,
            todayDeaths NUMBER,
            recovered NUMBER,
            todayRecovered NUMBER,
            active NUMBER,
            critical NUMBER,
            casesPerOneMillion FLOAT,
            deathsPerOneMillion FLOAT,
            tests NUMBER,
            testsPerOneMillion FLOAT,
            population NUMBER,
            fetched_at STRING
        );
        """
        cursor.execute(create_table_sql)

        # Insert rows into Snowflake
        for _, row in df.iterrows():
            insert_sql = f"""
            INSERT INTO covid_data VALUES (
                {row['updated']}, {row['cases']}, {row['todayCases']}, {row['deaths']}, {row['todayDeaths']},
                {row['recovered']}, {row['todayRecovered']}, {row['active']}, {row['critical']},
                {row['casesPerOneMillion']}, {row['deathsPerOneMillion']}, {row['tests']},
                {row['testsPerOneMillion']}, {row['population']}, '{row['fetched_at']}'
            );
            """
            cursor.execute(insert_sql)

        print("Data loaded into Snowflake table 'covid_data'")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Failed to load data into Snowflake: {e}")
=======
import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

# Load credentials
load_dotenv("include/config.env")

def load_to_snowflake():
    try:
        # Load .env variables
        user = os.getenv("SNOWFLAKE_USER")
        password = os.getenv("SNOWFLAKE_PASSWORD")
        account = os.getenv("SNOWFLAKE_ACCOUNT")
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
        database = os.getenv("SNOWFLAKE_DATABASE")
        schema = os.getenv("SNOWFLAKE_SCHEMA")

        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        cursor = conn.cursor()

        # Read the CSV
        df = pd.read_csv("data/covid_data.csv")

        # Create table if not exists
        create_table_sql = """
        CREATE OR REPLACE TABLE covid_data (
            updated NUMBER,
            cases NUMBER,
            todayCases NUMBER,
            deaths NUMBER,
            todayDeaths NUMBER,
            recovered NUMBER,
            todayRecovered NUMBER,
            active NUMBER,
            critical NUMBER,
            casesPerOneMillion FLOAT,
            deathsPerOneMillion FLOAT,
            tests NUMBER,
            testsPerOneMillion FLOAT,
            population NUMBER,
            fetched_at STRING
        );
        """
        cursor.execute(create_table_sql)

        # Insert rows into Snowflake
        for _, row in df.iterrows():
            insert_sql = f"""
            INSERT INTO covid_data VALUES (
                {row['updated']}, {row['cases']}, {row['todayCases']}, {row['deaths']}, {row['todayDeaths']},
                {row['recovered']}, {row['todayRecovered']}, {row['active']}, {row['critical']},
                {row['casesPerOneMillion']}, {row['deathsPerOneMillion']}, {row['tests']},
                {row['testsPerOneMillion']}, {row['population']}, '{row['fetched_at']}'
            );
            """
            cursor.execute(insert_sql)

        print("Data loaded into Snowflake table 'covid_data'")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Failed to load data into Snowflake: {e}")

