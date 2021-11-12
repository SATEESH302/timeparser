
import sys
import functools


def reading_file(filepath):
    # This
    data=open(filepath).read()
    d=data.split('\n')
    return d


def extract_time(d):
    sa = []
    for te in d:
        if te == '' or '\xa0\xa0' in te:
            print(te)
        else:
            sa.append(te)
            # d.remove(te)
    d = sa

    k = 0
    timedict = []
    for i in d:
        if i == 'Time Log:':
            # print(i)
            pass
        else:

            tokens = d[k].lower().split(' ')
            # print(tokens)
            if '' in tokens:
                if tokens.count('') >= 2:
                    if "am" in d[k].lower() or "pm" in d[k].lower():
                        newtokes = []
                        for l in tokens:
                            if l == '' or l == '-':
                                pass
                            else:
                                newtokes.append(l)

                        timedict.append(' '.join(newtokes[0:2]))

            timespent = tokens[1] + ' ' + tokens[3]
            timedict.append(timespent)

        k = k + 1

    return timedict


def coverting_stand_time(timedict):
    new_clean = []
    for sysmbol in timedict:
        if '-' in sysmbol or "/" in sysmbol:
            pass
        else:
            new_clean.append(sysmbol)
    timedict = new_clean

    timegap = {}

    for timestamp in range(0, len(timedict)):
        timegaplist = []
        for time in timedict[timestamp].split(' '):
            # timegaplist=[]
            if "pm" in time:

                changetime = time.split(':')
                # print(changetime)
                t = changetime[0]
                # print(t)
                if int(t) != 12:

                    # print(int(changetime[0])+12)
                    changetime.remove(t)

                    changetime.insert(0, str(int(t) + 12))
                    timegaplist.append(int(':'.join(changetime).replace('pm', '').replace(':', '')))
                else:
                    changetime.remove(t)

                    changetime.insert(0, str(t))
                    timegaplist.append(int(':'.join(changetime).replace('pm', '').replace(':', '')))

            else:
                if time != '':
                    changetime = time.split(':')
                    # print(changetime)
                    t = changetime[0]
                    # print(t)
                    if int(t) != 12:
                        # print(int(changetime[0])+12)
                        changetime.remove(t)

                        changetime.insert(0, str(int(t)))
                        timegaplist.append(int(':'.join(changetime).replace('am', '').replace(':', '')))
                    else:
                        changetime.remove(t)

                        changetime.insert(0, str(24 - int(0)))
                        timegaplist.append(int(':'.join(changetime).replace('am', '').replace(':', '')))

        timegap[timedict[timestamp]] = timegaplist

    return timegap

def speding_time(timegap):
    total_time={}
    for min in timegap.keys():
        #print(min)
        if min!=None:
            x=timegap[min]

            if len(x)>0 :

                y=str(functools.reduce(lambda a,b:b-a,x))

                if len(y)>2:

                    total_time[min]=abs(int(y[:-2])*60+int(y[-2:]))

                else:
                    total_time[min]=abs(int(y))

            else:
                continue
    hours=str(round(sum(total_time.values())/60,2)).split('.')[0] + " hours"
    minutes=str(round(float("0."+str(round(sum(total_time.values())/60,2)).split('.')[-1])*60,0)).split('.')[0]+ ' Min'
    spendtime=hours+' '+minutes
    total_spent_time=spendtime
    return  total_spent_time




def main(file_path):
    data = reading_file(file_path)
    extract_time_data = extract_time(data)
    stand_time = coverting_stand_time(extract_time_data)
    time_spent = speding_time(stand_time)
    # print(time_spent)
    # print(file_path.lower().replace('timelog',''))
    print(file_path.lower().replace('timelog','').replace(".txt",'')+' '+time_spent)
    return time_spent


if __name__=="__main__":

    main(sys.argv[1])
