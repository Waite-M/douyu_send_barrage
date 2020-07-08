from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client

from PIL import Image

import time


#加载配置项
class setOptions:
    options = Options()
    driver = ''
    def __init__(self,chrome_location):
        #指定浏览器路径
        self.options.binary_location = chrome_location

    #加载浏览器配置文件
    def loadChromeSetting(self,filesrc):
        link = r"--user-data-dir={}".format(filesrc)
        self.options.add_argument(link)

    #返回driver
    def reDriver(self,chromedriver_location=''):
        if chromedriver_location != '':
            self.driver = webdriver.Chrome(chromedriver_location, options=self.options)
            return self.driver
        else:
            self.driver = webdriver.Chrome(options=self.options)
            return self.driver


#发送弹幕
class sendMessage:
    #执行请求
    #设置浏览器
    def chromesetting(self,size = 'max',x='',y=''):
        if size == 'max':
            driver.maximize_window()
    def getRequest(self,url,driver):
        driver.get(url)
    def dragCaptcha(self):
        pass
    # #定位元素
    # def findElement(self,method='xpath',seletor):
    #     if method == 'xpath':
    #         driver.find_element_by_xpath(seletor)
    def sendit(self,string,driver,repeat):
        for i in range(repeat):
            str1 = string + str(i)
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="js-player-asideMain"]/div/div[2]/div/div[2]/div[2]/textarea').send_keys(str1)
            driver.find_element_by_xpath('//*[@id="js-player-asideMain"]/div/div[2]/div/div[2]/div[2]/div[2]').click()
            #斗鱼限制输入频率，每次输入间隔3s
            time.sleep(3)
        driver.quit()

# #第一版的验证方式，识别率不高，改用飞鹰接口
# class verify:
#     #获取图片
#     def getImg(self,driver,xpath ='',imgname = 'captcha.jpeg'):
#         img = r"D:/spider/captche/" + imgname
#         driver.find_element_by_xpath(xpath).get_screenshot_as_file(img)
#     #获取图片通过JS分别将缺口图和完整图显示出来
#     def setJS(self,driver,xpath = '',style = 'block;'):
#         element = driver.find_element_by_xpath(xpath)
#         driver.execute_script("arguments[0].style=arguments[1]",element,"display:{}".format(style))
#
#     #打开图片，计算图片的RGB差值从而获取对应像素点
#     def get_distance(self,captchaFull,captchaLess):
#         start = 44
#         # 遍历像素点横坐标
#         for i in range(distance, captchaFull.size[0]):
#             # 遍历像素点纵坐标
#             for j in range(captchaFull.size[1]):
#                 # 将坐标点的RGB进行比较
#                 if not self.is_rgb_equal(captchaFull, captchaLess, i, j):
#             # 返回此时横轴坐标就是滑块需要移动的距离
#                     return i
#     #遍历所有像素点，比较像素点的RGB差值 ，大于60认为不一致
#     def is_rgb_equal(self,captchaFull,captchaLess,x,y):
#         # 获取缺口图片的像素点(按照RGB格式)
#         bg_pixel = captchaLess.load()[x, y]
#         # 获取完整图片的像素点(按照RGB格式)
#         fullbg_pixel = captchaFull.load()[x, y]
#         # 设置一个判定值，像素值之差超过判定值则认为该像素不相同
#         threshold = 60
#         # 判断像素的各个颜色之差，abs()用于取绝对值
#         if (abs(bg_pixel[0] - fullbg_pixel[0] < threshold) and abs(bg_pixel[1] - fullbg_pixel[1] < threshold) and abs(
#                 bg_pixel[2] - fullbg_pixel[2] < threshold)):
#             # 如果差值在判断值之内，返回是相同像素
#             return True
#
#         else:
#             # 如果差值在判断值之外，返回不是相同像素
#             return False
#     #以像素点差点x坐标与移动块起始坐标作差，返回移动的距离
#     def dragmove(self,driver):
#         captchaFull = Image.open(r"D:/spider/captche/captchaFull.jpeg")
#         captchaLess = Image.open(r"D:/spider/captche/captchaLess.jpeg")
#         i = self.get_distance(captchaFull,captchaLess)
#         move_distance = i - 10
#         #获取需要移动的元素
#         source = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
#         action = ActionChains(driver)
#         # 鼠标左键按下不放
#         action.click_and_hold(source).perform()
#         # 平行移动大于解锁的长度的距离
#         action.drag_and_drop_by_offset(source, move_distance, 0).perform()
#         time.sleep(1)
#         action.release().perform()
#         print('登录成功')

