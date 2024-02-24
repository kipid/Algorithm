class Solution:
    def intToRoman(self, num: int) -> str:
        dict_ = {
            "0":"", "1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX",
            "00":"", "10":"X", "20":"XX", "30":"XXX", "40":"XL", "50":"L", "60":"LX", "70":"LXX", "80":"LXXX", "90":"XC",
            "000":"", "100":"C", "200":"CC", "300":"CCC", "400":"CD", "500":"D", "600":"DC", "700":"DCC", "800":"DCCC", "900":"CM",
            "0000":"", "1000":"M", "2000":"MM", "3000":"MMM"
        }
        s = ""
        for i, letter in enumerate(str(num)[::-1]):
            s = dict_[letter + "0"*i] + s
        return s