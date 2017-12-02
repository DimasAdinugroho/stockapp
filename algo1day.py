    timenow
    result = from url

    counter = 0  # for the firstdata

    if difference(timenow, endtrading)
        if counter = 0
            itemtime.day = timenow.day

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
                # change data at the same minute
                itemhigh = result.last
            else if last < itemlow
                # change data at the same minute
                itemlow = result.last

        itemask = result.ask
        itembid = result.bid
    else
        # change data at the previous minute (row)
        itemclose = result.last
        itemvolume = result.vol




