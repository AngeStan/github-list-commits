import requests, bs4


# the following block of code is to count the total number of up-to-date commits in "master"
def parse_count_commits(base_url, branch='master'):
    master_url = f"{base_url}/tree/{branch}"  # generation of the branch page url
    html_page = requests.get(master_url)
    soup = bs4.BeautifulSoup(html_page.text, features="html.parser")
    box = soup.select('.commits > a:nth-child(1) > span:nth-child(2)')  # interested CSS selection
    text = box[0].getText()
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    count = int(text.replace(",", ""))
    return text, count
