ts = 1655067600

for i in range(200):

    print("insert into `//home/yabs/stat/tmp/artyom-m/lf/" + str(ts) + "` with truncate")
    print("select * from $data where _logfeller_timestamp >= " + str(ts) + " and _logfeller_timestamp < " + str(ts + 1800) + ";")

    print("\n")

    ts += 1800
