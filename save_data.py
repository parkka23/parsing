import csv

def write_to_csv(data):
    with open('data.csv','w') as file:
        columns=["название","описание","цена","картинка"]
        writer=csv.DictWriter(file, columns)
        writer.writeheader()
        for prod in data:
            writer.writerow({
                "название":prod['title'],
                "описание":prod['describtion'],
                "цена":prod['price'],
                "картинка":prod['image']
            })

        