import psycopg2
from main import *

class Broadway:
    def __init__(self, url):
        self.html = BeautifulSoup(requests.get(url).text, 'lxml')
        self.connect = psycopg2.connect(dbname='postgres',
                                        user='izatturganaliev',
                                        host='localhost',
                                        password='password')

        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("create table if not exists broadway("
                            "id serial primary key, "
                            "name varchar(255));")
        self.connect.commit()
        self.cursor.execute("create table if not exists movies("
                            "id serial primary key, "
                            "name varchar(255),"
                            "price float ,"
                            "hall varchar(255),"
                            "time varchar(255),"
                            "broadway_id int,"
                            "constraint fk_broadway foreign key(broadway_id)"
                            "references broadway(id));")

        self.connect.commit()

    def save_broadway(self):
        self.cursor.execute("insert into broadway(name) "
                            "values('%s');" % 'Broadway')
        self.connect.commit()

    def save_movies(self):
        section = self.html.find('body').find_all('section')
        uls = section[1].find('div', class_='nano-content').find_all('ul')
        for i in uls:
            self.cursor.execute("insert into movies(time, name, price, hall, broadway_id) "
                                "values('%s','%s','%s','%s','%s');"
                                % (i.find_all('li')[0].text,
                                   i.find_all('li')[1].text,
                                   i.find_all('li')[2].text.strip(' с'),
                                   i.find_all('li')[3].text,
                                   1))
            self.connect.commit()

    def get_movies(self):
        self.cursor.execute("select * from movies;")
        self.connect.commit()
        for i in (self.cursor.fetchall()):
            print(i)

broadway = Broadway('https://broadway.kg/reserve/')
# broadway.create_table()
# broadway.save_broadway()
# broadway.save_movies()
broadway.get_movies()