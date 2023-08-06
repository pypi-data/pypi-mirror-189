import requests, time, json, pickledb, threading, itertools, os, sys

print("""\x1B[33m
  _           _      _           _   
 | |_  ___ __| |_ __| |_  ___ __| |__
 | ' \/ _ (_-<  _/ _| ' \/ -_) _| / /
 |_||_\___/__/\__\__|_||_\___\__|_\_\\
                                     """)
print("\n\x1b[37m [>] Library name: hostcheck")
print("\x1b[37m [>] Developer: Misha Korzhik")
time.sleep(0.1)

class host:
    def http(id_key:str, show=False):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("website", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-http?host={id_key}", headers={"Accept": "application/json"}).text)
        if show == True:
            done = False
            def animate():
                for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
                    if done:
                        break
                    sys.stdout.write('\r\x1B[32mParsing data ' + c + '\x1B[37m\r')
                    sys.stdout.flush()
                    time.sleep(0.07)
                sys.stdout.write('\r')
            t = threading.Thread(target=animate)
            t.start()
            time.sleep(10)
            done = True
        elif show == False:
            time.sleep(10)
        host.result_http(id_key, show)
    def result_http(id_key, show):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.http_list(id_key, result_key, show)
    def http_list(id_key, result_key, show):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    if data_output[3] == None: data_output[3] = "None"
                    if data_output[3][0] == "2": data_output[3] = f"{data_output[3]}"
                    elif data_output[3][0] == "3": data_output[3] = f"{data_output[3]}"
                    elif data_output[3][0] == "4" or data_output[3][0] == "5":
                        data_output[2][0] = f"{data_output[2]}"
                        data_output[3][0] = f"{data_output[3]}"
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", data_output[2], f"{round(data_output[1], 2)}s.", data_output[3], data_output[4]
                    r.append(server_list)
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "Connect timeout", "0.00s.", "599", "unknown IP"
                r.append(server_list)
                db.set(server_list, data)
            except SystemExit:
                exit(1)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")
        if show == True:
            f = open("check-host.json")
            s = 0
            data = json.load(f)
            getnode = data["nodes"]
            for nodes in getnode:
                s = s + 1
                node = data[nodes]
                string = ' '.join([str(elem) for i,elem in enumerate(node)])
                string = string.replace("OK", "\x1B[1m\x1B[32mConnected\x1B[37m\x1B[0m")
                string = string.replace("Moved Permanently", "\x1B[1m\x1B[33mMoved Permanently\x1B[37m\x1B[0m")
                string = string.replace("Connect timeout", "\x1B[1m\x1B[31mConnect timeout\x1B[37m\x1B[0m")
                string = string.replace("Connection refused", "\x1B[1m\x1B[31mConnection refused\x1B[37m\x1B[0m")
                string = string.replace("No such device or address", "\x1B[1m\x1B[31mHost not found\x1B[37m\x1B[0m")
                string = string.replace("Connection timed out", "\x1B[1m\x1B[31mConnect timeout\x1B[37m\x1B[0m")
                string = string.replace("301", "301\x1B[34m")
                string = string.replace("200", "200\x1B[34m")
                string = string.replace("599", "301\x1B[34m")
                string = string.replace("None", "None\x1B[34m", )
                string = string.replace("null.", "null.\x1B[34m")
                string = string.replace("Austria", "\x1B[34mAustria")
                string = string.replace("Brazil", "\x1B[34mBrazil")
                string = string.replace("Bulgaria", "\x1B[34mBulgaria")
                string = string.replace("Czechia", "\x1B[34mCzechia")
                string = string.replace("Finland", "\x1B[34mFinland")
                string = string.replace("France", "\x1B[34mFrance")
                string = string.replace("Germany", "\x1B[34mGermany")
                string = string.replace("Hong Kong", "\x1B[34mHong Kong")
                string = string.replace("India", "\x1B[34mIndia")
                string = string.replace("Iran", "\x1B[34mIran")
                string = string.replace("Israel", "\x1B[34mIsrael")
                string = string.replace("Italy", "\x1B[34mItaly")
                string = string.replace("Kazakhstan", "\x1B[34mKazakhstan")
                string = string.replace("Lithuania", "\x1B[34mLithuania")
                string = string.replace("Moldova", "\x1B[34mMoldova")
                string = string.replace("Netherlands", "\x1B[34mNetherlands")
                string = string.replace("Poland", "\x1B[34mPoland")
                string = string.replace("Portugal", "\x1B[34mPortugal")
                string = string.replace("Russia", "\x1B[34mRussia")
                string = string.replace("Serbia", "\x1B[34mSerbia")
                string = string.replace("Switzerland", "\x1B[34mSwitzerland")
                string = string.replace("Thailand", "\x1B[34mThailand")
                string = string.replace("Turkey", "\x1B[34mTurkey")
                string = string.replace("UAE", "\x1B[34mUAE")
                string = string.replace("UK", "\x1B[34mUnited Kingdom")
                string = string.replace("Ukraine", "\x1B[34mUkraine")
                string = string.replace("USA", "\x1B[34mUnited States")
                print(string)
            print(f"\x1B[0mNumber of servers {s}")
            f.close()

    def ping(id_key:str, show=False):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("website", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-ping?host={id_key}", headers={"Accept": "application/json"}).text)
        if show == True:
            done = False
            def animate():
                for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
                    if done:
                        break
                    sys.stdout.write('\r\x1B[32mParsing data ' + c + '\x1B[37m\r')
                    sys.stdout.flush()
                    time.sleep(0.07)
                sys.stdout.write('\r')
            t = threading.Thread(target=animate)
            t.start()
            time.sleep(10)
            time.sleep(1)
            done = True
        elif show == False:
            time.sleep(10)
        host.result_ping(id_key, show)
    def result_ping(id_key, show):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.ping_list(id_key, result_key, show)
    def ping_list(id_key, result_key, show):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    if data_output[0] == None: raise SystemExit
                    if data_output[0][0] == "OK": data_output[0][0] = f"OK"
                    elif data_output[0][0] == "TIMEOUT": data_output[0][0] = f"TIMEOUT"
                    elif data_output[0][0] == "MALFORMED": data_output[0][0] = f"MALFORMED"
                    elif data_output[0][0] == "TRACEROUTE": data_output[0][0] = f"TRACEROUTE"
                    if data_output[1][0] == "OK": data_output[1][0] = f"OK"
                    elif data_output[1][0] == "TIMEOUT": data_output[1][0] = f"TIMEOUT"
                    elif data_output[1][0] == "MALFORMED": data_output[1][0] = f"MALFORMEE"
                    elif data_output[1][0] == "TRACEROUTE": data_output[1][0] = f"TRACEROUTE"
                    if data_output[2][0] == "OK": data_output[2][0] = f"OK"
                    elif data_output[2][0] == "TIMEOUT": data_output[2][0] = f"TIMEOUT"
                    elif data_output[2][0] == "MALFORMED": data_output[2][0] = f"MALFORMED"
                    elif data_output[2][0] == "TRACEROUTE": data_output[2][0] = f"TRACEROUTE"
                    if data_output[3][0] == "OK": data_output[3][0] = f"OK"
                    elif data_output[3][0] == "TIMEOUT": data_output[3][0] = f"TIMEOUT"
                    elif data_output[3][0] == "MALFORMED": data_output[3][0] = f"MALFORMED"
                    elif data_output[3][0] == "TRACEROUTE": data_output[3][0] = f"TRACEROUTE"
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", f"{data_output[0][0]}/{data_output[1][0]}/{data_output[2][0]}/{data_output[3][0]}", f"{round(data_output[0][1] * 1000, 1)}ms/{round(data_output[1][1] * 1000, 1)}ms/{round(data_output[2][1] * 1000, 1)}ms/{round(data_output[3][1] * 1000, 1)}ms.", data_output[0][2]
                    r.append(server_list)
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "TIMEOUT/TIMEOUT/TIMEOUT/TIMEOUT", "F/F/F/F.", "unknown IP"
                r.append(server_list)
                db.set(server_list, data)
            except SystemExit:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "ERROR/ERROR/ERROR/ERROR", "null/null/null/null.", "unknown IP"
                db.set(server_list, data)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")
        if show == True:
            f = open("check-host.json")
            s = 0
            data = json.load(f)
            getnode = data["nodes"]
            for nodes in getnode:
                s = s + 1
                node = data[nodes]
                string = ' '.join([str(elem) for i,elem in enumerate(node)])
                string = string.replace("OK", "\x1B[1m\x1B[32mOK\x1B[37m\x1B[0m")
                string = string.replace("TIMEOUT", "\x1B[1m\x1B[31mTIMEOUT\x1B[37m\x1B[0m")
                string = string.replace("ERROR", "\x1B[1m\x1B[31mERROR\x1B[37m\x1B[0m")
                string = string.replace("TRACEROUTE", "\x1B[1m\x1B[31mTRACEROUTE\x1B[37m\x1B[0m")
                string = string.replace("MALFORMED", "\x1B[1m\x1B[31mMALFORMED\x1B[37m\x1B[0m")
                string = string.replace("ms.", "ms.\x1B[34m")
                string = string.replace("F.", "F.\x1B[34m")
                string = string.replace("null.", "null.\x1B[34m")
                string = string.replace("Austria", "\x1B[34mAustria")
                string = string.replace("Brazil", "\x1B[34mBrazil")
                string = string.replace("Bulgaria", "\x1B[34mBulgaria")
                string = string.replace("Czechia", "\x1B[34mCzechia")
                string = string.replace("Finland", "\x1B[34mFinland")
                string = string.replace("France", "\x1B[34mFrance")
                string = string.replace("Germany", "\x1B[34mGermany")
                string = string.replace("Hong Kong", "\x1B[34mHong Kong")
                string = string.replace("India", "\x1B[34mIndia")
                string = string.replace("Iran", "\x1B[34mIran")
                string = string.replace("Israel", "\x1B[34mIsrael")
                string = string.replace("Italy", "\x1B[34mItaly")
                string = string.replace("Kazakhstan", "\x1B[34mKazakhstan")
                string = string.replace("Lithuania", "\x1B[34mLithuania")
                string = string.replace("Moldova", "\x1B[34mMoldova")
                string = string.replace("Netherlands", "\x1B[34mNetherlands")
                string = string.replace("Poland", "\x1B[34mPoland")
                string = string.replace("Portugal", "\x1B[34mPortugal")
                string = string.replace("Russia", "\x1B[34mRussia")
                string = string.replace("Serbia", "\x1B[34mSerbia")
                string = string.replace("Switzerland", "\x1B[34mSwitzerland")
                string = string.replace("Thailand", "\x1B[34mThailand")
                string = string.replace("Turkey", "\x1B[34mTurkey")
                string = string.replace("UAE", "\x1B[34mUAE")
                string = string.replace("UK", "\x1B[34mUnited Kingdom")
                string = string.replace("Ukraine", "\x1B[34mUkraine")
                string = string.replace("USA", "\x1B[34mUnited States")
                print(string)
            print(f"\x1B[0mNumber of servers {s}")
            f.close()

    def tcp(id_key:str, show=False):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("tcp", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-tcp?host={id_key}", headers={"Accept": "application/json"}).text)
        if show == True:
            done = False
            def animate():
                for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
                    if done:
                        break
                    sys.stdout.write('\r\x1B[32mParsing data ' + c + '\x1B[37m\r')
                    sys.stdout.flush()
                    time.sleep(0.07)
                sys.stdout.write('\r')
            t = threading.Thread(target=animate)
            t.start()
            time.sleep(7)
            done = True
        elif show == False:
            time.sleep(7)
        time.sleep(7)
        host.result_tcp(id_key, show)
    def result_tcp(id_key, show):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.tcp_list(id_key, result_key, show)
    def tcp_list(id_key, result_key, show):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", f"connected", f"{round(data_output['time'], 2)}s"
                    r.append(server_list)
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "timeout", "0.00s"
                r.append(server_list)
                db.set(server_list, data)
            except KeyError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", f"{data_output['error']}", "0.00s"
                db.set(server_list, data)
            except SystemExit:
                exit(1)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")
        if show == True:
            f = open("check-host.json")
            s = 0
            data = json.load(f)
            getnode = data["nodes"]
            for nodes in getnode:
                s = s + 1
                node = data[nodes]
                string = ' '.join([str(elem) for i,elem in enumerate(node)])
                string = string.replace("connected", "\x1B[1m\x1B[32mconnected\x1B[0m")
                string = string.replace("timeout", "\x1B[1m\x1B[31mtimeout\x1B[0m")
                string = string.replace("Austria", "\x1B[34mAustria")
                string = string.replace("Brazil", "\x1B[34mBrazil")
                string = string.replace("Bulgaria", "\x1B[34mBulgaria")
                string = string.replace("Czechia", "\x1B[34mCzechia")
                string = string.replace("Finland", "\x1B[34mFinland")
                string = string.replace("France", "\x1B[34mFrance")
                string = string.replace("Germany", "\x1B[34mGermany")
                string = string.replace("Hong Kong", "\x1B[34mHong Kong")
                string = string.replace("India", "\x1B[34mIndia")
                string = string.replace("Iran", "\x1B[34mIran")
                string = string.replace("Israel", "\x1B[34mIsrael")
                string = string.replace("Italy", "\x1B[34mItaly")
                string = string.replace("Kazakhstan", "\x1B[34mKazakhstan")
                string = string.replace("Lithuania", "\x1B[34mLithuania")
                string = string.replace("Moldova", "\x1B[34mMoldova")
                string = string.replace("Netherlands", "\x1B[34mNetherlands")
                string = string.replace("Poland", "\x1B[34mPoland")
                string = string.replace("Portugal", "\x1B[34mPortugal")
                string = string.replace("Russia", "\x1B[34mRussia")
                string = string.replace("Serbia", "\x1B[34mSerbia")
                string = string.replace("Switzerland", "\x1B[34mSwitzerland")
                string = string.replace("Thailand", "\x1B[34mThailand")
                string = string.replace("Turkey", "\x1B[34mTurkey")
                string = string.replace("UAE", "\x1B[34mUAE")
                string = string.replace("UK", "\x1B[34mUnited Kingdom")
                string = string.replace("Ukraine", "\x1B[34mUkraine")
                string = string.replace("USA", "\x1B[34mUnited States")
                print(string)
            print(f"\x1B[0mNumber of servers {s}")
            f.close()

    def dns(id_key:str, show=False):
        f = open("check-host.json", "w")
        f.write("{}")
        f.close()
        db = pickledb.load('check-host.json', False, False)
        db.set("dns", id_key)
        db.dump()
        id_key = json.loads(requests.get(f"https://check-host.net/check-dns?host={id_key}", headers={"Accept": "application/json"}).text)
        if show == True:
            print("error! show dns data is not supoorted")
            exit(1)
        elif show == False:
            time.sleep(7)
        host.result_dns(id_key, show)
    def result_dns(id_key, show):
        result_key = requests.get(f"https://check-host.net/check-result/{id_key['request_id']}").text
        host.dns_list(id_key, result_key, show)
    def dns_list(id_key, result_key, show):
        db = pickledb.load('check-host.json', False, False)
        r = []
        for server_list in json.loads(result_key):
            try:
                for data_output in json.loads(result_key)[server_list]:
                    a_record, aaaa_record = ", ".join(data_output["A"]), ", ".join(data_output["AAAA"])
                    if a_record == "": a_record = f"no A record"
                    if aaaa_record == "": aaaa_record = f"no AAAA record"
                    r.append(server_list)
                    data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", a_record, aaaa_record, time.strftime("%M m. %S s.", time.gmtime(data_output["TTL"]))
                    db.set(server_list, data)
            except TypeError:
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", "no A record", "no AAAA record", "00m. 00s",
                r.append(server_list)
                db.set(server_list, data)
            except KeyError:
                if data_output["PTR"] == []: data_output["PTR"] = [f"no A record"]
                data = f"{id_key['nodes'][server_list][1]}, {id_key['nodes'][server_list][2]}", data_output["PTR"][0], f"no AAAA record", time.strftime("%M m. %S s.", time.gmtime(data_output["TTL"]))
                db.set(server_list, data)
            except SystemExit:
                exit(1)
        db.set("nodes", r)
        db.dump()
        print("saved as: check-host.json")
