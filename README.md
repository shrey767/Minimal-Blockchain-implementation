# Minimal-Blockchain-implementation
 The block structure consits of:
  1. pos: Index/position in the chain
  2. timestamp: Time of creation of block in seconds since beginning of the epoch (1/1/1970)
  3. data: Arbitary information in the block
  4. previous_block_hash: Hash of the previous block in the chain
  5. nonce: Proof of Work
  6. hash: Hash of the block (using SHA-256 on a combined string consisting of all the above parameters)

Validation Logic:
  Validation is done by using 2 checks:
  1. Realculating the hash of the current block using the previous block hash stored in the block and check if this newly calculated hash is same as the stored one.
  2. Checking if the actual previous block hash is same as the previous_block_hash variable stored in the current block.

  If either of these checks fail, the block as well as the chain is classified as invalid.

Finding Nonce/Proof of Work:
  1. The calculation of nonce is done by calculating a hash using timestamp, data and the nonce, then this nonce is incremented until a hash is found such that it starts with a specific number of zeroes.
  2. This nonce is called the proof of work because it makes blocks hard to fake, if a chain encounters two blocks at one (a fork) one with a valid nonce and the other invalid, it will use the block with the        valid nonce since it signifies that actual computational work was done to create this block and hence has better chance of being valid.
