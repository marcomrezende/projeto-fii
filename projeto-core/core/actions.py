from core import models
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


class AtivosDividendosAction:
    @staticmethod
    def create_or_update_ativos_e_dividendos():
        url = 'https://fiis.com.br/resumo/'
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', id='filter--result-table-resumo')
        tbody = table.find('tbody')
        rows = tbody.findAll('tr')
        for row in rows:
            models.AtivosDividendos.objects.update_or_create(
                ticket=row.find('a').get_text(),
                defaults=dict(
                    dividendo=float(row.findAll('td')[1].get_text())
                )
            )
