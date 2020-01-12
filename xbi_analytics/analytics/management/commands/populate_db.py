import csv
import json
import datetime
from django.core.management.base import BaseCommand
from analytics.models import GraphData, GridData, PieChartData

class Command(BaseCommand):
    args = ''
    help = 'command to populate database from csv files'

    def _read_graphdata_csv_file(self):
        file_name = 'Пример XBI - 1.csv'
        print(f'Reading {file_name}')
        
        data = []
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_number = 0
            
            for row in csv_reader:
                if line_number > 0:
                    date_raw = row["Дата"]
                    date = datetime.datetime(
                        int(date_raw.split('/')[2]),
                        int(date_raw.split('/')[0]),
                        int(date_raw.split('/')[1])
                    ).strftime('%Y-%m-%d')
                    data.append({
                        'date': date,
                        'month': row["Месяц"],
                        'rate': int(row["Процент"].strip('%'))
                    })
                line_number += 1
        return data

    def _read_griddata_csv_file(self):
        file_name = 'Пример XBI - 2.csv'
        print(f'Reading {file_name}')

        data = []
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_number = 0
            
            for row in csv_reader:
                if line_number > 0:
                    data.append({
                        'group': row["Группа"], # row["Дата"],
                        'number': row["Номер"],
                        'sending_city': row["Город отправки"],
                        'receiving_city': row["Город прибытия"],
                    })
                line_number += 1
        return data

    def _read_piechartdata_csv_file(self):
        file_name = 'Пример XBI - 3.csv'
        print(f'Reading {file_name}')
        
        data = []
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_number = 0
            
            for row in csv_reader:
                if line_number > 0:
                    data.append({
                        'group': row["Группа"],
                        'fraction': int(row["Доля"].strip('%')),
                    })
                line_number += 1
        return data

    def _create_graph_data(self):
        data = self._read_graphdata_csv_file()
        for item in data:
            graph_item = GraphData(**item)
            graph_item.save()

    def _create_grid_data(self):
        data = self._read_griddata_csv_file()
        for item in data:
            graph_item = GridData(**item)
            graph_item.save()

    def _create_piechart_data(self):
        data = self._read_piechartdata_csv_file()
        for item in data:
            graph_item = PieChartData(**item)
            graph_item.save()


    def handle(self, *args, **options):
        self._create_graph_data()
        self._create_grid_data()
        self._create_piechart_data()
