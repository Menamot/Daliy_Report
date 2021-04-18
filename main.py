# -*- coding: utf-8 -*-
import requests
import re
import time
import datetime
import base64
from urllib.parse import quote
from lxml import etree




class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://newsso.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE2MTA2NzIyMzUxNzQ2MzU1OTMsInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IldVSFdmcm50bldZSFpmelE1UXZYVUNWeSIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cHM6Ly9zZWxmcmVwb3J0LnNodS5lZHUuY24vTG9naW5TU08uYXNweD9SZXR1cm5Vcmw9JTJmRGVmYXVsdC5hc3B4Iiwic3RhdGUiOiIifQ==',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        }
        self.login_url = 'https://newsso.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE2MTA2NzIyMzUxNzQ2MzU1OTMsInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IldVSFdmcm50bldZSFpmelE1UXZYVUNWeSIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cHM6Ly9zZWxmcmVwb3J0LnNodS5lZHUuY24vTG9naW5TU08uYXNweD9SZXR1cm5Vcmw9JTJmRGVmYXVsdC5hc3B4Iiwic3RhdGUiOiIifQ=='
        self.post_url = 'https://selfreport.shu.edu.cn/DayReport.aspx'
        self.logined_url = 'https://selfreport.shu.edu.cn/Default.aspx'
        self.session = requests.Session()


