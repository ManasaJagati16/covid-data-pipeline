import requests
import pandas as pd
from datetime import datetime
import os

def extract_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        df = pd.json_normalize(data)
        df["fetched_at"] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        os.makedirs("data", exist_ok=True)
        output_path = "data/covid_countries_data.csv"
        df.to_csv(output_path, index=False)

        print(f"Saved {len(df)} rows to {output_path}")

    except Exception as e:
        print(f"Failed to extract data: {e}")

if __name__ == "__main__":
    extract_covid_data()
=======
import requests
import pandas as pd
from datetime import datetime
import os

def extract_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        df = pd.json_normalize(data)
        df["fetched_at"] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        os.makedirs("data", exist_ok=True)
        output_path = "data/covid_countries_data.csv"
        df.to_csv(output_path, index=False)

        print(f"Saved {len(df)} rows to {output_path}")

    except Exception as e:
        print(f"Failed to extract data: {e}")

if __name__ == "__main__":
    extract_covid_data()
