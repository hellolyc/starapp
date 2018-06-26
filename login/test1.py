import re
def search_fun(m):
    pattern = re.compile(u'[\u4e00-\u9fa5]')#[\u4e00-\u9fa5]
    results = pattern.search(m.group(1))
    out = m.group(0)
    print out
    if results:
        f = m.group(1).replace(u"\\n","{nn}")
        fileout = "_" + str(m.start(0)) + "\t" + m.group(1).replace(u"\\n","{nn}")
        print fileout
line = u"obj.transform.FindChild(\"tiaojian\").GetComponent<UILabel>().text =  + string.Format(\"达到{0}级\n上一章激活{1}条回忆\" , _huiyi.level"
pattern = re.compile(u'"(.+?)"')#[\s\S]
results = pattern.sub(search_fun,line)

