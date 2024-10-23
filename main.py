import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


# Start the FastAPI application

app = FastAPI()


# Define the allowed origins (your React app's URL)
origins = [
    "http://localhost:3000",  # React app local development server
    # React app in production (if applicable)
    "https://deciphertechnicalhub.netlify.app"
]

# Add CORS middleware to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


def sec_to_excel(url:str):
    headers = {
        'User-Agent': 'luv.ratan@decipherfinancials.co.in'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    stringSoup = str(soup)

    # Find all table elements in the HTML
    tables = soup.find_all("table")
    print(f"Number of tables found: {len(tables)}")

    # Create a dictionary for each table found
    table_dicts = []
    for idx, table in enumerate(tables):
        table_dict = {
            "Table_Index": idx,
            "Table_HTML": str(table)  # Store the HTML content of the table
        }
        table_dicts.append(table_dict)

    return {
        "full_html": stringSoup,
        "tables": table_dicts
    }


@app.get("/fetch-free-sec-data")
async def checkTable(url :str = Query(...)):
    data = sec_to_excel(url)
    return data


@app.get("/")
def homePage():
    return "Hello World"




