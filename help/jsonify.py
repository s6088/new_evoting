import json

def jsonify_votedata(votedatalist):
    jsondict = {'voter_public_key':votedatalist[0],'data':votedatalist[1],'key':votedatalist[2]}
    #--this returns a string for the dictionary but converts the bytes data
    #--into string...so we need to convert it back when recieved on the
    #--other end of the peer....
    return json.dumps(jsondict)


if __name__=='__main__':
    print(jsonify_votedata(['pub1234', 'data', 'key']))
