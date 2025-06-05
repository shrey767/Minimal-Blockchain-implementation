import hashlib
import time

class Block():
    def __init__(self,pos,data,previous_block_hash):
        self.index=pos                                            #position in the chain
        self.timestamp=str(time.time())                           #string of time when block is created
        self.data=data                                            #payload in block (assumed string)
        self.previous_block_hash=previous_block_hash              #hash of the previous block
        self.nonce=self.find_nonce()                              #proof of work
        self.hash=self.calculate_hash()
        
    def find_nonce(self):
        leading_zeroes=2
        nonce=0
        prefix=self.data+self.timestamp
        req='0'*leading_zeroes
        while 1:
            inp=prefix+str(nonce)
            res=hashlib.sha256(inp.encode()).hexdigest()
            if res.startswith(req):
                return nonce
            else:
                nonce+=1

    def calculate_hash(self):
        hashinput=" ".join([str(self.index),self.timestamp,self.data,self.previous_block_hash,str(self.nonce)])      #input of hashing function
        return hashlib.sha256(hashinput.encode()).hexdigest()
        


class BlockChain():
    def __init__(self):
        self.chain=[]

    def add_block(self,data):
        if not self.chain:
            block=Block(0,data,'0')        #create block, since there isn't a previous block, prev_block_hash is set to 0
            self.chain.append(block)       #append block
        else:
            prev_block=self.chain[-1]                                   #get newest block in chain
            new_block=Block(len(self.chain),data,prev_block.hash)       #create new block using hash of previous block
            self.chain.append(new_block)                                #append block

    def is_valid(self):
        all_valid=True
        for i in range(len(self.chain)):
            block=self.chain[i]
            actual_hash=block.calculate_hash()                          #calculate hash with updated values (if any)
            check1=(block.hash==actual_hash)                            #compare actual hash with stored hash
            if i==0:
                check2=True                                             #since there is no previous block
            else:
                if block.previous_block_hash==self.chain[i-1].hash:
                    check2=True
                else:
                    check2=False

            if check1 and check2:
                continue
            else:
                if all_valid:
                    print("Following block(s) are invalid:")
                    all_valid=False
                print(f"Block {i} is invalid")
        if all_valid:
            print("All blocks are valid")


