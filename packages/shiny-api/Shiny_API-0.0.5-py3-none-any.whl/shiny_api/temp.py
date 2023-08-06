from bs4 import BeautifulSoup

TEST_JSON = '<img src="https://km.support.apple.com/kb/securedImage.jsp?configcode=JF88&size=240x240"><br /><br />Serial Number: GG7X2LZ6JF88<br />Model Desc: IPAD 6TH GEN CELL<br />Model Name: iPad (6th Generation) Wi-Fi + Cellular<br />Model Number: A1954<br />Model iD: iPad7,6<br />Capacity: 32GB<br />Color: Space Gray<br />Type: Wi-Fi<br />Year: 2018<br />Week: 29 (17.07 - 23.07)<br />'


def sickw_html_to_dict(html):
    soup = BeautifulSoup(html, "html.parser")
    return_dict = {}
    for line in soup.findAll("br"):
        br_next = line.nextSibling
        if br_next != line and br_next is not None:
            data = br_next.split(":")
            return_dict[data[0]] = data[1].strip()
            # return_list.append(br_next)

    return return_dict


[print(f"{key}:{value}") for key, value in sickw_html_to_dict(TEST_JSON).items()]
