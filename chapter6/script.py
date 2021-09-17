from chapter5.script import Script
from chapter5.op import op_hash160, op_checksig
from unittest import TestCase

import chapter5.op as op

z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d  # message
sec = bytes.fromhex('04887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34')
sig = bytes.fromhex('3045022000eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c022100c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab601')
script_pubkey = Script([sec, 0xac])
script_sig = Script([sig])
combined_script = script_sig + script_pubkey
print(combined_script.evaluate(z))

# lst1 = [1,2,3,4,5]
# print(lst1)
# lst2 = lst1[:1]
# print(lst2)
#
# stt = "abcde"
# print(stt[::-1])
# print(stt[1:])

# Exercise 3
# Create a ScriptSig that can unlock this ScriptPubKey. Note OP_MUL multiplies the top two elements of the stack.
# 767695935687
# 56 = OP_6
# 76 = OP_DUP
# 87 = OP_EQUAL
# 93 = OP_ADD
# 95 = OP_MUL

script_pubkey = Script([0x76, 0x76, 0x95, 0x93, 0x56, 0x87])  # op_dup, op_dup, op_mul, op_add, op_6, op_equal
script_sig = Script([0x52])  # 82 in Decimal
combined_script = script_sig + script_pubkey  # => 82 + op_dup, op_dup, op_mul, op_add, op_6, op_equal
# print(combined_script.evaluate(0))  # stack =>


# Exercise 4
# Figure out what this Script is doing:
# 6e879169a77ca787
# 69 = OP_VERIFY
# 6e = OP_2DUP
# 7c = OP_SWAP
# 87 = OP_EQUAL
# 91 = OP_NOT
# a7 = OP_SHA1
# Use the Script.parse method and look up what various opcodes do at https://en.bitcoin.it/wiki/Script

script_pubkey = Script([0x6e, 0x87, 0x91, 0x69, 0xa7, 0x7c, 0xa7, 0x87])
c1 = '255044462d312e330a25e2e3cfd30a0a0a312030206f626a0a3c3c2f576964746820\
32203020522f4865696768742033203020522f547970652034203020522f537562747970652035\
203020522f46696c7465722036203020522f436f6c6f7253706163652037203020522f4c656e67\
74682038203020522f42697473506572436f6d706f6e656e7420383e3e0a73747265616d0affd8\
fffe00245348412d3120697320646561642121212121852fec092339759c39b1a1c63c4c97e1ff\
fe017f46dc93a6b67e013b029aaa1db2560b45ca67d688c7f84b8c4c791fe02b3df614f86db169\
0901c56b45c1530afedfb76038e972722fe7ad728f0e4904e046c230570fe9d41398abe12ef5bc\
942be33542a4802d98b5d70f2a332ec37fac3514e74ddc0f2cc1a874cd0c78305a215664613097\
89606bd0bf3f98cda8044629a1'
c2 = '255044462d312e330a25e2e3cfd30a0a0a312030206f626a0a3c3c2f576964746820\
32203020522f4865696768742033203020522f547970652034203020522f537562747970652035\
203020522f46696c7465722036203020522f436f6c6f7253706163652037203020522f4c656e67\
74682038203020522f42697473506572436f6d706f6e656e7420383e3e0a73747265616d0affd8\
fffe00245348412d3120697320646561642121212121852fec092339759c39b1a1c63c4c97e1ff\
fe017346dc9166b67e118f029ab621b2560ff9ca67cca8c7f85ba84c79030c2b3de218f86db3a9\
0901d5df45c14f26fedfb3dc38e96ac22fe7bd728f0e45bce046d23c570feb141398bb552ef5a0\
a82be331fea48037b8b5d71f0e332edf93ac3500eb4ddc0decc1a864790c782c76215660dd3097\
91d06bd0af3f98cda4bc4629b1'
collision1 = bytes.fromhex(c1)
collision2 = bytes.fromhex(c2)
script_sig = Script([collision1, collision2])
combined_script = script_sig + script_pubkey
print(combined_script.evaluate(0))


class ChapterTest(TestCase):

    def test_apply(self):

        op.op_hash160 = op_hash160
        op.op_checksig = op_checksig
        op.OP_CODE_FUNCTIONS[0xa9] = op_hash160
        op.OP_CODE_FUNCTIONS[0xac] = op_checksig