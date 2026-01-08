class SplitWiseSummary:

    def solution(self,summary):
        avg = round(sum(summary.values())/len(summary),2)
        split = {k : avg - v for k, v in summary.items()}
        print(split)


split_instance = SplitWiseSummary()

payment_summary = {
    "hari":1200,
    "vipin":1400,
    "john":1000,
    "vishnu":0,
    "tom":120,
    "avinash":0,
    "jinu":0,
    "asok":0
}
split_instance.solution(payment_summary)
