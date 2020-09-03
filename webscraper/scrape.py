import os
import csv
import shutil
import requests
import pandas as pd
from bs4 import BeautifulSoup


def create_data(file_name):
    file = open(file_name, "r")
    data = list(csv.reader(file))
    file.close()
    return data


def main():
    data = create_data("names.csv")

    path = r'C:\Users\codys\PycharmProjects\Pokemon\webscraper\learnable_moves'
    for i in range(438, len(data)):
        name = data[i+1][0]
        print(name)
        file = name + '.csv'

        URL = 'https://pokemondb.net/pokedex/' + name
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'lxml')

        tb = soup.find('table', class_="data-table")

        new_table = parse_html_table(tb)

        print(new_table)
        new_table.to_csv(name + ".csv", index=False)
        destination = path
        source = os.path.join(r"C:\Users\codys\PycharmProjects\Pokemon\webscraper", file)
        shutil.move(source, destination)


def parse_html_table(table):
    n_columns = 0
    n_rows = 0
    column_names = []

    # Find number of rows and columns
    # we also find the column titles if we can
    for row in table.find_all('tr'):

        # Determine the number of rows in the table
        td_tags = row.find_all('td')
        if len(td_tags) > 0:
            n_rows += 1
            if n_columns == 0:
                # Set the number of columns for our table
                n_columns = len(td_tags)

        # Handle column names if we find them
        th_tags = row.find_all('th')
        if len(th_tags) > 0 and len(column_names) == 0:
            for th in th_tags:
                column_names.append(th.get_text())

    # Safeguard on Column Titles
    if len(column_names) > 0 and len(column_names) != n_columns:
        raise Exception("Column titles do not match the number of columns")

    columns = column_names if len(column_names) > 0 else range(0, n_columns)
    df = pd.DataFrame(columns=columns,
                      index=range(0, n_rows))
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            df.iat[row_marker, column_marker] = column.get_text()
            column_marker += 1
        if len(columns) > 0:
            row_marker += 1

    # Convert to float if possible
    for col in df:
        try:
            df[col] = df[col].astype(float)
        except ValueError:
            pass

    return df

main()