def login(self, number, password):

    EVENTTARGET = 'p1$ctl00$btnSubmit'
    EVENTTARGET = quote(EVENTTARGET, 'utf-8')

    post_data = {
        'username': number,
        'password': password,
        'login_submit': ''
    }

    response = self.session.post(self.login_url, data=post_data, headers=self.headers)
    if response.status_code == 200:
        print(200)
    else:
        print(response.status_code)
    # 这里获取了每日一报的html源码
    response_self_report = self.session.get(self.post_url).text
    result_etree = etree.HTML(response_self_report)
    VIEWSTATE = quote(result_etree.xpath('//*[@id="__VIEWSTATE"]/@value')[0], 'utf-8')
    # VIEWSTATE = re.sub('/', '%2F', VIEWSTATE)
    # VIEWSTATE = re.sub('\+', '%2B', VIEWSTATE)
    # VIEWSTATE = re.sub('=', '%3D', VIEWSTATE)

    # VIEWSTATE = '__EVENTARGUMENT=&__VIEWSTATE=' + VIEWSTATE
    #print(VIEWSTATE)

    VIEWSTATEGENERATOR = result_etree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    #print(VIEWSTATEGENERATOR)

    TIME= time.strftime("%Y-%m-%d", time.localtime())
    TIME2 = time.strftime("%m月%d日", time.localtime())
    DayAgo = datetime.datetime.today() - datetime.timedelta(14)
    DayAgo = DayAgo.strftime("%m月%d日")

    F_STATE_origin = '''{"p1_BaoSRQ":{"Text":"%s"},"p1_DangQSTZK":{"F_Items":[["良好","良好（体温不高于37.3）",1],["不适","不适",1]],"SelectedValue":"良好"},"p1_ZhengZhuang":{"Hidden":true,"F_Items":[["感冒","感冒",1],["咳嗽","咳嗽",1],["发热","发热",1]],"SelectedValueArray":[]},"p1_QiuZZT":{"F_Items":[],"SelectedValueArray":[]},"p1_JiuYKN":{"F_Items":[],"SelectedValueArray":[]},"p1_JiuYYX":{"Required":false,"F_Items":[],"SelectedValueArray":[]},"p1_JiuYZD":{"F_Items":[],"SelectedValueArray":[]},"p1_JiuYZL":{"F_Items":[],"SelectedValueArray":[]},"p1_GuoNei":{"F_Items":[["国内","国内",1],["国外","国外",1]],"SelectedValue":"国内"},"p1_ddlGuoJia":{"DataTextField":"ZhongWen","DataValueField":"ZhongWen","F_Items":[["-1","选择国家",1,"",""],["阿尔巴尼亚","阿尔巴尼亚",1,"",""],["阿尔及利亚","阿尔及利亚",1,"",""],["阿富汗","阿富汗",1,"",""],["阿根廷","阿根廷",1,"",""],["阿拉伯联合酋长国","阿拉伯联合酋长国",1,"",""],["阿鲁巴","阿鲁巴",1,"",""],["阿曼","阿曼",1,"",""],["阿塞拜疆","阿塞拜疆",1,"",""],["埃及","埃及",1,"",""],["埃塞俄比亚","埃塞俄比亚",1,"",""],["爱尔兰","爱尔兰",1,"",""],["爱沙尼亚","爱沙尼亚",1,"",""],["安道尔","安道尔",1,"",""],["安哥拉","安哥拉",1,"",""],["安圭拉","安圭拉",1,"",""],["安提瓜和巴布达","安提瓜和巴布达",1,"",""],["奥地利","奥地利",1,"",""],["奥兰群岛","奥兰群岛",1,"",""],["澳大利亚","澳大利亚",1,"",""],["巴巴多斯","巴巴多斯",1,"",""],["巴布亚新几内亚","巴布亚新几内亚",1,"",""],["巴哈马","巴哈马",1,"",""],["巴基斯坦","巴基斯坦",1,"",""],["巴勒斯坦","巴勒斯坦",1,"",""],["巴林","巴林",1,"",""],["巴拿马","巴拿马",1,"",""],["巴西","巴西",1,"",""],["白俄罗斯","白俄罗斯",1,"",""],["百慕大","百慕大",1,"",""],["保加利亚","保加利亚",1,"",""],["贝宁","贝宁",1,"",""],["比利时","比利时",1,"",""],["冰岛","冰岛",1,"",""],["波多黎各","波多黎各",1,"",""],["波兰","波兰",1,"",""],["波斯尼亚和黑塞哥维那","波斯尼亚和黑塞哥维那",1,"",""],["玻利维亚","玻利维亚",1,"",""],["伯利兹","伯利兹",1,"",""],["博茨瓦纳","博茨瓦纳",1,"",""],["不丹","不丹",1,"",""],["布基纳法索","布基纳法索",1,"",""],["布隆迪","布隆迪",1,"",""],["布维岛","布维岛",1,"",""],["朝鲜","朝鲜",1,"",""],["赤道几内亚","赤道几内亚",1,"",""],["丹麦","丹麦",1,"",""],["德国","德国",1,"",""],["东帝汶","东帝汶",1,"",""],["东帝汶","东帝汶",1,"",""],["多哥","多哥",1,"",""],["多米尼加","多米尼加",1,"",""],["俄罗斯联邦","俄罗斯联邦",1,"",""],["厄瓜多尔","厄瓜多尔",1,"",""],["厄立特里亚","厄立特里亚",1,"",""],["法国","法国",1,"",""],["法国大都会","法国大都会",1,"",""],["法罗群岛","法罗群岛",1,"",""],["法属波利尼西亚","法属波利尼西亚",1,"",""],["法属圭亚那","法属圭亚那",1,"",""],["梵蒂冈","梵蒂冈",1,"",""],["菲律宾","菲律宾",1,"",""],["斐济","斐济",1,"",""],["芬兰","芬兰",1,"",""],["佛得角","佛得角",1,"",""],["冈比亚","冈比亚",1,"",""],["刚果","刚果",1,"",""],["刚果（金）","刚果（金）",1,"",""],["哥伦比亚","哥伦比亚",1,"",""],["哥斯达黎加","哥斯达黎加",1,"",""],["格林纳达","格林纳达",1,"",""],["格鲁吉亚","格鲁吉亚",1,"",""],["根西岛","根西岛",1,"",""],["古巴","古巴",1,"",""],["瓜德罗普岛","瓜德罗普岛",1,"",""],["关岛","关岛",1,"",""],["圭亚那","圭亚那",1,"",""],["哈萨克斯坦","哈萨克斯坦",1,"",""],["海地","海地",1,"",""],["韩国","韩国",1,"",""],["荷兰","荷兰",1,"",""],["黑山","黑山",1,"",""],["洪都拉斯","洪都拉斯",1,"",""],["基里巴斯","基里巴斯",1,"",""],["吉布提","吉布提",1,"",""],["吉尔吉斯斯坦","吉尔吉斯斯坦",1,"",""],["几内亚","几内亚",1,"",""],["几内亚比绍","几内亚比绍",1,"",""],["加拿大","加拿大",1,"",""],["加纳","加纳",1,"",""],["加蓬","加蓬",1,"",""],["柬埔寨","柬埔寨",1,"",""],["捷克","捷克",1,"",""],["津巴布韦","津巴布韦",1,"",""],["喀麦隆","喀麦隆",1,"",""],["卡塔尔","卡塔尔",1,"",""],["科科斯（基林）群岛","科科斯（基林）群岛",1,"",""],["科摩罗","科摩罗",1,"",""],["科特迪瓦","科特迪瓦",1,"",""],["科威特","科威特",1,"",""],["克罗地亚","克罗地亚",1,"",""],["肯尼亚","肯尼亚",1,"",""],["库克群岛","库克群岛",1,"",""],["拉脱维亚","拉脱维亚",1,"",""],["莱索托","莱索托",1,"",""],["老挝","老挝",1,"",""],["黎巴嫩","黎巴嫩",1,"",""],["立陶宛","立陶宛",1,"",""],["利比里亚","利比里亚",1,"",""],["利比亚","利比亚",1,"",""],["列支敦士登","列支敦士登",1,"",""],["留尼汪岛","留尼汪岛",1,"",""],["卢森堡","卢森堡",1,"",""],["卢旺达","卢旺达",1,"",""],["罗马尼亚","罗马尼亚",1,"",""],["马达加斯加","马达加斯加",1,"",""],["马恩岛","马恩岛",1,"",""],["马尔代夫","马尔代夫",1,"",""],["马耳他","马耳他",1,"",""],["马拉维","马拉维",1,"",""],["马来西亚","马来西亚",1,"",""],["马里","马里",1,"",""],["马其顿","马其顿",1,"",""],["马绍尔群岛","马绍尔群岛",1,"",""],["马提尼克岛","马提尼克岛",1,"",""],["马约特","马约特",1,"",""],["毛里求斯","毛里求斯",1,"",""],["毛里塔尼亚","毛里塔尼亚",1,"",""],["美国","美国",1,"",""],["美属萨摩亚","美属萨摩亚",1,"",""],["蒙古","蒙古",1,"",""],["蒙特塞拉特","蒙特塞拉特",1,"",""],["孟加拉","孟加拉",1,"",""],["秘鲁","秘鲁",1,"",""],["密克罗尼西亚","密克罗尼西亚",1,"",""],["缅甸","缅甸",1,"",""],["摩尔多瓦","摩尔多瓦",1,"",""],["摩洛哥","摩洛哥",1,"",""],["摩纳哥","摩纳哥",1,"",""],["莫桑比克","莫桑比克",1,"",""],["墨西哥","墨西哥",1,"",""],["纳米比亚","纳米比亚",1,"",""],["南非","南非",1,"",""],["南斯拉夫","南斯拉夫",1,"",""],["瑙鲁","瑙鲁",1,"",""],["尼泊尔","尼泊尔",1,"",""],["尼加拉瓜","尼加拉瓜",1,"",""],["尼日尔","尼日尔",1,"",""],["尼日利亚","尼日利亚",1,"",""],["纽埃","纽埃",1,"",""],["挪威","挪威",1,"",""],["诺福克岛","诺福克岛",1,"",""],["帕劳","帕劳",1,"",""],["皮特凯恩群岛","皮特凯恩群岛",1,"",""],["葡萄牙","葡萄牙",1,"",""],["日本","日本",1,"",""],["瑞典","瑞典",1,"",""],["瑞士","瑞士",1,"",""],["萨尔瓦多","萨尔瓦多",1,"",""],["萨摩亚","萨摩亚",1,"",""],["塞尔维亚","塞尔维亚",1,"",""],["塞拉利昂","塞拉利昂",1,"",""],["塞内加尔","塞内加尔",1,"",""],["塞浦路斯","塞浦路斯",1,"",""],["塞舌尔","塞舌尔",1,"",""],["沙特阿拉伯","沙特阿拉伯",1,"",""],["圣诞岛","圣诞岛",1,"",""],["圣多美和普林西比","圣多美和普林西比",1,"",""],["圣赫勒拿","圣赫勒拿",1,"",""],["圣基茨和尼维斯","圣基茨和尼维斯",1,"",""],["圣卢西亚","圣卢西亚",1,"",""],["圣马力诺","圣马力诺",1,"",""],["圣文森特和格林纳丁斯","圣文森特和格林纳丁斯",1,"",""],["斯里兰卡","斯里兰卡",1,"",""],["斯洛伐克","斯洛伐克",1,"",""],["斯洛文尼亚","斯洛文尼亚",1,"",""],["斯威士兰","斯威士兰",1,"",""],["苏丹","苏丹",1,"",""],["苏里南","苏里南",1,"",""],["所罗门群岛","所罗门群岛",1,"",""],["索马里","索马里",1,"",""],["塔吉克斯坦","塔吉克斯坦",1,"",""],["泰国","泰国",1,"",""],["坦桑尼亚","坦桑尼亚",1,"",""],["汤加","汤加",1,"",""],["特立尼达和多巴哥","特立尼达和多巴哥",1,"",""],["突尼斯","突尼斯",1,"",""],["图瓦卢","图瓦卢",1,"",""],["土耳其","土耳其",1,"",""],["土库曼斯坦","土库曼斯坦",1,"",""],["托克劳","托克劳",1,"",""],["瓦利斯群岛和富图纳群岛","瓦利斯群岛和富图纳群岛",1,"",""],["瓦努阿图","瓦努阿图",1,"",""],["危地马拉","危地马拉",1,"",""],["委内瑞拉","委内瑞拉",1,"",""],["文莱","文莱",1,"",""],["乌干达","乌干达",1,"",""],["乌克兰","乌克兰",1,"",""],["乌拉圭","乌拉圭",1,"",""],["乌兹别克斯坦","乌兹别克斯坦",1,"",""],["西班牙","西班牙",1,"",""],["西撒哈拉","西撒哈拉",1,"",""],["希腊","希腊",1,"",""],["新加坡","新加坡",1,"",""],["新喀里多尼亚","新喀里多尼亚",1,"",""],["新西兰","新西兰",1,"",""],["匈牙利","匈牙利",1,"",""],["叙利亚","叙利亚",1,"",""],["牙买加","牙买加",1,"",""],["亚美尼亚","亚美尼亚",1,"",""],["也门","也门",1,"",""],["伊拉克","伊拉克",1,"",""],["伊朗","伊朗",1,"",""],["以色列","以色列",1,"",""],["意大利","意大利",1,"",""],["印度","印度",1,"",""],["印度尼西亚","印度尼西亚",1,"",""],["英国","英国",1,"",""],["约旦","约旦",1,"",""],["越南","越南",1,"",""],["赞比亚","赞比亚",1,"",""],["泽西岛","泽西岛",1,"",""],["乍得","乍得",1,"",""],["直布罗陀","直布罗陀",1,"",""],["智利","智利",1,"",""],["中非","中非",1,"",""]],"SelectedValueArray":["-1"]},"p1_ShiFSH":{"Required":true,"Hidden":false,"SelectedValue":"是","F_Items":[["是","在上海",1],["否","不在上海",1]]},"p1_ShiFZX":{"Required":true,"Hidden":false,"SelectedValue":"是","F_Items":[["是","住校",1],["否","不住校",1]]},"p1_ddlSheng":{"Hidden":false,"F_Items":[["-1","选择省份",1,"",""],["北京","北京",1,"",""],["天津","天津",1,"",""],["上海","上海",1,"",""],["重庆","重庆",1,"",""],["河北","河北",1,"",""],["山西","山西",1,"",""],["辽宁","辽宁",1,"",""],["吉林","吉林",1,"",""],["黑龙江","黑龙江",1,"",""],["江苏","江苏",1,"",""],["浙江","浙江",1,"",""],["安徽","安徽",1,"",""],["福建","福建",1,"",""],["江西","江西",1,"",""],["山东","山东",1,"",""],["河南","河南",1,"",""],["湖北","湖北",1,"",""],["湖南","湖南",1,"",""],["广东","广东",1,"",""],["海南","海南",1,"",""],["四川","四川",1,"",""],["贵州","贵州",1,"",""],["云南","云南",1,"",""],["陕西","陕西",1,"",""],["甘肃","甘肃",1,"",""],["青海","青海",1,"",""],["内蒙古","内蒙古",1,"",""],["广西","广西",1,"",""],["西藏","西藏",1,"",""],["宁夏","宁夏",1,"",""],["新疆","新疆",1,"",""],["香港","香港",1,"",""],["澳门","澳门",1,"",""],["台湾","台湾",1,"",""]],"SelectedValueArray":["上海"]},"p1_ddlShi":{"Hidden":false,"Enabled":true,"F_Items":[["-1","选择市",1,"",""],["上海市","上海市",1,"",""]],"SelectedValueArray":["上海市"]},"p1_ddlXian":{"Hidden":false,"Enabled":true,"F_Items":[["-1","选择县区",1,"",""],["黄浦区","黄浦区",1,"",""],["卢湾区","卢湾区",1,"",""],["徐汇区","徐汇区",1,"",""],["长宁区","长宁区",1,"",""],["静安区","静安区",1,"",""],["普陀区","普陀区",1,"",""],["虹口区","虹口区",1,"",""],["杨浦区","杨浦区",1,"",""],["宝山区","宝山区",1,"",""],["闵行区","闵行区",1,"",""],["嘉定区","嘉定区",1,"",""],["松江区","松江区",1,"",""],["金山区","金山区",1,"",""],["青浦区","青浦区",1,"",""],["奉贤区","奉贤区",1,"",""],["浦东新区","浦东新区",1,"",""],["崇明区","崇明区",1,"",""]],"SelectedValueArray":["宝山区"]},"p1_XiangXDZ":{"Hidden":false,"Label":"国内详细地址（省市区县无需重复填写）","Text":"南区十一622"},"p1_ShiFZJ":{"Required":true,"Hidden":false,"F_Items":[["是","家庭地址",1],["否","不是家庭地址",1]],"SelectedValue":null},"p1_ContentPanel1":{"Hidden":true,"IFrameAttributes":{}},"p1_FengXDQDL":{"Label":"%s至%s是否在<span style='color:red;'>中高风险地区</span>逗留","SelectedValue":"否","F_Items":[["是","是",1],["否","否",1]]},"p1_TongZWDLH":{"Required":true,"Label":"上海同住人员是否有%s至%s来自<span style='color:red;'>中高风险地区</span>的人","SelectedValue":"否","F_Items":[["是","是",1],["否","否",1]]},"p1_CengFWH":{"Label":"%s至%s是否在<span style='color:red;'>中高风险地区</span>逗留过","F_Items":[["是","是",1],["否","否",1]],"SelectedValue":"否"},"p1_CengFWH_RiQi":{"Hidden":true},"p1_CengFWH_BeiZhu":{"Hidden":true},"p1_JieChu":{"Label":"%s至%s是否与来自<span style='color:red;'>中高风险地区</span>发热人员密切接触","SelectedValue":"否","F_Items":[["是","是",1],["否","否",1]]},"p1_JieChu_RiQi":{"Hidden":true},"p1_JieChu_BeiZhu":{"Hidden":true},"p1_TuJWH":{"Label":"%s至%s是否乘坐公共交通途径<span style='color:red;'>中高风险地区</span>","SelectedValue":"否","F_Items":[["是","是",1],["否","否",1]]},"p1_TuJWH_RiQi":{"Hidden":true},"p1_TuJWH_BeiZhu":{"Hidden":true},"p1_QueZHZJC":{"F_Items":[["是","是",1,"",""],["否","否",1,"",""]],"SelectedValueArray":["否"]},"p1_DangRGL":{"SelectedValue":"否","F_Items":[["是","是",1],["否","否",1]]},"p1_GeLSM":{"Hidden":true,"IFrameAttributes":{}},"p1_GeLFS":{"Required":false,"Hidden":true,"F_Items":[["居家隔离","居家隔离",1],["集中隔离","集中隔离",1]],"SelectedValue":null},"p1_GeLDZ":{"Hidden":true},"p1_FanXRQ":{"Hidden":true,"Text":"2020-07-19"},"p1_WeiFHYY":{"Hidden":true},"p1_ShangHJZD":{"Hidden":true},"p1_DaoXQLYGJ":{"Text":"无"},"p1_DaoXQLYCS":{"Text":"广州"},"p1_JiaRen":{"Label":"%s至%s家人是否有发热等症状"},"p1_JiaRen_BeiZhu":{"Hidden":true},"p1_SuiSM":{"Required":true,"SelectedValue":"绿色","F_Items":[["红色","红色",1],["黄色","黄色",1],["绿色","绿色",1]]},"p1_LvMa14Days":{"Required":true,"SelectedValue":"是","F_Items":[["是","是",1],["否","否",1]]},"p1_ctl00_btnReturn":{"OnClientClick":"document.location.href='/Default.aspx';return;"},"p1":{"Title":"陈文龙（18124723）的每日一报","IFrameAttributes":{}}}''' % (TIME, DayAgo, TIME2, DayAgo, TIME2, DayAgo, TIME2, DayAgo, TIME2, DayAgo, TIME2, DayAgo, TIME2)
    F_STATE = quote(str(base64.b64encode(F_STATE_origin.encode('utf-8')),'utf-8'), 'utf-8')
    data = {
        '__EVENTTARGET': EVENTTARGET,
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': VIEWSTATE,
        '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
        'p1%24ChengNuo': 'p1_ChengNuo',
        'p1%24BaoSRQ': TIME,
        'p1%24DangQSTZK': '%E8%89%AF%E5%A5%BD',
        'p1%24ChengNuo': 'p1_ChengNuo',
        'p1%24BaoSRQ': '2021-03-27',
        'p1%24DangQSTZK': '%E8%89%AF%E5%A5%BD',
        'p1%24TiWen': '',
        'p1%24JiuYe_ShouJHM':'',
        'p1%24JiuYe_Email':'',
        'p1%24JiuYe_Wechat':'',
        'p1%24QiuZZT':'',
        'p1%24JiuYKN':'',
        'p1%24JiuYSJ':'',
        'p1%24GuoNei':'%E5%9B%BD%E5%86%85',
        'p1%24ddlGuoJia%24Value': '-1',
        'p1%24ddlGuoJia':'%E9%80%89%E6%8B%A9%E5%9B%BD%E5%AE%B6',
        'p1%24ShiFSH':'%E6%98%AF',
        'p1%24ShiFZX':'%E6%98%AF',
        'p1%24ddlSheng%24Value':'%E4%B8%8A%E6%B5%B7',
        'p1%24ddlSheng':'%E4%B8%8A%E6%B5%B7',
        'p1%24ddlShi%24Value':'%E4%B8%8A%E6%B5%B7%E5%B8%82',
        'p1%24ddlShi':'%E4%B8%8A%E6%B5%B7%E5%B8%82',
        'p1%24ddlXian%24Value':'%E5%AE%9D%E5%B1%B1%E5%8C%BA',
        'p1%24ddlXian':'%E5%AE%9D%E5%B1%B1%E5%8C%BA',
        'p1%24XiangXDZ':'%E5%8D%97%E5%8C%BA%E5%8D%81%E4%B8%80622',
        'p1%24ShiFZJ':'%E5%90%A6',
        'p1%24FengXDQDL':'%E5%90%A6',
        'p1%24TongZWDLH':'%E5%90%A6',
        'p1%24CengFWH':'%E5%90%A6',
        'p1%24CengFWH_RiQi':'p1%24CengFWH_BeiZhu:p1%24JieChu:%E5%90%A6',
        'p1%24JieChu_RiQi':'',
        'p1%24JieChu_BeiZhu':'',
        'p1%24TuJWH':'%E5%90%A6',
        'p1%24TuJWH_RiQi':'',
        'p1%24TuJWH_BeiZhu':'',
        'p1%24QueZHZJC%24Value':'%E5%90%A6',
        'p1%24QueZHZJC':'%E5%90%A6',
        'p1%24DangRGL':'%E5%90%A6',
        'p1%24GeLDZ':'',
        'p1%24FanXRQ': '2020-07-19',
        'p1%24WeiFHYY':'',
        'p1%24ShangHJZD':'',
        'p1%24DaoXQLYGJ':'%E6%97%A0',
        'p1%24DaoXQLYCS':'%E5%B9%BF%E5%B7%9E',
        'p1%24JiaRen_BeiZhu':'',
        'p1%24SuiSM':'%E7%BB%BF%E8%89%B2',
        'p1%24LvMa14Days':'%E6%98%AF',
        'p1%24Address2':'',
        'F_TARGET': 'p1_ctl00_btnSubmit',
        'p1_ContentPanel1_Collapsed': 'true',
        'p1_GeLSM_Collapsed': 'false',
        'p1_Collapsed': 'false',
        'F_STATE': 'F_STATE'
    }
    print(data)
    hsdd={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    self.session.post(self.post_url, data=data, headers=hsdd)




init = Login()
login(init, number='学号', password='密码')


