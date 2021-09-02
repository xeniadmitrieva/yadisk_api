import client_Helper
import config


def GetRequestTest():
    url = config.myUrl + '?path=%2Ftest'
    result = client_Helper.SendRequest('GET', url, config.head, 'GetRequestTest')
    client_Helper.ExistingFileName(result, '1.png', 'GetRequestTest')
    print("GetRequestTest -> SUCCESS")


def PostUploadFileTest():
    path = client_Helper.randomString()
    url = config.myUrl + '/upload?path=' + path + '&url=' + config.urlLogo + '&disable_redirects=false'
    client_Helper.SendRequest('POST', url, config.head, 'PostUploadFileTest', 202)
    print("PostUploadFileTest -> SUCCESS")


def PostAndCheckingFileTest():
    fileName = client_Helper.randomString(9)
    url = config.myUrl + '/upload?path=' + fileName + '&url=' + config.urlLogo + '%2F2x%2Fgooglelogo_color_272x92dp.png''&disable_redirects=false'
    client_Helper.SendRequest('POST', url, config.head, 'PostUploadFileTest', 202)
    import time
    time.sleep(3)
    # проверка загрузки файла
    url = config.myUrl + '?path=%2F'
    result = client_Helper.SendRequest('GET', url, config.head, 'PostAndCheckingFileTest')
    client_Helper.ExistingFileName(result, fileName, 'PostAndCheckingFileTest')
    print("PostAndCheckingFileTest -> SUCCESS")


def CreateFolder():
    folderName = client_Helper.randomString()
    url = config.myUrl + '?path=' + str(folderName)
    client_Helper.SendRequest('PUT', url, config.head, 'CreateFolder', 201)
    return folderName


def DeleteFolderTest():
    folder = CreateFolder()
    client_Helper.SendRequest('DELETE', config.myUrl + '?path=' + folder, config.head, "DeleteFolderTest", 204)
    print("DeleteFolderTest -> SUCCESS")


GetRequestTest()
PostUploadFileTest()
DeleteFolderTest()
PostAndCheckingFileTest()
