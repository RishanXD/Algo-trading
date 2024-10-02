def chartink_screening(params):
    import requests
    from bs4 import BeautifulSoup
    import json


    # Step 1: Make a GET request to fetch the initial page where the CSRF token is provided
    session=requests.Session()


    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    }

    get_url = "https://chartink.com/login"
    response=session.get(get_url,headers=headers)
    
    
    try:
        # Find the meta tag with the name attribute set to 'csrf-token'
        soup = BeautifulSoup(response.content, "html.parser")
        csrf_token = soup.find("meta", attrs={"name": "csrf-token"})["content"]
        cookies=session.cookies.get_dict()
        cookies["remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d"]='''eyJpdiI6InBjTG5KemNNMVB1bW9LeFp0OUtBUXc9PSIsInZhbHVlIjoiY3RSaDVvMUk0b1Q1NzByTndtQ0gzV1FGV1NXUXZYRTNhWm03dWZMY0RacWJjbDBqeHJCcWk4YkMwTFgxcG5XUXhmck9zTUJDZjdWQldZNm5Ka0xwQU1FbkdUbWgzNDRaNXl5Z3k3dVdPYitQUHlIQnN1MmRiRWh1ejlmY01OdjV2MGpYaWw3MFZHZlZad2Y2RFNYbjNjWkx5ZS9rQU1CSHdHWGZ5TW1xY2RWa3U4QmFPemtuV3VjTFhCcHE4ZGR1RlhVeENyN3JQOTU3OWRzSG1VVklmc0RQemkvN1hDVW1VL0lRdFJqSzJFWT0iLCJtYWMiOiIwYTkzZGQ0NWUxN2M4NmUwMTg1ODIzMzhjY2M5OWUzY2RmODIxOWM0NTQ5NjYwNjMwZTU1OGM0NzlmN2U1MDhhIiwidGFnIjoiIn0%3D'''

    except Exception as e:
        print(f"Chartink CSRF token error: {e} , resolving it with the alternate method")
        csrf_refresh=session.get("https://chartink.com/csrf-token/refresh",headers=headers)
        csrf_token=(eval(csrf_refresh.text))["token"]
        cookies=session.cookies.get_dict()
        cookies['remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d']= 'eyJpdiI6IkpESnVoTFlHc3p2QWpxaE1MMjF2d0E9PSIsInZhbHVlIjoiVkZ4emNDNC9sTlAxRkt3M3A0dnoyOFNvRVdOSUl4aHNRNzlrY3BrQ2FaS1Q4aVRpNEw5b3VXTlBpMWEyMnUzRzRYbDg3TmZXZ0pXaDJibDFCbkVwUVZyTTBIakwyZVk3bnJIcERWOXZUMytTUGx5QXZKa1J6bWViQmRyK1BzZmh6ZVdSbUVRb2pWK0pTdis2S216RFdvQXp3UGs2NDJSUjVmVGdIVW80TUN4L1Nqcm00bGs1ZUdSeGQvR0R3ZWRZTGN0R3JYMktjQzJqbDd1NFRobC9SS2tMK2VRQ20rQ1R5MjlqWWdTeFp0VT0iLCJtYWMiOiJmZjk1YWU2NjI4MDIyY2JiNzhlYTM5ZmM5NGFmYjEyNzNiMTI4OTQ2MzQxNTU1ZTllZGFlODU4YTA1N2NmYjQyIiwidGFnIjoiIn0%3D'



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
    response = session.post("https://chartink.com/screener/process", headers=headers, params=params, cookies=cookies)

    # Check if the response is successful
    if response.status_code == 200:
        response_dict = response.json()
  
    else:
        print(f"Request failed with status code {response.status_code}")


    stock=[]
    for i in response_dict["data"]:
        stock.append(i["nsecode"])
    stock.sort()
    return stock