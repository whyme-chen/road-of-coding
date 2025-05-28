import requests
import argparse
import sys

"""
Environment domain map.
"""
ENV_CONFIG = {
    "dev": "https://dev-app.axzo.cn",
    "test": "https://test-api.axzo.cn", 
    "pre": "https://pre-api.axzo.cn",
    "prod": "https://api.axzo.cn"
}


def get_sms_code(env, phone):
    """
    Get SMS verification code for the given phone number in the specified environment.
    
    Args:
        env (str): Environment URL from ENV_CONFIG (dev/test/pre/prod)
        phone (int): Phone number to receive SMS code
        
    Returns:
        dict: Response JSON containing SMS code information if successful
        None: If request fails
        
    Raises:
        requests.exceptions.RequestException: If HTTP request fails
    """
    url = f'{ENV_CONFIG[env]}/pudge/webApi/saas/sms/code'
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        'origin': f'https://{env + "-" if env != "prod" else ""}cms.axzo.cn',
        'ouid': '',
        'outype': '',
        'priority': 'u=1, i',
        'referer': f'https://{env + "-" if env != "prod" else ""}cms.axzo.cn/',
        'saastenantid': '',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'terminal': 'NT_CMS_WEB_GENERAL',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'workspaceid': ''
    }
    
    data = {
        "phone": phone
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        result = response.json()
        print(f"get_sms_code response: {result}")
        return result["data"]  # Return just the verification code
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def get_token_wiht_code(env, phone, sms_code, qr_code, terminal):
    """
    Get authentication token using SMS verification code.
    
    Args:
        env (str): Environment URL from ENV_CONFIG (dev/test/pre/prod)
        phone (int): Phone number used for verification
        sms_code (int): SMS verification code received
        qr_code (str): QR code string for authentication
        
    Returns:
        dict: Response JSON containing token information if successful
        None: If request fails
        
    Raises:
        requests.exceptions.RequestException: If HTTP request fails
    """
    url = f'{ENV_CONFIG[env]}/braum/webApi/saas/signIn/sms/v2'
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        'origin': f'https://{env + "-" if env != "prod" else ""}cms.axzo.cn',
        'ouid': '',
        'outype': '',
        'priority': 'u=1, i',
        'referer': f'https://{env + "-" if env != "prod" else ""}cms.axzo.cn',
        'saastenantid': '',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'terminal': terminal,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'workspaceid': ''
    }
    
    data = {
        "phone": phone,
        "smsCode": sms_code,
        "qrCode": qr_code
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        print(f"get_token response: {result}")
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Get Axzo token with SMS verification')
    parser.add_argument('--env', default='test', help='Environment (default: test)')
    parser.add_argument('--phone', type=int, default=17870574155, help='Phone number (default: 17870574155)')
    parser.add_argument('--terminal', default='NT_CMS_WEB_GENERAL', help='Terminal type (default: NT_CMS_WEB_GENERAL)')
    
    # Parse arguments
    args = parser.parse_args()
    
    env = args.env
    phone_number = args.phone
    terminal = args.terminal
    qr_code = ""
    
    sys.argv[1]
    
    sms_code = get_sms_code(env, phone_number)
    if sms_code is not None:
        token_result = get_token_wiht_code(env, phone_number, sms_code, qr_code, terminal)
        if token_result is not None:
            print(f'Successfully obtained token: Bearer "{token_result['data']['accessToken']}')
            # return "Bearer " + token_result["accessToken"]
        else:
            print("Failed to obtain token")
            # return None
    else:
        print("Failed to get SMS code")