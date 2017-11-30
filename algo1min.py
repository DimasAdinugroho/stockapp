minuteprevous = timenow.minute #initiate

while loop
    timenow
    result = from url

    counter = 0 #for the firstdata

    if timenow.minute = minuteprevous
        if counter = 0
            itemtime.hour = timenow.hour
            itemtime.minute = timenow.minute
            itemtime.second = 0

            itemopen = result.last
            itemhigh = result.last
            itemlow = result.last
            itemclose = result.last

            itemvolume = result.vol

            itemask = result.ask
            itembid = result.bid
            counter += 1
        else
            if last > itemhigh
                #change data at the same minute
                itemhigh = result.last
            else if last < itemlow
                #change data at the same minute
                itemlow = result.last

            itemask = result.ask
            itembid = result.bid
        lastresult = result
    else
        #change data at the previous minute (row)
        itemclose = lastresult.last
        itemvolume = lastresult.vol - volpreviousminute

        #new minute
        create newrow
        itemtime.hour = timenow.hour
        itemtime.minute = timenow.minute
        itemtime.second = 0

        itemopen = result.last
        itemhigh = result.last
        itemlow = result.last
        itemclose = result.last

        itemvolume = result.vol

        itemask = result.ask
        itembid = result.bid
        minuteprevous = timenow.minute