class imgVerify:
    #登录
    def infoInput(self,driver,username,password):
        #点击 头像获取登录表单
        driver.find_element_by_xpath('//*[@id="js-header"]/div/div/div[3]/div[7]/div/div/a/span').click()
        #获取iframe框架,定位到框架内
        iframe = driver.find_element_by_xpath('//*[@id="login-passport-frame"]')
        driver.switch_to.frame(iframe)
        #点击密码方式登录
        driver.find_element_by_xpath('//*[@id="loginbox"]/div[2]/div[1]/div[1]').click()
        time.sleep(2)
        #先删除已存在的用户名和密码,在输入用户名密码然后点击登录
        nameInput = driver.find_element_by_xpath('//*[@id="loginbox"]/div[3]/div[2]/div[2]/form/div[1]/div/input')
        nameInput.click()
        nameInput.send_keys(Keys.CONTROL,'a')
        nameInput.send_keys(Keys.BACK_SPACE)
        nameInput.send_keys(username)

        passInput = driver.find_element_by_xpath('//*[@id="loginbox"]/div[3]/div[2]/div[2]/form/div[3]/input[1]')
        passInput.click()
        passInput.send_keys(Keys.CONTROL,'a')
        passInput.send_keys(Keys.BACK_SPACE)
        passInput.send_keys(password)
        #点击登录弹出验证
        driver.find_element_by_xpath('//*[@id="loginbox"]/div[3]/div[2]/div[2]/form/div[6]/input').click()
        print('用户名密码输入完成')
        time.sleep(2)
    #获取图片
    def getImg(self,driver):
        #判断验证类型，斗鱼使用超验的两种验证，一种滑动另一种是顺序点击
        #点击
        if self.isElementPresent(driver,'/html/body/div[4]/div[2]/div[6]/div/div/div[1]'):
            print(self.isElementPresent(driver,'/html/body/div[4]/div[2]/div[6]/div/div/div[1]'))
            self.img = r"D:/spider/captche/orderClick.png"
            # 需要截取的元素定位
            element  = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div')
            element.screenshot(self.img)
        #滑动：通过滑块元素判断为滑动验证类型
        if self.isElementPresent(driver,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_slider.geetest_ready > div.geetest_slider_button','css'):
            print(self.isElementPresent(driver,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_slider.geetest_ready > div.geetest_slider_button','css'))
            self.img = r"D:/spider/captche/ slidingBlock.png"
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]').get_screenshot_as_file(img)
    #返回坐标点
    def getCoordByChaoying(self,driver):
        self.getImg(driver)
        chaojiying = Chaojiying_Client('260631308', 'mengwei080305','4ba372176f5fbed6c385208ae49cd901')  # 用户中心>>软件ID 生成一个替换 96001
        im = open(self.img, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        if self.img == "D:/spider/captche/orderClick.png":
            dict = chaojiying.PostPic(im, 9004)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
            if dict['err_str'] =='OK':
                print(dict)
                return dict['pic_str']
        else:
            dict =chaojiying.PostPic(im, 9102)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
            print(dict)
            if dict['err_str'] =='OK':
                return dict['pic_str']
    #selenium 模拟拖动验证或顺序点击验证
    def verify(self,driver):
        #判断验证码类型
        coordlist = self.getCoordByChaoying(driver).split('|')
        #图片文字点击认证类型：根据返回的坐标依次点击
        if self.img == "D:/spider/captche/orderClick.png":
            source =driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div')
            for i in range(len(coordlist)):
                #依次获取坐标并点击
                x = int(coordlist[i].split(',')[0])
                y = int(coordlist[i].split(',')[1])
                ActionChains(driver).move_to_element_with_offset(source,x,y).click().perform()
                time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div/div[3]/a/div').click()
            print('登录成功')
            #返回主页面
            driver.switch_to.default_content()
        #滑块类型：获取滑块与缺口的坐标，计算x坐标差，移动
        if  self.img == "D:/spider/captche/slidingBlock.png":
            # 获取滑块
            source = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
            #计算滑动距离
            move_distance = coordlist[0].split(',')[0] - coordlist[1].split(',')[0]
            #移动
            action.drag_and_drop_by_offset(source, move_distance, 0).perform()
            time.sleep(1)
            action.release().perform()
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div/div[3]/a/div').click()
            print('验证完成登录成功')
        #判断元素是否存在
    def isElementPresent(self,driver,path,type='xpath'):
        try:
            if type == 'css':
                driver.find_element_by_css_selector(path)
            else:
                driver.find_element_by_xpath(path)
        except:
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True






setOptionsobj = setOptions(chrome_location = r'D:\Google\Chrome\Application\chrome.exe')
#加载浏览器配置
chromedata =  r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
setOptionsobj.loadChromeSetting(chromedata)
driver = setOptionsobj.reDriver()
sendMessageobj = sendMessage()
#斗鱼房间url
url = 'https://www.douyu.com/4246519'
#浏览器窗口最大
sendMessageobj.chromesetting()
sendMessageobj.getRequest(url,driver)
#执行显性等待
xpath = '//*[@id="js-player-asideMain"]/div/div[2]/div/div[2]/div[2]/textarea'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
imgVerifyobj = imgVerify()
#通过cookie判断是否已登录,未登录则进行登录验证
if 'acf_username' not in str(driver.get_cookies()):
    # 输入用户名密码
    imgVerifyobj.infoInput(driver, '18776276460', '13425720357')
    # 验证登录
    imgVerifyobj.verify(driver)
# #获取完整图片
# verifyobj.setJS(driver,'/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/canvas')
# verifyobj.getImg(driver,'/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]','captcheFull.jpeg')
# #获取缺图
# verifyobj.setJS(driver,'/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]','none')
# verifyobj.getImg(driver,'/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]','captcheLess.jpeg')
# 移动
# verifyobj.dragmove(driver)
#获取元素发送弹幕
sendMessageobj.sendit('23333',driver,3)

