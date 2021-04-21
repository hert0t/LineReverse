from THttpClientLite import THttpClient
from thrift.protocol.TCompactProtocol import TCompactProtocol


headersPolling = {
    "X-Line-Application":"ANDROIDLITE	2.16.0	Android OS	7.1.2",
    "X-Line-Access":"",
    "User-Agent":"LLA/2.16.0 MI20",
    "x-lal":"en_US",
    "x-las":"F", ## BOOLEAN isBackground, with Value "F" // "B"
    "x-lam":"w", ## BOOLEAN isNetworkConnect, with Value "w" // "m"
    "x-lac": "51089", ## SIM CODE
    }
headersTalk = {
    "X-Line-Application":"ANDROIDLITE	2.16.0	Android OS	7.1.2",
    "X-Line-Access":"",
    "User-Agent":"LLA/2.16.0 MI20",
    "x-lal":"en_US",
    }

## DOIT URE SELf :D
#headersEnc = {
#    "X-Line-Application":"ANDROIDLITE	2.16.0	Android OS	7.1.2",
#    "X-Line-Access":"",
#    "User-Agent":"LLA/2.16.0 MI20",
#    "x-lal":"en_US",
#    "x-lpqs":"/P5", ## PATH QUERY
#    "X-LCS":"", ## ENCRIPTION DATA (x-lcs encrypt.java)
#    "X-LE":"", ## OPTIONAL CONDITION
#    "X-LE-ORG":"" ## LENGHT + URL FRAGMENT
#    }

transport = THttpClient("https://gxx.line.naver.jp/P4") ## MODIFIED THttpClient (x-lcr, x-ls)
transport.setCustomHeaders(headersPolling)
protocol = TCompactProtocol(transport)
poll = YourService.Client(protocol)

transport = THttpClient("https://gxx.line.naver.jp/S4") ## MODIFIED THttpClient (x-lcr, x-ls)
transport.setCustomHeaders(headersTalk)
protocol = TCompactProtocol(transport)
poll = YourService.Client(protocol)
