import csv


class CsvRepository(object):
    @staticmethod
    def get_data(path: str) -> list:
        data = []
        with open(path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                data.append(row)

        return data

    @staticmethod
    def get_first_data_by_name_and_artist(path: str,
                                          name: str,
                                          artist: str) -> list:
        data = []
        with open(path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                if row[0] == name and row[1] == artist:
                    data = row
                    return data
        return []

    @staticmethod
    def get_header(path: str) -> list:
        with open(path, 'r', newline='') as csvfile:
            csv_dict_reader = csv.DictReader(csvfile)
            header = csv_dict_reader.fieldnames

        return header

    @staticmethod
    def get_header_and_data(path: str) -> list:
        data = []
        with open(path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            for row in csv_reader:
                data.append(row)

        return header, data

    @staticmethod
    def add_columns(path: str, columns: list) -> None:
        print('[INFO] - Add header on CSV')
        with open(path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()

        return

    @staticmethod
    def add(path: str, columns: list, data: list) -> None:
        with open(path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            for d in data:
                writer.writerow(d)
                # should be logging
                # print(f"[ADD]: {d}")

        return
