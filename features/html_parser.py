import requests, bs4


def parse_count_commits(base_url, branch='master'):  # count the total number of up-to-date commits in "master"
    branch_page = f"{base_url}/tree/{branch}"
    html_page = requests.get(branch_page)
    while True:
        try:
            html_page.raise_for_status()
            break
        except Exception as exc:
            input(f'There was a problem while getting the web page: {exc}.\nPress Enter to retry\n>')
            continue

    soup = bs4.BeautifulSoup(html_page.text, features="html.parser")  # object with class "bs4" must be created
    element = soup.select('.commits > a:nth-child(1) > span:nth-child(2)')  # interested CSS selection
    text = element[0].getText()  # to get the text out of a list from html
    text = text.replace(" ", "")  # removed blank spaces...
    text = text.replace("\n", "")  # ...and new lines from this html element
    count = int(text.replace(",", ""))  # removes eventual comma and get integer version
    return text, count
