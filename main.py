from bs4 import BeautifulSoup
import re
import requests
import Sender_Bot.main as Bot
import time

url = 'https://www.santannapisa.it/it/avvisi'
t_del = 10
med_keywords = ['Medicina', 'medicina', 'Mediche', 'mediche']
med_num = 3 
agr_keywords = ['Agrarie', 'agrarire', 'Vegetali', 'vegetali', 'Biotecnologie', 'biotecnologie']
agr_num = 2

def get_articles():

	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text, 'lxml')
	articles = soup.find_all('p')

	return articles

def find_articles(articles, keywords):

	articles_found = []

	for article in articles:

		found = False
		article_text = str(article)

		for keyword in keywords:
			if keyword in article_text:
				found = True
		if (found):
			articles_found.append(article)

	return articles_found

def look_for_new_articles(articles, number):

	if (len(articles) > number):

		new_article = articles[0]
		msg = new_article.text
		link = new_article.find('a')['href']
		Bot.send_message(msg)
		Bot.send_message(link)

	return len(articles) > number

def check(keywords, number, delay):

	articles = get_articles()
	articles_found = find_articles(articles, keywords)
	if (look_for_new_articles(articles_found, number) == False):
		print("Article not found")
		print(keywords)
		time.sleep(delay)
		check(keywords, number, delay)






