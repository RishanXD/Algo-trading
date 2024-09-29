def chartink_screening(payload):
    import requests
    from bs4 import BeautifulSoup
    import json


    # Step 1: Make a GET request to fetch the initial page where the CSRF token is provided
    session=requests.Session()
    

    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    get_url = "https://chartink.com/screener/cash-segment-bb-blast-rsi-60-60-58-volume?src=wassup"


    response=session.get(get_url,headers=headers)
    
    
    try:
        # Find the meta tag with the name attribute set to 'csrf-token'
        soup = BeautifulSoup(response.content, "html.parser")
        csrf_token = soup.find("meta", attrs={"name": "csrf-token"})["content"]
        cookies=session.cookies.get_dict()

    except TypeError:
        csrf_refresh=session.get("https://chartink.com/csrf-token/refresh",headers=headers)
        csrf_token=(eval(csrf_refresh.text))["token"]
        cookies=session.cookies.get_dict()


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://chartink.com",
        "Referer": get_url,
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRF-Token":csrf_token , 
    }




    # Make the POST request to /screener/process
    response = session.post("https://chartink.com/screener/process", headers=headers, data=payload, cookies=cookies)

    # Check if the response is successful
    if response.status_code == 200:
        raw_response = response.content
        # Convert the bytes to string
        response_str = raw_response.decode('utf-8')

        # Convert the JSON string to a dictionary
        response_dict = json.loads(response_str)

    else:
        print(f"Request failed with status code {response.status_code}")
    stock=[]
    for i in response_dict["data"]:
        stock.append(i["nsecode"])
    stock.sort()
    return stock