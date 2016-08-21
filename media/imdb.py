#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup

try:
	def get_movie_data(movie_name):
		movie_data = []
		url = 'http://www.imdb.com/find?ref_=nv_sr_fn&q='+movie_name+'&s=all'
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,'html.parser')
	
		for td in soup.findAll('td',{'class':'result_text'}):
    			href = td.find('a')['href']
    			movie_page = 'http://www.imdb.com'+href
   		 	break
	
		source_code = requests.get(movie_page)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,'html.parser')
		for title in soup.findAll('div',{'class':'title_wrapper'}):
			movie_data.append(title.find('h1').text.rstrip())
	
		for div in soup.findAll('div',{'class':'ratingValue'}):
			movie_data.append(float(div.text[:4]))
		genre = soup.findAll('span',{'class':'itemprop'})
		movie_data.append(genre[0].text)
		return movie_data
except:
	return none



