class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        st=[]
        def generate(op,cl):
            if op==cl==n:
                ans.append("".join(st))
                return
            if op<n:
                st.append("(")
                generate(op+1,cl)
                st.pop()
            if cl<op:
                st.append(")")
                generate(op,cl+1)
                st.pop()
        generate(0,0)
        return ans
