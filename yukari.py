# coding: utf-8
from line import LineClient
import win32clipboard

try:
    token = LineClient("","").authToken
    print token
    client = LineClient(authToken = token)
    
    #client = LineClient(authToken = "")
except:
  print "auth Failed"
  raise

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard() 
win32clipboard.SetClipboardText(u"Hello LINE Python!")
win32clipboard.CloseClipboard()

while True:
      op_list = []
      for op in client.longPoll():
         op_list.append(op)
 
      for op in op_list:
         sender   = op[0]
         receiver = op[1]
         message  = op[2]

         #print type(message.text)

         senderName = sender.name
         text = message.text
         senderNamep = sender.name.decode('utf-8')         
         if(isinstance(text,type(None)) == False):
             textp = message.text.decode('utf-8')

             print senderNamep + ":"
             print textp

             texts = senderName + "さんから" + text
             messa = unicode(texts,'utf-8')

             try:
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(messa)
                win32clipboard.CloseClipboard()
             except:
                print "clip failed"
                raise
         else:
            print senderNamep + ":message received failed"
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(unicode(senderName,'utf-8') + u"さんからのメッセージの受信に失敗しました。")
            win32clipboard.CloseClipboard()
