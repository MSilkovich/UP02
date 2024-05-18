from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_table_data():
    url = 'http://localhost:5555/'  # URL of the webpage with the table
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', id='input-table')  # Finding the table by ID

        if table:
            data = []
            rows = table.find_all('tr')  # Find all table rows

            for row in rows:
                cells = row.find_all('td')  # Find all cells in each row
                row_data = [cell.get_text(strip=True) for cell in cells] # Extract text from each cell
                data.append(row_data)

            return render_template('table_data.html', table_data=data)
        else:
            return 'Table with ID "input-table" not found on the webpage'
    else:
        return 'Failed to fetch data from the webpage'

if __name__ == '__main__':
    app.run(debug=True)