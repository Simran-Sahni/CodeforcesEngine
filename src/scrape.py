from bs4 import BeautifulSoup
import requests

home = 'http://codeforces.com'
prefix = 'http://codeforces.com/contest/'
suffix = '?locale=en'
problems = []

def scrape(id):
    contest_url = prefix + str(id) + suffix
    base_page = requests.get(contest_url)

    data = base_page.text
    soup = BeautifulSoup(data, "lxml")

    pref = '/contest/' + str(id) + '/problem/'

    for link in soup.find_all('a'):
        now = link.get('href')

        if now.startswith(pref) and (len(now) - len(pref) <= 2):
            if now not in problems:
                problems.append(now)
                prob_link = home + now
                prob_data = requests.get(prob_link).text
                prob_now = BeautifulSoup(prob_data, "lxml").find("div", class_="ttypography").get_text()
                prob_tags = BeautifulSoup(prob_data, "lxml").findAll("span", class_="tag-box")
                string_set = {"limit per test", "secondsmemory", "megabytesinputstandard inputoutputstandard output"}
                for a_string in string_set:
                    prob_now = prob_now.replace(a_string, "")
                end = 'ExampleInput'
                end1 = 'ExamplesInput'
                ind = prob_now.find(end)
                prob_now = prob_now[:ind]
                ind = prob_now.find(end1)
                prob_now = prob_now[:ind]
                temp = ''
                for it in prob_tags:
                    temp = temp + it.get_text()
                final_str = prob_now + temp
                problem_alphabet = (now[-2] + now[-1]) if now[-1].isdigit() else now[-1]
                final_str = final_str.replace("\r\n", " ") 
                file_name = str(id) + '-' + problem_alphabet + '.txt'
                #print(file_name)
                f = open(file_name, "wb+")
                f.write(final_str.encode('utf8'))
                f.close()

for i in range(1, 1423):
    scrape(i)
